---
type: lesson
kind: error
root_cause: the plan file still holds the old body of Case 471 (given, when, then, its then block and tasks) under the parent heading, before 471.1; its replace pairs on rule-documentation consume the anchors first, so the same pairs of 471.1 miss. The hook of rule-spec-write replaced the parent's prose from the new answer and kept the body sections the new answer leaves to the sub-cases.
status: archived
insight: "[[insight-spec-write-parent-body-kept-on-re-ratification]]"
origin: raw/2026-09-28/0000/ledger.md#L25
sprint: migration
created: 2026-09-28
tags: [hooks, workflow, session]
---

## Trigger

Case 471, ratified whole, was built again after pre-spec as a parent with sub-cases 471.1 and 471.2 and ratified again; the Stop check `guppi ratified` refused: the replace anchors of 471.1 on rule-documentation are not in the page.

## Root cause

the plan file still holds the old body of Case 471 (given, when, then, its then block and tasks) under the parent heading, before 471.1; its replace pairs on rule-documentation consume the anchors first, so the same pairs of 471.1 miss. The hook of rule-spec-write replaced the parent's prose from the new answer and kept the body sections the new answer leaves to the sub-cases.

## History

- 2026-09-28 created · raw/2026-09-28/0000/ledger.md#L25
- 2026-10-01 updated: clustered under insight-spec-write-parent-body-kept-on-re-ratification (synthesis) · raw/2026-10-01/1441/ledger.md#L32
- 2026-10-03 archived · insight actioned
- 2026-10-03 archived · cleanup
