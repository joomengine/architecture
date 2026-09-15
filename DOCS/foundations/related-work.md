---
title: Related work and intellectual boundaries
description: The closest mathematical and architectural precedents, their similarities, and the distinctions that remain meaningful.
section: Foundations
order: 14
evidence: Literature comparison and interpretation
---
# Related work and intellectual boundaries

## A composition, not an invention of every ingredient

VDMT names a particular organization of contextual acquisition, scoped derivation, staged output, and persistent editorial feedback. Its formal tools and many constituent mechanisms have established precedents. The scientific question is whether specifying their composition yields useful, portable contracts and experimentally distinguishable benefits—not whether a new name erases earlier work.

The originator's account of independent development is preserved in [provenance](provenance.md). Independence and historical priority are different claims. The comparisons below are architectural correspondences, not evidence of influence on the original implementation.

## Compiler pipelines and intermediate representations

Compiler infrastructures such as LLVM explicitly define intermediate representations and transformations. VDMT likewise separates source knowledge from intermediate and emitted forms. Its distinctive emphasis here is contextual recollection and an admitted editorial path from generated artifacts back into durable source. A compiler pipeline does not inherently promise that latter path. [R16](../reference/bibliography.md#r16)

A registry of code strings can serve an intermediate-representation role without having the structural guarantees of a typed AST or SSA representation. Calling both “IR” identifies a role, not equivalence of safety or optimization capability.

## Attribute grammars and hierarchical interpretation

Knuth's attribute-grammar work provides a precise precedent for inherited and synthesized information associated with structured occurrences. The field/view/component hierarchy has a useful correspondence: target settings flow toward children, while child-derived requirements contribute to parents and output artifacts. JCB is not thereby shown to implement an attribute-grammar evaluator. [R02](../reference/bibliography.md#r02)

VDMT also permits shared definition graphs, database-backed acquisition, and artifact feedback that are not captured merely by naming a parse tree's attributes.

## Fixed-point semantics and production systems

The finite closure laws use established order-theoretic reasoning. Tarski's work belongs to the mathematical foundation, not to the novelty claim. [R01](../reference/bibliography.md#r01)

Production systems maintain working facts and apply rules whose premises match those facts. Forgy's Rete algorithm specifically addresses efficient many-pattern/many-object matching. VDMT's guarded derivations are related at the semantic level, but the inspected JCB code does not establish a Rete network or a generic production-rule agenda. [R13](../reference/bibliography.md#r13)

## Blackboard architectures

Blackboard systems coordinate specialized knowledge sources through shared problem state; Nii's account explains this family and its development from HEARSAY-II. VDMT's specialized stores and reuse suggest a family resemblance. The important difference is that JCB's observed execution is strongly orchestrated through calls and phases, rather than established here as opportunistic blackboard scheduling. [R08](../reference/bibliography.md#r08)

A blackboard analogy is useful for explaining cooperation through shared knowledge, but too broad to specify binding order, occurrence identity, or edit-preservation laws.

## Tuple spaces

Gelernter's Linda organizes communication through independently existing tuples in a shared coordination space. A registry-mediated architecture can similarly decouple a producer from a consumer. However, VDMT does not require Linda's tuple matching, blocking operations, destructive receipt, or distributed communication semantics. A key-value lookup is not automatically a tuple-space operation. [R09](../reference/bibliography.md#r09)

## Staging, partial evaluation, and templates

Taha and Sheard's multi-stage programming work makes evaluation stages and cross-stage code construction explicit. VDMT's binding-time discipline is related, but a sequence of string substitutions does not inherit MetaML's type and scope guarantees. [R11](../reference/bibliography.md#r11)

Template expansion is a possible emitter. Partial evaluation is a more specific semantic operation: specializing a program with respect to known input. Not every template insertion is partial evaluation, and the present case study does not prove a general partial evaluator inside JCB. The portable contribution is to state when each value becomes authoritative and which stage may consume it.

## Memoization and incremental build systems

Michie's memo-function work is a precedent for retaining results to avoid repeated work. VDMT's recollection is broader: a request can trigger acquisition, interpretation, and further requests, while a cache is only one implementation of reuse. [R18](../reference/bibliography.md#r18)

Mokhov, Mitchell, and Peyton Jones separate concerns in build-system design, including dependency structure and rebuilding decisions. Their distinctions are especially relevant to VDMT's optional incremental profile. A within-build registry does not establish correct cross-build invalidation. [R04](../reference/bibliography.md#r04)

## Bidirectional transformations and round-trip engineering

Foster and colleagues' lens work formalizes how updates to a view can correspond to changes in a source. This is the closest mathematical comparison to VDMT's editorial feedback path. The marker-based model in this paper is deliberately partial and region-bounded; it does not claim a general inverse of every generated artifact. [R03](../reference/bibliography.md#r03)

Three-way merging and stable region identity are engineering mechanisms that can support the contract. They must be specified separately from extraction itself.

## Provenance, ETL, and materialized views

Database provenance research distinguishes combinations and alternatives of contributing inputs, which helps formalize explanations and invalidation. VDMT can use such models without claiming to originate them. [R05](../reference/bibliography.md#r05)

ETL and materialized-view pipelines also acquire, transform, and store derived information. VDMT adds explicit occurrence-sensitive synthesis and an admitted artifact-to-source loop. Conversely, it does not automatically inherit a database's transaction semantics. Event sourcing is another distinct commitment: an append-only event history is not established merely because a system stores the latest recovered edit.

## Cognitive architectures

ACT-R models specialized modules, buffers, production selection, and subsymbolic processes. Global-workspace models study coordination and broad availability in cognition. These provide useful comparison questions, not proof that compiler registries are biological memory or consciousness. [R10](../reference/bibliography.md#r10), [R14](../reference/bibliography.md#r14)

The [cognitive research page](../research/cognition.md) keeps the analogy operational and falsifiable.

## Contribution statement

The defensible contribution is an attributable formalization of an implemented architectural composition, with explicit interfaces, laws, limits, and a research program. The paper does not claim a new complexity class, a new general fixed-point theorem, universal optimality, or the first appearance of every related pattern. Its value can be assessed through independent reimplementation and controlled comparison.
