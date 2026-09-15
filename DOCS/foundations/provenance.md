---
title: Development and provenance
description: The author's independent development history, the public source record, and the relationship between implementation history and this formal account.
section: Foundations
order: 15
evidence: Author's development account and public source history
---
# Development and provenance

Joomla Component Builder originated as my independently developed response to the recurring work of building complete Joomla extensions. The objective was practical: express application intent in manageable definitions, reuse implementation knowledge, and repeatedly produce the detailed code and structure that Joomla applications require.

I developed the original approach without awareness of several of the compiler and model-driven engineering systems discussed in this publication. The connections to attribute grammars, staged generation, memoization, and other established work were identified retrospectively. They help describe the architecture accurately; they are not an invented account of what influenced its beginnings.

**Llewellyn van der Merwe**

## The public implementation record

The official source lineage begins with commit `ecf47809f960bd057af8a414168fada6fe22c5f7`, titled “first commit of free version,” recorded on **30 January 2016 at 20:28:43 UTC**. The compiler in that revision already uses specialised builder arrays, static and dynamic content stores, component-data loading, structure construction, and a later file-update sequence. [C23](../reference/source-map.md#c23)

That source is evidence of an implemented architecture at that date. It does not date every later capability, the present service layout, or this mathematical exposition to the same point in time. The source header also records an earlier creation date, while the author's development account describes work preceding public release. These are distinct kinds of historical record.

## From a large compiler to specialised services

The early compiler concentrated substantial behaviour in large classes. Over subsequent years, responsibilities were separated into services and object-oriented collaborators: component data, field processing, specialised builders, placeholders, language services, Power handling, architecture-specific emitters, and file-updating utilities.

The continuity lies in the dataflow and its responsibilities, not in preserving one class arrangement. Definitions are acquired, their consequences are organised, context is established at use-sites, and output is assembled through ordered work. Refactoring can change where a responsibility lives without changing the architectural purpose it serves.

The current [source map](../reference/source-map.md) names the inspected implementation paths. Historical and contemporary paths are kept separate so that the publication's references remain reproducible.

## Authorship and prior work

The architecture described here is my work and this is my white paper, supported by research and editorial assistance. Joomla, reusable third-party libraries, and the research cited in the bibliography retain their own authorship.

Independent development and historical priority are different statements. A mechanism can have been independently derived in JCB while corresponding to a principle published earlier. Giving that earlier work its proper credit makes the explanation more useful: readers can connect the implementation to a larger body of knowledge without erasing the actual development history.

The [related mechanisms in the bibliography](../reference/bibliography.md) therefore identify precise correspondences. A shared store resembles some aspects of blackboard coordination; context-sensitive attributes resemble aspects of attribute-grammar evaluation; marked-edit recovery relates to round-trip engineering. None of those observations requires that JCB implement another system's complete formalism.

## The purpose of this edition

This edition collects the implemented mechanisms into an architectural account that can be read independently of the PHP codebase. It supports three activities: understanding how JCB works, implementing its architectural choices in another technology, and studying the resulting model when considering future work.

The edition documents the present mechanism before proposing changes to it. Its mathematical vocabulary is a way to expose relationships, state changes, and ordering—not a substitute for the implementation record. [Edition and sources](../reference/edition.md)
