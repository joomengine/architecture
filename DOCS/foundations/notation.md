---
title: Mathematical notation
description: Types, functions, relations, orders, identities, and the exact meaning of the symbols used throughout the paper.
section: Foundations
order: 11
evidence: Formal model
---
# Mathematical notation

## Universes and partial information

$\mathbb{N}$ includes zero. $\mathcal{P}(X)$ is the powerset of $X$. A function $f:A\to B$ is total unless explicitly called partial. A partial function is written $f:A\rightharpoonup B$. We distinguish an absent binding $\bot$ from a present value such as `null`, `false`, zero, or the empty string.

A finite sequence is written $[x_1,\ldots,x_n]$. A set has no inherent order. When output order matters, an implementation must choose and document a total order rather than silently depending on set iteration.

## Names used by the abstract machine

| Symbol | Meaning |
| --- | --- |
| $e$ | Build epoch: one identified source snapshot and environment |
| $D_e$ | Durable source snapshot for epoch $e$ |
| $M_e$ | Validated editorial overlay or preserved region records |
| $I_e$ | Explicit input tuple, including rules, templates, configuration, and dependencies |
| $Q$ | Context-qualified requests |
| $K$ | Established facts and dependency observations |
| $R_i$ | Scoped intermediate store at stage $i$ |
| $\Gamma$ | Occurrence context, including owner, target, and relevant ancestry |
| $\Theta$ | Rule, transformation, and template definitions |
| $\Pi$ | Ordered artifact plan |
| $A_e$ | Generated artifact map for epoch $e$ |
| $X$ | Extraction of admissible marked editorial regions |
| $\mu$ | Reconciliation of extracted edits with persistent records |
| $N$ | Declared output normalization function |
| $\equiv_N$ | Output equality after applying $N$ |

Artifact maps are partial maps from logical artifact identity to byte strings and metadata. Paths are attributes of artifact occurrences; they are not automatically the identity of a reusable definition.

## Information order

For the finite fact model, $K_1\sqsubseteq K_2$ means $K_1\subseteq K_2$. This order represents increasing knowledge, not increasing string length, score, or memory usage. A transformation is monotone when

$$
K_1\sqsubseteq K_2 \Longrightarrow F(K_1)\sqsubseteq F(K_2).
$$

It is inflationary when $K\sqsubseteq F(K)$. A fixed point satisfies $F(K)=K$. Monotonicity and inflationarity are different properties. Neither alone makes arbitrary iteration terminate over an infinite domain.

For a map with incompatible values at one key, ordinary union is not a valid merge. We either restrict the admissible state space to consistent assignments, or use a join-semilattice that includes an explicit conflict element. [State space](../semantics/state-space.md) makes the choice explicit.

## Identity and context

A definition key is $d=(\text{namespace},\text{kind},\text{id},\text{revision})$. An occurrence key is $o=(d,\Gamma,\text{role},\text{destination})$. Not every implementation needs to serialize this exact tuple. It must preserve the distinctions that influence derivation and output.

A fact can be represented as $(k,v,p)$, where $k$ is a scoped key, $v$ its value, and $p$ its provenance. Equality of values does not imply equality of provenance; a runtime may store provenance separately to avoid copying large values.

## Equivalence

Byte equality, syntax-tree equivalence, and behavioral equivalence are not interchangeable. $A\equiv_N B$ means $N(A)=N(B)$ for a specified normalization $N$. The identity normalization yields byte equality. Removing timestamps is legitimate only when those timestamps are explicitly excluded from the claimed observable semantics.

A hash is a practical comparison mechanism, not a proof that two arbitrary values are equal without a collision assumption. The formal propositions use mathematical equality; engineering tests may use cryptographic digests and record that choice.
