---
type: estimate
kind: QA
status: passed
target: "[[rule-insights-schema]]"
purpose: An Insight page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest .guppi/tests/test_schemas.py -k insights on the live vault/wiki/insights/schema.yaml — a page in the shape, then one defect at a time; the live reading uv run --project .guppi guppi check, no schema finding on wiki/insights/
checked: 2026-10-04
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render, schema]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi render` writes `vault/wiki/insights/schema.yaml` from `rule-insights-schema`, and `uv run --project .guppi guppi lint` reads a page of `vault/wiki/insights/` by the keys of that file.

Then:
`vault/wiki/insights/schema.yaml` equals the Render of `rule-insights-schema`.
**＋** Lint reads from it: required `type, pattern, status, children, severity, origin, sprint, created, tags`; optional `addressed_by, deferred_by`; values `status: open | actioned | archived`; single `addressed_by`; conditional — `actioned` requires `addressed_by`; `computed: [severity]`; the sections `## Pattern` and `## History` required, `## Proposal` optional.
**＋** An Insight page with these fields, values and sections has no `schema` finding. A page that lacks a required field, holds a value outside the list, misses a conditional or lacks a required section has one finding per defect.
**＋** `description` holds the introduction, the Threshold, Reopening and the Slug; `fields` and `sections` describe each name of these lists; `examples` holds the example page.
**＋** `fields.addressed_by` names one decision, the latest; a list is not its shape.
**－** `vault/wiki/insights/schema.md` does not exist.

## Result

2026-10-04, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
