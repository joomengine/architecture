---
title: Mathematical vocabulary and domains
description: A common notation for portable identity, occurrences, contexts, contributions, state, artifacts, and representation equivalence.
section: Formal Model
order: 70
evidence: Formal definitions with implementation correspondence
---
# Mathematical vocabulary and domains

The formal model describes the operations developed in the preceding chapters. It removes dependence on PHP syntax while retaining the distinctions that affect behaviour: typed identity, occurrence context, ordered mutation, deferred work, external observations, and staged artifacts.

A symbol denotes a role in the computation. It need not correspond to one allocated class or database table. For example, the context of a JCB operation can be distributed across arguments, association records, configuration, and store keys.

## Basic domains

| Symbol | Meaning |
| --- | --- |
| $\mathcal{T}$ | Supported entity types |
| $\mathcal{U}$ | Normalized portable requests $u=(t,k,v)$ |
| $D$ | Local definitions and relationships |
| $G=(V,E)$ | Resolved typed definition graph |
| $\mathcal{O}$ | Contextual occurrences of definitions |
| $\Gamma$ | Interpretation context |
| $J$ | A selected interpretation operation |
| $\mathcal{C}$ | Typed contributions to intermediate state |
| $M$ | Family of intermediate stores |
| $W$ | Retained deferred operations |
| $P$ | An ordered binding environment |
| $A$ | Staged or completed artifact collection |
| $\Delta$ | Diagnostics and operation results |
| $\Sigma$ | Complete abstract machine state |
| $\tau$ | An ordered execution trace |

$T$ denotes a generation target, such as an output platform version. It is distinct from $\mathcal{T}$, the set of entity types. $C$ denotes build configuration; calligraphic $\mathcal{C}$ denotes contributions.

## Identity and occurrence

A portable request is $u=(t,k,v)$: entity type, identifying field, and normalized value. A GUID-addressed field and a function-name-addressed custom-code item are both valid instances. A local realization $\lambda_i(u)$ assigns an installation-specific record identity.

An occurrence is

$$
o=(u,p,a),
$$

where $p$ identifies its position in an association/expansion and $a$ contains use-specific settings. Its context can be represented as

$$
\Gamma(o)=(T,e,v,r,\ell,P,a).
$$

The components identify target, extension, view or use-site, generation role, language destination, binding environment, and additional settings. Only the dimensions actually read by an operation determine that operation's reuse boundary. [Context](../foundations/context.md)

## Partial maps, sequences, and sets

$X\rightharpoonup Y$ denotes a partial function: some inputs have no result. A store is usually a partial map from keys to typed values. The symbol $\bot$ denotes absence or an undefined result where the surrounding definition specifies that meaning.

$\langle x_1,\ldots,x_n\rangle$ denotes an ordered sequence. $S\cup R$ denotes set union. $s\mathbin{\|}t$ denotes sequence or string concatenation, as declared by the value type. These operations are not interchangeable. Appending two identical fragments retains both; set union does not.

A replacement map is an ordered sequence of key/value pairs because JCB's replacement semantics can consume tokens introduced by an earlier pair. [Staging](staging.md)

## Contributions and effects

An interpretation returns an ordered sequence

$$
J(d,\Gamma)=\langle c_1,\ldots,c_m\rangle,
\qquad c_i=(s_i,k_i,\omega_i,v_i).
$$

A contribution selects a store, key, update operation, and value. An operation can overwrite, fill an absent value, append, concatenate, remove, or enqueue work. The contribution vocabulary explains effects; it does not force every result into a set of immutable facts.

For an operation $f$, $\operatorname{read}(f)$ and $\operatorname{write}(f)$ name its relevant state locations. External reads are included through the observed input stream. The [state model](state.md) makes their order explicit.

## Artifacts and observation

An artifact has a logical role, destination, context, content, and remaining stages. The collection can include skeletons, prepared files, supporting assets, metadata, and archives. The predicate $\operatorname{complete}(a)$ is relative to the stages required for that artifact.

An observation function $\operatorname{obs}$ selects what a comparison measures: blueprint-relevant design, generated runtime structure, normalized text, raw bytes, or diagnostics. Equality of one observation does not imply equality of every other observation.

We use $\equiv_B$ for normalized blueprint-design equivalence and $\equiv_A$ for an explicitly chosen artifact equivalence. Raw byte equality remains ordinary equality over bytes. [Transport](transport.md)

## Finite builds and unrestricted application families

Each completed build has finite inputs and outputs. The architecture can admit an unbounded family of finite application descriptions without one build containing infinitely many entities or producing infinitely many bytes.

Termination arguments therefore concern the requests reachable in a particular operation and the completion of its handlers. Expressive breadth concerns the family of descriptions and authored extensions admitted by the model. Neither is established merely by counting output lines.

## How to read the propositions

Each proposition states assumptions, a conclusion, and the argument connecting them. They explain a bounded mechanism: traversal, reuse, sequencing, or transport. Their mathematical tools have established precedents in compiler construction, program semantics, and model transformation. [Bibliography](../reference/bibliography.md)

The implementation correspondence identifies where JCB realizes the relevant responsibilities. A proof about the explicit model applies to an implementation path only where its assumptions hold. Keeping those assumptions local makes the account useful for both source review and an independent implementation.
