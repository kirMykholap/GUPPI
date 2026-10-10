---
type: lesson
kind: error
root_cause: the agent wrote the preview before choosing the pages that own the behaviour — the comparison lives in `guppi/ratified.py`, which has no page of its own — and did not check the preview against the item lines of `tasks` before showing
status: archived
origin: raw/2026-09-24/2214/ledger.md#L50
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Trigger

the `ratification` section of Case 407.5 showed the line `decision[case 407.5][update][guppi-ratified-comparison-placeholder]`, a slug no page carries, and the right lines came only after the rule

## Root cause

the agent wrote the preview before choosing the pages that own the behaviour — the comparison lives in `guppi/ratified.py`, which has no page of its own — and did not check the preview against the item lines of `tasks` before showing

## History

- 2026-09-25 created · raw/2026-09-24/2214/ledger.md#L50
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
