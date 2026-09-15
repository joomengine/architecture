---
title: Blueprint representation
description: The portable entity graph, its payloads, dependency descriptors, indexes, documentation, and assets.
section: Blueprint Exchange
order: 20
evidence: Package entity configuration and the public Hello World blueprint
---
# Blueprint representation

A JCB blueprint is a portable description of development intent. It contains the definitions and relationships from which the compiler constructs an extension. A blueprint repository also contains material that makes those definitions discoverable and readable. The distinction matters: an index describing a component is not another copy of the component's design, and a generated README is not additional compiler input simply because it lives beside that design.

## Five parts of a repository representation

**Entity payloads** carry properties such as field types, view settings, query definitions, custom code, extension configuration, and stable identifiers. **Association payloads** carry relationships and use-specific settings: which field appears in a view, which view belongs to a component, or which module accompanies a component. **Dependency descriptors** identify other required entities or assets. **Indexes** map identities to discoverable payload locations and descriptive metadata. **Documentation** presents the same items to readers and repository browsers. Binary or textual **assets** supply referenced images, files, and folders.

The Hello World snapshot contains 33 JSON payload documents: 24 root `item.json` records and nine child relationship/configuration documents. It also contains 22 index JSON files and four transported assets. The accounting method and complete inventory are provided in [blueprint and product accounting](../examples/accounting.md). These categories are counted separately.

## The payload is a model projection

Export uses each entity's configuration to decide what to read, normalize, retain, and omit. For a component, the configuration identifies the component payload path and its index, declares child entities, and excludes installation-specific fields such as selected server records and particular export or translation-service credentials. The portable representation is therefore not a raw dump of every column in a local database. [B01](../reference/source-map.md#b01), [B05](../reference/source-map.md#b05)

Let $D$ be local working data and $t$ an entity type. Its portable projection is

$$
B_t=\operatorname{encode}_t(\operatorname{project}_t(D)).
$$

Projection and encoding do different work. Projection selects design properties and relationships. Encoding represents them in a transport form, including decoded code and normalized nested structures where the entity's mapper specifies those transformations. Local numeric record IDs and editing metadata need not be reproduced as application identity.

The projection is type-specific. The publication does not assume that every property named similarly across tables has identical export semantics. The configured maps and model services are the authority for the actual representation.

## Dependencies are explicit transport instructions

A payload can include a reserved `@dependencies` member. For example, the Hello World admin view identifies its field-association child using the view's GUID:

```json
{
  "key": "admin_view",
  "value": "65116558-be67-4931-95be-727fbfb16db7",
  "entity": "admin_fields",
  "table": "#__componentbuilder_admin_fields",
  "direction": "in"
}
```

The descriptor says how to find a dependent record. It is not a runtime application table definition. The reserved member separates transport relationships from ordinary persisted entity properties. [B03](../reference/source-map.md#b03), [E01](../reference/source-map.md#e01)

An outgoing reference uses the target entity's identifying field, commonly `guid`. An incoming child relation uses the owning entity's identifier as a relationship key. File descriptors additionally carry information such as target area and repository pointer. These distinctions govern traversal, import, and reset policy.

## Identity is not always a GUID

The portable key is the typed triple $u=(t,k,v)$ introduced in [identity](../foundations/identity.md). GUID-addressed fields and views are common, but custom code can be addressed by its function name. Hello World's `readMEcontributors` item is one such definition. Child payloads can be addressed by their parent relationship rather than by an independent GUID.

An implementation that blindly assumes every repository item has the shape `(guid, file)` would lose part of this model. The identifying field, entity type, and relationship direction are operational data.

## Repository layout is a representation choice

The component configuration uses `index/joomla-component.json` for discovery and `src/joomla_component` for payloads. Other entity types have their own configured names and paths. The index supplies paths to settings and readable item material. [B01](../reference/source-map.md#b01)

The compiler does not need Markdown prose to discover the meaning of a field. The JSON and its associated dependency and asset definitions carry that meaning. The generated documentation is valuable because it lets a developer inspect the same portable design without opening JCB.

A language-neutral implementation can use another serialization format while retaining the architecture: typed identity, explicit relationships, normalized design properties, separately described assets, and an index that locates the authoritative payload. The [export](export.md) and [import](import.md) chapters explain the operations over this representation.
