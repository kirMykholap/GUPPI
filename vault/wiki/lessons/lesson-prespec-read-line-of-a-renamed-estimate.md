---
type: lesson
kind: error
root_cause: check_tasks of guppi/prespec.py matches a read line by the slug of the then item, the old slug of a rename, and the Case schema does not say which slug of a rename a read line names
status: clustered
insight: "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"
origin: raw/2026-09-25/1228/ledger.md#L16
sprint: migration
created: 2026-09-25
tags: [session, workflow]
---

## Trigger

Cases 419.1 and 419.2 rename an Estimate and named its read line by the new slug; the Stop hook reported "has no task line" after the ratification

## Root cause

check_tasks of guppi/prespec.py matches a read line by the slug of the then item, the old slug of a rename, and the Case schema does not say which slug of a rename a read line names

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#L16
- 2026-09-25 updated: clustered into insight-workflow-case-schema-silent-on-what-the-scripts-accept · raw/2026-09-25/1228/ledger.md#L16
