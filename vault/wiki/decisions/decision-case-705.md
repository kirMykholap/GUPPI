---
type: decision
case: "705"
status: current
children: ["[[decision-case-705.1]]", "[[decision-case-705.2]]"]
origin: raw/2026-10-07/0636/ledger.md#case-705
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness]
---

## Problem

When the person drops a change to a ratified Case, its file keeps the changed text that nobody ratified. That file is newer than the Case's last decision line, so the hook of `rule-prespec-onward` stays silent for the rest of Plan Mode.

## Recommend

- **What dropping an approved Case after a change covers**
  - Recommended: (a) drop the change and keep the approved Case; taking back the whole decision is left not done and goes to the handoff.
  - Answer: agreed, (a).
- **How the file of the approved Case comes back**
  - Recommended: (a) `case-guppi` undoes its edits and answers with its summary; the main agent shows the Case again, and the person ratifies it again with the same lines.
  - Answer: agreed, (a).
- **What happens to `recommend` when the change is undone**
  - Recommended: (a) undo every section but `recommend`, which keeps its items and gains a `**Change**` item that records the drop.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/0636/ledger.md#case-705
