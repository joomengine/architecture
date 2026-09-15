"""Protect the transparent wordmark asset and its single-line presentation. MIT."""
from pathlib import Path
import unittest
from PIL import Image
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from scripts.build import Article

ROOT = Path(__file__).resolve().parents[1]


class WordmarkTests(unittest.TestCase):
    def test_png_has_transparent_canvas_and_visible_lettering(self):
        with Image.open(ROOT / 'web/static/wordmark.png') as image:
            self.assertEqual(image.format, 'PNG')
            self.assertGreater(image.width, image.height * 10)
            alpha = image.convert('RGBA').getchannel('A')
            self.assertEqual(alpha.getextrema()[0], 0)
            self.assertGreater(alpha.getextrema()[1], 240)
            for x, y in ((0, 0), (image.width - 1, 0), (0, image.height - 1), (image.width - 1, image.height - 1)):
                self.assertEqual(alpha.getpixel((x, y)), 0)
            histogram = alpha.histogram()
            self.assertGreater(histogram[0], image.width * image.height // 4)
            self.assertGreater(sum(histogram[241:]), image.width * image.height // 4)

    def test_homepage_uses_one_image_without_a_separate_caption(self):
        template = Environment(loader=FileSystemLoader(ROOT / 'web/templates')).get_template('page.html')
        article = Article('index.md', {'title': 'Home', 'section': 'Overview'}, '', b'', '/', 'index.html')
        markup = template.render(article=article, config={'title': 'VDMT', 'url': 'https://theory.vdm.io', 'version': '0.1.0'}, sections=[], toc=[], commit='test')
        wordmark = BeautifulSoup(markup, 'html.parser').select_one('.wordmark')
        self.assertIsNotNone(wordmark)
        self.assertEqual(len(wordmark.select('img')), 1)
        self.assertEqual(wordmark.select_one('img')['src'], '/assets/wordmark.png')
        self.assertEqual(wordmark.select_one('img')['alt'], 'Vast Development Method Theory')
        self.assertEqual(wordmark.get_text(strip=True), '')
        self.assertFalse((ROOT / 'web/static/wordmark.webp').exists())


if __name__ == '__main__':
    unittest.main()
