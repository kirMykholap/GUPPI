---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the agent closes a Frontier line of a sprint or backlog item · case N only when a decision line of Case N ends the item, and otherwise closes it as the item put off with the decision lines of the Case standing
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration and of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and `.claude/skills/hi/SKILL.md` from `rule-skill-hi`, the person ratifies a Case built on the item of a line of `raw/<date>/<hi HHMM>/frontier.md` with the source `sprint` or `backlog`.

Then:
The agent closes the line `[x] … · case N` only when a decision line of Case N ends the item.
**＋** A sprint item ends by Case N only when Case N or a sub-case updates the sprint page `entity-sprint-<id>`.
**＋** An item of `vault/wiki/backlog.md` whose page carries `deferred_by` ends by Case N only when a decision line of Case N other than a `defer` names the page, and a Case among Case N and its sub-cases that names the page carries `{supersedes:case M}` for each Case M of the page's `deferred_by`.
**＋** An open Insight of `vault/wiki/backlog.md` ends by Case N only when Case N or a sub-case updates the page of the Insight.
**＋** A sprint line whose Case updates no sprint page closes `[-] … · sprint · defer`, and the decision lines of that Case stand.
**＋** A backlog line whose Case defers its page again closes `[-] … · backlog · defer case N`. A backlog line whose Case neither ends the item nor defers it again closes `[-] … · backlog · kept`, and the decision lines of that Case stand.
**＋** The agent closes the line in the reply that carries the decision lines of Case N, so the frontier check of `uv run --project .guppi guppi prespec --check` of `rule-prespec` finds nothing on it.
**－** Any other backlog item ends by the ratification of Case N, and the check of `rule-prespec` judges the closers as before.

## Result

2026-11-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
