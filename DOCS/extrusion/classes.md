---
title: Recovering classes as reusable definitions
description: Lexical class recovery, namespace/path interpretation, Power identity, reference reconstruction, and placement in the editable model.
section: Extrusion
order: 52
evidence: Power harvester, ClassFile reader, Namespacer, Existing resolver, assembler, and writers
---
# Recovering classes as reusable definitions

Class-library extrusion recovers code into the same managed Power representation used by compilation. It identifies a declared type, retains its body and relevant metadata, resolves its namespace and import relationships, pairs it with an existing or new identity, and writes the resulting reusable definition.

The result is more than a copied source file. The class becomes locally editable and participates in JCB's dependency, placeholder, namespace, placement, export, and compilation mechanisms. [X03](../reference/source-map.md#x03)

## Harvest before writing

The Power extruder accepts selected library roots, bounds the scan, and constructs a tree of libraries, subfolders, and class candidates. Harvest can run without writing. Selection and existing-item policy determine which candidates proceed to assembly.

The writing path assembles the selected definitions, writes Powers, and records the relevant vendor/component values on the paired component so that later compilation can resolve the recovered placeholders back to their intended context.

A deliberate skip because every selected class already exists is a valid outcome. It differs from failing to find any usable declaration or filtering every candidate out unexpectedly. The report keeps those cases distinct.

## Lexical identity precedes body extraction

The class reader normalizes a UTF-8 BOM and line endings so lexical offsets and parser slices refer to the same text. It locates the first supported named declaration, distinguishing it from anonymous classes and `::class` constants. Namespace, declaration kind, inheritance, interfaces, documentation, imports, license material, and body are recovered through their corresponding paths.

Body extraction is checked against the located declaration. A body that cannot be matched to that declaration is not silently replaced with an empty body. An actually empty class and a failed extraction are different observations.

The reader can recognize syntax that the Power model does not represent completely. For example, the inspected stored type vocabulary does not preserve every modifier or declaration form. Selection and reporting must be interpreted against that vocabulary; lexical recognition alone is not a claim of lossless translation of arbitrary PHP. [X03](../reference/source-map.md#x03)

## Namespace and filesystem structure jointly inform placement

A class's declared namespace and the folders containing it often encode the same structure. The namespace resolver compares the relevant trailing segments and identifies the boundary between the retained vendor portion and the dotted stored path representation used by Powers.

A dotted library folder can explicitly identify its own namespace head. Otherwise, the namespace/path correspondence supplies the boundary, with a conventional fallback where a reliable path correspondence is unavailable.

The conceptual operation is

$$
\operatorname{placement}(n,p,c)=
(\text{stored namespace},\text{source role},\text{context bindings}),
$$

where $n$ is the declared namespace, $p$ the physical path information, and $c$ the class name. The three inputs constrain the answer. A short class name alone cannot determine its correct identity or owner.

## Concrete names become contextual again

Compilation specializes placeholder names into a particular application. Recovery reverses supported occurrences of those names into the stored placeholder representation. The namespace resolver records the concrete vendor and recognized component segments whose values must later be supplied by the paired component.

The class assembler also reverses supported language constants into their source text before storing code. Otherwise, a later compiler pass could generate a new language key from an already generated key. This is a concrete example of recovering the right *representation*, not merely preserving the visible output string.

The operation is bounded by the recognized naming and language conventions. It is not an arbitrary semantic renaming of every string that happens to resemble a component name.

## Imports and relationships use qualified identities

Class, function, and constant imports occupy different symbol namespaces. The assembler interprets the supported class imports, inherited types, and implemented interfaces using the declaration's namespace and existing aliases. It connects known identities to Power selections and preserves unresolved source relationships through the applicable code representation.

Existing Power matching uses qualified namespace information and the stored forms established by the resolver. Candidate selection and pairing remain separate from the textual similarity of two bodies. Reusing a class from another component merely because its short name is the same would not be a sound identity rule.

The [pairing chapter](pairing.md) explains the selected-component context and explicit decisions. This edition records the implemented matching rules rather than treating every candidate suggestion as an infallible ownership proof.

## Recover, then use the ordinary compiler

Once written, a recovered Power is processed by the existing loader and injector. Its relationships can trigger dependency acquisition; its placeholders receive the destination context; its namespace and file-local aliases are resolved; its source is placed according to its role.

The reverse path is valuable because it reconnects existing code to those reusable mechanisms. It can preserve authored implementation while recovering enough structure for managed reuse and regeneration, rather than forcing a developer to re-enter every class manually.

For another language, the equivalent operation would parse supported module/type declarations, retain authored bodies, recover imports and ownership, map physical placement to the module system, and persist the result as reusable compiler input. The details of PHP syntax are replaceable; the identity and representation boundaries are not.
