---
title: Context-qualified contributions and consistency
description: Contribution algebra, safe reuse, effect guards, occurrence expansion, and cross-artifact consistency relations.
section: Formal Model
order: 73
evidence: Formalization of field classification, scoped stores, and artifact traces
---
# Context-qualified contributions and consistency

Classification maps one contextual use of a definition into the consequences needed by several generators. Its formal object is an ordered contribution sequence, not a single final string and not necessarily a monotone set of facts.

## A typed contribution algebra

Let $M_s:K_s\rightharpoonup V_s$ be store $s$. A contribution $c=(s,k,\omega,v)$ applies a declared update at address $(s,k)$. Typical operations include

$$
\operatorname{set}(M,k,v)=M[k\mapsto v],
$$

$$
\operatorname{append}(M,k,v)=M[k\mapsto M(k)\mathbin{\|}\langle v\rangle],
$$

with a declared empty sequence for an absent append value. `Fill` writes only when its chosen absence predicate holds; `remove` deletes the binding; concatenation joins text. A set-union operation is used only for values whose semantics are sets.

For $J(d,\Gamma)=\langle c_1,\ldots,c_m\rangle$,

$$
M_0=M,\qquad M_i=\operatorname{apply}(c_i,M_{i-1}).
$$

The final $M_m$ is the interpretation's store effect. A field can set a title binding, append a searchable member, add schema data, and concatenate code in one interpretation. Their different operations remain explicit.

## Occurrence expansion precedes projection counting

A definition graph can reuse one field in several views. Let $\operatorname{uses}(d)$ be its finite occurrence set. Total interpretation is over occurrences:

$$
\mathcal{C}_{\mathrm{build}}
=\mathop{\operatorname{concat}}_{o\in\mathcal{O}\text{ in prescribed order}}
J(\operatorname{definition}(o),\Gamma(o)).
$$

The count of definitions, occurrences, contributions, and files can therefore differ substantially. Neither a one-to-one mapping nor a fixed expansion factor is assumed.

This distinction also explains why a definition-level acquisition cache can coexist with view-level script guards and per-file import maps. They operate over different domains.

## Proposition: a sufficient reuse condition

Assume $J$ is deterministic and its result depends only on the definition version $d$, a context projection $\pi_J(\Gamma)$, and a dependency observation $z$. Define a cache key

$$
\kappa_J=(\operatorname{id}(d),\operatorname{version}(d),\pi_J(\Gamma),z).
$$

Equal keys imply equal interpretation results, provided key equality faithfully represents equality of those dependencies.

**Argument.** Every argument read by $J$ has the same value in the two uses. Determinism therefore gives the same contribution sequence. No statement is made about dimensions that the key omits unless their irrelevance has been established.

A smaller key is valid when an equivalent dependency projection is justified. A key based only on a GUID is insufficient for a result whose language prefix, target namespace, or view-specific name can differ.

## Equal values do not make repeated effects harmless

Memoizing a prepared fragment and applying that fragment twice are separate operations. If its update is concatenation, repeating the same fragment duplicates content. A per-scope contribution guard can be required even when retrieval returns the same value.

For an effect $f$, safe repeated application needs idempotence,

$$
f(f(M))=f(M),
$$

or a guard ensuring that the effect is applied only once in the intended occurrence/role scope. JCB's field/view script tracking is a concrete example of the second approach. [Acquisition](../compiler/acquisition.md)

## A sufficient independence condition

Two deterministic operations $f$ and $g$ can be freely exchanged when their writes are disjoint and neither reads what the other writes, with no unmodeled external effects:

$$
W_f\cap W_g=\varnothing,\quad
W_f\cap R_g=\varnothing,\quad
W_g\cap R_f=\varnothing.
$$

Under these assumptions, applying either operation leaves the other's observed inputs unchanged, and their updates affect separate locations. Thus $f(g(M))=g(f(M))$.

Many compiler operations do not satisfy these conditions. Appending to the same ordered fragment or changing a language prefix before a consumer is intentionally order-sensitive. The prescribed execution order remains part of the architecture.

## Cross-artifact consistency is a relation

Let $a_1,\ldots,a_n$ be artifacts influenced by one occurrence. A consistency relation $\mathcal{I}$ can require their interpreted names, types, or policy references to agree:

$$
\mathcal{I}(d,o,a_1,\ldots,a_n).
$$

For Greeting, the form and metadata agree on logical name and field GUID where emitted; the SQL and metadata agree on `VARCHAR(255)` and ordinary-key status; the form and list refer to the intended language label; the association supplies title and sorting roles.

The form maximum of 50 and database width of 255 are not a violation because they are different properties. A correct invariant compares corresponding meanings, not every superficially similar number.

## Traceability connects the abstraction to output

A provenance relation records which occurrence produced a contribution and which consumer used it:

$$
\mathcal{P}\subseteq\mathcal{O}\times\mathcal{C}\times\mathcal{A}.
$$

The publication reconstructs selected paths through source references and marker traces. It does not assume that production JCB stores a complete provenance graph at runtime. The relation is useful for tests and explanations even when inferred from the orchestration.

The compiler's maintenance advantage follows from this coordination: shared interpretation and target rules update the artifacts related by $\mathcal{P}$ when the model is regenerated. The [implementation guide](../engineering/implementation.md) shows how another language can preserve these boundaries using typed records and explicit operations.
