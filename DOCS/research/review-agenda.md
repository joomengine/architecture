---
title: Review agenda and extension boundaries
description: The claims reviewers should challenge, the evidence still needed, and how the framework can grow without blurring its guarantees.
section: Research
order: 92
evidence: Research agenda
---
# Review agenda and extension boundaries

## Review the contribution at three levels

First, assess the historical and source account: does the cited implementation exhibit the mechanisms described, and are its limitations represented fairly? Second, assess the formal model: are definitions coherent, assumptions sufficient, and proofs valid? Third, assess usefulness: do independent implementations and controlled comparisons demonstrate a practical advantage?

These questions can have different answers. A valid finite closure proof does not establish historical novelty. A successful production compiler does not prove a cognitive hypothesis. A useful abstraction can be valuable even when its constituent mathematics is established.

## Formal questions

The finite positive model deliberately excludes unrestricted negative conditions, destructive updates, and unbounded occurrence expansion. Reviewers should examine whether the chosen strata and epoch boundaries adequately describe the intended applications.

The round-trip law assumes unique, admissible regions and unchanged interpretation within a build. Reviewers should challenge how a real system handles shared-definition edits, disappearing regions, ambiguous relocation, and transformations inside preserved content. Those are not peripheral edge cases; they determine the boundary of the preservation claim.

## Source questions

A complete dynamic audit of JCB should record actual dependency acquisition, state mutation, hook effects, and final artifact changes. The current static case study does not supply that trace. Feature-specific history would also refine the introduction dates of modern recovery and dependency mechanisms without changing the root implementation provenance already documented.

A source audit should not force JCB into the abstract machine. It should identify which contracts the implementation realizes directly, which it realizes through a different mechanism, and which remain proposed improvements.

## Empirical questions

The reported large build deserves a reproducible benchmark with explicit input, output, hardware, timing, and correctness boundaries. The cost of templates, copied libraries, packaging, and external acquisition must be visible. Controlled ablations can then identify whether registry reuse, batching, staging, or other factors explain the result.

Cross-language reimplementation is especially valuable because it tests whether the framework communicates enough meaning independently of PHP/Joomla conventions.

## Extension policy

Probabilistic retrieval, learned ranking, distributed stores, incremental truth maintenance, typed AST emitters, and stronger transactional publication are plausible extensions. Each should state which existing propositions remain valid and which need new assumptions or a new proof.

A versioned specification should preserve a small, intelligible core. Adding every useful technique to the definition would make conformance impossible to distinguish from general software engineering.

## Scholarly status

This edition is an AI-assisted research exposition prepared for the originator's review, with source-grounded observations and original formal specification text. It is not represented as an awarded doctoral thesis, an accepted journal article, or a completed independent peer review. Author approval and subsequent external review are substantive steps, not cosmetic labels.

Contributions, counterexamples, and corrections are welcomed through the repository workflow. The goal is a stronger, more transferable account, not protection of a claim from criticism.
