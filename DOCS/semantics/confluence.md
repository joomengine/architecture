---
title: Confluence and scheduling
description: Schedule-independent positive saturation, conflicting writes, ordered accumulation, and safe operation commutation.
section: Semantics
order: 25
evidence: Formal deductions
---
# Confluence and scheduling

## Same result is not the same as the same execution order

A deterministic scheduler can force one repeatable outcome even when alternative schedules would produce different results. Confluence is stronger: admissible executions from the same state can reach a common result. For terminating executions, a unique normal form is the relevant practical consequence.

A registry pipeline that always executes methods in the same order may be deterministic without being confluent. Renaming it a dataflow engine does not change that fact.

## Proposition 5 — schedule-independent positive saturation

Let there be finitely many monotone, inflationary rule operators on a finite consistent fact domain. Suppose a worklist execution is fair: every rule that remains capable of adding a fact is eventually evaluated. Continue until all rules are quiescent. Then the resulting fact set is the least common closed superset of the seed, independent of the fair schedule.

**Proof.** Every transition adds facts, so strict growth is finite. Every intermediate state is contained in any common closed superset of the seed, by induction and monotonicity. Fairness and quiescence imply that the final state is itself closed under every rule. It is therefore the least such set and is unique. $\square$

The worklist must terminate after detecting quiescence; a scheduler that endlessly re-evaluates rules which add nothing is not a terminating implementation merely because its fact set has stabilized.

## Conflicting writes

Two rules that write different strings to the same key do not satisfy the consistent-domain premise. Possible policies include rejecting the conflict, retaining alternatives in a lattice, choosing an explicitly prioritized writer, or combining contributions with a defined operation.

A last-writer-wins map tied to execution timing is not schedule-independent. A priority policy can restore determinism, but priority must be part of the semantics rather than an accident of service construction order.

## Ordered accumulation

Set union is associative, commutative, and idempotent. String concatenation is associative but not commutative. Appending fragments as workers finish can produce different programs.

To parallelize ordered output, collect pairs $(o,f)$, where $o$ is a stable ordering key, then sort and concatenate once. Duplicate ordering keys with incompatible fragments are conflicts. This preserves the intended semantics without assuming that text concatenation behaves like a set join.

## Independence criterion

For two operations $a$ and $b$, let $R_a,W_a,R_b,W_b$ be their read and write footprints. Disjoint writes and absence of cross read/write dependencies are sufficient for commutation when the operations are deterministic and have no hidden effects:

$$
W_a\cap W_b=\varnothing,\quad W_a\cap R_b=\varnothing,\quad W_b\cap R_a=\varnothing.
$$

These conditions are sufficient, not necessary. Shared writes may also commute under a suitable merge algebra. A runtime that does not know the footprints cannot safely infer independence from separate class names.

## Implication for VDMT

VDMT does not require all operations to commute. It requires the implementation to distinguish a dependency-mandated order from an order chosen only for execution convenience. That distinction is what allows later parallelization without changing meaning.

See [concurrency](../engineering/concurrency.md), [binding stages](../mechanisms/binding-stages.md), and [related work](../foundations/related-work.md).
