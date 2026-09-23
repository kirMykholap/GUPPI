---
type: estimate
kind: QA
status: passed
target: "[[rule-decisions-schema]]"
purpose: A Decision page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k decisions on the live vault/wiki/decisions/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/decisions/ but the pages of Cases 1–28 without Context and Problem (Slice 5)
checked: 2026-09-23
origin: raw/2026-09-22/0014/ledger.md#case-304.7
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

Given:
`rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
**＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
**＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read.
**＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/decisions/schema.yaml`: a page in the shape, then one defect at a time.

When:
`guppi render` writes `vault/wiki/decisions/schema.yaml` from `rule-decisions-schema`; `guppi lint` reads a page of `wiki/decisions/`.

Then:
The file equals the Render. Lint reads from it: required `type, case, status, origin, sprint, created, tags`; optional `create, update, delete, defer, source, supersedes, superseded_by`; values `status: current | superseded | archived`; the sections `## Context`, `## Problem` and `## History` required, `## Given`, `## When`, `## Criterion`, `## Deferred`, `## Note` optional.
**＋** A Decision page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list or lacking a required section has one finding per defect.
**＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the Slug, the fields deliberately absent, the body paragraph, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the example page; the History of a Decision takes `created`, `superseded by` and one `updated:` line of a Case that signs its text after the fact (358).
**－** `vault/wiki/decisions/schema.md` does not exist.

## Result

2026-09-23, uv run pytest tests/test_schemas.py -k decisions: 4 passed, 1 skipped (no conditional on a field); the live yaml carries required type, case, status, origin, sprint, created, tags, optional create, update, delete, defer, source, supersedes, superseded_by, status current | superseded | archived, sections Context, Problem, History required and Given, When, Criterion, Deferred, Note optional; uv run guppi lint: schema findings on wiki/decisions/ only on the 31 pages of Cases 1–28 (62 lines, Context and Problem); no decisions/schema.md

## History

- 2026-09-22 created · [[decision-case-304.7]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L57
- 2026-09-23 updated: the Criterion names the updated line of a Decision's History (case 358) · [[decision-case-358]]
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L27
