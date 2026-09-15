---
title: Reading artifacts and resolving their meaning
description: Static artifact readers, property-level provenance, configurable precedence, field recovery, and presentation classification.
section: Extrusion
order: 51
evidence: Discovery, readers, schema/form registries, and precedence resolver
---
# Reading artifacts and resolving their meaning

Extrusion separates locating an artifact from accepting a particular interpretation of it. Discovery identifies possible manifests, schemas, table metadata, forms, language files, and views. Typed readers extract the facts those artifacts actually represent. Resolvers then combine those facts into candidate model properties.

This structure prevents a familiar reverse-engineering mistake: treating the first plausible value found in a file as authoritative for every purpose. [X02](../reference/source-map.md#x02)

## Readers do not run the inspected application

The source readers inspect text and represented syntax. Schema readers split and interpret supported SQL statements; the table reader obtains supported literal metadata; form readers parse XML; language readers parse catalogues; presentation readers retain and classify the supported template content. The Power reader uses lexical and parser services to recover declared type structure.

The recovery operation is therefore not an application execution trace. It does not run an arbitrary installer or evaluate class bodies to discover what they might do. Dynamic values that cannot be recovered from the supported representation remain outside that reader's result.

This boundary is useful in another implementation language: each reader has a defined accepted grammar and produces facts with source locations or origins. The resolver consumes those facts independently of the reader's physical syntax.

## Property precedence is finer than whole-file precedence

The inspected default order is **table metadata, SQL notes, form XML, derived schema information**. It is configurable. A field can take its datatype from one source and its label or presentation attribute from another, because selection happens property by property.

For property $p$, let its usable candidates be

$$
C_p=\{(v_i,t_i)\mid v_i\text{ is supplied by tier }t_i\}.
$$

The resolver selects the candidate with the smallest configured rank. Equal ranks are resolved by the fixed default tier order. A value is not usable when it is `null` or the empty string; numeric zero and Boolean false remain legitimate values.

$$
\operatorname{selected}(p)
=\mathop{\operatorname{argmin}}_{(v,t)\in C_p}
\bigl(\operatorname{rank}(t),\operatorname{defaultRank}(t)\bigr).
$$

The resolved record retains both the chosen value and its origin. A portable implementation should preserve that pair: a value without its origin no longer explains why it prevailed. [X02](../reference/source-map.md#x02)

## Similar-looking properties can have different meanings

A database default and a form default are not automatically the same property. The resolver records database-default information separately where schema and table metadata state it. Similarly, database width and maximum input length can be distinct, as the Greeting example demonstrates.

SQL column comments can carry supported scalar configuration in JSON. XML can carry a field type, label, options, validation, conditions, and other attributes. Language resolution can turn a represented constant into its text. Derived schema interpretation supplies a lower-priority answer where a stronger source has not stated one.

The result is not “pick one file and copy it.” It is a property-level assembly governed by explicit precedence and meaning.

## Generated boilerplate is not another authored field

JCB generates standard fields and view structures from its own rules. The extrusion configuration identifies the standard columns and template names that should not be duplicated as ordinary authored definitions. The GUID field is deliberately treated differently from the standard skipped-column list because it can be a modeled field with a recoverable identity.

Likewise, repeated files such as a generated list body's default template do not necessarily represent separate reusable templates with the same global name. Recovery needs the artifact's role and containing view, not only its basename. [X02](../reference/source-map.md#x02)

This distinction keeps the recovered model compact. Reconstructing every mechanically generated fragment as independently authored code would preserve bytes at the cost of losing the architecture that made regeneration useful.

## View scope influences classification

Administrator and site views can have similarly named files. Explicit roots and discovered layout context distinguish them. The reader first establishes the screen identified by its main template or class, then associates subordinate presentation material with that screen and role.

A view's presence is directly observable from its layout and artifacts. Its complete original configuration is not automatically recoverable from the fact that a class exists. The resolver uses available schema, form, metadata, and naming information to establish the supported model, while retaining code where the selected recovery path supports it.

The resulting candidate may be an admin view, custom-admin view, site view, template, layout, or related query definition. Those roles determine which writer and subsequent compiler consumer will handle it.

## Resolution produces a reviewable intermediate model

The assembled candidate retains its name, type, selected properties, source context, proposed identity, and applicable relationships. Field conditions and relations are connected after identities are established. Sharing resolution can consolidate repeated descriptions of the same field before candidates are presented.

The next stage therefore reviews semantic candidates, not a raw directory listing. The developer can see the model that would enter JCB and decide how it should relate to existing definitions. [Pairing](pairing.md)

This is the reverse-side counterpart of contextual compilation: readers distribute observed facts into typed stores; resolvers establish meaning; later consumers use the retained decisions. Forward and reverse flows share architectural principles without being falsely described as exact inverses for every possible program.
