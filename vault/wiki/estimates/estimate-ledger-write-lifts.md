---
type: estimate
kind: QA
status: pending
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

Given a `Stop` payload whose reply carries one bare decision line, the same line inside a
fence, and one bare estimate line, with a `hi` recorded for the session: the ledger gains
exactly the two bare lines, verbatim, once, even when the hook runs twice on the same
payload. Without `hi` the hook exits 2 with a reason naming the count and the session, and
the ledger is untouched. With `stop_hook_active` true it exits 0 and writes nothing. In a
live session, the last lines of this slice reach `raw/2026-09-09/ledger.md` written by the
hook, not by hand.

## Method

pytest in `tests/test_ledger.py` with piped payloads against a temp vault; the live
reading is taken once by hand and written into the estimate line.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-10
