---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: "Whether guppi sprint ticks under Done when only a passed Estimate, keeps each status, and leaves a pending one and a failed one, with once: true or without, unticked"
method: uv run --project .guppi pytest .guppi/tests/test_sprint.py -k one_off
checked: 2026-11-25
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [harness, sprint]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi sprint` of `.guppi/guppi/sprint.py` renders `vault/wiki/sprint.md` from a sprint page whose `estimates` hold a `passed` Estimate, a `pending` one, a `failed` one with `once: true` and a `failed` one with no `once`.

Then:
The line of the `passed` Estimate stands under Done when as `- [x]`.
**＋** Each line keeps its status after ` · `, `failed` included.
**－** The line of the `pending` Estimate and the lines of both `failed` ones stay `- [ ]`.

## Result

2026-11-25, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
