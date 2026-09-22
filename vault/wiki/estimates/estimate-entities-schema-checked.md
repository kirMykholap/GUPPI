---
type: estimate
kind: QA
status: pending
target: "[[rule-entities-schema]]"
purpose: An Entity page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k entities on the live vault/wiki/entities/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/entities/
checked: 2026-09-22
origin: raw/2026-09-22/0014/ledger.md#case-306.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

Given:
`rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
**＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
**＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read.
**＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/entities/schema.yaml`: a page in the shape, then one defect at a time.

When:
`guppi render` writes `vault/wiki/entities/schema.yaml` from `rule-entities-schema`; `guppi lint` reads a page of `wiki/entities/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `parent, children, code_ref, deferred_by, rules`; values `kind: MOC | Leaf`, `status: draft | built | archived`; conditional — `Leaf` requires `parent`, `MOC` requires `children`; `computed: [rules]`; the sections `## Purpose` and `## History` required, `## How it works`, `## Milestones`, `## Backlog`, `## Closed`, `## Terms` optional.
**＋** An Entity page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; an Entity with `rules` on live Rules has none; the glossary page with `## Terms` has none.
**＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the Slug, `built`, `How it works` and Constraints notes, verbatim, one sentence on the edge after Constraints and one on the glossary page; `fields` and `sections` — the rows of the tables whole, `rules` and `## Terms` among them; `examples` — the two example pages.
**－** `vault/wiki/entities/schema.md` does not exist.

## Result

2026-09-22, uv run pytest tests/test_schemas.py -k entities: 5 passed, 25 deselected; make lint — no finding on entities/schema

## History

- 2026-09-22 created · [[decision-case-306.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L81
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
