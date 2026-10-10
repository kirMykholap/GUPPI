---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the Frontier is written and the readings of /hi taken before the reply that acknowledges the opening Case of a sprint, and whether that reply shows the Frontier, holds the readings in its LEDGER block and puts the Ask questions before the question which item is next
method: by hand, at the Retro of the session of case 769, the new Render of rule-orchestration in its spec.md read against the Criterion
origin: raw/2026-10-10/1913/ledger.md#case-769.4
sprint: plugin
created: 2026-10-10
tags: [session, workflow, sprint]
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

2026-10-10, Retro of session 1913, by hand: the new Render of rule-orchestration in spec.md (case 769.4) read against the Criterion — frontier.md written and the readings of /hi taken before the reply that acknowledges the opening Case; its LEDGER block holds the reading lines after the decision lines; its ## Frontier shows the new Frontier; the open A lines stand after the Frontier and before the question which item is next; the four parts and no tool call after the block stand

## History

- 2026-10-10 created · [[decision-case-769.4]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L37
