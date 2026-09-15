---
title: Queries, selections, and result structure
description: Dynamic Get definitions, aliases, joins, filters, list state, and generated model code.
section: Generation
order: 41
evidence: Dynamic Get modeling and selection services, list builders, and generated models
---
# Queries, selections, and result structure

A generated view needs more than a form or template. It needs a defined way to obtain application data, name the selected values, apply filters and ordering, and expose the result to presentation code. JCB represents much of that work through Dynamic Get definitions and field-derived list builders.

The query definition is compiled into the generated application's model. The runtime application executes that generated query logic; it does not need to consult JCB's authoring GUI to rediscover the design. [C12](../reference/source-map.md#c12), [D01](../reference/source-map.md#d01)

## Query intent has several dimensions

Dynamic Get definitions select a primary source, additional tables or views, selected columns and aliases, join relationships, filters, predicates, grouping, ordering, and result cardinality. The documented get roles distinguish a main item or list query from additional single or multiple-result methods.

The source can be a modeled backend view, a named database table, or an explicitly customized retrieval path. These choices determine how much structure the compiler can derive automatically and which parts remain authored code.

A compact abstract query is

$$
q=(S,J,\Pi,\Phi,G,O,L),
$$

where $S$ is the source, $J$ the joins, $\Pi$ the selection/alias map, $\Phi$ predicates and runtime filters, $G$ grouping, $O$ ordering, and $L$ limit/pagination behaviour. This tuple describes the represented query intent; the target emitter supplies the platform-specific query construction.

## Selection establishes names used later

The selection service distinguishes a direct database table from a modeled view table and resolves the corresponding table name. It parses selected expressions and aliases, records source-column-to-result-key relationships under a method key, and prepares query fragments.

For modeled view selections, it also retains mappings from the original field to its use in a particular site query. That information can later connect field treatment to the appropriate selected value. The result is not just SQL text: it includes a map between source meaning and result names. [C12](../reference/source-map.md#c12)

Write that map as

$$
\alpha_q:(\text{source alias},\text{column})\mapsto\text{result key}.
$$

Downstream consumers should use $\alpha_q$ rather than independently guessing which name a joined column acquired.

## Wildcards still require structural knowledge

A wildcard selection can require the compiler to obtain the underlying columns so it can establish field and alias mappings. The emitted query may retain a wildcard in the cases where the source's rules permit it, while particular joined single-row cases produce explicit aliased selections.

This is another example of semantic preparation exceeding the final text. The compiler may inspect a richer description to emit a compact query expression while retaining the mappings needed by later generation.

Alias collision handling is scoped by the query/method and its source roles. The inspected selection code can prefix a joined view's result key under its conflict condition. That is a particular policy, not a claim that arbitrary SQL expressions are globally normalized into a unique relational schema.

## Field-derived list behaviour joins the same model

An admin field association can activate search, sorting, filtering, list display, or a joined display relation. Classification stores those decisions in distinct builders. Later list-model generation combines them with standard state, selected fields, custom code, and target conventions.

The Greeting field's association makes it searchable and sortable. Its generated list head and sort options use the same resolved column and language label that appear in the field trace. The coordinated behaviour comes from the association plus compiler rules, not from additional manually written query code in the blueprint. [Field trace](../examples/field-trace.md)

## Query execution and result modeling are separate

After retrieval, the generated model may transform stored representations, attach related results, process configured custom code, prepare display values, or apply selected permission handling. A field relation can act before modeling, after modeling, or in presentation.

A useful decomposition is

$$
R=\operatorname{execute}(\operatorname{emitQuery}(q,T),\rho),
\qquad R'=\operatorname{modelResult}(R,\Gamma),
$$

where $\rho$ supplies runtime values such as filters, user information, or request parameters. The compiler emits both operations; compilation itself does not execute every future application query.

This separation matters when interpreting the phrase “the compiler understands the query.” It understands the represented structure sufficiently to emit the selected query and its result-handling code. Runtime data remains runtime input.

## Cardinality shapes generated methods

Single-item, list, and supplementary-query roles affect generated method structure and the values exposed to a view. Joined single records and collections have different representation requirements. Pagination connects model state and query limits to view-side navigation.

Those are cross-file obligations. A pagination choice can require both model logic and presentation support. A result alias used in a template must agree with the model's selected key. A lookup filter must use the correct field and value source.

The public Hello World site views and Dynamic Get records provide a small example of these connections. The Service Directory extends the same mechanisms across a substantially larger generated application. [Hello World](../examples/hello-world.md), [Service Directory](../examples/service-directory.md)

## The portable architectural principle

A reimplementation needs a typed query description, an alias/result map, target-aware emitters, and a clear boundary between compile-time structure and runtime values. It can use a different database API or language while preserving those roles.

Relational algebra provides vocabulary for selection, projection, and joins; model-driven generation explains the compilation of their structured description into code. The paper uses those correspondences to clarify the implementation rather than claim a new query algebra. [Bibliography](../reference/bibliography.md)
