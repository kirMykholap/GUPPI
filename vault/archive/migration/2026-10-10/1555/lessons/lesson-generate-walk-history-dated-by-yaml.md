---
type: lesson
kind: error
root_cause: Vault takes the yaml's date for `created` and reuses it for History and log lines; with a multi-date walk the date of the yaml and the date of the run differ, and History and the log should carry the run's date
status: archived
origin: raw/2026-09-10/ledger.md#L98
sprint: migration
created: 2026-09-10
tags: [harness, ledger]
---

## Trigger

the walk of Case 43 wrote two `2026-09-09` cascade lines into log.md after the `2026-09-10` lines, and rule-materialize ends its History with a 2026-09-09 line written today

## Root cause

Vault takes the yaml's date for `created` and reuses it for History and log lines; with a multi-date walk the date of the yaml and the date of the run differ, and History and the log should carry the run's date

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L98
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
