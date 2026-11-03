---
type: estimate
kind: QA
status: passed
target: "[[rule-lessons-schema]]"
purpose: A Lesson page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest .guppi/tests/test_schemas.py -k lessons on the live vault/wiki/lessons/schema.yaml — a page in the shape, then one defect at a time; the live reading uv run --project .guppi guppi check, no schema finding on wiki/lessons/
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render, schema]
core: true
---

## Criterion

When:
`guppi render` writes `vault/wiki/lessons/schema.yaml` from `rule-lessons-schema`, and `guppi lint` reads a page of `vault/wiki/lessons/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, root_cause, status, origin, sprint, created, tags`; optional `source, insight`; values `kind: error | knowledge`, `status: new | clustered | archived`; conditional — `knowledge` requires `source`, `clustered` requires `insight`; the sections `## Trigger`, `## Root cause` and `## History` required.
**＋** A Lesson page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
**＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, no Estimate and no `reviewed` status; `examples` holds the example pages.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
