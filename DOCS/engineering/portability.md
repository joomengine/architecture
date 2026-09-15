---
title: Portability and conformance profiles
description: Reimplementing the method across languages and storage systems while retaining explicit semantic obligations.
section: Engineering
order: 77
evidence: Proposed conformance framework
---
# Portability and conformance profiles

## Port the contracts, not the incidental syntax

A VDMT implementation does not need PHP arrays, Joomla services, a relational database, or hash-delimited placeholders. It needs an explicit account of task context, identity, discovery, derivation, binding, output, and admitted feedback.

One implementation may keep an immutable graph in memory and emit ASTs. Another may use database views and materialized intermediate tables. A third may interpret a compact domain-specific language. Their conformance depends on observable behavior and declared assumptions, not matching class names.

## Core profile checklist

Identify the complete build input and source epoch. Distinguish reusable definitions from contextual occurrences. Define request completion and failure. Specify store types, write ownership, and conflicts. State binding-stage order and artifact cardinality. Define output equivalence and retain reproducibility evidence.

A core implementation need not support human edits in generated output. It must say so rather than imply that every generated file can safely be changed and recovered.

## Round-trip profile checklist

Add an admissible region grammar, artifact/region identity, ownership validation, extraction, reconciliation, persistence, and reinsertion. State behavior for malformed markers, deleted regions, renamed destinations, simultaneous source/user changes, and conflicting edits to shared definitions.

Demonstrate the preservation law on the supported domain. A partial extractor is acceptable when its domain is explicit and failures are visible. Silently accepting ambiguous edits is not a stronger implementation.

## Incremental profile checklist

Track every relevant dependency, including transformation and template revisions. Invalidate affected results and demonstrate equivalence to a clean build. Specify deletion, alternative derivations, negative dependencies, and external source changes.

Caching alone does not qualify as incremental conformance. The difficult property is using a cached value only when all of its semantic inputs remain valid.

## Self-generative profile checklist

Identify which part of the generator-bearing system is modeled, generated, copied, or externally supplied. Record the seed and environment. Produce successive generations and compare them under a declared equivalence. Do not infer universal language expressiveness or trustworthiness from one successful self-build.

## A conformance statement

A useful statement has the form: “Implementation X, revision Y, supports the core and round-trip profiles for domain Z under assumptions A, with tests and artifacts B.” It should list unsupported behavior and any normalization applied to output comparisons.

These profiles are proposed by this specification. They are not an external standards body's certification and do not establish a trademark license. Their purpose is to make implementations comparable and critiques specific.

## Extension discipline

An extension should state whether it changes semantics or merely representation. Adding probabilistic retrieval, learned ranking, destructive updates, or distributed execution can be valuable, but may invalidate a finite deterministic proof. Keep the original contract available as a bounded mode or provide a new argument for the extended behavior.
