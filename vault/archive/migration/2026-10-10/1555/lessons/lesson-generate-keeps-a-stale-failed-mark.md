---
type: lesson
kind: error
root_cause: apply() sets `applied` on success but never removes a `failed` left by an earlier run, so an entry that later applies keeps both marks and every reader of the yaml sees a failure that is over
status: archived
origin: raw/2026-09-10/ledger.md#L130
sprint: migration
created: 2026-09-10
tags: [harness, ledger]
---

## Trigger

after Case 48 the old-harness entry carries `applied: '16:08:18'` beside its old `failed: generate: old-harness: no page to delete`, and the brief flags it as failed

## Root cause

apply() sets `applied` on success but never removes a `failed` left by an earlier run, so an entry that later applies keeps both marks and every reader of the yaml sees a failure that is over

## History

- 2026-09-11 created · raw/2026-09-10/ledger.md#L130
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
