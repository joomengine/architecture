---
title: Self-generation and maintenance propagation
description: JCB's own blueprint-driven application, reusable library inputs, and how shared compiler changes propagate through regenerated products.
section: Engineering
order: 83
evidence: Maintainer development account, official generated application, and compiler target/reuse mechanisms
---
# Self-generation and maintenance propagation

JCB builds its own application through the same blueprint-driven development approach it supplies to other projects. The generated application layers outside the library collection include the authoring interface and the Joomla integration needed to manage definitions and invoke the compiler. Reusable library and Power inputs supply substantial implementation, including the compiler's own specialized services.

This is a concrete use of the architecture on its own development tool. Its model describes the application that manages models; its generated interface supports further work on those definitions. [C01](../reference/source-map.md#c01), [E07](../reference/source-map.md#e07)

## Separate the generator's application from its supplied libraries

Let $B_J$ be JCB's application blueprint, $L_J$ its supplied libraries/Powers, and $\Theta_T$ its target generation rules. The self-build can be represented as

$$
A_J=\operatorname{compile}(B_J,L_J,\Theta_T,C,H).
$$

The output $A_J$ is the delivered JCB application with its generated layers and included dependencies. The equation does not say that $L_J$ is invented during compilation. Its manually developed and reviewed implementation is an input whose inclusion and placement the build coordinates.

The distinction also explains the repository structure. Generated application code and reusable library source are both present in the delivered project, but their immediate origins differ. A repository line count alone cannot assign authorship effort to either category.

## Self-generation exercises the architecture's actual workload

JCB's own model contains the relationships, editors, fields, permissions, custom code, and integrations required by a development platform. Regenerating that application exercises a broader model than a minimal example while keeping the same underlying acquisition, classification, binding, and packaging responsibilities.

The significance is operational: the architecture is used to maintain the application that exposes it. Its recurring self-build connects changes in stored design and reusable implementation to a concrete runnable product.

The maintained performance record describes repeated self-builds of this kind. [Build measurements](performance.md)

## Shared rules carry maintenance knowledge

A generated application's blueprint expresses choices such as a field's storage, a view's model, a permission option, or a target-platform reference. The compiler supplies recurring implementation around those choices.

When a shared generation rule is corrected, each model that uses that rule can receive the correction through regeneration. The work is performed at the generation-knowledge boundary rather than manually repeated in every affected application file.

Let $\Theta$ and $\Theta'$ differ in one rule family. For application models $B_1,\ldots,B_n$, the propagated products are

$$
A_i'=\operatorname{compile}(B_i,L_i,\Theta',T_i,C_i,H_i).
$$

Only applications whose selected paths consume the changed rule need exhibit a corresponding output change. The relation is determined by their definitions and occurrence choices, not by a claim that every update changes every file.

## Target adaptation preserves represented intent

JCB's target-specific emitters and Joomla Power mappings separate application intent from selected platform conventions. A platform change can be incorporated into those shared rules while the application retains its field and view definitions.

The compiler then emits the updated controller/model/view, service-provider, import, routing, or installation conventions under the chosen target. [Target selection](../compiler/targets.md)

This maintenance path is strongest where the design uses represented compiler abstractions. Arbitrary embedded target-specific code and deliberate whole-class replacements retain their own authorship and maintenance boundaries. Regeneration does not infer an unstated business-rule migration from unrelated source code.

## Editable regions and overrides have different ownership

A designated code region can be recovered and placed into the next generated structure. A full source-class override supplies a complete class and intentionally replaces the default emitter's ownership of that class. A reusable Power supplies a managed definition that can be updated independently.

Those choices allow different balances of automation and control. The paper describes them separately because their maintenance consequences differ: a recovered method fragment receives a regenerated surrounding class; a complete override retains the author's surrounding implementation as well.

## Distribution multiplies reuse across projects

Blueprint repositories distribute application design. Power and field-type repositories distribute reusable definitions. Repository-target definitions make those sources discoverable. Local-first acquisition preserves editable working copies while explicit reset/publication operations control updates.

The compiler combines those layers when generating an application. A reusable definition can therefore influence several projects through their declared dependencies, and a compiler rule can influence several output artifacts within each project.

The multiplier is the repeated application of shared knowledge under explicit context. It can be described without hypothetical saved-hour formulas: identify the changed input, identify its consumers, regenerate, and inspect the resulting products.

## A basis for studying the next implementation

The architectural account makes those relationships visible enough to evaluate. It identifies what must retain identity, what can be reused, which work must wait, and which outputs share a decision. That understanding can guide later improvements to JCB or another implementation.

This edition first documents the current mechanism. Future changes can then be compared against a clear behavioral model rather than against an impression formed from the size of the original classes or the number of generated files.
