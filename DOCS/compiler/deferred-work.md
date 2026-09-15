---
title: Deferred work and staged readiness
description: Remembering operations whose prerequisites are established later, including linked admin views and configuration fieldset passes.
section: Compiler
order: 34
evidence: Infusion secondRunAdmin, linked-view preparation, and configuration fieldsets
---
# Deferred work and staged readiness

Some generation work becomes known before all information needed to finish it is available. JCB records that work and completes it at an appropriate later point. The operation is not forgotten, and the compiler does not have to restart the entire build merely because one relationship depends on later interpretation.

Linked admin views and configuration fieldsets provide concrete examples. They expose the difference between the time a requirement is discovered and the time its output can be completed. [C07](../reference/source-map.md#c07)

## A requirement can be discovered early

While processing an admin view, the compiler can discover that a linked view requires further generation. Information about the other views, names, fields, or related fragments may still be under construction. Completing the linked-view output too early could use an incomplete aggregate or lack the necessary interpretation of the linked target.

The inspected implementation retains deferred admin work in `secondRunAdmin`, grouped by the operation to call and its argument arrays. After the earlier admin and component-content work, Infusion iterates those stored operations and invokes them. This is an explicit replay point in the actual execution sequence.

The architectural unit being retained is therefore not only a value. It is **an operation with the information needed to perform it later**.

## The phase boundary supplies the readiness guarantee

For a deferred operation $w$, define $\operatorname{req}(w)$ as the information it needs. Let $\operatorname{avail}(\Sigma)$ denote information established for the relevant use in state $\Sigma$. Its execution condition is

$$
\operatorname{req}(w)\subseteq\operatorname{avail}(\Sigma).
$$

The mathematical condition describes the dependency. In the source, the orchestrated replay point supplies the intended readiness: the earlier passes have processed the structures on which the later work relies. JCB does not require a generic scheduler that repeatedly tests every arbitrary task until it becomes runnable.

A corresponding language-neutral sequence is:

```text
for each admin-view occurrence:
    establish its local interpretation
    emit immediately available contributions
    retain linked work whose later inputs are not yet complete
complete component-wide admin aggregates
for each retained operation in the defined order:
    complete its linked contribution
continue with the next generation phase
```

This preserves the source's staged organization. A different implementation could use explicit task dependencies, but that would be a representation choice rather than evidence that JCB already uses such a scheduler.

## Configuration fieldsets have a deliberate second pass

Infusion prepares configuration fieldsets earlier and calls the fieldset creator again with its second-pass selector after deferred admin work. It temporarily sets the language target to the admin area for this operation and restores the prior value afterward.

The second call is not an accidental duplicate. It gives the fieldset machinery a point at which information accumulated during the earlier build can participate in completion. Its argument identifies the intended pass. [C07](../reference/source-map.md#c07)

This illustrates a useful distinction: **repeating a selected operation under a later readiness condition** is different from indiscriminately repeating the whole compiler until output stops changing.

## Deferred work, lazy acquisition, and late binding differ

Deferred work postpones an operation. Lazy acquisition obtains a definition when first needed. Late binding substitutes a value when the appropriate output context is available. All involve time, but they solve different problems.

A Power discovered during file processing may require late acquisition. A prepared custom-code block may wait for view-specific placeholders before retrieval. A linked admin-view operation may be queued until other view information is established. Combining them under one word such as *recursion* would hide the actual contracts.

The [acquisition](acquisition.md), [stores](stores.md), and [binding](binding.md) chapters explain the other cases. The complete compiler uses these mechanisms together.

## Ordering remains meaningful

If two retained operations update the same store, their order and update semantics can affect the result. The source's replay order is therefore part of its operation. A mathematical account can establish repeatability for a fixed sequence without claiming that every possible permutation has the same result.

For operations $f$ and $g$, schedule independence would require an appropriate commutation property such as

$$
f(g(\Sigma))=g(f(\Sigma)).
$$

Where that property has not been established, the specified order remains the contract. The white paper does not confuse deterministic orchestration with unrestricted confluence.

## Why this mechanism matters

Deferred work allows the compiler to preserve locality of discovery without demanding premature completion. The code that recognizes a relationship can record what must be done; a later stage can complete it once the broader context exists. Intermediate state carries the connection across that interval.

This is one of the clearest examples of the architecture's “remember now, use later” behaviour. Its value lies in the explicit relationship between identity, stored arguments, prerequisite information, and the point of consumption—not in the mere existence of another loop.

The [formal staging model](../formal/staging.md) and [reference mechanisms](../engineering/reference-model.md) make the same distinction executable on a small example.
