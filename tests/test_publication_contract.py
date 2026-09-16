"""End-to-end offline publication contracts; network/browser checks run separately. MIT."""
from contextlib import ExitStack, redirect_stdout
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import urlsplit
import zipfile
from scripts import archive, build, check_site

ROOT = Path(__file__).resolve().parents[1]


class PublicationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workspace = tempfile.TemporaryDirectory()
        cls.root = Path(cls.workspace.name)
        for name in ('DOCS', 'web'):
            shutil.copytree(ROOT / name, cls.root / name)
        for name in ('site.json', 'README.md', 'AUTHORS.md', 'CONTRIBUTING.md',
                     'LICENSE', 'NOTICE.md', 'CITATION.cff'):
            shutil.copyfile(ROOT / name, cls.root / name)
        # The publication checker needs file presence, not a network download.
        for name in ('mathjax/tex-svg.js', 'mermaid/mermaid.esm.min.mjs', 'brand/mark.png',
                     'brand/favicon.ico', 'brand/apple-touch-icon.png', 'manifest.json'):
            target = cls.root / 'vendor' / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('{}' if name.endswith('.json') else 'test asset')
        evidence = cls.root / 'web/static/evidence/hello-world.json'
        evidence.parent.mkdir(parents=True, exist_ok=True)
        evidence.write_text(json.dumps({'schema_version': 1, 'repositories': {}}))
        with cls.patched_roots(), redirect_stdout(io.StringIO()):
            build.main()
            check_site.main()
            archive.main()
        cls.data = json.loads((cls.root / 'site/articles.json').read_text())
        cls.config = json.loads((cls.root / 'site.json').read_text())

    @classmethod
    def patched_roots(cls):
        stack = ExitStack()
        for module in (build, check_site, archive):
            stack.enter_context(patch.object(module, 'ROOT', cls.root))
        stack.enter_context(patch.object(build, 'DOCS', cls.root / 'DOCS'))
        stack.enter_context(patch.object(build, 'SITE', cls.root / 'site'))
        stack.enter_context(patch.object(check_site, 'SITE', cls.root / 'site'))
        return stack

    @classmethod
    def tearDownClass(cls):
        cls.workspace.cleanup()

    def test_all_articles_have_exact_alternates_and_valid_local_links(self):
        report = json.loads((self.root / 'validation/site.json').read_text())
        self.assertFalse(report['errors'])
        self.assertEqual(report['articles'], report['markdown_pairs_verified'])
        self.assertGreater(report['local_links_checked'], report['articles'])

    def test_publication_identity_is_consistent_in_discovery_and_licenses(self):
        site = self.root / 'site'
        self.assertTrue((site / 'llms.txt').read_text().startswith('# ' + self.config['title']))
        self.assertEqual((site / 'CNAME').read_text().strip(), urlsplit(self.config['url']).hostname)
        for name in ('LICENSE', 'CITATION.cff'):
            self.assertIn(self.config['url'], (site / name).read_text())
        for record in self.data['articles']:
            self.assertEqual(record['canonical'], self.config['url'] + record['url'])
            self.assertEqual(record['markdown'], self.config['url'] + record['markdown_url'])
            self.assertTrue(record['source'].startswith(self.config['repository'] + '/blob/'))

    def test_archive_name_matches_the_workflow_and_contains_the_entire_site(self):
        with zipfile.ZipFile(self.root / 'jcb-architecture-site.zip') as package:
            expected = {'site/' + p.relative_to(self.root / 'site').as_posix()
                        for p in (self.root / 'site').rglob('*') if p.is_file()}
            self.assertEqual(set(package.namelist()), expected)
        workflow = (ROOT / '.github/workflows/publication.yml').read_text()
        self.assertIn('jcb-architecture-site.zip', workflow)
        self.assertIn('python scripts/prepare_evidence.py', workflow)

    def test_downloads_and_pinned_evidence_are_published(self):
        site = self.root / 'site'
        for name in ('jcb-architecture-complete.md', 'jcb-architecture-markdown.zip'):
            self.assertTrue((site / 'downloads' / name).is_file())
        self.assertTrue((site / 'evidence/hello-world.json').is_file())
        with zipfile.ZipFile(site / 'downloads/jcb-architecture-markdown.zip') as package:
            for record in self.data['articles']:
                self.assertEqual(package.read('DOCS/' + record['path']),
                                 (self.root / 'DOCS' / record['path']).read_bytes())

    def test_link_checker_rejects_a_broken_shared_link_instead_of_skipping_it(self):
        path = self.root / 'site/index.html'
        original = path.read_bytes()
        try:
            path.write_text(original.decode().replace('</article>', '<a href="/missing-page/">Broken</a></article>'))
            with self.patched_roots(), redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
                check_site.main()
        finally:
            path.write_bytes(original)
            with self.patched_roots(), redirect_stdout(io.StringIO()):
                check_site.main()


if __name__ == '__main__':
    unittest.main()
