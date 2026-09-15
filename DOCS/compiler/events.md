---
title: Extension hooks and observable effects
description: Events, configuration mutation, database reads, filesystem operations, and diagnostics as part of the compiler's operational semantics.
section: Compiler
order: 39
evidence: Compiler event interface and event calls in acquisition, generation, and file writing
---
# Extension hooks and observable effects

JCB exposes extension hooks around acquisition, modeling, content preparation, and file processing. They allow additional behaviour to participate at identified points in compilation. Several hooks receive mutable arguments or access shared build services.

The compiler's operational account includes those hooks. An execution diagram that follows only the built-in creators while ignoring event handlers would describe a different effective program whenever extensions are active. [C01](../reference/source-map.md#c01), [C02](../reference/source-map.md#c02)

## Hooks have a location and an effect boundary

The initializer triggers events around component acquisition. Field data exposes query and modeling events. View preparation exposes content events. Per-file processing exposes file-read and pre-write events. Each location determines which information is already available and what later consumers will observe.

A hook can alter a query before acquisition, modify an enriched definition, contribute generated content, or transform the string about to be written. Those operations have different consequences. Their place in the sequence is part of their meaning.

For an event $h$ at stage $i$, model its action as

$$
\Sigma_{i+1}=h(\Sigma_i,x_i),
$$

where $x_i$ represents any external values read by the handler. The built-in transition sequence continues from the resulting state.

## Determinism concerns the complete effective input

A fixed ordered program can be deterministic even when it mutates state. Determinism asks whether the same complete inputs and prescribed operations produce the same result. It does not ask whether every possible reordering of those operations would also produce that result.

For compiler output, the relevant input includes the selected definitions, target rules, repository responses, active event handlers, their configuration, and any environment values they are permitted to use. Dates, locale, filesystem content, or network material can be output-affecting inputs.

If a handler reads a changing external resource, that read changes the effective build input. If two runs fix the same input and handler behaviour, the ordered state transformations can still be repeatable. [Formal state](../formal/state.md), [Formal staging](../formal/staging.md)

This is a more useful description than either treating hooks as automatically nondeterministic or ignoring them when making a repeatability claim.

## Read and write sets expose dependencies

For an operation $o$, let $\operatorname{read}(o)$ and $\operatorname{write}(o)$ identify the state locations it consumes and changes. A hook that writes a view's name before classification affects the downstream keys and output. A hook that changes the final file string affects materialized bytes without necessarily changing the earlier model.

Two operations can be reordered safely only under an appropriate independence or commutation argument. Disjoint write sets alone are insufficient if one operation reads what the other writes. The [formal classification chapter](../formal/classification.md) states a sufficient noninterference condition for the small model.

The implementation commonly establishes this dependency discipline through explicit sequence. The mathematical account makes that discipline inspectable without asserting an automatic effect checker in production.

## Side effects extend beyond output files

Compilation can read and update local data, recover code, process version history, retrieve remote material, prepare folders, write generated files, synchronize configured repository locations, construct archives, and enqueue user-visible messages. Those effects are part of the lifecycle described by the paper.

A pure mathematical projection can be useful for a particular emitter, but the complete compiler is an effectful process. The [state model](../formal/state.md) therefore separates durable definitions, intermediate stores, staged artifacts, external observations, and diagnostics.

This separation also prevents an architectural mistake: interpreting a physical file write as proof that all of the file's semantic stages have completed. Skeleton files can exist before later bindings and injections are applied.

## Diagnostics preserve operational information

Warnings and errors communicate more than a final Boolean. They can identify missing definitions, failed external material, language mismatches, uncertain custom-code placement, or packaging problems. The specific path determines whether processing stops, continues with a fallback, or records an item for manual attention.

The custom-code placement fallback is a concrete example: commented recovery material plus a file/location warning carries information that would be lost in a result reduced to “success” or “failure.” [Custom code](custom-code.md)

## A portable implementation boundary

Another implementation can represent hooks as registered functions with explicit context arguments and effect permissions. It can record repository responses, external resource digests, and diagnostic events in a build trace. These are practical ways to preserve the same extension boundary and make it easier to inspect.

The publication does not require those additional records to exist in every JCB build. Its source account names the actual events and effects; its language-neutral model supplies a vocabulary for reasoning about them. The [verification chapter](../engineering/verification.md) distinguishes source correspondence, executable mechanism tests, artifact traces, and full runtime build tests.
