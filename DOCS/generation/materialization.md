---
title: Materialization, packaging, and repository output
description: Skeletons, file inventories, ordered content updates, late dependency completion, archives, and publication effects.
section: Generation
order: 47
evidence: Structure utilities, file inventories, extension updater, FileContent, and final compiler orchestration
---
# Materialization, packaging, and repository output

Materialization turns prepared structure and content into physical artifacts. JCB can create skeleton files before every semantic contribution is complete, update those files through later stages, add reusable code and supporting assets, and finally construct installation archives and configured repository outputs.

The physical filesystem is therefore part of the build state. A file's existence is not equivalent to its semantic completion. [C19](../reference/source-map.md#c19), [C20](../reference/source-map.md#c20)

## Structure and content are related but distinct

Structure utilities select templates, create directories, copy or prepare skeletons, and record file details. The file inventory groups outputs by their processing role and context. Dynamic files are associated with the view or extension whose binding environment will complete them.

A conceptual artifact record is

$$
a=(\iota,p,r,\Gamma,S),
$$

where $\iota$ is its logical identity, $p$ its destination, $r$ its emitter role, $\Gamma$ its context, and $S$ its remaining stages. JCB represents these responsibilities through paths, file arrays, builder keys, and orchestrated service calls rather than necessarily allocating this exact record type.

The record explains why a destination path alone is not the whole artifact definition. Two files can use the same skeleton but different contexts; one file can receive several successive transformations.

## The updater follows an explicit family order

The inspected extension updater requires the relevant static and dynamic inventories, loads previously discovered Power requests, obtains BOM content, and processes static files, dynamic files, modules, plugins, and Powers. It then prepares autoloader material and performs the corresponding static-file autoloader update before removing the consumed dynamic inventory. [C19](../reference/source-map.md#c19)

The sequence reflects dependencies between file content and the reusable code discovered while processing it. Autoloader completion belongs after the relevant Power information has been established.

This is a concrete example of staged readiness reaching the filesystem. The compiler does not merely write every output once from an already final map.

## Per-file processing establishes its local environment

For a file, the content service sets the current filename binding, reads the staged content, handles the configured header/BOM convention, applies shared bindings, and then applies the selected contextual bindings. Conditional custom-code expansion, a pre-write event, and Power/Joomla Power injection follow before the final write in that path.

The binding order and action mode determine how introduced tokens are handled. The [binding chapter](../compiler/binding.md) gives exact examples rather than treating all replacement algorithms as equivalent.

Counters record generated work such as files, folders, Powers, and line occurrences according to their respective update points. Those internal counters should be interpreted using their measurement boundaries; a separately counted repository snapshot can have a different inventory after copying, packaging, or excluding metadata. [Build measurements](../engineering/performance.md)

## Additional files and folders are part of the model

Component, module, plugin, and library settings can name extra files, folders, or URL-sourced material. Their configured targets and paths participate in structure preparation and installation/package metadata. Reusable Power structures also add their own source and support files.

These supplied artifacts are part of the complete build input. They should be counted separately from blueprint payloads and from text synthesized by a particular emitter. This separation makes an expansion or size measurement reproducible without denying the compiler's assembly work.

## Packaging follows file preparation

The final compiler orchestration handles language output and messages, update XML destinations, generated README material, and configured local repository synchronization before constructing the component archive and then associated module and plugin archives.

Packaging is a deployment representation of the generated product. A blueprint repository transports editable design knowledge; an installation archive transports the runtime extension and its installation metadata. Both are outputs in the larger lifecycle, but they serve different consumers. [Lifecycle](../foundations/lifecycle.md)

The implementation's repository and server integrations are selected by configuration. The paper does not assume that every compilation publishes to a remote Git service or deploys an extension automatically.

## Failures have operation-specific consequences

A file read, write, dependency retrieval, content update, repository synchronization, or archive creation can fail at its own boundary. The compiler's return values and messages determine whether processing stops, continues, or records a recoverable result.

An archive produced at one stage does not prove that every optional publication integration completed. Likewise, a warning about recoverable custom-code placement carries different meaning from an unreadable required template. The formal model retains diagnostics alongside artifacts rather than flattening them into one undifferentiated output.

## Reproducibility has a declared comparison boundary

To compare two materialized builds byte for byte, the source definitions, target rules, reusable dependencies, active hooks, and output-affecting environment values must be controlled. Dates, local editing markers, path-dependent metadata, and archive metadata can otherwise differ while the application model remains equivalent.

The [transport model](../formal/transport.md) distinguishes design equivalence, normalized artifact equivalence, and byte equality. The distinction is useful when importing the same blueprint into another instance or comparing generated repositories.

The resulting architecture provides a clear path from retained semantic information to a deployable product: plan the required structures, prepare contextual content, complete the ordered stages, preserve diagnostics, and package the resulting artifact set.
