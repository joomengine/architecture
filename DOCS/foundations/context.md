---
title: Context and interpretation
ndescription: Context-qualified reuse and the separation of build, target, occurrence, and runtime concerns.
description: How target, extension, view, role, and binding environment qualify the interpretation and reuse of definitions.
section: Foundations
order: 13
evidence: Compiler configuration, view-sensitive processing, and output bindings
---
# Context and interpretation

A definition does not determine all of its generated uses by itself. Its interpretation depends on where it is used and what is being built. A field label acquires an extension and view language prefix; a reusable class acquires a resolved namespace and destination; a code block receives the placeholders active at the point of use.

Represent the relevant environment as

$$
\Gamma=(T,e,v,r,\ell,P,a),
$$

where $T$ is the generation target, $e$ the extension, $v$ the view or other use-site, $r$ the generation role, $\ell$ the language destination, $P$ the binding environment, and $a$ additional occurrence settings. This tuple is a semantic description, not a requirement to copy the entire environment into every cache key.

## Context is carried in several forms

In JCB, context can be carried by a service argument, an association record, a view-scoped store key, or the shared build configuration. `ContentOne` supplies shared file bindings; `ContentMulti` partitions bindings by view or extension key. The custom-code dispenser stores prepared material and applies the active placeholders when retrieving it. Field-specific processing tracks which field scripts have already contributed to a view. [C04](../reference/source-map.md#c04), [C06](../reference/source-map.md#c06), [C09](../reference/source-map.md#c09)

These mechanisms cooperate. A globally reusable field definition does not require every derived fragment to be globally reusable. Some of its properties can be cached by definition identity, while other consequences must be established for each use-site.

## Reuse depends on the information actually read

For an interpretation $J$, let $\pi_J(\Gamma)$ denote the dimensions of context on which it depends. A sufficient reuse condition is

$$
\pi_J(\Gamma_1)=\pi_J(\Gamma_2)
\quad\Longrightarrow\quad
J(d,\Gamma_1)=J(d,\Gamma_2),
$$

provided the definition and other read inputs are also the same.

A database-column description may depend on different dimensions than a language key or namespace. Treating them as separate contributions allows their reuse boundaries to differ. The [classification model](../formal/classification.md) develops this as a dependency contract.

This condition is used to explain correct reuse, not to assert that every production callback has been proved context-independent. An extension hook that reads an additional value extends the actual dependency set. The operational trace must include that read.

## Ordered context changes

A shared configuration can be updated as generation moves from an administrator view to a site view, module, or plugin. Such a design requires the correct context to be established before each consumer runs. Where a service temporarily changes a value and restores it, both actions belong to its behaviour.

The module and plugin infusers, for example, establish their build target, language target, and language prefix before assembling their content. Target architecture services select implementations using the requested output Joomla version. [C17](../reference/source-map.md#c17), [C18](../reference/source-map.md#c18), [C21](../reference/source-map.md#c21)

A language-neutral implementation may express these boundaries using explicit immutable context arguments instead. That is a representation choice; preserving the visible interpretation and ordering is the architectural requirement.

## Build context and runtime policy

The user running the compiler is not the user who will later operate a generated application. Build-time access controls govern operations such as reading local data and accepting external code. Generated access-control rules govern later application operations.

The compiler processes the *definition* of runtime policy. It emits checks, action declarations, and interface behaviour that Joomla evaluates against runtime users and assets. Conflating those contexts would make an architectural explanation of field permissions incorrect. [Permissions](../generation/permissions.md)

The same separation applies to host and target versions. The Joomla installation executing JCB supplies host services; the chosen compile target determines output conventions. [Target selection](../compiler/targets.md)
