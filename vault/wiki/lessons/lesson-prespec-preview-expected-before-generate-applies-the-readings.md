---
type: lesson
kind: error
root_cause: the main agent wrote the expected output of a command from the end state of the session, not from the state of the pages when the command runs, and did not check the order ledger → generate → close
status: clustered
insight: "[[insight-workflow-code-live-before-the-page-it-reads]]"
origin: raw/2026-10-10/1555/ledger.md#L6
sprint: migration
created: 2026-10-10
tags: [sprint, workflow]
---

## Trigger

at /pre-spec of session 1555 the main agent put to the person a Work Mode task that runs the preview of guppi sprint-close and expects no refusal; case-guppi found that the readings of Work Mode reach the Estimate pages only when guppi generate applies the ledger at the librarian's run, so the preview lists those four Estimates as not settled, and the person answered a second question

## Root cause

the main agent wrote the expected output of a command from the end state of the session, not from the state of the pages when the command runs, and did not check the order ledger → generate → close

## History

- 2026-10-10 created · raw/2026-10-10/1555/ledger.md#L6
- 2026-10-10 updated: clustered under insight-workflow-code-live-before-the-page-it-reads (synthesis) · raw/2026-10-10/1555/ledger.md#L6
