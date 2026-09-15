---
title: JCB generating JCB
description: Evidence for self-generation, the precise scope of the claim, and a reproducible multi-stage self-build protocol.
section: JCB Case Study
order: 59
evidence: Project documentation and author testimony
---
# JCB generating JCB

## The reported capability

Llewellyn reports that JCB builds the JCB application itself. The pinned project README identifies the distributed component as created with Joomla Component Builder. This is direct project documentation consistent with the author's account. [J03](../reference/bibliography.md#j03)

The capability is significant because the generated product contains the application in which the compiler operates again. It exercises the same modeling, code reuse, packaging, and maintenance mechanisms against a substantial generator-bearing system.

## Correct terminology

The appropriate description is **self-generation of the generator-bearing application**, with **bootstrapping** for the repeated use of generated versions to build later versions. It should not be described as a PHP-language compiler compiling itself unless that separate claim is actually true and demonstrated.

JCB's model-to-Joomla transformation and PHP's execution semantics are different layers. The theory remains language-independent precisely because it does not confuse the host language with the language or model being transformed.

## Evidence not supplied by a README

A README statement does not specify the full database model, seed version, external dependencies, build environment, generated-versus-copied scope, or equality criterion. Those are needed for an independently reproducible self-build certificate.

No complete live three-stage JCB self-build was performed for this edition. The reference-model tests in this repository are not relabeled as such a build.

## Proposed certificate

Freeze a seed JCB installation, its complete model of JCB, templates, custom-code records, powers, target settings, and environment. Generate and activate the first output in a fresh environment. Use that generated instance to build the same frozen model again, then repeat once more.

Retain the source snapshot, dependency identities, commands, logs, artifact manifests, normalization policy, and comparison of the second and third generated outputs. Explicitly list files copied unchanged, files generated from templates, and code injected from reusable definitions.

A successful comparison demonstrates stable reproduction for the supplied model and environment. Tests of generated application behavior provide additional evidence. Neither result proves correctness for every possible input.

## Trust and expressiveness

Self-generation can demonstrate that the modeling system represents its own application domain well. It does not establish Turing completeness, cognitive understanding, or a security guarantee. Established compiler bootstrapping and compiler-trust research supplies useful comparison methods and warnings. [R06](../reference/bibliography.md#r06), [R07](../reference/bibliography.md#r07)

The formal [self-generation page](../mechanisms/self-generation.md) defines the relevant equations and separates this cross-generation stability from the inner context-closure fixed point.
