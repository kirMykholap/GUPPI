---
type: estimate
kind: QA
status: passed
target: "[[rule-pretask]]"
checked: 2026-09-16
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Context

The skill is a short instruction plus one recorded line. What has to hold is that the line
lands where the hook looks, that the agent is dispatched once with the whole set rather
than per decision, and that nothing it returns is dropped on the floor.

## Criterion

Given:
`guppi pretask --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `pretask` line with the session's stamp on the Skill call.
**＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
**＋** The tests in `tests/test_pretask.py` fix `--check`; the live reading is the `/pre-task` of this session.
**－** The `PreToolUse ExitPlanMode` hook (`rule-pretask-hook`) does not change.

When:
The person invokes `/pre-task`, or the agent calls the skill, before the Spec is approved.

Then:
The agent runs `guppi pretask --check` on the plan file and fixes the plan, the frontier or the line for every finding until the command prints nothing; `guppi gate` writes the stamped `pretask` line into the event log on the Skill call.
**＋** The agent lists every decision of this Plan Mode, one line each: slug — kind — `purpose` for a `create`, an `update`, a `delete`; a `defer` by its slug and the word `defer`; for an `update` of a rule or an entity, the page's `estimates` and which of them the Case names by slug.
**＋** `ask-guppi` is dispatched once with the list, the absolute path of the plan file, the instruction to read every Case outside `## Deferred` — `when`, `then`, the `then` block — and two questions: which decisions contradict a page, `index.md` or each other; whether an Estimate the Case does not name speaks of the thing the Case changes.
**＋** Every finding returned is raised as a Case or named in one line as already known; then Plan Mode exits again.
**－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

## Method

One reading by hand, written into the estimate line — the exception the Method rule
allows.

## Result

2026-09-16, the /pre-task of this session: `--check` run and its four old-form findings named known in one line; the list carried every decision with its type and purpose, defers by slug and the word defer, and for each rule update the page's estimates and which the Case names; ask-guppi dispatched once with the plan path, the instruction to read every Case outside ## Deferred and both questions; three findings raised as Case 208, the rest named known; read against the Criterion of 203.2 with the Render still of 198

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
