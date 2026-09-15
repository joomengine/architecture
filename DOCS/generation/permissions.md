---
title: Compiling access-control behaviour
description: Action declarations, component and record assets, field-level form treatment, configured result redaction, and permission-sensitive storage.
section: Generation
order: 43
evidence: Permission creators, form generation, result modeling, and save transformations
---
# Compiling access-control behaviour

JCB can represent access-control decisions in the model and generate the declarations and checks that a Joomla application evaluates at runtime. The compiler processes policy structure; the generated application applies it to users, groups, assets, and records.

This separation is essential. The permission of the person running JCB to import code is a build-time concern. The permission of a later application user to edit a record or interact with a field is generated runtime behaviour. [C14](../reference/source-map.md#c14)

## Actions, scopes, and generated consumers

The permission creator builds mappings for view-specific and component/global actions, labels and descriptions, dashboard behaviour, and related access sections. Model and view generators use those mappings rather than independently inventing action names at every destination.

A runtime authorization request can be modeled as

$$
\operatorname{allow}(u,a,s),
$$

where $u$ is the runtime user, $a$ an action, and $s$ the relevant asset scope. The compiler emits the action and asset expressions; Joomla's runtime policy machinery supplies the result.

Existing-record operations can use a record asset, while creation paths can use the component asset where no record identity exists yet. Generated toolbar state, controller checks, form treatment, and model behaviour consume the appropriate action mappings. The exact consumer and scope determine the guarantee.

## Field-level policy changes form behaviour

The inspected form-generation path implements field options named `edit`, `access`, and `view`. Their generated behaviour is type-sensitive:

| Field option | Representative generated form behaviour |
| --- | --- |
| Edit | Disables and marks a field read-only when authorization fails; selected input types receive additional disabled styling; empty values receive type-dependent filtering or removal treatment |
| Access | Removes the field from the form when authorization fails |
| View | Removes spacer-like fields, or makes ordinary fields hidden with additional handling for empty or array values |

These are the actual roles of the selected options. A hidden input is a presentation and submission choice, not a confidentiality boundary by itself. The access and strict-result paths serve different purposes and must be configured and understood accordingly. [C14](../reference/source-map.md#c14)

The source contains separate handling for view/record creation, deletion, editing, and state changes. Those record-level operations should not be casually renamed “delete a field” or treated as identical to the three field-form options.

## Strict result treatment is separately controlled

Where field-permission generation enables the relevant path, the generated model includes a runtime `strict_permission_per_field` setting, defaulting to inactive. When active, selected `access` or `view` authorization failures cause the corresponding retrieved field value to be replaced with an empty string in the result-processing loop.

This is post-retrieval result treatment. It is not the same operation as adding a database predicate that prevents the column from being read. The generated code checks the configured field action against record and component scope as represented in the emitted condition. [C14](../reference/source-map.md#c14)

For the selected value treatment, write

$$
R'[i,f]=
\begin{cases}
\varepsilon, & \text{strict mode and the generated authorization condition denies }f,\\
R[i,f], & \text{otherwise}.
\end{cases}
$$

The equation exposes both the option and the runtime condition. It does not assert that every output path automatically has the same redaction policy.

## Storage handling must respect omitted fields

Permission-driven form treatment can remove a value from submitted data. The save generator accounts for that interaction in its JSON-item handling: it distinguishes an omitted value that should be cleared from an omitted value absent because the user lacks the relevant permissions.

That is a non-obvious cross-concern dependency. A storage transformation that always converted a missing field to an empty value could erase data that the current user was not allowed to edit. The compiler's permission-aware branch coordinates the form and save paths. [C14](../reference/source-map.md#c14)

This example shows why access control belongs inside the architectural explanation rather than in a feature list. The permission definition affects declarations, controls, result treatment, and storage semantics together.

## The policy is generated, not decided at compile time

The compiler does not know every future application user or record. It emits expressions and branches that evaluate those values later. The design describes permitted operations; the runtime supplies the user and asset context.

A portable implementation should likewise separate policy declarations from policy evaluation and from the UI consequences of an authorization result. Hiding a control, rejecting a write, filtering a result, and declaring an action are distinct responsibilities even when driven by the same policy definition.

## Evidence and scope

The Hello World package demonstrates generated access sections and ordinary application action structure. It is not configured to exercise every field-level policy branch. The detailed field behaviour in this chapter is traced to the compiler's corresponding generation paths. [E02](../reference/source-map.md#e02), [C14](../reference/source-map.md#c14)

This combination of source correspondence and concrete output keeps the account precise. The architecture supplies coordinated policy generation for its represented options; applications and extensions retain responsibility for the behaviour of custom code and independently added interfaces.
