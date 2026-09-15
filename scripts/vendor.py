#!/usr/bin/env python3
"""Acquire versioned, integrity-checked browser assets; never run on page views.

No font files are extracted. MathJax uses SVG glyph paths. Registry tarball
integrity is checked, and vendor.lock.json additionally pins acquisition bytes
when present. SPDX-License-Identifier: MIT
"""
from __future__ import annotations
import base64
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import shutil
import tarfile
import time
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'vendor'
PACKAGES = {'mathjax': '3.2.2', 'mermaid': '11.12.0'}
LIMIT = 80 * 1024 * 1024


def acquire(url: str) -> bytes:
    if urlparse(url).scheme != 'https':
        raise ValueError('Only HTTPS acquisition is permitted.')
    error = None
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={'User-Agent': 'VDMT-publication/0.1.0'}), timeout=60) as response:
                if urlparse(response.geturl()).scheme != 'https':
                    raise ValueError('Insecure acquisition redirect.')
                data = response.read(LIMIT + 1)
                if len(data) > LIMIT:
                    raise ValueError('Acquisition exceeds the configured byte limit.')
                return data
        except Exception as exc:
            error = exc
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise RuntimeError(f'Unable to acquire {url}: {error}')


def package(name: str, version: str, expected: dict) -> dict:
    metadata = json.loads(acquire(f'https://registry.npmjs.org/{name}/{version}'))
    dist = metadata['dist']
    integrity = dist['integrity']
    if expected.get('integrity') and integrity != expected['integrity']:
        raise ValueError(f'Locked integrity changed for {name}.')
    algorithm, encoded = integrity.split('-', 1)
    if algorithm != 'sha512':
        raise ValueError('Expected SHA-512 npm integrity.')
    archive = acquire(dist['tarball'])
    if hashlib.sha512(archive).digest() != base64.b64decode(encoded, validate=True):
        raise ValueError(f'Corrupt {name} tarball.')
    prefix = f'package/{"es5" if name == "mathjax" else "dist"}/'
    total = 0
    count = 0
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as bundle:
        for member in bundle.getmembers():
            if not member.isfile():
                continue
            path = PurePosixPath(member.name)
            if path.is_absolute() or '..' in path.parts:
                raise ValueError('Unsafe archive member.')
            relative = None
            if member.name.startswith(prefix) and path.suffix in {'.js', '.mjs', '.json', '.css'}:
                relative = member.name[len(prefix):]
            elif path.name.upper().startswith(('LICENSE', 'COPYING')) and len(path.parts) == 2:
                relative = path.name
            if relative is None:
                continue
            total += member.size
            if total > 180 * 1024 * 1024:
                raise ValueError('Extracted package exceeds the configured limit.')
            stream = bundle.extractfile(member)
            if stream is None:
                raise ValueError('Missing archive member content.')
            target = DEST / name / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(stream.read())
            count += 1
    return {'version': version, 'integrity': integrity, 'tarball': dist['tarball'], 'files': count}


def main() -> None:
    lock_path = ROOT / 'vendor.lock.json'
    locked = json.loads(lock_path.read_text()) if lock_path.exists() else {}
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir()
    records = {'packages': {}, 'brand': {}}
    for name, version in PACKAGES.items():
        records['packages'][name] = package(name, version, locked.get('packages', {}).get(name, {}))
    image_data = acquire('https://www.vdm.io/VDM.png')
    digest = hashlib.sha256(image_data).hexdigest()
    if locked.get('brand', {}).get('sha256') not in (None, digest):
        raise ValueError('The locked VDM brand source has changed; review before updating.')
    Image.MAX_IMAGE_PIXELS = 80_000_000
    with Image.open(io.BytesIO(image_data)) as source:
        source.load()
        original_size = list(source.size)
        mark = ImageOps.contain(source.convert('RGBA'), (256, 256), Image.Resampling.LANCZOS)
        canvas = Image.new('RGBA', (256, 256), (255, 255, 255, 0))
        canvas.alpha_composite(mark, ((256 - mark.width) // 2, (256 - mark.height) // 2))
        brand = DEST / 'brand'
        brand.mkdir()
        canvas.save(brand / 'mark.png', optimize=True)
        canvas.save(brand / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
        canvas.resize((180, 180), Image.Resampling.LANCZOS).save(brand / 'apple-touch-icon.png', optimize=True)
    records['brand'] = {'url': 'https://www.vdm.io/VDM.png', 'sha256': digest, 'original_size': original_size}
    records['files'] = {path.relative_to(DEST).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in sorted(DEST.rglob('*')) if path.is_file()}
    (DEST / 'manifest.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'packages': records['packages'], 'brand': records['brand']}, indent=2))


if __name__ == '__main__':
    main()
