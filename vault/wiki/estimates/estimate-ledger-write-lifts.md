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
the ledger is untouched. With `stop_hook_active` true it exits 0 and writes nothing. In a
live session, the last lines of this slice reach `raw/2026-09-09/ledger.md` written by the
hook, not by hand.

## Method

pytest in `tests/test_ledger.py` with piped payloads against a temp vault; the live
reading is taken once by hand and written into the estimate line.

## Result

Passing, two live readings on 2026-09-09 plus the suite. Reading 1, first reply of session
C, pre-15.1 contract: eight bare estimate lines reached `raw/2026-09-09/ledger.md`, once
each. Reading 2, the reply acknowledging case 15, post-15.1 contract: five lines inside a
```` ```LEDGER ```` block landed at 17:09:59 with the time prefix, once each; a bare copy
and an untagged fence in earlier replies were ignored. `tests/test_ledger.py`: 16 tests
green (31 in the suite).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-10
- 2026-09-09 updated: criterion follows the LEDGER block and the time prefix · raw/2026-09-09/ledger.md#case-15.1
- 2026-09-09 status: pending → passed · written by hand, no generator yet
