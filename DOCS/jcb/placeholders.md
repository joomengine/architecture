---
title: JCB placeholder behavior
description: Actual replacement modes, shared and local environments, marker families, and why replacement is not a general fixed-point solver.
section: JCB Case Study
order: 55
evidence: Source observations
---
# JCB placeholder behavior

## A family of mechanisms

JCB uses placeholders for ordinary generated values, reusable code, dependencies, and custom-code tracking. These uses should not be collapsed into a single abstract “placeholder pass.” Their inputs, timing, and authority differ.

The key-modeling classes align content registry keys with placeholder syntax. `Placeholder::update()` then performs replacement against a supplied map, while `update_()` uses the active map held by the placeholder service. [J06](../reference/bibliography.md#j06), [J08](../reference/bibliography.md#j08)

## Three action modes

The inspected `update()` method supports three modes. Mode 1 directly calls PHP's `str_replace` with arrays of keys and values. Mode 2 first checks whether any supplied key appears and, when one does, performs replacement. Mode 3 removes entries from a temporary replacement map when their keys do not occur in the input string, then replaces using the remaining entries. [J08](../reference/bibliography.md#j08)

Mode 3 does **not** delete unknown placeholders from the artifact. It also does not establish that all required placeholders have been resolved. It is a selection of relevant replacement-map entries for that call.

## Replacement order

PHP array-based `str_replace` applies replacements in order. Text introduced by an earlier entry can be affected by a later entry. Consequently, the replacement map's order can matter when values contain other keys. The theory's reference implementation deliberately uses a separately specified non-recursive pass; it is not advertised as byte-compatible with every JCB replacement behavior. [R12](../reference/bibliography.md#r12)

The presence-filtering step adds another nuance: a key absent in the original input can be removed from the map even if an earlier replacement would have introduced it. The correct behavior of a real build therefore depends on how the compiler prepares fragments and schedules later passes.

## Tracking markers

The `keys()` method constructs inserted/replaced tracking markers, including record IDs, when placeholder tracking is enabled. The extractor has corresponding marker families and reading states. These are part of the round-trip protocol, not ordinary variable substitutions. [J08](../reference/bibliography.md#j08), [J11](../reference/bibliography.md#j11)

The source comments intentionally alter some example delimiter characters to avoid the compiler recognizing its own documentation. Copying those comment examples verbatim as user-facing syntax would be misleading. This paper describes the mechanism and links the source rather than inventing a replacement marker manual.

## Portability lesson

A reimplementation must specify whether substitutions are simultaneous or sequential, whether replacement values can contain tokens, which stage owns each token family, and how unresolved obligations are detected. A generic regex that repeatedly substitutes until no delimiters remain is not an equivalent implementation without a termination and ordering argument.
