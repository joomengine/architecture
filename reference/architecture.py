"""Executable mechanisms for the JCB architectural white paper.

These small, deterministic models expose the contracts discussed in the paper.
They do not invoke Joomla, execute imported code, or reproduce every emitter.
SPDX-License-Identifier: MIT
"""
from __future__ import annotations

from collections import deque
from collections.abc import Callable, Mapping, Sequence
from copy import deepcopy
from dataclasses import dataclass, field
import re
from typing import Any


@dataclass(frozen=True, order=True)
class EntityKey:
    """Portable identity: entity type, identifying field, and value."""

    entity: str
    key: str
    value: str

    def __post_init__(self) -> None:
        for name in ("entity", "key", "value"):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a nonempty normalized string")
            if value != value.strip():
                raise ValueError(f"{name} contains surrounding whitespace")


@dataclass(frozen=True)
class Definition:
    identity: EntityKey
    properties: Mapping[str, Any]
    dependencies: tuple[EntityKey, ...] = ()


@dataclass(frozen=True)
class Repository:
    """An index hit may have an invalid payload, represented here by None."""

    name: str
    index: Mapping[EntityKey, Definition | None]


@dataclass
class Resolution:
    attempted: list[EntityKey] = field(default_factory=list)
    resolved: dict[EntityKey, Definition] = field(default_factory=dict)
    failures: dict[EntityKey, str] = field(default_factory=dict)
    origins: dict[EntityKey, str] = field(default_factory=dict)

    @property
    def successful(self) -> bool:
        """All attempted requests resolved; not a certificate of undeclared edges."""
        return not self.failures and len(self.resolved) == len(self.attempted)


def resolve_graph(
    roots: Sequence[EntityKey],
    local: Mapping[EntityKey, Definition],
    repositories: Sequence[Repository],
    *,
    inspect_local_dependencies: bool = False,
) -> tuple[Resolution, dict[EntityKey, Definition]]:
    """Resolve a finite in-memory graph using local-first, first-index selection.

    A selected bad remote payload fails that request rather than silently falling
    through to a later repository. By default, local hits are retained without
    traversing their dependencies: their completeness is a separate premise.
    Inputs are copied so this demonstration does not mutate its caller's records.
    """
    database = deepcopy(dict(local))
    pending = deque(roots)
    visited: set[EntityKey] = set()
    result = Resolution()
    while pending:
        request = pending.popleft()
        if not isinstance(request, EntityKey):
            raise TypeError("Requests must be EntityKey objects")
        if request in visited:
            continue
        visited.add(request)
        result.attempted.append(request)
        if request in database:
            definition = database[request]
            if not isinstance(definition, Definition) or definition.identity != request:
                result.failures[request] = "Invalid local identity or record"
                continue
            result.resolved[request] = definition
            result.origins[request] = "local"
            if inspect_local_dependencies:
                pending.extend(definition.dependencies)
            continue
        selected = next((repo for repo in repositories if request in repo.index), None)
        if selected is None:
            result.failures[request] = "No configured index contains the request"
            continue
        payload = selected.index[request]
        if not isinstance(payload, Definition) or payload.identity != request:
            result.failures[request] = f"Invalid selected payload in {selected.name}"
            continue
        definition = deepcopy(payload)
        database[request] = definition
        result.resolved[request] = definition
        result.origins[request] = selected.name
        pending.extend(definition.dependencies)
    return result, database


DEFAULT_TIERS = ("table", "notes", "xml", "derived")


def select_property(
    candidates: Mapping[str, Any], ranks: Mapping[str, int] | None = None
) -> tuple[Any, str] | None:
    """Choose value and origin, retaining 0/False and a stable default tie-break."""
    if set(candidates) - set(DEFAULT_TIERS):
        raise ValueError("Unknown property source tier")
    priority = {tier: index for index, tier in enumerate(DEFAULT_TIERS)}
    if ranks:
        if set(ranks) - set(DEFAULT_TIERS):
            raise ValueError("Unknown precedence tier")
        if any(not isinstance(rank, int) or isinstance(rank, bool) for rank in ranks.values()):
            raise TypeError("Precedence ranks must be integers")
        priority.update(ranks)
    usable = [tier for tier in DEFAULT_TIERS if tier in candidates
              and candidates[tier] is not None and candidates[tier] != ""]
    if not usable:
        return None
    winner = min(usable, key=lambda tier: (priority[tier], DEFAULT_TIERS.index(tier)))
    return deepcopy(candidates[winner]), winner


@dataclass(frozen=True)
class Contribution:
    store: str
    key: str
    operation: str
    value: Any = None


def apply_contributions(
    initial: Mapping[str, Mapping[str, Any]], contributions: Sequence[Contribution]
) -> dict[str, dict[str, Any]]:
    """Apply ordered typed updates; absence here means no key, not false/zero."""
    memory = deepcopy({name: dict(values) for name, values in initial.items()})
    for contribution in contributions:
        target = memory.setdefault(contribution.store, {})
        key, operation = contribution.key, contribution.operation
        value = deepcopy(contribution.value)
        if operation == "set":
            target[key] = value
        elif operation == "fill":
            if key not in target:
                target[key] = value
        elif operation == "remove":
            target.pop(key, None)
        elif operation == "append":
            previous = target.get(key, [])
            if not isinstance(previous, list):
                raise TypeError("append requires an ordered list")
            target[key] = previous + [value]
        elif operation == "concat":
            previous = target.get(key, "")
            if not isinstance(previous, str) or not isinstance(value, str):
                raise TypeError("concat requires strings")
            target[key] = previous + value
        else:
            raise ValueError(f"Unknown contribution operation: {operation}")
    return memory


@dataclass(frozen=True)
class FieldDefinition:
    identity: EntityKey
    name: str
    label: str
    datatype: str = "VARCHAR"
    database_length: int = 255
    maximum_input: int = 50
    form_default: str = "Some text"
    nullable: bool = True
    explicit_index: int = 0


@dataclass(frozen=True)
class FieldUse:
    extension: str
    view: str
    title: bool = False
    alias: bool = False
    category: bool = False
    searchable: bool = False
    sortable: bool = False
    persist: bool = True


def _identifier(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", value):
        raise ValueError(f"Invalid identifier for this small model: {value!r}")
    return value


def classify_field(definition: FieldDefinition, use: FieldUse) -> list[Contribution]:
    """A deliberately small field projection matching the paper's Greeting trace."""
    name = _identifier(definition.name)
    extension, view = _identifier(use.extension), _identifier(use.view)
    if definition.explicit_index not in (0, 1, 2) or isinstance(definition.explicit_index, bool):
        raise ValueError("Index selection must be 0, 1, or 2")
    if definition.database_length <= 0 or definition.maximum_input <= 0:
        raise ValueError("Field lengths must be positive")
    text_family = definition.datatype.upper() in {
        "TEXT", "TINYTEXT", "MEDIUMTEXT", "LONGTEXT", "BLOB", "TINYBLOB", "MEDIUMBLOB", "LONGBLOB"
    }
    key_kind = "none"
    if not text_family:
        if definition.explicit_index == 1:
            key_kind = "unique"
        elif definition.explicit_index == 2 or use.title or use.alias or use.category:
            key_kind = "ordinary"
    label_key = f"COM_{extension}_{view}_{name}_LABEL".upper()
    occurrence = f"{extension}.{view}.{name}"
    result = [
        Contribution("forms", occurrence, "set", {
            "name": name, "label": label_key, "maxlength": definition.maximum_input,
            "default": definition.form_default,
        }),
        Contribution("languages", label_key, "fill", definition.label),
        Contribution("metadata", occurrence, "set", {
            "identity": definition.identity.value, "title": use.title, "key": key_kind,
        }),
    ]
    if use.persist:
        db_type = definition.datatype.upper()
        if not text_family:
            db_type += f"({definition.database_length})"
        result.append(Contribution("schemas", occurrence, "set", {
            "name": name, "type": db_type, "nullable": definition.nullable, "key": key_kind,
        }))
        if use.searchable:
            result.append(Contribution("search", f"{extension}.{view}", "append", name))
        if use.sortable and not text_family:
            result.append(Contribution("sorting", f"{extension}.{view}", "append", name))
    return result


def ordered_replace(text: str, pairs: Sequence[tuple[str, str]], action: int = 1) -> str:
    """JCB-style ordered replacement, including original-input map filtering."""
    if not isinstance(text, str):
        raise TypeError("Input must be text")
    if not isinstance(action, int) or isinstance(action, bool) or action not in (1, 2, 3):
        raise ValueError("Action must be 1, 2, or 3")
    entries = list(pairs)
    for key, value in entries:
        if not isinstance(key, str) or not key or not isinstance(value, str):
            raise ValueError("Replacement entries require nonempty text keys and text values")
    if action == 2 and not any(key in text for key, _ in entries):
        return text
    if action == 3:
        entries = [(key, value) for key, value in entries if key in text]
    result = text
    for key, value in entries:
        result = result.replace(key, value)
    return result


class PrerequisiteError(ValueError):
    """The designated execution point has not established required information."""


@dataclass(frozen=True)
class DeferredWork:
    name: str
    prerequisites: frozenset[str]
    operation: Callable[[Mapping[str, Any]], Any]


def complete_deferred(
    work: Sequence[DeferredWork], available: Mapping[str, Any]
) -> dict[str, Any]:
    """Replay once in the specified order, without a hidden fixed-point scheduler."""
    state = deepcopy(dict(available))
    for item in work:
        missing = item.prerequisites - state.keys()
        if missing:
            raise PrerequisiteError(f"{item.name}: missing {', '.join(sorted(missing))}")
        state[item.name] = item.operation(deepcopy(state))
    return state


def portable_projection(record: Mapping[str, Any], fields: Sequence[str]) -> dict[str, Any]:
    """Select an explicit design schema; preserve nested structure and ordering."""
    if len(set(fields)) != len(fields):
        raise ValueError("Projection fields must be unique")
    missing = set(fields) - record.keys()
    if missing:
        raise ValueError(f"Missing design fields: {', '.join(sorted(missing))}")
    return {name: deepcopy(record[name]) for name in fields}
