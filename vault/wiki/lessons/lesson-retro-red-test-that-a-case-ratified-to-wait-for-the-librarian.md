---
type: lesson
kind: error
root_cause: rule-retro says a red test is never an expected red and is fixed or reverted, while a Case may ratify a test whose green waits for the librarian's render and reword; no rule lets such a test stand red under Expected red
status: clustered
insight: "[[insight-workflow-code-live-before-the-page-it-reads]]"
origin: raw/2026-10-15/1739/ledger.md#L15
sprint: plugin
created: 2026-10-15
tags: [workflow, tests, retro]
---

## Trigger

Case 819.1 ratified .guppi/tests/test_guppi_package.py, which reads the files of .claude/ and the live pages; at the Retro of session 1739 its 9 tests were red, not held by the Baseline of work.md, and the commit 181a4054 went in with them red, since the Case 819 context says that red is a note for the handoff

## Root cause

rule-retro says a red test is never an expected red and is fixed or reverted, while a Case may ratify a test whose green waits for the librarian's render and reword; no rule lets such a test stand red under Expected red

## History

- 2026-10-15 created · raw/2026-10-15/1739/ledger.md#L15
- 2026-10-15 updated: clustered under insight-workflow-code-live-before-the-page-it-reads (synthesis) · raw/2026-10-15/1739/ledger.md#L15
- 2026-10-15 updated: tagged retro, the tag the ledger hook refused at the Retro of session 1739 · [[decision-case-826]]
