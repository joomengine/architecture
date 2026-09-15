---
title: Hierarchical reuse and expansion
description: Shared definitions, contextual occurrences, fan-in, fan-out, cardinality, and the source of large output expansion.
section: Mechanisms
order: 32
evidence: Formal model
---
# Hierarchical reuse and expansion

## Definitions form a graph; uses form occurrences

A field type can be reused by many field definitions. A field definition can occur in several views. A view definition can occur in several components. Values derived for a view can be reused across several files belonging to that component.

This is a shared definition graph plus a context-qualified occurrence structure. Treating it as a single tree loses sharing; treating it as only a set of definitions loses the distinct uses.

## Worked cardinalities

Consider two field types, `Text` and `Choice`, and three field definitions: `title`, `email`, and `status`. The `contact` view uses all three; `subscription` uses `email` and `status`. A `CRM` component uses both views, while a `Portal` component uses `contact`.

There are three field definitions but eight field occurrences: three in `CRM/contact`, two in `CRM/subscription`, and three in `Portal/contact`. There are two view definitions but three view occurrences. If each view occurrence produces four files and each component produces three singleton files, the plan contains eighteen file occurrences. These are illustrative counts, not measurements of JCB.

The same `email` definition may have different permissions or labels in the three occurrence contexts. Sharing its base definition must not overwrite those distinctions.

## Expansion function

Let $D$ be the definition graph, $r$ a root, and $\Gamma_0$ its initial context. Expansion produces

$$
\operatorname{expand}(D,r,\Gamma_0)=O,
$$

where $O$ is a finite set or ordered family of occurrences. An occurrence records the definition it instantiates and the context inherited or assigned through the incoming relationship.

A reusable relationship itself can carry settings. Therefore the interpreter may depend on edge attributes, not merely on the parent and child nodes. This matters whenever a view is enabled in one component but disabled, reordered, or configured differently in another.

## Fan-out and fan-in

One view-derived value can fan out to a model, controller, permission definition, and language entry. Conversely, one output fragment may require several fields and component-level configuration. The compiler's large output is explained partly by this multiplicative projection of shared knowledge into many conventional destinations.

That does not create semantic information from nothing. Templates, transformation rules, target conventions, and dependency libraries contribute information alongside the database input. Comparing only database line count with output line count omits those other inputs.

## Aggregate ordering

Fields in a view often have a meaningful order. An unordered set of field identities is insufficient for rendering. Preserve an explicit order or a canonical sorting rule, and define how ties are handled. The same applies to view order and fragment contributions.

## Failure boundaries

Shared mutable occurrence state can leak settings between components. Caching by definition alone can reuse a target-specific interpretation incorrectly. A recursive definition may produce unbounded occurrences even when the definition graph is finite. Two different occurrences may resolve to the same destination path.

The corresponding safeguards are [scoped memory](scoped-memory.md), [occurrence identity](occurrence-identity.md), [termination](../semantics/termination.md), and [materialization validation](materialization.md).
