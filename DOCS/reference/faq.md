---
title: Questions and answers
description: Direct answers about the theory's contribution, provenance, mathematical status, portability, licensing, and evidence.
section: Reference
order: 104
evidence: Summary of the specification
---
# Questions and answers

## Is VDMT just a new name for a dictionary or template engine?

No. A dictionary supplies storage and a template engine supplies one rendering mechanism. VDMT specifies how context is acquired and completed, how definitions are distinguished from occurrences, how derived information is scoped and bound, and how admitted edits can become persistent input. A system using a dictionary does not automatically implement those contracts.

## Is it one algorithm?

It is a formal architectural framework containing a family of algorithms and conformance profiles. A worklist, nested calls, batched acquisition, or another correct mechanism can realize context completion. The [definition](../foundations/definition.md) states the minimum commitments.

## Why call it a theory when JCB already works?

An implementation demonstrates a construction. The theory explains and generalizes its organization, specifies laws, and proposes testable consequences. Working software does not by itself prove every explanation or optimality claim. This edition is a research white paper and formal specification, not a claim of an awarded degree.

## When was the method public?

Its originating public-source implementation is recorded in JCB's root commit of **30 January 2016, 20:28:43 UTC**. The compiler in that tree already contains specialized builder memory and staged file construction. This manuscript's formal edition is dated 2026. [Provenance](../foundations/provenance.md) distinguishes those records.

## Who developed it?

The originating architecture is attributed to **Llewellyn van der Merwe**, working through Vast Development Method. The root commit and compiler header support that attribution. His account of independent development is retained as author testimony, while prior related work is credited.

## Must an implementation use PHP or Joomla?

No. The contracts concern identity, context, state transitions, binding, and preservation. JCB is the originating case study, not a required runtime. See [portability](../engineering/portability.md).

## Are the registries physically moving the same memory around?

Not necessarily. A transition can share an object, copy a value, derive a new form, or retain a key. VDMT primarily describes logical information roles and lifetimes. Physical allocation and cache behavior require separate measurement.

## Does JCB's self-build prove Turing completeness?

No. Self-generation of a generator-bearing application and universal computational expressiveness are different properties. The precise self-build claim and reproducibility protocol are in [self-generation](../mechanisms/self-generation.md).

## Does the round trip preserve every edit?

Only edits in the declared admissible domain. Marked-region recovery is not a general inverse compiler. Unknown, malformed, duplicated, or migrated regions require a defined conflict or migration policy. Unmarked output may be regenerated from source.

## Is the million-line performance example independently verified here?

No. It is retained as an author-reported observation. The [benchmark protocol](../engineering/benchmarks.md) explains how to reproduce and evaluate it without confusing generated lines with manually authored source or omitting template and library inputs.

## Is this the optimal human-memory design?

That is not established. The [research program](../research/hypotheses.md) proposes bounded engineering and cognitive comparisons. An optimality claim needs a workload class, objective, constraints, and evidence that distinguishes alternatives.

## Can others implement and extend it?

Yes. The paper uses CC BY 4.0 for original explanatory material and MIT for original reference code. Attribution is required when reusing licensed expression. Copyright does not create exclusive ownership of mathematical ideas or independently implemented algorithms. See [licensing](licensing.md).

## Where is the Markdown for a page?

Use its **Read Markdown** or **Download Markdown** action. Every article is authored in `DOCS/`, and the build publishes the exact source bytes under `/markdown/`. The complete corpus and manifest are linked from every page's publication navigation.
