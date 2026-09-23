---
type: estimate
kind: QA
status: passed
target: "[[rule-estimates-schema]]"
purpose: An Estimate page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k estimates on the live vault/wiki/estimates/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/estimates/
checked: 2026-09-23
origin: raw/2026-09-22/0014/ledger.md#case-304.4
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

Given:
`rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
**＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
**＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read.
**＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/estimates/schema.yaml`: a page in the shape, then one defect at a time.

When:
`guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`; `guppi lint` reads a page of `wiki/estimates/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, status, target, origin, sprint, created, tags`; optional `purpose, method, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Context`, `## Method`, `## Result` optional, `## Result` required on `passed` and on `failed`.
**＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
**＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, the Result and Criterion paragraph, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the two example pages.
**－** `vault/wiki/estimates/schema.md` does not exist.

## Result

2026-09-23, uv run pytest tests/test_schemas.py -k estimates: 4 passed, 1 skipped (no conditional on a field); the live yaml carries required type, kind, status, target, origin, sprint, created, tags, optional purpose, method, checked, Result required on passed and failed; uv run guppi lint: no schema finding on wiki/estimates/, the unmigrated counter apart; no schema.md

## History

- 2026-09-22 created · [[decision-case-304.4]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L54
- 2026-09-23 updated: the live reading is due again — the description of method in the Render changed; the Criterion stands (case 350) · [[decision-case-350]]
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L29
