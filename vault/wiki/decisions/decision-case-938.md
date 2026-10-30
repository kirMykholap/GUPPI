---
type: decision
case: "938"
status: current
update: ["[[rule-orchestration]]", "[[estimate-orchestration-names-related-cases-in-the-dispatch]]"]
origin: raw/2026-10-30/2005/ledger.md#case-938
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness]
---

## Problem

The test of related Cases leaves out a Case that set the form of a text a check reads. So a later Case that writes text of that kind is built without it, and it can bring back the form that the earlier Case fixed.

## Recommend

- **Which Cases the test of related Cases adds**
  - Recommended: (b) a Case that sets the form of a text a check reads, or how the check reads it, when the item's Case may write text of that kind.
  - Answer: agreed, (b).
- **How the change is checked**
  - Recommended: (a) replace the Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch`, with its `purpose` and `method` set anew.
  - Answer: agreed, (a).

## History

- 2026-10-30 created · raw/2026-10-30/2005/ledger.md#case-938
