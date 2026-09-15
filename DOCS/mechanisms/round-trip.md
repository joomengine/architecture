---
title: Round-trip editing and preservation laws
description: A partial bidirectional contract for preserving marked adaptations without claiming to invert arbitrary generated code.
section: Mechanisms
order: 36
evidence: Formal model and deductions
---
# Round-trip editing and preservation laws

## The output becomes a bounded input

The round-trip profile adds a controlled path from generated artifacts back into persistent source knowledge. A human can edit a designated region, the system can recover that region using explicit conventions, and the next build can reinsert the adaptation.

The adjective **bounded** is essential. The system is not required to infer every possible semantic change from arbitrary edited output. It recognizes an admissible edit language and a set of regions with stable identities.

## A precise domain

Fix a source snapshot $D$ and a finite set $S_D$ of editable region identities. Let $\mathcal{M}_D$ contain canonical maps assigning a byte string to every region in $S_D$. This includes default content where necessary; a delta-only overlay needs a separate normalization that supplies defaults.

Define a partial renderer and extractor:

$$
\operatorname{put}_D:\mathcal{M}_D\rightharpoonup\mathcal{A}_D,
\qquad
\operatorname{get}_D:\mathcal{A}_D\rightharpoonup\mathcal{M}_D.
$$

The admissible artifact domain requires unambiguous region markers, unique region identities, a valid ownership mapping, and content that does not violate the marker grammar. The renderer preserves the identity markers while placing each region's content into its assigned location.

## Proposition 7 — extraction after rendering

Assume each region is emitted exactly once, markers are parseable and unambiguous, content is preserved byte-for-byte within the declared encoding, and no later stage alters a preserved region. Then

$$
\operatorname{get}_D(\operatorname{put}_D(M))=M.
$$

**Proof.** For each $s\in S_D$, unique markers identify precisely the byte interval written from $M(s)$. Extraction returns that interval under the same identity. Equality holds pointwise over the common domain $S_D$. $\square$

If a later stage rewrites tokens inside editorial content, the law must instead be stated over a canonicalized region representation or tested after a documented reverse transformation. Raw-byte preservation cannot be claimed simultaneously with an unspecified rewriting stage.

## No-edit stability

Let $\mu$ reconcile a canonical extracted region map with persistent memory and satisfy $\mu(M,M)=M$. Then

$$
\mu(M,\operatorname{get}_D(\operatorname{put}_D(M)))=M.
$$

This is the formal no-edit round-trip law. It concerns authoritative editorial memory, not every timestamp or packaging byte in a build.

## Admissible edit conservation

Let $A'$ differ from $\operatorname{put}_D(M)$ only within admitted region bodies, without changing their identities or violating syntax. With $M'=\operatorname{get}_D(A')$, Proposition 7 gives

$$
\operatorname{get}_D(\operatorname{put}_D(M'))=\operatorname{get}_D(A').
$$

Thus the next rendering preserves those edited bodies. Unmarked changes outside the owned regions are not covered and may be regenerated from source.

## What changes when the generator changes?

When $D$ changes, the region set can change. A removed or renamed region cannot be silently assumed to have a destination. Reconciliation must apply an explicit migration, retain the record as an orphan requiring attention, or reject publication. This is a cross-epoch problem, not a consequence of the fixed-$D$ law above.

## Relationship to bidirectional transformations

The preservation laws are related to lens-style reasoning about updating a view and recovering source information. JCB's marker-and-fingerprint mechanism is a specialized operational realization, not evidence that it implements a general well-behaved lens calculus. The distinction is important because generated output often contains much information that was never editable source. [R03](../reference/bibliography.md#r03)

See [reconciliation](reconciliation.md) for merge policy and [editorial recovery in JCB](../jcb/editorial-recovery.md) for the observed implementation.
