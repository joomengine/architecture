---
title: Build measurements and cost structure
description: Repeated self-build measurements, input/output accounting, acquisition and generation costs, and the practical resource tradeoffs of retained state.
section: Engineering
order: 82
evidence: Maintainer build record, compiler timing boundary, and pinned repository inventories
---
# Build measurements and cost structure

In repeated JCB self-builds, an exported blueprint of approximately **30,000 lines** has produced an application of **more than one million lines** in approximately **60–64 seconds** on the demonstrated setup. These are measurements from the maintainer's repeated builds and demonstrations. The architecture uses compiler rules, templates, reusable Power classes, and other supplied material in addition to the project blueprint.

The measurement describes compilation and assembly of the application. It does not imply that every reusable class body is newly authored during that interval. Reuse and coordinated placement are part of the work being measured.

## The timing boundary includes preparation

The inspected compiler starts its timer before initialization and inherited content preparation. The successful path stops it after final file processing, language and metadata work, repository-output handling, archives, and completion notices. The timer therefore does not measure only the last placeholder pass. [C01](../reference/source-map.md#c01)

The exact environment, enabled options, dependency state, and output size determine an individual run. The maintained approximate measurement is not assigned retrospectively to every revision or every machine. A reproducible run record fixes those values alongside the input blueprint and output inventory.

The [edition record](../reference/edition.md) identifies the maintainer's measurement as an engineering record and the source-derived timer boundary as a separate observation.

## Output size and blueprint size answer different questions

The pinned official source snapshot contains 1,014,391 physical UTF-8 text lines under the inventory rule used for this edition. Of those, 484,477 are outside its top-level `libraries` directory. This inventory describes the repository snapshot, not the exact timed build's counter or a claim about manually typed source.

The application layers outside the library collection are generated through JCB's blueprint-driven process. The library collection includes supplied reusable implementation, including much of the compiler's own service code. JCB's self-build coordinates those inputs into the delivered application. [Regeneration and self-build](regeneration.md)

Hello World's smaller example separately contains 1,298 physical payload JSON lines and 32,988 physical text lines across its three product repositories. Its indexes, descriptions, assets, and supplied libraries are counted explicitly. [Accounting](../examples/accounting.md)

Neither ratio is a standalone measure of correctness or labor. The ratios describe how much implementation is materialized from compact represented intent and reusable generation knowledge.

## A useful cost decomposition

For an invocation, write

$$
T_{\mathrm{build}}=T_{\mathrm{acquire}}+T_{\mathrm{normalize}}
+T_{\mathrm{interpret}}+T_{\mathrm{defer}}+T_{\mathrm{bind}}
+T_{\mathrm{write}}+T_{\mathrm{package}}+T_{\mathrm{effects}}.
$$

Acquisition includes database and configured repository work. Interpretation processes contextual occurrences and their contributions. Deferred completion handles selected later operations. Binding depends on replacement-map order, content size, and introduced text. Writing and packaging depend on the artifact volume and filesystem/archive operations. Effects include the active hooks and selected integrations.

The terms can overlap in implementation timing; the decomposition names responsibilities for measurement rather than asserting that each has already been separately profiled.

## Reuse reduces particular repeated costs

A cached definition can avoid repeated database acquisition. A cached repository index can serve many identity requests. A per-view contribution guard can avoid duplicate scripts. Retained schema or alias information can feed several emitters without being rediscovered independently.

If $n$ uses share a base acquisition of cost $a$ and each requires contextual interpretation cost $j_i$, acquisition reuse changes the corresponding idealized cost from

$$
\sum_{i=1}^{n}(a+j_i)
\quad\text{to}\quad
 a+\sum_{i=1}^{n}j_i,
$$

apart from lookup and retention overhead. It does not remove the distinct contextual work represented by $j_i$.

The actual benefit depends on the workload. Retaining a value that is cheap to recompute but very large can cost more memory than it saves time. The architecture makes that tradeoff visible through distinct store lifetimes.

## Binding and output impose their own bounds

Ordered replacement can scan intermediate strings several times. A map with $m$ relevant entries over content of size $b$ can involve work proportional to repeated scans, with intermediate expansion affecting the actual cost. Original-input filtering changes which entries are processed but also has its own presence-check cost.

Materializing $B$ output bytes requires at least $\Omega(B)$ byte-transfer work in a model that charges for written bytes. No cache removes the cost of actually producing the requested artifact set. Archive compression, copied assets, and filesystem behavior can dominate particular builds.

Peak memory includes acquired definitions, contextual contributions, pending work, active content, and temporary copies. Measuring it requires the host process and actual build options, not only the blueprint size.

## A reproducible measurement record

A concrete record should identify the blueprint revision, compiler revision, target, templates and reusable dependencies, host versions and resource limits, enabled hooks/integrations, local-versus-remote acquisition state, elapsed-time boundary, peak memory, and output selection rule. Repeated runs should retain their individual observations rather than only the fastest one.

Cold and warm dependency conditions are different workloads. A build that imports missing definitions from repositories should not be compared silently with one whose complete graph is already local. Correctness-equivalent output is required when comparing alternative implementations.

This procedure extends the maintained build record; it does not recast those existing measurements as a hypothetical future capability.

## The architectural performance result

JCB's approach spends work on interpreting structured intent and reusing established implementation knowledge, then writes the complete native products. Its resource requirements follow those conventional acquisition, transformation, and output operations. The useful engineering question is which repeated work is eliminated, which contextual work remains necessary, and how the retained state affects time and memory.

That account is more actionable than an unqualified “fast generator” label. It tells an implementer where to measure, what can be reused safely, and which costs follow from the requested output itself.
