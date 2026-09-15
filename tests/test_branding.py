"""Source-derived wordmark transparency and responsive placement contracts. MIT."""
from pathlib import Path
import unittest
from bs4 import BeautifulSoup
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


class WordmarkTests(unittest.TestCase):
    def test_all_lettering_assets_have_transparent_margins(self):
        paths = sorted((ROOT / 'web/static/wordmark').glob('*.webp'))
        self.assertEqual(len(paths), 5)
        for path in paths:
            with self.subTest(asset=path.name), Image.open(path) as image:
                self.assertEqual(image.height, 80)
                alpha = image.convert('RGBA').getchannel('A')
                self.assertEqual(alpha.getextrema()[0], 0)
                self.assertGreaterEqual(alpha.getextrema()[1], 250)
                self.assertIsNone(alpha.crop((0, 0, image.width, 8)).getbbox())
                self.assertIsNone(alpha.crop((0, 72, image.width, 80)).getbbox())

    def test_wordmark_has_one_accessible_label_and_no_caption(self):
        soup = BeautifulSoup((ROOT / 'web/templates/page.html').read_text(), 'html.parser')
        wordmark = soup.select_one('.wordmark')
        self.assertIsNotNone(wordmark)
        root = wordmark.find('svg', recursive=False)
        self.assertIsNotNone(root)
        self.assertEqual(root.get('role'), 'img')
        self.assertEqual(root.find('title').text, 'Vast Development Method Theory')
        self.assertIsNone(wordmark.find('span'))
        self.assertEqual(root.get('viewbox'), '0 0 1200 80')

    def test_all_svg_image_references_exist(self):
        soup = BeautifulSoup((ROOT / 'web/templates/page.html').read_text(), 'html.parser')
        for image in soup.select('.wordmark image'):
            href = image.get('href', '')
            self.assertTrue(href.startswith('/assets/wordmark/'))
            self.assertTrue((ROOT / 'web/static' / href.removeprefix('/assets/')).is_file())

    def test_glyphs_share_one_baseline(self):
        soup = BeautifulSoup((ROOT / 'web/templates/page.html').read_text(), 'html.parser')
        for image in soup.select('.wordmark image'):
            self.assertEqual(image.get('height'), '80')
            self.assertIn(image.get('y'), (None, '0'))

    def test_wordmark_styles_are_scoped_and_loaded_after_the_theme(self):
        css = (ROOT / 'web/static/wordmark.css').read_text()
        for declaration in ('width: 100%', 'max-width: none', 'background: transparent', 'border: 0', 'padding: 0'):
            self.assertIn(declaration, css)
        soup = BeautifulSoup((ROOT / 'web/templates/page.html').read_text(), 'html.parser')
        sheets = [node.get('href') for node in soup.select('link[rel="stylesheet"]')]
        self.assertGreater(sheets.index('/assets/wordmark.css'), sheets.index('/assets/site.css'))
