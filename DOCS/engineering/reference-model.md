---
title: Executable reference model
description: The deliberately bounded Python model, its supported laws, its example, and its differences from JCB.
section: Engineering
order: 71
evidence: Original reference implementation
---
# Executable reference model

## Purpose and scope

The repository includes an original Python reference model in `reference/vdmt.py`, a runnable example in `examples/demo.py`, and unit tests in `tests/`. It makes the central contracts executable without requiring Joomla, PHP, a database server, or network access.

The model is intentionally bounded. It is not a port of JCB, does not include upstream GPL compiler code, and does not claim production equivalence with JCB's placeholder or custom-code syntax.

## Supported operations

The model represents immutable, scoped facts with string values. A knowledge store rejects incompatible assignments to one key. A finite request graph is traversed with duplicate suppression and explicit failure for an unknown required request.

Positive rules have fixed premises and finite fixed consequences. Saturation can therefore be tested against the finite closure laws without pretending arbitrary user callbacks are monotone. Rule and request ordering is canonical for reproducible traces.

The binding operation uses a finite sequence of non-recursive token-substitution passes. Unknown required tokens at the end are errors. This differs deliberately from PHP's ordered array `str_replace` semantics in the inspected JCB implementation.

The editorial model recognizes an explicitly reserved, line-oriented region grammar. It rejects duplicate, nested, unmatched, or malformed markers. Rendering requires a complete region map and preserves admitted bodies; a three-way whole-region reconciler returns a conflict when source and user changes disagree.

Artifact helpers validate portable relative paths, logical identities, and destination collisions before constructing a deterministic artifact map. They do not implement a distributed transaction or prove target-program correctness.

## Run the example

```bash
python examples/demo.py
python -m unittest discover -s tests -v
```

The example uses shared field/type/view definitions in two components, expands them into context-specific occurrences, and renders singleton and per-view artifacts. It then changes one admitted editorial region, extracts it, and rebuilds with the recovered value. Its JSON output identifies the generated artifacts and preservation result.

These are synthetic demonstration inputs. Their counts and timings must not be presented as the author's reported million-line JCB build.

## Relationship to the mathematics

Request traversal corresponds to the stable-resolver case in [context closure](../semantics/context-closure.md). Positive saturation corresponds to [Propositions 1–3](../semantics/fixed-points.md). Schedule variations test examples of the [confluence conditions](../semantics/confluence.md), but passing tests is not a replacement for the proof.

The region grammar supplies concrete admissibility conditions for [Proposition 7](../mechanisms/round-trip.md). It uses LF line endings and reserves its marker prefix so that an arbitrary body cannot accidentally become a new region boundary.

## Deliberate omissions

There is no generic parser for arbitrary source languages, no automatic semantic merge, no complete incremental invalidation engine, no neural memory, and no self-hosting PHP compiler. Persistence adapters, authorization, atomic deployment, and rich provenance are interfaces for a real implementation to supply.

These omissions keep the example's claims precise. A small executable model is useful when it demonstrates the contracts clearly; it becomes misleading when it is described as proof that a much larger production runtime satisfies every assumption.
