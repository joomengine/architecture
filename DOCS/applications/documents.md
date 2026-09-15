---
title: Application to document synthesis
description: Structured evidence, reusable sections, occurrence-specific interpretation, and controlled editorial feedback in reports and publications.
section: Applications
order: 81
evidence: Proposed application
---
# Application to document synthesis

## Treat claims as structured inputs

A report generator can recollect evidence records, resolve referenced datasets, derive tables or summaries, and assemble a publication. The important unit is not merely a paragraph string. It is a claim or content item with provenance, scope, revision, and an identified role in the document.

For example, one study result may appear in an executive summary, a technical discussion, and an appendix. These are different occurrences of the same source evidence. Their wording and detail can vary, but their attribution and interpretation should remain consistent.

## Context-sensitive reuse

A reusable section definition can receive an audience, jurisdiction, reporting period, or product context. Those parameters belong in its interpretation key. A cached paragraph from one reporting period must not silently appear in another merely because both sections share a title.

Aggregates should be calculated after the contributing evidence set is closed. A statement such as “all included studies support the conclusion” is not valid while inclusion is still being resolved. Negative claims require a declared search boundary and evidence policy.

## A bounded editorial loop

A document can designate editable narrative regions while retaining generated tables and citations under source control. Extraction recovers only those owned regions. The reconciler detects whether both the evidence-derived baseline and the human text have changed.

A new dataset may make a preserved paragraph obsolete even when its markers remain intact. Byte-preservation is therefore not enough: the application needs a review rule connecting editorial regions to the evidence they discuss. VDMT can record that dependency, but cannot determine scientific truth merely by retaining text.

## Multiple publication formats

One Markdown source can produce HTML and a raw Markdown alternate, as this publication does. A document system could additionally emit PDF or another structured format. Each output has its own serialization and validation requirements; equivalent meaning does not require byte equality across formats.

The same-source rule reduces drift between formats. It does not eliminate renderer defects, broken links, or mathematical notation problems. Publication tests should validate the actual rendered outputs rather than only the source text.

## Evaluation

Compare source consistency, stale-claim rate, editorial preservation, build reproducibility, and review effort against a manually synchronized multi-format workflow. Keep human evaluation separate from syntactic correctness: a complete, correctly rendered document can still be poorly argued.

The [citation](../reference/citation.md) and [publication](../reference/publication.md) pages describe this repository's own source-to-page contract, which is a narrow demonstrator of staged document synthesis, not a claim that the website implements every VDMT profile.
