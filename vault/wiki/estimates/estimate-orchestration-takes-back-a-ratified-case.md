---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: A ratified Case the person takes back in Plan Mode is retired by a short Case of the main agent whose defer lines supersede it, and the line of its item closes as its source is put off
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
checked: 2026-11-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, ledger]
core: true
---

## Criterion

When:
In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the person asks in the chat to take back a Case of the session that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, whole or one of its sub-cases.

Then:
In the same reply the main agent shows a short Case of its own in the form of a deferred decision, with no dispatch of `case-guppi`, and carries its `LEDGER` block, with no tool call after it.
**＋** The block holds one `defer` line for each rule, entity and insight page the Case taken back names, one for each Estimate it updates, and one for the page that each Estimate it updates checks or each Estimate it creates would check, once per page; each line carries `{supersedes:case N}` for the Case or sub-case taken back.
**＋** At the librarian's run, `.guppi/guppi/generate.py` adds the short Case to the `deferred_by` of each rule, entity and insight page a `defer` line names, and each such page stands in `vault/wiki/backlog.md`, also when the Case taken back changed only existing Estimates.
**＋** The `context` of the short Case names the Case taken back and each Estimate that Case creates; the person's words asking for the take-back are its ratification, and no question asks for it.
**＋** The `Stop` hook of `rule-spec-write` writes the short Case under `## Deferred` and removes the Case taken back from the plan file.
**＋** When no part of the Case stays in the plan, the line of its item in `raw/<date>/<hi HHMM>/frontier.md` changes in the same reply from the closer it stands with to `[-] … · sprint · defer` for an item of the sprint, `[-] … · backlog · kept` for an item of the backlog, or `[-] … · defer case M` of the short Case for any other source, and a line that already stands with that closer stays as it is.
**＋** The reply ends as the reply that carries a defer: the Frontier with the line closed by that closer, then the question which open item is next, or before `/pre-spec` the question whether to go on to `/pre-spec`, or after `/pre-spec` no question.
**－** The file of the Case taken back under `raw/<date>/<hi HHMM>/cases/` is not emptied, and no `case-guppi` undoes it.
**－** In Work Mode no Case is taken back: the main agent tells the person that the ratified Case stands, and that a Case of a later session may replace it.

## Result

2026-11-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
