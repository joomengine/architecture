---
title: Termination and bounded recursion
description: Separate stopping arguments for discovery, derivation, occurrence expansion, token substitution, and repeated builds.
section: Semantics
order: 26
evidence: Formal deductions and implementation obligations
---
# Termination and bounded recursion

## There is no single universal stopping argument

A compiler can contain several loops with different measures of progress. The fact that a database query returns finitely many rows does not establish termination of recursive dependency loading, template expansion, external code, or an installed plugin.

The useful question is: **what well-founded measure changes for this loop?** A strict decrease in a natural-number measure, or ascent in a finite-height information order, gives a usable argument under the relevant assumptions.

## Discovery

For a stable finite request graph with completed-set suppression, the number of uncompleted reachable requests decreases after each productive visit. Cycles such as $a\to b\to a$ do not prevent termination. Failure to include scope or revision in identity can nevertheless make the returned context wrong.

A request generator producing a new key at every step defeats the bound. An implementation must impose a finite domain, a decreasing structural rank, or a limit that returns a clearly reported failure.

## Positive derivation

The [finite closure proof](fixed-points.md) bounds strict fact-growth rounds. The cost of checking rules remains separate. Finite-height lattices generalize the same argument, while infinite domains may require widening or other approximation techniques with their own soundness obligations. Such techniques are not asserted to be present in JCB.

## Hierarchical occurrence expansion

A finite definition graph can induce infinitely many occurrences when a recursive definition keeps instantiating itself. Sharing the definition does not bound the expanded tree.

For an acyclic occurrence grammar, topological depth supplies a bound. For recursive grammars, require an explicit depth, a decreasing parameter, or a finite set of admissible occurrence identities. Report an expansion cycle rather than silently discarding a needed occurrence.

## Binding and rewriting

One-pass substitution over a finite string and finite replacement map terminates. Repeating substitution until no token remains can fail when a replacement regenerates itself or another token in a cycle.

A staged system can instead assign token families to a finite sequence of phases. Each phase performs a non-recursive pass, then validates its contract. A stricter recursive resolver may use a token-dependency graph and reject cycles. The chosen semantics must be documented; “replace placeholders” does not specify it sufficiently.

## Editorial recovery

Parsing a finite file terminates if the parser advances through its input. Malformed or nested markers may still make the result ambiguous. Termination is not correctness. Extraction should reject ambiguous regions and avoid partial persistence unless explicitly supported.

## The outer lifecycle

Repeated builds are intentional, externally initiated epochs. The lifecycle need not converge when humans keep editing the input. A no-edit stability law concerns repeated synthesis from unchanged input, not the eventual end of all future development.

## Limits as failure semantics

Depth, time, memory, request-count, and output-size limits are operational protections. A timeout is not a mathematical proof that no solution exists. A successful bounded run is not a proof that every future input terminates. Expose the limit reached and retain enough provenance to diagnose it.

[Security](../engineering/security.md) discusses these bounds as defense against accidental and adversarial expansion.
