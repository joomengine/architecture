---
title: White paper
description: The integrated argument and formal account of contextual recollection, staged synthesis, and persistent editorial reconciliation.
section: Overview
order: 1
evidence: Formal framework, source observations, and research hypotheses
---
# Vast Development Method Theory

**Contextual recollection, staged synthesis, and persistent editorial reconciliation**  
**Llewellyn van der Merwe · Vast Development Method**  
Version 0.1.0 · 15 September 2026

## Abstract

Systems that synthesize large artifacts from compact structured descriptions must coordinate acquisition, reuse, contextual interpretation, and output construction. When generated artifacts are also editing surfaces, they must additionally preserve selected human adaptations without treating arbitrary output as authoritative source. Vast Development Method Theory (VDMT) specifies an architectural framework for this combination. Its central construction is a context-qualified knowledge state completed through bounded dependency discovery and guarded derivation, projected through reusable definitions and distinct occurrences into an ordered artifact plan, and connected across build epochs by partial editorial extraction and reconciliation.

The framework separates an inner knowledge-completion loop from an outer development loop. For a finite positive fragment, the paper proves stabilization, least closure, and closure-operator laws. It states conditions for deterministic staged output and schedule-independent saturation, and gives a partial round-trip law for uniquely identified admissible regions. These results concern the explicit model, not unrestricted production callbacks. Joomla Component Builder supplies the originating implementation case study and a public source lineage from 30 January 2016. Static inspection supports specialized intermediate stores, nested acquisition, context-sensitive reuse, staged file binding, and recovery of marked edits. The paper identifies differences between that implementation and the stronger portable contracts. Performance and cognitive-recollection interpretations are developed as falsifiable hypotheses rather than asserted as universal optimality.

## 1. Problem and contribution

A source description is rarely already arranged in the form required by every output. A field definition may contribute to a database schema, an edit form, a validation routine, a query, and several language entries. The same definition may be used in different views with different permissions or naming contexts. A view may occur in several components. One artifact may aggregate many occurrences, while another is emitted once for each occurrence.

A simple source-to-template picture hides three difficult questions. What information must be acquired before an interpretation is complete? Which results may be reused without confusing their contexts? What happens when an existing generated artifact contains an intentional human adaptation?

VDMT addresses those questions through explicit contracts. It is not a claim to have invented dictionaries, fixed points, compiler passes, or bidirectional transformations. Its proposed contribution is a language-independent specification of their particular composition, drawn from an implemented architectural lineage and made suitable for independent review and reimplementation. The [formal definition](foundations/definition.md) describes core, round-trip, incremental, and self-generative profiles rather than requiring every implementation to support every extension.

The technical descriptor is **context-closed, occurrence-sensitive staged synthesis with partial bidirectional editorial reconciliation**. “Memory” in this account concerns logical availability, identity, scope, and lifecycle. It does not prescribe physical addresses or claim an optimal heap allocator.

## 2. Method and evidence

The analysis combines the originator's account, static inspection of selected executable paths at pinned JCB revisions, comparison with established literature, and an original abstract specification with a small executable reference model. It distinguishes source observations, historical records, author testimony, formal deductions, proposed extensions, and empirical hypotheses. The [evidence taxonomy](foundations/epistemic-status.md) applies throughout.

The contemporary case study uses commit `bca4a1520484f3e2c2fbd12964a5995b0d058de1`; the historical comparison uses root commit `ecf47809f960bd057af8a414168fada6fe22c5f7`. This is not a complete dynamic trace of a live Joomla installation. The reference-model tests exercise the abstract contracts and are not presented as a full JCB benchmark or self-build certificate.

## 3. State, identity, and interpretation

For one build epoch, fix the complete input

$$
I_e=(D_e,M_e,\Theta_e,C_e,E_e),
$$

where $D_e$ is durable source knowledge, $M_e$ validated editorial memory, $\Theta_e$ rules and templates, $C_e$ task and target configuration, and $E_e$ the relevant environment. The environment includes any version, locale, clock value, or external dependency allowed to affect output.

A machine state contains a phase, discovered and completed requests, established knowledge, intermediate stores, an artifact plan, staged outputs, provenance, and errors. Its transitions identify what they read and write. A registry is one possible representation of a store; it is not the mathematical definition of the store's role.

Three identities are fundamental. A definition identifies reusable source knowledge. An occurrence identifies a use of that definition under a context $\Gamma$. An artifact identifies a planned output. A destination path is an attribute of the artifact and need not be the enduring identity of its definition or editable regions.

Interpretation therefore has the form $J(d,\Gamma)$ rather than simply $J(d)$. Reusing a result across two contexts is justified only when their relevant dimensions agree:

$$
\Gamma_1\sim_J\Gamma_2\Longrightarrow J(d,\Gamma_1)=J(d,\Gamma_2).
$$

A conservative implementation includes every relevant context dimension in its cache key. An optimized implementation may use a smaller projection only with a justified dependency contract. [Identity](mechanisms/occurrence-identity.md) and [composition](semantics/composition.md) develop this distinction.

## 4. The inner loop: completing the context

Resolving a request can reveal further requests. Loading a view reveals fields; loading a field reveals its type and custom dependencies. The visible implementation may use nested loops, recursion, batched queries, or a worklist. The semantic operation is dependency completion, not a requirement for exactly two loops or two passes.

For a stable resolver on a frozen epoch, write

$$
\rho_e(q)=(F_e(q),\operatorname{deps}_e(q)).
$$

Starting with task roots $Q_0$, accumulate

$$
Q_{n+1}=Q_n\cup\bigcup_{q\in Q_n}\operatorname{deps}_e(q).
$$

A completed-request set prevents redundant visits when request identity is stable. A finite graph can contain cycles without preventing traversal termination. However, a resolver whose answer depends on newly derived knowledge may need to be revisited; a permanent visited flag is then insufficient. [Context closure](semantics/context-closure.md) states both cases.

After or alongside acquisition, positive rules can derive additional facts. Let $U$ be a finite, consistent fact universe and $G$ a deterministic monotone consequence operator. Define

$$
F(K)=K\cup G(K),\qquad K_{n+1}=F(K_n).
$$

Every strict transition adds a fact from the finite set $U\setminus K_0$. Hence there are at most $|U\setminus K_0|$ strict growth rounds. The stabilized result is the least closed superset of the seed: induction shows that each intermediate state lies inside every closed superset containing the seed. Consequently, the closure is extensive, monotone, and idempotent:

$$
K\subseteq\operatorname{cl}(K),\qquad
\operatorname{cl}(\operatorname{cl}(K))=\operatorname{cl}(K).
$$

These are established forms of fixed-point reasoning, here applied explicitly to the bounded architecture. The [full proofs](semantics/fixed-points.md) credit the prior mathematical foundation. [R01](reference/bibliography.md#r01)

Absence tests, overwrites, and changing aggregates do not automatically satisfy this model. A fallback based on “no label exists” should be evaluated after its authoritative source stratum is closed. An ordered field list should be rendered after its membership and ordering are established. Arbitrary source mutation is handled between epochs or under a separately specified effect contract.

## 5. Hierarchical reuse and output expansion

A shared definition graph and its occurrence expansion are different structures. A field type can support many fields, a field can occur in many views, and a view can occur in several components. Values synthesized from one view occurrence can then fan out into several files. Rules also exhibit fan-in when several premises jointly determine one fragment.

This explains how a relatively compact model can generate a much larger artifact set. It does not imply that the database creates information from nothing: templates, rules, target conventions, reusable libraries, and copied assets are additional inputs.

A worked example in [hierarchical reuse](mechanisms/hierarchy-and-reuse.md) has three field definitions but eight field occurrences, two view definitions but three view occurrences, and eighteen planned files under explicit singleton and per-view cardinality rules. The example is synthetic and separates counts of definitions, occurrences, and artifacts rather than treating them as one scale measure.

The same distinction prevents scope errors. Sharing a field definition is useful; sharing a mutable occurrence-specific label across unrelated components is not. Logical reuse is successful when it preserves contextual meaning, not merely when it reduces allocation count.

## 6. Staged binding and materialization

An artifact plan records logical identity, destination, emitter, context, and binding stages. Rendering is a composition

$$
A^{(0)}=T,\qquad A^{(i+1)}=\sigma_i(A^{(i)},P_i),
$$

where $P_i$ is the authoritative environment for stage $i$. Staging makes late values and unresolved obligations explicit. A token introduced after its owning stage has finished requires pre-binding, a declared later pass, or rejection; an unspecified “repeat until finished” loop hides both ordering and termination hazards.

Simultaneous non-recursive substitution and sequential replacement are different semantics. The reference model chooses the former within each explicit pass. JCB's inspected placeholder implementation uses PHP's array-based `str_replace`, whose order can affect introduced text. Its action 3 filters unused replacement-map entries, not unknown tokens in the output. [J08](reference/bibliography.md#j08), [R12](reference/bibliography.md#r12)

Physical file creation can precede semantic completion. A compiler may copy skeletons, populate intermediate stores, and later update the files. VDMT therefore distinguishes incomplete staged artifacts from validated outputs rather than requiring a rigid all-data-before-any-file chronology.

Deterministic output follows conditionally when source and environment are fixed, discovery and derivation have unique results, conflicts and ordering are explicit, rendering is deterministic, and publication preserves the rendered bytes. The [determinism proposition](semantics/determinism.md) proves that composition. The [confluence proposition](semantics/confluence.md) separately addresses schedule-independent positive saturation; a repeatable fixed schedule does not by itself establish confluence.

## 7. The outer loop: persistent editorial reconciliation

The round-trip profile allows an output to become a bounded source of new knowledge. It recognizes designated editorial regions, extracts their content, reconciles changes with persistent records, and uses the result in the next synthesis epoch. It does not infer every possible semantic change from arbitrary edited output.

For a fixed source $D$, let $S_D$ be the finite region-identity set and $\mathcal{M}_D$ complete canonical region maps. Define partial functions

$$
\operatorname{put}_D:\mathcal{M}_D\rightharpoonup\mathcal{A}_D,
\qquad
\operatorname{get}_D:\mathcal{A}_D\rightharpoonup\mathcal{M}_D.
$$

If every region is emitted exactly once, markers are unambiguous, admitted bodies are preserved, and no later stage changes them, then extraction recovers each written interval under the same identity:

$$
\operatorname{get}_D(\operatorname{put}_D(M))=M.
$$

With an idempotent no-change reconciliation policy $\mu(M,M)=M$, a no-edit round trip leaves authoritative editorial memory unchanged. Admissible edits to region bodies can therefore survive regeneration. If reverse transformations operate inside the bodies, the law must instead name the canonical representation they preserve. The [round-trip article](mechanisms/round-trip.md) provides the domain and proof.

Reconciliation is not merely extraction. A useful whole-region three-way policy compares the previous baseline $b$, current source $s$, and extracted user value $u$. If $u=b$, retain $s$; if $s=b$, accept validated $u$; if $u=s$, retain their agreement; otherwise report a conflict. Shared definitions, removed regions, and path migrations require explicit ownership and migration policies.

The cross-epoch relation is

$$
M_{e+1}=\mu(M_e,X(A'_e)),\qquad
A_{e+1}=B(I_{e+1}),
$$

with extraction partial and reconciliation permitted to fail. Unlike positive accumulation within one epoch, this outer loop may replace or remove information. It need not converge while humans continue developing the system. Lens-style bidirectional transformation research is a close precedent for reasoning about such laws, but the marker-bounded mechanism does not claim a general lens calculus. [R03](reference/bibliography.md#r03)

## 8. Originating implementation and historical record

JCB's root commit records **30 January 2016 at 20:28:43 UTC**, names Llewellyn van der Merwe as author and committer, and contains the early compiler. That compiler already has specialized builder arrays, static/dynamic content memory, component-data loading, staged structure construction, and later file updating. This is substantive evidence of the method's public implementation lineage, not a date inferred solely from a license's copyright year. [J01](reference/bibliography.md#j01), [J02](reference/bibliography.md#j02)

The source header reports creation on 30 April 2015. Llewellyn places private beginnings approximately two years before public release and reports independent development without prior awareness of the related theories surveyed here. Those recollections are retained as author testimony. The 2026 manuscript, current class arrangement, and every later feature are not retroactively dated to 2016.

The contemporary initializer recovers custom code before component building and build-directory reset. Component enrichment and field-data services demonstrate nested acquisition and context-sensitive reuse. `ContentOne` and `ContentMulti` supply shared and view-scoped binding environments. The file writer applies shared bindings before view bindings, then conditional custom-code processing and power injection. Dependencies can still be acquired during file updating. [J04](reference/bibliography.md#j04)–[J12](reference/bibliography.md#j12)

The extractor scans eligible file types in active installed targets, recognizes marker families, delegates GUI-code recovery, reverse-transforms captured content, and maintains insert/update buffers with location information and contextual fingerprints. The later compiler phase handles stored custom-code injection. These mechanisms support the outer-loop interpretation while leaving universal preservation and conflict handling as stronger claims requiring explicit tests.

## 9. Self-generation and expressive scope

The author reports that JCB builds JCB, and the pinned README identifies the component as created with JCB. This is self-generation of the generator-bearing application and can support a bootstrapping workflow. It is not automatically a PHP-language compiler compiling itself. [J03](reference/bibliography.md#j03)

A stronger certificate would freeze a seed, model, dependencies, and environment; generate and activate successive instances; and compare later outputs under a declared equivalence. Stable reproduction is meaningful evidence for that model. It neither proves Turing completeness nor resolves seed trust. Established compiler bootstrap and trust literature supplies the comparison and caution. [R06](reference/bibliography.md#r06), [R07](reference/bibliography.md#r07)

## 10. Costs, performance, and cognitive hypotheses

The build cost separates acquisition, discovery, derivation, planning, binding, writing, validation, and packaging. Reuse can reduce repeated acquisition and derivation, but writing $B$ requested output bytes still costs $\Omega(B)$ in a byte-charging model. Large intermediate stores can also increase peak memory. There is no universal advantage to retaining every value.

The author reports approximately 30,000 input-associated lines becoming 1.3 million generated lines in about 60 seconds. This edition does not independently reproduce that build. The [benchmark protocol](engineering/benchmarks.md) specifies complete inputs, independent artifact counting, cold/warm conditions, repeated runs, correctness-equivalent comparators, and mechanism ablations.

The recollection analogy motivates a further research program. Context-qualified retrieval, reusable interpretations, and accountable correction can be useful engineering mechanisms for external AI memory. However, human cognitive theories include commitments about timing, capacity, error, learning, and specialized processing that do not follow from compiler registries. ACT-R and global-workspace research are credited comparison points, not validation of biological equivalence. [R10](reference/bibliography.md#r10), [R14](reference/bibliography.md#r14)

An optimality claim requires a workload class, admissible algorithms, objective, resource constraints, and a correctness relation. The present contribution is a framework that makes those questions testable, not a declaration that they have all been settled.

## 11. Conclusion

VDMT's central insight is to organize synthesis around **completed context, scoped interpretation, ordered materialization, and controlled persistent feedback**. The inner loop makes required knowledge available; the occurrence structure makes reuse meaningful; the binding plan makes output obligations explicit; and the outer loop preserves selected human decisions across regeneration.

JCB demonstrates an attributable implementation lineage of this composition. The formal model extracts portable contracts and proves bounded properties without claiming that every production mechanism satisfies the simplest assumptions. Independent implementations, dynamic source audits, preservation tests, and controlled benchmarks can now evaluate and extend the framework at clearly identified boundaries.

The full specification continues through the [reading guide](reading-guide.md), [source map](jcb/source-map.md), [implementation guide](engineering/implementation-guide.md), and [research agenda](research/review-agenda.md). Every article is available as its own Markdown source as well as a web page.
