---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: "Whether guppi sprint ticks under Done when only a passed Estimate, keeps each status, and leaves a pending one and a failed one, with once: true or without, unticked"
method: uv run --project .guppi pytest .guppi/tests/test_sprint.py -k one_off
checked: 2026-11-25
origin: raw/2026-11-25/0605/ledger.md#case-1051
sprint: plugin
created: 2026-11-25
tags: [harness, sprint]
---

## Criterion

When:
`uv run --project .guppi guppi sprint` of `.guppi/guppi/sprint.py` renders `vault/wiki/sprint.md` from a sprint page whose `estimates` hold a `passed` Estimate, a `pending` one, a `failed` one with `once: true` and a `failed` one with no `once`.

Then:
The line of the `passed` Estimate stands under Done when as `- [x]`.
**＋** Each line keeps its status after ` · `, `failed` included.
**－** The line of the `pending` Estimate and the lines of both `failed` ones stay `- [ ]`.

## Result

2026-11-25, Retro of session 0816, `uv run --project .guppi pytest .guppi/tests/test_sprint.py -k one_off`: 1 passed, 34 deselected; `test_a_failed_one_off_estimate_stays_unticked_and_keeps_its_status` renders "- [x] the branch merged · passed", "- [ ] make lint exits 0 · pending", "- [ ] read once · failed" and "- [ ] a lasting check · failed", against the Criterion of Case 1057.2

## History

- 2026-11-25 created · [[decision-case-1051]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0605/ledger.md#L23
- 2026-11-25 updated: the Criterion replaced whole — a failed one-off Estimate stays unticked · [[decision-case-1057.2]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0816/ledger.md#L30
