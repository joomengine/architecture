---
title: File updates and final emission
description: The concrete shared-to-local binding order, late dependency injection, custom-code handling, and packaging boundary.
section: JCB Case Study
order: 56
evidence: Source observations
---
# File updates and final emission

## The updater coordinates several artifact families

`Extension\Files\Updater::update()` checks for static and dynamic file collections, loads discovered powers when present, obtains the configured header material, and processes static, dynamic, module, plugin, and power files. It then prepares autoloading and performs an additional static-file autoloader update before releasing the dynamic file collection. [J07](../reference/bibliography.md#j07)

This is important evidence against a literal reading that all information is loaded once at the very beginning. Dependency-related work can occur during file updating, after structures and content already exist.

## View-scoped fan-out

`Extension\Files\Dynamic::update()` iterates the dynamic collection by view, checks that the corresponding content map is an array, and processes existing files whose recorded view matches. Each call carries file name, path, header material, and view context into `FileContent::set()`.

Thus the same prepared view context can supply several different file occurrences. The files remain distinct artifacts even when they share a template family or some binding values.

## Concrete binding sequence

At the pinned revision, `FileContent::set()` performs the following visible sequence:

1. Trigger the pre-content event and set the shared `FILENAME` binding.
2. Read the file, trigger the content-read event, and handle the BOM/header marker when present.
3. Apply `ContentOne` bindings, except for the special `code.power` case.
4. Apply the selected view's `ContentMulti` bindings when a view is supplied.
5. Conditionally update custom code for paths marked in the registry.
6. Trigger the before-write event, inject power and Joomla-power references, and write the result.
7. Add the number of `PHP_EOL` occurrences to the line counter.

[J07](../reference/bibliography.md#j07)

The order is shared bindings **before** view bindings in this method. The paper does not replace this observed order with a convenient but inaccurate universal “local first, global last” diagram.

## Additional finalization

The top-level compiler's `run()` calls file updating and then handles stored custom-code injection, language output, readme and server/repository work, and packaging. Therefore “the file writer has returned” is not necessarily the end of all content-affecting work in the compilation lifecycle. [J12](../reference/bibliography.md#j12)

A full dynamic audit should trace these later operations and the extension events before asserting a complete final-byte model.

## Counting and reproducibility

The inspected line counter counts newline occurrences in strings processed by this writer. That is not automatically identical to a separate physical-line count across every packaged file, and it says nothing by itself about how many lines were manually authored.

A reproducibility benchmark should independently inventory final artifacts and record bytes, physical lines, generated versus copied files, and package metadata. The [benchmark protocol](../engineering/benchmarks.md) avoids treating a UI counter as an independently validated scientific measurement.
