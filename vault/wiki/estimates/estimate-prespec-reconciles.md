---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
method: "by hand at Retro of the session that changes it: the new Render of rule-prespec and rule-ask in the Spec, read against the Criterion, recorded in the estimate line"
checked: 2026-10-12
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Criterion

When:
The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

Then:
The agent runs `uv run guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
**＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
**＋** A finding in `vault/raw/<date>/<hi HHMM>/frontier.md` or in a line of the session's ledger is fixed there, and the command runs again until it prints no finding.
**＋** At the first run of `/pre-spec` in the session, the agent dispatches one `ask-guppi` over the plan, or over the conserved Spec that the plan's title line names, as `rule-skill-hi` sets that line, with the absolute path of the plan file, the instruction to judge every Case outside `## Deferred` with its sub-cases, and the instruction to read for each such Case its `context`, `when`, `then` and `then` block and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items.
**＋** The questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out; and whether the `When` or `Then` of a Criterion a Case sets asks someone to read or see what only a later session, the librarian's run or a `/hi` produces, when the `method` of that Estimate, in the plan or else on its live page, cannot take that reading in the Case's own session.
**＋** The agent answers the findings with one report before any Case is sent back: the list of what the `ask-guppi` run did not check; each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
**＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
**－** The last question finds nothing where a part of the `method` waits for an event it names that brings that reading, nor in the Criterion of an Estimate whose target is a sprint page `entity-sprint-<id>`, whose `method` may wait for a later session of its sprint.
**－** No second `ask-guppi` is dispatched at the first run, and a later run of `/pre-spec` in the session dispatches none.
**－** The report never says that the whole Spec is checked.
**－** The agent writes no list of the decisions: the plan is the list.
**－** The body of a deferred decision is not read, and `ask-guppi` is not asked whether a Case changes a page that another Case of the plan defers: `uv run guppi prespec --check` notes such a pair at every run, as `estimate-prespec-notes-a-page-another-case-defers` sets it.

## Result

2026-10-12, Retro, the new Render of rule-prespec and rule-ask in the Spec of session 2252 read against the Criterion of case 782.1: the replace of rule-prespec names a fourth question — whether the When or Then of a Criterion asks someone to read what only a later session, the librarian's run or a /hi produces, when the method cannot take that reading in the Case's own session — with an event the method names and an Estimate of a sprint page as no such finding; the replace of rule-ask has ask-guppi answer the questions the skill sets in its order; each old text stands once on its page; the other lines of the Criterion stand in the page unchanged

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
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 updated: the Criterion replaced whole — one ask-guppi per top-level Case at the first run, of the plan or of the conserved Spec its title line names, the report naming what each run judged and did not check (case 634.1) · [[decision-case-634.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-04/2245/ledger.md#L15
- 2026-10-05 updated: the Criterion replaced whole — one ask-guppi over the whole plan at the first run, the report giving what that run did not check; the method a reading of the new Render in the Spec at Retro (case 674.1) · [[decision-case-674.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/2103/ledger.md#L21
- 2026-10-07 updated: the Criterion replaced whole — ask-guppi is not asked about a page one Case changes and another puts off; the check notes it (case 726.2) · [[decision-case-726.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/2114/ledger.md#L26
- 2026-10-12 updated: the Criterion replaced whole — ask-guppi is also asked whether the When or Then of a Criterion needs a reading only a later session can take · [[decision-case-782.1]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/2252/ledger.md#L12
