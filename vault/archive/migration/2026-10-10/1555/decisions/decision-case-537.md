---
type: decision
case: "537"
status: archived
create: ["[[estimate-case-check-refuses-a-letter-outside-the-script]]"]
update: ["[[rule-case-check]]", "[[insight-case-form-chat-form-read-by-no-script]]"]
origin: raw/2026-09-30/0248/ledger.md#case-537
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow, session]
---

## Problem

A Case with Russian letters in its name, `context` or `problem` reaches the person, because the check of each answer of `case-guppi` does not run the language finding. `/pre-spec` finds the letters only later, and the Case is built and ratified again. The insight that records this pattern is still open.

## History

- 2026-09-30 created · raw/2026-09-30/0248/ledger.md#case-537
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
