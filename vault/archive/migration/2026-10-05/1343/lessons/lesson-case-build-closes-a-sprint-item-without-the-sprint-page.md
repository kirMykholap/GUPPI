---
type: lesson
kind: error
root_cause: the frame of case-guppi does not carry the pre-spec rule that a Case which closes a sprint item also updates the sprint page (case 314.2).
status: archived
insight: "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"
origin: raw/2026-09-29/1432/ledger.md#L32
sprint: migration
created: 2026-09-29
tags: [harness, workflow]
---

## Trigger

Case 510 closed the Slice 4 item of the sprint with an update of its Estimate alone; /pre-spec found no update of entity-sprint-migration, and the Case was built again after a new round.

## Root cause

the frame of case-guppi does not carry the pre-spec rule that a Case which closes a sprint item also updates the sprint page (case 314.2).

## History

- 2026-09-29 created · raw/2026-09-29/1432/ledger.md#L32
- 2026-09-29 updated: clustered under insight-workflow-case-schema-silent-on-what-the-scripts-accept (synthesis) · raw/2026-09-29/1432/ledger.md#L32
- 2026-10-05 archived · insight actioned
- 2026-10-05 archived · cleanup
