---
type: estimate
kind: QA
status: pending
target: "[[rule-lessons-schema]]"
purpose: A Lesson page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k lessons on the live vault/wiki/lessons/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/lessons/
checked: 2026-09-23
origin: raw/2026-09-22/0014/ledger.md#case-304.5
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

When:
`guppi render` writes `vault/wiki/lessons/schema.yaml` from `rule-lessons-schema`, and `guppi lint` reads a page of `vault/wiki/lessons/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, root_cause, status, origin, sprint, created, tags`; optional `source, insight`; values `kind: error | knowledge`, `status: new | clustered | archived`; conditional — `knowledge` requires `source`, `clustered` requires `insight`; the sections `## Trigger`, `## Root cause` and `## History` required.
**＋** A Lesson page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
**＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, no Estimate and no `reviewed` status; `examples` holds the example pages.

## Result

2026-09-23, uv run pytest tests/test_schemas.py -k lessons: 5 passed; the live yaml carries the required and optional fields, kind error | knowledge, status new | clustered | archived, knowledge requires source, clustered requires insight, Trigger, Root cause, History required; uv run guppi lint: no schema finding on wiki/lessons/

## History

- 2026-09-22 created · [[decision-case-304.5]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L55
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L31
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the history of schema.md out (case 490.6) · [[decision-case-490.6]]
