---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
method: One reading by hand of the first /pre-spec after the render, written into the estimate line — the exception the Method rule allows
checked: 2026-10-01
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Criterion

When:
The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved.

Then:
The agent runs `guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
**＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
**＋** A finding in the Frontier or in a ledger line is fixed there, and the command runs again until it prints no finding.
**＋** At the first run of `/pre-spec` in the session, `ask-guppi` is dispatched once with the absolute path of the plan file and the instruction to read every Case outside `## Deferred` — `context`, `when`, `then`, the `then` block — and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items; a later run of `/pre-spec` in the session dispatches no `ask-guppi`.
**＋** Three questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out.
**＋** The agent answers the findings with one report before any Case is sent back: each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
**＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
**－** The agent writes no list of the decisions: the plan is the list.
**－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

## Result

2026-10-01, by hand, the first /pre-spec after the render, session 1237: guppi prespec --check ran on the plan with --session dd5dac5e and printed 9 note lines and no finding; ask-guppi was dispatched once with the absolute path of the plan and the reading instructions, the Deferred Cases by slug only; one numbered report answered its seven findings before any Case was sent back, each with its fix or why it is known, none needing the person; the findings in Cases 567 and 569 went to their case-guppi by SendMessage, the Cases were shown and ratified again, and the Spec hook wrote them into the plan; after that the check ran once more, printed no finding, and ExitPlanMode followed with no second /pre-spec; guppi gate wrote the prespec mark at 14:08:41

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
- 2026-09-23 updated: the live reading is due again — the Render gained the simulation of the pairs; the Criterion stands (case 351) · [[decision-case-351]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/0034/ledger.md#L62
- 2026-09-23 updated: the question on contradictions as the Render asks it (case 364.3) · [[decision-case-364.3]]
- 2026-09-24 updated: the Criterion replaced whole — the translation, ask-guppi reading the plan and the context, the report before the re-showing (case 388) · [[decision-case-388]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1228/ledger.md#L42
- 2026-09-26 updated: the Criterion replaced whole — no translation before the run, a finding in a Case to its case-guppi (case 441.4) · [[decision-case-441.4]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L35
- 2026-10-01 updated: the Criterion replaced whole - ask-guppi at the first run of the session only, one report that sorts the findings, no second call after the Cases built again are ratified (case 561.1) · [[decision-case-561.1]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L40
