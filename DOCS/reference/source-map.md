---
title: Implementation and evidence source map
description: Pinned compiler paths, inspected responsibilities, integrated extrusion fingerprints, and public blueprint/product sources.
section: Reference
order: 90
evidence: Source catalogue and responsibility-level inspection ledger
---
# Implementation and evidence source map

The core implementation references use the official **Joomla Component Builder** repository at commit **`bca4a1520484f3e2c2fbd12964a5995b0d058de1`**. Paths below beginning `Compiler/`, `Package/`, or `Remote/` are relative to `libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/`, unless stated otherwise. Each entry identifies the responsibility examined, not an assertion that every method in that directory implements the same guarantee.

The integrated extrusion capture is recorded separately under X01–X04. It contains implemented operations included in this architectural edition but is not attributed to the older core pin. The [edition record](edition.md) explains this boundary. All public compiler links use the official project.

## C01

**Entry, timing, initialization, and final orchestration.** [Compiler.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler.php) contains the constructor, `run()`, final custom-code placement, repository output, and archive sequence. [Initializer.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Initializer.php) establishes the once-only initialization sequence, code recovery before reset, component loading, version handling, and structures. Include inherited Infusion work when tracing the constructor.

## C02

**Shared services, configuration, and extension boundaries.** [Compiler/Factory.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Factory.php), `Compiler/Config.php`, and the [compiler service providers](https://github.com/joomengine/Joomla-Component-Builder/tree/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Service) connect shared stores and selected collaborators. Event interfaces and calls in the consuming paths establish where handlers can affect state. Service lifetime and construction are part of execution.

## C03

**Component acquisition and nested enrichment.** [Component/Data.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Component/Data.php), `Compiler/Component.php`, and `Compiler/Model/Adminviews.php` load the root, establish its registry, enrich configuration and code, and follow view occurrences into their referenced data. Examine the query and `energize()` sequence, not only the final returned object.

## C04

**Field definitions, names, and contextual code.** [Field/Data.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Field/Data.php) implements ID/GUID indexing, local acquisition, guarded remote retry, field-type enrichment, and use-site custom-code processing. The [Field services](https://github.com/joomengine/Joomla-Component-Builder/tree/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Field), including `Name`, `UniqueName`, `TypeName`, and `Customcode`, supply naming scope and per-view contribution guards. Cached data can be processed and mutated; it is not represented as a universally pure GUID lookup.

## C05

**Semantic classification.** [Creator/Builders.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Creator/Builders.php) is the central field-contribution trace: schema and keys, list membership, relations, titles and aliases, storage treatment, search, sorting, filters, layouts, languages, and component-field metadata. Inspect the branch conditions and update operations of each contribution. The Greeting title-to-index rule is in the schema-building branch.

## C06

**Store operations and output environments.** [Abstraction/Registry.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Abstraction/Registry.php) supplies shared registry operations. [ContentOne.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Builder/ContentOne.php) models shared placeholder keys; [ContentMulti.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Builder/ContentMulti.php) partitions bindings by context. Specialised builders retain their own value and update meanings.

## C07

**Content preparation and deferred completion.** [Helper/Infusion.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Helper/Infusion.php) prepares content, interprets views, replays `secondRunAdmin` operations and argument arrays, and invokes the second configuration-fieldset pass. `Compiler/Creator/ConfigFieldsets.php` implements the selected fieldset work. The source has a prescribed replay point, not a generic least-fixed-point scheduler.

## C08

**Exact binding semantics.** [Placeholder.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Placeholder.php) defines ordinary ordered replacement, presence checking, original-input map filtering, active-placeholder updating, and marker construction. Action 3 filters map entries; it does not remove every unknown output token. The host replacement primitive is documented in [R12](bibliography.md#r12).

## C09

**Custom, GUI, external, and recovered code.** [Customcode.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Customcode.php) coordinates expansion and discovery. The [Customcode services](https://github.com/joomengine/Joomla-Component-Builder/tree/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Customcode) include `Dispenser`, `Gui`, `Extractor`, `External`, and `Reverse`. They establish preparation/retrieval, local editing addresses, static extraction, content-history acceptance, and supported reversal. Final fingerprint placement and `loadEscapedCode()` are in C01's compiler. A missing file and an unresolved location in an existing file have different diagnostic paths.

## C10

**Power acquisition, dependency processing, and injection.** [Power.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Power.php) and the [Power collaborators](https://github.com/joomengine/Joomla-Component-Builder/tree/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Power) handle GUID acquisition, recursive preparation, source placement, import aliases, and per-file injection. [JoomlaPower.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/JoomlaPower.php) selects target-sensitive platform mappings. Distinguish a processing guard from completed preparation and a definition's qualified name from a file-local alias.

## C11

**Nested template and layout acquisition.** [Templatelayout/Data.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Templatelayout/Data.php) recognizes supported literal load/render forms, resolves aliases, stores templates/layouts under their respective scopes, and follows nested content. Its recognized syntax defines the discovered dependency relation.

## C12

**Dynamic Get and alias/result structure.** [Dynamicget/Selection.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Dynamicget/Selection.php), `Compiler/Dynamicget/Data.php`, and `Compiler/Model/Dynamicget.php` prepare sources, selections, aliases, joins, filters, and method-specific mappings. Query execution remains a runtime operation in the generated application.

## C13

**History and update contributions.** [Model/Updatesql.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Model/Updatesql.php), `Historycomponent.php`, `Historyadminview.php`, and `Sql.php` in the same model directory process supported old/new relationships and properties. They contribute migration information; compiling that information is not the later execution of an installation migration.

## C14

**Permission declarations and consumers.** [Creator/Permission.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Creator/Permission.php) prepares action mappings. [Helper/Interpretation.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Helper/Interpretation.php) contains the generated form treatment, field options, strict result processing, and permission-sensitive JSON save path. Inspect the respective branches around lines 4,030, 15,436–15,700, and 16,808 onward. Their conditions differ; a hidden input is not equivalent to removing data from every runtime result.

## C15

**Language collection and output.** [Language.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Language.php) and [Language services](https://github.com/joomengine/Joomla-Component-Builder/tree/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Language) implement keyed collection, extraction, source/translation maintenance, association updates, inclusion thresholds, and messages. `Set`, `Update`, `Translation`, `Insert`, `Purge`, and `Multilingual` have separate responsibilities.

## C16

**Router modeling and emission.** [Model/Router.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Model/Router.php) prepares view/key/alias data. [Creator/Router.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Creator/Router.php) selects default, configured, or authored work; `RouterConstructorDefault`, `RouterMethodsDefault`, and their manual counterparts implement those selected paths.

## C17

**Module content.** [Joomlamodule/JoomlaSix/Infusion.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Joomlamodule/JoomlaSix/Infusion.php) establishes module context and prepares provider, dispatcher, Dynamic Get, helper, default template, installer, fieldset, and manifest content. Data and structure services and the architecture provider supply the corresponding acquisition and target responsibilities.

## C18

**Plugin content.** [Joomlaplugin/JoomlaSix/Infusion.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Joomlaplugin/JoomlaSix/Infusion.php) establishes plugin naming and language context and prepares extension, provider, installer, fieldset, and manifest material. Plugin group, base-class, method, and property definitions participate through their data paths.

## C19

**File inventory and ordered updating.** [Extension/Files/Updater.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Extension/Files/Updater.php), `Extension/Files/Dynamic.php`, and [Extension/FileContent.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Extension/FileContent.php) establish file-family order, context selection, shared-before-context binding, later code processing, injection, writing, and autoloader completion.

## C20

**Packaging and configured publication.** C01's `Compiler.php` contains the final language/update/README/repository operations and component, module, and plugin archive paths. Structure and utility collaborators manage the associated file trees. These are operation-specific outcomes, not an asserted distributed transaction.

## C21

**Target dispatch.** [Service/ArchitectureModule.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Service/ArchitectureModule.php) provides a concrete target-selection example. The same directory contains `ArchitectureController`, `ArchitectureView`, `ArchitectureComponent`, `ArchitecturePlugin`, `ArchitectureDashboard`, and `ArchitectureModel`. Inspect target configuration before service resolution and the lifetime of cached selection.

## C22

**Generated design metadata.** C05's `Creator/Builders.php` assembles the component-field map. The [Hello World Table class](https://github.com/vast-development-method/hello-world-joomla-component/blob/a81c0dd8b8f41905671a86796a3e5995685fdaba/libraries/jcb_powers/JCB.Joomla/src/Helloworld/Table.php#L73-L96) shows the emitted Greeting GUID, type, roles, tab, and database properties.

## C23

**Historical implementation.** [Root commit](https://github.com/joomengine/Joomla-Component-Builder/commit/ecf47809f960bd057af8a414168fada6fe22c5f7), 30 January 2016 at 20:28:43 UTC, and its [admin/helpers/compiler.php](https://github.com/joomengine/Joomla-Component-Builder/blob/ecf47809f960bd057af8a414168fada6fe22c5f7/admin/helpers/compiler.php). The early source already contains specialised builders, static/dynamic content stores, acquisition, structure construction, and later file updates. Later features and this manuscript are not backdated to that commit.

## C24

**API and AJAX generation.** The [Joomla 4 compiler templates](https://github.com/joomengine/Joomla-Component-Builder/tree/bca4a1520484f3e2c2fbd12964a5995b0d058de1/admin/compiler/joomla_4) include API controller and JSON-view material. C07's Infusion establishes the API bindings; [Model/Ajaxadmin.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Model/Ajaxadmin.php) prepares selected AJAX input and method contributions, flags, and tokens. Entry registration and runtime authorization must be read in their respective generated integration paths.

## B01

**Entity catalogue and transport schema.** [Componentbuilder/Factory.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Factory.php) records the canonical entity map. [Package entity configurations](https://github.com/joomengine/Joomla-Component-Builder/tree/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Package) declare identifying fields, child relationships, indexes, payload paths, projection/encoding, and ignored local properties. `Package/Field/Remote/Config.php` and `Package/AdminView/Remote/Config.php` are representative cases. Distribution-channel flags are not interchangeable with every handler's retrieval eligibility.

## B02

**Graph acquisition and publication dispatch.** [Package/Builder/Get.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Package/Builder/Get.php) and [Set.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Package/Builder/Set.php) select handlers, drain entity batches, distinguish reset policy, process files/folders, and aggregate results. Empty queues and successful persistence remain different observations.

## B03

**Dependency extraction and tracking.** [Package/Dependency/Resolver.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Package/Dependency/Resolver.php), `Package/Dependency/Tracker.php`, and `Remote/SetDependenciesTrait.php` handle outgoing references, incoming children, recognized dynamic content, nested fields/rules, and asset queues. Edge direction affects subsequent operation policy.

## B04

**Repository selection.** [Abstraction/Grep.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Abstraction/Grep.php), `Componentbuilder/Remote/Grep.php`, and `Componentbuilder/Package/Grep.php` establish configured-source traversal, index caching, item matching, and payload location. Trace selection and fetching separately when determining fallback behavior.

## B05

**Portable export and remote updates.** [Abstraction/Remote/Set.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Abstraction/Remote/Set.php) and [Componentbuilder/Remote/Set.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Remote/Set.php) prepare payloads, dependencies, item descriptions, index updates, and eligible per-repository writes. Their normalization and unchanged-content checks differ from raw database-row comparison.

## B06

**Remote initialization and local persistence.** [Componentbuilder/Remote/Get.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Remote/Get.php) coordinates local-preservation and retrieval behavior. [Data/Item.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Data/Item.php) supplies table-aware item persistence. Examine the return values of individual operations before assigning a stronger meaning to aggregate result buckets.

## B07

**File and folder transport.** [Package/Remote services](https://github.com/joomengine/Joomla-Component-Builder/tree/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Package/Remote) include `GetContent`, `GetFile`, `GetFolder`, `SetContent`, `SetFile`, and `SetFolder`. They normalize resource identities, locate repository content, interpret target destinations, and retain the distinction between ordinary and forced acquisition.

## B08

**Repository definitions.** [Repository/Remote/Config.php](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Repository/Remote/Config.php), the repository services, and E06's repository-index snapshot describe managed source configuration. Read/write branches and channels are inputs to discovery and publication, not properties inferred from an entity's short name.

## X01

**Integrated component extrusion.** The captured implementation under `Componentbuilder/Extrusion/` includes `Extruder.php`, `Config.php`, discovery/layout adapters, typed registries, resolvers, and writers. `harvest`, `candidates`, and the writing operation separate observation, pairing, and persistence. The capture is identified by file SHA-256, independently of any moving branch:

| File | SHA-256 |
| --- | --- |
| `Extruder.php` | `9f7bc95ba0d3912b40cbb0f14a689371523c46c26dc1c14e5a8513277521e1c6` |
| `Config.php` | `7aef639bbb031d7f8e487b0b78acbfa59169c806472462657c6c7bba38246476` |

These are implemented edition-scoped operations, not paths asserted to exist at the older core compiler pin. Release availability is determined by the [official project](https://github.com/joomengine/Joomla-Component-Builder).

## X02

**Static readers and property precedence.** Under the same capture, reader services examine schema, form, language, manifest, table metadata, and view artifacts. `Resolver/Precedence.php` selects each usable property's value and origin by configured rank and stable default tier order. Its SHA-256 is `81665ea7c80df6506ad5fe1699c9e1348bdb4c35f293c748455326d2d752ac6b`. Zero and false are admitted values; null and empty string are omitted. The reader grammars define recovery coverage.

## X03

**Class recovery and reusable Power assembly.** Capture paths and SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `Powers/Extruder.php` | `3d572f1ffb82b1ed7badab938ef5cffa1a2333ab7d855c2ad1ce030f3aa3c44c` |
| `Powers/Reader/ClassFile.php` | `4a59011afdbae2d29b95341e10716170f65099cc360b9d7c7c9eee73552e2635` |
| `Powers/Resolver/Namespacer.php` | `4e78fe939ebdeb66fd4a9e66b5d168446325275abf65d20b6682ce9238771e06` |
| `Powers/Assembler.php` | `bffa8682f55257f03b41e0caac15ad152c6a269350ad35ebcdf4acc2e64aa879` |

The trace covers declaration location, body extraction, namespace/path interpretation, supported placeholder/language reversal, relationship assembly, and selected writes. Lexical recognition is distinguished from the declaration forms fully represented by the destination model.

## X04

**Pairing and write order.** `Resolver/Pairing.php` (SHA-256 `0dc7f59d0c1d85b4840ec07e116498ad2a7ac528e0c30565e8049605e8610e3d`), `Resolver/Candidates.php`, `Resolver/Sharing.php`, `Resolver/Reuse.php`, and `Writer/Dispatcher.php` (SHA-256 `d0de812634c16ad2a14805f5148a43806cbb5fae339214cc50bba5b39258cd84`) retain explicit verdicts, identity selection, shared-field decisions, and the dependency-compatible writer sequence. Each write and diagnostic has its own outcome.

## E01

**Hello World blueprint.** [Snapshot](https://github.com/vast-development-method/hello-world-blueprint/tree/5802e7c1d9bfaac005c765ccda830a7d07cd7e12). Entity payloads under `src/`, child records, `@dependencies`, indexes, README descriptions, and assets support the [worked lifecycle](../examples/hello-world.md). The accompanying [accounting](../examples/accounting.md) publishes separate categories.

## E02

**Hello World component product.** [Snapshot](https://github.com/vast-development-method/hello-world-joomla-component/tree/a81c0dd8b8f41905671a86796a3e5995685fdaba). Forms, SQL, list/view/model code, language entries, Table metadata, installer, and GUI-code markers support the field and custom-code traces.

## E03

**Site Redirect module product.** [Snapshot](https://github.com/vast-development-method/hello-world-joomla-module/tree/20be318a6163e253c2a9803434622467d6006709). Dispatcher, provider, template, manifest, language, and installer material demonstrate a distinct extension context.

## E04

**Hello World Privacy plugin product.** [Snapshot](https://github.com/vast-development-method/hello-world-joomla-plugin/tree/6a785145ee84212fec65a53b7c6c362ab0f8b408). The plugin class and manifest show the component-sensitive name resolved from its reusable definition.

## E05

**Service Directory family.** [Blueprint collection](https://github.com/joomengine/joomla-packages/tree/5e8733cb82c4467cf5e0a39c05a0133b457fec80) and [generated application](https://github.com/joomengine/Joomla-Service-Directory/tree/0ac9788cb9239ed2801ba19c7e2393c70e03f9c4). The two root versions and the product snapshot are treated as related artifacts, not silently asserted to be a byte-matched build certificate. The application author is Lemuel van der Merwe. [Larger example](../examples/service-directory.md)

## E06

**Reusable distribution channels.** The inspected snapshots are [packages](https://github.com/joomengine/packages/tree/7a26dac49093c4b9a79c793e65736efbd25f0005), [Super Powers](https://github.com/joomengine/super-powers/tree/adf335173201edeaf95f0ef6c3dc1bcabd23f3bc), [Joomla Powers](https://github.com/joomengine/joomla-powers/tree/e38ad0600bdd82513021ec7e5b2b9eecfe7f2f0b), [field types](https://github.com/joomengine/joomla-fieldtypes/tree/3be64d59378b5650825b97b44dbd58f2cdb82fcb), [snippets](https://github.com/joomengine/snippets/tree/a7f536be6ea7a8af5bdf86d81c9f7f547b862365), and [repository definitions](https://github.com/joomengine/repoindex/tree/9634461fd06cdb8235bac841e557410aac18817f). Their schemas and handlers have different responsibilities; their item counts are not interchangeable product counts.

## E07

**JCB's generated application and maintained build record.** The [official README](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/README.md) identifies the application as created with JCB. The author's development record describes its generated application layers, supplied reusable library inputs, and repeated self-build timing. C01 establishes the inspected timer boundary; the repository inventory establishes the separately counted source snapshot. [Performance](../engineering/performance.md), [self-generation](../engineering/regeneration.md).

## D01

**Operational documentation.** [JCB documentation snapshot](https://github.com/joomengine/jcb-documentation/tree/ecd3670232d344295fc4f673b2d3dc40a64b3bf6). The English documentation covers authoring, fields and relationships, custom code, Dynamic Gets, Powers, compilation, and maintenance. Its operational explanations informed the source investigation; implementation claims are connected to the corresponding compiler paths above.

## Using the ledger

A stronger claim should follow a listed operation into its collaborators, record the relevant branch conditions, and compare its actual consumer and output. A shared service name alone does not prove scope correctness. A generated comment alone does not prove a unique origin. A source fingerprint fixes a capture but is not a substitute for a fresh runtime build.

The [verification guide](../engineering/verification.md) explains how the source, artifact, executable, mathematical, and runtime checks fit together.
