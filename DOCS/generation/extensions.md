---
title: Components, modules, and plugins
ndescription: Complete extension products from a related design graph.
description: Shared compiler services and extension-specific acquisition, context, structure, content, and packaging paths.
section: Generation
order: 46
evidence: Component generation, module and plugin data/structure/infusion services, and public outputs
---
# Components, modules, and plugins

JCB can produce a component together with related modules and plugins. The outputs share reusable definitions and compiler services while retaining extension-specific structures, namespaces, entry points, language prefixes, and installation metadata.

The Hello World repositories make that distinction visible: one portable design graph is associated with a component, the Site Redirect module, and a Privacy plugin. Their generated repositories are different products of the compilation lifecycle, not three copies of the same template tree. [E01–E04](../reference/source-map.md#e01)

## Component generation coordinates application concerns

A component can include administrator, site, and selected API areas, models, controllers, views, forms, layouts, fields, validation rules, libraries, language files, installation/update SQL, manifests, and installer code. Which artifacts appear depends on the model and target configuration.

The component's selected views provide the occurrences from which much of this material is derived. Field classification, Dynamic Gets, permissions, routing, custom code, and layout relationships contribute to the resulting native application. [C01](../reference/source-map.md#c01), [C05](../reference/source-map.md#c05), [C19](../reference/source-map.md#c19)

The compiler's contribution is the coordinated implementation, including low-level details, rather than only the creation of empty controller or model files.

## Module generation has its own context

The module data service acquires the module definition and its related settings. Structure generation prepares the target's module files. Infusion establishes the module's build target, language target, and prefix, then prepares provider, dispatcher, Dynamic Get, helper, default-template, installer, fieldset, and manifest material according to the selected target and features.

These responsibilities are delegated to architecture services where target versions require different output conventions. The module shares placeholder, language, dependency, and file services without adopting the component's namespace and file layout indiscriminately. [C17](../reference/source-map.md#c17), [C21](../reference/source-map.md#c21)

For an extension occurrence $e$, the content environment is

$$
P_e=\operatorname{prepareExtension}(d_e,\Gamma_e,\Theta_T).
$$

The target-specific file writer then uses that environment for the module's artifacts.

## Plugin generation resolves group and class structure

A plugin definition identifies its plugin group, base-class information, methods, properties, custom code, and selected installation/configuration material. Those referenced class-related entities participate in acquisition and blueprint distribution.

The plugin infuser establishes plugin-specific placeholders, namespace information, build and language targets, and the language prefix. It then prepares the extension class, service-provider material, installer code, fieldsets, and main manifest through the applicable architecture services. [C18](../reference/source-map.md#c18)

The Hello World plugin's blueprint name includes a component placeholder. The selected component context resolves that name into the final plugin identity. This is a particularly clear example of a reusable definition whose final naming is established by its occurrence. [Extension trace](../examples/extension-trace.md)

## Structure, content, and archive are separate stages

Each extension family has data acquisition, structure preparation, content preparation, file updating, and archive responsibilities. A directory can be created before all its content is bound. A content map can be prepared before its corresponding file is finally written. An archive is produced after the selected file operations.

This separation permits shared dependencies and late-discovered Powers to join the output process while the compiler retains the distinct artifact sets for components, modules, and plugins. [Materialization](materialization.md)

It also makes diagnostics precise. A component archive result, a module archive result, and a plugin archive result are separate outcomes in the orchestration. The complete build report should preserve those distinctions.

## Native products retain their runtime contracts

The generated extensions use the target platform's extension structure and the dependencies included or referenced by the selected build. The authoring model has been compiled into those artifacts; normal runtime requests do not need the JCB editor to interpret the blueprint again.

Reusable Powers and other supplied classes are part of the generated/assembled product where selected. Their inclusion does not imply that the compiler authored those class bodies during each run. It resolves, contextualizes, places, and connects supplied knowledge as part of the application. [Powers](../compiler/powers.md), [Accounting](../examples/accounting.md)

## A shared model can drive a product family

The component's module and plugin relationships provide one way to define a related set of products. The same field types, code definitions, configuration patterns, and target rules can also be reused across independent projects.

This produces a maintenance multiplier: a correction to shared generation knowledge can be applied through regeneration wherever that knowledge is used. The effect is governed by each model's selected features and authored overrides. [Regeneration](../engineering/regeneration.md)

For another language or framework, the corresponding product family might contain a server, client library, worker, migration set, or command-line tool. The transferable architecture is a shared definition graph interpreted through distinct product contexts and emitters—not a requirement that every product have Joomla's extension categories.
