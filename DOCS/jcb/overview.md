---
title: JCB as the originating case study
description: Mapping a production generator to VDMT without making Joomla or PHP part of the theory's definition.
section: JCB Case Study
order: 50
evidence: Source observations and architectural interpretation
---
# JCB as the originating case study

## Scope of the case study

Joomla Component Builder is the originating implementation from which this account extracts VDMT. The authoritative source is [joomengine/Joomla-Component-Builder](https://github.com/joomengine/Joomla-Component-Builder). Contemporary observations in this edition are pinned to `bca4a1520484f3e2c2fbd12964a5995b0d058de1`; the historical comparison uses the root commit `ecf47809f960bd057af8a414168fada6fe22c5f7`.

The inspection follows selected executable paths and data structures. It is not a dynamic recording of an entire live Joomla compilation, and it does not certify every extension, target version, or input. This boundary is explicit so that the case study remains independently checkable.

## The observed architecture

The current compiler has a substantial initialization phase. It recovers marked custom code from eligible installed files, builds the component data model, handles version and build settings, prepares output structures, and populates content through the inherited infusion path. Its later run phase updates files, injects stored custom code, processes language and auxiliary outputs, and packages the result. [J04](../reference/bibliography.md#j04), [J12](../reference/bibliography.md#j12)

Within that process, source definitions are loaded and enriched through several services. Field data can be indexed and reused while still undergoing context-sensitive custom-code processing. Content builders separate broadly shared bindings from view-scoped bindings. The file-content writer applies those binding environments and later injection operations before writing. [J05](../reference/bibliography.md#j05), [J06](../reference/bibliography.md#j06), [J07](../reference/bibliography.md#j07), [J09](../reference/bibliography.md#j09)

## Mapping to the abstract framework

| VDMT role | Observed JCB realization |
| --- | --- |
| Durable source knowledge | Component, view, field, field-type, and custom-code database records |
| Context discovery | Component enrichment, child-data services, referenced dependencies, guarded fallback acquisition |
| Scoped intermediate memory | Component state, specialized builders, field indexes, content registries |
| Occurrence interpretation | View relationships, target settings, field processing with view context |
| Staged binding | Placeholder environments, view-specific maps, custom-code and power injection |
| Materialization | Prepared structures, file-content updates, language files, packaging |
| Persistent editorial feedback | Installed-file extraction and custom-code persistence, followed by reinsertion |

This mapping is an interpretation grounded in source, not a claim that JCB uses the mathematical names in this paper.

## What the implementation teaches

The strongest reusable insight is the combination: dependency-sensitive acquisition, contextual reuse, multiple output projections, and an editorial path back into persistent input. A simple picture of values moving through three dictionaries misses the nested acquisition and the outer feedback loop.

At the same time, the source corrects an overly tidy pipeline diagram. Files can exist as skeletons before final content is ready; dependencies can still be loaded during file updating; component-wide content includes a per-file `FILENAME` mutation; and extension hooks can alter state. Therefore the abstraction must describe semantic roles and contracts rather than pretend the implementation is a pure, linear, immutable pipeline.

The following pages explain these mechanisms separately. [Runtime boundaries](runtime-boundaries.md) identifies which formal properties remain implementation obligations rather than established facts.
