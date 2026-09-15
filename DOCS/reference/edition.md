---
title: Edition scope and engineering record
description: The publication's authorship, implementation scope, source captures, mathematical conventions, and measurement boundaries.
section: Reference
order: 92
evidence: Edition metadata and source/measurement scope
---
# Edition scope and engineering record

**Title:** Joomla Component Builder: Contextual Compilation Architecture  
**Author:** Llewellyn van der Merwe  
**Publisher:** Vast Development Method  
**Architectural edition:** 1.0.0 · 16 September 2026  
**Publication:** architecture.joomlacomponentbuilder.com

This is the author's technical white paper, prepared with research and editorial assistance. It explains the implemented architecture in language-neutral terms and connects the explanation to source responsibilities, public blueprints, generated products, and executable mathematical examples.

The edition number identifies the publication. It is not a Joomla or JCB software release number.

## Compiler and integrated capability scope

The core compiler source study is pinned to official revision `bca4a1520484f3e2c2fbd12964a5995b0d058de1`. It covers acquisition, semantic classification, intermediate stores, deferred execution, target selection, ordered binding, code injection, generated application concerns, recovery, and packaging.

The edition additionally documents the implemented component and class extrusion machinery prepared for the integrated release: bounded artifact discovery, typed readers, property precedence, candidate pairing, shared-field resolution, class/namespace reconstruction, and ordered model writers. This capture extends beyond the older core pin. Its paths and SHA-256 fingerprints are recorded under [X01–X04](source-map.md#x01), rather than linked to files that are absent from that pinned revision.

The architectural description includes those implemented operations. Availability in a particular installed release is determined by the [official JCB repository and release](https://github.com/joomengine/Joomla-Component-Builder), not by the white paper's edition number. This separates capability description from release packaging without requiring the architecture to be rewritten when the integration is published.

## Source and documentation captures

The [source map](source-map.md) fixes the core compiler, operational documentation, Hello World blueprint and products, Service Directory family, and reusable distribution repositories. The inspection follows the principal operation paths and their collaborators. A repository snapshot being collected is not represented as a claim that every line in it was independently audited.

The documentation repository supplies the authoring and operational context for mechanisms visible in source. Public examples make selected input/output correspondences inspectable. The supplemental source capture fixes the integrated extrusion behavior without introducing another public compiler repository into the publication.

Historical implementation is separately pinned to root commit `ecf47809f960bd057af8a414168fada6fe22c5f7`, recorded on 30 January 2016 at 20:28:43 UTC. The current paper and every later feature are not retroactively assigned that date.

## The maintained measurement record

The author records repeated self-builds in which an approximately 30,000-line exported JCB blueprint produces an application exceeding one million lines in approximately 60–64 seconds on the demonstrated setup. Compiler rules, templates, reusable Powers, libraries, and assets participate as additional inputs.

The paper preserves this as an engineering measurement record. It does not assign a hardware configuration or per-run data that was not supplied. The inspected timer boundary and the separately counted pinned repository snapshots are identified in [performance](../engineering/performance.md). A new reproducible run package can add its environment, blueprint, output inventory, and individual timings to that record.

Output volume, compilation elapsed time, and hypothetical manual development effort are different measurements. Compiler-produced estimates based on seconds per line or file are not relabeled as measured hours saved.

## Mathematical scope

The formal account introduces explicit identities, contexts, contributions, state transitions, request graphs, binding sequences, and representation equivalences. Its propositions state assumptions for the mechanism being described. Finite request traversal, safe contextual reuse, prescribed-sequence repeatability, and transport preservation are separate results.

A source path corresponds to a proposition where the path meets its assumptions. The model does not replace ordered mutation with a fictional immutable state, infer global transactions from ordered writes, or turn every generated region into a universally invertible transformation.

The mathematical contribution of the publication is the explicit account of this architecture's relationships and operations. Established proof techniques and related systems are credited in the [bibliography](bibliography.md).

## Authorship and originality

The development account records the author's independent construction of JCB and its subsequent refactoring and maintenance. Retrospective correspondences to earlier research are acknowledged as correspondences, not invented influences. Independent development and first historical invention are different claims.

Application authors retain their attribution. In particular, the Service Directory example names Lemuel van der Merwe as its application author. Joomla and reusable third-party works retain their own authorship and licenses. The paper's account of JCB does not claim ownership of those works.

## Using this edition

The main reading path describes what the system does and how its operations fit together. The [source map](source-map.md), [verification guide](../engineering/verification.md), [citation information](citation.md), and [publication details](publication.md) support reproducible examination. Each article has an exact Markdown alternate, and complete downloadable editions are generated from the same source.

The intended use is understanding and reuse: another engineer should be able to identify a represented decision, follow its transformation, examine the mathematical relation, and implement the same architectural choice in a different technology.
