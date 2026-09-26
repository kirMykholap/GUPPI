---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A Case with work has its tasks block, and every Estimate it creates or sets pending has a read line of its own
method: uv run pytest tests/test_prespec.py
checked: 2026-09-26
origin: raw/2026-09-24/1916/ledger.md#case-399.4
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run guppi prespec --check <plan>` reads the `tasks` block of each Case of the plan.

Then:
A Case with a decision line of a kind other than `defer` in the window and no `tasks` block is the finding `case N: decision lines and no tasks block`.
**＋** An Estimate the Case's `then` block creates or sets `pending` needs a line `` - [ ] read `<slug>` `` whose first backticked slug is that Estimate, matched by `READ_LINE`; with none, the finding `case N: <slug> has no task line`.
**＋** An Estimate whose `update` carries `rename` is that Estimate under the slug of its `rename`, the slug its reading names; a read line of its old slug is not its own task line.
**＋** A slug named only on another Estimate's read line is the finding `case N: <slug> is named on another read line, not its own`.
**－** A Case that a `{supersedes:case N}` of the window names needs no `tasks` block.

## Result

2026-09-26, `uv run pytest -q tests/test_prespec.py`; 120 passed, the tasks block, the read line, the rename and the other-read-line findings asserted, and a superseded Case needs no tasks block

## History

- 2026-09-25 created · [[decision-case-399.4]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L40
- 2026-09-25 updated: the Criterion replaced whole — a renamed Estimate is read under the slug of its rename (case 432) · [[decision-case-432]]
- 2026-09-26 status: pending → passed · raw/2026-09-26/1745/ledger.md#L31
