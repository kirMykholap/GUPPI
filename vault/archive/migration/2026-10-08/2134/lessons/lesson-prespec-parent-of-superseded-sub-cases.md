---
type: lesson
kind: error
root_cause: "`check_ratified` excepts only the ids a `{supersedes:case N}` of the window names; a parent Case with no ledger lines of its own, whose every sub-case is superseded, is named by no supersedes, so its section in the ratified copy stays a finding"
status: archived
insight: "[[insight-case-check-a-case-id-leaves-only-by-a-supersedes-line]]"
origin: raw/2026-09-24/2214/ledger.md#L26
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Trigger

after Case 412 superseded each of 407.1–407.5, `prespec --check` still printed `case 407: in the ratified copy, not in the plan`

## Root cause

`check_ratified` excepts only the ids a `{supersedes:case N}` of the window names; a parent Case with no ledger lines of its own, whose every sub-case is superseded, is named by no supersedes, so its section in the ratified copy stays a finding

## History

- 2026-09-25 created · raw/2026-09-24/2214/ledger.md#L26
- 2026-10-07 updated: clustered under insight-case-check-a-case-id-leaves-only-by-a-supersedes-line (synthesis) · raw/2026-10-07/1804/ledger.md#L27
- 2026-10-08 archived · insight actioned
- 2026-10-08 archived · cleanup
