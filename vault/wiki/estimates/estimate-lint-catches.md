---
type: estimate
kind: QA
status: passed
target: rule-lint
origin: raw/2026-09-09/ledger.md#case-21
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Context

Lint is the first reader of the whole graph. The unit cases seed one page per defect
class and pin the finding each produces; the live reading is the first pass over the
pages written by hand since Slice 0, whose findings are the debt the brief carries.

## Criterion

Against a temp vault seeded with one page per defect class, `guppi lint` names each
defective page with the class and nothing else, exits 1, and exits 0 with no output on a
clean vault; the two Method classes (case 26.2) are seeded too. Against the live vault:
the first run's findings are each either an item of the brief's known-false list or
become a Case.

## Method

pytest in `tests/test_lint.py`, one test per defect class; the live reading once by hand,
written into the estimate line.

## Result

Passing, 2026-09-09, session D. `tests/test_lint.py`: 22 tests green. Live, first run over
the vault, 15 findings: three `ref` lines for the children of `rule-plan-mode` that
arrive later in the slice, one `ref` line for `rule-documentation` (Slice 3), nine
`status` lines `draft while every Estimate is passed` on the Slice 1 pages and
`rule-render-harness` (`built` is the Slice 3 generator's to set), one `method` line for
`estimate-session-start-context` (fixed by case 26.2 in the same slice), and one `method`
line for `estimate-hi-no-read-calls` — a MOC whose children are all hand readings, which
the ratified Method rule does not cover; raised to the owner as a Case.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-21
- 2026-09-09 updated: criterion gains the two Method defect classes · raw/2026-09-09/ledger.md#case-26.2
- 2026-09-09 status: pending → passed · written by hand, no generator yet
