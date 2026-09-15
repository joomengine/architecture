---
title: Architectural glossary
description: Product terms and language-neutral concepts used consistently throughout the white paper.
section: Reference
order: 93
evidence: Terminology derived from implementation roles and established computer science
---
# Architectural glossary

The terms below identify roles in the architecture. Where JCB uses a product-specific name, its general engineering meaning is given alongside it. The [notation](../formal/notation.md) supplies the mathematical symbols.

## Artifact

A generated or assembled product with a role, destination, context, content, and remaining processing stages. Files, language catalogues, supporting assets, manifests, and archives are artifacts. A file can exist before its final binding and injection stages are complete. [Materialization](../generation/materialization.md)

## Blueprint

The portable design representation: selected entity properties, typed identities, relationships, dependencies, authored code, and assets. Repository indexes and README descriptions locate or explain that design; they are counted separately from its payloads. [Representation](../blueprints/representation.md)

## Build context

The values that qualify an operation, including target, extension, view, generation role, language destination, active bindings, and occurrence settings. Runtime users and application data are a different context supplied when the generated application runs. [Context](../foundations/context.md)

## Compilation

The coordinated acquisition, interpretation, contribution, staged binding, code placement, and materialization of a represented application. The complete execution includes constructor preparation, later file updating, diagnostics, and packaging. [Execution](../compiler/execution.md)

## Contribution

A result of interpreting a definition's use: a store, key, update operation, and value. It may be schema data, a language entry, a query alias, a fragment, a requirement flag, or deferred work. Contributions are not all strings or immutable facts. [Classification](../compiler/classification.md)

## Definition

Reusable design knowledge with typed identity. A field, view, Power, template, or query definition can participate in several uses. Its identity differs from a local database row number and from a final output path. [Identity](../foundations/identity.md)

## Deferred work

An operation retained with its arguments because its required information will be ready later. JCB's selected admin replay and configuration-fieldset passes are examples. It differs from acquiring a definition lazily or binding a placeholder late. [Deferred work](../compiler/deferred-work.md)

## Dependency

A typed relationship or resource requirement exposed by an entity's schema, association, recognized embedded reference, or asset configuration. Incoming owned children and outgoing shared references can have different reset policies. [Dependency traversal](../blueprints/dependencies.md)

## Dispenser

JCB's role- and context-indexed store for prepared code. Retrieval can apply the active placeholder environment, add surrounding material, and remove consumed content. It is not merely a cache of final output strings. [Custom code](../compiler/custom-code.md)

## Dynamic Get

JCB's structured query/retrieval definition. It describes sources, selections, aliases, joins, filters, ordering, and result roles that are compiled into model code. Runtime query values remain inputs to the generated application. [Queries](../generation/queries.md)

## Extrusion

Recovery of represented model information from an existing component or class library. Discovery, static readers, precedence, identity resolution, reviewable candidates, and writers return supported structure to JCB's editable definitions. It differs from importing an explicit blueprint. [Extrusion](../extrusion/overview.md)

## GUI-linked region

A generated code region associated with a local table, property, and record address so eligible edits can be recovered. Its local numeric address is not the portable identity of the application model. [Custom-code trace](../examples/custom-code-trace.md)

## Infusion

The implementation's name for preparing and coordinating generated content. It invokes interpretation and creators, establishes shared and contextual bindings, and completes selected deferred work. The term is retained when naming the source service, not required of a reimplementation. [Execution](../compiler/execution.md)

## Initialization and reset

Initialization ordinarily preserves an acceptable local definition and acquires one where missing. Reset explicitly requests refresh; owned incoming children and referenced reusable definitions follow their respective recursive policies. These operations are not interchangeable overwrite modes. [Import](../blueprints/import.md)

## Intermediate representation

Information retained between input acquisition and final output. JCB uses structured records, specialized builders, flags, code fragments, and binding maps. Calling these intermediate representations identifies their role without attributing the structural guarantees of a typed AST or SSA system. [Stores](../compiler/stores.md)

## Occurrence

A definition's particular use under an association, placement, and context. Two views can reuse one field while assigning different roles or layout positions. The occurrence is not necessarily a separately allocated object in the implementation. [Identity](../foundations/identity.md)

## Placeholder and binding environment

A placeholder identifies text to be replaced using an applicable environment. JCB's environments and action modes have ordered replacement semantics, including original-input filtering in action 3. A binding stage is the point at which a selected environment is applied. [Binding](../compiler/binding.md)

## Power and Joomla Power

A Power is a managed reusable code definition with stable identity, dependencies, namespace, and placement behavior. A Joomla Power represents a version-sensitive platform class mapping. Both connect stable references to context-appropriate symbols, but their payloads and generation roles differ. [Powers](../compiler/powers.md)

## Recollection

An explanatory term for retrieving identified retained information when a consumer needs it, sometimes with further acquisition or contextual processing. It denotes a software operation here, not a claim about biological memory. The precise store and retrieval contract should be named whenever ambiguity matters.

## Reconciliation and recovery

Returning designated authored changes to managed design state under the implementation's identity and transformation rules. Fingerprint placement and commented fallback distinguish executable placement from recoverability. This is not a general automatic three-way merge or an inverse for arbitrary source edits. [Transport](../formal/transport.md)

## Semantic classification

Interpreting a definition in context and routing its different consequences to concern-specific consumers. It is not an ordinary sorting algorithm over comparable values. Schema, query, form, policy, language, and code-placement consequences can arise from the same occurrence. [Classification](../compiler/classification.md)

## Target

The platform and generation conventions selected for output. It differs from the host running the compiler and from the application's own version number. Target-specific emitters and Joomla Power mappings carry shared adaptation knowledge. [Targets](../compiler/targets.md)

## Trace and equivalence

A trace records an ordered sequence of operations or source-to-output correspondences. An equivalence states which observations a comparison preserves: portable design, normalized artifacts, or raw bytes. A local identity or date difference can matter to one comparison and not another, but the rule must be declared. [State](../formal/state.md), [transport](../formal/transport.md)
