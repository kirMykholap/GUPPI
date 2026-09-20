---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
method: One reading by hand of the first /pre-spec after the render, written into the estimate line — the exception the Method rule allows
checked: 2026-09-20
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Criterion

Given:
`guppi prespec --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `prespec` line with the session's stamp on the Skill call.
**＋** `--session` takes the eight-character session id — the second token of the `hi:` line, between the time and the folder; `session_stamp` cuts any value to eight characters, so a wrong token answers "no hi recorded for session <8 characters>; nothing checked" on stderr with exit 0, and nothing was checked.
**＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
**＋** The tests in `tests/test_prespec.py` fix `--check`; the live reading is the first `/pre-spec` after the render of case 261.
**－** The `PreToolUse ExitPlanMode` hook (`rule-prespec-hook`) does not change here.
**－** The code of `guppi prespec` does not change: the exit 0 without a `hi` is the design of case 213.

When:
The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved.

Then:
The agent runs `guppi prespec --check` on the plan file with `--session <id>`, the eight-character session id — the second token of the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi`, between the time and the folder (cases 213.3, 256) — and reads the first line of the output before the exit code: "no hi recorded for session …; nothing checked" means the wrong value, and the check did not run; it fixes the plan, the frontier or the line for every finding until the command prints nothing; `guppi gate` writes the stamped `prespec` line into the event log on the Skill call.
**＋** The agent lists every decision of this Plan Mode, one line each: slug — kind — `purpose` for a `create`, an `update`, a `delete`; a `defer` by its slug and the word `defer`; for an `update` of a rule or an entity, the page's `estimates` and which of them the Case names by slug.
**＋** `ask-guppi` is dispatched once with the list, the absolute path of the plan file, the instruction to read every Case outside `## Deferred` — `when`, `then`, the `then` block — and two questions: which decisions contradict a page, `index.md` or each other; whether an Estimate the Case does not name speaks of the thing the Case changes.
**＋** Every finding returned is raised as a Case or named in one line as already known; then Plan Mode exits again.
**＋** The Insight `insight-pretask-session-flag-takes-the-id-not-the-hi-line` is `actioned`; its two lessons go to the archive by the cascade; a third lesson with the same cause reopens it.
**－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

## Result

2026-09-20, the /pre-spec of session 0958 typed by the person, on the skill as rendered by 261: `uv run guppi prespec --check <plan> --session c27cd9be` — the eight-character id from the hi: line — printed nothing and exited 0 on the first run, 22 ledger lines against the plan's items, the frontier's nine lines closed; the stamped prespec mark written by guppi gate on the typed command; the list of 20 decisions with the estimates of each updated rule and which the Case names; ask-guppi dispatched once with the list, the plan path and the two questions; six findings on Q1 — a failed Estimate in both lists of 268.1, two copies of the carry omissions and of the pull sentence on rule-carry-over and rule-git-context, two stale sentences of rule-skill-hi, the method of estimate-hi-writes-frontier lost between 265 and 268.2, the decisions 220/243 — taken as changes to 265, 268.1, 268.2 or named as known; none on Q2, every replace old verified once on its page; Plan Mode exited again after the ratification of the changes

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.2
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L75
- 2026-09-12 updated: the mechanical check of the plan against the session's decision lines joins the criterion; pending for the reading at this session's pre-task (case 59.1) · [[decision-case-59.1]]
- 2026-09-12 updated: the frontier findings join the criterion (case 59.2) · [[decision-case-59.2]]
- 2026-09-12 updated: the tasks findings join the criterion (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: the governed-file finding joins the criterion (case 59.6) · [[decision-case-59.6]]
- 2026-09-12 updated: the findings of case 72.5 join the criterion; pending until the unit reading · [[decision-case-72.5]]
- 2026-09-12 criterion: case 73.4 added · [[decision-case-73.4]]
- 2026-09-12 criterion: case 74 added · [[decision-case-74]]
- 2026-09-12 criterion: case 75.2 added · [[decision-case-75.2]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L158
- 2026-09-12 criterion: case 90.2 added · [[decision-case-90.2]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L208
- 2026-09-13 criterion: case 103.4 added · [[decision-case-103.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L38
- 2026-09-14 criterion: case 128 added · [[decision-case-128]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L25
- 2026-09-16 updated: the Criterion replaced whole by case 203.2 — the live run of the skill; the blocks 73.4, 74, 75.2, 90.2, 103.4 go to -checks-the-plan, 128 stays here (case 203.2) · [[decision-case-203.2]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L34
- 2026-09-17 updated: method as a field, the old sections dropped — the recut completed (case 211.3) · [[decision-case-211.3]]
- 2026-09-17 updated: the first line of Then — the check runs with --session from the hi line (case 213.3) · [[decision-case-213.3]]
- 2026-09-18 status: pending → passed · raw/2026-09-17/1119/ledger.md#L39
- 2026-09-20 updated: the Criterion replaced whole — the session id named as the second token of the hi: line, the first line of the output read (case 256) · [[decision-case-256]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0527/ledger.md#L21
- 2026-09-20 ref `rule-pretask` → `rule-prespec` · [[decision-case-261]]
- 2026-09-20 ref `rule-pretask-hook` → `rule-prespec-hook` · [[decision-case-261]]
- 2026-09-20 renamed from `estimate-pretask-reconciles` · [[decision-case-261]]
- 2026-09-20 updated: renamed with rule-prespec — the Criterion names /pre-spec, guppi prespec, the mark prespec and tests/test_prespec.py (case 261) · [[decision-case-261]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L25
