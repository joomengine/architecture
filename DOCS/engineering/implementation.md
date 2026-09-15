---
title: Implementing the architecture in another technology
description: A language-neutral decomposition of model authoring, typed discovery, contextual compilation, artifact generation, transport, and reconstruction.
section: Engineering
order: 80
evidence: Implementation guidance derived from the documented architecture
---
# Implementing the architecture in another technology

The architecture can be implemented without reproducing JCB's PHP classes or Joomla-specific emitters. Its reusable structure is the separation of design identity, contextual use, retained contributions, deferred operations, target knowledge, and materialized products.

A practical implementation begins with a small complete vertical slice. Define one entity and its associations, acquire it by stable identity, derive several coordinated outputs, export and import it, and demonstrate that the same represented intent reaches each output correctly. The Greeting example supplies a concrete template for that exercise. [Field trace](../examples/field-trace.md)

## Define the authoring model before the interface

Specify typed entity schemas, portable identifying fields, ordered associations, supported embedded references, assets, and custom-code roles. Then let a GUI, API, command-line tool, or repository file produce the same normalized representation.

The interface should express design choices rather than expose an unexplained collection of output filenames. A searchable field, for example, is a model decision whose query and interface consequences belong to generation rules.

Keep reusable definitions separate from their occurrences. The occurrence supplies role, placement, and context; it should not require copying and modifying a globally shared definition merely to change one use.

## Give resolution an explicit contract

A resolver needs a typed request, a local lookup policy, ordered configured sources, a payload mapper, persistence, dependency extraction, and request-state tracking. Initialization and reset should be different operations where local authoring is supported.

```text
acquire(request, mode, context):
    normalize request identity
    consult operation attempt state
    apply local-preservation policy for mode
    select source through the configured index contract
    retrieve and validate the represented payload
    map it into local design data
    record persistence outcome and discovered dependencies
    dispatch dependencies according to their relationship roles
    report unresolved requests and asset outcomes
```

Do not let the queue's emptiness stand in for graph validity. Attempted, resolved, and failed requests have distinct meanings. [Resolution](../formal/resolution.md)

## Make contribution types explicit

An interpreter receives a definition and occurrence context and returns contributions. Each contribution specifies its destination, address, update operation, and value. Schema records, query aliases, ordered layout members, code fragments, requirement flags, and deferred tasks should retain their different types.

A typed map, record collection, or graph store can replace a PHP registry. The important property is that producers and consumers agree on the value's meaning and scope. A generic key/value service alone does not define that contract.

Represent names once they have been resolved within their scope. Downstream emitters should consume that decision rather than independently choose suffixes or aliases. This keeps forms, data paths, imports, and metadata aligned.

## Separate reusable preparation from contextual completion

A code dispenser can retain prepared fragments indexed by role and occurrence. Retrieval supplies the current binding environment and optional surrounding syntax. A definition cache can retain acquired source data while a per-view guard controls an effect such as script inclusion.

Those mechanisms must not share a key merely because both retain text. Define the dependency projection for each reusable result and the application scope for each effect. [Contribution model](../formal/classification.md)

Deferred work can be a stored operation and arguments with a designated later phase. A dependency-task representation is another option, provided it preserves the same prerequisites and ordering. Do not introduce an unspecified repeat-until-stable loop where a finite sequence of selected completion stages is sufficient.

## Keep target knowledge behind responsibilities

Define logical emitter responsibilities such as schema, item model, list model, form, controller, module entry, plugin entry, manifest, and installation update. Select their concrete implementation through an explicit target context.

A Python implementation might return structured syntax trees or text fragments; a JVM implementation might transform models; another system might use typed intermediate code. The representation can differ while the responsibilities remain comparable.

Separate the host executing the generator from the platform targeted by its output. Establish target selection before resolving cached target-specific services.

## Materialize through an explicit stage plan

An artifact needs a destination, role, context, and ordered transformations. Skeleton creation, shared binding, use-site binding, custom expansion, dependency injection, validation, and packaging are distinct operations.

The selected substitution semantics must be specified. Reproducing JCB's ordered replacement requires preserving map order and the original-input filtering rule where used. Replacing it with simultaneous substitution is a deliberate semantic change, not an implementation-neutral optimization. [Staging](../formal/staging.md)

Track artifacts and diagnostics separately. A completed optional publication step, a generated source file, a recoverable code-placement warning, and a successfully created archive answer different questions.

## Add transport and reconstruction at their actual boundaries

Blueprint export projects portable design information and serializes its dependency graph. Import restores that graph under explicit existing-item policies. Installed-artifact extrusion uses readers, precedence, identity resolution, reviewable candidates, and ordered writers. Marked-code recovery uses designated region identities and placement context.

These operations can share identity services and representations without being called the same inverse transformation. Preserve the domain and equivalence appropriate to each. [Transport](../formal/transport.md)

## Test a complete represented decision

For the first vertical slice, test that a field's resolved name appears consistently in schema, form, query, and metadata; that its context changes only the intended outputs; that export/import preserves its portable identity; and that a missing dependency produces a specific diagnostic.

Then add shared definitions, cyclic dependency references, deferred operations, custom-code binding, alternate targets, and explicit recovery cases. The [reference mechanisms](reference-model.md) demonstrate several of those contracts at small scale.

The purpose is to reproduce the architectural relationships, not to start by recreating JCB's complete feature catalogue. A small correct implementation of the full lifecycle gives subsequent emitters and entity types a stable foundation.
