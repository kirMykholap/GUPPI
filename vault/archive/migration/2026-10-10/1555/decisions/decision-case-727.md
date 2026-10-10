---
type: decision
case: "727"
status: archived
update: ["[[rule-case-protocol]]"]
supersedes: ["[[decision-case-722.3]]"]
origin: raw/2026-10-08/0050/ledger.md#case-727
sprint: migration
created: 2026-10-08
tags: [session, workflow, ledger]
---

## Problem

`case-schema.md` says that a Frontier line is always closed again by the Case that replaces the earlier one. A Case taken back from a sprint or a backlog item closes its line by a closer that names no Case, and so the schema contradicts `orchestration.md`.

## Recommend

- **How the sentence on the Frontier line is fixed**
  - Recommended: (a) keep the sentence and add the take-back as an exception that points to `orchestration.md`.
  - Answer: agreed, (a).
- **What checks that the fix is done**
  - Recommended: (a) no new check; `estimate-case-protocol-loaded` checks the render and `estimate-orchestration-takes-back-a-ratified-case` keeps checking the behaviour.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/0050/ledger.md#case-727
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
