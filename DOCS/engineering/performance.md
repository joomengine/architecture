---
title: Cost model and performance hypotheses
description: Acquisition, derivation, binding, output size, live memory, reuse thresholds, and why no universal optimum follows from the architecture.
section: Engineering
order: 75
evidence: Analytical model and empirical hypotheses
---
# Cost model and performance hypotheses

## Decompose the cost

For one build, use

$$
T=T_{\mathrm{acquire}}+T_{\mathrm{discover}}+T_{\mathrm{derive}}+T_{\mathrm{plan}}+T_{\mathrm{bind}}+T_{\mathrm{write}}+T_{\mathrm{validate}}+T_{\mathrm{package}}.
$$

This is accounting, not a universal asymptotic theorem. The terms depend on source latency, value sizes, rule behavior, output expansion, target validation, and the implementation's representation choices.

Let $N$ be reachable definition count, $E$ dependency edges, $O$ occurrence count, $F$ artifact count, and $B$ total emitted bytes. A stable indexed request traversal has expected bookkeeping cost $O(N+E)$, excluding acquisition and payload processing. Occurrence interpretation can cost at least proportional to the occurrences actually needed. Materialization requires $\Omega(B)$ work in a byte-charging model.

## Where reuse can help

A naive design may acquire or interpret the same definition separately for every occurrence. A scoped design can acquire the definition once per revision and repeat only the context-dependent work.

For one reusable computation, let $r$ be reuse count, $c$ recomputation cost, $l$ lookup cost, and $s$ storage/invalidation overhead. A simplified reuse benefit condition is

$$
(r-1)c > rl+s.
$$

The expression assumes the cached result is valid and includes no hidden context-dependent recomputation. It is a decision aid, not a proof that caching every value is beneficial.

## Binding complexity

A renderer that scans a file once for each of $P$ replacement keys may incur work on the order of $P$ times the evolving string length. A token-aware single-pass renderer can have different costs, but must preserve the intended replacement semantics.

JCB's `str_replace` behavior and presence filtering cannot be replaced by a different algorithm solely on the basis of a better asymptotic expression. First establish semantic equivalence on nested tokens, ordering, and late bindings. [J08](../reference/bibliography.md#j08)

## Memory cost

Peak live memory is the sum of live source objects, occurrence values, fragment buffers, plans, output buffers, caches, and runtime overhead. Logical reuse does not imply physical sharing. Large strings may be duplicated across stores or retained longer than necessary.

Useful measurements include peak resident memory, allocated bytes, number and size of live registry values, cache hit/miss counts, and release points. Streaming emission can reduce output-buffer memory but may complicate late binding and whole-artifact validation.

## Expansion is not compression alone

If a relatively small database produces a large codebase, the output also contains information from templates, rules, framework conventions, copied assets, and reusable libraries. The database is not the only input. Generated line count is therefore an expansion measure, not a measure of newly reasoned knowledge or manually authored effort.

## What “optimal” would require

An optimality claim needs a workload class, admissible algorithms, resource model, correctness constraint, and objective. A system minimizing latency may use more memory; one minimizing memory may repeat acquisition. There may be a Pareto frontier rather than one best design.

VDMT provides contracts that make these tradeoffs inspectable. It does not presently establish a universal optimum for software memory or human recollection. The [hypothesis program](../research/hypotheses.md) proposes comparisons that could support narrower claims.
