---
type: lesson
kind: error
root_cause: the agent took the ratification of a Case built on a sprint item as the end of that item, while a sprint item ends by a Case only when the Case updates the sprint page; a Case that settles part of a milestone line leaves the line to close `· sprint · defer`
status: new
origin: raw/2026-10-10/1913/ledger.md#L44
sprint: plugin
created: 2026-10-10
tags: [session, sprint]
---

## Trigger

the agent closed the milestone line C1 `[x] … · sprint · case 769` after Case 769 was ratified, and guppi prespec --check printed "frontier: C1 closes a sprint item with case 769, no update of the sprint page under Case 769"

## Root cause

the agent took the ratification of a Case built on a sprint item as the end of that item, while a sprint item ends by a Case only when the Case updates the sprint page; a Case that settles part of a milestone line leaves the line to close `· sprint · defer`

## History

- 2026-10-10 created · raw/2026-10-10/1913/ledger.md#L44
