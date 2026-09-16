"""Protect the agreed text identity and retained small publisher mark. MIT."""
import json
from pathlib import Path
import unittest
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, select_autoescape
from scripts.build import Article

ROOT = Path(__file__).resolve().parents[1]


class BrandingTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT / 'site.json').read_text())
        self.template = Environment(loader=FileSystemLoader(ROOT / 'web/templates'),
                                    autoescape=select_autoescape(['html'])).get_template('page.html')

    def render(self, path='index.md'):
        article = Article(path, {'title': 'Article title', 'section': 'Overview',
                                'description': 'Test description', 'evidence': 'Source trace'},
                          '', b'', '/', 'index.html', rendered='<h1>Article title</h1>')
        markup = self.template.render(article=article, config=self.config,
            sections=[], toc=[], commit='test', canonical=self.config['url'] + '/',
            markdown_url='/markdown/' + path, citation='Test citation', source_url='https://example.org/source')
        return BeautifulSoup(markup, 'html.parser')

    def test_header_is_text_and_retains_only_the_small_publisher_mark(self):
        for path in ('index.md', 'compiler/execution.md'):
            with self.subTest(path=path):
                soup = self.render(path)
                brand = soup.select_one('.brand')
                self.assertIn('Joomla Component Builder', brand.get_text())
                self.assertIn('Architecture', brand.get_text())
                self.assertEqual(len(brand.select('img')), 1)
                self.assertEqual(brand.img['alt'], 'VDM')
                self.assertLessEqual(int(brand.img['width']), 48)
                self.assertFalse(soup.select('.wordmark, img[src*="wordmark"]'))
                self.assertFalse((ROOT / 'web/static/wordmark.png').exists())

    def test_metadata_uses_current_identity_and_author(self):
        soup = self.render()
        self.assertIn(self.config['short_title'], soup.title.text)
        self.assertEqual(soup.select_one('meta[name="citation_author"]')['content'], self.config['author'])
        self.assertEqual(soup.select_one('meta[property="og:site_name"]')['content'], self.config['short_title'])
        self.assertEqual(soup.select_one('link[rel="canonical"]')['href'], self.config['url'] + '/')

    def test_footer_preserves_author_publisher_and_reuse_information(self):
        footer = self.render().select_one('.article-footer')
        self.assertIn(self.config['author'], footer.text)
        self.assertIn(self.config['publisher'], footer.text)
        self.assertIsNotNone(footer.select_one('a[href="/reference/licensing/"]'))

    def test_editorial_link_resolves_to_an_existing_article(self):
        link = self.render().select_one('.evidence-note a')
        self.assertEqual(link.get_text(), 'Edition and sources')
        target = ROOT / 'DOCS' / (link['href'].strip('/') + '.md')
        self.assertTrue(target.is_file())

    def test_search_describes_the_architecture(self):
        soup = self.render()
        for button in soup.select('.search-open'):
            self.assertIn('Search the architecture', button.get_text())
        self.assertIn('extrusion', soup.select_one('#search-input')['placeholder'])

    def test_every_page_retains_markdown_and_citation_actions(self):
        soup = self.render('compiler/execution.md')
        self.assertEqual(soup.select_one('link[type="text/markdown"]')['href'],
                         self.config['url'] + '/markdown/compiler/execution.md')
        self.assertEqual(soup.select_one('a[download]')['href'], '/markdown/compiler/execution.md')
        self.assertIsNotNone(soup.select_one('button[data-copy="Test citation"]'))


if __name__ == '__main__':
    unittest.main()
