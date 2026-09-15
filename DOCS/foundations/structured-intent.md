---
title: Structured intent as compiler input
description: How GUI-authored choices form a domain-specific application description whose consequences are supplied by compiler rules.
section: Foundations
order: 11
evidence: Blueprint properties, editor definitions, and compiler interpretation
---
# Structured intent as compiler input

The JCB editor lets a developer express many implementation decisions as structured choices. A field has a type and storage description. Its placement in an admin view can give it list, title, alias, search, sorting, filtering, alignment, and tab roles. A component selects views, extension relationships, configuration, namespace, target, and packaging behaviour. Custom code supplies the parts that are intentionally expressed as code.

These choices form a domain-specific application description. The GUI is one authoring surface for it; the database is a working representation; a repository blueprint is a portable representation. Compilation depends on the represented intent, not on whether a person originally entered it by clicking a control or importing a definition. [B01](../reference/source-map.md#b01), [E01](../reference/source-map.md#e01)

## A small decision can have several precise consequences

In Hello World, a field association sets `title`, `sort`, `search`, and `link` alongside the field identifier. Each flag addresses a distinct concern. The compiler records title behaviour, sortable ordering, searchable query participation, and link presentation while retaining the field's common identity and name.

The important economy is **not repeated textual compression**. The developer specifies a decision once, and established generation rules carry that decision into the relevant implementation locations. The rule knowledge already resides in the compiler and its supplied material.

Let an editor submission $u$ be normalized into a model $N(u)$. For a concern $k$ and target $T$, an interpretation rule computes

$$
P_{k,T}(N(u),\Gamma).
$$

The result can be a fragment, a structured record, a requirement, or no contribution when the feature is disabled. The same normalized choice can therefore feed several concern-specific projections without assigning it several inconsistent meanings.

## Representation is not the same as natural-language inference

The editor's intent is constrained and explicit: identifiers, selected options, structured relationships, templates, and authored code. For example, a searchable flag authorizes generation of known search behaviour; it does not infer an unspecified business rule from the word *Greeting*.

This distinction explains both the compactness and the repeatability of the input. A developer need not restate Joomla's controller and model conventions for every field, because the compiler supplies them. Application-specific choices remain represented in the blueprint or custom code.

The architecture thus combines declarative configuration with imperative escape points. A model can express conventional behaviour compactly while retaining a route for domain-specific methods, views, scripts, libraries, and services. [C05](../reference/source-map.md#c05), [C09](../reference/source-map.md#c09)

## Selection, validation, and interpretation are separate

An editor can constrain which values are entered. Persistence can normalize and encode those values. Compilation interprets their relationships under a target and a use-site context. Runtime code then applies the generated behaviour to application data and users.

These are four different moments. A compiler permission to import a blueprint, for example, is not the runtime permission of a future user to edit a generated record. Similarly, a field's database width and its form input's maximum length are distinct properties. The Hello World Greeting field uses a database width of 255 and an input maximum of 50; the compiler preserves their different roles. [Field trace](../examples/field-trace.md)

## A language-neutral implementation

An implementation in another technology needs an explicit model schema and a normalization layer, not a replica of JCB's PHP forms. It can offer a browser editor, command-line authoring, an API, or file-based definitions. All should produce the same typed model for the compiler.

The essential interface is:

```text
normalize(authoring_input) -> model or diagnostics
resolve(model_roots, repositories) -> available definition graph
interpret(definition_use, context) -> ordered contributions
materialize(contributions, target_rules) -> application artifacts
```

Validation remains attached to these boundaries. References must identify supported entity types; generated names must satisfy target rules; feature combinations must be interpreted consistently. The interface does not turn arbitrary incomplete input into a complete application.

Model-driven engineering and structured language work provide the established vocabulary for this arrangement. The relevant correspondence is the separation of domain intent from repeated target-platform implementation, not a claim that every GUI is a compiler. [R01–R03](../reference/bibliography.md#r01)
