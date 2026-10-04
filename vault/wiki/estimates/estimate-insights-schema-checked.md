---
type: estimate
kind: QA
status: passed
target: "[[rule-insights-schema]]"
purpose: An Insight page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k insights on the live vault/wiki/insights/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/insights/
checked: 2026-10-04
origin: raw/2026-09-22/0014/ledger.md#case-304.6
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

When:
`uv run guppi render` writes `vault/wiki/insights/schema.yaml` from `rule-insights-schema`, and `uv run guppi lint` reads a page of `vault/wiki/insights/` by the keys of that file.

Then:
`vault/wiki/insights/schema.yaml` equals the Render of `rule-insights-schema`.
**＋** Lint reads from it: required `type, pattern, status, children, severity, origin, sprint, created, tags`; optional `addressed_by, deferred_by`; values `status: open | actioned | archived`; single `addressed_by`; conditional — `actioned` requires `addressed_by`; `computed: [severity]`; the sections `## Pattern` and `## History` required, `## Proposal` optional.
**＋** An Insight page with these fields, values and sections has no `schema` finding. A page that lacks a required field, holds a value outside the list, misses a conditional or lacks a required section has one finding per defect.
**＋** `description` holds the introduction, the Threshold, Reopening and the Slug; `fields` and `sections` describe each name of these lists; `examples` holds the example page.
**＋** `fields.addressed_by` names one decision, the latest; a list is not its shape.
**－** `vault/wiki/insights/schema.md` does not exist.

## Result

2026-10-04, at the /hi of session 2245: uv run pytest -q tests/test_schemas.py -k insights 5 passed, 1 skipped; make lint printed 35 finding lines, 4 deferred and 31 unread, none under wiki/insights/, and no line from its render, sprint, backlog or glossary check, so vault/wiki/insights/schema.yaml matches the Render of rule-insights-schema; vault/wiki/insights/schema.md does not exist; schema.yaml holds single: [addressed_by], computed: [severity], the Threshold, Reopening and Slug paragraphs in description, and one addressed_by in its example

## History

- 2026-09-22 created · [[decision-case-304.6]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L56
- 2026-09-23 updated: the Criterion names properties.single and addressed_by under it (case 362.2) · [[decision-case-362.2]]
- 2026-09-23 updated: the Criterion names the one link of addressed_by (case 361) · [[decision-case-361]]
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L30
- 2026-09-27 updated: the Criterion replaced whole — one sentence of the introduction changed by case 451.4, Given lifted into When and Then (case 451.15) · [[decision-case-451.15]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L25
- 2026-10-04 updated: the Criterion replaced whole — the prose stands as data, with no claim that it is word for word the old schema.md (case 632.9) · [[decision-case-632.9]]
- 2026-10-05 status: pending → passed · raw/2026-10-04/2245/ledger.md#L1
