---
title: Blueprint and product accounting
description: Reproducible counts of payloads, indexes, descriptions, assets, and generated repository text at fixed revisions.
section: Worked Examples
order: 64
evidence: Programmatic inventory of the pinned public source snapshots
---
# Blueprint and product accounting

A useful size comparison identifies exactly what is counted. A blueprint repository contains authoritative entity payloads as well as indexes, generated explanations, assets, and license material. An output repository contains synthesized application code, supplied reusable classes, assets, and descriptive files. Combining all of those into one unexplained input number would obscure the architecture.

The figures below count the [pinned Hello World snapshots](hello-world.md). They are static repository inventories, separate from the maintainer's timed JCB self-build measurements.

## Portable design and supporting repository material

| Category | Files | Physical text lines | Bytes |
| --- | ---: | ---: | ---: |
| Entity and relationship payload JSON under `src/` | 33 | 1,298 | 65,600 |
| Index JSON under `index/` | 22 | 269 | 11,885 |
| Markdown descriptions | 22 | 1,198 | 100,268 |
| Transported assets | 4 | 18 in the text asset | 68,416 |

The 33 payloads comprise 24 root `item.json` records and nine child relationship/configuration documents. The four assets comprise three images and one text file. The repository also carries its license. Index and Markdown categories describe or locate the model; they are not added to the payload count as if they were independent application decisions.

The payload files contain 65,600 serialized bytes. Embedded code can be represented with escaped newlines inside JSON strings. Consequently, 1,298 physical JSON lines is a property of this serialization, not a count of logical statements, distinct decisions, or authored code lines after decoding.

## Generated product repositories

| Product | All files | UTF-8 text files | Physical text lines |
| --- | ---: | ---: | ---: |
| Component | 259 | 255 | 31,981 |
| Module | 19 | 19 | 540 |
| Plugin | 12 | 12 | 467 |
| **Combined** | **290** | **286** | **32,988** |

The combined physical-text expansion relative to the serialized payload's physical lines is approximately **25.4 times**. This is a descriptive ratio between two specified representations. It is not a compression bound, a measure of manual labor, or an attribution of every output byte solely to the project payload.

The compiler's rules, target templates, reusable Powers, libraries, assets, and environmental values are additional build inputs. The output includes their selected generation and assembly results.

## Counting rule

The inventory visits regular files recursively, outside Git's own metadata. For a text-line count, it accepts files that decode as UTF-8 and contain no NUL character, then counts physical lines using the decoded text's line boundaries. Binary files remain in the total file count and byte inventory but not the text-line count.

Payload selection is structural: JSON below `src/`, with root item records and child documents counted separately. Index selection is JSON below `index/`. Markdown descriptions are selected by their `.md` extension. The asset category follows `src/file_folder/`.

This rule deliberately avoids guessing which generated file was “important enough” to count. A narrower runtime-only, executable-only, or dependency-excluding analysis would be a different metric and should publish its own selection rule.

## Internal build counters are a different observation

The generated component README includes compiler-produced line, file, and folder counts and illustrative time-saving calculations. They need not equal this later repository inventory. Counter update points, added repository descriptions, copied dependencies, and later repository changes can alter the counting boundary.

The README's estimates based on seconds per line or file are formulas, not measured developer hours or measured compiler elapsed time. They are not used here as productivity evidence. The [performance chapter](../engineering/performance.md) instead separates actual compilation timing from output volume and hypothetical labor estimates.

## Why the distinction strengthens the example

The blueprint is compact because repeated implementation knowledge resides in reusable generation rules and supplied definitions. The output is large because those inputs are specialized and distributed across a complete application's concerns. There is no need to pretend the compiler invents reusable class bodies during each run for this to be a meaningful capability.

The more informative observation combines quantity with traceability. The Greeting field's SQL, form, language, list, and metadata outputs can be connected to its properties and occurrence roles. The module and plugin outputs can be connected to their definitions and component context. The count describes their scale; the trace explains their origin.

## Repeating the inventory

The repository provides `scripts/research_inventory.py` to inventory local checkouts of the four example repositories without running their code. Its output records revision identifiers, categories, file hashes, and marker correspondences. Running the inventory is not a fresh Joomla compilation; repeating the full build additionally requires the selected JCB environment and dependencies. [Verification](../engineering/verification.md)

Fixing those two boundaries allows both operations to be useful: an artifact inventory can be reproduced quickly, and a runtime build can be compared under its declared configuration without confusing the two experiments.
