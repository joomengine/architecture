---
title: Exporting the design graph
description: From local definitions to normalized repository payloads, relationship closure, generated indexes, and documentation.
section: Blueprint Exchange
order: 23
evidence: Package builder set, remote set, entity projection, and repository writer
---
# Exporting the design graph

Export turns selected local design knowledge into a repository representation that another JCB installation can consume. The operation combines graph traversal, type-specific projection, serialization, asset transport, and publication metadata. It is not equivalent to compressing the current database or copying the generated Joomla extension tree.

The author can select a component as the root. The exporter then follows the relationships and supported embedded references needed to represent that component, writes the corresponding definitions, and constructs the repository indexes and readable descriptions. The Hello World repository is the resulting kind of product. [B02](../reference/source-map.md#b02), [E01](../reference/source-map.md#e01)

## Select, normalize, discover, publish

The package builder obtains each selected entity through its configured identifying field. Its remote-set service maps the local item into the portable form and extracts dependencies before attempting repository writes. Newly discovered entity work is accumulated and drained through the same family of handlers. Files and folders are handled after the entity traversal.

A useful decomposition is

$$
\operatorname{export}(R_0,D)=
\operatorname{publish}\bigl(\operatorname{encode}(\operatorname{project}(D|_{R^*}))\bigr),
$$

where $R^*$ is the supported dependency closure of the selected roots. The notation separates the conceptual operations; it does not impose an all-or-nothing transaction over the repository network.

Projection is important for both portability and clarity. For example, the component configuration omits selected installation-specific access, server, export, and translation-service fields while retaining the design information intended for transport. Referenced files such as the component image and compiler BOM material have declared destinations. [B01](../reference/source-map.md#b01)

## One definition can be published to several approved destinations

Repository configuration determines whether an item can be written and to which branch. The writer considers eligible, approved repositories with usable write-branch settings. Reading a definition and authorizing its publication are separate operations.

For each destination, the exporter can create or update the item payload, its readable item description, and its index entry. It can also update the repository's aggregate README or entity catalogue. Those descriptive files are generated from the same design record rather than maintained as an independent hand-written blueprint. [B05](../reference/source-map.md#b05)

This organization makes a repository simultaneously a machine-consumable distribution surface and an inspectable design record. A user can read the exported descriptions, inspect the payload, and import the item by its stable identity.

## Change detection avoids unnecessary writes

The writer retrieves existing metadata when needed and compares the prepared representation with the remote state. It uses repository content identifiers for updates and can skip an unchanged item. The comparison is more specific than simply comparing raw local database rows: portable fields are normalized, and dependency descriptors are normalized for comparison.

In the inspected dependency comparison, order normalization does not erase multiplicity: repeated descriptors remain repeated records. A language-neutral implementation should distinguish set equality, multiset equality, and sequence equality instead of assuming that all three are interchangeable. [B05](../reference/source-map.md#b05)

Generated indexes are merged with existing index content. Exporting one selected component therefore need not discard unrelated definitions already published in the same repository.

## Publication has observable intermediate states

The implementation writes items and supporting files through repository operations. A successful write of one item is not a proof that every later item, asset, or index update also succeeds. Likewise, publication to one approved destination can succeed while another destination reports a failure.

This is the actual operational granularity: selected entities, per-repository writes, metadata updates, and diagnostics. The architecture remains useful without describing those operations as a distributed transaction. A reviewable publication record identifies which outputs were written and which requests failed.

The distinction also explains why an index and its payload should be kept aligned. An index entry is a locator for authoritative settings; a payload that is missing or malformed at that location is a retrieval error, not a second valid interpretation of the entity.

## Export is not compilation

The exported field retains its model properties. It does not contain every generated form element, query clause, model method, language declaration, or database statement that the compiler will derive from those properties. Those consequences arise when an imported or local definition is interpreted in a concrete build context.

Conversely, custom code deliberately authored as part of a definition remains part of the portable design. The blueprint can therefore mix declarative settings with reusable code bodies. The export boundary does not require an application to be describable solely through a fixed set of graphical controls.

The [Hello World field trace](../examples/field-trace.md) shows this difference directly. The blueprint specifies a field and its use; the generated component contains the coordinated implementation. The next chapter follows the portable design back into local working data.
