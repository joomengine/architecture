---
title: Pinned source map
description: Exact source paths, inspected methods, and the narrow claims each supports.
section: JCB Case Study
order: 51
evidence: Source observations
---
# Pinned source map

## Revisions and path convention

Contemporary revision: `bca4a1520484f3e2c2fbd12964a5995b0d058de1`. Historical revision: `ecf47809f960bd057af8a414168fada6fe22c5f7`. Every source reference in the bibliography resolves to one of these immutable revisions, not to a moving branch.

In the table, `Compiler/` abbreviates `libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/`. The final orchestration class is one directory above that prefix.

## Inspection ledger

| Source | Inspected responsibility | Supported conclusion |
| --- | --- | --- |
| `Componentbuilder/Compiler.php` | Constructor and `run()` orchestration | Initialization and inherited infusion precede final file updating, custom-code handling, language work, and packaging |
| `Compiler/Initializer.php` | `init()`, extraction, component build, reset, structure methods | Marked-code recovery precedes component build and build-directory reset in the visible orchestration |
| `Compiler/Component.php` | `build()`, `__get()` | A component registry is loaded once from the data service, with explicit missing-data failure |
| `Compiler/Component/Data.php` | Joined query and `energize()` | Root component data is enriched with children and generation settings |
| `Compiler/Model/Adminviews.php` | View relationship processing | View occurrences carry settings and trigger retrieval of their referenced view data |
| `Compiler/Field/Data.php` | `get()`, `getFieldData()`, `set()`, query and retry | Base field data is indexed by ID/GUID; contextual processing and guarded fallback remain in the retrieval path |
| `Compiler/Builder/ContentOne.php` | Key modeling | A flat content environment converts logical keys into placeholder keys |
| `Compiler/Builder/ContentMulti.php` | Separator and key modeling | A view-scoped environment maps `view|key` into a view and placeholder key |
| `Compiler/Helper/Infusion.php` | Start of `buildFileContent()` | Component and placeholder values are transformed or copied into output-binding memory |
| `Compiler/Placeholder.php` | `update()`, `update_()`, marker `keys()` | Replacement has explicit action modes and marker construction; action 3 filters the map, not unknown output tokens |
| `Compiler/Extension/Files/Updater.php` | `update()` | Static, dynamic, module, plugin, and power file processing are ordered; late dependency/autoloader work exists |
| `Compiler/Extension/Files/Dynamic.php` | `update()` | Dynamic files are grouped by view and rendered with that view's content context |
| `Compiler/Extension/FileContent.php` | `set()` | Shared bindings precede view bindings, conditional custom-code updating, events, power injection, writing, and newline counting |
| `Compiler/Customcode/Extractor.php` | Marker definitions, `run()`, `searchFileContent()` | Eligible installed files are scanned; marked bodies and contextual location data are captured into insert/update buffers |
| Historical `admin/helpers/compiler.php` | Fields, constructor, `buildComponent()` | The 2016 source already embodies specialized builders and a staged static/dynamic construction and file-update sequence |

The bibliography entries [J01–J12](../reference/bibliography.md#j01) provide the full paths and links. Where the ledger says “inspected,” it refers to the cited methods, not a claim that every line of every file was exhaustively audited.

## Reproduction procedure

Check out the stated commit, inspect the listed methods, and follow each call into its service implementation when making a stronger claim. Preserve event hooks and constructor effects in the trace. A diagram that starts at `run()` alone omits work performed during construction.

For a dynamic audit, record the source snapshot and target, instrument database reads and mutations, record registry reads/writes and file operations, and retain call traces around extraction and final injection. Compare the observed trace with the semantic phases rather than assuming class names determine phase boundaries.

## Negative evidence

The selected paths do not establish a generic worklist scheduler, a global least-fixed-point evaluator, immutable stores, complete provenance, complete cross-build invalidation, transactional publication, or universal round-trip correctness. Those features are formally specified or proposed elsewhere and must not be retroactively attributed to the inspected implementation.
