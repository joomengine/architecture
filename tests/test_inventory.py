"""Tests for category accounting and non-unique blueprint marker provenance. MIT."""
import json
from pathlib import Path
import tempfile
import unittest
from scripts.research_inventory import inventory, marker_traces


class InventoryTests(unittest.TestCase):
    def test_categories_do_not_count_indexes_as_payload(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, content in {
                'src/field/x/item.json': b'{"name":"x"}\n',
                'src/view/children/x/fields.json': b'{}\n',
                'index/fields.json': b'{}\n',
                'README.md': b'# Description\n\nText\n',
                'src/file_folder/x/image.png': b'\x89PNG\0x',
                '.git/config': b'not counted\n',
            }.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            (root / 'linked').symlink_to(root / 'README.md')
            result = inventory(root, blueprint=True)
            self.assertEqual(result['totals']['payload']['files'], 2)
            self.assertEqual(result['totals']['index']['files'], 1)
            self.assertEqual(result['totals']['assets']['text_files'], 0)
            self.assertEqual(result['root_item_payloads'], 1)
            self.assertEqual(result['child_or_other_payloads'], 1)
            self.assertEqual(result['totals']['all']['files'], 5)
            self.assertTrue(all(len(record['sha256']) == 64 for record in result['files']))

    def test_identical_markers_retain_both_source_properties(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            blueprint, product = base / 'blueprint', base / 'product'
            payload = blueprint / 'src/view/x/item.json'
            payload.parent.mkdir(parents=True)
            payload.write_text(json.dumps({'php_save': '// Add PHP save', 'php_before_save': '// Add PHP save'}))
            product.mkdir()
            (product / 'model.php').write_text('<?php\n// Add PHP save\n// Add PHP save\n')
            roots = {'hello-blueprint': blueprint, 'component': product}
            reports = {key: inventory(path, blueprint=key == 'hello-blueprint') for key, path in roots.items()}
            traces = marker_traces(roots, reports, 'hello-blueprint')
            self.assertEqual(len(traces), 1)
            self.assertEqual(len(traces[0]['source_properties']), 2)
            self.assertEqual(len(traces[0]['output_occurrences']), 2)
            self.assertEqual(traces[0]['output_occurrences'][0]['line'], 2)


if __name__ == '__main__':
    unittest.main()
