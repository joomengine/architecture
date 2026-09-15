---
title: The module and plugin contexts
description: Following module fields and code and a context-named plugin from portable definitions into distinct native extension structures.
section: Worked Examples
order: 63
evidence: Hello World component associations, module/plugin payloads, and generated extension repositories
---
# The module and plugin contexts

Hello World's component blueprint links a Site Redirect module and a Privacy plugin. Both are represented as their own definitions. They share the acquisition and compilation infrastructure while receiving extension-specific names, namespaces, language contexts, manifests, and generated files.

The example demonstrates that context is not limited to switching between two forms inside one component. It also selects how a definition becomes a different kind of deployable product. [Extension generation](../generation/extensions.md)

## The module supplies intent and authored behaviour

The module identity is `21c9f6f5-3193-485d-94e7-f9c789a9fa2e`, with name `SiteRedirect`. Its configuration references the Redirect field `12035b51-753b-4e3f-9f41-cde3a6046286`. That field in turn connects to the represented groups and URL controls used by the configuration structure.

The module's authored code reads the configured redirect entries, obtains user groups, compares them with the selected groups, and performs the corresponding redirect. It also invokes the selected module layout through a Joomla Power reference and a module-name placeholder. [Module payload](https://github.com/vast-development-method/hello-world-blueprint/blob/5802e7c1d9bfaac005c765ccda830a7d07cd7e12/src/joomla_module/21c9f6f5-3193-485d-94e7-f9c789a9fa2e/item.json)

These are two kinds of input: a structured field/configuration graph and an explicitly authored operation. The compiler does not invent the redirect business rule. It provides the target's extension structure, resolves the selected references, constructs field configuration, and places the authored rule in that structure.

## Its output is a native module tree

The pinned [module product](https://github.com/vast-development-method/hello-world-joomla-module/tree/20be318a6163e253c2a9803434622467d6006709) contains `src/Dispatcher/Dispatcher.php`, `services/provider.php`, `tmpl/default.php`, `mod_siteredirect.xml`, language files, installer code, and supporting directories.

The target-specific module infuser supplies the provider and dispatcher arrangements. Fieldset generation supplies the configuration representation. Language handling provides the selected module labels and messages. Placeholder and Joomla Power processing resolve the template's and authored code's platform references.

The module version stored in its definition is its own extension version; it is not the Joomla generation target. Those two values must not be conflated when examining the payload.

## The plugin's name is completed by its use

The plugin identity is `8aa96d76-94e3-47d1-8dd8-f430b72ed0f7`. Its name property is `[[[Component]]]`, not a permanently fixed Hello World name. The component context supplies that placeholder when the plugin is generated.

The plugin references its group, base-class information, three methods, and three properties through typed dependency descriptors. Its portable definition therefore includes both reusable class structure and a context-sensitive naming decision. [Plugin payload](https://github.com/vast-development-method/hello-world-blueprint/blob/5802e7c1d9bfaac005c765ccda830a7d07cd7e12/src/joomla_plugin/8aa96d76-94e3-47d1-8dd8-f430b72ed0f7/item.json)

In the [generated plugin](https://github.com/vast-development-method/hello-world-joomla-plugin/tree/6a785145ee84212fec65a53b7c6c362ab0f8b408), the corresponding files include `src/Extension/Helloworld.php`, `services/provider.php`, `helloworld.xml`, language material, and installer code.

This is a direct instance of

$$
\operatorname{name}(d,\Gamma_{\mathrm{HelloWorld}})
=\mathrm{Helloworld}.
$$

The exact case follows the naming rule of the selected output role. The portable identity does not change merely because a name is specialized for this occurrence.

## Context is established before content is assembled

Module and plugin infusers set their own build area, language target, and prefix before generating their content. They prepare their corresponding shared/contextual placeholder maps and select target-specific architecture services.

The same generic string can therefore be inappropriate in two contexts even where both outputs belong to one overall build. A module label must not accidentally inherit the component's prefix. A plugin class must use its plugin namespace and group conventions. A file-local Power alias is resolved within the imports of that particular file.

These relationships explain why reusable intermediate stores require explicit scope and a defined lifecycle. They are not incidental bookkeeping around an otherwise context-free template.

## Product identity and blueprint identity stay separate

The component's module and plugin association records describe which definitions participate in the product family. Each resulting extension tree has its own installation identity and archive path. A changed association, target rule, field definition, or reusable method can consequently affect different parts of that family.

The compiler maintains the connection between the model and those outputs. The generated application code does not require JCB to be installed alongside every deployed product, except for dependencies explicitly selected by the design.

The [accounting chapter](accounting.md) counts these products separately, and the [formal model](../formal/classification.md) represents their shared definitions and distinct occurrences without assigning a one-definition-to-one-file rule.
