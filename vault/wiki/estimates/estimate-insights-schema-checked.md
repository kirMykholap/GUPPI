---
type: estimate
kind: QA
status: passed
target: "[[rule-insights-schema]]"
purpose: An Insight page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k insights on the live vault/wiki/insights/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/insights/
origin: raw/2026-09-22/0014/ledger.md#case-304.6
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

Given:
`rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
**＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
**＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
**＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/insights/schema.yaml`: a page in the shape, then one defect at a time.

When:
`guppi render` writes `vault/wiki/insights/schema.yaml` from `rule-insights-schema`; `guppi lint` reads a page of `wiki/insights/`.

Then:
The file equals the Render. Lint reads from it: required `type, pattern, status, children, severity, origin, sprint, created, tags`; optional `addressed_by, deferred_by`; values `status: open | actioned | archived`; conditional — `actioned` requires `addressed_by`; `computed: [severity]`; the sections `## Pattern` and `## History` required, `## Proposal` optional.
**＋** An Insight page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
**＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the Threshold, Reopening, the Slug, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the example page.
**－** `vault/wiki/insights/schema.md` does not exist.

## Result

2026-09-22, uv run pytest tests/test_schemas.py -k insights, 4 passed and 1 skipped on the live vault/wiki/insights/schema.yaml: no conditional on a field to break, the other three defects one finding each, a page in the shape none; the live leg, make lint after the librarian's render, not taken

## History

- 2026-09-22 created · [[decision-case-304.6]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L56
