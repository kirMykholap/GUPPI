---
type: decision
case: "539.3"
status: archived
update: ["[[rule-sprint]]", "[[entity-sprint-migration]]", "[[rule-backlog]]", "[[rule-skill-hi]]"]
origin: raw/2026-09-30/0248/ledger.md#case-539.3
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, librarian, sprint]
---

## Problem

`generate` moves sprint items by a count of put-offs. That count always reaches the finish conditions of the sprint, which can only be read at the close, so the move turns them into put-off work in `backlog.md`. The person wants no line of the sprint page to move without their request. They also want the finish conditions to stand only under Done when, so that each milestone holds exactly the items whose closing closes it.

## History

- 2026-09-30 created · raw/2026-09-30/0248/ledger.md#case-539.3
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
