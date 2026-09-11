---
type: lesson
kind: error
root_cause: the Stop hook fires when the assistant's turn ends in text; a reply whose last act is a tool call whose result comes back as the next turn (Skill, ExitPlanMode) has no Stop, so its LEDGER block is never read; a reply that carries a LEDGER block must end in text, after the tool call, or the ledger writer needs a second event
status: new
origin: raw/2026-09-10/ledger.md#L119
sprint: migration
created: 2026-09-10
tags: [harness, hooks, ledger]
---

## Trigger

the LEDGER blocks of the two replies that acknowledged Cases 48 and 49 never reached ledger.md; the first reply ended with the Skill call of /pre-task, the second with ExitPlanMode; the lines were found missing at /retro and re-emitted there

## Root cause

the Stop hook fires when the assistant's turn ends in text; a reply whose last act is a tool call whose result comes back as the next turn (Skill, ExitPlanMode) has no Stop, so its LEDGER block is never read; a reply that carries a LEDGER block must end in text, after the tool call, or the ledger writer needs a second event

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L119
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
