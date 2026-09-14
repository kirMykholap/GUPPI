---
type: decision
case: "64"
status: archived
defer: ["[[rule-work-mode]]", "[[rule-subagent-guppi]]"]
supersedes: ["[[decision-case-29]]"]
superseded_by: ["[[decision-case-78]]"]
origin: raw/2026-09-12/ledger.md#case-64
sprint: migration
created: 2026-09-12
tags: []
---

## Context

Case 29 (2026-09-10) deferred `rule-work-mode` and `rule-subagent-guppi` together: Work
Mode as ratified rules — the plan, the branch and baseline, the subagent that executes
and never decides, the four hooks of the draft in `docs/migration/rule-work-mode.md`.
Since then case 59.3 dropped the separate executable plan (`plan.md`,
`to-executable-plan`): the `tasks` blocks of the Spec are what a subagent executes. The
owner's clause of case 59 belongs here: a fork in Work Mode is not a return to Plan
Mode — the subagent stops, the fork is written as a short-form Case under `## Deferred`,
shown at Retro, worked next session.

## Problem

Work Mode runs on the draft and on habit; `rule-work-mode` and `rule-subagent-guppi` are
placeholders and lint orphans. The draft has to be reconciled with 59.3 and the fork
clause before its Cases are formed. Postponed four times now.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-64
- 2026-09-12 superseded by decision-case-78 · [[decision-case-78]]
- 2026-09-13 archived · superseded
- 2026-09-13 archived · cleanup
