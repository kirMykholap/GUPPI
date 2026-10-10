---
type: decision
case: "671"
status: archived
children: ["[[decision-case-671.1]]", "[[decision-case-671.2]]"]
origin: raw/2026-10-05/1831/ledger.md#case-671
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow, session, ledger]
---

## Problem

A Case ratified in the session and built again under its number with a target renamed or dropped passes every check until the Spec hook refuses its old line. A whole new Case then has to supersede it.

## Recommend

- **How the gap is closed**
  - Recommended: (a) the check of a rebuilt Case also sends it back when a ledger line of one of its numbers has no item under that number, with the new number and the marks, and the draft `rule-ledger-line-withdrawn-on-re-ratification` is deleted.
  - Answer: agreed, (a).
- **How the fix is checked**
  - Recommended: (a) a new Estimate under `rule-case-check` with its own tests; the Estimate of the layout check stays as it is.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/1831/ledger.md#case-671
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
