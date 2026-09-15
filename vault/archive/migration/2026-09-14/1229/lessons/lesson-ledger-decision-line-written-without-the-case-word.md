---
type: lesson
kind: error
root_cause: the table of case-schema.md shows the line as decision[case_id][kind][slug], a placeholder the agent read literally, while every earlier ledger writes the word case before the id; nothing between the reply and materialize checks a written line against the grammar, and the Stop hook writes verbatim by design; the lines were written again in the right form, the wrong ones stay as the trace
status: archived
insight: "[[insight-ledger-line-written-unchecked]]"
origin: raw/2026-09-12/ledger.md#L100
sprint: migration
created: 2026-09-12
tags: [ledger, workflow]
---

## Trigger

every decision line of session I up to 10:09 was written as decision[58][update][slug], and materialize.parse_line accepts decision[case 58] only, so 33 lines of the day would go under unparsed; the check of case 59.1 found them while comparing the plan with the ledger

## Root cause

the table of case-schema.md shows the line as decision[case_id][kind][slug], a placeholder the agent read literally, while every earlier ledger writes the word case before the id; nothing between the reply and materialize checks a written line against the grammar, and the Stop hook writes verbatim by design; the lines were written again in the right form, the wrong ones stay as the trace

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L100
- 2026-09-12 updated: clustered by librarian: a ledger line is unchecked until materialize, with lesson-spec-then-items-unchecked-against-ledger-lines · raw/2026-09-12/ledger.md#L100
- 2026-09-14 insight section derived
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
