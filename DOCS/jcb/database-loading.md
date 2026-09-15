---
title: Database loading and nested enrichment
description: Root queries, relationship metadata, field-type joins, indexed reuse, and context-dependent retrieval.
section: JCB Case Study
order: 53
evidence: Source observations
---
# Database loading and nested enrichment

## Root acquisition is only the beginning

`Component\Data` constructs a query around the component record and joins related settings for views, updates, configuration, dashboard, files/folders, modules, plugins, and routing. Its `energize()` method then invokes a sequence of enrichment operations, including view loading, build dates, custom-code dispenser settings, SQL, and extension-specific data. [J05](../reference/bibliography.md#j05)

The component registry's `build()` method calls this data service and loads the resulting object. It guards against rebuilding the component state and throws when the data service returns no component. That is a specific load-once behavior, not proof that the entire compiler performs only one database query.

## Relationship metadata matters

`Model\Adminviews` decodes the component's view relationships, processes order and generation flags, and obtains each referenced view's settings through the admin-data service. The relationship can enable site editing, import/export, history, or other behavior. [J10](../reference/bibliography.md#j10)

This supports the theory's distinction between a reusable view definition and its occurrence in a component. Some generation decisions belong to the linking relationship, not just to the shared view record.

The presence of a sorting call does not establish a mathematically total order for every possible input. A reproducibility audit must inspect comparator behavior, ties, and malformed values rather than infer correctness from the name `usort`.

## Fields and field types

`Field\Data` joins a field with its field-type record, including type name and properties. It stores retrieved field objects and indexes both numeric IDs and GUIDs. Subsequent requests can use the index rather than repeating the original acquisition. [J09](../reference/bibliography.md#j09)

However, retrieving an indexed field still calls `getFieldData()`, which invokes the field custom-code updater with single-view and list-view names. The returned base object is therefore part of a context-sensitive path. Describing it as an immutable memoized value would omit an important nuance.

## Fallback acquisition

When local field loading fails, the inspected implementation can attempt a remote fetch for a valid GUID. A retry map limits that attempt, and successful acquisition is followed by another local load. This is a concrete gather-again path, distinct from both containment traversal and unrestricted recursion.

A portable reproducibility model must identify the acquired remote revision or bytes. A successful remote fetch changes what knowledge is available; it cannot be ignored in the build's input record.

## Architectural consequence

JCB does not merely bulk-load the database and then perform isolated string replacement. It enriches objects through relationships, reuses indexed knowledge, and applies context-specific transformations. The [context-closure abstraction](../semantics/context-closure.md) captures that role without asserting that JCB uses a universal closure evaluator.

The selected source does not establish a complete database transaction snapshot across all these calls. Consistency under concurrent source editing remains a separate implementation and measurement question.
