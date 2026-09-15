"""General behavior-boundary tests for the original reference model. MIT."""
import itertools
import unittest
from reference.vdmt import Artifact, ContractError, Conflict, Fact, Knowledge, MissingBinding, MissingRequest, Resolution, Rule, artifact_map, bind, extract_regions, gather, manifest, put_regions, reconcile, saturate, validate_path
from examples.demo import build, demonstration


class KnowledgeTests(unittest.TestCase):
    def test_empty_value_is_present(self):
        self.assertEqual(Knowledge([Fact(('k',), '')]).get(('k',)), '')

    def test_absent_fails(self):
        with self.assertRaises(MissingRequest):
            Knowledge().get(('k',))

    def test_scopes_are_distinct(self):
        knowledge = Knowledge([Fact(('A', 'label'), 'one'), Fact(('B', 'label'), 'two')])
        self.assertEqual(len(knowledge.facts()), 2)

    def test_conflicting_batch_is_atomic(self):
        knowledge = Knowledge([Fact(('x',), 'a')])
        with self.assertRaises(Conflict):
            knowledge.extend([Fact(('new',), 'b'), Fact(('x',), 'bad')])
        self.assertEqual(knowledge.facts(), frozenset([Fact(('x',), 'a')]))

    def test_invalid_fact_type(self):
        with self.assertRaises(ContractError):
            Fact(('x',), None)

    def test_duplicate_assignment_is_noop(self):
        fact = Fact(('x',), 'a')
        self.assertFalse(Knowledge([fact]).extend([fact]))


class ClosureTests(unittest.TestCase):
    def setUp(self):
        self.a, self.b, self.c = (Fact((key,), 'yes') for key in ('a', 'b', 'c'))
        self.rules = [Rule('ab', (self.a,), (self.b,)), Rule('bc', (self.b,), (self.c,))]

    def test_nested_gathering(self):
        source = {'a': Resolution((self.a,), ('b',)), 'b': Resolution((self.b,), ('c',)), 'c': Resolution((self.c,))}
        self.assertEqual(gather(['a'], source).facts, frozenset((self.a, self.b, self.c)))

    def test_request_cycle_and_duplicates(self):
        source = {'a': Resolution((self.a,), ('b', 'b')), 'b': Resolution((self.b,), ('a',))}
        self.assertEqual(gather(['a', 'a'], source).completed, ('a', 'b'))

    def test_missing_dependency(self):
        with self.assertRaises(MissingRequest):
            gather(['a'], {'a': Resolution((), ('missing',))})

    def test_extensivity_and_idempotence(self):
        result = saturate([self.a], self.rules)
        self.assertIn(self.a, result)
        self.assertEqual(result, saturate(result, self.rules))

    def test_monotonicity_over_small_domain(self):
        facts = (self.a, self.b, self.c)
        subsets = [frozenset(combo) for size in range(4) for combo in itertools.combinations(facts, size)]
        for left in subsets:
            for right in subsets:
                if left <= right:
                    self.assertLessEqual(saturate(left, self.rules), saturate(right, self.rules))

    def test_rule_order_does_not_change_closure(self):
        results = [saturate([self.a], list(order)) for order in itertools.permutations(self.rules)]
        self.assertTrue(all(result == results[0] for result in results))

    def test_positive_rule_cycle(self):
        rules = self.rules + [Rule('ca', (self.c,), (self.a,))]
        self.assertEqual(len(saturate([self.a], rules)), 3)

    def test_conflicting_consequence(self):
        with self.assertRaises(Conflict):
            saturate([self.a], [Rule('bad', (self.a,), (Fact(('a',), 'no'),))])

    def test_duplicate_rule_names(self):
        with self.assertRaises(ContractError):
            saturate([], [self.rules[0], self.rules[0]])


class BindingTests(unittest.TestCase):
    def test_stages(self):
        self.assertEqual(bind('{{A}}', [{'A': '{{B}}'}, {'B': 'done'}]), 'done')

    def test_one_pass_is_not_recursive(self):
        with self.assertRaises(MissingBinding):
            bind('{{A}}', [{'A': '{{B}}', 'B': 'done'}])

    def test_map_order_is_irrelevant(self):
        self.assertEqual(bind('{{A}} {{B}}', [{'B': '2', 'A': '1'}]), bind('{{A}} {{B}}', [{'A': '1', 'B': '2'}]))

    def test_missing_terminal_binding(self):
        with self.assertRaises(MissingBinding):
            bind('{{MISSING}}', [])

    def test_empty_binding_is_valid(self):
        self.assertEqual(bind('{{EMPTY}}', [{'EMPTY': ''}]), '')

    def test_wrong_stage_order_fails(self):
        with self.assertRaises(MissingBinding):
            bind('{{A}}', [{'B': 'done'}, {'A': '{{B}}'}])


class EditorialTests(unittest.TestCase):
    template = 'before\n<!-- VDMT:BEGIN a -->\ndefault\n<!-- VDMT:END a -->\nafter\n'

    def test_get_put_law(self):
        for value in ('', 'changed\n', 'Unicode: λ and é\n', 'first\nsecond\n'):
            self.assertEqual(extract_regions(put_regions(self.template, {'a': value})), {'a': value})

    def test_multiple_regions(self):
        text = self.template + '<!-- VDMT:BEGIN b -->\n<!-- VDMT:END b -->\n'
        memory = {'a': 'one\n', 'b': 'two\n'}
        self.assertEqual(extract_regions(put_regions(text, memory)), memory)

    def test_no_edit_stability(self):
        original = extract_regions(self.template)
        self.assertEqual(reconcile(original, original, extract_regions(put_regions(self.template, original))), original)

    def test_malformed_markers(self):
        cases = [self.template.replace('END a', 'END b'), self.template.replace('<!-- VDMT:END a -->\n', ''),
                 self.template + self.template, '<!-- VDMT:BEGIN a -->\n<!-- VDMT:BEGIN b -->\n',
                 'prefix <!-- VDMT:BEGIN a -->\n', '<!-- VDMT:WRONG a -->\n', '<!-- VDMT:END a -->\n']
        for text in cases:
            with self.subTest(text=text), self.assertRaises(ContractError):
                extract_regions(text)

    def test_reject_body_without_lf(self):
        with self.assertRaises(ContractError):
            put_regions(self.template, {'a': 'no newline'})

    def test_reject_marker_in_body(self):
        with self.assertRaises(ContractError):
            put_regions(self.template, {'a': '<!-- VDMT:BEGIN evil -->\n'})

    def test_domain_mismatch(self):
        with self.assertRaises(ContractError):
            put_regions(self.template, {})

    def test_three_way_cases(self):
        self.assertEqual(reconcile({'a': 'old'}, {'a': 'old'}, {'a': 'user'}), {'a': 'user'})
        self.assertEqual(reconcile({'a': 'old'}, {'a': 'source'}, {'a': 'old'}), {'a': 'source'})
        self.assertEqual(reconcile({'a': 'old'}, {'a': 'same'}, {'a': 'same'}), {'a': 'same'})
        with self.assertRaises(Conflict):
            reconcile({'a': 'old'}, {'a': 'source'}, {'a': 'user'})

    def test_region_migration_is_explicit(self):
        with self.assertRaises(Conflict):
            reconcile({'a': 'x'}, {'b': 'x'}, {'a': 'x'})


class ArtifactTests(unittest.TestCase):
    def test_invalid_portable_paths(self):
        for path in ('../x', '/x', 'a//b', 'a/./b', 'a\\b', 'C:/x', 'a/CON.txt', 'a/b.', 'a/b ', 'a\x00b', 'cafe\u0301.txt'):
            with self.subTest(path=path), self.assertRaises(ContractError):
                validate_path(path)

    def test_valid_path(self):
        self.assertEqual(validate_path('component/view/file.txt'), 'component/view/file.txt')

    def test_destination_collision(self):
        with self.assertRaises(Conflict):
            artifact_map([Artifact('one', 'A.txt', 'x'), Artifact('two', 'a.txt', 'x')])

    def test_identity_collision(self):
        with self.assertRaises(Conflict):
            artifact_map([Artifact('same', 'a.txt', 'x'), Artifact('same', 'b.txt', 'y')])

    def test_manifest_is_canonical(self):
        self.assertEqual(manifest({'b': '2', 'a': '1'}), manifest({'a': '1', 'b': '2'}))

    def test_demo_counts_and_round_trip(self):
        result = demonstration()
        self.assertEqual(result['counts'], {'requests': 9, 'field_definitions': 3, 'field_occurrences': 8, 'view_occurrences': 3, 'artifacts': 18})
        self.assertTrue(result['round_trip_preserved'])

    def test_independent_builds_match(self):
        self.assertEqual(build()[0], build()[0])


if __name__ == '__main__':
    unittest.main()
