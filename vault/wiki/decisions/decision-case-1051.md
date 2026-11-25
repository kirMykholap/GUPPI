---
type: decision
case: "1051"
status: current
create: ["[[estimate-sprint-ticks-a-read-one-off-estimate]]"]
update: ["[[rule-sprint]]"]
origin: raw/2026-11-25/0605/ledger.md#case-1051
sprint: plugin
created: 2026-11-25
tags: [harness, sprint, session, workflow, librarian]
---

## Problem

The sprint view leaves a one-off Estimate unticked after it is read and failed, while the sprint page calls it done.

## Recommend

- **What happens to the failed one-off check of the sprint page**
  - Recommended: (b) make done mean read for a one-off check; the failure stays as the record.
  - Answer: agreed, (b); case 1046 carries it.
- **Whether `guppi check` stops showing red for a failed one-off check**
  - Recommended: (a) keep the red line until the close.
  - Answer: agreed, (a).
- **Whether the sprint page can reach the status "built" with a failed one-off check**
  - Recommended: (a) the sprint page stays draft until the close.
  - Answer: agreed, (a).
- **How `sprint.md` shows a one-off check that was read and failed**
  - Recommended: (b) tick a read one-off check, its status `failed` kept after it.
  - Answer: agreed, (b).

## History

- 2026-11-25 created · raw/2026-11-25/0605/ledger.md#case-1051
