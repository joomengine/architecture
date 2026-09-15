---
title: Assets and repository coordination
description: Files, folders, repository indexes, channel configuration, and the boundaries between portable design and external resources.
section: Blueprint Exchange
order: 25
evidence: Asset normalization, content transport, repository definitions, and ecosystem repositories
---
# Assets and repository coordination

An application blueprint includes more than database-shaped records. Definitions can refer to images, compiler input files, library folders, scripts, and other material whose content lives in the filesystem. JCB gives those resources a transport path rather than assuming that every destination installation already contains them.

Repository definitions are themselves managed information. They identify where a particular channel of reusable material can be read and, where authorized, written. The same overall lifecycle therefore coordinates both development definitions and the locations from which definitions are obtained. [B07](../reference/source-map.md#b07), [B08](../reference/source-map.md#b08)

## Asset references retain both identity and destination

An exported file dependency can carry a repository key, a normalized pointer, its original value, an entity kind such as `file`, and a target area. Hello World's admin-view icons demonstrate this directly: an image referenced by the view becomes a transported file dependency associated with the images target.

The content's repository identity and its destination path serve different purposes. A normalized key locates the published content. A target plus a value tells the importer where the content belongs in the local environment. Treating the two as one unconstrained filename would obscure both portability and path handling.

The normalization and content services map those values into the configured targets. Ordinary acquisition can retain an existing local file; forced retrieval can refresh it. The operation records diagnostics for resources that cannot be obtained or placed. [B07](../reference/source-map.md#b07)

## Files and folders are not ordinary entity rows

Entity payloads are mapped through table-aware persistence. Asset content is written through filesystem services. The package builder drains entity dependencies and then invokes file/folder transport for the accumulated asset requests.

This separation allows the graph to contain both kinds of requirement without pretending they have identical storage semantics. A database insert, an image write, a directory transfer, and an index update can fail independently. Their status belongs to the operation's report.

For a definition graph $G$, write its complete transport requirement as

$$
\operatorname{requirements}(G)=V_G\cup A_G,
$$

where $V_G$ is the selected entity set and $A_G$ the asset set. The union is typed: it does not erase the difference between an entity request and an asset request. A complete import must satisfy each request using its appropriate handler.

## Channels select the appropriate repository contract

The ecosystem separates component packages, Super Powers, Joomla Powers, field types, snippets, and repository definitions into corresponding distribution surfaces. Their indexes have different item schemas and their contents serve different compiler responsibilities.

The public repositories supplied with this edition illustrate those roles. `joomengine/packages` and `joomengine/joomla-packages` distribute application blueprints. `joomengine/super-powers` distributes reusable code definitions. `joomengine/joomla-powers` supplies target-sensitive Joomla class mappings. `joomengine/joomla-fieldtypes` supplies field-type definitions. `joomengine/snippets` carries reusable interface material. `joomengine/repoindex` describes repository targets. [E06](../reference/source-map.md#e06)

These are examples of the distribution architecture, not a restriction to a centrally owned catalogue. The configured repository list determines which sources a particular installation uses.

## Read and write policy are separate

A read branch supplies definitions for acquisition. A write branch identifies the destination for publication. Entity approval and repository eligibility determine which writes are attempted. Index caching reduces repeated acquisition of the same catalogue within an operation.

The distinction is useful in a review workflow. A developer can consume an accepted definition, make local changes, and publish those changes to an appropriate review destination without redefining the item's portable identity. The branch and revision remain part of the source configuration when reproducibility matters.

The repository API also returns content identifiers used for updates and unchanged-content checks. Those identifiers support repository operations; they should not be confused with proof of authorship or execution safety for the downloaded code.

## External code is another, distinct path

JCB also supports explicit external-code references embedded in code. That mechanism reads a specified resource and applies its own change-history and authorization behaviour. It is not interchangeable with importing a managed Power or field definition from an entity index. [Custom code and external material](../compiler/custom-code.md)

The white paper keeps these paths separate because they have different identities, trust decisions, and local persistence. Their shared purpose is to make required material available to compilation; their operational contracts determine how that availability is achieved.

## Reuse beyond the original representation

An implementation in another language can preserve the same architecture with object storage, a package registry, or another versioned transport. It needs typed resource identities, target-aware placement, explicit source selection, and a clear distinction between metadata and executable or display content.

The portability lies in those relationships and operations. It does not depend on retaining JCB's repository folder names or using a particular Git hosting provider. The [implementation guide](../engineering/implementation.md) develops that separation while keeping the source-specific behaviour visible in the [source map](../reference/source-map.md).
