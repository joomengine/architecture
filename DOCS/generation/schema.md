---
title: Schemas, storage, and update history
description: Field persistence, normalized database properties, derived keys, storage transformations, generated metadata, and migration contributions.
section: Generation
order: 40
evidence: Field builders, history models, SQL update state, and Hello World output
---
# Schemas, storage, and update history

A field's database description is one projection of its design. The compiler decides whether the occurrence is persisted, normalizes its type and default information, derives index requirements, and retains the result for SQL and metadata generation. The same field can also produce form and runtime storage logic.

The schema is therefore coordinated with the application model rather than authored as an unrelated second description. [C05](../reference/source-map.md#c05), [C13](../reference/source-map.md#c13)

## Persistence is an occurrence decision

The field builder determines whether a field participates in database storage from the configured use. The inspected non-database mode bypasses schema contributions while still allowing the field to participate in the relevant interface behaviour.

A field definition and a column are consequently different objects. A spacer, display-only field, or deliberately non-persisted control need not create a database column simply because it has a field identity.

Write the persistence decision as $p(d,o)\in\{0,1\}$. A schema contribution exists only when the selected type and occurrence rules require it:

$$
C_{\mathrm{schema}}(d,o)=
\begin{cases}
\operatorname{column}(d,o), & p(d,o)=1,\\
\varnothing, & p(d,o)=0.
\end{cases}
$$

The empty contribution does not erase the other possible contributions of the field.

## Normalization precedes emission

The builder records datatype, length, default, nullability, local and portable identity, and key-related information. Numeric defaults are normalized according to the implemented numeric type rules. Text/blob families follow a different length and default path from ordinary length-bearing columns.

The intermediate description is consumed by SQL generation and by the component-field metadata builder. The latter combines type and length into a normalized database type and retains properties such as key and unique-key status. [C05](../reference/source-map.md#c05), [C22](../reference/source-map.md#c22)

This is an example of two emitters consuming a shared interpretation. The SQL and metadata output should reflect the same normalized column decision, even though their syntax differs.

## Key requirements can be derived from a field's role

The Greeting field's blueprint sets its explicit index option to zero, yet the generated table has an index for that column. The reason is visible in the builder: a non-text field used as a title, alias, or category can require a normal key even when the field definition did not independently request one. Hello World's field association marks Greeting as the title. [Field trace](../examples/field-trace.md)

For the inspected branch, let $x$ mean an excluded text/blob family, $i$ the explicit index selector, and $a$, $t$, $c$ the alias, title, and category roles. The selected key kind is

$$
\operatorname{keyKind}=
\begin{cases}
\mathrm{unique}, & \neg x\land i=1,\\
\mathrm{ordinary}, & \neg x\land i\ne1\land(i=2\lor a\lor t\lor c),\\
\mathrm{none}, & \text{otherwise}.
\end{cases}
$$

The equation preserves the branch precedence. It explains a generated consequence that is not obvious from the field's isolated JSON record. The occurrence settings and compiler rule supply the missing context.

## Storage treatment spans save and load paths

Fields can select storage treatments such as JSON representation, encoded strings, or configured encryption/custom processing. Classification records which fields require each treatment. Later model-generation operations consume those builders when preparing save and retrieval logic.

The architectural requirement is coordination: a representation written by one path must be interpreted appropriately by the corresponding read path. A storage selector therefore affects more than the database column declaration. It can require imports, helper services, initialization fragments, and permission-sensitive handling of omitted values. [C05](../reference/source-map.md#c05), [C14](../reference/source-map.md#c14)

The paper describes those generated responsibilities without equating an encoding option with a security guarantee. The concrete selected implementation determines the actual transformation.

## History generates migration information

The history/modeling services compare selected previous and current component, view, and field-related information. New associations and changed properties contribute to update-SQL state. The update service handles supported old repeatable and newer subform representations and records additions or old/new values under identified keys.

The compiler later uses those contributions to prepare update artifacts. Recording a schema change during compilation is distinct from executing the migration against a deployed application's database. Installation and update processing consume the generated artifacts at a later lifecycle stage. [C13](../reference/source-map.md#c13)

The relevant relation is a supported design delta:

$$
\delta=\operatorname{compare}(D_{\mathrm{previous}},D_{\mathrm{current}}),
\qquad U=\operatorname{emitUpdate}(\delta,T).
$$

The domain of `compare` is the set of properties and relationships handled by the implementation. It is not a general semantic differencer for arbitrary external databases.

## Generated metadata reconnects output to design

JCB emits a component-field map containing field identity, label, type, title status, list, storage treatment, tab, database properties, and represented links. Hello World's generated Table class contains this map alongside the runtime application.

That metadata makes parts of the design explicit in the product and provides useful input to tools that inspect or recover structure. It is one reason the architecture's forward and reverse paths can share vocabulary. [Extrusion analysis](../extrusion/analysis.md)

The resulting maintenance mechanism combines portable intent, normalized schema decisions, history-derived updates, and complete generated application code. A change is represented once and propagated through the concerns that the compiler knows depend on it.
