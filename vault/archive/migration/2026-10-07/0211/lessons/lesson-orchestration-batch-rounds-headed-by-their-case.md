---
type: lesson
kind: error
root_cause: rule-orchestration numbers the questions of a batch `<Case id>.Q<n>` but sets no way to mark where the round of each Case begins, so the agent added a heading, which the check reads as its own text before a round
status: archived
insight: "[[insight-orchestration-items-taken-together-unruled]]"
origin: raw/2026-10-07/0211/ledger.md#L16
sprint: migration
created: 2026-10-07
tags: [orchestration]
---

## Trigger

in session 0211 the reply that showed the rounds of Cases 697 and 698 together put a heading of the agent's own, `### Case 697 — C4`, before the first Context paragraph; the Stop check of rule-case-check refused it and the rounds were shown a second time

## Root cause

rule-orchestration numbers the questions of a batch `<Case id>.Q<n>` but sets no way to mark where the round of each Case begins, so the agent added a heading, which the check reads as its own text before a round

## History

- 2026-10-07 created · raw/2026-10-07/0211/ledger.md#L16
- 2026-10-07 updated: clustered under insight-orchestration-items-taken-together-unruled (synthesis) · raw/2026-10-07/0211/ledger.md#L16
- 2026-10-07 archived · insight actioned
- 2026-10-07 archived · cleanup
