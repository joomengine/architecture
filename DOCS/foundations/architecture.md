---
title: The architectural object
description: The complete object transformed by contextual compilation, from reusable definitions and use-site settings to coordinated output artifacts.
section: Foundations
order: 10
evidence: Architectural abstraction with implementation correspondence
---
# The architectural object

JCB compiles a structured application description. The description is distributed across reusable entities, relationships, configuration, custom code, and assets. It is assembled for a particular build rather than read as one undifferentiated source string.

The architectural object is therefore a **contextual application model together with its generation environment**. A database stores one representation of that model. Repository JSON stores a portable representation. Generated source files store the application's implementation for a target platform. The compiler connects these representations through explicit operations.

## Definitions, uses, contributions, and products

A definition supplies reusable information. A use attaches that information to a particular application context. Processing the use produces contributions to several concerns. Those contributions are later assembled into artifacts.

For a definition $d$ and context $\Gamma$, write

$$
J(d,\Gamma)=\langle c_1,c_2,\ldots,c_m\rangle.
$$

Each $c_i$ is a contribution with a destination store, a key, an update operation, and a value. Some contributions are code fragments. Others are schema descriptions, flags, aliases, language mappings, requirements, or deferred operations. A value need not be executable text to affect the generated application.

For the Greeting field, the reusable definition describes its type, label, and database properties. Its admin-view association marks it as a title, searchable, sortable, and visible in the list. Processing that association creates consequences beyond the form input itself. [Field trace](../examples/field-trace.md)

## A graph rather than a flat list

Let $G=(V,E)$ be the resolved definition graph. Vertices are typed entities. Edges identify references, ownership relationships, associations, or asset requirements. The same vertex can participate in several uses; an occurrence expansion supplies those uses without pretending that shared definitions have become unrelated copies.

The artifact graph is different from the definition graph. Several definitions can contribute to one file. One definition can contribute to several files. A component relation can include a module or plugin whose own data and emitters produce another extension tree.

Consequently, no general one-definition-to-one-file correspondence is assumed. The useful relation is

$$
\mathcal{R}\subseteq \mathcal{O}\times\mathcal{C}\times\mathcal{A},
$$

where $\mathcal{O}$ denotes contextual occurrences, $\mathcal{C}$ contributions, and $\mathcal{A}$ artifacts. A trace records which contribution from which occurrence participates in which artifact.

## The generation environment supplies reusable knowledge

A complete build includes more than the project blueprint. It includes compiler rules, skeletons and templates, reusable libraries and Powers, target conventions, configuration, and relevant environment values. A compact blueprint is effective because those inputs already embody recurring implementation decisions.

Write a build input as

$$
I=(D,R,\Theta,T,C,H),
$$

with local definitions $D$, configured repository responses $R$, generation rules and supplied reusable material $\Theta$, target $T$, build configuration $C$, and relevant host environment $H$.

This expression identifies dependencies of the computation. It does not require JCB to serialize all of them into a single immutable object before compilation. The actual execution can acquire more definitions and produce filesystem state while other semantic work is still in progress. [State model](../formal/state.md)

## The compiler is the coordinating centre

JCB's orchestration acquires component data, enriches its children, prepares shared and context-specific output material, performs deferred work, and updates staged files. The implementation uses a shared service container, specialised builders, code dispensers, and target-specific architecture services. These are concrete representations of the model's responsibilities. [C01–C06](../reference/source-map.md#c01)

The contribution of this account is to make that coordination explicit enough to study and reproduce. Another implementation could use records, typed maps, graph nodes, functions, or a different persistence layer while preserving the same separation of identities, contexts, contributions, ordering, and outputs.

The next chapters examine [structured intent](structured-intent.md), [identity](identity.md), and [context](context.md) before following the [complete lifecycle](lifecycle.md).
