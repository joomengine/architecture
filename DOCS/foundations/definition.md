---
title: Formal definition and scope
description: The minimum commitments of VDMT and the distinction between core synthesis, round-trip, and self-generative profiles.
section: Foundations
order: 10
evidence: Formal model
---
# Formal definition and scope

## Definition

**Vast Development Method Theory** describes a family of computational architectures in which an identified task induces a context of recollected and derived information; that context is completed through bounded dependency discovery, distributed into explicitly scoped intermediate representations, and materialized through an ordered binding plan. In its round-trip profile, designated edits to the resulting artifacts are reconciled into persistent source state for subsequent synthesis epochs.

“Memory” denotes the logical availability, identity, provenance, and lifecycle of information. It does not prescribe a physical allocator, a cache hierarchy, or a particular database. “Recollection” means resolving a context-qualified request from a source snapshot or already established knowledge. It need not involve approximate similarity, learning, or a neural representation.

The framework's technical descriptor is **context-closed staged synthesis with persistent editorial reconciliation**. VDMT remains the proper name; the descriptor enables comparison with established terminology.

## Architectural commitments

A core implementation must expose the following contracts, whether through distinct classes or a single well-specified program:

* An explicit build input and source epoch, including configuration that can affect output.
* Stable definition identity and distinguishable occurrence context.
* Dependency discovery with a documented stopping or failure rule.
* Scoped recollection and derivation stores with defined conflict semantics.
* A phase-ordered binding and artifact-planning process.
* A defined output-equivalence relation and a reproducibility contract.

These commitments identify an inspectable method, not a performance guarantee. A one-pass renderer may be a degenerate instance of staged synthesis but does not demonstrate the characteristic dependency-completion and contextual-reuse behavior. An implementation should not advertise the richer VDMT profile merely because it holds values in a dictionary.

## Profiles

**Core synthesis profile.** Implements the six contracts above. Existing outputs are not authoritative input. The formal development first treats this profile because its state can be isolated within one epoch.

**Round-trip profile.** Adds artifact identities, an admissible edit language, extraction, persistence, conflict detection, and reinsertion laws. Only marked or otherwise explicitly owned edits are covered. An unrestricted inverse of generated output is neither required nor generally possible.

**Self-generative profile.** Can describe and regenerate an identified subset of its own implementation or host application using the same source-to-artifact contracts. Its claim must identify the subset, the seed implementation, and the comparison procedure. This profile does not imply that the implementation compiles the host language itself.

**Incremental profile.** Adds dependency-complete invalidation and demonstrates equivalence to a clean rebuild. It is an extension, not an assumption about every JCB registry.

These are proposed conformance profiles of this specification. They are not historical names used by JCB and not externally accredited certifications.

## The two-loop distinction

Let $K_t$ be the knowledge available at step $t$ within one build, and $D_e$ the durable source state at epoch $e$. The inner computation expands $K_t$ until the required context is complete. The outer computation may change $D_e$ when admissible edits are recovered from prior artifacts. Thus the inner relation can be monotone even while the outer evolution permits deletion or replacement.

This separation is essential. Without it, a proof that adds facts within a frozen snapshot might be incorrectly applied to a process that overwrites source records while it runs.

## Exclusions

VDMT does not require PHP, Joomla, strings as its intermediate representation, a universal global registry, a particular number of passes, or a database as its only durable medium. It does not assert that every task benefits from eager context loading. It does not equate deterministic behavior with semantic correctness or scientific truth.

The principal inherited mathematical tools are fixed-point semantics and compositional reasoning. The principal related engineering traditions are staged compilation, dataflow, incremental build systems, and bidirectional transformations. Their authors are credited in [related work](related-work.md) and the [bibliography](../reference/bibliography.md).
