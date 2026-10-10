---
type: lesson
kind: error
root_cause: neither the check of the case file nor guppi prespec --check nor ask-guppi judges the fields that materialize requires of a create item, so a missing type reaches the ratified Spec unseen
status: archived
origin: raw/2026-10-08/2352/ledger.md#L40
sprint: migration
created: 2026-10-08
tags: [case-build, prespec, schema]
---

## Trigger

the create items of rule-skill-sprint-open (743.6) and rule-skill-sprint-close (743.8) hold kind, purpose, enforcement and sections but no type: rule, and uv run guppi materialize --show marks all four create entries incomplete: [type] after the Case was ratified twice and passed /pre-spec

## Root cause

neither the check of the case file nor guppi prespec --check nor ask-guppi judges the fields that materialize requires of a create item, so a missing type reaches the ratified Spec unseen

## History

- 2026-10-09 created · raw/2026-10-08/2352/ledger.md#L40
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
