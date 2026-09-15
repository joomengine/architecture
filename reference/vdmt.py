"""Executable contracts for the bounded VDMT model, not a JCB port.

Only finite, fixed positive rules are supported. Binding is non-recursive within
one pass. Editorial regions use a reserved LF-delimited grammar. See DOCS/ for
the assumptions and intentional differences from the production case study.
SPDX-License-Identifier: MIT
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import heapq
import re
import unicodedata
from collections.abc import Iterable, Mapping, Sequence


class ContractError(ValueError):
    """An input violates an explicit reference-model contract."""


class Conflict(ContractError):
    """Two authoritative assignments disagree."""


class MissingRequest(ContractError):
    """A required request has no authoritative resolution."""


class MissingBinding(ContractError):
    """A required token remains after all declared binding stages."""


@dataclass(frozen=True, order=True)
class Fact:
    key: tuple[str, ...]
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.key, tuple) or not self.key:
            raise ContractError('Fact keys must be nonempty tuples.')
        if any(not isinstance(part, str) or not part for part in self.key):
            raise ContractError('Every key dimension must be a nonempty string.')
        if not isinstance(self.value, str):
            raise ContractError('The reference model uses string-valued facts.')


class Knowledge:
    """Consistent scoped assignments; an empty string remains a present value."""

    def __init__(self, facts: Iterable[Fact] = ()) -> None:
        self._values: dict[tuple[str, ...], str] = {}
        self.extend(facts)

    def extend(self, facts: Iterable[Fact]) -> bool:
        candidate = dict(self._values)
        for fact in facts:
            if not isinstance(fact, Fact):
                raise ContractError('Knowledge accepts Fact instances only.')
            if fact.key in candidate and candidate[fact.key] != fact.value:
                raise Conflict(f'Incompatible values at {fact.key!r}.')
            candidate[fact.key] = fact.value
        changed = candidate != self._values
        self._values = candidate
        return changed

    def contains(self, fact: Fact) -> bool:
        return fact.key in self._values and self._values[fact.key] == fact.value

    def get(self, key: tuple[str, ...]) -> str:
        if key not in self._values:
            raise MissingRequest(f'No established value at {key!r}.')
        return self._values[key]

    def facts(self) -> frozenset[Fact]:
        return frozenset(Fact(key, value) for key, value in self._values.items())


@dataclass(frozen=True)
class Resolution:
    facts: tuple[Fact, ...] = ()
    dependencies: tuple[str, ...] = ()


@dataclass(frozen=True)
class Closure:
    facts: frozenset[Fact]
    completed: tuple[str, ...]


def gather(roots: Iterable[str], source: Mapping[str, Resolution]) -> Closure:
    """Traverse a finite, stable request graph. Unknown roots/dependencies fail."""
    pending = list(roots)
    if any(not isinstance(q, str) or not q for q in pending):
        raise ContractError('Requests must be nonempty strings.')
    heapq.heapify(pending)
    completed: set[str] = set()
    knowledge = Knowledge()
    while pending:
        request = heapq.heappop(pending)
        if request in completed:
            continue
        if request not in source:
            raise MissingRequest(f'Unresolved required request: {request}')
        result = source[request]
        if not isinstance(result, Resolution):
            raise ContractError('Resolvers must return Resolution records.')
        knowledge.extend(result.facts)
        completed.add(request)
        for dependency in result.dependencies:
            if not isinstance(dependency, str) or not dependency:
                raise ContractError('Dependency keys must be nonempty strings.')
            if dependency not in completed:
                heapq.heappush(pending, dependency)
    return Closure(knowledge.facts(), tuple(sorted(completed)))


@dataclass(frozen=True)
class Rule:
    name: str
    requires: tuple[Fact, ...]
    produces: tuple[Fact, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ContractError('A rule needs a stable name.')
        if not isinstance(self.requires, tuple) or not isinstance(self.produces, tuple):
            raise ContractError('Rule premises and consequences must be immutable tuples.')
        if any(not isinstance(fact, Fact) for fact in self.requires + self.produces):
            raise ContractError('Rules require fixed Fact premises and consequences.')


def saturate(seed: Iterable[Fact], rules: Sequence[Rule]) -> frozenset[Fact]:
    """Least positive closure for finite fixed consequences, or explicit conflict."""
    if len({rule.name for rule in rules}) != len(rules):
        raise ContractError('Rule identifiers must be unique.')
    ordered = sorted(rules, key=lambda rule: rule.name)
    knowledge = Knowledge(seed)
    while True:
        changed = False
        for rule in ordered:
            if all(knowledge.contains(fact) for fact in rule.requires):
                changed = knowledge.extend(rule.produces) or changed
        if not changed:
            return knowledge.facts()


TOKEN = re.compile(r'\{\{([A-Z][A-Z0-9_]*)\}\}')


def bind(template: str, stages: Sequence[Mapping[str, str]]) -> str:
    """One simultaneous pass per stage; replacement bodies are not rescanned."""
    if not isinstance(template, str):
        raise ContractError('Templates must be strings.')
    result = template
    for environment in stages:
        if any(not isinstance(k, str) or not isinstance(v, str)
               for k, v in environment.items()):
            raise ContractError('Bindings must map strings to strings.')
        result = TOKEN.sub(lambda match: environment.get(match.group(1), match.group(0)), result)
    remaining = sorted(set(TOKEN.findall(result)))
    if remaining:
        raise MissingBinding('Unresolved tokens: ' + ', '.join(remaining))
    return result


MARKER = re.compile(r'<!-- VDMT:(BEGIN|END) ([A-Za-z0-9_.:/-]+) -->\n')
RESERVED = '<!-- VDMT:'


def _regions(text: str) -> dict[str, tuple[int, int]]:
    if not isinstance(text, str) or '\r' in text:
        raise ContractError('Editorial artifacts must be strings with LF line endings.')
    regions: dict[str, tuple[int, int]] = {}
    opened: tuple[str, int] | None = None
    offset = 0
    for line in text.splitlines(keepends=True):
        if RESERVED in line:
            match = MARKER.fullmatch(line)
            if match is None:
                raise ContractError('Malformed or non-line-oriented reserved marker.')
            operation, identity = match.groups()
            if operation == 'BEGIN':
                if opened is not None or identity in regions:
                    raise ContractError('Nested or duplicate editorial region.')
                opened = (identity, offset + len(line))
            else:
                if opened is None or opened[0] != identity:
                    raise ContractError('Unmatched editorial region end.')
                regions[identity] = (opened[1], offset)
                opened = None
        offset += len(line)
    if opened is not None:
        raise ContractError('Unclosed editorial region.')
    return regions


def extract_regions(text: str) -> dict[str, str]:
    return {identity: text[start:end] for identity, (start, end) in _regions(text).items()}


def put_regions(template: str, memory: Mapping[str, str]) -> str:
    regions = _regions(template)
    if set(regions) != set(memory):
        raise ContractError('Editorial memory must cover exactly the template region domain.')
    for body in memory.values():
        if not isinstance(body, str) or '\r' in body or RESERVED in body:
            raise ContractError('Invalid or marker-bearing editorial body.')
        if body and not body.endswith('\n'):
            raise ContractError('A nonempty region body must end with LF.')
    result = template
    for identity, (start, end) in sorted(regions.items(), key=lambda item: item[1][0], reverse=True):
        result = result[:start] + memory[identity] + result[end:]
    return result


def reconcile(base: Mapping[str, str], source: Mapping[str, str], user: Mapping[str, str]) -> dict[str, str]:
    """Whole-region three-way comparison; migration must happen outside this model."""
    if set(base) != set(source) or set(base) != set(user):
        raise Conflict('Changed region domains require an explicit migration.')
    merged: dict[str, str] = {}
    for key in sorted(base):
        b, s, u = base[key], source[key], user[key]
        if not all(isinstance(value, str) for value in (b, s, u)):
            raise ContractError('Editorial values must be strings.')
        if u == b or u == s:
            merged[key] = s
        elif s == b:
            merged[key] = u
        else:
            raise Conflict(f'Simultaneous incompatible edits to region {key!r}.')
    return merged


WINDOWS_RESERVED = {'CON', 'PRN', 'AUX', 'NUL'} | {f'{p}{i}' for p in ('COM', 'LPT') for i in range(1, 10)}


def validate_path(path: str) -> str:
    """Conservative portable logical path policy, before filesystem resolution."""
    if not isinstance(path, str) or not path or path.startswith('/'):
        raise ContractError('An artifact path must be relative and nonempty.')
    if unicodedata.normalize('NFC', path) != path:
        raise ContractError('Artifact paths must use NFC normalization.')
    if any(ord(char) < 32 for char in path) or any(char in path for char in '\\:*?"<>|'):
        raise ContractError('Unsupported artifact path characters.')
    for part in path.split('/'):
        if not part or part in {'.', '..'} or part.endswith((' ', '.')):
            raise ContractError('Invalid artifact path segment.')
        if part.split('.')[0].upper() in WINDOWS_RESERVED:
            raise ContractError('Reserved portable filename.')
    return path


@dataclass(frozen=True)
class Artifact:
    identity: str
    path: str
    content: str


def artifact_map(artifacts: Iterable[Artifact]) -> dict[str, str]:
    items = list(artifacts)
    identities: set[str] = set()
    destinations: set[str] = set()
    for item in items:
        if not isinstance(item, Artifact) or not item.identity or not isinstance(item.content, str):
            raise ContractError('Invalid artifact record.')
        path = validate_path(item.path)
        if item.identity in identities or path.casefold() in destinations:
            raise Conflict('Duplicate artifact identity or portable destination.')
        identities.add(item.identity)
        destinations.add(path.casefold())
    return {item.path: item.content for item in sorted(items, key=lambda item: item.path)}


def manifest(artifacts: Mapping[str, str]) -> list[dict[str, str | int]]:
    return [{'path': path, 'bytes': len(content.encode('utf-8')),
             'sha256': hashlib.sha256(content.encode('utf-8')).hexdigest()}
            for path, content in sorted(artifacts.items())]
