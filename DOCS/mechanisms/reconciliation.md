---
title: Editorial reconciliation and conflicts
description: Stable regions, authority, three-way comparison, occurrence-local edits, shared-definition updates, and persistence boundaries.
section: Mechanisms
order: 37
evidence: Formal model and proposed implementation contract
---
# Editorial reconciliation and conflicts

## Extraction is not yet authorization to overwrite

Finding a recognizable marker establishes a candidate edit. It does not establish that the editor was authorized, that the destination is unique, or that the database has not changed since the artifact was generated.

A reconciler should receive the previous source or region baseline, the current persistent record, the extracted candidate, and the artifact's provenance. The result is an accepted update, a no-op, or an explicit conflict.

## Three-way comparison

Let $b$ be the last generated region baseline, $s$ the current source value, and $u$ the extracted user value. A simple whole-region policy is:

| Condition | Result |
| --- | --- |
| $u=b$ | No editorial change; retain $s$ |
| $s=b$ | Source unchanged; accept $u$ after validation |
| $u=s$ | Both sides agree; retain that value |
| Otherwise | Conflict requiring a declared merge policy |

This policy does not pretend to semantically merge arbitrary programs. A text merge or AST merge can be added as a separate operation, with its own tests and conflict reporting.

## Occurrence-local versus shared edits

If a reusable definition appears in several components, an edit in one occurrence may belong only to that occurrence. Alternatively, the user may intend to update the shared definition. Those are different commands.

A safe system records the intended scope. Shared-definition updates extracted from several occurrences must agree or produce a conflict. File scan order is not a legitimate authority rule unless it is explicitly chosen and justified as policy.

## Identity and relocation

Region IDs are preferable to raw line numbers as persistent identities. Context fingerprints can help relocate regions after neighboring generated content changes, but ambiguous matches must remain ambiguous. A hash match is not an authorization check, and a non-cryptographic fingerprint is not a security signature.

The inspected JCB extractor stores location information and surrounding-content fingerprints alongside captured code. This is concrete evidence for recovery beyond a simple fixed line-number replacement. It does not establish complete conflict detection under arbitrary edits. [J11](../reference/bibliography.md#j11)

## Persistence protocol

A proposed robust implementation parses and validates the entire candidate set before committing accepted changes. It associates updates with a source revision and uses optimistic concurrency or a transaction to avoid overwriting a record changed by another actor.

If extraction partially succeeds, the system must define whether it commits the accepted subset or aborts the whole reconciliation. Neither behavior should be hidden. The next build's snapshot is taken only after the selected reconciliation policy has completed.

## Removed and malformed regions

An absent marker may mean an accidental deletion, a deliberate request to remove an adaptation, or a generator change. These meanings require different responses. Do not treat all missing regions as authorization to delete stored content.

Reject duplicate IDs, malformed nesting, unmatched boundaries, and unknown ownership. If a region's target disappears, preserve its record for explicit migration or resolution rather than silently losing the user's work.

## Research significance

The important outer-loop memory is not simply a cache of output text. It is an authoritative, versioned record of selected human adaptations that participates in future synthesis. That makes the loop a constrained co-evolution of model and artifact, rather than an unrestricted inverse compiler.
