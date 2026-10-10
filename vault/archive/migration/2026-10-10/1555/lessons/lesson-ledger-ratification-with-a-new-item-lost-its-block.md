---
type: lesson
kind: error
root_cause: a reply that ratifies and adds an item in one message was answered as the new item alone; the acknowledging reply — the LEDGER block first — was skipped because the agent's turn went straight to the next Case, and nothing between ratification and pre-spec checks that each ratified Case has its lines
status: archived
origin: raw/2026-09-23/0034/ledger.md#L42
sprint: migration
created: 2026-09-23
tags: [session, ledger, workflow]
---

## Trigger

the person's reply "Ратифицирую. И думаю, что lint должен проверять, что в поле всего одна ссылка" ratified Case 361 and raised a new item; the agent wrote 361 into the Spec, closed its Frontier line and showed Case 362, but no reply carried the LEDGER block of 361, and /pre-spec was refused by guppi gate: two items of the Spec have no ledger line

## Root cause

a reply that ratifies and adds an item in one message was answered as the new item alone; the acknowledging reply — the LEDGER block first — was skipped because the agent's turn went straight to the next Case, and nothing between ratification and pre-spec checks that each ratified Case has its lines

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#L42
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
