---
title: Composition and dependency structure
description: How local interpretations combine into larger artifacts, and when shared definitions can be safely reused.
section: Semantics
order: 27
evidence: Formal model and deductions
---
# Composition and dependency structure

## More than a linear pipeline

The surface execution may look sequential, but its data dependencies form a graph. A field occurrence draws on a type definition and an enclosing view; a view draws on several fields; several output files draw on the same view-derived values. The most precise general representation is an attributed dependency graph, with hyperedges where a rule requires several premises simultaneously.

A transformation can be written

$$
f_i:(R_{a_1},\ldots,R_{a_k},\Gamma_i)\to\Delta R_{b_i}.
$$

The $\Delta$ indicates a contribution, not necessarily a destructive replacement of the target store. Its merge policy is part of $f_i$'s contract.

## Definition-level and occurrence-level composition

Let $d$ be a reusable definition. A target-specific interpretation is $J(d,\Gamma)$. Reusing the definition is safe when the interpreter receives every context dimension that can affect its result.

Caching $J(d,\Gamma_1)$ for use in $\Gamma_2$ is justified only when an equivalence relation establishes that the relevant contexts agree:

$$
\Gamma_1\sim_J\Gamma_2\Longrightarrow J(d,\Gamma_1)=J(d,\Gamma_2).
$$

This is a proof obligation or an implementation contract, not an inference from the values happening to match once. A conservative cache includes the entire relevant context in the key. More aggressive caching may use an audited projection of context.

## Inherited and synthesized information

Some values flow downward: a component's target version, namespace, and naming conventions constrain its view and field occurrences. Other values flow upward: the fields determine a view's validation or query requirements. Finally, those synthesized values fan outward into multiple artifact locations.

This resembles the distinction between inherited and synthesized attributes in attribute grammars, but the paper does not claim that JCB is implemented as an attribute grammar. It uses the analogy to expose dependency direction. [R02](../reference/bibliography.md#r02)

## Proposition 6 — safe independent composition

Suppose modules $A$ and $B$ are deterministic, have no hidden effects, and have disjoint writes with no cross read/write dependency. Then applying $A$ followed by $B$ produces the same combined store as applying $B$ followed by $A$.

**Proof.** Neither operation changes the inputs read by the other. Their outputs are therefore unchanged by order. Disjoint writes make their final map union unambiguous. $\square$

When the modules share outputs, a specified commutative merge can replace disjointness. When one reads the other's outputs, an explicit order or common closure is required.

## Compositional correctness is conditional

Correct fragments do not automatically make a correct program. The composition boundary may introduce name capture, duplicate declarations, incompatible types, ordering constraints, or target-specific syntax errors. Therefore artifact validation must include whole-output checks, not only tests of individual fragments.

The same principle applies outside code generation: individually valid document sections can contradict each other, and individually valid configuration files can describe an impossible deployment.

## Reuse is a semantic relation

A reusable definition is not merely copied text. It is a source of meaning whose interpretation can vary with context while retaining identity. Keeping the definition graph compact and making occurrence expansion explicit is a principal route to understanding the large output expansion observed in JCB, without mistaking textual volume for newly invented information.
