---
title: Historical provenance and authorship
description: The public implementation date, author attribution, early source evidence, and the distinction between a method and a later formal edition.
section: Foundations
order: 13
evidence: Historical record and author testimony
---
# Historical provenance and authorship

## Historical public implementation date

**30 January 2016** is the date recorded for the initial public-source implementation in Joomla Component Builder's authoritative history. The root commit is `ecf47809f960bd057af8a414168fada6fe22c5f7`, with author and committer timestamp `2016-01-30T20:28:43Z`, no parents, and the message “first commit of free version.” Both identities name **Llewellyn van der Merwe**. At UTC+02:00, the timestamp is **22:28:43** on the same date. [J01](../reference/bibliography.md#j01)

The `LICENSE.txt` history leads to that commit. More importantly, the compiler included in the same tree already contains the characteristic combination of dedicated builder arrays, static and dynamic content collections, database-loaded component data, template-based file construction, and a subsequent file-content update pass. [J02](../reference/bibliography.md#j02)

The historical claim is therefore substantive: the architecture was embodied in distributed executable source, not merely named in a later biography. A Git commit records repository history and timestamps; it is not, by itself, an independent timestamping authority or a complete log of a hosting service's past visibility settings. This edition uses the root public-source history, together with the author's account, as its disclosure record rather than claiming a separate legal determination of priority.

## Development before public release

Llewellyn places the beginning of private development approximately two years before public release. That makes **around 2014** an approximate author-reported origin, not an exact day. The historical compiler header separately records `@created 30th April, 2015`, `@build 30th January, 2016`, and his authorship. Those are different milestones and are preserved as such. [J02](../reference/bibliography.md#j02)

A header date is evidence of what that source reports; it does not disprove earlier private experimentation. Nor should the approximate start be converted into a fabricated precise date.

## Attribution

The method's originator is **Llewellyn van der Merwe**, working through Vast Development Method. The primary evidence includes the root commit authorship and the original compiler header. The contemporary source retains that attribution. JCB's broader contributor community is not erased by attributing the architectural origin to its author.

The canonical project name is **Joomla Component Builder (JCB)**. The authoritative repository cited in this publication is `joomengine/Joomla-Component-Builder`; its project domain is linked from the pinned README. No knowledge of Joomla is required to use the abstract framework. [J03](../reference/bibliography.md#j03)

## Independent development and related work

Llewellyn reports that he developed the architecture independently, without prior awareness of the theories compared in this paper. We retain that statement explicitly as author testimony. Source history cannot prove what literature an author had or had not encountered. Independent development is compatible with convergence on useful ideas already studied elsewhere.

Accordingly, the paper credits fixed-point semantics, compiler staging, dependency-driven build systems, blackboard and working-memory architectures, and bidirectional transformations. It does not claim their invention or suggest that resemblance diminishes the engineering contribution of their particular composition in JCB.

## Method, implementation, and manuscript dates

Three dates must not be collapsed:

| Record | Date and status |
| --- | --- |
| Approximate private origin | Around 2014, author testimony |
| Historical source header creation | 30 April 2015, reported in the original compiler |
| Public-source implementation lineage | 30 January 2016, root JCB commit |
| This formal specification edition | 15 September 2026, version 0.1.0 |

The phrase “VDMT has a public implementation lineage from 2016” is appropriate. The phrase “this 2026 manuscript was published in 2016” is not. Similarly, the early builder arrays support a historical staged-memory interpretation, but they do not prove that every modern extraction, service, or dependency mechanism existed at the root commit.

## Preserving the record

Citations should retain full commit identifiers, source paths, and the edition of the theory. Future corrections should be additive and reviewable. A formal publication archive or DOI may be created later, but none is invented in this edition. See [citation guidance](../reference/citation.md) and [the historical case study](../jcb/historical-implementation.md).
