---
type: decision
case: "890"
status: current
children: ["[[decision-case-890.1]]", "[[decision-case-890.2]]", "[[decision-case-890.3]]", "[[decision-case-890.4]]"]
origin: raw/2026-10-26/0118/ledger.md#case-890
sprint: plugin
created: 2026-10-26
tags: [hooks, harness, workflow, session]
---

## Problem

The check of a Case reads another Case built again from the plan as last ratified and looks for its words in its current file, so a sibling built again makes the check fail until it is ratified again; and one Case of a batch with a stored finding holds back the showing of every Case of the batch.

## Recommend

- **Which text of another Case the check uses**
  - Recommended: (a) the last built text, for every check.
  - Answer: agreed, (a).
- **What happens when the check refuses one Case of a batch**
  - Recommended: (a) the clean Cases are shown at once, and the faulty one goes back.
  - Answer: agreed, (a).
- **The other put-off on `rule-orchestration`**
  - Recommended: (a) it stays out of this Case.
  - Answer: agreed, (a).
- **Where the clean Cases go first**
  - Recommended: (a) in both places, a batch before `/pre-spec` and the loop after its findings.
  - Answer: agreed, (a).
- **How the change to the check is checked**
  - Recommended: (a) a new check, with the clash check reworded.
  - Answer: agreed, (a).
- **How the change to the batch is checked**
  - Recommended: (a) a new check for the batch, and the loop check reworded.
  - Answer: agreed, (a).

## History

- 2026-10-26 created · raw/2026-10-26/0118/ledger.md#case-890
