---
type: decision
case: "539.1"
status: archived
update: ["[[rule-sprint]]", "[[rule-page-generation]]", "[[estimate-sprint-items-move-only-by-a-case]]"]
delete: ["[[estimate-sprint-drops-an-emptied-milestone]]"]
origin: raw/2026-09-30/0248/ledger.md#case-539.1
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, librarian, sprint, ledger]
---

## Problem

`generate` moves sprint items by a count of put-offs. That count always reaches the finish conditions of the sprint, which can only be read at the close, so the move turns them into put-off work in `backlog.md`. The person wants no line of the sprint page to move without their request. They also want the finish conditions to stand only under Done when, so that each milestone holds exactly the items whose closing closes it.

## History

- 2026-09-30 created · raw/2026-09-30/0248/ledger.md#case-539.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
