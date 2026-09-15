---
type: lesson
kind: error
root_cause: find_item in materialize.py matches a then item by slug only, while the schema's item for a Rule-class file carries file and no slug; the one test of the case seeds both keys, so it stayed green while every Spec written by the schema was marked incomplete
status: new
origin: raw/2026-09-15/1110/ledger.md#L18
sprint: migration
created: 2026-09-15
tags: [harness, librarian]
---

## Trigger

13 file entries of raw/2026-09-14/1633/materialize.yaml and the entry of 133 in 1229 marked incomplete [then] although each had its then item, written with file and change as case-schema.md says; the brief of two runs listed them as "a Rule-class update carries no then block"

## Root cause

find_item in materialize.py matches a then item by slug only, while the schema's item for a Rule-class file carries file and no slug; the one test of the case seeds both keys, so it stayed green while every Spec written by the schema was marked incomplete

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#L18
