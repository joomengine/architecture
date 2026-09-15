---
title: Falsifiable hypotheses and experiments
description: Controlled tests of reuse, context isolation, editorial stability, incremental correctness, and memory orchestration.
section: Research
order: 91
evidence: Experimental proposals
---
# Falsifiable hypotheses and experiments

## H1 — reuse reduces repeated acquisition on high-fan-out tasks

**Prediction:** for output-equivalent workloads with repeated definitions and expensive acquisition, sharing definition-level results reduces acquisition count and elapsed time relative to per-occurrence acquisition, until lookup and storage overhead dominate.

**Test:** vary reuse count and acquisition latency independently while holding emitted bytes and validation constant. Measure queries, CPU, memory, and wall time. Include low-reuse cases. A result showing no gain or a slowdown in the proposed favorable regime weakens the hypothesis or exposes a faulty cost model.

## H2 — explicit occurrence context reduces cross-scope errors

**Prediction:** implementations whose keys include the relevant owner, target, and occurrence dimensions produce fewer incorrect cross-context substitutions than a definition-only cache under deliberately varied contexts.

**Test:** generate shared definitions with different occurrence overrides and target versions. Compare results against a clean uncached interpreter. The principal outcome is correctness, not only speed. One cross-owner leak falsifies a universal isolation claim for the tested implementation.

## H3 — admitted edits survive regeneration under a stable region contract

**Prediction:** for artifacts satisfying the region grammar and unchanged region identities, extraction followed by regeneration preserves the canonical edited bodies.

**Test:** generate valid region maps, render, edit admitted bodies, extract, reconcile, and render again. Include empty bodies and Unicode. Separately test malformed markers and region migrations; they should produce declared failures or migration outcomes, not silent data loss.

This hypothesis tests an implementation of the formal law. The conditional proof does not excuse an implementation failure.

## H4 — complete dependency invalidation matches clean rebuilding

**Prediction:** an incremental implementation with complete dependency tracking produces the same normalized artifact map as a clean rebuild after changes to data, templates, rules, target settings, and editorial memory.

**Test:** mutate one input category at a time, including deletion and alternative derivations. Compare manifests. Any unexplained mismatch identifies an incomplete dependency record, incorrect recomputation, or a deficient equivalence definition.

## H5 — structured external memory improves bounded AI tasks

**Prediction:** on tasks requiring repeated use of changing, attributed evidence, scoped memory with dependency-aware revision reduces stale or unsupported answers compared with a fixed-context or unversioned retrieval baseline at comparable resource budgets.

**Test:** use held-out tasks, controlled source changes, authorized corrections, and blinded assessment. Measure answer quality, evidence accuracy, stale-memory rate, retrieval work, and context size. Include adversarial source instructions. A benefit on one task family does not establish general intelligence or psychological equivalence.

## H6 — self-generation is stable for an identified model

**Prediction:** successive generated JCB instances, given the same complete model and environment, produce equivalent later-stage outputs under a declared normalizer.

**Test:** execute the [self-build protocol](../jcb/self-build.md), retaining every input and artifact manifest. A mismatch must be explained rather than removed by an overly broad normalizer.

## Optimality is a separate problem

To claim an optimum, specify the workload class, admissible algorithms, objective, resource constraints, and correctness relation. A theorem may establish a lower bound within a restricted model; an experiment may show that an implementation approaches it on sampled workloads. Neither supports the unrestricted statement “the best possible memory design.”

The immediate research objective is narrower and productive: identify which contracts improve correctness and which mechanisms improve resource use under reproducible conditions.
