---
type: lesson
kind: error
root_cause: parse_line raised instead of returning None on a line off its grammar, and the ledger hook swallowed every exception with exit 0, so the one bad line of the transcript blocked every later line in silence
status: archived
origin: raw/2026-09-30/1736/ledger.md#L43
sprint: migration
created: 2026-09-30
tags: [session, hooks, ledger]
---

## Trigger

in session 1736 the main agent wrote a reading with a space between its brackets; parse_line raised AttributeError on it, the ledger hook caught the error and exited 0, and for two Stops no ledger line of the session was written, nor Case 551 into the plan, while every reply looked recorded

## Root cause

parse_line raised instead of returning None on a line off its grammar, and the ledger hook swallowed every exception with exit 0, so the one bad line of the transcript blocked every later line in silence

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#L43
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
