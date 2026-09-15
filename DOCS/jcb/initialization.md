---
title: Initialization and phase ordering
description: Why constructor work, custom-code extraction, component building, and skeleton creation belong in the runtime account.
section: JCB Case Study
order: 52
evidence: Source observations
---
# Initialization and phase ordering

## Compilation begins before `run()`

The pinned `Componentbuilder\Compiler` constructor stores its collaborators, starts the compilation timer, calls the initializer, and then calls the inherited constructor. The inherited infusion path builds content for the structures. Reading only the public `run()` method would therefore miss a substantial part of compilation. [J12](../reference/bibliography.md#j12), [J06](../reference/bibliography.md#j06)

## The initializer's visible order

`Initializer::init()` has a guard intended to run initialization once. It triggers the pre-get event, sets language and field-builder configuration, calls custom-code extraction, builds the component, handles version information, removes the prior build directory, loads utility powers, triggers the post-get event, and prepares default and external/component structures. [J04](../reference/bibliography.md#j04)

The ordering of extraction before reset is especially significant. It provides a place to recover admitted changes from installed output before the new build proceeds. The inspected method calls `extractCustomCode()` before `buildComponent()`, so captured changes can participate in the subsequent data-loading path. This statement concerns the visible order; collaborators may perform other reads during construction.

## Initialization is not read-only

Version handling can inspect registry flags for SQL additions or updates and increment a component version. Defaults are written into shared content memory. Output directories are removed and recreated through structure services. These are real state transitions, not merely object allocation.

For a formal reproducibility claim, such operations must be accounted for in the epoch boundary. A practical production procedure may reconcile and update metadata first, then identify the effective source snapshot used by synthesis. The paper does not assume JCB automatically creates that abstract immutable snapshot.

## Skeleton creation

The initializer builds library, power, module, plugin, and component structures. It distinguishes base component structure, single-instance structure, and multiple/dynamic structure. A later phase still updates file contents.

This means the logical order is not simply “finish every value, then create every file.” A more accurate account is “prepare structure and content state, then complete the artifacts through ordered updates.” The [materialization model](../mechanisms/materialization.md) explicitly accommodates incomplete skeletons.

## Relation to the inner and outer loops

The outer editorial loop begins before fresh synthesis: installed artifacts can contribute persistent custom-code knowledge. The inner loop appears during component enrichment and dependency loading. Both are present in initialization, but they are not the same operation and do not share one termination proof.

## Review implications

When modifying or reimplementing this flow, preserve the temporal contracts rather than copying method names. In particular, do not reset a location before recovering the edits whose preservation contract depends on it; do not treat version mutations as invisible inputs; and do not publish a skeleton as a completed artifact merely because it exists.

These are deductions from the observed ordering and the formal contracts, not a claim that every possible JCB extension already enforces them.
