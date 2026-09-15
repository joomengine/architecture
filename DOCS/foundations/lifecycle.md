---
title: The complete development lifecycle
description: The distinct flows connecting editor intent, portable blueprints, installed artifacts, compilation, and regeneration.
section: Foundations
order: 14
evidence: Compiler, package, extrusion, and recovery operations
---
# The complete development lifecycle

The compiler sits inside a development lifecycle with several entry and exit paths. Keeping those paths distinct explains how JCB can accept design information from an editor, a repository, or an existing extension without treating all three as the same source format.

## Authoring and durable definitions

A developer authors fields, views, relationships, configuration, and code through JCB's editor. These become local records. Referenced definitions can already be present or can be acquired from configured repositories through supported resolution paths.

The local database is an editable working representation. It contains design information as well as installation-local state. Export selects the portable parts rather than treating every database column as part of a blueprint. [Structured intent](structured-intent.md), [Blueprint representation](../blueprints/representation.md)

## Blueprint exchange

Export traverses selected entities and their relationships, prepares portable payloads and dependency descriptors, and writes their repository representations. Indexes make those representations discoverable; generated documentation makes them understandable in the repository and JCB interface.

Import resolves selected identities, preserves local definitions under ordinary initialization, acquires missing definitions, and follows discovered dependencies. Reset is an explicit refresh operation with a different overwrite policy. Assets have their own acquisition and placement path. [Export](../blueprints/export.md), [Import](../blueprints/import.md)

Thus, export and import connect two representations of design knowledge. A generated Joomla installation package is a different product: it contains runtime implementation rather than the editable JCB model.

## Compilation and deployment products

Compilation enriches the selected component graph, produces concern-specific contributions, prepares artifact structures, binds content in ordered stages, and produces extension trees and archives. Components, modules, and plugins share services and conventions while using extension-specific generation paths.

The resulting application runs using its Joomla target and included dependencies. It is not a browser facade that must consult the authoring GUI whenever a generated field is displayed. The compiler has already placed the relevant implementation in the product. [Extension generation](../generation/extensions.md)

## Extrusion from an existing extension

Extrusion starts from an installed or unpacked component's artifacts. It discovers schemas, forms, language material, manifests, permissions, classes, and view-related material. Readers recover represented facts; resolvers combine them; the developer reviews candidate mappings; writers create or update JCB definitions.

This differs from blueprint import. The artifacts do not necessarily encode every original design decision, and some decisions can be represented in more than one way. Extrusion therefore includes selection, precedence, pairing, and retained source context. [Extrusion](../extrusion/overview.md)

## Marked-code recovery

Generated files can also contain designated code regions connected to stored custom code or GUI properties. Before the next build resets its working output, the recovery machinery inspects eligible installed files and retrieves those marked edits. Fingerprint-based placement later seeks the intended location in regenerated files; an unresolved placement in an existing file has an explicit commented recovery path and warning.

This is a bounded editorial feedback mechanism, not the same operation as broad installed-component extrusion. [Custom code](../compiler/custom-code.md)

## Regeneration as the connecting operation

The next build consumes the updated definitions and current generation rules. Reusable definitions and compiler changes can therefore propagate across multiple applications through compilation. Target-specific rules can carry platform adaptations while the model retains application intent.

Formally, distinguish the transformations:

$$
\operatorname{export}:D\to B,\qquad
\operatorname{import}:(D,B)\to D',
$$

$$
\operatorname{compile}:(D,\Theta,T,C,H)\to(A,\Delta),
$$

$$
\operatorname{extrude}:A\to\text{candidate definitions},\qquad
\operatorname{recover}:A\rightharpoonup\text{designated edits}.
$$

Here $\Delta$ includes diagnostics and other recorded build effects. These functions have different domains and policies. Their combination is useful precisely because the representation boundaries remain explicit. [Formal state](../formal/state.md), [Transport equivalence](../formal/transport.md)
