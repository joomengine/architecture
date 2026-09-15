---
title: Terminology and category distinctions
description: Choosing established technical language without confusing memory, recursion, self-generation, determinism, and cognition.
section: Foundations
order: 15
evidence: Definitions and terminology comparison
---
# Terminology and category distinctions

## Theory, framework, method, and algorithm

This publication uses **theory** as the proper name requested by the originator and as an account containing definitions, explanatory structure, conditional propositions, and testable hypotheses. Its present technical status is a **formal architectural framework and research white paper**.

An algorithm is a particular procedure with specified inputs, steps, and results. VDMT admits several algorithms: worklist discovery, positive saturation, ordered rendering, marker extraction, and reconciliation. It is therefore more precise to describe a family of algorithms governed by contracts than to claim one universal algorithm whose implementation must resemble the PHP source line for line.

A working implementation establishes that a particular construction is realizable. It does not make every explanation of that construction true, nor does it prove a hypothesis of optimality.

## Logical memory versus physical allocation

Logical memory concerns what information is available under which identity, scope, revision, and authority. Physical allocation concerns addresses, object layouts, copying, garbage collection, cache lines, and storage devices.

VDMT primarily specifies the former. A reimplementation can optimize the latter independently, provided the observable contracts are preserved. “Moving knowledge between registries” can mean deriving a new representation rather than physically relocating the same bytes.

## Recursion, iteration, and feedback

Recursion is self-reference in a definition or call structure. Iteration repeats a transition. Feedback makes a prior result influence a later input. A nested loop is not necessarily recursion, and a feedback lifecycle need not converge to one permanent output.

The inner VDMT loop completes a context within an epoch. The outer loop admits new human adaptations between epochs. Self-generation introduces a third, distinct comparison between generator-bearing artifacts across builds.

## Determinism, confluence, and correctness

Determinism means the complete input determines the result. Confluence concerns agreement across admissible execution orders. Correctness means the result satisfies a stated specification. A system can be deterministic and consistently wrong; it can be correct under one fixed schedule without being confluent.

Reproducibility additionally requires that another execution can reconstruct the relevant input and environment. These terms should not be replaced by the vague claim that a system “always knows.”

## Self-generation and Turing completeness

Self-generation means producing an identified part of the system that performs generation. Bootstrapping concerns using successive generated implementations. A self-hosting language compiler is a more specific case involving the language it compiles. Turing completeness concerns computational expressiveness under a defined model, not merely the ability to reproduce source or a host application. [R06](../reference/bibliography.md#r06), [R07](../reference/bibliography.md#r07)

There is no automatic award or certification created by crossing from ordinary generation to self-generation.

## Recollection and comprehension

In this paper, recollection is a context-qualified retrieval or reconstruction operation. Comprehension is used cautiously: operationally, it can mean that a system has assembled enough consistent structure to answer the defined task. That does not establish human semantic understanding, subjective experience, or truth of the premises.

The cognitive interpretation is a research hypothesis whose value depends on predictions beyond a resemblance in vocabulary. [Cognition](../research/cognition.md) defines the proposed tests.

## A compact technical description

For scholarly communication, the most informative descriptor is:

> **A context-closed, occurrence-sensitive staged synthesis architecture with partial bidirectional editorial reconciliation.**

Each term identifies a testable responsibility. The name **Vast Development Method Theory (VDMT)** identifies the attributed framework that combines them.
