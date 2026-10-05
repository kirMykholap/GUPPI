---
type: lesson
kind: error
root_cause: the agent wrote the mark of the parent from the words of the short form and did not check how the scripts read it; the Spec hook removes a parent with its sub-cases, while `prespec.superseded_in_window` and `materialize.mark_superseded` mark only the number named, two readings of one mark
status: clustered
insight: "[[insight-harness-one-rule-implemented-twice-drifts]]"
origin: raw/2026-10-05/1343/ledger.md#L42
sprint: migration
created: 2026-10-05
tags: [session, workflow]
---

## Trigger

at the /pre-spec of session 1343 the main agent put off Case 653 by the short-form Case 658 with one mark {supersedes:case 653}; the decision lines of Case 653 were those of 653.1 and 653.2, so `guppi prespec --check` printed three findings "no Case 653.x heading in the plan", and `materialize` would have applied the three updates the person put off; Case 659 carried a mark for each number.

## Root cause

the agent wrote the mark of the parent from the words of the short form and did not check how the scripts read it; the Spec hook removes a parent with its sub-cases, while `prespec.superseded_in_window` and `materialize.mark_superseded` mark only the number named, two readings of one mark

## History

- 2026-10-05 created · raw/2026-10-05/1343/ledger.md#L42
- 2026-10-05 updated: clustered under insight-harness-one-rule-implemented-twice-drifts (synthesis) · raw/2026-10-05/1343/ledger.md#L42
