---
title: Hello World — blueprint to three products
description: A public, identity-linked example connecting exported application definitions to a generated component, module, and plugin.
section: Worked Examples
order: 60
evidence: Pinned public blueprint and generated repository snapshots
---
# Hello World — blueprint to three products

The Hello World example makes the compiler's representation boundaries inspectable. Its blueprint repository contains exported JCB definitions, relationship records, dependency descriptors, indexes, generated descriptions, and assets. Its three output repositories contain the generated component, module, and plugin.

The example deliberately places recognizable comments in GUI-backed code properties. Those comments let a reader follow authored material through its stored property and into the generated method or file. Field identifiers and contextual names provide a second trace through the compiler's derived output.

## The four repositories

| Representation | Pinned source |
| --- | --- |
| Portable design | [Hello World blueprint](https://github.com/vast-development-method/hello-world-blueprint/tree/5802e7c1d9bfaac005c765ccda830a7d07cd7e12) |
| Component product | [Hello World component](https://github.com/vast-development-method/hello-world-joomla-component/tree/a81c0dd8b8f41905671a86796a3e5995685fdaba) |
| Module product | [Site Redirect module](https://github.com/vast-development-method/hello-world-joomla-module/tree/20be318a6163e253c2a9803434622467d6006709) |
| Plugin product | [Hello World Privacy plugin](https://github.com/vast-development-method/hello-world-joomla-plugin/tree/6a785145ee84212fec65a53b7c6c362ab0f8b408) |

The repository names identify their roles; the commits fix the examined snapshots. Subsequent repository changes do not silently change the examples in this edition.

## Start with the component identity

The root component is `3745af8f-f96b-4e17-831e-eb4062cd4389`. Its payload selects the name `HelloWorld`, namespace prefix `JCB`, component version `6.0.0`, and preferred Joomla target 6. Its dependencies identify component associations, configuration, reusable code, and assets.

The root is not the entire blueprint. Component child records connect it to its admin view, site views, module, plugin, routing, dashboard, and updates. The admin view then connects to field associations and custom tabs. Referenced fields point to their types; plugin definitions point to their group, base-class information, methods, and properties.

This is a typed graph, not a single JSON form whose every property maps to one output line. [Blueprint representation](../blueprints/representation.md)

## The main visible entities

| Entity | Portable identity |
| --- | --- |
| Hello World component | `3745af8f-f96b-4e17-831e-eb4062cd4389` |
| Greeting admin view | `65116558-be67-4931-95be-727fbfb16db7` |
| Greeting field | `75e830a6-a3a5-4327-9161-3f774a6f1591` |
| Site Redirect module | `21c9f6f5-3193-485d-94e7-f9c789a9fa2e` |
| Privacy plugin definition | `8aa96d76-94e3-47d1-8dd8-f430b72ed0f7` |
| Reusable README contribution | Function-name key `readMEcontributors` |

The repository contains five field definitions, two site views, two Dynamic Gets, and the code-related definitions required by its plugin example. Some required field types are supplied by the configured external field-type repository rather than duplicated into this blueprint snapshot. The local-first dependency process makes that distinction operational. [Discovery](../blueprints/discovery.md)

## What import reconstructs

An ordinary import resolves the selected root, creates missing local definitions, follows its supported dependency descriptors, and transports required assets. Existing local definitions can remain authoritative under initialization policy; an explicit reset requests the corresponding refresh behaviour.

The destination database assigns its own local record identities. Portable GUIDs and declared relationship keys preserve the design graph. The editor can then present the imported fields, views, code, and extension relationships as local working definitions.

Compilation consumes that local graph together with its target rules, templates, reusable libraries, and environment. The output is the native extension tree, not a runtime interpreter for the JSON blueprint. [Import](../blueprints/import.md), [Execution](../compiler/execution.md)

## Three complementary traces

The [Greeting field trace](field-trace.md) follows a small declaration into its form, SQL, language entries, list behaviour, and generated metadata. The index derived from its title role is particularly instructive: it appears even though the field's isolated explicit-index property is zero.

The [custom-code trace](custom-code-trace.md) follows stored code properties into controller, model, view, and installer locations. It also explains why identical marker text in two properties must not be mistaken for one unique origin.

The [extension trace](extension-trace.md) follows module fields and code, plugin class relationships, component-sensitive naming, and target-specific file structures. It shows reuse across different product contexts rather than only across files in one component.

## What the example measures

The blueprint's 33 payload JSON files occupy 65,600 bytes and 1,298 physical text lines. The three product repositories contain 32,988 physical text lines across 286 text files, within 290 files in total. Indexes, documentation, supplied library code, and binary assets are separately identified in the [accounting chapter](accounting.md).

These figures describe the pinned representations. They do not turn escaped JSON code strings into a claim about hand-written effort, and they are not the separate JCB self-build timing measurement.

The example's principal value is the trace itself: the same identified design choices can be seen before compilation and in their coordinated implementation afterward. The [formal transport model](../formal/transport.md) explains what must be held fixed when repeating that lifecycle in another installation.
