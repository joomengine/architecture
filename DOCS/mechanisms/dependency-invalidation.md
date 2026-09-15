---
title: Dependency invalidation and incremental builds
description: How changed sources invalidate derived knowledge, and the conditions under which an incremental rebuild equals a clean rebuild.
section: Mechanisms
order: 38
evidence: Proposed extension and formal deductions
---
# Dependency invalidation and incremental builds

## Reuse across epochs is a stronger claim

Reusing a value within one frozen build is simpler than reusing it after the source has changed. A cross-epoch cache needs a dependency record that includes source data, transformation versions, templates, configuration, target version, editorial overlays, and relevant external inputs.

A cache key that omits an input can produce a stable but stale answer. Repeatedly obtaining the same wrong output is not useful determinism.

## Dependency graph

Let $x\to y$ mean that $y$ depends on $x$. For changed inputs $\Delta$, a conservative affected set is

$$
\operatorname{affected}(\Delta)=\operatorname{reachable}^{+}(\Delta).
$$

Recompute affected values in a dependency-respecting order or by a valid closure procedure. Reuse unaffected values only if their dependency identities and transformation revisions remain unchanged.

## Deletion and alternative derivations

Positive closure adds facts within an epoch. Source deletion between epochs can invalidate facts, so it is not an inflationary transition in the same information order.

A fact may have more than one derivation. Removing one supporting input need not make the fact false if another complete derivation still exists. A conservative algorithm can invalidate and recompute the entire affected region. A more precise truth-maintenance approach tracks alternative justifications. It must not simply delete all descendants and assume none can be rederived.

## Proposition 8 — incremental equivalence

Assume complete dependency tracking, deterministic derivations, correct identification of changed inputs, recomputation of every affected value to the same closure as a clean build, and reuse only of unaffected values. Then the incremental result equals the clean result under the same output equivalence.

**Proof.** Unaffected values have unchanged complete inputs and therefore unchanged results. By assumption, affected values are recomputed to their clean-build results. Their union is the clean final store; deterministic planning and rendering then yield equivalent artifacts. $\square$

The difficult engineering premise is dependency completeness. The proposition is not evidence that a cache already satisfies it.

## Granularity

Fine-grained dependencies reduce unnecessary recomputation but cost memory and bookkeeping. Coarse component-level invalidation is easier to make correct but may rebuild more than necessary. Both can implement VDMT. The choice belongs to a measured workload and failure-risk model.

## Relation to established build-system work

Incremental build research distinguishes dependency discovery, scheduling, and rebuilding decisions. That separation is directly useful here: VDMT's contextual discovery should not be confused with its policy for reusing previously computed outputs. [R04](../reference/bibliography.md#r04)

## JCB boundary

This article proposes a generalized incremental profile. The inspected registry and field-cache paths alone do not establish a comprehensive cross-build invalidation engine in JCB. A future claim of incremental conformance must demonstrate clean/incremental equivalence under changes to each relevant input category.
