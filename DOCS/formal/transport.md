---
title: Transport equivalence and bounded reconstruction
description: Portable design preservation, local identity remapping, conditional regeneration equivalence, marked-region laws, and extrusion's reconstruction domain.
section: Formal Model
order: 75
evidence: Formalization of blueprint exchange, generated markers, and extrusion candidates
---
# Transport equivalence and bounded reconstruction

Export/import, regeneration, marked-code recovery, and extrusion cross different representation boundaries. Their useful laws must identify which information each transformation preserves. Raw database equality, equivalent application structure, and identical output bytes are different relations.

## The normalized portable design

Let $\beta(D)$ extract the blueprint-relevant design from local data: typed identities, selected properties, supported relationships, and asset identities/content under the export contract. Installation-local primary keys, unrelated records, and intentionally omitted configuration are outside that projection.

Define

$$
D_1\equiv_B D_2\quad\Longleftrightarrow\quad\beta(D_1)=\beta(D_2).
$$

Equality includes relationship roles and relevant ordering. An ordered field association cannot be replaced by an unordered set merely because it contains the same field GUIDs.

For local identity maps $\lambda_1$ and $\lambda_2$, a transported relationship commutes with realization when both endpoints resolve to the same portable entities:

$$
\operatorname{portable}(\lambda_i(u))=u.
$$

Local row numbers can differ while this relation is preserved.

## Proposition: design preservation through transport

Assume export serializes every selected property and required relationship in $\beta(D)$ without loss; required assets are retained; import uses the corresponding decoding and identity rules; and the selected existing-item policy accepts the transported state. Then the imported design $D'$ satisfies $D'\equiv_B D$.

**Argument.** Each selected entity property is recovered by the corresponding decode operation. Typed identities recover the same vertices. Relationship keys recover the same endpoints, roles, and ordered association values. The asset condition preserves the selected resource observations. Thus every component of $\beta(D')$ equals the corresponding component of $\beta(D)$.

Ordinary local-first initialization does not meet the acceptance premise when an intentionally retained local definition differs from the remote one. Explicit reset is one way to choose another policy. The law describes a correctly scoped transport, not an instruction to overwrite local work indiscriminately.

## Regeneration equivalence needs the generation environment

Suppose compilation's selected artifact observation depends only on $\beta(D)$ and an environment $E$ containing target rules, supplied libraries, templates, hooks, and other output-affecting observations. Then

$$
D_1\equiv_B D_2\land E_1=E_2
\quad\Longrightarrow\quad
\operatorname{obs}_A(\operatorname{compile}(D_1,E_1))
=\operatorname{obs}_A(\operatorname{compile}(D_2,E_2)).
$$

The argument is substitution of equal effective inputs into the deterministic operation sequence. If a hook reads an omitted local property, the premise that compilation depends only on $\beta(D)$ no longer holds for that observation.

Editor-region markers can include local IDs; output can include dates or archive metadata. Comparing runtime structure may normalize selected metadata, while a byte-equality comparison must fix or identically normalize every such value. The comparison must publish its normalization, not delete inconvenient differences after seeing the result.

## Marker-bounded recovery

Let $S$ be a finite set of region identities and $M:S\to\mathcal{B}$ a map of admitted bodies. An emitter places each body in a uniquely identified region; an extractor recovers those regions.

If identities occur exactly once, delimiters are unambiguous, admitted bodies cannot forge structural delimiters, and no intervening operation changes a body, then

$$
\operatorname{extract}(\operatorname{emit}(M))=M.
$$

**Argument.** Each identity determines one non-overlapping interval. Emission places the corresponding body in that interval, and extraction returns precisely that interval under the same identity. Equality follows pointwise over $S$.

Where generation applies a specialization $s$ and recovery applies a canonicalization $r$, the needed condition becomes $r(s(m))=m$ on the admitted body domain. That condition must be checked for the actual transformations. A string-replacement reversal is not automatically an inverse on arbitrary text with ambiguous names.

JCB's GUI and fingerprint mechanisms have their own identity and placement domains. The existing-file commented fallback preserves recoverable code when automatic executable placement cannot be established. It is a different observation from successful placement at the original semantic location. [Custom code](../compiler/custom-code.md)

## Extrusion is evidence-based reconstruction

For artifact collection $A$, extrusion reads facts $H(A)$, resolves candidate model $Q$, and applies review decisions before writing. The result is a supported reconstruction, not necessarily the unique original model that produced the artifacts.

Non-uniqueness is concrete. The same ordinary database index can follow from an explicit index selection or from a title role. A SQL file alone cannot distinguish those origins. Table metadata, forms, associations retained elsewhere, and review decisions can supply additional information.

The reverse map is therefore naturally partial or set-valued before selection:

$$
\operatorname{candidates}(A)\subseteq\mathcal{D},
\qquad
\operatorname{extrude}(A,V)=\operatorname{select}(\operatorname{candidates}(A),V).
$$

The implemented resolver makes that selection through property precedence, identity/sharing rules, and pairing decisions. The chosen model can then enter normal compilation and become an explicit blueprint for future work.

## The common architectural result

These laws expose the useful invariants without collapsing distinct operations. Blueprint transport preserves a selected design representation. Compilation realizes it under target knowledge. Marked recovery preserves designated authored content under recognized transformations. Extrusion reconstructs represented structure from existing products.

Together they allow development intent to move between authoring, distribution, local editing, and deployable artifacts while retaining explicit identities and transformation rules. The [implementation guide](../engineering/implementation.md) translates those boundaries into a portable engineering design.
