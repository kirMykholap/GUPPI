---
type: decision
case: "552.2"
status: archived
parent: "[[decision-case-552]]"
create: ["[[estimate-ledger-write-refuses-a-line-it-cannot-read]]"]
update: ["[[rule-ledger-write]]"]
origin: raw/2026-09-30/1736/ledger.md#case-552.2
sprint: migration
created: 2026-09-30
tags: [session, hooks, harness, ledger]
---

## Recommend

- **What the ledger hook does with a line `parse_line` cannot read**
  Recommended: (b) refuse it at once: not written, exit 2 with one stderr line when it stands in the reply just finished.
  Answer: (b) refuse it at once.

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#case-552.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
