---
title: Definition, occurrence, and artifact identity
description: Stable identity across reuse, multiple destinations, renaming, editorial recovery, and component boundaries.
section: Mechanisms
order: 33
evidence: Formal model and proposed portability contract
---
# Definition, occurrence, and artifact identity

## Three identities, three responsibilities

A **definition identity** identifies reusable source knowledge. An **occurrence identity** identifies one contextual use of that knowledge. An **artifact identity** identifies one planned output. None should be silently substituted for another.

A useful representation is

$$
d=(\text{namespace},\text{kind},\text{id},\text{revision}),
$$
$$
o=(d,\Gamma,\text{role}),\qquad
 a=(\text{owner},\text{logical artifact role},\text{occurrence key}).
$$

The artifact's destination path is then calculated from $a$ and the target configuration. This allows the logical identity to survive a path change when the application supports such a migration.

## Repeated files and singleton files

One template may produce files at several locations. Those are different artifacts, even if their bytes are identical. Conversely, several facts may contribute to one singleton file. Such a file is not duplicated merely because several rules mention it.

The artifact planner must distinguish “emit once for the component,” “emit once per view occurrence,” “emit once per field-type implementation,” and “copy to every declared destination.” These are different cardinality rules, not special cases to hide inside path concatenation.

## Scope ownership

A component-local fact must not be resolved from another component merely because it has the same short name. A shared definition may be deliberately global, but its sharing policy must be explicit. Namespace, ownership, and revision are part of authority.

This is a general architectural obligation, not a diagnosis of a particular matching defect in an uninspected implementation. The goal is to make invalid cross-owner reuse unrepresentable or detectably conflicting.

## Editorial identity

A preserved region needs an identity such as $(a,\text{region id})$. The region's content is not its identity: editing the content must not erase its association. Line numbers are useful observations but fragile identities because preceding code can move.

If the same source definition appears in multiple editable occurrences, extraction may produce multiple candidate updates. There are only a few coherent policies: keep edits occurrence-local; require all shared-definition edits to agree; or ask an authorized user to choose a shared update. Silently letting the last scanned file win is not a principled merge.

## Renames and migrations

Changing a path can preserve logical identity. Changing the meaning of a region may require a new identity. A migration should explicitly map old identities to new ones and preserve a record of the mapping. A heuristic path match must not be treated as certain when several targets are plausible.

## Identity is not merely hashing

A hash can verify bytes or help locate context. It does not establish who owns a definition, whether two equal strings have the same meaning, or whether an edit should be shared across components. Cryptographic identity and semantic identity solve different problems.

## Conformance check

Given two occurrences of one definition in different components, a test should demonstrate both reuse of the base knowledge and isolation of occurrence-specific values. Given two planned artifacts resolving to one path, the implementation should detect the collision before publication. Given a moved editable region, it should either apply a declared migration or return a conflict rather than guess.
