---
title: Vast Development Method Theory
description: A language-independent account of contextual recollection, staged synthesis, and persistent editorial reconciliation.
section: Overview
order: 0
evidence: Formal framework
---
# Vast Development Method Theory

## From structured knowledge to reproducible artifacts

**Vast Development Method Theory (VDMT)** is a formal architectural framework for systems that repeatedly ask what information a task requires, recollect that information in context, derive further usable structure, and assemble consistent artifacts without losing explicitly preserved human adaptations.

Its central object is not a string template or a PHP registry. It is a **versioned configuration of knowledge, dependencies, contexts, derivations, artifact plans, and editorial memory**. Registries, databases, typed maps, graph stores, and files are possible representations of that configuration.

The framework separates three activities that are often conflated:

1. **Recollection:** resolve a request against an identified source snapshot, including requests discovered while resolving earlier requests.
2. **Synthesis:** derive context-specific facts and fragments, then bind and materialize them according to an explicit dependency and phase order.
3. **Reconciliation:** recover authorized, marked changes from existing artifacts and preserve them as input to the next synthesis epoch.

The first two operate within a build. The third connects builds. An implementation may realize only part of this framework; conformance must name the part it implements.

## The defining insight

A reusable definition does not need to be rediscovered independently for every place it is used. It can be recollected by stable identity, interpreted in a particular occurrence context, and projected into several destinations. Equally, a generated artifact need not be a disposable endpoint: designated regions can become a controlled source of future knowledge.

This yields a compact description:

> **Complete the context; derive within scope; bind in stages; materialize deliberately; reconcile only what has an explicit identity and preservation contract.**

The contribution of this paper is to specify that composition, its assumptions, and its reusable contracts. It does not claim to have invented fixed points, dependency graphs, template substitution, or bidirectional transformations. [Related work](foundations/related-work.md) explains those relationships.

## Read at the right depth

The [white paper](white-paper.md) gives the argument, central equations, and conclusions in one article. The [definition](foundations/definition.md) specifies the architectural boundary. The [state model](semantics/state-space.md), [closure semantics](semantics/context-closure.md), and [round-trip laws](mechanisms/round-trip.md) provide the mathematical foundation. The [implementation guide](engineering/implementation-guide.md) translates the contracts into a language-independent design.

[Joomla Component Builder](jcb/overview.md) is the originating implementation examined in the case study. Its public compiler source records the method's implementation from **30 January 2016**. That provenance is documented after the theory, rather than making Joomla knowledge a prerequisite for understanding it.

## What is established, and what remains a research question?

The paper distinguishes source observations, historical records, author testimony, formal deductions, proposed extensions, and hypotheses. The finite monotone model has provable closure and determinism properties under stated assumptions. Those proofs are not automatically proofs about every extension hook or mutation in an existing production system.

The broader suggestion that the architecture resembles human recollection is developed as a testable research direction. It is not a conclusion that software registries are biological memory, or that a fast generator implements human understanding.

**Originator:** Llewellyn van der Merwe. **Publisher:** Vast Development Method. **Edition:** 0.1.0, 15 September 2026. [Citation and rights](reference/citation.md).
