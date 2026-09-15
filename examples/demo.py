"""A complete synthetic two-component build and admitted-edit round trip.

Run from the repository root: python examples/demo.py
No Joomla installation, external packages, or network access is required.
SPDX-License-Identifier: MIT
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from reference.vdmt import Artifact, Fact, Knowledge, Resolution, Rule, artifact_map, bind, extract_regions, gather, manifest, put_regions, reconcile, saturate


COMPONENTS = {'CRM': ('contact', 'subscription'), 'Portal': ('contact',)}
VIEWS = {'contact': ('title', 'email', 'status'), 'subscription': ('email', 'status')}
FIELDS = {'title': 'Text', 'email': 'Text', 'status': 'Choice'}


def build(memory: dict[str, str] | None = None) -> tuple[dict[str, str], dict[str, int]]:
    source: dict[str, Resolution] = {}
    for name, views in COMPONENTS.items():
        source['component:' + name] = Resolution((Fact(('component', name), name),), tuple('view:' + v for v in views))
    for name, fields in VIEWS.items():
        source['view:' + name] = Resolution((Fact(('view', name), name),), tuple('field:' + f for f in fields))
    for name, kind in FIELDS.items():
        source['field:' + name] = Resolution((Fact(('field', name), kind),), ('type:' + kind,))
    for kind in sorted(set(FIELDS.values())):
        source['type:' + kind] = Resolution((Fact(('type', kind), kind),))
    closed = gather(('component:CRM', 'component:Portal'), source)
    rules: list[Rule] = []
    occurrences = 0
    for owner, views in COMPONENTS.items():
        for view in views:
            for field in VIEWS[view]:
                occurrences += 1
                rules.append(Rule(owner + '/' + view + '/' + field,
                    (Fact(('field', field), FIELDS[field]), Fact(('type', FIELDS[field]), FIELDS[field])),
                    (Fact(('occurrence', owner, view, field), FIELDS[field]),)))
    knowledge = Knowledge(saturate(closed.facts, rules))
    planned: list[Artifact] = []
    defaults: dict[str, str] = {}
    for owner, views in COMPONENTS.items():
        for role in ('manifest', 'permissions', 'index'):
            path = f'{owner}/{role}.txt'
            planned.append(Artifact(path, path, bind('{{OWNER}} / {{ROLE}}\n', ({'OWNER': owner}, {'ROLE': role}))))
        for view in views:
            values = ', '.join(field + ':' + knowledge.get(('occurrence', owner, view, field)) for field in VIEWS[view])
            for role in ('model', 'controller', 'form', 'language'):
                path = f'{owner}/{view}/{role}.txt'
                region = path + '/custom'
                body = bind('{{OWNER}} / {{VIEW}} / {{ROLE}}\n{{FIELDS}}\n',
                            ({'OWNER': owner}, {'VIEW': view, 'ROLE': role, 'FIELDS': values}))
                body += f'<!-- VDMT:BEGIN {region} -->\n<!-- VDMT:END {region} -->\n'
                defaults[region] = ''
                planned.append(Artifact(path, path, body))
    if memory is not None and set(memory) != set(defaults):
        raise ValueError('The demo requires a complete editorial region map.')
    selected = defaults if memory is None else memory
    outputs = []
    for item in planned:
        regions = extract_regions(item.content)
        outputs.append(Artifact(item.identity, item.path, put_regions(item.content, {k: selected[k] for k in regions})))
    return artifact_map(outputs), {'requests': len(closed.completed), 'field_definitions': len(FIELDS),
        'field_occurrences': occurrences, 'view_occurrences': sum(map(len, COMPONENTS.values())), 'artifacts': len(outputs)}


def demonstration() -> dict:
    first, counts = build()
    baseline = {key: value for content in first.values() for key, value in extract_regions(content).items()}
    desired = dict(baseline)
    chosen = 'CRM/contact/model.txt/custom'
    desired[chosen] = 'Human adaptation retained.\n'
    edited = {path: put_regions(content, {key: desired[key] for key in extract_regions(content)})
              for path, content in first.items()}
    captured = {key: value for content in edited.values() for key, value in extract_regions(content).items()}
    accepted = reconcile(baseline, baseline, captured)
    second, _ = build(accepted)
    recovered = {key: value for content in second.values() for key, value in extract_regions(content).items()}
    assert recovered == desired
    return {'kind': 'synthetic reference demonstration, not a JCB benchmark', 'counts': counts,
            'round_trip_preserved': recovered == desired, 'manifest': manifest(second)}


if __name__ == '__main__':
    print(json.dumps(demonstration(), indent=2, ensure_ascii=False))
