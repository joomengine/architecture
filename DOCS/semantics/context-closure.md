---
title: Context closure
description: Finite dependency discovery, context-qualified requests, stable resolution, and the conditions for worklist saturation.
section: Semantics
order: 21
evidence: Formal model
---
# Context closure

## Requests can discover further requests

A request is not necessarily a request for one database row. Resolving a view can reveal field occurrences; resolving a field can reveal a field-type definition; resolving a code fragment can reveal a reusable dependency. The context is complete only when the required dependencies have been resolved or explicitly classified as missing or forbidden.

Let $Q_e$ be a finite universe of admissible, context-qualified requests and $U_e$ a finite universe of possible facts for the frozen epoch. A simple resolver is

$$
\rho_e(q)=(F_e(q),\operatorname{deps}_e(q)),
$$

with $F_e(q)\subseteq U_e$ and $\operatorname{deps}_e(q)\subseteq Q_e$. Starting from roots $Q_0$, define

$$
Q_{n+1}=Q_n\cup\bigcup_{q\in Q_n}\operatorname{deps}_e(q),\qquad
K_{n+1}=K_n\cup\bigcup_{q\in Q_n}F_e(q).
$$

The result after stabilization is the requested context closure. It is task-relative: unrelated database records are not required merely because they exist.

## Worklist execution

```text
pending := canonical_order(root_requests)
completed := empty set
knowledge := seed_facts
while pending is not empty:
    q := take_next(pending)
    if q in completed: continue
    facts, dependencies := resolve(snapshot, q)
    require facts are well-typed and compatible with knowledge
    knowledge := knowledge union facts
    completed := completed union {q}
    pending := pending union (dependencies minus completed)
return knowledge, completed
```

A request identity includes the context and revision relevant to the result. Caching only by a class's short name or by a field's display label is unsound when those names are reused.

## When a visited set is insufficient

The algorithm above assumes resolving $q$ has a stable result under the frozen input. Some resolvers also depend on newly derived knowledge: $\rho_e(q,K)$. In that case, marking $q$ complete forever after one visit can miss dependencies discovered later.

There are two sound designs. Either separate stable source discovery from subsequent derivation, or track the dependencies of the resolver and re-enqueue $q$ when those dependencies gain information. The joint operator over $(Q,K)$ must then satisfy the [fixed-point](fixed-points.md) assumptions. “Visited once” is an optimization with preconditions, not a universal law of recollection.

## Absence and completion

Failure to find a value has different meanings before and after context closure. Before closure it can mean not yet loaded. After an authoritative, successful lookup it can mean absent in the snapshot. Store an explicit result or completed-query record when this difference matters.

Negative caching is safe only within its declared snapshot and query context. A failed network request is not evidence that a dependency does not exist.

## Bounds

For a stable resolver, each request is completed once. Traversal overhead is $O(|Q^*|+|E_Q|)$ with expected constant-time indexed membership, excluding database, decoding, validation, and value-size costs. This is a graph-traversal bound, not a claim that the full compilation runs in linear time.

Finite reachability is essential. A resolver that invents a fresh request on every invocation may never close. A finite graph may contain cycles without preventing traversal termination, provided request identities are stable and duplicate visits are suppressed.

The practical double loop described by the originator is a concrete instance of this more general dependency-completion process. See [nested gathering](../mechanisms/nested-gathering.md).
