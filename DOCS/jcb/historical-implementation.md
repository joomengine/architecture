---
title: The public compiler of January 2016
description: What the root source actually demonstrates, and what cannot be backdated from modern class names or features.
section: JCB Case Study
order: 58
evidence: Historical source observations
---
# The public compiler of January 2016

## The primary artifact

The root public-source commit `ecf47809f960bd057af8a414168fada6fe22c5f7` contains `admin/helpers/compiler.php`. Its header identifies Llewellyn van der Merwe, version 2.0.8, a build date of 30 January 2016, and a creation date of 30 April 2015. The commit records 30 January 2016 at 20:28:43 UTC. [J01](../reference/bibliography.md#j01), [J02](../reference/bibliography.md#j02)

The license file's history points to the same root commit, but the executable compiler is the substantive architectural evidence.

## Dedicated intermediate memory

The early class declares separate collections for static and dynamic file content, placeholders, language content, queries, lists, search, filters, layouts, permissions, custom fields, aliases, categories, tags, history, serialization, and other generation concerns.

These are ordinary PHP arrays and properties rather than the modern service/class structure. The theory's historical interpretation must therefore be based on their roles, not on the later introduction date of a class named `Registry`.

## Staged execution

The constructor obtains component data through `getComponentData()` and establishes target/template paths. Its `buildComponent()` method removes the old build folder, creates folders, builds static files, builds dynamic files, prepares file content, updates files, and packages the component.

The visible method names include `setStatic()`, `dynamique()`, `buildFileContent()`, and `updateFiles()`. This already demonstrates a distinction between structure creation, content preparation, and a later replacement/update phase. [J02](../reference/bibliography.md#j02)

## What can be dated

The combined presence of source loading, specialized builders, static/dynamic content stores, template-oriented structure creation, and a subsequent file-update pass supports a public implementation lineage from **30 January 2016**.

This is stronger than a claim based only on a copyright year. It is also narrower than saying the entire present specification, every contemporary extraction feature, or the modern service architecture existed in exactly the same form at that date.

## What remains undated in this inspection

The selected historical excerpt does not establish the first introduction date of every custom-code recovery variant, modern power resolver, remote-fetch mechanism, incremental behavior, or current abstraction. Those dates require feature-specific history inspection.

The paper deliberately preserves this distinction. The method can have an early public implementation while its engineering realization is refined over time. A later formal vocabulary can describe an earlier pattern without pretending that the vocabulary was published then.

## Historical interpretation

The early source shows a compact source model being interpreted through many specialized generation concerns and projected into a larger file system. The modern source shows a more separated service architecture and richer feedback mechanisms. Their continuity supports an architectural lineage, while the formal contracts in this publication make that lineage available for reimplementation beyond PHP and Joomla.
