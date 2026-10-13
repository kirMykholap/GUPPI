---
type: lesson
kind: error
root_cause: case-guppi let a Case of a session use a form of an update that only the code of that session's Work Mode would accept, though every check of the Case file runs the code that stands before Work Mode
status: clustered
insight: "[[insight-workflow-code-live-before-the-page-it-reads]]"
origin: raw/2026-10-12/2349/ledger.md#L58
sprint: plugin
created: 2026-10-12
tags: [case-build, prespec, harness]
---

## Trigger

Case 787.2 was built to drop a section with the key drop that Case 792 of the same session would add; the check of the Case file, running the code before Work Mode, refused the key, and Case 792 was put off to the backlog

## Root cause

case-guppi let a Case of a session use a form of an update that only the code of that session's Work Mode would accept, though every check of the Case file runs the code that stands before Work Mode

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#L58
- 2026-10-13 updated: clustered under insight-workflow-code-live-before-the-page-it-reads (synthesis) · raw/2026-10-12/2349/ledger.md#L58
