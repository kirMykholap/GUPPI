---
type: estimate
kind: QA
status: pending
target: "[[rule-estimates-schema]]"
purpose: An Estimate page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k estimate on the live vault/wiki/estimates/schema.yaml — a page in the shape, a page without method, then one defect at a time; the live reading make lint, no schema finding on wiki/estimates/
checked: 2026-09-29
origin: raw/2026-09-22/0014/ledger.md#case-304.4
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

When:
`guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
**＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
**＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
**＋** `fields` and `sections` describe each name of these lists; `description` holds, among its paragraphs, the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
**－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.

## Result

2026-09-29, uv run pytest tests/test_schemas.py -k estimates: 4 passed, 1 skipped (no conditional on a field); uv run guppi render --check exit 0; make lint prints no schema finding on wiki/estimates/; grep of vault/wiki/estimates/schema.yaml for unmigrated, ## Context, ## Method and Given: finds only the Criterion description saying no Given: stands in a Criterion

## History

- 2026-09-22 created · [[decision-case-304.4]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L54
- 2026-09-23 updated: the live reading is due again — the description of method in the Render changed; the Criterion stands (case 350) · [[decision-case-350]]
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L29
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the history of schema.md out (case 490.4) · [[decision-case-490.4]]
- 2026-09-29 updated: the Criterion replaced whole — method required, the two old sections gone (case 506.1) · [[decision-case-506.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L27
- 2026-09-30 updated: the method runs -k estimate and names a page without method, so the test of method runs; the reading is due again, the Criterion stands (case 556) · [[decision-case-556]]
