---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: "Whether guppi sprint ticks under Done when an Estimate that is passed, or failed with once: true, keeps each status, and leaves a pending one and a failed one with no once unticked"
method: uv run --project .guppi pytest .guppi/tests/test_sprint.py -k one_off
origin: raw/2026-11-25/0605/ledger.md#case-1051
sprint: plugin
created: 2026-11-25
tags: [harness, sprint]
---

## Criterion

When:
`uv run --project .guppi guppi sprint` of `.guppi/guppi/sprint.py` renders `vault/wiki/sprint.md` from a sprint page whose `estimates` hold a `passed` Estimate, a `pending` one, a `failed` one with `once: true` and a `failed` one with no `once`.

Then:
The line of the `passed` Estimate and the line of the `failed` one with `once: true` stand under Done when as `- [x]`.
**＋** Each line keeps its status after ` · `, `failed` included.
**－** The line of the `pending` Estimate and the line of the `failed` one with no `once` stay `- [ ]`.

## Result

2026-11-25, Retro of session 0605: uv run --project .guppi pytest .guppi/tests/test_sprint.py -k one_off 1 passed — under Done when the passed and the failed once: true Estimates stand - [x], the pending and the failed one with no once - [ ], each line keeping its status

## History

- 2026-11-25 created · [[decision-case-1051]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0605/ledger.md#L23
