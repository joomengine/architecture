---
title: Intermediate stores and information lifecycle
description: Definition caches, concern-specific builders, dispensers, binding environments, and deferred work as different kinds of retained state.
section: Compiler
order: 33
evidence: Registry abstraction, builder services, ContentOne, ContentMulti, and Dispenser
---
# Intermediate stores and information lifecycle

JCB retains information in several kinds of intermediate store. Their physical representations often use arrays or registry services, but their architectural responsibilities differ. Understanding those responsibilities explains what is remembered, how it is addressed, and why it remains available to a later consumer.

A shared map is useful because it connects producers and consumers. A complete explanation must additionally name the value's origin, scope, update operation, readiness, and lifetime. [C02](../reference/source-map.md#c02), [C06](../reference/source-map.md#c06)

## A taxonomy of retained state

| Store role | Typical retained value | Why it is retained |
| --- | --- | --- |
| Definition cache | Acquired field, view, or Power data | Avoid repeated acquisition and preserve identity |
| Concern-specific builder | Schema properties, searchable fields, language requirements, aliases, or method contributions | Collect information for a later generator |
| Contextual code dispenser | Prepared custom code indexed by role and use-site | Delay retrieval-time binding until the correct context exists |
| Output-binding environment | Shared and view/extension-specific placeholder values | Supply a defined stage of file materialization |
| Deferred-work collection | Operation identity and arguments | Complete work after other contributions become available |
| Processing state | Attempted requests, per-view contribution guards, loaded-state flags | Prevent repeated work or recursive re-entry |

These roles can coexist in one build. They should not be collapsed into a universal cache or a single undifferentiated “memory.” The same implementation type can serve different roles, and a role can be implemented by another data structure in a different language.

## Keys express the intended scope

Some stores use a definition ID or GUID. Others use a view name, extension key, target area, field name, or a combination. `ContentOne` models shared content keys as placeholder keys. `ContentMulti` separates a view or extension scope from the placeholder name through its key convention.

This permits a shared component binding and a view-specific method fragment to be retrieved differently even if both are ultimately inserted into text. A schema field list and an output placeholder map are also distinct: one describes what must be rendered, while the other supplies already prepared material to a binding stage. [C06](../reference/source-map.md#c06)

For a store $M_s$, write its address space as $K_s$ and its value space as $V_s$:

$$
M_s:K_s\rightharpoonup V_s.
$$

The partial function means an address may not yet have a value. It does not prescribe physical memory addresses, heap allocation, or a particular registry library.

## Updates are not all monotone accumulation

The registry abstraction supports operations such as setting, getting with a default, checking existence, removing values, and adding content according to the configured operation. Builders can append members or concatenate fragments; other consumers replace bindings as they move to another file or context.

For example, file content processing sets the current filename binding before handling a file. That is an intentional state change associated with the current artifact. It is not a newly discovered immutable fact that should remain true for every later file.

Consequently, an accurate state model includes replacement and removal as well as accumulation. A finite monotone closure model can describe a bounded dependency set, but it cannot by itself describe every production registry update. [Formal state](../formal/state.md)

## Readiness belongs to the producer-consumer relationship

A value can be present without being ready for every possible use. A prepared custom-code fragment can still contain context-sensitive placeholders. A partial aggregate can exist before all of its member contributions have been processed. A recursive load guard can be present while its definition is still being prepared.

The relevant condition is

$$
\operatorname{ready}(v,o,\Sigma),
$$

meaning that value $v$ is ready for operation $o$ in state $\Sigma$. JCB often enforces readiness through the sequence of calls and phases rather than attaching an explicit readiness type to every stored value.

The [deferred-work chapter](deferred-work.md) shows the case where that sequence is made especially visible: work is retained precisely because its consumers' prerequisites are not yet complete.

## Retrieval can perform interpretation

The dispenser retrieves code under active placeholders, adds requested surrounding text, and can remove an entry after use. A field loader can perform per-view code processing when returning a cached field. Retrieval is therefore sometimes an operation, not merely a raw map lookup. [C04](../reference/source-map.md#c04), [C09](../reference/source-map.md#c09)

This behaviour explains the recollection analogy in ordinary engineering terms. The system retains an identified representation, then recalls and interprets it when a particular consumer needs it. No claim about biological memory is needed to describe that useful separation.

## Lifetime and shared services

The service container ensures that the relevant producers and consumers share instances during the build. Per-build definitions, guards, bindings, and aggregates should be understood within that lifecycle. Reusing a compiler container across independent build configurations requires the reset discipline of the calling workflow; otherwise, target selection and retained state can outlive their intended context.

A portable implementation can choose explicit context objects and build-owned store collections instead. It still needs the same answers: who writes a value, who reads it, which key identifies it, when it becomes authoritative for that consumer, and when it is replaced or discarded.

Intermediate stores make the coordination economical. They also consume memory and create ordering obligations. The [cost account](../engineering/performance.md) and [implementation guide](../engineering/implementation.md) examine those tradeoffs without assuming that retaining every value is always preferable.
