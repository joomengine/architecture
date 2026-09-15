---
title: Deferred execution and substitution semantics
description: Prerequisite ordering, phase boundaries, exact ordered replacement, filtered maps, and finite stage completion.
section: Formal Model
order: 74
evidence: Formalization of deferred admin work, fieldset passes, and Placeholder semantics
---
# Deferred execution and substitution semantics

Staging determines when information is consumed. It appears in deferred operations, contextual code retrieval, file binding, and late dependency injection. The common concern is readiness; the individual operations retain different semantics.

## Deferred operations retain their arguments

Represent deferred work by

$$
w=(f,a,r,p),
$$

where $f$ is the operation, $a$ its arguments, $r$ its required information, and $p$ its designated phase. The condition for execution is that the phase has been reached and the required observations have been established for that operation.

JCB's `secondRunAdmin` retains operations and argument arrays and replays them after the earlier admin/component work. Its control sequence supplies the prerequisite ordering. The mathematical $r$ makes that dependency explicit; it does not claim that production entries all contain machine-readable prerequisite sets.

## Phase ordering can establish readiness

Suppose every producer required by work $w$ completes in an earlier phase, its results are retained, and no intervening operation invalidates them. Then the designated replay phase can execute $w$ with those requirements available.

**Argument.** Every required producer precedes replay. Retention preserves its result through the intervening steps. The non-invalidation assumption ensures the result remains applicable. Their conjunction establishes the operation's readiness at replay.

This proposition explains the purpose of a phase boundary. It does not require a generic scheduler or a whole-program fixed-point loop. A second fieldset pass and a linked-view replay are selected operations at known completion points. [Deferred work](../compiler/deferred-work.md)

## Ordered replacement within one pass

For an ordered map $P=\langle(k_1,v_1),\ldots,(k_n,v_n)\rangle$, define

$$
\sigma_1(s,P)=s_n,\qquad
s_0=s,\quad s_i=\operatorname{replaceAll}(s_{i-1},k_i,v_i).
$$

Each `replaceAll` replaces the occurrences in its input for that operation; it does not repeatedly process the newly inserted value against the same key until no match remains. Keys are nonempty in the model.

For the filtered action, first select entries using the original input:

$$
P_s=\langle(k_i,v_i)\in P\mid k_i\text{ occurs in }s\rangle,
\qquad \sigma_3(s,P)=\sigma_1(s,P_s).
$$

The selection happens once, before the ordered replacements. The presence-check action returns $s$ when no key occurs and otherwise applies the ordinary ordered map. [Binding](../compiler/binding.md)

## An introduced token distinguishes the algorithms

Let $P=\langle(A,B),(B,x)\rangle$. Then

$$
\sigma_1(A,P)=x,\qquad \sigma_3(A,P)=B,
$$

because the filtered action removes the `B → x` entry when `B` is absent from the original input. For input `A B`, both entries survive filtering and the result is `x x`.

Reversing the entry order changes the ordinary result for input `A` to `B`. These examples establish that ordered replacement, original-input filtering, and simultaneous substitution are different semantics.

They also show why determinism does not require commutativity. Fix the map order and input, and the result is well-defined. Change the order, and a different result can be correct for that different input program.

## A finite pass does not imply small output

A pass with finitely many finite key/value pairs terminates on finite input under finite string-replacement operations. It can still expand its input substantially. Several stages can compound that expansion.

If $b_i$ is the byte length before replacement $i$ and $m_i$ the number of selected occurrences, then

$$
b_{i+1}=b_i+m_i(|v_i|-|k_i|).
$$

The occurrence count is evaluated on that replacement's actual input, which can include text introduced earlier in the pass. Costs therefore depend on intermediate as well as final sizes.

## Multiple passes have an explicit composition

For staged environments $P_0,\ldots,P_{n-1}$ and selected actions $a_i$,

$$
s_{i+1}=\sigma_{a_i}(s_i,P_i).
$$

Custom-code expansion, events, and Power injection can occur between passes and can expose new work. The operation that introduces a token must precede a suitable consumer if that token is intended to be resolved in the build.

A token introduced after its applicable consumer has already run will remain unless another designated operation handles it. The formal model identifies that ordering issue; it does not attribute a universal unresolved-token validator to the production placeholder service.

## Context has a lifetime

A prepared fragment can be retained before its destination is known. Retrieval applies the context at the later consumption point. A filename binding, module prefix, or view-specific method body has a scope and lifetime different from a globally reusable definition.

A phase-local environment can therefore be overwritten legitimately as the compiler moves to another artifact. Correctness depends on establishing it before use and avoiding unintended leakage into another context. An implementation using explicit context arguments can make the same boundary structural rather than relying on shared mutable configuration.

The [reference mechanisms](../engineering/reference-model.md) test the exact replacement cases, deferred prerequisite handling, and ordered contribution behaviour. These small tests make the semantic distinctions executable without pretending to recreate the complete Joomla compiler.
