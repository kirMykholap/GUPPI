---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the list of the rounds of a batch marks where each Case's round begins by its Context label, which names the Case and its item, and by its question numbers, with no heading of the main agent's own
method: "by hand at the Retro of this session: the new Render of rule-orchestration in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-07/0211/ledger.md#case-699.5
sprint: migration
created: 2026-10-07
tags: [session, workflow]
---

## Criterion

When:
In Plan Mode before `/pre-spec`, the main agent shows in one list the rounds of `case-guppi` that came back for a batch of Cases, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The `**Context:**` paragraph of each first round on an item opens with a label that names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`.
**＋** A later round, which has no Context paragraph, is marked by its question numbers `<Case id>.Q<n>` alone.
**＋** No heading or other line of the main agent's own stands before a round to mark where it begins, so the reply opens with a Context label or a question line, which the check of `rule-case-check` accepts.
**－** A round shown alone, outside a batch, keeps its `**Context:**` label as `case-guppi` gave it, translated.

## Result

2026-10-07, Retro, the new Render of rule-orchestration in the Spec (case 699.5): its anchor stands once; the Context label of each first round names its Case and its Frontier item, such as `**Context — Case 7 (C2):**`, with no heading of the agent's own

## History

- 2026-10-07 created · [[decision-case-699.5]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L45
