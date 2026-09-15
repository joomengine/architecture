---
title: Routing, API surfaces, and AJAX tasks
description: View-to-route mappings, request keys, target-specific API artifacts, and generated asynchronous controller/model boundaries.
section: Generation
order: 45
evidence: Router modeling and creators, API templates, AJAX modeling, and Infusion bindings
---
# Routing, API surfaces, and AJAX tasks

A generated application needs entry paths as well as data and presentation. JCB prepares routing configuration, view and request mappings, selected API artifacts, and AJAX task/controller/model material from the same application definitions and contextual names used elsewhere in the build.

These mechanisms connect external requests to generated application responsibilities. They are different delivery surfaces, with different platform contracts, rather than one interchangeable set of URLs. [C16](../reference/source-map.md#c16), [C24](../reference/source-map.md#c24)

## Router configuration follows represented views

The router model records the views, table relationships, keys, aliases, and selected construction modes needed by routing generation. The default constructor creator emits view registrations and adds a key where the represented view has the required key and alias information.

The router creator also reconciles certain default request keys with request mappings accumulated elsewhere in the build. A list view without an item key is not automatically treated as a single-record route merely because another view uses `id`. [C16](../reference/source-map.md#c16)

Represent a route-view record as

$$
r_v=(v,k_v,a_v,t_v,m_v),
$$

where $v$ identifies the view, $k_v$ its item key where applicable, $a_v$ its alias, $t_v$ its data source, and $m_v$ the selected mode. The emitted router consumes that record rather than rediscovering the view's identity from its final template filename.

## Build and parse operations use the same mapping

For supported item views, generated methods can convert an item identifier to a route segment and resolve a segment back to an identifier using the selected alias and table. The no-ID configuration changes the segment representation and the corresponding lookup path.

The two directions need compatible keys and alias semantics. They are not a universal inverse for arbitrary strings: the database contents, alias uniqueness, selected view, and route configuration determine which segments resolve.

A precise correspondence is therefore restricted to admitted items and segments:

$$
\operatorname{parse}_v(\operatorname{build}_v(i))\sim i,
$$

under the selected router's representation and lookup conditions. The paper uses this as an explanatory relation, not as a proof about every custom route implementation.

## Default, configured, and authored routing paths

The router creator selects default generation, manually configured generation, or custom code from the dispenser according to its mode settings. Constructor material before and after the parent call and selected method bodies have separate preparation paths.

This preserves a useful ownership boundary. A developer can use the compiler's derived mapping or explicitly supply the part whose behaviour differs. The custom material still receives the surrounding application context and participates in staged output binding.

## API output reuses application identity and policy

The inspected API templates use the component namespace, single or list view identity, content type, target headers, and generated permission fragments. Infusion prepares the corresponding API controller and JSON-view bindings alongside the admin-view material.

The generation path supplies API-facing artifacts when the component's selected configuration and target support them. Endpoint registration, authentication, and deployment configuration remain the responsibilities of their selected Joomla integration and extension setup. The presence of an API controller template is not by itself an assertion that every possible route is publicly exposed. [C24](../reference/source-map.md#c24)

The architectural point is reuse of the established application interpretation: view names, model responsibilities, and policy fragments do not need to be reauthored as an unrelated API model.

## AJAX separates declared input from authored work

The admin AJAX model processes selected AJAX input definitions and custom model methods. It records controller-input material in the dispenser, establishes flags that require AJAX structures, and ensures the relevant token contribution is available. A site-edit use can also cause the corresponding site AJAX path to be prepared.

Infusion later generates task registration, input handling, headers, and model method content for the appropriate area. The controller boundary is generated from represented input/task settings; the application-specific method body remains authored code. [C24](../reference/source-map.md#c24)

This is a practical instance of structured intent plus imperative implementation. The developer supplies which task and data contract are needed and what the method should do. The compiler supplies the surrounding framework structure at its designated locations.

## Cross-surface consistency

Routing, API, and AJAX generation depend on names and policies established elsewhere. A renamed view, changed request key, moved namespace, or revised permission action has consequences across those surfaces.

The compiler's shared builders and contextual bindings carry those decisions to the relevant consumers. The resulting native application contains the entry code; JCB remains a development-time dependency rather than a request-time interpreter of the authoring GUI.

The [formal classification model](../formal/classification.md) describes the common pattern: one resolved decision can contribute to several artifacts, each with its own syntax and runtime role. The [source map](../reference/source-map.md) identifies the distinct implementations so that their behaviour is not conflated.
