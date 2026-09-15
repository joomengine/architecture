---
title: Dependency traversal and bounded discovery
description: Relationship direction, embedded references, nested subforms, assets, and the queues that complete a requested blueprint graph.
section: Blueprint Exchange
order: 22
evidence: Dependency resolver, dependency traits, and package builder traversal
---
# Dependency traversal and bounded discovery

Selecting a component does not identify all of its required information immediately. Its configuration points to relationship records. Those records identify views, fields, modules, or plugins. Code and markup can introduce additional references to reusable definitions. The package machinery discovers this graph as it processes its vertices.

JCB's dependency resolver extracts several classes of relation in one operation: outgoing entity references, incoming owned children, references in supported dynamic content, nested subform fields, validation rules, files, and folders. Each class has its own interpretation. [B03](../reference/source-map.md#b03)

## Direction records the relationship's role

An outgoing dependency says that the current entity refers to another definition. A field refers to a field type; a view association refers to a field. An incoming dependency identifies a child record by its parent relationship: a component has a `component_admin_views` record, and an admin view has an `admin_fields` record.

Both directions must be traversed to transport the relevant design. They are not equivalent for every operation. In particular, resetting a parent can require refreshing its owned child configuration without overwriting every separately maintained reusable definition it references. [Import and reset](import.md)

Represent a dependency as

$$
e=(u_s,u_t,\delta,m),
$$

where $u_s$ and $u_t$ are typed source and target identities, $\delta$ records the relationship direction or role, and $m$ carries transport metadata. This is a labelled graph: retaining the edge label preserves decisions that an unlabelled set of GUIDs would discard.

## References can be embedded in structured fields and code

Many relationships are available from schema metadata. Others appear in supported code conventions: custom-code references, Power keys, placeholders, template aliases, layout aliases, or field definitions embedded in subforms. The resolver inspects the configured fields and extracts the references that those conventions represent.

This is not a claim to solve arbitrary program analysis. A supported literal reference is discoverable because its syntax and interpretation are known. An identifier computed by arbitrary runtime code may not be recoverable by a static reference scan. The compiler's template/layout mechanism likewise recognizes supported literal call forms and follows their nested content. [Templates and layouts](../generation/forms-layouts.md)

The important architectural choice is to route both explicit database relationships and recognized embedded references into the same typed dependency process. A consumer then receives an available local definition without needing a separate import procedure for every origin of the reference.

## Queue expansion separates discovery from dispatch

The dependency trait records requests in a tracker keyed by entity and identifying value. Entity dependencies and file/folder dependencies use different queues. The package builder selects a handler for each entity family, processes its current requests, and drains newly discovered work.

In the inspected implementation, a queued batch is removed before its recursive processing. This prevents the same pending batch from being re-entered as though it were new. Per-request attempt markers provide a second boundary around repeated acquisition. [B02](../reference/source-map.md#b02), [B03](../reference/source-map.md#b03)

A language-neutral description is:

```text
pending := normalized root requests
attempted := empty
while pending contains an entity batch:
    batch := remove one batch from pending
    for request in batch:
        if request not in attempted:
            attempted.add(request)
            result := selected_handler.acquire(request)
            record result
            pending.add(result.discovered_entity_requests)
transport the accumulated file and folder requests
```

The source uses nested service calls and tracker drains rather than requiring this exact loop. The pseudocode makes the traversal obligation visible.

## Cycles do not require repeated acquisition forever

A definition graph can contain shared references and cycles. If requests have stable identities, each newly processed request marks progress. With a finite reachable request universe and handlers that themselves complete, guarded traversal performs only finitely many distinct acquisition attempts.

The bound applies to attempts, not to successful resolution. A missing record, a failed payload, or a persistence error can leave an unresolved request. Completion of traversal and completeness of the resulting graph must therefore be recorded separately. [Formal resolution](../formal/resolution.md)

Similarly, a flag set before recursion is a cycle guard, not evidence that the corresponding record is fully loaded. This distinction also appears in Power loading, where the loader can mark an item while recursively acquiring its related definitions. [Powers](../compiler/powers.md)

## Completeness is relative to the dependency contract

Let $R_0$ be selected roots and $\operatorname{deps}(u)$ the dependencies declared or discovered by the supported resolver. The reachable set is the least set satisfying

$$
R_0\subseteq R^*,\qquad
u\in R^*\Longrightarrow\operatorname{deps}(u)\subseteq R^*.
$$

This expression explains the target of dependency traversal. It does not assert that the whole compiler is a least-fixed-point rule engine, or that undeclared external behaviour has been discovered. The resolver's schema and recognized conventions define the relation being closed.

Once those requests are available locally, compilation still has to interpret their contextual uses and generate their consequences. Dependency completion makes information available; it does not replace semantic classification, deferred work, or output binding.
