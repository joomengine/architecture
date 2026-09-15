---
title: Binding in ordered stages
description: Shared and contextual environments, ordered replacement semantics, introduced tokens, and the transition from staged text to file content.
section: Compiler
order: 35
evidence: Placeholder, ContentOne, ContentMulti, Dispenser, and FileContent
---
# Binding in ordered stages

A reusable code fragment can contain names that depend on the extension, view, or target where it will be used. JCB retains such material and applies the appropriate binding environment when that context is available. It also fills file skeletons using shared and context-specific content accumulated by earlier generation work.

These are staged binding operations. The stages matter because a value inserted by one operation can still contain tokens handled by another. The exact replacement semantics determine what happens within each stage. [C06](../reference/source-map.md#c06), [C08](../reference/source-map.md#c08)

## Shared bindings and use-site bindings

`ContentOne` supplies shared material such as component identity, author information, versions, and common generated fragments. `ContentMulti` supplies bindings associated with a view or extension key. The per-file writer sets the current filename and applies shared content before the selected contextual content.

Prepared custom code can also be bound when retrieved from the dispenser. This allows one stored fragment to use the placeholders active for its destination rather than fixing all names at initial storage time. [C09](../reference/source-map.md#c09)

For a staged artifact $a_i$ and binding environment $P_i$, write

$$
a_{i+1}=\sigma(a_i,P_i).
$$

The environment is authoritative for that stage. The complete artifact is produced by a defined sequence of these operations together with other transformations such as code expansion, header processing, and dependency injection.

## Replacement within a pass is ordered

The inspected placeholder service uses array-based ordered string replacement. For a map presented as the ordered sequence

$$
P=\langle(k_1,v_1),\ldots,(k_n,v_n)\rangle,
$$

its ordinary replacement is

$$
s_0=s,\qquad
s_i=\operatorname{replaceAll}(s_{i-1},k_i,v_i).
$$

Later entries can therefore replace tokens introduced by earlier entries. This differs from simultaneous substitution, where all matches are selected from the original input and replacements are not revisited during that pass.

JCB's implementation gives the operation three action modes. The ordinary mode performs replacement. A presence-check mode skips work when none of the keys occurs. The filtered mode first removes entries whose keys do not occur in the original input, then performs ordered replacement with the remaining entries. [C08](../reference/source-map.md#c08)

## Filtering the map changes introduced-token behaviour

Consider the ordered map `A → B`, `B → x`.

| Input and mode | Selected entries | Result |
| --- | --- | --- |
| `A`, ordinary replacement | Both entries | `x` |
| `A`, original-input filtering | Only `A → B` | `B` |
| `A B`, original-input filtering | Both entries | `x x` |

The filtered mode does not remove unknown placeholders from the output. It removes unused entries from the replacement map before applying that map. This distinction is essential when describing later binding stages or testing an implementation in another language.

The [reference mechanisms](../engineering/reference-model.md) exercise these cases directly. A reimplementation that silently substitutes a simultaneous or recursive replacement algorithm would change the represented semantics.

## File processing has several ordered transformations

The per-file service reads the staged file, processes its PHP header and BOM convention, applies shared bindings, applies contextual bindings when a context is supplied, conditionally updates custom code, triggers the pre-write event, resolves Power and Joomla Power references, and writes the result. Power source files have a selected bypass around the ordinary shared binding path. [C19](../reference/source-map.md#c19)

The sequence can be represented as a composition:

$$
\operatorname{write}\circ\operatorname{inject}\circ\operatorname{event}
\circ\operatorname{custom}\circ\sigma_{\Gamma}\circ\sigma_{\mathrm{shared}}.
$$

Each operation has its own condition and input. The expression captures the inspected order; it is not an assertion that all of these operations are pure functions. Events, dependency retrieval, counters, and file writes have effects recorded in the [state model](../formal/state.md).

## Newly exposed work belongs to a later operation

A custom-code expansion can expose a Power reference. A template can introduce a placeholder handled by a subsequent binding environment. A file update can require a library definition that was not previously active. JCB's sequence gives such work designated processing points.

This explains why generation need not be a single substitution over a complete final dictionary. The compiler can prepare some values early, keep other fragments contextual, and perform selected discovery and injection later.

The corresponding ordering obligation is straightforward: a token or dependency must have an applicable consumer after the operation that introduces it. Repeating replacement indefinitely is a different algorithm with different termination and escaping behaviour. The paper describes the actual selected stages instead. [Formal staging](../formal/staging.md)

## Contextual names make reuse concrete

The Hello World plugin definition uses a component placeholder in its name. When included under the component context, the generated plugin receives the corresponding resolved identity and files. Custom code similarly reaches its designated model, controller, view, or installer position with the destination's active names. [Extension trace](../examples/extension-trace.md), [Custom-code trace](../examples/custom-code-trace.md)

The reuse is therefore semantic as well as textual: the same stored representation can be interpreted for its use-site. The compiler's naming, namespace, and role decisions must already agree with the environment supplied to that stage.

Staging gives this process an inspectable order. It also explains where a value remains unresolved and which operation is responsible for completing it. That is the useful abstraction to carry into another implementation language.
