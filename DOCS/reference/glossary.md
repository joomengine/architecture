---
title: Glossary
description: Concise definitions of the architectural and mathematical terms used in the VDMT specification.
section: Reference
order: 103
evidence: Definitions
---
# Glossary

## Artifact

An identified output with content and metadata. A file is one realization. A physical destination is an attribute of an artifact, not automatically the identity of a reusable definition.

## Binding

Resolving an output obligation against an authoritative environment. Binding stages specify when values may be consumed and whether introduced tokens are eligible for later processing.

## Closure

A state containing its seed and every consequence licensed by the specified bounded rules. Closure is relative to the rule system and source epoch, not a claim of all possible knowledge.

## Confluence

Agreement of admissible reduction paths through a common result. It is stronger than choosing one deterministic execution order. See [scheduling](../semantics/confluence.md).

## Context

The owner, task, target, ancestry, role, and other dimensions that affect interpretation. Only relevant dimensions need appear in a particular key, but omitting a relevant one makes reuse unsound.

## Definition

Reusable source knowledge identified independently of its uses. A definition can have many occurrences with different settings.

## Derivation

A transformation from established premises and context to a consequence. A pure positive derivation can participate in finite closure; arbitrary mutation requires another contract.

## Determinism

The property that a complete input determines a unique result. It does not imply correctness, truth, or independence from execution order.

## Editorial memory

Persistent records of admitted human adaptations, with identity and reconciliation policy. It is not simply a cache of the last generated file.

## Epoch

One identified source and environment boundary for synthesis. Source changes between epochs are distinct from knowledge accumulation within an epoch.

## Fixed point

A state $x$ satisfying $F(x)=x$. Finite knowledge closure and stable self-generation are different applications of this concept with different operators.

## Inflationary

A transformation satisfying $x\sqsubseteq F(x)$ in an information order. It does not retract established information in that order.

## Intermediate representation

A form between source input and final output used for interpretation or transformation. It may be structured data, a typed graph, an AST, or text; these representations have different guarantees.

## Materialization

Producing the concrete artifact representation from a plan and its bindings. Skeleton creation and semantic completion are separate events.

## Memoization

Retaining a computation's result for reuse under an equivalent complete input. It is one optimization for recollection, not the entire architecture.

## Monotone

A transformation preserving the information order: more input knowledge does not remove its previous consequences. Monotonicity alone does not guarantee finite termination.

## Occurrence

A context-qualified use of a definition. Occurrence identity prevents shared definitions from erasing differences between components, targets, roles, or destinations.

## Provenance

The source, rule, context, and dependency information explaining a result. Traceability does not by itself establish that the premises or conclusion are true.

## Recollection

Resolving a context-qualified request from a source snapshot, already established knowledge, or a defined reconstruction. It is an operational term here, not a claim of biological recall.

## Reconciliation

Determining how extracted edits relate to the current persistent source and previous baseline, including no-op, accepted update, conflict, or migration.

## Registry

An implementation container for keyed values. A semantic registry is not the same role as a service container, and neither name implies a physical memory-allocation algorithm.

## Round trip

A bounded source-to-artifact-to-source path governed by preservation laws. It is not a general inverse of arbitrary generated output.

## Self-generation

Generating an identified part of the generator-bearing system. Bootstrapping uses successive generated instances. Neither term automatically implies Turing completeness.

## Stratum

A stage whose input knowledge is closed before later operations such as absence tests or aggregates rely on it. Strata help separate monotone accumulation from non-monotone decisions.

## VDMT

Vast Development Method Theory: the attributed framework for contextual recollection, occurrence-sensitive staged synthesis, and persistent editorial reconciliation described in this publication.
