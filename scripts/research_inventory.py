#!/usr/bin/env python3
"""Inventory pinned source checkouts without executing their code.

Use --corpus-root for the publication's named Hello World checkouts, or provide
repeated --repository LABEL=PATH arguments. JSON output contains every counted
file and its hash, separate blueprint categories, and non-unique marker traces.
SPDX-License-Identifier: MIT
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from typing import Any

DEFAULT_LABELS = ("hello-blueprint", "hello-component", "hello-module", "hello-plugin")
TEXT_MARKER = re.compile(r"//\s*Add\s+(?:PHP|JavaScript|JS|CSS)\b[^\r\n]*", re.IGNORECASE)


def files_under(root: Path):
    """Never follow links or count Git's own metadata."""
    for directory, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = sorted(name for name in dirs if name != ".git" and not (Path(directory) / name).is_symlink())
        for name in sorted(names):
            path = Path(directory) / name
            if path.is_file() and not path.is_symlink():
                yield path


def text_content(content: bytes) -> str | None:
    if b"\0" in content:
        return None
    try:
        return content.decode("utf-8")
    except UnicodeDecodeError:
        return None


def category(relative: str, blueprint: bool) -> str:
    if not blueprint:
        return "product"
    path = Path(relative)
    if relative.startswith("src/file_folder/"):
        return "assets"
    if relative.startswith("src/") and path.suffix == ".json":
        return "payload"
    if relative.startswith("index/") and path.suffix == ".json":
        return "index"
    if path.suffix == ".md":
        return "documentation"
    return "other"


def inventory(root: Path, *, blueprint: bool = False) -> dict[str, Any]:
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError(f"Not a directory: {root}")
    records = []
    totals: dict[str, dict[str, int]] = defaultdict(lambda: {"files": 0, "bytes": 0, "text_files": 0, "physical_text_lines": 0})
    for path in files_under(root):
        content = path.read_bytes()
        text = text_content(content)
        relative = path.relative_to(root).as_posix()
        group = category(relative, blueprint)
        lines = len(text.splitlines()) if text is not None else None
        record = {"path": relative, "category": group, "bytes": len(content),
                  "sha256": hashlib.sha256(content).hexdigest(), "text_lines": lines}
        records.append(record)
        for key in ("all", group):
            totals[key]["files"] += 1
            totals[key]["bytes"] += len(content)
            if lines is not None:
                totals[key]["text_files"] += 1
                totals[key]["physical_text_lines"] += lines
    result: dict[str, Any] = {"totals": dict(sorted(totals.items())), "files": records}
    if blueprint:
        result["root_item_payloads"] = sum(record["category"] == "payload" and Path(record["path"]).name == "item.json" for record in records)
        result["child_or_other_payloads"] = totals["payload"]["files"] - result["root_item_payloads"]
    return result


def strings(value: Any, pointer: str = ""):
    if isinstance(value, str):
        yield pointer, value
    elif isinstance(value, dict):
        for key, child in value.items():
            escaped = str(key).replace("~", "~0").replace("/", "~1")
            yield from strings(child, pointer + "/" + escaped)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from strings(child, pointer + "/" + str(index))


def marker_traces(roots: dict[str, Path], reports: dict[str, dict], blueprint_label: str) -> list[dict]:
    """Retain every source property sharing a marker, not a false unique origin."""
    origins: dict[str, list[dict]] = defaultdict(list)
    root = roots[blueprint_label]
    for record in reports[blueprint_label]["files"]:
        if record["category"] != "payload":
            continue
        value = json.loads((root / record["path"]).read_text(encoding="utf-8"))
        for pointer, text in strings(value):
            for match in TEXT_MARKER.finditer(text):
                marker = match.group().strip()
                origin = {"path": record["path"], "pointer": pointer}
                if origin not in origins[marker]:
                    origins[marker].append(origin)
    matches: dict[str, list[dict]] = defaultdict(list)
    for label, root in roots.items():
        if label == blueprint_label:
            continue
        for record in reports[label]["files"]:
            if record["text_lines"] is None:
                continue
            text = (root / record["path"]).read_text(encoding="utf-8")
            for number, line in enumerate(text.splitlines(), 1):
                for marker in origins:
                    if marker in line:
                        matches[marker].append({"repository": label, "path": record["path"], "line": number})
    return [{"marker": marker, "source_properties": origins[marker], "output_occurrences": matches[marker]}
            for marker in sorted(origins)]


def git_revision(path: Path) -> str | None:
    if not (path / ".git").exists():
        return None
    try:
        result = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"],
                                check=True, capture_output=True, text=True, timeout=5)
        return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None


def assignment(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("Use LABEL=VALUE")
    label, target = value.split("=", 1)
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", label) or not target:
        raise argparse.ArgumentTypeError("Use a nonempty simple label and value")
    return label, target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-root", type=Path)
    parser.add_argument("--repository", action="append", type=assignment, default=[])
    parser.add_argument("--revision", action="append", type=assignment, default=[])
    parser.add_argument("--blueprint", default="hello-blueprint")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    roots = {label: Path(path).resolve() for label, path in args.repository}
    if len(roots) != len(args.repository):
        parser.error("Repository labels must be unique")
    if args.corpus_root:
        for label in DEFAULT_LABELS:
            roots.setdefault(label, (args.corpus_root / label).resolve())
    if not roots:
        parser.error("Supply --corpus-root or --repository")
    revisions = dict(args.revision)
    if len(revisions) != len(args.revision) or set(revisions) - set(roots):
        parser.error("Revision labels must be unique and identify supplied repositories")
    if any(not re.fullmatch(r"[0-9a-fA-F]{40}", revision) for revision in revisions.values()):
        parser.error("A declared revision must be a full 40-character commit SHA")
    try:
        reports = {label: inventory(path, blueprint=label == args.blueprint) for label, path in sorted(roots.items())}
        for label, path in roots.items():
            reports[label]["revision"] = revisions.get(label) or git_revision(path)
        result = {"schema_version": 1,
                  "method": "Regular files outside .git; no symlinks; UTF-8 without NUL; physical splitlines; SHA-256 bytes.",
                  "repositories": reports,
                  "marker_traces": marker_traces(roots, reports, args.blueprint) if args.blueprint in roots else []}
    except (OSError, ValueError) as error:
        parser.error(str(error))
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
