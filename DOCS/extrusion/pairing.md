---
title: Pairing, sharing, and ordered writes
description: Matching recovered candidates to local definitions, retaining user decisions, consolidating shared fields, and writing dependent records in order.
section: Extrusion
order: 53
evidence: Candidates, Pairing, Sharing, Reuse, and writer dispatcher
---
# Pairing, sharing, and ordered writes

Recovered structure must be connected to the destination model. Creating a fresh copy of every field or class would lose reuse. Updating an unrelated existing definition would corrupt another project's intent. Pairing therefore operates on identities, candidate kinds, and the selected component's relationships, with explicit decisions available before writing.

JCB retains those decisions in a separate registry. Writers consume them when selecting the identity and action for each candidate. [X04](../reference/source-map.md#x04)

## A candidate is not yet a database write

The candidate catalogue groups recovered items by kind and relates them to definitions associated with the selected component. GUID matches and scoped name matches can suggest an existing target. A recovered item with no suitable match can propose creation.

The proposal contains more information than a short name: its kind, source key, recovered properties, context, and proposed target matter. Candidates for fields, views, code definitions, and relationships have different matching responsibilities.

The developer's choices are represented by `create`, `update`, and `ignore`. An update identifies its selected target. An ignore prevents that candidate from being written. A create can derive a distinct stable identity rather than accidentally reuse the identity already held by another definition.

## Decisions have precedence over automatic settlement

The pairing resolver validates the action and the target identity. Its automatic settlement path does not overwrite a verdict already recorded by the caller. Sharing and reuse therefore use the same decision channel as human approval rather than introducing a hidden second authority.

For candidate $q$ and verdict $v$, the selected identity is

$$
\iota(q,v)=
\begin{cases}
\bot, & v=\mathrm{ignore},\\
\operatorname{target}(v), & v=\mathrm{update},\\
\operatorname{derive}(\mathrm{kind}(q),\mathrm{forcedNew},\iota_0(q)), & v=\mathrm{create},\\
\iota_0(q), & \text{no explicit verdict}.
\end{cases}
$$

Here $\bot$ means no write for that candidate, and $\iota_0$ is its derived or recovered identity. The source's deterministic derivation is a naming mechanism, not a proof that two arbitrary artifacts have identical semantics.

Decision keys preserve the boundary between view and column segments. Collapsing `invoice.line_total` and `invoice_line.total` into one flattened key would lose a real distinction; the resolver retains that separation.

## Shared fields are settled before association writes

Several recovered views can describe the same reusable field. Sharing resolution groups compatible candidates, selects a shared identity, and records how their views should link to it. Explicit decisions still take precedence.

The architectural objective is to recover the definition/occurrence distinction: one field definition can serve several associations. Consolidation is not simply deduplication by display label. The field's represented structure and the resolver's compatibility rules determine whether sharing is appropriate.

The report records shared and consolidated fields so that a smaller written count is explained rather than mistaken for silent loss. This is another reason a raw number of inserted rows is not a sufficient description of extrusion.

## Writing follows dependency order

The dispatcher writes component details first. When administrator modeling is enabled, fields precede admin views, their field associations, and conditions. Dynamic Gets precede the corresponding site-view and custom-admin-view relationships. Component links are completed after the definitions they reference.

This ordering permits later writers to use the identities established by earlier ones. Let $w_i\prec w_j$ mean writer $j$ requires an identity or record produced by writer $i$. The dispatcher supplies an execution order compatible with its supported dependency relation.

The source does not wrap every writer in a single global transaction. Individual write results and failures remain part of the report. A portable implementation must distinguish dependency order from atomic commit: one does not imply the other.

## Existing-item policy and review policy are different controls

The general `onExisting` selection governs supported skip, update, or replace behaviour. Pairing decisions select a candidate's target and whether it should be written. Dry-run selection allows the relevant writer paths to report intended work without persisting it.

These controls should not be collapsed into one Boolean called “overwrite.” They address different questions: which definition is this, what should happen where it already exists, and should this run apply the resulting writes?

## Diagnostics complete the recovery account

The extruder reports unreadable artifacts, unresolved field types, absent translations, duplicate candidate view names, dropped conditions, and deliberate skips. A completed run can therefore be useful without pretending that every property of every source artifact was recoverable.

The report's completion flag means the orchestration reached its defined completion path. It does not erase the per-item record. The same distinction is used by the forward compiler's artifacts and diagnostics. [Execution](../compiler/execution.md)

Pairing completes the bridge back to normal development. The resulting local graph has explicit identities and relationships, can be edited in the GUI, can be exported as a blueprint, and can be compiled through JCB's ordinary generators. The architecture makes recovered information usable rather than leaving it as a disconnected source archive.
