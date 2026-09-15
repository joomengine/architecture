---
title: Verification and traceability
ndescription: Source, artifact, mathematical, and runtime verification boundaries.
description: How source correspondence, public artifacts, executable mechanisms, mathematical arguments, and runtime builds establish different parts of the account.
section: Engineering
order: 84
evidence: Publication verification method and reproducible checks
---
# Verification and traceability

A useful architectural publication lets a reader move from a claim to the evidence appropriate to it. This edition combines implementation paths, public blueprint/product traces, mathematical arguments, executable reference mechanisms, and maintained build measurements.

These forms of evidence reinforce each other while answering different questions. A repository trace shows a generated artifact. A source path explains the operation that can produce it. A mechanism test checks a defined behavior. A runtime build exercises the full environment. A proof derives a conclusion under explicit assumptions.

## Source correspondence

The [source map](../reference/source-map.md) groups paths by responsibility and identifies the pinned core revision. The integrated extrusion scope is recorded separately so that a source link is never asked to support code absent from its revision.

A review follows the actual entry and calls through their collaborators, including constructor work, mutable state, events, deferred processing, and later file updates. Class names alone are not proof of ordering or guarantees. The prose uses inspected operations and distinguishes structural correspondence from a complete formal verification of every path.

## Public artifact traces

The Hello World trace connects typed source identities and code-property roles to generated artifacts. It checks the field GUID, database/form properties, derived index, language key, list behavior, marker destinations, module context, and plugin naming.

The inventory script operates on local pinned checkouts and records file counts, line counts, bytes, hashes, and selected marker matches. It does not execute imported code. The resulting manifest can be compared across source snapshots under the same selection rule.

Identical marker text in multiple properties is retained as a many-origin case rather than falsely assigned a unique provenance. Field identity and role provide stronger evidence than an unqualified substring match. [Custom-code trace](../examples/custom-code-trace.md)

## Executable mathematical mechanisms

The reference tests check typed requests, local-first policy, cyclic traversal, failed selection, property precedence, contextual contributions, deferred prerequisites, exact ordered substitution, and normalized design observations.

Those tests provide executable examples of the formal definitions. They do not replace Joomla integration tests. Keeping the model small permits exhaustive checks over selected small cases and makes a semantic change visible when an alternative implementation is tried.

The [formal chapters](../formal/notation.md) state assumptions explicitly. A termination argument requires a finite reachable request universe and terminating handlers. A reuse argument requires a key covering the relevant inputs. A transport law requires the selected design to be retained and accepted by the import policy.

## Full build reproduction

A complete reproduction records the compiler and blueprint revisions, local initialization/reset policy, repository and dependency versions, target, environment, hooks, and assets. It then imports or restores the selected model, runs compilation, retains diagnostics and timing, and compares the generated products under a declared observation.

For a fresh-instance transport test, local database primary keys can differ. The portable graph should be compared independently of those IDs. For byte comparison, local GUI markers, dates, archives, and other output-affecting values must be controlled or normalized by a rule stated before comparison. [Transport](../formal/transport.md)

The measured self-build record is an engineering observation from repeated use. A new reproduction adds a precisely packaged instance of that observation; it does not determine whether prior builds occurred.

## Review the interactions, not only isolated functions

Important checks cross concern boundaries: form and schema names, save/read storage transformations, permission-driven omission and persistence, query aliases and templates, language keys and catalogue entries, Power symbols and imports, deferred prerequisites and consuming phases.

A successful string replacement does not by itself establish those relationships. Tests should inspect the interpreted result or generated artifact relation that the operation is supposed to preserve.

Similarly, a completed extrusion can include skipped candidates and unresolved details. The report and selected writes must be reviewed together. The source's explicit recovery behavior should be tested as behavior rather than treated as an unspecified error.

## Publication validation

The website build checks article metadata, one primary heading per page, internal paths and anchors, canonical addresses, exact Markdown alternates, article hashes, complete downloads, and machine-readable indexes. Browser checks cover navigation, search, system-following/manual themes, mathematical rendering, diagrams, and narrow-screen layout.

These checks establish the integrity of the publication, not the runtime correctness of all JCB extensions. Their purpose is to ensure that the explanation, mathematics, and supporting evidence are actually accessible to readers.

## A stable basis for further work

The publication provides an explicit account against which future changes can be examined. A proposed optimization can identify the observation it preserves. A new entity type can state its identity and dependency contract. A new backend can demonstrate the same contextual contributions in another syntax.

That is the practical value of verification here: it turns architectural understanding into concrete questions and repeatable checks, while leaving each conclusion attached to the evidence that supports it.
