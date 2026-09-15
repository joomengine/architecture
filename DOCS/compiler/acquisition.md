---
title: Acquiring and enriching the application model
description: Nested loading, reusable definition caches, occurrence-specific processing, and the transition from stored records to compiler-ready data.
section: Compiler
order: 31
evidence: Component data, model enrichment, admin-view and field services
---
# Acquiring and enriching the application model

The database representation is not already arranged in the form required by every generator. Component records refer to child configurations and views; views refer to fields and query definitions; fields refer to types, rules, and custom behaviour. Acquisition follows those relationships and enriches the records into forms that the compiler can use.

JCB combines root queries, nested loading, reusable definition caches, normalization, history processing, and conditional remote retrieval. The result is a contextual application model, not merely a list of rows copied from the database. [C03](../reference/source-map.md#c03), [C04](../reference/source-map.md#c04)

## Root acquisition and enrichment

The component-data service loads the selected component together with related configuration and then applies a sequence of modeling operations. These establish identity and naming information, version and history state, files and libraries, admin and site view relationships, custom code, configuration, update material, modules, plugins, and routing choices.

The sequence matters. A component's selected admin views determine field-related and generated-table work that later operations consume. Module and plugin relationships determine which additional extension data and structures must be prepared. Code fields may need decoding and custom-code processing before they can be retained for later use.

The enriched model is stored through the component service. Consumers can retrieve its established properties without repeating the original joined acquisition for every output fragment. This is reuse at the component-data boundary, not a claim that all subsequent interpretation is context-free.

## A view association is more than a view identifier

An association identifies the reused view and carries the settings of its use in the component. The view's own settings in turn identify its field associations, conditions, relations, tabs, scripts, and other behaviour.

This nested organization lets common definitions remain reusable while particular uses supply their own roles. It also means the acquisition graph and the occurrence structure must not be confused. Loading a field definition once can be correct even when the compiler still needs to process that field under several view contexts. [Identity](../foundations/identity.md)

## Field data separates base identity from contextual consequences

The field loader supports lookup by ID or GUID and maintains an index connecting both forms to an acquired field object. When a valid GUID cannot be found locally, a guarded package-retrieval attempt can populate the local data and allow a retry.

The retrieved field is enriched with its field-type information, decoded XML, validation-rule handling, storage treatment, history, and other compiler settings. Subsequent retrieval also invokes field-specific custom-code handling with the current single and list view names. [C04](../reference/source-map.md#c04)

The distinction is important: the cached object is not a frozen, completely context-free semantic value. The implementation can update and interpret it as part of retrieval. Its architecture is better represented as a reusable base definition plus controlled contextual processing than as a pure memoized function of the field GUID alone.

A language-neutral decomposition is

$$
d=\operatorname{loadBase}(u),\qquad
(d',c)=\operatorname{prepareUse}(d,\Gamma),
$$

where $c$ contains any additional contributions and $d'$ the prepared representation used by the next stage. Whether $d'$ shares physical storage with $d$ is an implementation choice that must be understood when reasoning about mutation.

## Guards distinguish repeated work from repeated meaning

Field custom-code processing records which field scripts have already contributed to a view. It also tracks decoding and prepares scripts through the dispenser. Those guards avoid duplicate contributions while still permitting the same field to participate in another view.

Power acquisition similarly has load-state guards around recursive references. Package acquisition has attempt guards and queues. These mechanisms share a purpose—controlling repeated work—but have different keys and lifetimes. One cannot infer their exact semantics from the word *cache* alone. [Stores](stores.md), [Powers](powers.md)

For a reusable operation $f$, the cache key must cover the inputs whose changes can alter $f$'s result. For an effectful operation that adds scripts or language entries, the guard must also match the intended contribution scope. The [classification model](../formal/classification.md) separates those cases.

## Absence can trigger work

A missing local definition is sometimes an instruction to acquire it, rather than an immediate terminal failure. A missing derived value can trigger preparation or a default. A missing optional feature can mean no contribution should be generated. These are different interpretations of absence.

The source's guards and branch conditions determine which case applies. For example, a remote field retry is limited by identity and attempt state. A configuration default is selected by a different path. The formal model uses distinct transitions instead of treating every missing value as a single generic recollection operation.

## The acquisition boundary remains open where the implementation requires it

Some dependencies become visible only while processing code, templates, or Power references later in compilation. The architecture therefore does not require one universal acquisition pass that resolves every possible dependency before output preparation begins.

The practical rule is narrower: a consumer must obtain the information it actually requires at the point its operation uses that information. Early acquisition and shared caches reduce repeated work; late discovery handles dependencies exposed by later interpretation. [Deferred work](deferred-work.md), [Binding](binding.md)

The [source map](../reference/source-map.md) links these responsibilities to their services. The next chapter follows acquired definitions into the concern-specific contributions that constitute the compiler's central semantic work.
