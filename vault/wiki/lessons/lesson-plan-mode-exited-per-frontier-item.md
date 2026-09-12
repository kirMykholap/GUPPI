---
type: lesson
kind: error
root_cause: CLAUDE.md says Plan Mode does not end while a Frontier item is neither ratified nor deferred, but nothing says what a Frontier item with no decision in it becomes; the agent treated a mechanical item as a plan of its own instead of one line in the Work Mode order of the single Spec; one Spec per Plan Mode, ExitPlanMode once, when the owner closes the discussion
status: new
origin: raw/2026-09-12/ledger.md#L1
sprint: migration
created: 2026-09-12
tags: [session, workflow]
---

## Trigger

the owner said "начнем с 1, дальше я скажу" about the Frontier; the agent wrote a plan for item 1 alone, ran pre-task on an empty decision list and called ExitPlanMode; the owner rejected it: the phrase named the order of discussion, not the scope of the plan

## Root cause

CLAUDE.md says Plan Mode does not end while a Frontier item is neither ratified nor deferred, but nothing says what a Frontier item with no decision in it becomes; the agent treated a mechanical item as a plan of its own instead of one line in the Work Mode order of the single Spec; one Spec per Plan Mode, ExitPlanMode once, when the owner closes the discussion

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L1
