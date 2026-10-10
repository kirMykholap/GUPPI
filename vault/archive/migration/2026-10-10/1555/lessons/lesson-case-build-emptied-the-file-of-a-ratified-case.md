---
type: lesson
kind: error
root_cause: the Render of rule-case-build told case-guppi to empty a file it leaves behind under another number whatever its Case, against the rule of rule-orchestration that the file of a Case with a decision line is never emptied
status: archived
origin: raw/2026-10-07/2114/ledger.md#L27
sprint: migration
created: 2026-10-07
tags: [harness, workflow]
---

## Trigger

asked to build ratified Case 722 again without one ledger line, case-guppi emptied case-722.md, moved the Case to the new number 724, and wrote case-722.md back from the store only when the person dropped the change

## Root cause

the Render of rule-case-build told case-guppi to empty a file it leaves behind under another number whatever its Case, against the rule of rule-orchestration that the file of a Case with a decision line is never emptied

## History

- 2026-10-07 created · raw/2026-10-07/2114/ledger.md#L27
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
