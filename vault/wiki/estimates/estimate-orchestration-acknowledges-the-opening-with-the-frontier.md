---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the Frontier is written and the readings of /hi taken before the reply that acknowledges the opening Case of a sprint, and whether that reply shows the Frontier, holds the readings in its LEDGER block and puts the Ask questions before the question which item is next
method: "by hand: the Render of rule-orchestration in vault/wiki/orchestration.md read against the Criterion"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, sprint]
core: true
---

## Criterion

When:
The person ratifies the opening Case of `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
Before that reply, the agent writes `raw/<date>/<hi HHMM>/frontier.md` as `rule-skill-hi` sets it, and takes each reading of an open `W` line whose whole method runs now.
**＋** The reply keeps the four parts of an acknowledging reply, in their order.
**＋** Its `LEDGER` block holds the decision lines of the opening Case, then the `estimate[...]` line of each reading taken.
**＋** Its `## Frontier` shows the lines of the new `raw/<date>/<hi HHMM>/frontier.md`.
**＋** After the lines of the Frontier and before the question which item is next, the reply puts each open `A` line to the person as `rule-skill-hi` sets it: the Estimate by slug and its question.
**－** No tool call follows the `LEDGER` block in the same reply.

## Result

2026-10-10, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
