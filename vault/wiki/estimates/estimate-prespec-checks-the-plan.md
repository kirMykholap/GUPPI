---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: The check of the plan against the session's lines, frontier, tasks, governed paths and the form of an Estimate item
method: pytest tests/test_prespec.py, the tests of --check
checked: 2026-09-21
origin: raw/2026-09-16/1955/ledger.md#case-203.1
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, tests]
---

## Criterion

Given:
`guppi prespec --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `prespec` line with the session's stamp on the Skill call.
**＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
**＋** The ledger hook finds the session's window by the stamp: the first `hi` of the stamp after its first `session-start`, over the logs from today back to the date of that start (case 213).
**＋** A rule with several promises is a parent Case that creates the rule and one sub-case per Estimate (`case-schema.md`).
**＋** The tests in `tests/test_prespec.py` fix `--check`; the live reading is the `/pre-spec` of a session after the render of case 261.
**－** The `PreToolUse ExitPlanMode` hook (`rule-prespec-hook`) does not change here.

When:
`guppi prespec --check <plan>` runs in a session with a `hi`.

Then:
One finding per line on stdout, exit 1 on any, 0 and silent when clean; without a `hi` in the session's window, exit 0 and one line on stderr.
**＋** The stamp is `--session`, else `CLAUDE_SESSION_ID`; with neither, one line on stderr `prespec: no session id; pass --session <stamp> from the hi: line`, exit 2, nothing checked; the last `session-start` of today's log is not read (case 213.1).
**＋** The session's window is found as the ledger hook finds it — by the stamped `hi`, over the logs back to the date of its `session-start` — so the `hi` of yesterday's session is found after midnight (case 213.1).
**＋** Lines: a decision line of the window with no item of its kind under its own Case heading — unless a `{supersedes:case N}` of the window names its Case, whose heading still in the plan is a finding of its own (299.2); an item with no line; a `defer` line matches a `defer` item, a Rule-class file line an `update` with that `file` or `slug`; an item under another sub-case's heading is a finding.
**＋** The frontier `raw/<hi date>/<hi HHMM>/frontier.md`: a missing file, an open line, a `case N` whose heading the plan lacks, a `defer case N` with no `defer` item under Case N.
**＋** Tasks: a Case with a line of a kind other than `defer` and no `tasks` block; an Estimate a `then` block creates or sets `pending` with no task line naming its slug.
**＋** Governed: an `update` item with `file` on a path a live Rule page governs.
**＋** Form: a Case whose `then` block holds two or more Estimate items without a written `sections: Criterion` — one promise per Case, split it; an `update` of an Estimate whose page does not exist; a `create` of an Estimate whose `ref` names neither a live rule or entity nor the slug of a `create` item of category `rules` or `entities` in the same plan (case 221).
**＋** Grammar: every record line of the window — the session's ledger whole plus the date-level ledgers from the `hi` time on — through `materialize.parse_line`; one that does not parse is a finding with its file and line number.
**＋** A `then` block that does not parse: the error as a finding of its Case.
**－** No finding on a Leaf `create` without `method`, an `update` without `contract` or a derived slug: those keys are not read.

## Result

2026-09-21, uv run pytest tests/test_prespec.py 68 green — the Lines check exempts a Case a supersedes of the window names and reports its heading still in the plan; the 64 earlier tests of --check unchanged

## History

- 2026-09-16 created · [[decision-case-203.1]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L33
- 2026-09-17 updated: two lines in the Criterion — the stamp from --session or the environment, refused without one; the window found as the ledger hook finds it, across midnight (case 213.1) · [[decision-case-213.1]]
- 2026-09-17 updated: the Form line of the Criterion — a ref to a rule or entity the same plan creates is no finding (case 221) · [[decision-case-221]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L52
- 2026-09-20 ref `rule-pretask` → `rule-prespec` · [[decision-case-261]]
- 2026-09-20 ref `rule-pretask-hook` → `rule-prespec-hook` · [[decision-case-261]]
- 2026-09-20 renamed from `estimate-pretask-checks-the-plan` · [[decision-case-261]]
- 2026-09-20 updated: renamed with rule-prespec — the Criterion names guppi prespec, the mark prespec, the stderr prefix prespec and tests/test_prespec.py (case 261) · [[decision-case-261]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0740/ledger.md#L13
- 2026-09-20 status: passed → passed · raw/2026-09-20/0740/ledger.md#L16
- 2026-09-22 updated: one line of the Criterion — the lines of a Case superseded by a line of the window need no item, its heading in the plan is a finding (case 299.5) · [[decision-case-299.5]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L28
