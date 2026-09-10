---
type: lesson
kind: error
root_cause: Vault takes the yaml's date for `created` and reuses it for History and log lines; with a multi-date walk the date of the yaml and the date of the run differ, and History and the log should carry the run's date
status: new
estimates: [estimate-generate-walk-history-dated-by-yaml]
origin: raw/2026-09-10/ledger.md#L98
sprint: migration
created: 2026-09-10
tags: [harness, ledger]
---

## Trigger

the walk of Case 43 wrote two `2026-09-09` cascade lines into log.md after the `2026-09-10` lines, and rule-materialize ends its History with a 2026-09-09 line written today

## Root cause

Vault takes the yaml's date for `created` and reuses it for History and log lines; with a multi-date walk the date of the yaml and the date of the run differ, and History and the log should carry the run's date

## Estimates

- [[estimate-generate-walk-history-dated-by-yaml]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L98
