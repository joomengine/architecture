---
title: Provenance and explanations
description: Explaining why a value exists, why it was reused, where it was emitted, and which human adaptation affected it.
section: Mechanisms
order: 39
evidence: Proposed extension and formal model
---
# Provenance and explanations

## Recollection should be explainable

A system that can answer “what do I know about this?” should also be able to answer “where did that knowledge come from?” The latter question distinguishes trustworthy reuse from an unexplained cache hit.

For each derived fact, record its source identities, source epoch, rule identifier and revision, occurrence context, and direct supporting facts. For each artifact, record the fragments and bindings used. For each editorial update, record the source artifact and the reconciliation decision.

## Derivation graph

A derivation is a hyperedge from its premises to its consequence. Multiple hyperedges can justify the same consequence. This permits explanations of both fan-in and alternative derivations without copying entire histories into every value.

A compact trace record can contain:

```json
{
  "result": "view:CRM/contact:validation",
  "epoch": "example-snapshot-1",
  "rule": "validation-from-fields@1",
  "inputs": ["field:CRM/contact/email", "field:CRM/contact/status"],
  "evidence": "derived",
  "scope": ["CRM", "contact"]
}
```

This is an illustrative schema for a future implementation, not a JCB database export.

## Different questions require different traces

“Why was this dependency loaded?” needs the request-discovery graph. “Why does this file contain this line?” needs derivation and binding provenance. “Why was this user edit accepted?” needs a reconciliation record. “Why was this result reused?” needs cache-key and invalidation evidence.

A single timestamp or source-line comment cannot answer all four questions.

## Provenance is not truth

A derivation can be perfectly traceable and still rest on a false premise or an incorrect rule. Provenance supports audit and debugging; it is not an oracle of semantic correctness. The same warning is especially important in AI applications, where a retrieved assertion should not become a verified fact solely because the system stored its source URL.

## Storage tradeoffs

Full traces can be expensive when many artifacts reuse the same knowledge. Store shared provenance nodes once and link to them. Decide whether to retain all alternative derivations or one sufficient explanation. If only one is retained, do not claim that the trace captures every reason a fact remains valid after deletion.

Database provenance research offers established models for tracking combinations and alternatives of contributing inputs. VDMT can adopt those ideas without claiming to originate them. [R05](../reference/bibliography.md#r05)

## Privacy and trust

Provenance may expose secrets, source paths, usernames, or private document content. A public build manifest should not disclose everything in an internal trace. Separate internal audit records from publishable evidence and apply explicit access and retention rules.

The present JCB case study identifies selected trace-like mechanisms, including source markers and custom-code location records. A complete generic provenance hypergraph is a proposed extension, not an observed universal property of the compiler.
