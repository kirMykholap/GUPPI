---
type: estimate
kind: QA
status: passed
target: rule-ledger-write
origin: raw/2026-09-09/ledger.md#case-10
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, ledger]
---

## Context

This is the hook the whole migration waits on: item 5 of the definition of done says the
final session's ledger is written by it, not by hand. The unit cases pin the contract; the
live reading proves the registration.

## Criterion

Given a `Stop` payload whose reply carries a decision line and an estimate line inside a
`LEDGER` block, and a third decision line both bare and inside an untagged fence, with a
`hi` recorded for the session: the ledger gains exactly the two lines of the block, their
text verbatim and the time of writing in front, once, even when the hook runs twice on the
same payload; a line already present by hand, without a time, is not written again.
Without `hi` the hook exits 2 with a reason naming the count and the session, and
the ledger is untouched. With `stop_hook_active` true it exits 0 and writes nothing. With the `session-start` and the `hi` in yesterday's event log and only `tool` lines
in today's, the lines are written into today's ledger. A reply carrying a `LEDGER` block
that ends in `/pre-task` reaches the ledger once, at the next `Stop` of the session. In a
live session, the last lines of this slice reach `raw/2026-09-09/ledger.md` written by the
hook, not by hand.

## Method

pytest in `tests/test_ledger.py` with piped payloads against a temp vault; the live
reading is taken once by hand and written into the estimate line.

## Result

tests/test_ledger.py 28 green with the midnight window (a start and hi in yesterday's log, only tool lines today, writes into today's ledger; no start on any date refuses; another session's start today closes yesterday's window) and the read-back (an earlier reply's block lands at the next Stop, a subagent's block is ignored, a line in an earlier day's ledger is not written again, a missing transcript falls back to the last message); live 2026-09-11 session H: the reply of 11:32 carried three estimate lines and a lesson in a LEDGER block and ended in the /pre-task Skill call, no Stop fired, the ledger stayed at 67 lines; the next reply ended in text and its Stop at 11:32:59 wrote the four lines once, read from the transcript, with that time

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-10
- 2026-09-09 updated: criterion follows the LEDGER block and the time prefix · raw/2026-09-09/ledger.md#case-15.1
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-11 updated: the midnight window added to the criterion; pending until the reading · [[decision-case-55.1]]
- 2026-09-11 updated: the transcript read-back added to the criterion; pending until the live reading · [[decision-case-55.2]]
- 2026-09-11 status: pending → passed · raw/2026-09-11/ledger.md#L72
