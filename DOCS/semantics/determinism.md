---
title: Determinism and reproducibility
description: The exact input boundary and output equivalence needed to make consistent outcomes a verifiable property.
section: Semantics
order: 24
evidence: Formal deductions and implementation obligations
---
# Determinism and reproducibility

## The claim that matters

Let $B$ be a build procedure and $I$ its complete explicit input. Determinism means

$$
B(I)=A\ \land\ B(I)=A'\Longrightarrow A=A'.
$$

For a normalized reproducibility claim, replace equality with $A\equiv_N A'$, where the normalization is declared in advance. Determinism is a property of a function or operational semantics, not a synonym for being useful, fast, correct, or intelligent.

The phrase “the system knows what to produce” can be given an operational interpretation: its rules and inputs determine a unique result or a uniquely specified failure. It is not evidence that the system's source knowledge is true.

## Proposition 4 — deterministic staged build

Assume: the source and editorial snapshots are fixed; request resolution is deterministic; derivation has a unique compatible closure; conflict resolution and ordering are explicit; templates and binding stages are fixed; rendering is deterministic; and publication preserves the rendered bytes. Then repeated successful builds of the same input produce identical artifact maps.

**Proof.** The same roots and resolver yield the same request closure. Unique derivation yields the same scoped stores. Deterministic planning yields the same artifact identities and ordered destinations. Each binding stage is a function of fixed templates and fixed values, so induction over stages gives the same rendered content. Deterministic serialization yields the same bytes. Publication does not alter them. $\square$

The proposition does not establish that an existing compiler satisfies every premise. It provides a checklist for establishing such a claim.

## Hidden inputs

Typical hidden inputs include database row order, current dates, random identifiers, target runtime behavior, filesystem enumeration, locale, Unicode normalization, external downloads, plugin configuration, compression timestamps, and line endings. A build can be semantically stable while its ZIP bytes change because of archive metadata.

Each input should be frozen, recorded, or deliberately excluded from a narrower comparison. A digest over the source database alone is not a complete build identity if templates or external code can change independently.

## Three useful comparison levels

**Byte reproducibility** compares every artifact byte and relevant path. It is the strongest and easiest comparison to automate when inputs are controlled.

**Normalized artifact reproducibility** ignores only declared differences, such as a build timestamp field. The normalizer must not erase meaningful code changes merely to make a test pass.

**Behavioral equivalence** compares program behavior under a defined semantics or test domain. Passing a finite test suite supplies evidence, not a universal proof of program equivalence.

## Errors and diagnostic ordering

A parallel implementation can consistently reject an invalid build while reporting a different first conflict on different runs. Distinguish determinism of the acceptance decision from determinism of the diagnostic transcript. Canonically sorting collected errors is one way to make reports stable.

## JCB interpretation

The contemporary source visibly uses dates, version updates, mutable stores, extension events, and external-code facilities. Those mechanisms are compatible with reproducible builds only when their effects are included in the boundary or normalized appropriately. A complete dynamic determinism certificate is not claimed here. [JCB runtime boundaries](../jcb/runtime-boundaries.md) states the implementation-specific limitations.

A practical test compiles twice from independent clean environments using the same complete input snapshot, compares manifests, and then varies one input at a time. [Benchmarking](../engineering/benchmarks.md) and [testing](../engineering/testing.md) specify the evidence to retain.
