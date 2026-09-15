---
title: Identity across representations
description: Typed entity keys, local database identities, contextual occurrences, and artifact locations in the JCB lifecycle.
section: Foundations
order: 12
evidence: Entity map, blueprint records, compiler lookups, and GUI markers
---
# Identity across representations

Identity allows a definition to survive changes in storage, use, and physical location. It also determines what can safely be reused. JCB's lifecycle contains several identities, and the distinctions between them explain much of its behaviour.

## Portable entity identity

A portable request is represented as

$$
u=(t,k,v),
$$

where $t$ is an entity type, $k$ its identifying field, and $v$ the value of that field. Many entities use a GUID. Other supported entities use an alias or a relationship key. The custom-code example `readMEcontributors` is identified by its function name; it is not a GUID-shaped exception to be discarded. [B01](../reference/source-map.md#b01), [E01](../reference/source-map.md#e01)

The type matters. A field identifier, a view identifier, and a Power identifier are not interchangeable merely because their values have the same lexical form. The key field matters for the same reason: a numeric database primary key is not automatically a portable identifier.

Repository indexes map portable identities to payload locations. Payloads retain their entity references, and dependency descriptors specify the target type and identifying field. This permits a request to be resolved without embedding the destination installation's row number in every relationship.

## Local database identity

A local installation can assign a numeric primary key to a record whose portable identity remains unchanged. Denote the local realization in installation $i$ by

$$
\lambda_i(u)=\text{local record identity}.
$$

Two installations can have $\lambda_1(u)\ne\lambda_2(u)$ while referring to the same portable definition. Imported relationships must therefore be interpreted through their declared identity representation, not copied under the assumption that all local row numbers coincide.

JCB's field loader indexes acquired definitions by both ID and GUID. Its editor-linked code markers can also contain local table, property, and numeric-record information. Those markers are useful local addresses for recovery; they should not be mistaken for the enduring identity of the application design. [C04](../reference/source-map.md#c04), [C09](../reference/source-map.md#c09)

## Occurrence identity

A shared field may occur in more than one view. A view definition may be attached under different component settings. The occurrence is the use, not another independently authored definition.

Write

$$
o=(u,p,a),
$$

where $u$ identifies the definition, $p$ identifies its place in an association or expansion, and $a$ contains occurrence-specific settings. The context $\Gamma(o)$ supplies the surrounding extension, target, view, role, and other relevant values.

An implementation need not allocate a permanent occurrence object for every such tuple. JCB often carries these distinctions in association records, loop variables, view names, configuration, and store keys. The tuple makes the distinction explicit for analysis without claiming that the production code uses that exact data type.

## Artifact and region identity

A generated artifact has a role and a destination. A file path is often a convenient location but is not equivalent to the identity of the definition that contributed to it. One definition can affect several paths; several definitions can affect one path.

Designated editable regions add another address. GUI markers associate recovered code with a stored property. Hash-based custom-code records also retain contextual placement information. These are different mechanisms, and a filename alone is not enough to describe both. [Custom code](../compiler/custom-code.md)

## Consequence for reproducibility

A blueprint transfer can preserve the application description while installation-local row numbers differ. Generated editor markers, dates, and similar metadata can consequently differ even when application structure and behaviour are preserved. Byte equality is a stronger comparison that requires those output-affecting values to be fixed or normalized under a declared rule.

The [transport model](../formal/transport.md) makes that equivalence explicit. It does not weaken the purpose of portable blueprints; it identifies which identity must remain stable for their purpose to be achieved.
