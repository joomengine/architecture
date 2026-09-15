---
title: Language keys and multilingual output
description: Contextual key construction, source-string collection, translation reuse, target catalogues, and inclusion policy.
section: Generation
order: 44
evidence: Language service, extractor, translation state, file generation, and Hello World labels
---
# Language keys and multilingual output

A generated label has two connected representations: a key inserted into code or markup, and a value stored in an appropriate language catalogue. JCB prepares both while interpreting the application model. The same field can contribute labels to form, list, filter, and other output roles.

Language processing is therefore a cross-artifact coordination problem. A form's reference and a catalogue's entry must agree on identity and scope even though they are emitted at different points. [C15](../reference/source-map.md#c15)

## Context supplies the key namespace

The compiler's language prefix and current target distinguish component, module, plugin, administrator, site, and related output areas. Field and view interpretation constructs role-specific keys from those settings and the represented names or source strings.

Hello World's Greeting label becomes `COM_HELLOWORLD_GREETING_GREETING_LABEL`. The generated form and list material refer to that key, and the language file supplies `Greeting` as its value. The original field description need not repeat the fully qualified language key at every use. [Field trace](../examples/field-trace.md)

For a label source $s$, role $r$, and context $\Gamma$, write

$$
k=\operatorname{languageKey}(s,r,\Gamma),\qquad
L[\operatorname{area}(\Gamma),k]=\operatorname{normalize}(s).
$$

The key-construction function and destination area are both part of the interpretation.

## Collection is shared, but destination remains explicit

The language service stores content by target and key. Its ordinary keyed setter fills an empty entry rather than blindly overwriting every previously established value. An explicit target setter can replace a whole target collection. String normalization trims content and, when configured, removes line breaks.

These are concrete update policies, not a general conflict-resolution engine. A reimplementation should state whether an entry is first-established, replaced, merged, or rejected when the same key is supplied again. [C15](../reference/source-map.md#c15)

The compiler also extracts supported language references and source strings from custom content. Code preparation can consequently produce language contributions while it discovers custom-code and Power dependencies. A value that appears to be “just code” can affect several later products.

## Reusable translations connect source strings to targets

The multilingual services retrieve existing translation records and map available translations into the language output collections for the current extension and area. They update or insert source-string records and maintain their association with components, modules, or plugins.

The source string, its translated values, and the emitted placeholder key are related but distinct identities. A translation record can be reused where the same source string participates in another generated context, while each output still uses the appropriate extension-specific key.

The inspected language-maintenance path also updates relationships and handles strings no longer linked to the current target. This work occurs in local design/translation data; generated language files are later products of that maintained information. [C15](../reference/source-map.md#c15)

## Translation completeness controls file inclusion

The translation checker compares a non-source language's available string count with the source-language total. Its configured percentage threshold determines whether that language file is included, with a selected debug mode affecting the threshold path. Inclusion and exclusion are reported through language messages.

For a nonempty source catalogue of size $N$ and an available translated count $n_\ell$, the comparison uses

$$
p_\ell=100\frac{n_\ell}{N}.
$$

This is an inclusion policy for generated language material, not an automatic translation process. The source language and translation records remain explicit inputs. [C15](../reference/source-map.md#c15)

## Language changes follow generation context

Module and plugin infusers establish their own language targets and prefixes before generating provider, dispatcher, extension, template, fieldset, and manifest content. Shared custom code can be processed for multiple areas where the selected path requires it.

A language prefix must therefore be correct at the time the relevant contribution is generated. Applying an unrelated component prefix to a plugin's labels would be a context error even if every string replacement completed successfully. [Context](../foundations/context.md), [Extensions](extensions.md)

## Diagnostics are part of the result

The final compiler phases write language data and report inclusion, exclusion, and mismatch information. These messages help distinguish a successfully generated application tree from a complete translation set for every language.

The mathematical model treats those messages as output observations alongside the language files. It does not hide a missing translation behind an undifferentiated successful-build flag. [Events and effects](../compiler/events.md)

## The reusable principle

Another compiler can adopt the same separation: collect source strings during semantic interpretation, assign context-qualified keys, reuse translation records, apply explicit destination and completeness policy, and emit both references and catalogues from the coordinated state.

The mechanism is valuable because language support is generated with the application's fields, actions, and views rather than added independently afterward. It is another concrete example of one design decision producing several mutually dependent artifacts.
