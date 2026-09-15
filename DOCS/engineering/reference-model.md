---
title: Executable reference mechanisms
description: Small executable models of typed resolution, precedence, contextual contributions, deferred work, ordered binding, and transport observations.
section: Engineering
order: 81
evidence: Executable examples and unit tests shipped with this publication
---
# Executable reference mechanisms

The publication includes a small executable companion to the mathematics. It isolates mechanisms that can be tested without installing Joomla: typed request identity, local-first dependency traversal, property precedence, contextual field contributions, deferred prerequisites, ordered placeholder replacement, and normalized transport observations.

The implementation lives in `reference/architecture.py`. The demonstration lives in `examples/demo.py`, and the tests live in `tests/test_architecture.py`. Python is used as an executable notation for the companion; the white paper's definitions do not depend on Python.

## Run the companion

From the repository root:

```bash
python -m unittest discover -s tests -v
python examples/demo.py
```

The demonstration prints structured results so that the selected identities, outputs, and stage decisions can be inspected. It performs no network access, executes no imported application code, and requires no credentials.

## Resolution examples

A request includes entity type, identifying field, and value. The example resolver preserves a local record under initialization, otherwise searches an ordered repository collection, records attempt and outcome state, and follows represented dependencies.

Tests cover a shared dependency, a cycle, a missing request, local-first behavior, and a selected repository entry whose payload is invalid. The last case verifies that index selection and payload fallback are separate policies.

The purpose is to make the [termination argument](../formal/resolution.md) concrete. Visiting a request once bounds repeated acquisition; it does not convert a failed request into a resolved definition.

## Classification examples

A small field model distinguishes reusable database/form properties from occurrence roles such as title, search, and sorting. Its interpretation produces schema, form, language, and list-related observations.

The Greeting case retains database width 255 and form maximum 50 and derives an ordinary index from the title role despite an explicit-index value of zero. The executable result mirrors the branch explained in the [field trace](../examples/field-trace.md), not every possible JCB field type.

Additional tests change the occurrence context to check that context-qualified names and roles change at the intended boundary while the portable field identity remains stable.

## Ordered binding examples

The replacement function implements ordinary ordered replacement, the presence-check action, and original-input map filtering. Tests exercise introduced tokens, reversed map order, unknown tokens, and a replacement that contains its own key.

For the map `A → B`, `B → x`, ordinary replacement of `A` gives `x`, while original-input filtering gives `B`. This small distinction is important enough to test directly because a superficially similar substitution algorithm would produce different generated text. [Formal staging](../formal/staging.md)

## Deferred work and property precedence

The companion represents deferred work with named prerequisites and a retained operation. It rejects execution before those prerequisites are available and records the result after they are supplied. This exposes the readiness relation that JCB's selected phase boundaries establish operationally.

The precedence helper selects usable property values by configured tier rank and a stable default tie-break. Zero and false are retained as meaningful values; only the declared missing-value cases are excluded. Tests distinguish configured rank from the order in which candidates happen to be iterated. [Extrusion analysis](../extrusion/analysis.md)

## Representation observations

Transport tests compare a declared portable projection while allowing local record IDs to differ. They also ensure that ordered associations remain ordered and that differing represented design values are not discarded by normalization.

The companion's normalization is deliberately small and explicit. It must not be mistaken for a complete implementation of every JCB entity's export mapper. Its role is to test the mathematical distinction between design equivalence and raw record equality. [Formal transport](../formal/transport.md)

## What these tests establish

The tests establish behavior of the companion code and the worked mechanisms it implements. Source references separately establish JCB's corresponding responsibilities. Repository inventories establish the observed public artifacts. A full Joomla build exercises another, larger boundary.

Keeping those boundaries distinct makes the companion useful rather than inflated: another engineer can run and modify a small model, inspect the actual compiler paths, and decide how to represent the same mechanism in a different technology.
