---
title: Self-generation and bootstrapping
description: Regenerating a generator's host system, with precise distinctions from self-hosting compilers, fixed points, and Turing completeness.
section: Mechanisms
order: 41
evidence: Formal model and terminology comparison
---
# Self-generation and bootstrapping

## A system can be one of its own products

A generator may accept a model of the application that hosts the generator and produce that application again. This is **self-generation** at the model-to-artifact level. When successive generated versions are used to build later versions, the workflow is a form of **bootstrapping**.

The scope must be explicit. Generating the Joomla application that contains a PHP-based compiler is not the same as implementing a compiler for the PHP language. A conventional self-hosting language compiler is written in the language it compiles. JCB's reported self-build should be described at the level its model and output actually cover.

## A testable construction

Let $G_0$ be the trusted seed generator, $D_G$ the model of the generator-bearing application, and $E$ the fixed environment. Build

$$
A_1=G_0(D_G,E),\qquad G_1=\operatorname{activate}(A_1).
$$

Then build $A_2=G_1(D_G,E)$, activate $G_2$, and build $A_3=G_2(D_G,E)$. Compare $N(A_2)$ and $N(A_3)$ using a declared normalizer $N$.

Equality is evidence of a stable generated result for that model and environment. It is not a proof of correctness for all possible models or of the absence of malicious behavior in the seed.

## A fixed point at the right level

For a fixed model and environment, define $H(G)=\operatorname{activate}(G(D_G,E))$ when activation succeeds. A stable self-generation claim can be expressed as $H(G)\equiv G$ under a specified equivalence. Such a fixed point is different from the finite fact closure inside one build.

Do not merge those two uses of “fixed point.” One concerns increasing knowledge under derivation rules. The other concerns reproduction of a generator-bearing artifact or its behavior.

## What self-generation demonstrates

It can demonstrate that the modeling and generation facilities are expressive enough to represent an important, nontrivial part of their own host system. It can stress-test persistence, packaging, reusable code, and long-term maintenance. It is a substantial engineering capability when the regenerated scope is broad and the process is reproducible.

It does not establish universal computational power. A small program can copy itself without being a universal machine. Conversely, a universal programming language need not have a self-hosting compiler. “Turing completeness” and the ACM Turing Award are not certifications automatically obtained by self-generation.

## Established comparison

GCC's documented bootstrap compares successive compiler stages, supplying a useful methodological analogy. Thompson's discussion of compiler trust explains why self-reproduction alone cannot establish trustworthiness. These are credited precedents, not claims that JCB follows their exact implementation. [R06](../reference/bibliography.md#r06), [R07](../reference/bibliography.md#r07)

## Evidence boundary in this paper

The author reports that JCB builds JCB, and the pinned JCB README identifies the component as created with JCB. This supports the self-generation account. A complete three-stage JCB reproduction, including its database model and all dependency inputs, was not run for this edition. The [self-build case study](../jcb/self-build.md) states precisely what evidence is available and how a stronger reproducibility certificate can be produced.
