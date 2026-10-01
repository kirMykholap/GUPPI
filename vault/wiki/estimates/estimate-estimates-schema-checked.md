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
`pytest tests/test_schemas.py` runs the test of section conditions once per category, over the live `vault/wiki/<category>/schema.yaml`.

Then:
For each rule under `body.conditional` of the schema, a page in the shape that has the values of its `when` and lacks its required sections has one `schema` finding per missing section, `missing section <section> (given <when>)`, and no other finding.
**＋** Under `-k estimate`, the test reads `vault/wiki/estimates/schema.yaml`: an Estimate page with `status: passed` and no `## Result` has one such finding, and an Estimate page with `status: failed` and no `## Result` has one.
**＋** Under `-k rules`, the test reads `vault/wiki/rules/schema.yaml`: a Rule page with `enforcement: render` and no `## Render` has one such finding.
**－** A schema with no `body.conditional` skips the test, with a reason that names the missing section condition.
**－** `check_schema` in `guppi/lint.py` and every `vault/wiki/<category>/schema.yaml` stay as they are.

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
- 2026-10-01 deferred · [[decision-case-576]]
- 2026-10-01 updated: the test of a section required under a condition now covers ## Result on passed and failed; the Criterion stands, and the question case 576 put off is answered (case 583) · [[decision-case-583]]
