---
type: estimate
kind: QA
status: passed
target: "[[rule-entities-schema]]"
purpose: An Entity page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest .guppi/tests/test_schemas.py -k entities on the live vault/wiki/entities/schema.yaml — a page in the shape, then one defect at a time; the live reading uv run --project .guppi guppi check, no schema finding on wiki/entities/
checked: 2026-10-13
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render, schema]
core: true
---

## Criterion

When:
`guppi render` writes `vault/wiki/entities/schema.yaml` from `rule-entities-schema`, and `guppi lint` reads a page of `vault/wiki/entities/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `parent, children, code_ref, deferred_by, rules, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `core: true`; conditional — `Leaf` requires `parent`, `MOC` requires `children`; the sections `## Purpose` and `## History` required, `## How it works`, `## Milestones`, `## Backlog`, `## Closed`, `## Terms` optional.
**＋** The file also holds `computed: [rules]`, which lint does not read.
**＋** An Entity page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; an Entity with `rules` on live Rules has none; the glossary page with `## Terms` has none.
**＋** An Entity page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
**＋** `fields` and `sections` describe each name of these lists, `rules`, `core` and `## Terms` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, the Slug, `built`, `How it works` and Constraints notes, the sentence on the edge Rule → Entity and the one on the glossary page; `examples` holds the example pages.

## Result

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
