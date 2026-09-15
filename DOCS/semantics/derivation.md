---
title: Guarded derivation and strata
description: How recollected facts become new facts and fragments without hiding non-monotone conditions or destructive updates.
section: Semantics
order: 22
evidence: Formal model
---
# Guarded derivation and strata

## From availability to consequence

A derivation rule has an identifier, input pattern, guard, transformation, output scope, and provenance rule. In the finite model, write

$$
r=(P_r,g_r,c_r),\qquad
P_r\subseteq K\ \land\ g_r(K)\Longrightarrow c_r(K)\subseteq U_e.
$$

The premise may require a field definition, a field occurrence, its type, the enclosing view, and the target version. The consequence can include a validation fact, a database-column description, or a context-specific output fragment. A consequence need not be stored as text until a later stage.

The architecture permits fan-out: one established fact can support several derivations. It also permits fan-in: a fragment can require several independent facts. Consequently, a dependency hypergraph is often more expressive than a simple list of stages.

## Positive rules

For the simplest closure proof, enabled rules remain enabled as knowledge grows, and their contributions are monotone. A positive premise such as “the field is declared searchable” has this form when declarations are immutable within the epoch.

The accumulating operator is

$$
F(K)=K\cup\bigcup_{r\text{ enabled in }K}c_r(K).
$$

The union must be compatible under the chosen key semantics. A rule that overwrites an earlier value does not satisfy this model merely because it is implemented by a registry's `set` method.

## Negative conditions

Consider “if no label is available, generate a fallback.” If a real label arrives later, the first result may be wrong. Absence is not generally monotone: learning more can invalidate the condition that nothing is known.

A safe design closes the authoritative label sources first, freezes that stratum, then calculates fallbacks in a later stratum. A negative dependency may point to an earlier closed stratum, not back into the same unrestricted positive closure. Alternatively, use an explicit precedence lattice and carry unresolved alternatives until a final resolution stage. The chosen policy must be visible.

## Aggregates and completeness

Generating a comma-separated list of every field before field discovery is complete produces a value that must later be replaced. This is not an error if treated as a staged aggregate. It is an error in reasoning if presented as an append-only fact.

The clean decomposition is: accumulate field-occurrence identities as a set; close that set; order it canonically; then render the aggregate once. A production implementation may incrementally maintain the aggregate, but it must prove equivalence to that specification.

## Context-sensitive transformations

A field-type definition can be shared while its rendered field name, ownership, or target-language syntax differs between occurrences. The transformation is therefore $c_r(d,\Gamma)$, not merely $c_r(d)$. Memoization must include the context dimensions on which the transformation actually depends.

Context can be inherited from parents and synthesized from children, but the dependency directions must be stated. [Composition](composition.md) describes why this resembles attributed structures without asserting that JCB implements an attribute-grammar evaluator.

## Effects and extensions

A rule that reads the clock, queries an unfrozen remote service, mutates the source database, or executes user code can still be useful. Such behavior must be modeled as an explicit input or effect, not concealed inside a “pure” rule.

The specification recommends separating pure derivations from effectful adapters. This is a proposed portability and verification discipline; it is not a claim that all inspected JCB transformations are pure.
