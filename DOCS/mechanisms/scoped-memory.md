---
title: Scoped memory and recollection
description: Logical memory, ownership, missing values, availability, and lifecycle without confusing registries with physical allocation.
section: Mechanisms
order: 30
evidence: Formal model and implementation interpretation
---
# Scoped memory and recollection

## What moves between stores?

The phrase “memory moves from one registry to another” is useful intuition but imprecise as an implementation statement. A transition can copy a value, share an object reference, derive a new representation, append a fragment, retain a key, or release a store. These operations have different costs and semantics.

VDMT's concern is the **logical movement of information between roles**. A source field becomes a validated field fact; that fact supports a view-specific interpretation; the interpretation contributes to several output fragments. The physical bytes may or may not move.

## A contextual lookup

Let a lookup be $\operatorname{get}(R,k,\Gamma,e)$. Its meaning depends on the store's kind, the key, occurrence context, and source epoch. A successful result includes a value and sufficient provenance to explain its authority.

For example, `label` under one view is not necessarily the same fact as `label` under another view. A field definition may supply a default while the occurrence supplies an override. Scope resolution must specify whether the override shadows, augments, or conflicts with the default.

## Availability is not truthiness

An empty string can be the correct emitted value for an optional section. Zero can be a valid numeric property. `false` can be an explicit instruction not to generate a feature. Treating all of these as “not found” can create unintended defaults or duplicate derivations.

The abstract lookup distinguishes absent, present, and conflict states. A separate status may indicate pending or failed acquisition. This is particularly important when a system first checks what it knows and then loads additional context.

## Store roles

A practical decomposition separates source objects, normalized facts, occurrence interpretations, fragment contributions, binding environments, artifact plans, and editorial records. These stores need not correspond one-to-one to classes. They do need documented lifetimes and write ownership.

Persistent editorial records outlive a build. Occurrence interpretations normally do not. A cache can span builds only if its keys and invalidation rules identify every relevant input revision. A service container, which locates implementation objects, is not the same thing as a semantic registry, which stores build knowledge.

## Recollection versus memoization

Recollection is the semantic act of answering a request. Memoization is one possible optimization that stores the result of a computation. A cache hit is valid only when the cached computation's input identity still matches. An eagerly loaded registry is not necessarily a cache, and a `get` method may perform context-sensitive work even when a base object is already stored.

The inspected JCB `Field\Data` illustrates this distinction: it indexes loaded fields by ID/GUID, yet `getFieldData()` also invokes contextual custom-code updating. The base object is reused, but the retrieval path is not simply a pure immutable-map lookup. [J09](../reference/bibliography.md#j09)

## Physical memory consequences

Specialized stores can avoid repeated database access and redundant derivation. They can also retain too much data, duplicate large strings, or prevent early release. An optimal physical representation cannot be inferred from the conceptual architecture alone.

A portable implementation should measure peak live bytes, value duplication, lookup counts, cache misses, and the point at which each store can be released. Those measurements belong to [performance analysis](../engineering/performance.md), not to the definition of logical recollection.
