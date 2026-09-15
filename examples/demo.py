#!/usr/bin/env python3
"""Run the white paper's small executable mechanism traces. MIT."""
from __future__ import annotations
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from reference.architecture import (Contribution, Definition, DeferredWork, EntityKey,
    FieldDefinition, FieldUse, Repository, apply_contributions, classify_field,
    complete_deferred, ordered_replace, portable_projection, resolve_graph, select_property)


def main() -> None:
    field = EntityKey("field", "guid", "75e830a6-a3a5-4327-9161-3f774a6f1591")
    field_type = EntityKey("fieldtype", "guid", "201327fe-3067-4316-a155-3fe2a52e05c0")
    repository = Repository("example", {
        field: Definition(field, {"name": "greeting"}, (field_type,)),
        field_type: Definition(field_type, {"name": "Text"}),
    })
    resolution, _ = resolve_graph([field], {}, [repository])
    memory = apply_contributions({}, classify_field(
        FieldDefinition(field, "greeting", "Greeting"),
        FieldUse("helloworld", "greeting", title=True, searchable=True, sortable=True),
    ))
    pairs = [("A", "B"), ("B", "x")]
    deferred = complete_deferred([
        DeferredWork("linked_output", frozenset({"view_names"}),
                     lambda state: " -> ".join(state["view_names"]))
    ], {"view_names": ["greeting", "greetings"]})
    design = {"id": 17, "guid": field.value, "fields": ["greeting", "alias"]}
    result = {
        "resolution": {"attempted": [key.value for key in resolution.attempted],
                       "successful": resolution.successful},
        "greeting": memory,
        "binding": {"ordinary": ordered_replace("A", pairs),
                    "filtered": ordered_replace("A", pairs, 3),
                    "filtered_with_both_keys": ordered_replace("A B", pairs, 3)},
        "precedence": select_property({"table": 0, "xml": 50}),
        "deferred": deferred,
        "portable": portable_projection(design, ["guid", "fields"]),
        "effect_order": apply_contributions({}, [Contribution("code", "body", "concat", "first"),
                                                  Contribution("code", "body", "concat", " second")]),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
