---
title: Reading guide
description: Routes from a concrete generated field to the compiler architecture, its mathematics, and its implementation in another language.
section: Overview
order: 2
evidence: Publication guide
---
# Reading guide

The publication can be read as a white paper, an architectural reference, or a worked investigation. All three routes meet at the same object: the transformation of structured development intent into a coordinated set of application artifacts.

## Begin with a visible result

Read the [Hello World overview](examples/hello-world.md), then the [Greeting field trace](examples/field-trace.md). A compact field definition and its view association explain the generated column, form input, language entries, list features, and table metadata. The distinction between a definition and its use becomes visible before it is formalised.

Continue with [custom-code markers](examples/custom-code-trace.md) and [module/plugin generation](examples/extension-trace.md). These traces show how stored code, contextual names, component relationships, and extension-specific emitters participate in the same build.

The [accounting chapter](examples/accounting.md) identifies exactly what belongs to the blueprint, what belongs to its repository description, and what belongs to the generated products. It is useful when reading any size or expansion figure.

## Read the continuous white paper

The [white paper](white-paper.md) is the main narrative. Its chapters introduce the model, follow the lifecycle, explain the compiler's coordinating mechanisms, and derive the mathematical account from those mechanisms. Follow its links when a particular operation needs more detail.

No knowledge of Joomla class names is required for the main argument. The glossary defines the few product terms retained because they identify specific JCB concepts: *Power*, *Dynamic Get*, *Infusion*, *blueprint*, and *extrusion*. [Glossary](reference/glossary.md)

## Understand the implementation architecture

Start with [structured intent](foundations/structured-intent.md), [identity](foundations/identity.md), and [context](foundations/context.md). Then read [compiler execution](compiler/execution.md) in order. Initialization, data acquisition, content preparation, file updating, and packaging have separate responsibilities; work performed while constructing the compiler must be included in the trace.

The core sequence is [acquisition](compiler/acquisition.md), [classification](compiler/classification.md), [stores](compiler/stores.md), [deferred work](compiler/deferred-work.md), and [binding](compiler/binding.md). Read the generation chapters alongside this sequence to see which accumulated information feeds schemas, queries, forms, permissions, languages, routing, and extension packaging.

[Target selection](compiler/targets.md) separates the Joomla installation hosting JCB from the Joomla generation targeted by the output. [Events](compiler/events.md) describes extension hooks as part of execution rather than invisible background behaviour.

## Follow portable definitions and recovered structure

The blueprint chapters explain [representation](blueprints/representation.md), [discovery](blueprints/discovery.md), [dependency traversal](blueprints/dependencies.md), [export](blueprints/export.md), [import and reset](blueprints/import.md), and [assets and repositories](blueprints/assets.md).

Read [extrusion](extrusion/overview.md) after that sequence. An exported blueprint explicitly carries JCB definitions; an installed extension carries artifacts from which particular definitions can be recovered. Their import paths share a destination but do not have identical information content or correctness conditions.

## Read or implement the mathematics

Begin with [notation](formal/notation.md) and the [state model](formal/state.md). The remaining formal articles cover [resolution](formal/resolution.md), [classification](formal/classification.md), [staging](formal/staging.md), and [transport equivalence](formal/transport.md).

Each mathematical construction has an operational meaning. A graph edge identifies a dependency or relationship; a context selects the interpretation of a use; a store update records a particular kind of contribution; a transition changes a specified part of build state. A proposition states its assumptions before deriving its conclusion.

The [implementation guide](engineering/implementation.md) and [executable reference mechanisms](engineering/reference-model.md) turn that account into a practical starting point. They use a small vocabulary rather than attempting to reproduce every Joomla emitter.

## Check a statement against its source

The [source map](reference/source-map.md) groups the implementation paths by responsibility. The [edition record](reference/edition.md) identifies the inspected revisions and the integrated capability scope. The [bibliography](reference/bibliography.md) credits the established work used to describe related mechanisms.

A source trace, a recorded build measurement, and a proof about a stated mathematical model answer different questions. The publication identifies which one is being used without requiring the reader to interrupt the architectural explanation at every paragraph.
