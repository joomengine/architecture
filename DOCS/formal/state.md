---
title: Operational state and execution traces
description: A transition-system account of the compiler's stateful orchestration, effectful acquisition, intermediate contributions, and materialized products.
section: Formal Model
order: 71
evidence: Formal model derived from the documented execution sequence
---
# Operational state and execution traces

The complete compiler is an effectful process. It reads definitions, can acquire remote material, updates shared stores, creates and rewrites files, recovers designated code, and records messages. Its mathematical representation must include those operations rather than treating compilation as one pure substitution over an already complete dictionary.

## State components

For one invocation, define

$$
\Sigma=(q,D,K,O,M,W,P,A,X,\Delta).
$$

$q$ is control state, including the current phase and call/continuation position. $D$ is local design state. $K$ records acquisition attempts and outcomes. $O$ contains established occurrences and contextual selections. $M$ is the intermediate-store family. $W$ contains deferred operations. $P$ contains active binding environments. $A$ contains staged artifacts. $X$ records relevant external observations. $\Delta$ contains diagnostics and operation results.

The representation does not require all these values to be stored in one production object. It identifies the information necessary to explain observable execution.

An operation labelled $o$ produces a transition

$$
\Sigma\xrightarrow{o/x}\Sigma',
$$

where $x$ supplies an external observation when the operation reads one. A complete trace is a finite sequence of such transitions beginning with a build request and ending at the selected completion or failure state.

## Representative transition rules

A local acquisition reads a definition under its typed request and records a local result. A remote acquisition additionally chooses a configured source, reads its payload, maps it to local data, and records dependencies. The attempt guard is established at its prescribed point; the persistence result is a separate event.

Interpretation of an occurrence applies its contribution sequence:

$$
M'=\operatorname{foldApply}(J(d,\Gamma),M).
$$

A deferred-work transition appends an operation and its arguments to $W$. A replay transition removes or consumes work in the specified phase and applies its contributions. A binding transition transforms an artifact using the selected ordered environment. A write transition changes the physical-artifact observation and can update counters or diagnostics.

These rules retain replacement and removal. An output filename binding can change from one artifact to the next without violating the state model.

## Control state carries the actual order

JCB's constructor performs initialization and content preparation before the final orchestration method. Within preparation, admin interpretations and aggregates precede selected deferred work. File processing has its own shared-binding, contextual-binding, custom-code, event, and injection sequence.

The control component $q$ represents those ordering choices. It is not an invented opportunistic scheduler. A language-neutral implementation can encode the sequence using functions and phases, a state machine, or explicit tasks with equivalent prerequisites. [Execution](../compiler/execution.md)

An artifact may exist while some of its stages remain. Let $S(a)$ be its outstanding stage sequence. A write to a skeleton does not imply $S(a)=\langle\rangle$. Completion is determined by the required operations, not by filesystem existence alone.

## External observations are part of effective input

Repository payloads, installed source files, configuration, event-handler behaviour, dates, locale, and filesystem results can affect output. For a comparison, their relevant observations are fixed or explicitly normalized.

Represent the effective invocation by

$$
I=(D_0,\Theta,T,C,H,\xi),
$$

where $\xi$ is the stream of external observations supplied at the corresponding reads. This is an analysis boundary. JCB need not prefetch the entire stream before beginning compilation.

## Proposition: repeatability of a prescribed trace

Assume the initial state is fixed, every operation is deterministic for its state and supplied observation, and the control policy chooses the same next operation from the same state. Then two executions with the same effective input have the same state at every corresponding step and therefore the same selected final observation.

**Argument.** Initial states are equal. If the states at step $i$ are equal, the control policy selects the same operation and the input stream supplies the same observation. Deterministic transition semantics then gives equal states at step $i+1$. Induction establishes equality through the common completion point.

This proposition allows ordered mutation. It does not require operations to commute. A different schedule can produce a different result while each prescribed schedule remains repeatable. [Staging](staging.md)

## Observation and representation independence

Let $S$ be concrete implementation state and $\alpha(S)$ its abstract representation. A correspondence establishes that a concrete operation or finite sequence has the same relevant effect as an abstract transition:

$$
\alpha(S)\xrightarrow{*}\alpha(S').
$$

The star permits concrete housekeeping steps that do not change the selected abstract observation. For example, a database result can be decoded and indexed through several method calls before it is available as one modeled definition.

The source map supplies responsibility-level correspondences for this edition. It is not a machine-checked simulation proof of every method. Another implementation can use different physical representations while testing the same observations at the named boundaries.

## Failure and recovery remain visible

A transition can record a warning, reject a candidate, retain a commented code block, or stop a required operation. The final result is

$$
\operatorname{result}(\tau)=(A,\Delta,\operatorname{status}(q)).
$$

A success flag does not discard diagnostics. An unresolved optional translation and a failed required file write remain distinguishable. This gives the model enough information to describe both JCB's normal generation and its explicit recovery paths.

The following articles specialize this state model for [resolution](resolution.md), [classification](classification.md), [staging](staging.md), and [transport](transport.md).
