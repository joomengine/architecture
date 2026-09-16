#!/usr/bin/env python3
"""Archive the already built publication, never the working environment. MIT."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    site = ROOT / 'site'
    if not (site / 'articles.json').is_file():
        raise SystemExit('Build the publication before archiving it.')
    with zipfile.ZipFile(ROOT / 'jcb-architecture-site.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(site.rglob('*')):
            if path.is_file():
                if path.suffix.lower() in {'.woff', '.woff2', '.ttf', '.otf', '.eot'}:
                    raise ValueError('Font files must not be included.')
                archive.write(path, 'site/' + path.relative_to(site).as_posix())
    print('Created jcb-architecture-site.zip')


if __name__ == '__main__':
    main()
