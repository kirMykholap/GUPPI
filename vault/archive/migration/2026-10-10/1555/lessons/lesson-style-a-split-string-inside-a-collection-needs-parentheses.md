---
type: lesson
kind: error
root_cause: a finding's message is long enough that the agent splits it over two source lines by habit, and ruff refuses an unparenthesized implicit concatenation inside a collection; the forms that pass are the parts wrapped in their own parentheses, or the message held in a module constant and reused, which the test file already does with `NO_FORM`.
status: archived
origin: raw/2026-09-22/2046/ledger.md#L38
sprint: migration
created: 2026-09-22
tags: [tests, harness]
---

## Trigger

`make style` failed three times in this session's Work Mode, each time ISC004 on a new test's `assert out.splitlines() == ["…" "…"]` — two string parts concatenated implicitly inside a list.

## Root cause

a finding's message is long enough that the agent splits it over two source lines by habit, and ruff refuses an unparenthesized implicit concatenation inside a collection; the forms that pass are the parts wrapped in their own parentheses, or the message held in a module constant and reused, which the test file already does with `NO_FORM`.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#L38
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
