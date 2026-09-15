---
title: Powers, namespaces, and code placement
description: Stable reusable code identity, local and remote acquisition, recursive dependencies, import aliases, target mappings, and generated source placement.
section: Compiler
order: 37
evidence: Power loaders, extractors, injectors, structure builders, and Joomla Power mappings
---
# Powers, namespaces, and code placement

A Power is a managed reusable code definition. Its stable identifier allows application code and other definitions to refer to it without fixing every physical namespace, import alias, and destination at the point of reference. The compiler resolves the definition, interprets its dependencies and context, and places the resulting code where the generated application needs it.

The mechanism joins repository distribution to compilation. Acquiring a Power supplies local editable knowledge; compiling it resolves how that knowledge participates in a particular product. [C10](../reference/source-map.md#c10)

## Acquisition and recursive preparation

The Power loader checks its active and processing state, attempts to load the GUID-addressed definition from local data, and can invoke repository retrieval when that definition is missing. A successful acquisition permits a guarded retry after local persistence.

Preparation processes namespace information, inheritance and interface relationships, imports, load selections, headers, main code, and relevant packaging or reusable-library metadata. References can lead to other Powers. A processing marker is established around recursive work so that a cycle does not simply re-enter the same definition forever.

The state distinction is essential: an item being processed and an item whose preparation has completed are different states. The [resolution model](../formal/resolution.md) expresses this without pretending that a single Boolean proves all dependencies are ready.

## Reference identity is separated from the final symbol

A Power key embedded in a code fragment identifies a reusable definition. During injection, the compiler scans for those keys, resolves the corresponding definitions, examines the file's existing import statements and trait uses, and constructs a per-file replacement map.

The resulting local symbol can reuse an existing alias or receive a distinct name where another import already occupies the desired short name. The injector then adds required import statements and replaces the Power keys. Its per-file maps are reset for each file, because import naming is a file-level context. [C10](../reference/source-map.md#c10)

Formally, let $u$ identify a Power and $F$ the destination file context:

$$
\operatorname{resolveSymbol}(u,F)=
(\text{qualified name},\text{local name},\text{required import}).
$$

The qualified name and local alias need not be equal. Retaining that distinction allows two classes with the same final short name to participate in one file through explicit aliases.

## Namespaces also determine physical placement

The Power's namespace and placement settings are processed into output paths. Structure building creates the required directories, skeleton source files, and supporting material, records those files for later content updates, and avoids rebuilding already handled Powers.

Some Powers live in reusable library locations. Source-oriented placement can target the extension's own source namespace, supplying an additional class or a deliberate replacement for a generated class. The official documentation describes the relationship between component, module, or plugin namespace roots and their generated source trees. [C10](../reference/source-map.md#c10), [D01](../reference/source-map.md#d01)

A complete-class replacement is a different ownership choice from a small marked method insertion. When a definition supplies the whole class, the author controls that class's implementation. Future changes to the default emitter do not automatically rewrite the replacement's internal logic. This is a consequence of the selected extension mechanism, not a contradiction of regeneration.

## Joomla Powers resolve target-platform references

Joomla Powers represent references to Joomla classes and their version-sensitive namespace/type mappings. The loader selects a mapping for the compile target, with the configured default where applicable. The identifier can therefore remain stable while the generated import follows the target's class arrangement.

This separates three things: the application's intent to use a particular platform capability, the class mapping for the selected Joomla generation, and the local name used in a particular emitted file. [Target selection](targets.md)

The mapping data is itself distributed in the public `joomengine/joomla-powers` repository. Reusable code definitions and platform-reference mappings are related distribution concepts, but their payloads and generation responsibilities differ. [E06](../reference/source-map.md#e06)

## Dependencies can be discovered late

Custom-code expansion and final file processing can expose Power keys after earlier model acquisition. The file updater and associated Power services perform the additional preparation and output work needed by those discoveries.

The important invariant is consumer readiness: the final symbol and required supporting code must be resolved for the output that uses them. The architecture does not require every possible Power to be loaded before the first skeleton file exists.

This is why the compiler's acquisition and materialization boundaries overlap in time. It can preserve early reusable work and still respond to dependencies revealed by later interpretation. [Execution](execution.md), [Binding](binding.md)

## Managed reuse is more than copying source

The combined operation includes stable identity, repository selection, local persistence, editable definitions, recursive relationships, namespace resolution, import collision handling, source placement, and output registration. Copying a source file provides only one part of that process.

A language-neutral implementation can use another module system, linker model, or package representation. It needs an equivalent separation between definition identity, target-qualified implementation, file-local symbol selection, and physical inclusion. The [implementation guide](../engineering/implementation.md) uses those roles rather than requiring another language to imitate PHP namespaces literally.

The public Power and Joomla Power repositories supply inspectable instances of this managed-reuse model, while the official compiler shows how the definitions become part of generated applications.
