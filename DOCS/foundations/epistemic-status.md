---
title: Evidence and claim status
description: A taxonomy that separates implementation observations, historical evidence, testimony, proofs, proposals, and empirical hypotheses.
section: Foundations
order: 12
evidence: Methodology
---
# Evidence and claim status

A scientific architectural account must state more than its conclusion. It must identify the object of the conclusion and the evidence that supports it. This paper uses six classes.

## S — Source observation

A claim about behavior directly visible in identified source code. It includes a revision, path, and relevant method or line range. Example: JCB's `Initializer::init()` invokes custom-code extraction before `Component::build()` at the pinned contemporary revision. This establishes the visible orchestration order, not the absence of every indirect read or side effect in constructors and extensions.

## H — Historical record

A claim supported by a dated repository object, release, manifest, or preserved source header. The 2016 root commit is such a record. A copyright notice or file header may report a creation date; it is not a substitute for inspection of the code at that historical revision.

## A — Author testimony

A statement supplied by Llewellyn van der Merwe about development history, intention, practical operation, or an observed performance result. His report of independent development and his approximate pre-publication start date belong here. Testimony is evidence of the author's account; it should neither be erased nor silently relabeled as an independent experiment.

## F — Formal model or deduction

A definition, abstraction, proposition, or proof in this paper. A proposition is conditional on its listed assumptions. Proofs about a finite monotone model do not certify unrestricted PHP callbacks. Equally, a source limitation does not invalidate a clearly labeled generalization; it defines an implementation gap to investigate.

## P — Proposed implementation extension

A design not established as present in the inspected JCB source, such as a comprehensive provenance graph, transactionally atomic publication, a generic lattice scheduler, or complete dependency invalidation. Such proposals may strengthen future implementations but must not be presented as discoveries already implemented in JCB.

## E — Empirical hypothesis or measurement

A hypothesis proposes an observable distinction. A measurement records a specified experiment. These are different subtypes: a benchmark plan is not a benchmark result. This repository's reference-model tests and example timings concern the reference model, not a full JCB build.

## Scope of this edition

The case study combines static inspection of selected contemporary compiler paths, inspection of the root historical compiler, and the author's account of the system's practical behavior. It is not a full dynamic trace of a live Joomla installation. The source map identifies what was examined. Neither a source comment nor a method name alone establishes an algorithmic invariant.

The formal framework is an explanatory extraction and proposed specification. It is not represented as a previously peer-reviewed mathematical theory. Its propositions include proofs and counterexamples so that reviewers can test the assumptions rather than accept the terminology on authority.

## Reading mixed claims

An article may contain several evidence classes. For example, marked-code extraction is **S**; its relationship to bidirectional transformations is an interpretive comparison; the round-trip law defined here is **F**; and a future transactional reconciler is **P**. Page-level labels identify the dominant status, while the prose marks important changes of status.

## Publication discipline

Do not infer novelty from the absence of a citation in implementation source. Do not infer universal superiority from successful use. Do not infer that a method was absent in 2016 because its modern class name was introduced later. Conversely, do not date a modern feature to 2016 merely because it now belongs to the same project.

This discipline protects both the originator's attributable contribution and the reader's ability to reproduce, criticize, and extend the work.
