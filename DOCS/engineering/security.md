---
title: Security and trust boundaries
description: Source authority, code-generation trust, marker injection, path safety, dependency integrity, and safe publication.
section: Engineering
order: 73
evidence: Proposed implementation contract
---
# Security and trust boundaries

## Generated does not mean trusted

A generator can faithfully reproduce malicious input. Determinism, provenance, and successful parsing do not make the resulting program safe. Every source adapter should identify its authority, trust level, and permitted contribution type.

Distinguish ordinary data, identifiers, expressions, templates, and executable code. A user allowed to change a field label is not necessarily allowed to inject arbitrary PHP or shell code. Where executable custom code is an intended feature, authorization and review are the boundary; generic escaping cannot preserve arbitrary code while also making it harmless.

## Context and ownership

Include tenant, component, repository, target, or other ownership dimensions in identity where they affect access. A cache hit must not bypass authorization. Two equal short names in different owners' contexts must not cause cross-project disclosure or mutation.

Provenance can itself contain sensitive information. Public manifests should expose only approved metadata, while internal audit records can retain richer traces under access controls.

## Editorial marker attacks

An untrusted body may contain text resembling a region boundary. The extractor must use an explicit grammar and reject ambiguous nesting or duplicates. A valid-looking marker does not prove that the editor was authorized or that the record belongs to the current artifact.

Bind region IDs to artifact ownership and the previous generation manifest. Treat unknown or conflicting IDs as errors. Context fingerprints locate text; they are not signatures. Base64-encoded captured code remains code, not sanitized or encrypted content.

## Filesystem safety

Validate destinations before writing. Reject traversal, absolute paths, unexpected separators, case collisions, and unowned output locations. Resolve symlink behavior explicitly. Prefer a fresh staging directory with controlled permissions rather than following arbitrary existing paths.

A compiler that imports edits from installed files needs a separate allowlist of readable targets. It should not recursively scan unrelated directories merely because a filename matches an extension pattern.

## Acquisition and supply chain

Remote definitions, templates, and browser dependencies must have recorded versions and integrity information. Use authenticated or verified transport as appropriate; distinguish a missing resource from a failed network request. Do not silently fall back to a different dependency version while claiming reproducibility.

The website build acquires versioned rendering dependencies and records integrity metadata. Its published pages do not need to send readers' article content to a third-party rendering service.

## Resource bounds

Bound request count, expansion depth, file size, output bytes, parser work, and execution time. A small definition graph can expand into a very large occurrence set. Rejecting an exceeded limit is safer than exhausting the host and publishing a partial result.

## Publication and recovery

Validate the complete staged output before changing the active publication. Retain the last known successful manifest and make rollback explicit. Database persistence and filesystem publication require a concrete recovery protocol; they are not automatically one transaction.

Self-generation does not remove the seed-trust problem. A stable self-build can reproduce an unwanted behavior just as consistently as a wanted one. [R07](../reference/bibliography.md#r07)
