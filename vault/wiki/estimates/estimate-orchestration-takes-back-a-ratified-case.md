---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: A ratified Case the person takes back in Plan Mode is retired by a short Case of the main agent whose defer lines supersede it, and the line of its item closes as its source is put off
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-07/1804/ledger.md#case-713
sprint: migration
created: 2026-10-07
tags: [session, workflow, ledger]
---

## Criterion

When:
In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the person asks in the chat to take back a Case of the session that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, whole or one of its sub-cases.

Then:
In the same reply the main agent shows a short Case of its own in the form of a deferred decision, with no dispatch of `case-guppi`, and carries its `LEDGER` block, with no tool call after it.
**＋** The block holds one `defer` line for each rule, entity and insight page the Case taken back names, one for each Estimate it updates, and one for the page that each Estimate it creates would check, once per page; each line carries `{supersedes:case N}` for the Case or sub-case taken back.
**＋** The `context` of the short Case names the Case taken back and each Estimate that Case creates.
**＋** The person's words asking for the take-back are its ratification: no question asks for it.
**＋** The `Stop` hook of `rule-spec-write` writes the short Case under `## Deferred` and removes the Case taken back from the plan file.
**＋** When no part of the Case stays in the plan, the line of its item in `raw/<date>/<hi HHMM>/frontier.md` changes in the same reply from `[x] … · case N` to `[-] … · sprint · defer` for an item of the sprint, `[-] … · backlog · kept` for an item of the backlog, or `[-] … · defer case M` of the short Case for any other source.
**＋** The reply ends as the reply that carries a defer: the Frontier, then the question which open item is next, or before `/pre-spec` the question whether to go on to `/pre-spec`, or after `/pre-spec` no question.
**－** The file of the Case taken back under `raw/<date>/<hi HHMM>/cases/` is not emptied, and no `case-guppi` undoes it.
**－** In Work Mode no Case is taken back: the main agent tells the person that the ratified Case stands, and that a Case of a later session may replace it.

## Result

2026-10-07, Retro, by hand: the new Render of rule-orchestration in the Spec (Case 713, its four replace pairs) read against the Criterion — every then line is set: a short Case of the main agent with no dispatch, its LEDGER block with one defer line per rule, entity and insight page, per Estimate it updates and per page each created Estimate checks, each with {supersedes:case N}; the context naming the Case and its created Estimates; the person's words as ratification; the Case removed from the plan and its file standing; the Frontier line changed to the closer of its source; the reply ending as a defer reply; no take-back in Work Mode. The faults F2–F6 that pre-spec found elsewhere in the same Render stand, put off by case 721

## History

- 2026-10-07 created · [[decision-case-713]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/1804/ledger.md#L19
