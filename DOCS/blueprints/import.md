---
title: Import, initialization, and reset
ndescription: Local-first acquisition and explicit refresh of portable definitions.
description: How portable definitions become local working records, with separate initialization and reset policies for shared and owned entities.
section: Blueprint Exchange
order: 24
evidence: Remote get, package builder, dependency tracker, and table-aware item persistence
---
# Import, initialization, and reset

Import makes portable design knowledge available in a JCB installation. The critical question is not only how to deserialize JSON. It is which identity the payload represents, how its relationships are restored, what should happen to an existing local definition, and which additional entities or assets must accompany it.

JCB separates ordinary initialization from reset. That separation protects editable local knowledge while still providing an explicit route for refreshing it from a repository. [B02](../reference/source-map.md#b02), [B06](../reference/source-map.md#b06)

## Initialization is local-first

An ordinary initialization request first checks whether the requested local record already exists. When it does, the operation can retain that record and report it as local. When it does not, the selected remote payload is retrieved and mapped into the table-aware local representation. Its dependency descriptors add further requests to the tracker.

A portable identifier is therefore resolved through the local installation's data model. The destination need not share the source installation's numeric primary keys. Relationship descriptors and table metadata identify how references are to be stored or resolved. [Identity](../foundations/identity.md)

The local result is a managed definition. A user can subsequently open it in the GUI, revise its properties or code, compile it, and export it again. Import is not merely a temporary network read performed by a string template.

## Reset is an explicit different operation

Reset requests fresh repository material for the selected entity even where a local representation exists. The package builder also distinguishes owned incoming child records from outgoing references to shared definitions.

The inspected recursive reset path forces the refresh of dependencies marked `direction: in`. Those records represent children identified through the selected parent. Outgoing dependencies continue through ordinary acquisition unless explicitly selected for reset themselves. [B02](../reference/source-map.md#b02)

This policy has a concrete purpose. Resetting a component's association record should refresh that component's selected field or view settings. It should not, merely by following a reference, silently overwrite every reusable field or library that another local project also uses.

In a language-neutral implementation, the edge role participates in refresh policy:

$$
\operatorname{mode}(e)=
\begin{cases}
\operatorname{reset}, & \text{selected parent reset and }e\text{ is an owned incoming relation},\\
\operatorname{initialize}, & \text{ordinary referenced dependency}.
\end{cases}
$$

An explicitly selected root can of course request its own reset. The formula describes the inspected recursive distinction, not a universal rule for every import tool.

## Persistence and traversal have separate state

The retrieval services record request guards, local hits, remote results, dependency queues, and diagnostics. The table-aware item service performs the local insert or update. Attempting retrieval, mapping a payload, persisting it, and completing all of its dependencies are different events.

The package builder aggregates result buckets such as local, added, and not found across nested operations. Those collections describe the operations performed; they are not a substitute for a globally transactional success certificate. A record can have been involved in more than one request path, and an acquired parent can still expose a dependency that cannot be resolved.

A precise operational model therefore retains both request state and data state. The [formal resolution chapter](../formal/resolution.md) uses `attempted`, `resolved`, and `failed` as separate concepts. They make the source's guards understandable without implying that a guard flag proves a complete record exists.

## Repository dependencies and assets complete the imported design

A component payload may depend on its admin-view associations, site-view associations, module and plugin links, router configuration, and other child records. Views add fields, conditions, relations, tabs, query definitions, and referenced reusable material. Files and folders add the images or code assets named by those records.

The resulting local graph is what compilation consumes. An index file alone cannot reconstruct it. Nor does downloading only the component's root `item.json` guarantee that all its required definitions are already available.

The [Hello World lifecycle](../examples/hello-world.md) identifies its root, association records, externally supplied field types, and generated extension products. That trace makes dependency completion inspectable rather than hiding it behind the word *import*.

## The preservation relation

For the supported design projection, export and import aim to preserve entity meaning and references while allowing installation-local storage details to differ. Let $\equiv_B$ denote equality of the normalized blueprint-relevant model. A round trip has the intended relation

$$
\operatorname{import}(\operatorname{export}(D))\equiv_B D
$$

when the selected design graph and required assets are transported, references resolve consistently, and the selected initialization/reset policies admit that result.

This is not raw database equality: omitted credentials, local IDs, editing metadata, and unrelated records need not match. It also is not automatically byte equality of generated output, because output-affecting dates, local GUI markers, target rules, and supplied dependencies are separate inputs. The [transport model](../formal/transport.md) states those conditions explicitly.
