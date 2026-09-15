---
title: Local-first entity discovery
description: Configured repository search across the supported entity catalogue, with local persistence, request guards, and explicit selection policy.
section: Blueprint Exchange
order: 21
evidence: Entity factory, package builder, remote retrieval, and repository indexes
---
# Local-first entity discovery

Repository discovery is not confined to Powers. JCB applies a common acquisition architecture across component definitions, their relationships, fields, views, templates, layouts, queries, code definitions, and other supported entities. A definition can be absent from the current installation yet available through a configured source. Once acquired, it becomes locally managed working data and can participate in ordinary compilation.

“Global” discovery means discovery across the repositories configured for the operation. It does not mean an unbounded web crawl or a broadcast to every repository on the Internet. Repository order, channel, branch, index, and entity identity determine the search. [B01–B04](../reference/source-map.md#b01)

## The supported entity catalogue

The inspected factory identifies 45 canonical entity types. Its catalogue includes both reusable root definitions and relationship/configuration records:

| Family | Entity types |
| --- | --- |
| Component and component children | `joomla_component`, `component_admin_views`, `component_custom_admin_views`, `component_site_views`, `component_router`, `component_config`, `component_placeholders`, `component_updates`, `component_files_folders`, `component_custom_admin_menus`, `component_dashboard`, `component_modules`, `component_plugins` |
| Modules | `joomla_module`, `joomla_module_updates`, `joomla_module_files_folders_urls` |
| Plugins | `joomla_plugin`, `joomla_plugin_group`, `joomla_plugin_updates`, `joomla_plugin_files_folders_urls` |
| Views and view relationships | `admin_view`, `admin_fields`, `admin_fields_relations`, `admin_fields_conditions`, `admin_custom_tabs`, `custom_admin_view`, `site_view` |
| Reusable application definitions | `template`, `layout`, `dynamic_get`, `custom_code`, `field`, `validation_rule`, `fieldtype`, `library`, `library_config`, `library_files_folders_urls`, `class_method`, `class_property`, `class_extends`, `placeholder` |
| Code and distribution definitions | `power`, `joomla_power`, `repository`, `snippet` |

File and folder transport has separate handlers. The catalogue should not be read as a statement that every compiler lookup automatically performs a remote search, or that every type uses the same key and serializer. The factory and service container select the applicable handler; entity configuration supplies its precise contract. [B01](../reference/source-map.md#b01)

## Ordinary acquisition preserves local working knowledge

For an ordinary initialization request, an existing local definition satisfies the request. A missing definition can be obtained from a configured repository, mapped into the local representation, and stored. Dependencies exposed by that payload are queued for acquisition. This policy allows a developer to retain local edits rather than having a remote copy overwrite them on every lookup.

The broad operation is:

```text
initialize(request):
    normalize the entity type and identifying value
    if this request has already been attempted in this operation:
        return its recorded state
    record that the attempt has begun
    if an acceptable local record exists:
        record LOCAL
        return the local record
    select a configured repository whose index contains the request
    retrieve and map its payload
    persist the mapped definition
    enqueue its declared dependencies and assets
    record the operation's result
```

This pseudocode exposes the roles. The actual handlers determine error handling and persistence behaviour; marking an attempt is not the same event as successful retrieval. [B02](../reference/source-map.md#b02), [B06](../reference/source-map.md#b06)

## Repository selection and payload retrieval are distinct

The repository search services cache and consult indexes for the appropriate entity channel. They search configured sources in order and select an index match. The selected entry then supplies the payload location and identifying information.

In the inspected retrieval path, selecting the first index match does not guarantee automatic fallback to every later repository if that selected payload is malformed or unavailable. Index selection and payload failure are separate states. A reader implementing the architecture should make that policy explicit instead of treating a lookup as an unspecified “search everywhere until something works.” [B04](../reference/source-map.md#b04)

A repository's read branch and write branch also have different purposes. A developer can consume reviewed definitions from one branch while publishing changes to another. The request's effective source therefore includes repository configuration and branch selection, not just an entity GUID.

## Discovery extends the local model

The architectural consequence of retrieval is local ownership of an editable representation. Acquiring a field is not simply fetching transient text for one output file. Its definition is stored, can be inspected in the GUI, can be revised, and can be reused by subsequent requests and builds. Powers follow this same broad pattern while adding code-specific dependency and namespace processing.

The field loader demonstrates an embedded use of the mechanism: after local lookup fails for a valid GUID, a guarded remote attempt can add the field and allow the loader to retry. Other acquisition paths invoke the package builder explicitly. Both connect portable identity to local data; neither requires every consumer to know the repository's physical file layout. [C04](../reference/source-map.md#c04)

## Scope and repeatability

A request guard bounds repeated work within an operation. A stable source snapshot and fixed repository precedence make acquisition repeatable for the same requests. Changing a repository branch, a local record, or selection policy changes the effective input.

The [dependency chapter](dependencies.md) explains how newly discovered requests are drained. The [import chapter](import.md) distinguishes ordinary initialization from an explicit reset, and the [formal resolution model](../formal/resolution.md) states the conditions under which traversal terminates and resolves a complete requested graph.
