---
type: decision
case: "993"
status: current
children: ["[[decision-case-993.1]]", "[[decision-case-993.2]]"]
origin: raw/2026-11-01/2227/ledger.md#case-993
sprint: plugin
created: 2026-11-01
tags: [session, workflow, ledger]
---

## Problem

`estimate-orchestration-acknowledging-reply` stands `passed` while the `STOP:` line of its Criterion has had no reading, and that line can be read only in a session that has the event it needs.

## Recommend

- **How the unread STOP: line gets a reading**
  - Recommended: (a) split the `STOP:` line into its own Estimate, whose `method` waits for an acknowledging reply after `/pre-spec` that waits for the person's word; the old Criterion is replaced whole without it, points to the new Estimate, goes `pending` and is read at the Retro of this session.
  - Answer: agreed, (a).

## History

- 2026-11-02 created · raw/2026-11-01/2227/ledger.md#case-993
