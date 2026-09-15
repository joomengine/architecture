---
title: Custom code, dispensers, and recovery
description: Prepared code, reusable references, external resources, GUI-linked regions, and fingerprint-based placement across regeneration.
section: Compiler
order: 36
evidence: Customcode pipeline, Dispenser, Gui, Extractor, External, Reverse, and compiler placement
---
# Custom code, dispensers, and recovery

JCB combines structured generation with explicitly authored code. A developer can place code in defined GUI areas, refer to reusable custom-code records, include selected external material, or preserve designated modifications in installed output. These paths meet the compiler at different points and retain different kinds of identity.

The architecture does not treat custom code as an unstructured exception pasted onto the end of a generated application. It prepares, indexes, contextualizes, and places that code through services connected to the same build state used by the generators. [C09](../reference/source-map.md#c09)

## Preparation and later retrieval

The dispenser's setter can decode stored content, process custom and external references, add GUI-linked markers, process dynamic hashing and encoded-string conventions, and retain the resulting script under role and use-site keys. Its update policy can replace or append content.

Retrieval is a later operation. The dispenser applies the currently active placeholders, adds requested prefix, note, and suffix material, and can remove the stored entry after consumption. A fragment can consequently be prepared before all destination-specific names are fixed.

Write this as

$$
q=\operatorname{prepare}(c,\kappa),\qquad
M[r,o]\leftarrow q,
$$

$$
c'=\operatorname{decorate}(\sigma(q,P_\Gamma),\eta).
$$

Here $\kappa$ selects preparation options, $(r,o)$ identifies role and occurrence, $P_\Gamma$ is the retrieval-time environment, and $\eta$ selects surrounding material. The state update and later interpretation are separate responsibilities.

## Reusable custom-code records

A custom-code reference can identify a record by numeric ID or function-name alias. The service retains resolved alias-to-ID information and supports argument-bearing references. It loads the selected code and substitutes it according to the configured convention.

Hello World's README design refers to `readMEcontributors`. Its portable identity is the function name, and its generated contribution appears inside the final README rather than in an executable class. That example demonstrates that the same code-distribution machinery can contribute to documentation as well as runtime source. [Custom-code trace](../examples/custom-code-trace.md)

The custom-code update sequence processes external content, reusable custom-code references, language extraction, and discovery of Power and Joomla Power references. Expansion can therefore expose further dependencies that join the compiler's existing acquisition and injection paths.

## GUI-linked regions retain a local editing address

When marker generation is enabled and the required configuration is present, GUI code can be wrapped with a marker identifying its table, property, and local record ID. These addresses allow subsequent recovery to reconnect an edited region to the corresponding GUI-backed value.

A GUI marker is a local recovery address. Its numeric record component need not be identical in two installations containing equivalent portable blueprints. The field or view GUID and the GUI region's local address serve different purposes. [Identity](../foundations/identity.md)

The public examples deliberately place recognizable comments in several GUI code areas. The generated outputs show those comments at the intended model, controller, view, or installer locations. Their trace is stronger than a generic claim that “custom code is supported,” because it connects a particular stored property to its actual consumer.

## Recovery precedes the new build's reset

The initializer invokes custom-code extraction before rebuilding the component and resetting the build directory. The extractor scans eligible file types in active installed targets, recognizes its marker families, delegates GUI-region recovery, and captures code together with location information and surrounding fingerprints.

Captured content is reverse-transformed where required before being stored back in local records or update buffers. This can restore reusable placeholder forms rather than preserving only the fully specialized names from the previous output. The exact marker family and reverse operation determine the representation retained. [C01](../reference/source-map.md#c01), [C09](../reference/source-map.md#c09)

This path differs from installed-component extrusion. Recovery follows designated code addresses established by the generation workflow; extrusion analyzes a broader set of artifacts to reconstruct candidate definitions. [Extrusion](../extrusion/overview.md)

## Placement includes an explicit recovery fallback

Stored custom-code placement uses recorded location context and fingerprints to find an insertion or replacement position in newly generated files. When the surrounding structure still matches, the code can be placed at that position despite changes elsewhere in the file.

If the required context cannot be matched in an existing target file, the compiler invokes its escaped-code path: it retains the code as commented material and emits a warning naming the file and recorded location. The developer can reposition the code, remove the comments, and compile again. A missing target file has a separate diagnostic path. [C09](../reference/source-map.md#c09)

The mechanism distinguishes automatic executable placement from recoverability. It avoids treating an uncertain location as permission to execute a fragment in an arbitrary place. The fallback is part of the operational design, not an undefined failure outside the model.

## External resources have their own acceptance policy

An explicit external-code reference identifies a URL or local path and can specify a line-cutting convention. The service caches fetched content within the active operation and compares its hash with recorded history.

In the inspected implementation, new or changed external content requires administrative authorization. Authorized acceptance updates the recorded hash and emits a notice; an unauthorized new or changed resource is excluded with an error. This is change detection and acceptance policy. The hash is not a digital signature or proof that the source is safe. [C09](../reference/source-map.md#c09)

This path is distinct from importing a managed entity through a repository index. The identity is a resource reference, and the acceptance decision concerns its content history.

## The preservation relation is bounded and explicit

For an admitted marker structure, recovery can be described as a partial extraction function

$$
X:A\rightharpoonup M,
$$

where $A$ is an artifact collection and $M$ the recovered designated code. Marker identity, supported syntax, reverse transformation, and target availability define the domain.

A round-trip law must name the representation being preserved. Exact body equality is appropriate only when no intervening transformation changes the body. Where generation specializes placeholders and recovery reverses them, equality concerns the corresponding canonical code representation. [Formal transport](../formal/transport.md)

The useful capability is a controlled path for authored decisions to re-enter regeneration. It operates alongside declarative model changes, dependency reuse, and target-aware generation, while the compiler remains the coordinating centre.
