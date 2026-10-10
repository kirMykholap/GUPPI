---
type: lesson
kind: error
root_cause: case-guppi judged a changed live text against the check functions a test runs over it, not against the test's own helper code that reads the same text
status: archived
insight: "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"
origin: raw/2026-10-09/2049/ledger.md#L21
sprint: migration
created: 2026-10-09
tags: [workflow, session]
---

## Trigger

Case 751.6 put a horizontal rule before the example of a showing and its context said the test of tests/test_orchestration.py accepts the example as changed, judged by the functions of the check alone; at Retro the test failed on a copy of the page with the change, since its own helper store_of_showing read the ratification by fence_ledger_lines over the whole text, which stops at the first rule, and the Spec held no task for the test

## Root cause

case-guppi judged a changed live text against the check functions a test runs over it, not against the test's own helper code that reads the same text

## History

- 2026-10-09 created · raw/2026-10-09/2049/ledger.md#L21
- 2026-10-09 updated: clustered under insight-workflow-fact-signed-from-a-check-that-does-not-cover-it (synthesis) · raw/2026-10-09/2049/ledger.md#L21
- 2026-10-10 archived · insight actioned
- 2026-10-10 archived · cleanup
