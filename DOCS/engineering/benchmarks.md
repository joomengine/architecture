---
title: Benchmark protocol and reported scale
description: Preserving the author's performance report while specifying a reproducible, controlled evaluation.
section: Engineering
order: 76
evidence: Author report and experimental protocol
---
# Benchmark protocol and reported scale

## The reported observation

Llewellyn reports a representative build that transforms approximately **30,000 lines of source/database-associated information into 1.3 million generated lines in about 60 seconds**. This edition retains that account as an author-reported observation. It was not independently reproduced in a live JCB environment for this paper.

Simple arithmetic gives an apparent output/input line ratio of about **43.3** and an output rate of about **21,667 lines per second**. Those figures are derived from the reported inputs; they are not additional measurements and do not establish causation or optimality.

## Define the measurement boundary

Record the exact JCB commit, Joomla/PHP versions, operating system, CPU, memory, storage, database version and placement, configuration, template revisions, powers, custom-code records, and external dependencies. Identify whether time includes extraction, acquisition, compilation, validation, packaging, repository synchronization, and network transfer.

Define a line consistently. Distinguish physical lines, nonblank lines, logical statements, database rows, encoded source snippets, and generated/copied files. Record bytes as well as lines. The inspected writer's newline counter is useful operational data but not a substitute for an independent final-artifact inventory. [J07](../reference/bibliography.md#j07)

## Reproducible procedure

Use a redistributable fixture or a private fixture with a published schema, generator, and hashes that permit an equivalent test. Freeze the source and environment. Run an untimed validation build, then a declared number of timed repetitions in fresh output directories.

Separate cold and warm conditions. Randomize the order of compared implementations to reduce drift. Record every run, including failures and outliers, and report the median, dispersion, sample count, and raw data rather than only the fastest run.

A warm database buffer, filesystem cache, or dependency cache must not be presented as a cold-start result.

## Comparators and ablations

Compare at least a direct per-occurrence acquisition design, a shared-definition design, and a staged context-sensitive design producing equivalent outputs. Hold templates, validation, and packaging policy constant.

Ablate one mechanism at a time: source caching, derived-fragment caching, batching, late binding, or output buffering. This helps distinguish the effect of the architecture from template size, library copying, database locality, and implementation-language overhead.

## Scaling dimensions

Vary definition count, occurrence fan-out, dependency depth, field/view breadth, editable-region count, artifact count, and output bytes independently where possible. Include low-reuse and high-reuse workloads. A design that excels at high fan-out may be wasteful for one small artifact.

Measure elapsed time, CPU time, peak memory, query count, acquired bytes, cache behavior, output bytes, and validation failures. Retain manifests to establish output equivalence before comparing speed.

## Publication of results

Store machine-readable run records with the implementation revision and input hashes. Report hardware and software changes between series. Do not convert a reference-model microbenchmark into a claim about the full JCB compiler.

This repository's executable example is a contract demonstration, not a synthetic recreation of the million-line claim. A future benchmark publication can add measured results without changing the historical author report into something it was not.
