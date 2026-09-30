---
type: decision
case: "539"
status: current
children: ["[[decision-case-539.1]]", "[[decision-case-539.2]]", "[[decision-case-539.3]]", "[[decision-case-539.4]]"]
origin: raw/2026-09-30/0248/ledger.md#case-539
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, librarian, sprint, ledger]
---

## Problem

`generate` moves sprint items by a count of put-offs. That count always reaches the finish conditions of the sprint, which can only be read at the close, so the move turns them into put-off work in `backlog.md`. The person wants no line of the sprint page to move without their request. They also want the finish conditions to stand only under Done when, so that each milestone holds exactly the items whose closing closes it.

## History

- 2026-09-30 created · raw/2026-09-30/0248/ledger.md#case-539
- 2026-09-30 updated: the parent page written for a Case of session 0248 by the librarian run of session 1306, kept as written and signed after the fact (case 550) · [[decision-case-550]]
