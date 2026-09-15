---
title: Host, target, and architecture selection
description: Separating the Joomla installation running JCB from the platform conventions selected for generated output.
section: Compiler
order: 38
evidence: Compiler configuration, architecture service providers, and Joomla Power mappings
---
# Host, target, and architecture selection

JCB runs inside a Joomla installation and generates extensions for a selected Joomla target. These are distinct contexts. The host supplies services used to execute the compiler; the target determines the conventions of the generated application.

The architecture makes this distinction operational through configuration, templates, architecture services, and version-sensitive mappings. The inspected compiler contains target families for Joomla 3, 4, 5, and 6. Individual features and emitters follow their supported target contracts. [C21](../reference/source-map.md#c21)

## One model, selected implementation rules

A blueprint can retain the application's fields, views, relationships, queries, and custom intent while the compiler selects target-specific generation rules. For a normalized model $D$ and target $T$, write

$$
A_T=\operatorname{compile}(D,\Theta_T,C,H),
$$

where $\Theta_T$ denotes the selected target rules and supplied target material. Changing $T$ changes the implementation conventions applied to the same represented application intent.

This does not imply that arbitrary target-specific custom code automatically becomes portable. A blueprint that embeds platform-specific calls still contains those calls unless a mapping or transformation handles them. Target portability is strongest where the model uses the compiler's represented abstractions and version-aware references.

## Logical services select concrete emitters

The architecture service providers register concrete implementations for supported Joomla generations and expose logical services to consumers. When a consumer requests a model, controller, view, module, or plugin operation, the provider selects the implementation using the compile-target configuration.

The module architecture provider, for example, registers version-specific services and resolves its logical operation against the configured Joomla version. This keeps a consumer's responsibility separate from the details of each target implementation. [C21](../reference/source-map.md#c21)

A language-neutral description is

$$
\operatorname{service}(r,T)=\Theta_T[r],
$$

where $r$ is a generation responsibility. The responsibility remains stable while its implementation changes with the target.

## Shared service lifetime matters

Target-specific service selection can be cached in shared provider state. The selected target must therefore be established before those services are resolved, and independent builds must respect the calling workflow's reset boundaries.

An implementation should not assume that changing a configuration value after target services have already been created will reconstruct all of them automatically. The source's service lifecycle is part of the execution model. [Stores](stores.md), [Events](events.md)

This is a general lesson of configuration-driven dispatch: a target is both an input value and a selection boundary for the objects or functions that implement it.

## Symbol mappings complement emitter selection

Joomla Powers select the appropriate namespace and type for a stable platform-reference identifier. Templates and emitters select structural conventions. Together, these mechanisms handle different dimensions of target adaptation.

A generated plugin may need a particular service-provider arrangement as well as the correct imported platform class. A model may need a target-specific method body and a target-appropriate form or routing convention. A single textual version placeholder cannot express all of those differences; distinct architecture responsibilities can. [Powers](powers.md), [Extensions](../generation/extensions.md)

## Build area is another axis

Within a component, administrator, site, and API areas have different responsibilities. Modules can target their configured client. Plugins belong to a group and have their own extension context. The compiler establishes build and language targets as it moves through those areas.

The complete context is therefore more informative than a Joomla version number alone. It includes the extension kind, area, namespace, view role, and applicable configuration. The [context model](../foundations/context.md) records those dimensions separately.

## Regeneration carries shared platform knowledge

When a target emitter or reusable mapping is updated, applications that use that represented mechanism can receive the change on regeneration. The implementation decision is maintained in the compiler or reusable definition rather than repeated by hand in each generated project.

The maintenance effect is conditional on the application's ownership choices. Default-generated regions follow the changed rules. Deliberate complete-class overrides and arbitrary embedded code remain authored material with their own maintenance obligations. [Regeneration](../engineering/regeneration.md)

The architecture thus multiplies a shared implementation change across the models that use it. The effect follows from the separation between application intent and target implementation; it does not require a claim of automatic semantic migration for every possible external program.

For another technology, the same structure can select database dialects, framework versions, deployment platforms, or language backends. The portable principle is explicit dispatch by a complete target context, with stable model meaning and clearly owned target-specific rules.
