---
title: Application to code generation
description: Reusing domain definitions across target languages while preserving context, typed bindings, and admitted custom behavior.
section: Applications
order: 80
evidence: Proposed application
---
# Application to code generation

## A language-independent compiler plan

Consider a service description containing entities, fields, permissions, and operations. A VDMT implementation can gather the entity graph, resolve referenced types, derive target-specific names and validation rules, and emit schemas, server handlers, clients, and documentation. PHP is one possible target, not a requirement.

The source context should distinguish a domain fact such as “email is required” from its representation in a particular target. A database constraint, a browser validation hint, and an API schema property are separate projections of that fact. Reusing the domain fact prevents redundant acquisition; it does not remove the need to validate each target projection.

## Definitions and occurrences

An `Address` definition may occur as a customer's billing address and a supplier's contact address. The type can be shared, while nullability, authorization, serialization name, and lifecycle belong to the occurrence. A cache keyed only by `Address` would be incorrect if it retained an occurrence-specific rendering.

Use the identity model from [definition and occurrence identity](../mechanisms/occurrence-identity.md). Interpret definitions against explicit contexts, then plan artifacts from those interpretations rather than allowing arbitrary code fragments to decide their own destinations.

## Staged representations

A useful progression is domain facts → validated semantic model → target-specific intermediate representation → artifact plan → serialized output. String templates can implement the last stages, but an AST emitter can provide stronger guarantees against identifier capture and malformed syntax.

The theory does not require that all stages share one representation. A typed relation can become an AST node and later a string, provided the transformation and provenance are clear. Late-bound imports should be derived from actual dependency usage, not from a global list that happens to work in one example.

## Preserving developer adaptations

Two strategies are compatible with VDMT. Keep custom logic in separate source-owned extension modules and reference them from generated code; or use the [round-trip profile](../mechanisms/round-trip.md) to recover explicitly marked regions. The first avoids parsing generated files; the second accommodates an IDE workflow in which the output is also an editing surface.

Neither strategy should promise to preserve arbitrary unmarked edits. A domain-specific semantic merge is an additional capability, not an automatic consequence of the framework.

## Verification

Parse every generated target, check cross-file symbol resolution, validate schemas, and exercise behavior. Compare a clean build with an incremental build after changing a shared definition and an occurrence override separately. Test that the same source model can target two languages without leaking one target's names or syntax into the other.

A successful cross-language implementation would support portability of the contracts. It would not establish that one language is universally faster or that every code-generation workload benefits from the same caching policy.
