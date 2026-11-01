---
type: decision
case: "983"
status: current
update: ["[[rule-backlog]]", "[[estimate-backlog-checks-the-file]]"]
origin: raw/2026-11-01/1721/ledger.md#case-983
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, librarian, sprint]
---

## Problem

`guppi backlog --check` goes red in the Baseline of any session that puts off an item already on the list, though only the librarian's run of that session can write the new count, so every such session explains the same red again.

## Recommend

- **What should the check do with the put-offs of the session that is running**
  - Recommended: (b) the check accepts the file in either of two forms: the render with every Frontier, or the render without the Frontier of the newest session; the writer does not change.
  - Answer: agreed, (b).

## History

- 2026-11-01 created · raw/2026-11-01/1721/ledger.md#case-983
