#!/usr/bin/env python3
"""Reproduce the published example inventory from fixed, fingerprinted sources. MIT.

Only four public source archives are read. No imported code is executed. Use
--corpus-root to verify existing checkouts without any network access.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import sys
import tarfile
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.research_inventory import inventory, marker_traces

CONTRACT = ROOT / 'reference' / 'evidence' / 'hello-world-sources.json'
OUTPUT = ROOT / 'web' / 'static' / 'evidence' / 'hello-world.json'
MAX_ARCHIVE = 16 * 1024 * 1024
MAX_CONTENT = 64 * 1024 * 1024
MAX_FILES = 10000
METHOD = 'Regular files outside .git; no symlinks; UTF-8 without NUL; physical splitlines; SHA-256 bytes.'


def fingerprint(report: dict) -> str:
    """A path/content fingerprint independent of archive metadata and traversal."""
    entries = sorted((item['path'], item['sha256']) for item in report['files'])
    payload = json.dumps(entries, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    return hashlib.sha256(payload).hexdigest()


def unpack(data: bytes, target: Path) -> None:
    """Read regular members under one archive root; never extract links or devices."""
    target.mkdir(parents=True, exist_ok=True)
    seen: set[str] = set()
    total = 0
    archive_root = None
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
        for member in archive:
            path = PurePosixPath(member.name)
            if path.is_absolute() or '..' in path.parts or '\\' in member.name:
                raise ValueError('Unsafe archive path')
            if not path.parts:
                continue
            if archive_root is None:
                archive_root = path.parts[0]
            if path.parts[0] != archive_root:
                raise ValueError('Archive has multiple roots')
            if len(path.parts) < 2 or '.git' in path.parts or not member.isfile():
                continue
            relative = PurePosixPath(*path.parts[1:])
            key = relative.as_posix()
            if key in seen:
                raise ValueError('Archive has duplicate paths')
            seen.add(key)
            total += member.size
            if len(seen) > MAX_FILES or member.size < 0 or total > MAX_CONTENT:
                raise ValueError('Source archive exceeds the declared inventory limits')
            stream = archive.extractfile(member)
            if stream is None:
                raise ValueError('Unreadable regular archive member')
            with stream:
                content = stream.read(member.size + 1)
            if len(content) != member.size:
                raise ValueError('Truncated archive member')
            destination = target.joinpath(*relative.parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
    if not seen:
        raise ValueError('Source archive contains no regular files')


def fetch(repository: str, revision: str) -> bytes:
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Invalid source repository identity')
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError('Source revision must be a full commit SHA')
    url = f'https://codeload.github.com/{repository}/tar.gz/{revision}'
    request = Request(url, headers={'User-Agent': 'JCB-Architecture-Evidence/1.0'})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=60) as response:
                content = response.read(MAX_ARCHIVE + 1)
            if len(content) > MAX_ARCHIVE:
                raise ValueError('Compressed source archive exceeds the size limit')
            return content
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
        except (URLError, TimeoutError):
            if attempt == 2:
                raise
        time.sleep(attempt + 1)
    raise RuntimeError('Source retrieval did not complete')


def prepare(contract: dict, corpus: Path, *, download: bool) -> dict:
    roots = {}
    reports = {}
    for label, source in sorted(contract['repositories'].items()):
        if not re.fullmatch(r'[a-z0-9-]+', label):
            raise ValueError('Invalid evidence label')
        root = corpus / label
        if download:
            unpack(fetch(source['repository'], source['revision']), root)
        report = inventory(root, blueprint=label == contract['blueprint'])
        if fingerprint(report) != source['file_inventory_sha256']:
            raise ValueError(f'{label}: source path/content fingerprint differs from the reviewed capture')
        if report['totals'] != source['totals']:
            raise ValueError(f'{label}: inventory totals differ from the reviewed counting contract')
        report['revision'] = source['revision']
        roots[label] = root
        reports[label] = report
    return {'schema_version': 1, 'method': METHOD, 'repositories': reports,
            'marker_traces': marker_traces(roots, reports, contract['blueprint'])}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus-root', type=Path, help='Verify existing named checkouts instead of downloading')
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args()
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    if args.corpus_root:
        result = prepare(contract, args.corpus_root.resolve(strict=True), download=False)
    else:
        with tempfile.TemporaryDirectory(prefix='jcb-evidence-') as temporary:
            result = prepare(contract, Path(temporary), download=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(args.output)
    print(json.dumps({'verified_sources': len(result['repositories']),
                      'marker_traces': len(result['marker_traces']), 'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
