---
title: State space and abstract machine
description: A typed build state that separates durable knowledge, temporary stores, artifact plans, provenance, and external effects.
section: Semantics
order: 20
evidence: Formal model
---
# State space and abstract machine

## A build is an epoch, not an unbounded mutable universe

Fix an epoch $e$ and an explicit input tuple

$$
I_e=(D_e,M_e,\Theta_e,C_e,E_e).
$$

$D_e$ is the source snapshot, $M_e$ the validated editorial memory, $\Theta_e$ the transformations and templates, $C_e$ the configuration and target, and $E_e$ the relevant environment. Environment includes any compiler/runtime version, locale, external dependency, or clock value that is allowed to affect the claimed output.

The machine state is

$$
S=(p,Q,V,K,R_1,\ldots,R_m,\Pi,A,\mathcal{P},\mathcal{E}),
$$

where $p$ is the phase, $Q$ the discovered requests, $V$ the completed requests, $K$ the established context, $R_i$ intermediate stores, $\Pi$ the artifact plan, $A$ staged artifacts, $\mathcal{P}$ provenance, and $\mathcal{E}$ errors. Physical copies are not implied: a store can contain an immutable reference to a shared value.

A transition $S\xrightarrow{\tau}S'$ identifies the rule, reads, writes, and source epoch. This is an operational specification. It does not require a VM or a new programming language.

## Typed and scoped bindings

Use keys of the form $(\text{kind},\Gamma,\text{name})$. Different kinds distinguish a semantic fact, a code fragment, a render slot, a destination, and an editorial region. Different contexts distinguish two uses of the same definition. This prevents an apparently equal name from silently identifying unrelated facts.

A runtime lookup has an algebraic result:

$$
\operatorname{lookup}(k)\in\{\operatorname{Absent},\operatorname{Present}(v,p),\operatorname{Conflict}(c)\}.
$$

`Present(null)` is not `Absent`. Errors are not empty strings. A missing optional field may be acceptable; a missing required namespace at emission is not.

## Consistency and joins

Ordinary map union is undefined when two writers assign different values to the same key. Two formal options are useful.

**Consistent finite-fact model.** Restrict $K$ to subsets of a finite universe $U_e$ and require that all reachable sets are consistent under a specified key/value relation. Joins are set unions within the consistent execution. Violation yields an error, not an arbitrary winner.

**Explicit-conflict model.** For each key $k$, use a flat lattice $L_k=\{\bot\}\cup V_k\cup\{\top\}$, where different concrete values join to $\top$, the conflict state. The product $L=\prod_k L_k$ has componentwise joins. An implementation may calculate a unique conflict-containing closure, but successful publication additionally requires that no required key is $\top$.

The proofs in the following pages use the first model unless stated otherwise. Their consistency assumption is material, not decorative.

## Phase boundaries

The abstract phases are reconcile, freeze, gather, derive, plan, bind, validate, and publish. These are semantic boundaries, not a demand that every implementation execute exactly eight methods. A compiler may precreate file skeletons before all content is derived. It must still distinguish incomplete artifacts from validated outputs.

Persistent source mutation belongs to reconciliation before freezing, or to a separately declared side effect after the build. Mixing an evolving database with a claim of one fixed source snapshot invalidates the simplest determinism argument.

## Observable behavior

The successful result is a finite artifact map and a manifest. Failure is also an observable result: the machine returns diagnostics and does not publish a partial result as successful. The abstract transaction does not make a database and filesystem magically atomic; an implementation must supply a concrete commit protocol.

[Determinism](determinism.md), [reconciliation](../mechanisms/reconciliation.md), and [materialization](../mechanisms/materialization.md) explain the additional conditions required for these transitions to be reliable.
