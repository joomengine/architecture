---
title: Fields, forms, layouts, and nested presentation
ndescription: Field structure and recursive presentation dependencies.
description: From field-type definitions and view associations to form attributes, layouts, validation, conditional behaviour, and nested template dependencies.
section: Generation
order: 42
evidence: Field creators, layout builders, template/layout acquisition, and public documentation
---
# Fields, forms, layouts, and nested presentation

A form is one visible result of several coordinated interpretations. Field-type definitions supply available properties and behaviour; field definitions select those properties; view associations establish placement and roles; the target supplies form and view conventions; permissions and conditions can modify generated behaviour.

The compiler retains those decisions in field, layout, script, language, and code stores before assembling the output. A form is therefore not an isolated template expansion detached from the application model. [C04](../reference/source-map.md#c04), [C05](../reference/source-map.md#c05)

## Field types and field instances

A field type describes a reusable kind of input or display element. A field instance supplies its configured name, label, properties, storage information, and custom behaviour. Its use in an admin view adds placement, ordering, tab, list, title, alias, filter, and related roles.

These layers let one field-type definition support many fields and one field definition participate in several contexts. The compiler resolves names and attributes under those contexts rather than assuming every reuse should share a mutable occurrence-specific result.

Hello World's Greeting field illustrates the distinction. Its database length is 255, while its form maximum is 50. Its title and list roles are carried by the view association. The generated schema and XML retain those different meanings. [Field trace](../examples/field-trace.md)

## Layout is an accumulated interpretation

The field builder determines a tab name from the view's tab mapping, recognizes selected standard placement cases, and records the field in the layout builder with its occurrence settings. Later form and view generation consumes the resulting arrangement.

For a view $v$, the layout can be modeled as an ordered grouping

$$
\mathcal{L}_v=\langle(\text{region}_i,\langle o_{i1},\ldots,o_{in_i}\rangle)\rangle.
$$

The grouping retains occurrence identity and order. It is not merely a set of field definitions, because the same definitions in another order or region can produce a different interface.

Conditional fields, custom tabs, and relation-specific scripts add further contributions. Their generated code depends on the same resolved names used by the form and data model. [C05](../reference/source-map.md#c05), [D01](../reference/source-map.md#d01)

## Validation and custom field behaviour

Field XML can identify a validation rule. The field-data path registers the rule, and later content preparation creates the required validation output when custom rule data is present. Custom field definitions can also require generated classes and supporting code.

A rule name, its implementation, the form reference, and the generated file are related outputs. Their alignment is another instance of the compiler's definition-to-contribution-to-artifact relationship.

Scripts associated with a field are prepared through the dispenser and guarded by field/view processing state. Reusing the field in a view need not append its script repeatedly; using it in another view can require a distinct contribution. [Acquisition](../compiler/acquisition.md), [Stores](../compiler/stores.md)

## Templates and layouts can reveal further dependencies

JCB's template/layout data service recognizes supported literal template-load and layout-render references in content. It resolves the corresponding alias, stores the acquired template or layout data, and scans the acquired HTML and view-code material for further references.

Templates are retained under a build-target, view, and template key. Layouts use a build-target and layout key. The scopes differ because templates and layouts have different reuse roles. When content is destined for both relevant language/build areas, the implementation can prepare layout data for the corresponding area as well. [C11](../reference/source-map.md#c11)

The service stores a discovered item before traversing its nested content. This gives repeated or cyclic references a stable presence check and avoids treating every encounter as a new acquisition.

## Static recognition has an explicit domain

The template/layout scanner recognizes particular literal call forms, including the supported quote variants and Joomla Power layout reference convention. It follows those represented dependencies; it does not infer the value of every arbitrary runtime expression that might compute a template name.

For content $c$, let $\operatorname{refs}(c)$ be the references recognized by that grammar. Nested acquisition completes the reachable set under those references. The [dependency model](../formal/resolution.md) applies with that explicitly defined relation.

The precision is useful to another implementer. It identifies which syntax must be recognized and how the result enters the shared acquisition machinery, rather than describing the feature as unrestricted source-code comprehension.

## Presentation and model concerns remain connected

A list-field relation can combine the presentation fragments of several fields, retaining their generated links and formatting. A model-side relation instead combines raw or modeled values. A template consumes the names and shapes established by its Dynamic Get. Permissions can change which form controls or result values are exposed under configured paths.

These connections make the generated interface part of the application, not merely its wireframe. The [queries](queries.md) and [permissions](permissions.md) chapters explain the corresponding model and policy work.

A portable implementation can use another UI technology while retaining the same sequence: resolve field kinds, interpret occurrences, establish names and data contracts, collect layout and behaviour contributions, resolve nested presentation dependencies, and emit the target's interface artifacts.
