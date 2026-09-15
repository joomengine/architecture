---
title: Runtime boundaries and nonclaims
description: Where the abstract proofs apply, where production behavior is richer, and what evidence would close the gap.
section: JCB Case Study
order: 60
evidence: Source observations and methodological limits
---
# Runtime boundaries and nonclaims

## A formal abstraction is not an automatic certificate

The finite monotone model in this paper supplies a clean explanation of contextual completion. JCB's production compiler contains mutable objects, overwrites, ordered string replacement, source updates, filesystem effects, external acquisition, and extension events. Those mechanisms can be correct without satisfying the positive fragment's assumptions.

The case study therefore does not assert that the whole runtime is a monotone lattice program, a confluent rewrite system, or an immutable dataflow engine.

## Specific boundaries

**Shared mutable state.** `FileContent::set()` changes `ContentOne`'s `FILENAME` per file. Field retrieval can perform contextual custom-code updating on stored data. These are concrete reasons to avoid a blanket immutability claim. [J07](../reference/bibliography.md#j07), [J09](../reference/bibliography.md#j09)

**Ordering.** Shared placeholders precede view placeholders in the inspected file writer. `str_replace` has ordered replacement behavior. A new parallel schedule or a simultaneous token engine must not be assumed equivalent without tests. [J07](../reference/bibliography.md#j07), [J08](../reference/bibliography.md#j08)

**Input completeness.** Remote field acquisition, late power loading, build dates, and extension hooks can affect output beyond the initial component query. A reproducibility manifest must include those inputs or specify a narrower comparison. [J05](../reference/bibliography.md#j05), [J07](../reference/bibliography.md#j07), [J09](../reference/bibliography.md#j09)

**Round-trip scope.** The extractor recognizes configured marker conventions in eligible file types and active paths. It is not evidence for recovering arbitrary unmarked edits in arbitrary files. Context fingerprints assist location; they do not prove unique semantic correspondence under every modification. [J11](../reference/bibliography.md#j11)

**Publication.** File creation and ZIP packaging are observed. A database/filesystem-wide transaction or an atomic deployment protocol is not established by the inspected paths.

## What a stronger audit should record

Instrument one real build with a frozen input set. Record every source acquisition and mutation, registry read/write, dependency request, file creation/update, and hook invocation. Repeat from a clean environment and compare outputs. Then introduce controlled changes to field definitions, occurrence settings, templates, marked edits, and external dependencies.

The objective is not to force the implementation to resemble a diagram. It is to identify which semantic contracts it already satisfies and where a generalized implementation needs a stronger boundary.

## Why these limits strengthen the theory

A useful theory should explain an implementation without erasing its complexity. It should also support implementations that choose different representations: typed ASTs instead of strings, immutable maps instead of mutable registries, worklists instead of nested calls, or versioned overlays instead of in-place database updates.

The contribution is the portable organization of knowledge completion, contextual reuse, staged output, and controlled feedback. Claims of universal performance, perfect recovery, or human-like comprehension require separate evidence and remain research questions.
