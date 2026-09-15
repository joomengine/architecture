---
title: Resolution, reachability, and termination
description: Typed local-first lookup, ordered repository selection, guarded dependency traversal, finite termination, and graph-completion conditions.
section: Formal Model
order: 72
evidence: Formal account of package and compiler acquisition mechanisms
---
# Resolution, reachability, and termination

Resolution connects a portable request to an available local definition. Dependency traversal repeats that operation for requests exposed by the acquired material. The model separates selection, retrieval, persistence, and completion so that an attempt guard is not mistaken for proof of success.

## Local-first lookup

Let $u=(t,k,v)$ be a normalized request, $L(u)$ a local lookup, and $\mathcal{R}=\langle r_1,\ldots,r_n\rangle$ the configured repository order. For ordinary initialization,

$$
\operatorname{resolve}(u)=
\begin{cases}
L(u), & \text{an acceptable local definition exists},\\
\operatorname{persist}(\operatorname{map}(\operatorname{fetch}(r_j,u))), & \text{a repository is selected},\\
\operatorname{failure}(u), & \text{otherwise}.
\end{cases}
$$

The selected $j$ is the first applicable index match under the configured search contract. Payload retrieval and mapping can fail after selection. The model does not silently replace that contract with “try every later payload until one succeeds.” [Discovery](../blueprints/discovery.md)

Explicit reset changes the local-preservation decision. Recursive reset policy also depends on the edge role: owned incoming children can be refreshed while referenced reusable definitions continue through ordinary initialization. [Import](../blueprints/import.md)

## Request state and definition state

Use an attempted set $V$, a pending queue $Q$, a successful-resolution map $S$, and a failure map $F$. These are logical roles; the production implementation distributes its guards and result buckets across services.

```text
Q := normalized roots
V := empty
S := empty
F := empty
while Q is not empty:
    u := remove the next request
    if u is in V:
        continue
    add u to V before recursively exposed work can re-enter it
    result := resolve(u)
    if result supplies an accepted local definition:
        S[u] := result.definition
        append its supported discovered requests to Q
    else:
        F[u] := result.diagnostic
```

A request in $V$ has been attempted. A request in the domain of $S$ has an accepted definition. Those predicates have different meanings. A failure can leave the traversal finite but the requested graph incomplete.

## Proposition: termination of guarded traversal

Assume the reachable normalized request universe $U$ is finite, each handler completes, each first attempt enqueues only finitely many requests from $U$, and already-attempted requests do not enqueue new work on their duplicate visit. Then the loop terminates.

**Argument.** Consider the lexicographic measure

$$
\mu=(|U\setminus V|,|Q|)\in\mathbb{N}\times\mathbb{N}.
$$

A first attempt decreases the first component even if it increases the queue length. A duplicate visit leaves the first component unchanged and decreases the second by removing the queued request. Handler completion makes each transition finite. Lexicographic order on these natural-number pairs is well-founded, so there cannot be an infinite sequence of visits.

A cycle such as $u\to v\to u$ is therefore compatible with termination. The guard controls repeated processing; it does not require the dependency graph to be acyclic.

## Reachability describes the intended acquired graph

For a fixed dependency relation $\operatorname{deps}$ and roots $R_0$, define

$$
R_{i+1}=R_i\cup\bigcup_{u\in R_i}\operatorname{deps}(u).
$$

For finite $U$, the sequence stabilizes at the least dependency-closed set $R^*$ containing the roots. Each strict growth step adds a member of $U$; every closed superset containing the roots contains each $R_i$ by induction.

This is ordinary finite reachability/closure reasoning. It describes the requested dependency set, not every mutation and generation operation in the compiler. The source can realize the traversal through nested calls and queue drains rather than these mathematical rounds.

## Conditions for completeness are stronger than termination

Successful graph completion requires that every required request be resolved and that the supported dependencies of accepted records be accounted for. If a local-first path skips dependency examination on a local hit, completeness additionally relies on those local records already having the required local dependencies, or on another stage discovering them.

Formally, a successful result for the selected roots requires

$$
R^*\subseteq\operatorname{dom}(S)
$$

under the applicable validity policy. An empty pending queue alone does not establish that inclusion.

Likewise, a resolver can only close the relation it knows how to extract. Schema-described references and recognized literal code keys belong to that relation. Arbitrary runtime-computed references require a separate contract or runtime mechanism.

## Snapshot stability and schedule independence

When local data, repository selection, payloads, and dependency extraction are stable, different fair traversal orders can reach the same dependency set. Equality of that set does not establish equality of every intermediate side effect, database update sequence, or diagnostic order.

Where the selected payload depends on changing remote state or earlier mutations, resolution includes those observations. A permanent visited marker is insufficient for an algorithm whose earlier answers must be revised after new information appears. JCB's documented acquisition guards should be interpreted within their actual operation lifetime, not generalized into a universal knowledge-completion engine.

## Cost boundaries

With indexed guards and a represented finite graph, traversal bookkeeping can be proportional to visited requests plus discovered edges. Database operations, repository index fetches, payload transfers, parsing, and persistence add their own costs.

Caching a repository index amortizes repeated catalogue access. Retaining a resolved local definition avoids repeated network acquisition. Neither removes the cost of writing the required output or processing distinct contextual occurrences later. [Performance](../engineering/performance.md)

The model isolates these responsibilities so that an implementer can change the transport or queue representation without changing typed identity, local-preservation policy, or the meaning of completion.
