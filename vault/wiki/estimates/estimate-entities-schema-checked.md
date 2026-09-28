---
type: estimate
kind: QA
status: pending
target: "[[rule-entities-schema]]"
purpose: An Entity page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k entities on the live vault/wiki/entities/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/entities/
checked: 2026-09-23
origin: raw/2026-09-22/0014/ledger.md#case-306.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

When:
`guppi render` writes `vault/wiki/entities/schema.yaml` from `rule-entities-schema`, and `guppi lint` reads a page of `vault/wiki/entities/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `parent, children, code_ref, deferred_by, rules`; values `kind: MOC | Leaf`, `status: draft | built | archived`; conditional — `Leaf` requires `parent`, `MOC` requires `children`; the sections `## Purpose` and `## History` required, `## How it works`, `## Milestones`, `## Backlog`, `## Closed`, `## Terms` optional.
**＋** The file also holds `computed: [rules]`, which lint does not read.
**＋** An Entity page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; an Entity with `rules` on live Rules has none; the glossary page with `## Terms` has none.
**＋** `fields` and `sections` describe each name of these lists, `rules` and `## Terms` among them; `description` holds the introduction, the Slug, `built`, `How it works` and Constraints notes, the sentence on the edge Rule → Entity and the one on the glossary page; `examples` holds the example pages.

## Result

2026-09-23, uv run pytest tests/test_schemas.py -k entities: 5 passed; the live yaml carries the required, optional, values and conditional of the Criterion, computed [rules], sections Purpose and History required, How it works, Milestones, Backlog, Closed, Terms optional; uv run guppi lint: no schema finding on wiki/entities/; no schema.md

## History

- 2026-09-22 created · [[decision-case-306.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L81
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L28
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given, the history of schema.md and the computed key read by lint out (case 490.3) · [[decision-case-490.3]]
