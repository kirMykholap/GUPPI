---
type: decision
case: "534"
status: archived
children: ["[[decision-case-534.1]]", "[[decision-case-534.2]]"]
origin: raw/2026-09-30/0248/ledger.md#case-534
sprint: migration
created: 2026-09-30
tags: [harness, session, render, hooks]
---

## Problem

The Bash tool starts each Python process of a session in the locale's code page. Unless each command sets the encoding, a dash reaches the agent as U+FFFD and other characters stop the script. That already produced one false reading and one false Frontier item. The harness should set UTF-8 once, for every Python process of the session, through a ratified rule.

## History

- 2026-09-30 created · raw/2026-09-30/0248/ledger.md#case-534
- 2026-09-30 updated: the parent page written for a Case of session 0248 by the librarian run of session 1306, kept as written and signed after the fact (case 550) · [[decision-case-550]]
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
