---
title: Binding stages and placeholder semantics
description: Ordered substitution, delayed values, token namespaces, staging hazards, and the distinction between simultaneous and sequential replacement.
section: Mechanisms
order: 34
evidence: Formal model and source comparison
---
# Binding stages and placeholder semantics

## A placeholder is an unresolved obligation

A placeholder represents a value not yet materialized at that location. It can stand for a name, a fragment, a language constant, a dependency reference, or an editorial insertion. The delimiter syntax is incidental; the binding time and authority are not.

Let $P_i$ be the binding environment for stage $i$. A staged renderer is

$$
A^{(0)}=T,\qquad A^{(i+1)}=\sigma_i(A^{(i)},P_i).
$$

The final artifact is valid only if all obligations assigned to completed stages are resolved or explicitly allowed to remain as literal target-language content.

## Ordering is semantic

Suppose a global stage resolves `{{component}}`, and a later local stage inserts a body containing that token. The earlier global stage cannot have resolved a token that did not yet exist in the text. The design must pre-bind the body, schedule a declared later global pass, or forbid that dependency direction.

This is why the number and order of replacement passes matter. A generic “replace everything until it looks finished” loop hides both dependencies and possible nontermination.

## Two replacement semantics

**Simultaneous, non-recursive substitution** replaces tokens recognized in the original input of that pass. Replacement values are not scanned again during the same pass.

**Sequential replacement** applies an ordered list of replacements to the evolving string. A replacement can introduce text matched by a later replacement. Reordering the map can therefore change the result.

The reference model chooses explicit non-recursive passes for clarity. The inspected JCB `Placeholder::update()` and `update_()` call PHP `str_replace` with key/value arrays; this is an implementation-specific sequential replacement behavior, not the reference model's semantics. The paper does not equate them. [J08](../reference/bibliography.md#j08), [R12](../reference/bibliography.md#r12)

## Presence filtering is not unresolved-token validation

JCB's action 3 filters replacement-map entries whose keys are absent from the input string before calling replacement. It does **not** mean “remove unknown placeholders from the file,” and it is not a complete check that every required token was resolved. [J08](../reference/bibliography.md#j08)

A portable implementation should separately validate unresolved required tokens, distinguish intended literal delimiters, and report the source of the missing binding.

## Scoped and late bindings

Component-wide bindings, view-specific bindings, reusable-code references, and language or dependency bindings can have different lifetimes. A shared environment can be reused across many artifacts while a local environment belongs to one occurrence.

Late binding is justified when the value becomes authoritative only after other structure is known. It should not become a way to hide a dependency that could have been modeled earlier.

## Escaping and capture

A string token replaced inside PHP, JSON, HTML, SQL, or a shell script crosses a syntax boundary. The renderer must know whether it is inserting an identifier, string literal, expression, or trusted code block. Generic HTML escaping is not a universal solution.

For structured targets, an AST or typed intermediate representation can make binding safer. That is a valid VDMT implementation choice even though JCB's observed mechanism often uses strings and templates.

See [file emission](../jcb/file-emission.md) for the concrete JCB ordering, and [security](../engineering/security.md) for trust boundaries.
