---
title: Related mechanisms and bibliography
description: Primary references for model-driven engineering, contextual attributes, staged generation, memoization, modularity, and bounded bidirectional transformations.
section: Reference
order: 91
evidence: Primary literature and official technical documentation
---
# Related mechanisms and bibliography

The architecture was developed independently in the course of building JCB. The references below provide established terminology and mathematical context for mechanisms that can be recognized retrospectively. A correspondence identifies what two approaches have in common; it does not invent an influence on the original development or claim that their complete implementations are equivalent.

Implementation evidence is catalogued separately in the [source map](source-map.md). The principal correspondences concern structured intent, contextual interpretation, retained intermediate information, dependency ordering, and controlled regeneration.

## R01

**Object Management Group. Model Driven Architecture.** [Official overview](https://www.omg.org/mda/).

The separation between application intent and target-platform implementation supplies a useful context for GUI-authored JCB models and target-specific generation. JCB's database-backed entity schema and custom-code roles are its concrete representation choices; use of model-driven terminology does not imply conformance to every OMG modeling or transformation specification. See [structured intent](../foundations/structured-intent.md) and [targets](../compiler/targets.md).

## R02

**Donald E. Knuth. “Semantics of context-free languages.”** *Mathematical Systems Theory* 2, 127–145, 1968. DOI: `10.1007/BF01692511`. [Publisher](https://link.springer.com/article/10.1007/BF01692511).

Inherited and synthesized attributes provide a precise precedent for information flowing into a structured occurrence and results flowing out of it. JCB's field/view/component interpretation has a corresponding direction of information flow, while its implementation uses database entities, services, shared builders, and ordered calls rather than an attribute-grammar evaluator. See [context](../foundations/context.md) and [classification](../compiler/classification.md).

## R03

**Torbjörn Ekman and Görel Hedin. “The JastAdd system—modular extensible compiler construction.”** *Science of Computer Programming* 69(1–3), 14–26, 2007. DOI: `10.1016/j.scico.2007.02.003`. [Publisher](https://doi.org/10.1016/j.scico.2007.02.003) · [JastAdd concept overview](https://jastadd.cs.lth.se/web/documentation/concept-overview.php).

JastAdd combines modular compiler construction with reference attributes, contextual information, and demand-driven evaluation. It is a close comparison for obtaining an interpretation when required and retaining relationships between uses and definitions. JCB's manually orchestrated phases, mutable builders, repository acquisition, and textual emitters remain distinct. The comparison helps identify the actual dependencies of reuse rather than treating every retained result as a context-free cache.

## R04

**JetBrains. MPS generator documentation.** [Generator](https://www.jetbrains.com/help/mps/mps-generator.html) · [Generator cookbook](https://www.jetbrains.com/help/mps/generator-cookbook.html) · [Mapping labels](https://www.jetbrains.com/help/mps/generator-language.html) · [Generation plans](https://www.jetbrains.com/help/mps/generation-plan.html).

MPS mapping labels retain a relationship from input nodes to generated nodes so later reference generation can retrieve the correct counterpart. Generation plans and priorities make transformation ordering explicit. This is a particularly relevant comparison for JCB's retained identities, deferred consumers, and staged generation. MPS's model-to-model transformations and typed node representation differ from JCB's mixture of structured stores and prepared text. The shared architectural question is how a later consumer finds the interpretation established by an earlier producer.

## R05

**Andrey Mokhov, Neil Mitchell, and Simon Peyton Jones. “Build systems à la carte.”** *Proceedings of the ACM on Programming Languages* 2, ICFP, article 79, 2018. DOI: `10.1145/3236774`. [Author/institutional publication](https://www.microsoft.com/en-us/research/publication/build-systems-la-carte/).

The expanded **“Build systems à la carte: theory and practice”**, *Journal of Functional Programming* 30, 2020, has DOI `10.1017/S0956796820000088`. [Journal-version record](https://www.microsoft.com/en-us/research/publication/build-systems-a-la-carte/).

Separating dependency structure, execution order, and rebuilding decisions is useful when analyzing JCB's acquisition queues and deferred work. A within-build cache or fixed replay phase is not automatically a complete cross-build incremental invalidation system. This publication keeps those responsibilities distinct. See [resolution](../formal/resolution.md) and [deferred work](../compiler/deferred-work.md).

## R06

**Donald Michie. “‘Memo’ Functions and Machine Learning.”** *Nature* 218, 19–22, 1968. DOI: `10.1038/218019a0`. [Publisher](https://www.nature.com/articles/218019a0).

Memoization supplies the basic precedent for retaining a computed result to avoid repeating work. JCB's retained state is broader: some entries are acquired definitions, others contextual contributions or operations awaiting later prerequisites. Retrieval can have effects. The paper therefore distinguishes memoized values, contribution guards, dispensers, and deferred work rather than using *cache* for all four.

## R07

**J. Nathan Foster, Michael B. Greenwald, Jonathan T. Moore, Benjamin C. Pierce, and Alan Schmitt. “Combinators for bidirectional tree transformations: A linguistic approach to the view-update problem.”** *ACM Transactions on Programming Languages and Systems* 29(3), article 17, 2007. DOI: `10.1145/1232420.1232424`. [Publisher](https://doi.org/10.1145/1232420.1232424). The earlier conference presentation appeared at POPL 2005.

Bidirectional transformation research supplies the vocabulary for relating a source representation, a derived view, and updates returned from that view. JCB's marked-code recovery is bounded by recognized regions and supported reverse transformations; extrusion reconstructs candidates from represented artifacts. Their domains and preservation relations must be stated separately. See [transport and reconstruction](../formal/transport.md).

## R08

**Eclipse Acceleo. User Guide.** [Official archived guide](https://wiki.eclipse.org/Acceleo/User_Guide).

Protected areas and JMerge integration are established approaches to retaining authored material across generation. They provide relevant context for JCB's designated code regions, GUI addresses, and placement recovery. The comparison concerns regeneration ownership and preservation, not an assertion that every marker scheme has identical identity, merge, or fallback semantics. JCB's commented recovery path is described by its own source in [custom code](../compiler/custom-code.md).

## R09

**Alfred Tarski. “A lattice-theoretical fixpoint theorem and its applications.”** *Pacific Journal of Mathematics* 5(2), 285–309, 1955. DOI: `10.2140/pjm.1955.5.285`. [Publisher](https://msp.org/pjm/1955/5-2/p05.xhtml).

Order-theoretic fixed-point reasoning is an established foundation. The paper's finite dependency-closure argument uses an elementary finite instance: adding reachable requests stabilizes when no new request is added. It does not identify the entire effectful compiler with a monotone fixed-point evaluator, and it does not present the closure argument as new mathematics.

## R10

**David L. Parnas. “On the criteria to be used in decomposing systems into modules.”** *Communications of the ACM* 15(12), 1053–1058, 1972. DOI: `10.1145/361598.361623`. [Publisher](https://doi.org/10.1145/361598.361623).

Information hiding and responsibility-based decomposition supply a useful context for the compiler's separation into acquisition, naming, classification, language, target architecture, binding, and filesystem services. The history of refactoring a large compiler into specialized collaborators is described in [provenance](../foundations/provenance.md). The correspondence concerns boundaries and change ownership, not compliance inferred merely from having many classes.

## R11

**LLVM Project. LLVM Language Reference Manual.** [Official reference](https://llvm.org/docs/LangRef.html).

Intermediate representations separate source from target and give transformations a defined object to manipulate. JCB's concern-specific records and prepared fragments perform intermediate roles. A registry of text does not acquire the type, control-flow, or SSA properties of LLVM IR simply because both are intermediate. The paper uses the role-level comparison while retaining the concrete structure of JCB's stores.

## R12

**PHP Documentation Group. `str_replace`.** [Official manual](https://www.php.net/manual/en/function.str-replace.php).

Array-based string replacement processes entries in order, which can affect subsequently introduced text. JCB's placeholder action modes add their own map-selection rules. The exact composition is defined in [binding](../compiler/binding.md) and [staging](../formal/staging.md), and tested in the executable companion. This technical reference is included because substituting a superficially similar algorithm would alter behavior.

## R13

**PHP Framework Interop Group. PSR-4: Autoloader.** [Official specification](https://www.php-fig.org/psr/psr-4/).

Namespace-to-path mapping supplies a relevant target-platform convention for reusable code placement and autoloading. JCB adds stable Power identity, local acquisition, contextual namespace processing, per-file import aliases, and selected source placement around those conventions. PSR-4 is a naming/loading contract, not a complete description of that compiler workflow.

## R14

**H. Penny Nii. “Blackboard Systems: Part One—The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures.”** *AI Magazine* 7(2), 38–53, 1986. DOI: `10.1609/aimag.v7i2.537`. [Publisher](https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v7i2.537).

Specialized producers and consumers cooperating through shared state have a family resemblance to blackboard organization. JCB's observed execution is explicitly orchestrated, however; the presence of shared stores does not establish opportunistic blackboard scheduling. The useful connection is coordination through retained information with defined responsibilities.

## R15

**Todd J. Green, Grigoris Karvounarakis, and Val Tannen. “Provenance semirings.”** *Proceedings of PODS*, 31–40, 2007. DOI: `10.1145/1265530.1265535`. [Publisher](https://doi.org/10.1145/1265530.1265535).

Provenance research studies how contributing inputs relate to a result. The paper's occurrence–contribution–artifact relation uses that general question to organize source traces. It does not assert that JCB implements a provenance semiring or records a complete provenance graph during every build. The trace relation is a tool for explanation and verification.

## R16

**Walid Taha and Tim Sheard. “Multi-stage programming with explicit annotations.”** *Proceedings of PEPM*, 203–217, 1997. DOI: `10.1145/258993.259019`. [Publisher](https://doi.org/10.1145/258993.259019).

Explicit staging provides a vocabulary for separating preparation from later computation. JCB's deferred work, retrieval-time contextualization, and ordered file binding exhibit different staging responsibilities. String substitution does not inherit the scope and type guarantees of a staged programming calculus; the account states its actual replacement semantics instead.

## Correspondence without flattening the architecture

These references identify several established tools for understanding the implementation. No single comparison replaces the complete account. Attribute computation does not alone specify blueprint transport; mapping labels do not alone specify local persistence; memoization does not specify deferred effectful work; protected regions do not specify field permissions or target-aware class placement.

The architectural object studied here is their implemented coordination around reusable definitions and complete generated applications. Its originality is presented through the attributable implementation and the particular organization described, while established principles receive their own credit. A reader can use the references to deepen any part of the account and the [source map](source-map.md) to inspect how JCB realizes it.
