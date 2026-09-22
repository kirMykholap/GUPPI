---
type: estimate
kind: QA
status: passed
target: "[[rule-lessons-schema]]"
purpose: A Lesson page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k lessons on the live vault/wiki/lessons/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/lessons/
origin: raw/2026-09-22/0014/ledger.md#case-304.5
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

Given:
`rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
**＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
**＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
**＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/lessons/schema.yaml`: a page in the shape, then one defect at a time.

When:
`guppi render` writes `vault/wiki/lessons/schema.yaml` from `rule-lessons-schema`; `guppi lint` reads a page of `wiki/lessons/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, root_cause, status, origin, sprint, created, tags`; optional `source, insight`; values `kind: error | knowledge`, `status: new | clustered | archived`; conditional — `knowledge` requires `source`, `clustered` requires `insight`; the sections `## Trigger`, `## Root cause` and `## History` required.
**＋** A Lesson page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
**＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the Slug, no Estimate, no `reviewed` status, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the two example pages.
**－** `vault/wiki/lessons/schema.md` does not exist.

## Result

2026-09-22, uv run pytest tests/test_schemas.py -k lessons, 5 passed on the live vault/wiki/lessons/schema.yaml: the same four defects, one finding each, a page in the shape none; the live leg, make lint after the librarian's render, not taken

## History

- 2026-09-22 created · [[decision-case-304.5]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L55
