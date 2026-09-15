---
title: Artifact planning and materialization
description: From logical output identities to validated files, with cardinality, collision, staging, and publication contracts.
section: Mechanisms
order: 35
evidence: Formal model and proposed implementation contract
---
# Artifact planning and materialization

## Plan before declaring success

An artifact plan is a finite ordered family

$$
\Pi=[(a_i,p_i,t_i,\Gamma_i,b_i)]_{i=1}^{n},
$$

where $a_i$ is logical identity, $p_i$ the destination, $t_i$ the template or emitter, $\Gamma_i$ the occurrence context, and $b_i$ the binding plan. A file is one possible artifact; a record, message, or structured document is another.

Planning makes output cardinality visible. It distinguishes singleton artifacts from per-occurrence artifacts and makes path collisions detectable before writes occur.

## Skeletons and completed artifacts

Some implementations create directories and copy template skeletons before all content is known. This is compatible with staged synthesis if those files are treated as incomplete build artifacts. A file's existence on disk is not evidence that it is ready to install or publish.

The observed JCB initializer prepares component structures before the final file updater. The abstract model therefore separates physical creation from semantic completion rather than insisting on a strict “all data first, any file later” chronology. [J04](../reference/bibliography.md#j04), [J07](../reference/bibliography.md#j07)

## Path validity

Destination validation must account for traversal segments, absolute paths, case-insensitive collisions, reserved names, normalization, symlinks, and ownership of the output root. A portable implementation should validate logical paths before resolving them onto the host filesystem.

Two artifacts with the same path and different contents are a conflict. Equal contents do not automatically make the duplication intentional; the planner should still define whether duplicate destinations are permitted and how provenance is combined.

## Publication protocol

A robust implementation renders into a fresh staging directory, validates the entire manifest, and only then switches the published pointer or directory. This is a proposed production contract, not an assertion that JCB implements a filesystem transaction.

The switch must use facilities whose atomicity is valid for the actual filesystem and deployment topology. A cross-filesystem move, database commit, and remote upload are not one atomic action simply because they occur in one method. Recovery should identify the last committed manifest and clean up abandoned staging areas safely.

## Manifest

Record artifact identity, relative path, byte length, digest, emitter revision, relevant input identities, and editorial-region coverage. This supports reproducibility comparisons and detects outputs omitted from the nominal build count.

If packaging adds compression timestamps or file modes, define whether those are part of the claimed output semantics. Counting generated text and comparing ZIP bytes are different measurements.

## Validation layers

Validation can include required-token completion, target syntax parsing, schema checks, cross-file consistency, dependency presence, permission checks, and application tests. No single check replaces the others. Syntactically valid code can still express the wrong semantics.

## Lower bound

If $B$ bytes must actually be emitted, materialization requires at least $\Omega(B)$ work in a model charging for each output byte. Reuse can reduce acquisition and derivation costs; it cannot eliminate the cost of writing the requested output. This simple bound helps keep large expansion claims in proportion.

See [performance](../engineering/performance.md) for a more complete cost decomposition.
