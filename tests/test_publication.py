"""General source/rendering contracts, independent of network and browser assets. MIT."""
from pathlib import Path
import tempfile
import unittest
import mistune
from scripts.build import Article, Renderer, read_article, resolve_markdown, slugify


class PublicationTests(unittest.TestCase):
    def test_slug_generation(self):
        self.assertEqual(slugify('Closure &amp; <em>scope</em>'), 'closure-scope')

    def test_relative_markdown_links(self):
        target = Article('foundations/definition.md', {}, '', b'', '/foundations/definition/', 'foundations/definition/index.html')
        self.assertEqual(resolve_markdown('../foundations/definition.md#scope', 'semantics/state.md', {target.path: target}), '/foundations/definition/#scope')
        self.assertEqual(resolve_markdown('../foundations/definition.md', 'semantics/state.md', {target.path: target}, raw=True), '/markdown/foundations/definition.md')

    def test_unknown_markdown_target_fails(self):
        with self.assertRaises(ValueError):
            resolve_markdown('../missing.md', 'a/b.md', {})

    def test_external_link_is_unchanged(self):
        url = 'https://example.org/paper.md'
        self.assertEqual(resolve_markdown(url, 'index.md', {}), url)

    def test_duplicate_headings_get_unique_ids(self):
        article = Article('index.md', {}, '', b'', '/', 'index.html')
        renderer = Renderer(article, {})
        renderer.heading('Repeated', 2)
        renderer.heading('Repeated', 2)
        self.assertEqual([h['id'] for h in renderer.headings], ['repeated', 'repeated-2'])

    def test_math_and_diagram_are_preserved(self):
        article = Article('index.md', {}, '', b'', '/', 'index.html')
        parser = mistune.create_markdown(renderer=Renderer(article, {}), plugins=['math', 'table'])
        result = parser('Inline $x^2$.\n\n$$\nF(K)=K\n$$\n\n```mermaid\nflowchart LR\n A --> B\n```\n')
        self.assertIn('class="math"', result)
        self.assertIn('class="mermaid"', result)
        self.assertIn('F(K)=K', result)

    def test_embedded_html_is_not_executable(self):
        article = Article('index.md', {}, '', b'', '/', 'index.html')
        parser = mistune.create_markdown(renderer=Renderer(article, {}))
        self.assertNotIn('<script>', parser('<script>alert(1)</script>'))

    def test_metadata_and_exact_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'index.md'
            raw = b'---\ntitle: Example\ndescription: Test page\nsection: Overview\norder: 1\nevidence: Test\n---\n# Example\n\nText.\n'
            path.write_bytes(raw)
            article = read_article(path, root)
            self.assertEqual(article.raw, raw)
            self.assertEqual(article.url, '/')

    def test_multiple_h1_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'index.md'
            path.write_text('---\ntitle: Example\ndescription: Test\nsection: Overview\norder: 1\nevidence: Test\n---\n# One\n\n# Two\n')
            with self.assertRaises(ValueError):
                read_article(path, root)

    def test_incomplete_metadata_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'index.md'
            path.write_text('---\ntitle: Only title\n---\n# Test\n')
            with self.assertRaises(ValueError):
                read_article(path, root)


if __name__ == '__main__':
    unittest.main()
