---
title: Service Directory and the wider definition ecosystem
description: A larger application blueprint/product pair and the surrounding repositories supplying reusable classes, fields, mappings, and distribution definitions.
section: Worked Examples
order: 65
evidence: Pinned Service Directory, package, Power, field-type, snippet, and repository-index sources
---
# Service Directory and the wider definition ecosystem

Hello World isolates a few mechanisms so their traces are easy to follow. The Service Directory supplies a larger application context: many fields and views, custom code, reusable layouts and templates, query definitions, placeholders, validation rules, and extension relationships.

The application has its own authorship. Its blueprint and generated README identify **Lemuel van der Merwe** as the application author. This white paper's authorship and JCB's architecture belong to **Llewellyn van der Merwe**; generating another author's application does not transfer that application's authorship. [E05](../reference/source-map.md#e05)

## Two versioned component identities in the blueprint repository

The pinned [Joomla packages repository](https://github.com/joomengine/joomla-packages/tree/5e8733cb82c4467cf5e0a39c05a0133b457fec80) contains two Service Directory component roots:

| Component identity | Recorded component version | Namespace prefix |
| --- | --- | --- |
| `160d0efb-6bf0-48eb-8d46-55cf74729501` | `6.0.3` | `JoomService` |
| `35a38329-d1e9-43df-a8f8-af1b8e6d8bd9` | `5.0.3` | `JoomService` |

They are separate root records. The counts of the entire repository must not be presented as the private dependency closure of only one of them.

Each root references component admin/site associations, updates, menus, router and configuration records, files/folders, plugin relationships, reusable custom-code aliases, and assets. The versioned [generated Service Directory repository](https://github.com/joomengine/Joomla-Service-Directory/tree/0ac9788cb9239ed2801ba19c7e2393c70e03f9c4) shows the native application product of this family.

## The repository exposes several layers of reuse

Across the inspected package snapshot, the root payload catalogue contains 133 fields, 25 admin views, 20 layouts, 13 Dynamic Gets, seven site views, seven templates, 25 custom-code records, ten placeholders, and additional validation, class, plugin, and component definitions.

Those counts identify available definitions, not generated file cardinalities. A layout can be called from several contexts. A field can appear in several associations. A Dynamic Get can serve a particular result role. The compiler expands those uses according to the selected component graph and target, rather than emitting one file for every catalogue item.

The generated application includes its administrator and site structure, forms, SQL, runtime classes, language material, assets, and reusable code. The same intermediate-store and contextual-generation mechanisms examined in Hello World operate over a broader set of interactions here.

## Application blueprints are only one distribution channel

The wider repositories demonstrate distinct categories of reusable input:

| Repository | Architectural role |
| --- | --- |
| `joomengine/packages` | Component blueprints and their dependency graphs |
| `joomengine/super-powers` | Managed reusable code definitions |
| `joomengine/joomla-powers` | Target-sensitive Joomla namespace/type mappings |
| `joomengine/joomla-fieldtypes` | Reusable field-type definitions |
| `joomengine/snippets` | Reusable interface and presentation material |
| `joomengine/repoindex` | Repository-target definitions for discovery and publication |
| `joomengine/jcb-documentation` | Operational explanations of authoring, reuse, compilation, and maintenance |

The [source map](../reference/source-map.md#e06) pins each examined repository. They are not interchangeable bags of source files: their indexes, payload types, acquisition handlers, and compiler consumers differ.

## What this adds to the architectural account

The ecosystem shows the same identity and transport principles operating at several levels. A project can import an application design, acquire a missing field type, resolve a code definition, select a target-specific platform mapping, and emit complete extension artifacts. Each operation has a defined representation boundary, yet the results can join one compiler execution.

This is the important composition. The repository channels do not replace the compiler; they make its required definitions available. The compiler does not replace authoring; it interprets represented choices and authored code. Generated products do not replace blueprints as the editable source of intent; they are the target implementation.

## Scope of the comparison

The two package roots and the generated repository are related public artifacts, but their version labels and snapshots are not asserted to be a byte-matched export/build certificate. A precise runtime reproduction selects one root, fixes the compiler and all dependencies, and compares the resulting artifact set under a declared equivalence.

That distinction leaves the evidence intact. The repositories directly show the represented definitions and the generated application structures. The compiler source explains the operations connecting those representation families. The [verification chapter](../engineering/verification.md) describes how to add a controlled fresh-build record without rewriting the architectural account.

The larger example therefore complements, rather than replaces, the small trace: Hello World makes individual correspondences easy to inspect; Service Directory demonstrates the breadth of design information coordinated through the same architecture.
