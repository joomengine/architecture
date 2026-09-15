"""Offline source preparation and path/content integrity checks. MIT."""
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from scripts.prepare_evidence import CONTRACT, fingerprint, prepare, unpack
from scripts.research_inventory import inventory


def archive(entries):
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode='w:gz') as stream:
        for name, content in entries:
            item = tarfile.TarInfo(name)
            item.size = len(content)
            stream.addfile(item, io.BytesIO(content))
    return output.getvalue()


class EvidenceTests(unittest.TestCase):
    def test_archive_is_read_as_data_under_one_root(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / 'source'
            unpack(archive([('repo/a.txt', b'one\n'), ('repo/sub/b.bin', b'\0x')]), target)
            self.assertEqual((target / 'a.txt').read_bytes(), b'one\n')
            self.assertEqual((target / 'sub/b.bin').read_bytes(), b'\0x')

    def test_traversal_absolute_and_duplicate_paths_are_rejected(self):
        cases = [[('repo/../outside', b'x')], [('/absolute', b'x')],
                 [('repo/a', b'x'), ('repo/a', b'y')],
                 [('repo/a', b'x'), ('other/b', b'y')]]
        for entries in cases:
            with self.subTest(entries=entries), tempfile.TemporaryDirectory() as temporary:
                with self.assertRaises(ValueError):
                    unpack(archive(entries), Path(temporary) / 'source')

    def test_empty_archive_is_not_an_accepted_source(self):
        with tempfile.TemporaryDirectory() as temporary, self.assertRaises(ValueError):
            unpack(archive([]), Path(temporary) / 'source')

    def test_fingerprint_is_independent_of_listing_order(self):
        a = {'path': 'a', 'sha256': 'first'}
        b = {'path': 'b', 'sha256': 'second'}
        self.assertEqual(fingerprint({'files': [a, b]}), fingerprint({'files': [b, a]}))
        self.assertNotEqual(fingerprint({'files': [a]}), fingerprint({'files': [b]}))

    def test_pinned_contract_is_complete_and_distinguishes_payloads(self):
        contract = json.loads(CONTRACT.read_text())
        self.assertEqual(len(contract['repositories']), 4)
        for record in contract['repositories'].values():
            self.assertRegex(record['revision'], r'^[0-9a-f]{40}$')
            self.assertRegex(record['file_inventory_sha256'], r'^[0-9a-f]{64}$')
            all_counts = record['totals']['all']
            for metric in all_counts:
                self.assertEqual(all_counts[metric], sum(value[metric] for key, value in record['totals'].items() if key != 'all'))
        self.assertEqual(contract['repositories']['hello-blueprint']['totals']['payload']['files'], 33)

    def test_existing_checkout_must_match_the_complete_contract(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'sample'
            source.mkdir()
            (source / 'one.txt').write_text('original\n')
            report = inventory(source)
            contract = {'blueprint': 'absent', 'repositories': {'sample': {
                'repository': 'owner/repo', 'revision': 'a' * 40,
                'file_inventory_sha256': fingerprint(report), 'totals': report['totals']}}}
            # Empty blueprint selection is not used in the publication; only exercise integrity failure here.
            (source / 'one.txt').write_text('changed\n')
            with self.assertRaisesRegex(ValueError, 'fingerprint'):
                prepare(contract, root, download=False)


if __name__ == '__main__':
    unittest.main()
