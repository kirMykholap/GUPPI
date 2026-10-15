---
type: estimate
kind: QA
status: passed
target: "[[rule-entities-schema]]"
purpose: An Entity page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest .guppi/tests/test_schemas.py -k entities on the live vault/wiki/entities/schema.yaml — a page in the shape, then one defect at a time; the live reading uv run --project .guppi guppi check, no schema finding on wiki/entities/
checked: 2026-10-13
origin: raw/2026-09-22/0014/ledger.md#case-306.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
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

2026-10-13, uv run pytest tests/test_schemas.py -k entities: 6 passed, 1 skipped, the new test that a page in the shape with core: true, origin guppi and sprint guppi has no schema finding among them; the new Render in raw/2026-10-13/1753/spec.md (Case 804.1) adds core to optional, core: [true] to values, a core description and the value guppi to the descriptions of origin and sprint; the live schema.yaml follows at the librarian's render, whose make lint is its live reading

## History

- 2026-09-22 created · [[decision-case-306.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L81
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L28
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given, the history of schema.md and the computed key read by lint out (case 490.3) · [[decision-case-490.3]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L53
- 2026-10-13 updated: the Criterion replaced whole — the field core and the shipped values (case 804) · [[decision-case-804.1]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1753/ledger.md#L116
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
