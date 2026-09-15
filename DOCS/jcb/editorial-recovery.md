---
title: Recovery of marked editorial changes
description: Installed-file scanning, marker recognition, GUI recovery, reverse transformation, location fingerprints, and persistent reinsertion.
section: JCB Case Study
order: 57
evidence: Source observations and author testimony
---
# Recovery of marked editorial changes

## The omitted feedback path

The originator identifies a crucial feature: the system being regenerated can already exist, and a developer can have edited designated regions of its installed files. Those regions are not simply discarded. JCB can recognize its conventions, recover the edits, store them, and reuse them in later output.

This is corroborated by the contemporary initializer's extraction call before component building and by the executable custom-code extractor. The README also describes bidirectional IDE synchronization and insert/replace round trips. [J03](../reference/bibliography.md#j03), [J04](../reference/bibliography.md#j04), [J11](../reference/bibliography.md#j11)

## What is scanned

`Customcode\Extractor::run()` enumerates active target paths and recursively searches configured file types. The inspected type list includes PHP, JavaScript, and XML patterns. It is therefore more precise to say **eligible files in active installed targets**, not every file on the system.

For each file it calls `searchFileContent()`, periodically processes new/existing record buffers, and flushes remaining work at the end. The implementation temporarily changes the working directory and restores it after scanning.

## Recognition and capture

`searchFileContent()` first delegates a GUI-code search, then scans the file line by line with `SplFileObject`. It tracks start/end markers, reading state, code buckets, line positions, and surrounding content. It distinguishes new inserted/replaced regions from updates to existing tracked regions.

When a region closes, the captured content passes through the reverse-transform service with the placeholder context and target; existing records also supply their ID. The resulting code is base64-encoded for the persistence representation. Base64 is an encoding, not encryption or validation.

## Location memory

The extractor retains line information and fingerprints of surrounding trimmed lines. The inspected end-target fingerprint uses three lines and an MD5 digest with a count prefix. This helps explain how reinsertion can use more than a permanently fixed line number.

A contextual fingerprint is not a cryptographic authorization mechanism. The selected code does not establish that every moved, duplicated, or heavily edited region will resolve uniquely. The formal reconciler therefore treats ambiguous ownership or location as a conflict rather than assuming a hash always identifies the intended target.

## Reinsertion and persistence

The top-level compiler's later run phase handles custom-code injection after ordinary file updating. The author's practical account and the project documentation explain that recovered changes are persisted and reused across builds. The inspected extractor's insert/update buffers and the later injection path provide source-level support for that architecture. [J11](../reference/bibliography.md#j11), [J12](../reference/bibliography.md#j12)

This edition does not claim an independently executed round-trip test of a live Joomla installation. It separates the observed mechanism from the stronger preservation laws proposed in [round-trip semantics](../mechanisms/round-trip.md).

## Generalization

The transferable mechanism is an admissible editorial language, stable region identity, extraction, reverse or canonical transformation, persistent reconciliation, and later binding. It is not an unrestricted reverse compiler. Its value lies in preserving selected human decisions while the surrounding generated structure continues to evolve.
