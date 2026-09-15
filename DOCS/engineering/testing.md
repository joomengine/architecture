---
title: Validation and conformance testing
description: Behavioral boundaries, property checks, adversarial cases, source audits, and the separation between tests and proofs.
section: Engineering
order: 72
evidence: Test methodology
---
# Validation and conformance testing

## Test contracts, not anecdotes

A conformance suite should encode general behavior boundaries: identity isolation, closure, conflict detection, ordering, preservation, and failure semantics. A regression test can use a particular example, but its assertion should state the general contract it protects rather than memorialize one accidental implementation detail.

## Core synthesis checks

Test that repeated requests do not duplicate acquisition, reachable cycles terminate under stable identity, unknown required requests fail, and equal definitions can support distinct occurrence contexts. Test that zero-length values remain present values and that incompatible writers produce a conflict.

For finite positive rules, check extensivity, idempotence, and monotonicity over small generated domains. Compare results under permutations of rule order. The mathematical proof establishes the general bounded result; tests check that the implementation matches the specified machine on exercised inputs.

## Binding and artifact checks

Test one-pass non-recursion, explicit later-stage resolution, missing terminal bindings, and map-order independence within a simultaneous pass. Include a counterexample showing that changing the order of stages can change the outcome.

Test duplicate artifact IDs, duplicate and case-folded destinations, traversal paths, absolute paths, backslashes, invalid names, and deterministic serialization. Compare outputs from independent clean runs rather than reusing the same mutable objects in one process.

## Editorial checks

Cover empty and nonempty region bodies, multiple regions, duplicate IDs, mismatched end markers, nesting, missing ends, malformed reserved prefixes, and unauthorized or unknown regions. Test the extraction-after-rendering law and no-edit stability.

Exercise three-way reconciliation when only the user changed, only the source changed, both agree, and both disagree. Deletion and region migration need explicit policies; an absent marker must not silently become permission to discard persistent content.

## Whole-system checks

A real compiler needs target syntax validation, installation or activation checks, application behavior tests, and cross-file consistency checks. Fragment tests alone cannot prove the generated application correct.

A round-trip JCB audit should use a disposable installation, record the model and generated baseline, edit only designated regions, recompile, and compare both recovered records and final files. Test moved surrounding code and ambiguous fingerprints separately. This live audit was not substituted by the Python reference tests.

## Publication checks

The site build validates metadata and internal links. The publication checker verifies that each article has an HTML page, an exact Markdown alternate, a matching source digest, and valid local destinations. Browser checks exercise math, diagrams, navigation, search, mobile layout, and system/manual theme behavior.

The CI artifacts retain the actual check reports. This article specifies what is tested; it does not hardcode a permanent passing test count that would become stale as the suite changes.

## Reporting a result

Report the input, implementation revision, environment, command, result, and limitations. “All tests passed” means the executed suite passed, not that every proposition about every possible implementation has been proved. A failing counterexample is valuable research evidence and should lead to a corrected assumption, implementation, or claim.
