---
type: decision
case: "680"
status: current
update: ["[[entity-sprint-migration]]"]
supersedes: ["[[decision-case-642]]"]
origin: raw/2026-10-05/2249/ledger.md#case-680
sprint: migration
created: 2026-10-05
tags: [sprint, workflow]
---

## Problem

Notes that no Case took up hold places in the backlog that every session loads, and they would stay there after the sprint closes. The line of a page that Case 676 deletes would leave a link to a deleted page.

## Recommend

- **What happens to the postponed close of the sprint**
  - Recommended: (a) retire the postponement in this Case; the close stays in view as the Slice 5 milestone in `sprint.md`.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed with the main agent's recommendation on Case 676 that this Case also removes the line of `[[rule-subagent-guppi]]` from `## Backlog`.
  - Taken: a second `replace` pair removes that line.
- **Change**
  - Asked: the person agreed to the fix of a pre-spec finding: `context` must name `estimate-sprint-migration-merges`, whose Criterion speaks of a line of the `## Backlog`, and say why it stands.
  - Taken: `context` names that Estimate and the search behind it; the Criterion stands because the merge line stays.

## History

- 2026-10-06 created · raw/2026-10-05/2249/ledger.md#case-680
