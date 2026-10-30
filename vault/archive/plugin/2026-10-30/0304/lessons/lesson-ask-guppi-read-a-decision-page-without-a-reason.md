---
type: lesson
kind: error
root_cause: ask-guppi read the Decision of a deferred_by on a page it only looked at, before a finding named that page, against the rule that a Decision page is read only for a reason its frame names
status: archived
insight: "[[insight-ask-guppi-reads-a-decision-outside-its-frame]]"
origin: raw/2026-10-13/1426/ledger.md#L30
sprint: plugin
created: 2026-10-13
tags: [workflow, prespec]
---

## Trigger

at the /pre-spec of session 1426 ask-guppi ran a Grep of vault/wiki/decisions/decision-case-616.md for its ## Problem because entity-guppi carries deferred_by, though entity-guppi stood in no finding, and reported the break itself

## Root cause

ask-guppi read the Decision of a deferred_by on a page it only looked at, before a finding named that page, against the rule that a Decision page is read only for a reason its frame names

## History

- 2026-10-13 created · raw/2026-10-13/1426/ledger.md#L30
- 2026-10-28 updated: clustered under insight-ask-guppi-reads-a-decision-outside-its-frame (synthesis) · raw/2026-10-28/1907/ledger.md#L22
- 2026-10-30 archived · insight actioned
- 2026-10-30 archived · cleanup
