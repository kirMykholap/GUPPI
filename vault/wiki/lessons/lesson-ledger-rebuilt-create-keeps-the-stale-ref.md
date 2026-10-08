---
type: lesson
kind: error
root_cause: a re-ratification appends a changed decision line beside the first one, which the ledger never withdraws, and materialize takes the ref of an entry from its own ledger line before the item of the Spec, so the stale ref stays an entry of the yaml with nothing that marks it superseded
status: clustered
insight: "[[insight-ledger-ratified-line-never-withdrawn]]"
origin: raw/2026-10-08/2352/ledger.md#L41
sprint: migration
created: 2026-10-08
tags: [ledger, case-build, librarian]
---

## Trigger

Case 743 rebuilt at /pre-spec changed the ref of two create lines from rule-session to rule-session-start and rule-plan-mode; the ledger holds lines 15 and 19 with {ref:rule-session} beside lines 27 and 28 with the new refs, and uv run guppi materialize --show gives entries 15 and 19 ref: rule-session

## Root cause

a re-ratification appends a changed decision line beside the first one, which the ledger never withdraws, and materialize takes the ref of an entry from its own ledger line before the item of the Spec, so the stale ref stays an entry of the yaml with nothing that marks it superseded

## History

- 2026-10-09 created · raw/2026-10-08/2352/ledger.md#L41
- 2026-10-09 updated: clustered under insight-ledger-ratified-line-never-withdrawn (synthesis) · raw/2026-10-08/2352/ledger.md#L41
