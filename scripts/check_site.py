#!/usr/bin/env python3
"""Validate every HTML/Markdown pair, local link, anchor, and publication index.
SPDX-License-Identifier: MIT
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import zipfile
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'


def main() -> None:
    config = json.loads((ROOT / 'site.json').read_text())
    data = json.loads((SITE / 'articles.json').read_text())
    records = data['articles']
    sources = {path.relative_to(ROOT / 'DOCS').as_posix() for path in (ROOT / 'DOCS').rglob('*.md')}
    errors = []
    if sources != {record['path'] for record in records}:
        errors.append('Manifest/source article sets differ.')
    parsed = {}
    links = 0
    for record in records:
        source = ROOT / 'DOCS' / record['path']
        alternate = SITE / record['markdown_url'].lstrip('/')
        output = SITE / record['html_file']
        if not alternate.is_file() or alternate.read_bytes() != source.read_bytes():
            errors.append(f'{record["path"]}: Markdown alternate is not exact.')
        if record['sha256'] != hashlib.sha256(source.read_bytes()).hexdigest():
            errors.append(f'{record["path"]}: incorrect source digest.')
        if not output.is_file():
            errors.append(f'{record["path"]}: missing HTML.')
            continue
        soup = BeautifulSoup(output.read_text(), 'html.parser')
        parsed[output.resolve()] = soup
        if len(soup.select('h1')) != 1 or not soup.title or not soup.title.text.strip():
            errors.append(f'{record["path"]}: title/H1 contract failed.')
        alternate_link = soup.select_one('link[rel="alternate"][type="text/markdown"]')
        canonical = soup.select_one('link[rel="canonical"]')
        if not alternate_link or alternate_link.get('href') != config['url'] + record['markdown_url']:
            errors.append(f'{record["path"]}: missing Markdown discovery link.')
        if not canonical or canonical.get('href') != config['url'] + record['url']:
            errors.append(f'{record["path"]}: incorrect canonical URL.')
        if not soup.select_one('a[download]'):
            errors.append(f'{record["path"]}: no download action.')
        ids = [node.get('id') for node in soup.select('[id]')]
        if len(ids) != len(set(ids)):
            errors.append(f'{record["path"]}: duplicate DOM IDs.')
    host = urlsplit(config['url']).netloc
    for record in records:
        page = (SITE / record['html_file']).resolve()
        if page not in parsed:
            continue
        for node in parsed[page].select('[href], [src]'):
            value = node.get('href') or node.get('src')
            target_url = urlsplit(urljoin(config['url'] + record['url'], value))
            if target_url.scheme not in ('http', 'https') or target_url.netloc != host:
                continue
            links += 1
            target = (SITE / unquote(target_url.path).lstrip('/')).resolve()
            if not target.is_relative_to(SITE.resolve()):
                errors.append(f'{record["path"]}: link escapes output root: {value}')
                continue
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{record["path"]}: missing local target: {value}')
                continue
            if target_url.fragment and target.suffix == '.html':
                if target not in parsed:
                    parsed[target] = BeautifulSoup(target.read_text(), 'html.parser')
                if parsed[target].find(id=unquote(target_url.fragment)) is None:
                    errors.append(f'{record["path"]}: missing anchor: {value}')
    listed = [record for record in records if record['listed']]
    search = json.loads((SITE / 'search.json').read_text())
    if {record['url'] for record in listed} != {record['url'] for record in search}:
        errors.append('Search index does not cover exactly the listed articles.')
    llms = (SITE / 'llms.txt').read_text()
    sitemap = (SITE / 'sitemap.xml').read_text()
    for record in listed:
        if config['url'] + record['markdown_url'] not in llms or config['url'] + record['url'] not in sitemap:
            errors.append(f'{record["path"]}: missing discovery entry.')
    with zipfile.ZipFile(SITE / 'downloads' / 'vdmt-markdown.zip') as archive:
        for record in records:
            if archive.read('DOCS/' + record['path']) != (ROOT / 'DOCS' / record['path']).read_bytes():
                errors.append(f'{record["path"]}: Markdown archive mismatch.')
    forbidden = {'.woff', '.woff2', '.ttf', '.otf', '.eot'}
    if any(path.suffix.lower() in forbidden for path in SITE.rglob('*') if path.is_file()):
        errors.append('Unexpected distributed font file.')
    report = {'source_commit': data['source_commit'], 'articles': len(records), 'listed_articles': len(listed),
              'markdown_pairs_verified': len(records), 'local_links_checked': links,
              'words': sum(record['words'] for record in records), 'errors': errors}
    (ROOT / 'validation').mkdir(exist_ok=True)
    (ROOT / 'validation' / 'site.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
