---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A Case with work has its tasks block, and every Estimate it creates or sets pending has a read line of its own
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py
checked: 2026-09-26
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan>` reads the `tasks` block of each Case of the plan.

Then:
A Case with a decision line of a kind other than `defer` in the window and no `tasks` block is the finding `case N: decision lines and no tasks block`.
**＋** An Estimate the Case's `then` block creates or sets `pending` needs a line `` - [ ] read `<slug>` `` whose first backticked slug is that Estimate, matched by `READ_LINE`; with none, the finding `case N: <slug> has no task line`.
**＋** An Estimate whose `update` carries `rename` is that Estimate under the slug of its `rename`, the slug its reading names; a read line of its old slug is not its own task line.
**＋** A slug named only on another Estimate's read line is the finding `case N: <slug> is named on another read line, not its own`.
**－** A Case that a `{supersedes:case N}` of the window names needs no `tasks` block.

## Result

2026-09-26, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
