---
title: The Greeting field across the compiler
description: A stable field identifier, its contextual association, and the derived form, schema, index, language, list, and metadata outputs.
section: Worked Examples
order: 61
evidence: Exact blueprint properties and corresponding generated files
---
# The Greeting field across the compiler

The Greeting field is a compact example of contextual compilation. Its definition does not explicitly contain a form file, SQL statement, list header, sort option, language catalogue, or table metadata class. It supplies properties which, together with its view association and compiler rules, produce those coordinated artifacts.

The field's portable identifier is **`75e830a6-a3a5-4327-9161-3f774a6f1591`**. The admin view using it is **`65116558-be67-4931-95be-727fbfb16db7`**. [Definition](https://github.com/vast-development-method/hello-world-blueprint/blob/5802e7c1d9bfaac005c765ccda830a7d07cd7e12/src/field/75e830a6-a3a5-4327-9161-3f774a6f1591/item.json)

## The reusable definition

The field selects a text field type, the logical name `greeting`, and the label `Greeting`. Its database properties describe `VARCHAR` with length 255, nullable storage, and no explicit index selection. Its XML properties include a displayed size of 10, a maximum input length of 50, and the default text `Some text`.

Database width, form width, maximum input length, and form default are different decisions. The compiler does not need to flatten them into one generic “field size.” The distinction remains visible in the generated artifacts.

The field type is another identified definition, `201327fe-3067-4316-a155-3fe2a52e05c0`, supplied through the field-type distribution mechanism. Its identity is not the identity of this particular Greeting field.

## The occurrence adds its roles

The [admin-fields association](https://github.com/vast-development-method/hello-world-blueprint/blob/5802e7c1d9bfaac005c765ccda830a7d07cd7e12/src/admin_view/children/65116558-be67-4931-95be-727fbfb16db7/admin-fields.json) supplies:

```json
{
  "field": "75e830a6-a3a5-4327-9161-3f774a6f1591",
  "list": "1",
  "order_list": "1",
  "title": "1",
  "sort": "1",
  "search": "1",
  "link": "1",
  "tab": "1",
  "alignment": 1,
  "order_edit": "1"
}
```

This is the use of the field in the Greeting view. The view maps its first tab to `Details`. The component supplies the extension name and language prefix. The target supplies the emitted Joomla conventions.

In the formal vocabulary, the field is $d$, the association is an occurrence $o$, and those surrounding values form $\Gamma(o)$. The generated contributions are $J(d,\Gamma(o))$.

## The generated projections

| Concern | Observed result | Output location |
| --- | --- | --- |
| Database column | `greeting VARCHAR(255)`, nullable with the emitted default | `admin/sql/install.mysql.utf8.sql`, line 8 |
| Database index | Ordinary `idx_greeting` key | Same SQL file, line 25 |
| Editor | Text field named `greeting`, maximum 50, default `Some text` | `admin/forms/greeting.xml`, lines 120–138 |
| Language | `COM_HELLOWORLD_GREETING_GREETING_LABEL` maps to `Greeting` | Administrator language catalogue |
| List sorting | The header and sort choices refer to the resolved `a.greeting` column and label | `admin/tmpl/greetings/default_head.php`; Greetings view class |
| Table metadata | Same GUID, title status, list `greetings`, tab `Details`, `VARCHAR(255)`, ordinary key | `libraries/jcb_powers/JCB.Joomla/src/Helloworld/Table.php`, lines 73–96 |

Inspect the [form](https://github.com/vast-development-method/hello-world-joomla-component/blob/a81c0dd8b8f41905671a86796a3e5995685fdaba/admin/forms/greeting.xml#L120-L138), [SQL](https://github.com/vast-development-method/hello-world-joomla-component/blob/a81c0dd8b8f41905671a86796a3e5995685fdaba/admin/sql/install.mysql.utf8.sql#L1-L30), and [table metadata](https://github.com/vast-development-method/hello-world-joomla-component/blob/a81c0dd8b8f41905671a86796a3e5995685fdaba/libraries/jcb_powers/JCB.Joomla/src/Helloworld/Table.php#L73-L96). The related administrator and site outputs share the interpreted model through their selected generation paths.

## Why an index appears without an explicit index request

The isolated field has its explicit index setting at zero. Its association makes it the title field. In the applicable non-text schema branch, the compiler gives title, alias, and category roles an ordinary index where a unique-key selection does not take precedence.

For this occurrence:

$$
\mathrm{explicitIndex}=0,\quad \mathrm{title}=1,\quad
\mathrm{textFamily}=0
\quad\Longrightarrow\quad\mathrm{ordinaryKey}=1.
$$

This is not unexplained extra code added by a template. It is a derived consequence of the field's contextual role, retained for both SQL and metadata emission. The [schema chapter](../generation/schema.md) gives the branch structure and source correspondence.

## Names are completed in context

The blueprint's label `Greeting` becomes an extension- and view-qualified language key. The list query refers to the field under its source alias. The table metadata carries its portable GUID and role information. These representations differ because they serve different consumers, while still tracing back to the same identified use.

A reimplementation can use different syntax for the SQL, form description, or language catalogue. It should retain the relationship between the common field decision and each emitted projection.

## The architectural observation

A field does not become important by producing many lines. It becomes architecturally interesting when one represented decision must remain coherent across independent runtime concerns. Here the compiler coordinates storage, input, labels, listing, sorting, and generated metadata through retained intermediate interpretations.

The example is small enough to inspect completely and broad enough to show why the central operation is semantic classification rather than simple copying. [Classification](../compiler/classification.md), [Formal classification](../formal/classification.md)
