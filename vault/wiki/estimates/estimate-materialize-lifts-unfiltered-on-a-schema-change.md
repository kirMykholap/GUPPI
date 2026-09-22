---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A create of a category whose schema rule the same unit creates or updates is lifted with every key into fields and no unknown; a unit without that entry is lifted by the schema on disk
method: uv run pytest tests/test_materialize.py -k schema_change — a unit with create rule-rules-schema and create rule-x carrying a key the disk schema lacks, the key in fields and no unknown; the same create without the schema entry, unknown as before
origin: raw/2026-09-22/1121/ledger.md#case-308.2
sprint: migration
created: 2026-09-22
tags: [harness, librarian]
---

## Criterion

Given:
`materialize` lifts a `create` by the category's `schema.yaml` on disk: a key outside the schema is `unknown` and does not reach `fields` (case 214.1).
**＋** The `schema.yaml` of a category is the Render of `rule-<category>-schema`, written by `render` after `generate` (case 304).

When:
`materialize` walks a unit whose Spec holds a `create` or `update` with the slug `rule-<category>-schema`.

Then:
A `create` of that category in the same unit is lifted whole: every key into `fields`, no `unknown` — wherever the schema entry stands in the Spec, before or after.
**＋** The pages the librarian writes carry the field before `render` lands the schema on disk.
**－** A unit without such an entry is lifted by the schema as before; the other categories of the same unit too.

## Result

2026-09-22, uv run pytest tests/test_materialize.py -k "schema_rule or filters_as_before": 2 passed, 71 deselected — the key in fields with the schema line, unknown without it

## History

- 2026-09-22 created · [[decision-case-308.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L89
