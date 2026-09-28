---
type: lesson
kind: error
root_cause: "the code of a Case runs in Work Mode and the pages of a Case change at the librarian's run, so a check that reads a page the same Spec updates is red in between by construction; the interval is a property of the session, not of pre-task — its place is one sentence in rule-work-mode (Slice 3b): such a check is read after the run, and its red in Work Mode is an expectation named in the handoff, not a finding"
status: archived
insight: "[[insight-workflow-code-live-before-the-page-it-reads]]"
origin: raw/2026-09-17/1119/ledger.md#L43
sprint: migration
created: 2026-09-17
tags: [harness, workflow, session]
---

## Trigger

case 227 put `sprint --check` into `make lint` and case 229.1 moved the Slices of the sprint page under `## Milestones`; in Work Mode the code ran at once and the page waited for the librarian, so `make lint` went red on the sprint step until the run, as `render --check` does after an `update` of a Render

## Root cause

the code of a Case runs in Work Mode and the pages of a Case change at the librarian's run, so a check that reads a page the same Spec updates is red in between by construction; the interval is a property of the session, not of pre-task — its place is one sentence in rule-work-mode (Slice 3b): such a check is read after the run, and its red in Work Mode is an expectation named in the handoff, not a finding

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#L43
- 2026-09-18 updated: clustered by librarian under insight-workflow-code-live-before-the-page-it-reads · raw/2026-09-17/1119/ledger.md#L43
- 2026-09-28 archived · insight actioned
- 2026-09-28 archived · cleanup
