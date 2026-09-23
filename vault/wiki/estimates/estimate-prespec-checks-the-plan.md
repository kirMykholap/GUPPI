---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: The check of the plan against the session's lines, frontier, tasks, governed paths and the form of an Estimate item
method: pytest tests/test_prespec.py, the tests of --check
checked: 2026-09-23
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
**＋** Lines: a decision line of the window with no item of its kind under its own Case heading — unless a `{supersedes:case N}` of the window names its Case, whose heading still in the plan is a finding of its own (299.2); an item with no line; a `defer` line matches a `defer` item; an `update` item carrying `file` is a finding of its own (case 320); an item under another sub-case's heading is a finding.
**＋** The frontier `raw/<hi date>/<hi HHMM>/frontier.md`: a missing file, an open line under `## Cases` — an open line under `## Work` is clean (356.1) —, a `case N` whose heading the plan lacks, a `defer case N` with no `defer` item under Case N; `[-] … · sprint` is clean, `[x] … · sprint` a finding (case 310.6); a line whose source segment is `sprint` closed `· defer case N` a finding (356.2). A line closed `· case N` whose source segment — the one before the closer — is `sprint` needs an `update` of the sprint page under Case N; the word inside the slug of a title is not the source (cases 314.2, 335).
**＋** Tasks: a Case with a line of a kind other than `defer` and no `tasks` block; an Estimate a `then` block creates or sets `pending` with no line `- [ ] read `<slug>`` whose first backticked slug is that Estimate, as `generate` matches it when it ticks; a slug named on another Estimate's read line gives the finding in its own words (case 327).
**＋** Governed: an `update` item carrying `file` — the file route is gone (case 320).
**＋** Form: a Case whose `then` block holds two or more Estimate items without a written `sections: Criterion` — one promise per Case, split it; an `update` of an Estimate whose page does not exist; a `create` of an Estimate whose `ref` names neither a live rule or entity nor the slug of a `create` item of category `rules` or `entities` in the same plan (case 221).
**＋** Grammar: every record line of the window — the session's ledger whole plus the date-level ledgers from the `hi` time on — through `materialize.parse_line`; one that does not parse is a finding with its file and line number.
**＋** A `then` block that does not parse: the error as a finding of its Case.
**－** No finding on a `create` of a rule or an entity without `method`, an `update` without `contract` or a derived slug: those keys are not read. A `create` of an Estimate with no `method`, or with a `method` naming none of the four forms lint classifies, is a finding (case 331).

## Result

2026-09-23, uv run pytest tests/test_prespec.py: 92 passed; live, the /pre-spec of session 1126: guppi prespec --check printed "frontier: C11 is open" (the box left unticked), then after the amended Cases four items without a decision line, then exit 0 once the lines stood in the ledger

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
- 2026-09-22 updated: the closer `· sprint` (case 310.6) · [[decision-case-310.6]]
- 2026-09-22 updated: the file route is a finding, not a route (case 320) · [[decision-case-320]]
- 2026-09-22 updated: any file item is a finding (case 323) · [[decision-case-323]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L87
- 2026-09-23 updated: the task line of a reading in the Criterion — matched as generate ticks it (case 327) · [[decision-case-327]]
- 2026-09-23 updated: the line on a create without method makes room for the finding of case 331 (case 338.2) · [[decision-case-338.2]]
- 2026-09-23 updated: the source segment of a Frontier line in the Criterion (case 335) · [[decision-case-335]]
- 2026-09-23 updated: the Criterion names an open Work line clean (case 356.1) · [[decision-case-356.1]]
- 2026-09-23 updated: the Criterion names the finding on a deferred sprint line (case 356.2) · [[decision-case-356.2]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L40
