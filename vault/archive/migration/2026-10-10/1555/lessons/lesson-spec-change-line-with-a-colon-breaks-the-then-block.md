---
type: lesson
kind: error
root_cause: "a plain YAML scalar ends at the first `: ` — a `change` or `purpose` line that quotes a field name with its colon must be double-quoted, and a `file` item is an `update`, never a `create`; both are form errors of the agent that only the check sees, since the chat form shows the then block nowhere; the check found them in one run and the fix was two edits"
status: archived
origin: raw/2026-09-20/0527/ledger.md#L23
sprint: migration
created: 2026-09-20
tags: [harness, workflow]
---

## Trigger

`guppi pretask --check` on the plan of session 0527 printed "case 256: then block is not YAML: mapping values are not allowed here" and three "has no item in the plan" lines for the same Case; the `change` of the Estimate item read `… the second token of the hi: line, …` unquoted, and the four file items of 258.1 stood under `create:` with no create line

## Root cause

a plain YAML scalar ends at the first `: ` — a `change` or `purpose` line that quotes a field name with its colon must be double-quoted, and a `file` item is an `update`, never a `create`; both are form errors of the agent that only the check sees, since the chat form shows the then block nowhere; the check found them in one run and the fix was two edits

## History

- 2026-09-20 created · raw/2026-09-20/0527/ledger.md#L23
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
