"""Behavioral boundaries of the executable architectural mechanisms. MIT."""
from copy import deepcopy
from itertools import permutations
import json
import unittest
from reference.architecture import (
    Contribution, Definition, DeferredWork, EntityKey, FieldDefinition, FieldUse,
    PrerequisiteError, Repository, apply_contributions, classify_field,
    complete_deferred, ordered_replace, portable_projection, resolve_graph,
    select_property,
)


class IdentityAndResolutionTests(unittest.TestCase):
    def setUp(self):
        self.a = EntityKey("view", "guid", "a")
        self.b = EntityKey("field", "guid", "b")
        self.c = EntityKey("fieldtype", "guid", "c")

    def test_type_and_key_are_part_of_identity(self):
        self.assertNotEqual(self.a, EntityKey("field", "guid", "a"))
        self.assertNotEqual(self.a, EntityKey("view", "name", "a"))

    def test_alias_identity_does_not_require_a_guid(self):
        self.assertEqual(EntityKey("custom_code", "function_name", "readMEcontributors").value,
                         "readMEcontributors")

    def test_identity_rejects_missing_or_unnormalized_parts(self):
        for args in (("", "guid", "a"), ("field", "", "a"), ("field", "guid", " a")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                EntityKey(*args)

    def test_shared_dependency_is_attempted_once(self):
        repo = Repository("r", {self.a: Definition(self.a, {}, (self.b, self.c)),
                                self.b: Definition(self.b, {}, (self.c,)),
                                self.c: Definition(self.c, {})})
        result, local = resolve_graph([self.a, self.b], {}, [repo])
        self.assertTrue(result.successful)
        self.assertEqual(len(result.attempted), 3)
        self.assertEqual(set(local), {self.a, self.b, self.c})

    def test_cycle_terminates_without_losing_definition(self):
        repo = Repository("r", {self.a: Definition(self.a, {}, (self.b,)),
                                self.b: Definition(self.b, {}, (self.a,))})
        result, _ = resolve_graph([self.a], {}, [repo])
        self.assertEqual(result.attempted, [self.a, self.b])
        self.assertTrue(result.successful)

    def test_missing_dependency_is_not_success(self):
        repo = Repository("r", {self.a: Definition(self.a, {}, (self.b,))})
        result, _ = resolve_graph([self.a], {}, [repo])
        self.assertIn(self.a, result.resolved)
        self.assertIn(self.b, result.failures)
        self.assertFalse(result.successful)

    def test_local_first_preserves_local_edits(self):
        old = {self.a: Definition(self.a, {"label": "local"})}
        repo = Repository("remote", {self.a: Definition(self.a, {"label": "remote"})})
        result, local = resolve_graph([self.a], old, [repo])
        self.assertEqual(local[self.a].properties["label"], "local")
        self.assertEqual(result.origins[self.a], "local")

    def test_local_completeness_is_a_separate_premise(self):
        local = {self.a: Definition(self.a, {}, (self.b,))}
        result, _ = resolve_graph([self.a], local, [])
        self.assertTrue(result.successful)
        self.assertNotIn(self.b, result.attempted)
        result, _ = resolve_graph([self.a], local, [], inspect_local_dependencies=True)
        self.assertIn(self.b, result.failures)

    def test_first_index_match_does_not_hide_a_failed_payload(self):
        bad = Repository("first", {self.a: None})
        good = Repository("later", {self.a: Definition(self.a, {})})
        result, local = resolve_graph([self.a], {}, [bad, good])
        self.assertIn("first", result.failures[self.a])
        self.assertNotIn(self.a, local)

    def test_payload_identity_must_match_request(self):
        result, _ = resolve_graph([self.a], {}, [Repository("r", {self.a: Definition(self.b, {})})])
        self.assertFalse(result.successful)

    def test_duplicate_failed_requests_do_not_repeat_attempts(self):
        result, _ = resolve_graph([self.a, self.a, self.a], {}, [])
        self.assertEqual(result.attempted, [self.a])

    def test_inputs_are_not_mutated_or_aliased(self):
        source = Definition(self.a, {"nested": [1]})
        repo = Repository("r", {self.a: source})
        result, local = resolve_graph([self.a], {}, [repo])
        local[self.a].properties["nested"].append(2)
        self.assertEqual(source.properties["nested"], [1])
        self.assertEqual(result.origins[self.a], "r")


class PrecedenceTests(unittest.TestCase):
    def test_default_precedence_retains_origin(self):
        self.assertEqual(select_property({"xml": "x", "table": "t", "derived": "d"}), ("t", "table"))

    def test_missing_values_do_not_shadow_useful_values(self):
        self.assertEqual(select_property({"table": None, "notes": "", "xml": "x"}), ("x", "xml"))

    def test_zero_and_false_are_values(self):
        self.assertEqual(select_property({"table": 0, "xml": 10}), (0, "table"))
        self.assertEqual(select_property({"table": False, "xml": True}), (False, "table"))

    def test_configured_priority_overrides_defaults(self):
        self.assertEqual(select_property({"table": "t", "xml": "x"}, {"xml": -1}), ("x", "xml"))

    def test_ties_are_stable_under_candidate_permutation(self):
        values = {"table": "t", "notes": "n", "xml": "x", "derived": "d"}
        for order in permutations(values):
            result = select_property({key: values[key] for key in order}, {key: 0 for key in values})
            self.assertEqual(result, ("t", "table"))

    def test_absent_candidates_and_bad_tiers(self):
        self.assertIsNone(select_property({"xml": ""}))
        with self.assertRaises(ValueError):
            select_property({"unknown": 1})
        with self.assertRaises(TypeError):
            select_property({"xml": 1}, {"xml": True})


class ContributionTests(unittest.TestCase):
    def test_ordered_overwrites_are_not_commutative(self):
        a, b = Contribution("s", "k", "set", 1), Contribution("s", "k", "set", 2)
        self.assertNotEqual(apply_contributions({}, [a, b]), apply_contributions({}, [b, a]))

    def test_append_preserves_multiplicity(self):
        c = Contribution("s", "k", "append", "x")
        self.assertEqual(apply_contributions({}, [c, c])["s"]["k"], ["x", "x"])

    def test_fill_does_not_replace_false_or_zero(self):
        for value in (0, False, ""):
            self.assertEqual(apply_contributions({"s": {"k": value}},
                [Contribution("s", "k", "fill", 7)])["s"]["k"], value)

    def test_removal_and_concatenation(self):
        result = apply_contributions({"s": {"old": 1}}, [Contribution("s", "old", "remove"),
            Contribution("s", "code", "concat", "a"), Contribution("s", "code", "concat", "b")])
        self.assertEqual(result, {"s": {"code": "ab"}})

    def test_typed_operations_reject_wrong_values(self):
        for initial, contribution in [({"s": {"k": "text"}}, Contribution("s", "k", "append", 1)),
                                     ({}, Contribution("s", "k", "concat", 1))]:
            with self.assertRaises(TypeError):
                apply_contributions(initial, [contribution])
        with self.assertRaises(ValueError):
            apply_contributions({}, [Contribution("s", "k", "unknown")])

    def test_disjoint_contributions_commute(self):
        a, b = Contribution("s", "a", "set", 1), Contribution("s", "b", "set", 2)
        self.assertEqual(apply_contributions({}, [a, b]), apply_contributions({}, [b, a]))

    def test_input_memory_is_unchanged(self):
        initial = {"s": {"k": [1]}}
        before = deepcopy(initial)
        apply_contributions(initial, [Contribution("s", "k", "append", 2)])
        self.assertEqual(initial, before)


class FieldProjectionTests(unittest.TestCase):
    def setUp(self):
        self.field = FieldDefinition(EntityKey("field", "guid", "greeting-id"), "greeting", "Greeting")

    def project(self, **kwargs):
        return apply_contributions({}, classify_field(self.field, FieldUse("helloworld", "greeting", **kwargs)))

    def test_title_derives_index_without_explicit_index(self):
        self.assertEqual(self.project(title=True)["schemas"]["helloworld.greeting.greeting"]["key"], "ordinary")
        self.assertEqual(self.project()["schemas"]["helloworld.greeting.greeting"]["key"], "none")

    def test_database_length_and_form_maximum_are_distinct(self):
        result = self.project(title=True)
        key = "helloworld.greeting.greeting"
        self.assertEqual(result["schemas"][key]["type"], "VARCHAR(255)")
        self.assertEqual(result["forms"][key]["maxlength"], 50)
        label = result["forms"][key]["label"]
        self.assertEqual(result["languages"][label], "Greeting")

    def test_unique_index_takes_precedence_over_title(self):
        definition = FieldDefinition(self.field.identity, "greeting", "Greeting", explicit_index=1)
        result = apply_contributions({}, classify_field(definition, FieldUse("hello", "view", title=True)))
        self.assertEqual(result["schemas"]["hello.view.greeting"]["key"], "unique")

    def test_text_family_does_not_take_ordinary_length_or_key(self):
        definition = FieldDefinition(self.field.identity, "greeting", "Greeting", datatype="TEXT", explicit_index=2)
        result = apply_contributions({}, classify_field(definition, FieldUse("hello", "view", title=True)))
        self.assertEqual(result["schemas"]["hello.view.greeting"]["type"], "TEXT")
        self.assertEqual(result["schemas"]["hello.view.greeting"]["key"], "none")

    def test_nonpersistent_field_keeps_form_without_schema(self):
        result = self.project(persist=False)
        self.assertIn("forms", result)
        self.assertNotIn("schemas", result)

    def test_occurrences_get_distinct_contextual_labels(self):
        first = self.project()
        other = apply_contributions({}, classify_field(self.field, FieldUse("other", "view")))
        self.assertNotEqual(set(first["languages"]), set(other["languages"]))
        self.assertEqual(first["metadata"]["helloworld.greeting.greeting"]["identity"],
                         other["metadata"]["other.view.greeting"]["identity"])

    def test_search_and_sort_are_separate_contributions(self):
        result = self.project(searchable=True)
        self.assertIn("search", result)
        self.assertNotIn("sorting", result)


class BindingAndStagingTests(unittest.TestCase):
    def test_introduced_tokens_and_original_input_filter(self):
        pairs = [("A", "B"), ("B", "x")]
        self.assertEqual(ordered_replace("A", pairs), "x")
        self.assertEqual(ordered_replace("A", pairs, 3), "B")
        self.assertEqual(ordered_replace("A B", pairs, 3), "x x")

    def test_order_changes_result(self):
        self.assertEqual(ordered_replace("A", [("B", "x"), ("A", "B")]), "B")

    def test_unknown_tokens_are_not_removed(self):
        self.assertEqual(ordered_replace("UNKNOWN A", [("A", "x")], 3), "UNKNOWN x")

    def test_replacement_does_not_repeat_its_own_key(self):
        self.assertEqual(ordered_replace("A", [("A", "AA")]), "AA")

    def test_presence_check_and_empty_map(self):
        self.assertEqual(ordered_replace("nothing", [("A", "B")], 2), "nothing")
        self.assertEqual(ordered_replace("A", [], 3), "A")

    def test_replacement_validation(self):
        with self.assertRaises(ValueError):
            ordered_replace("A", [("", "B")])
        for action in (0, 4, True):
            with self.subTest(action=action), self.assertRaises(ValueError):
                ordered_replace("A", [("A", "B")], action)

    def test_deferred_work_requires_ready_inputs(self):
        work = DeferredWork("result", frozenset({"name"}), lambda state: state["name"].upper())
        with self.assertRaises(PrerequisiteError):
            complete_deferred([work], {})
        self.assertEqual(complete_deferred([work], {"name": "view"})["result"], "VIEW")

    def test_deferred_sequence_can_consume_earlier_results(self):
        a = DeferredWork("a", frozenset({"seed"}), lambda state: state["seed"] + 1)
        b = DeferredWork("b", frozenset({"a"}), lambda state: state["a"] * 2)
        self.assertEqual(complete_deferred([a, b], {"seed": 2})["b"], 6)
        with self.assertRaises(PrerequisiteError):
            complete_deferred([b, a], {"seed": 2})


class TransportTests(unittest.TestCase):
    def test_local_ids_can_differ_under_declared_projection(self):
        first = {"id": 1, "guid": "stable", "fields": ["a", "b"]}
        second = {"id": 99, "guid": "stable", "fields": ["a", "b"]}
        self.assertEqual(portable_projection(first, ["guid", "fields"]),
                         portable_projection(second, ["guid", "fields"]))

    def test_serialization_preserves_selected_design(self):
        source = {"guid": "stable", "fields": [{"id": "a", "nullable": False}, {"id": "b", "length": 0}]}
        projected = portable_projection(source, ["guid", "fields"])
        self.assertEqual(json.loads(json.dumps(projected)), projected)

    def test_association_order_is_not_discarded(self):
        self.assertNotEqual(portable_projection({"fields": ["a", "b"]}, ["fields"]),
                            portable_projection({"fields": ["b", "a"]}, ["fields"]))

    def test_missing_or_duplicate_design_properties_fail(self):
        with self.assertRaises(ValueError):
            portable_projection({}, ["guid"])
        with self.assertRaises(ValueError):
            portable_projection({"guid": "a"}, ["guid", "guid"])


if __name__ == "__main__":
    unittest.main()
