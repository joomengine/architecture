---
title: How to cite and share the work
description: Edition-aware citations, source-specific references, raw Markdown URLs, and attribution for adaptations.
section: Reference
order: 102
evidence: Publication guidance
---
# How to cite and share the work

## Suggested citation

> van der Merwe, Llewellyn. *Vast Development Method Theory: Contextual Recollection, Staged Synthesis, and Persistent Editorial Reconciliation*. Version 0.1.0. Vast Development Method, 2026. https://theory.vdm.io.

When historical provenance matters, add: “Historical public implementation: Joomla Component Builder, root commit `ecf47809f960bd057af8a414168fada6fe22c5f7`, 30 January 2016.” Do not replace the manuscript year with 2016.

## Cite the object being discussed

For a definition or proposition, cite this edition and the focused article or heading. For behavior of JCB, cite the pinned source path and commit. For inherited mathematical or architectural concepts, cite the relevant original work in the [bibliography](bibliography.md).

A citation to the theory cannot substitute for evidence that a particular implementation satisfies its assumptions. Similarly, a source citation cannot by itself establish the validity of a psychological hypothesis.

## Machine-readable citation

The repository includes `CITATION.cff`, with the author's name, work title, edition, publication URL, repository, and license identifiers. It contains no invented ORCID, DOI, academic affiliation, or degree.

A DOI may be added if a future release is deposited with an appropriate archive. Until then, cite the version and repository commit for a reproducible reference.

## Sharing one article

Each article has a canonical HTML URL and a same-origin raw Markdown alternate. The page toolbar provides both reading and download actions. The raw file is the exact Markdown source used for that page, including its front matter; it is not a separately maintained summary.

For example, the formal state model is published as `/semantics/state-space/` and its Markdown as `/markdown/semantics/state-space.md`. Relative links between Markdown articles remain within the corresponding Markdown hierarchy.

## Sharing the whole edition

The build provides a complete Markdown corpus, a Markdown archive, an article manifest, and `llms.txt` / `llms-full.txt` discovery surfaces. The manifest records the SHA-256 digest of each article's source bytes. This supports checking whether a shared copy matches a particular build.

Hashes identify bytes, not scholarly quality or authorship by themselves. Retain the author, title, version, source URL, and license when redistributing the work.

## Adaptations and quotations

Mark an adaptation as adapted, identify its author, and preserve appropriate attribution to the original. Do not imply that Llewellyn or VDM reviewed or endorsed changes they have not approved. Third-party quotations and source code retain their own rights; the paper's CC BY license does not automatically apply to them.

See [licensing](licensing.md) for the exact scope and the controlling legal-code link.
