---
type: decision
case: "308.1"
status: archived
update: ["[[rule-glossary]]"]
origin: raw/2026-09-22/1121/ledger.md#case-308.1
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Context

`materialize` lifts the fields of a `create` by the category's `schema.yaml` on disk: a key the schema does not name is marked `unknown` and does not reach the page. The schema is now rendered from `rule-<category>-schema` — by the `render` step, after `generate`. In session 0014 case 304 created `rule-rules-schema` with the field `applies_to`, and case 306.4 created `rule-glossary` with that field; `materialize` walked by the old `schema.yaml`, dropped `applies_to`, and the edge Rule → Entity of the glossary was not made: `rule-glossary` without `applies_to`, `entity-glossary` without `rules`, lint silent — neither side of the edge exists. `rule-harness` and `rule-sprint` got their `applies_to` by an `update` with `set` — a `set` is not checked against the schema. Pages: `rule-glossary` `built`, `entity-glossary` `draft`; `rule-materialize` `built`, its ten Estimates untouched but for one new one.

## Problem

Two defects. The edge of the glossary is absent — an `update` is needed. And the order of the pipeline: a `create` that uses a field the same Spec adds to the schema always loses that field — the schema on disk catches up only after `generate`.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-308.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
