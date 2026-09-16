---
type: estimate
kind: QA
status: passed
target: "[[rule-pretask]]"
purpose: The check of the plan against the session's lines, frontier, tasks, governed paths and the form of an Estimate item
method: pytest tests/test_pretask.py, the tests of --check
origin: raw/2026-09-16/1955/ledger.md#case-203.1
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, tests]
---

## Criterion

Given:
`guppi pretask --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `pretask` line with the session's stamp on the Skill call.
**＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
**＋** The tests in `tests/test_pretask.py` fix `--check`; the live reading is the `/pre-task` of this session.
**－** The `PreToolUse ExitPlanMode` hook (`rule-pretask-hook`) does not change.

When:
`guppi pretask --check <plan>` runs in a session with a `hi`.

Then:
One finding per line on stdout, exit 1 on any, 0 and silent when clean; without a `hi` in the session's window, exit 0 and one line on stderr.
**＋** Lines: a decision line of the window with no item of its kind under its own Case heading; an item with no line; a `defer` line matches a `defer` item, a Rule-class file line an `update` with that `file` or `slug`; an item under another sub-case's heading is a finding.
**＋** The frontier `raw/<hi date>/<hi HHMM>/frontier.md`: a missing file, an open line, a `case N` whose heading the plan lacks, a `defer case N` with no `defer` item under Case N.
**＋** Tasks: a Case with a line of a kind other than `defer` and no `tasks` block; an Estimate a `then` block creates or sets `pending` with no task line naming its slug.
**＋** Governed: an `update` item with `file` on a path a live Rule page governs.
**＋** Form: a Case whose `then` block holds two or more Estimate items without a written `sections: Criterion` — one promise per Case, split it; an `update` of an Estimate whose page does not exist; a `create` of an Estimate whose `ref` names no live rule or entity.
**＋** Grammar: every record line of the window — the session's ledger whole plus the date-level ledgers from the `hi` time on — through `materialize.parse_line`; one that does not parse is a finding with its file and line number.
**＋** A `then` block that does not parse: the error as a finding of its Case.
**－** No finding on a Leaf `create` without `method`, an `update` without `contract` or a derived slug: those keys are not read.

## Result

2026-09-16, `pytest tests/test_pretask.py`: 48 green — two Estimate items without a written Criterion a finding, one plus one with a written Criterion clean, a sub-case its own Case, an update of an Estimate without a page and a create whose ref names no live page each a finding, contract and estimate_slug not read; live, `guppi pretask --check` on this session's plan: exit 0, the four `has no contract` of the old form gone

## History

- 2026-09-16 created · [[decision-case-203.1]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L33
