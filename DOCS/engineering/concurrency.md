---
title: Concurrency and parallelization
description: Which operations can commute, where mutable context blocks parallelism, and how to preserve deterministic output order.
section: Engineering
order: 74
evidence: Formal deductions and proposed implementation contract
---
# Concurrency and parallelization

## Parallelism follows dependencies, not class boundaries

Separate classes do not imply independent operations. Two services may write the same registry, read a changing global target, or append to the same ordered string. Parallelizing them without a dependency model can change the generated program.

The sufficient commutation conditions in [confluence](../semantics/confluence.md) require disjoint writes and no cross read/write dependencies, unless shared writes use a suitable merge algebra. Hidden effects invalidate that reasoning.

## Safe opportunities

Independent source requests can be acquired concurrently when the source snapshot and authority are fixed. Independent occurrence interpretations can run in parallel when their context is explicit and base definitions are immutable. Separate artifact renders can run concurrently when each has its own binding environment and destination.

Shared positive facts can be accumulated with an associative, commutative, idempotent merge when conflicts are represented or rejected consistently. A distributed implementation must additionally handle delivery, retries, and failure recovery; the algebra alone does not provide a network protocol.

## Ordered output

Text concatenation is not commutative. Collect contributions with stable ordering keys and render after sorting. A worker's completion time should not become the order of declarations, imports, fields, or document sections.

If contributions can have equal order keys, define a secondary key or a conflict. A merely stable sort does not fix nondeterminism in the original arrival order of equal keys.

## JCB-specific caution

The inspected file writer updates shared `ContentOne.FILENAME` for each file. Field retrieval can update stored data using view names. These are concrete examples of context-bearing mutation that a parallel reimplementation must isolate or synchronize. [J07](../reference/bibliography.md#j07), [J09](../reference/bibliography.md#j09)

The paper does not recommend running those methods concurrently unchanged. A safer design passes an immutable shared environment plus a per-file overlay and uses separate occurrence values rather than mutating a shared definition object.

## Phase barriers

A barrier can make a stratum authoritative before a later aggregate or absence test runs. Barriers cost latency, but removing them without another correctness mechanism can make fallbacks depend on timing.

A demand-driven scheduler can reduce unnecessary barriers if it tracks complete dependencies and knows when each requested result is closed. That is a stronger scheduler contract, not a free optimization.

## Measurement

Measure acquisition, derivation, binding, and writing separately. If output I/O dominates, accelerating registry lookup may have little effect on total time. If a shared mutable stage remains serial, adding workers elsewhere can increase memory use without proportional speedup.

Compare parallel and serial artifact manifests under the same input before reporting a throughput improvement. Record peak memory and error behavior as well as elapsed time. Parallelization is valuable only when it preserves the intended semantics and resource constraints.
