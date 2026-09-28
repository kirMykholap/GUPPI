---
type: estimate
kind: QA
status: pending
target: "[[rule-materialize]]"
purpose: A create of a category whose schema rule the same unit creates or updates is lifted with every key into fields and no unknown; a unit without that entry is lifted by the schema on disk
method: uv run pytest tests/test_materialize.py -k schema_change — a unit with create rule-rules-schema and create rule-x carrying a key the disk schema lacks, the key in fields and no unknown; the same create without the schema entry, unknown as before
origin: raw/2026-09-22/1121/ledger.md#case-308.2
sprint: migration
created: 2026-09-22
tags: [harness, librarian]
---

## Criterion

When:
`materialize` walks a unit whose ledger holds a decision line, a `create` or an `update`, with the slug `rule-<category>-schema`.

Then:
A `create` of that category in the same unit is lifted whole: every key goes into `fields`, and no key is `unknown`, wherever the schema entry stands in the Spec, before or after.
**＋** The pages the librarian writes carry the field before `render` lands the schema on disk.
**－** In a unit without such an entry, and for the other categories of the same unit, a `create` is lifted by `vault/wiki/<category>/schema.yaml` on disk: a key outside the schema is `unknown` and does not reach `fields`.

## Result

2026-09-22, uv run pytest tests/test_materialize.py -k "schema_rule or filters_as_before": 2 passed, 71 deselected — the key in fields with the schema line, unknown without it

## History

- 2026-09-22 created · [[decision-case-308.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L89
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the lift by the schema on disk stated (case 489.6) · [[decision-case-489.6]]
