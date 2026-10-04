---
type: lesson
kind: error
root_cause: case-guppi wrote a count in its context from the lines a Grep printed, not from the hits the claim names, so a line that holds two hits was counted once — a count taken from its own reading of an output, not from a command that counts the thing claimed
status: archived
insight: "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"
origin: raw/2026-10-04/0004/ledger.md#L23
sprint: migration
created: 2026-10-04
tags: [workflow, session]
---

## Trigger

at the /pre-spec of session 0004 ask-guppi found that the context of Case 620 said "two of the three [hits] in `rule-skill-hi` stand in History", where the page holds four hits on three lines

## Root cause

case-guppi wrote a count in its context from the lines a Grep printed, not from the hits the claim names, so a line that holds two hits was counted once — a count taken from its own reading of an output, not from a command that counts the thing claimed

## History

- 2026-10-04 created · raw/2026-10-04/0004/ledger.md#L23
- 2026-10-04 updated: clustered under insight-workflow-fact-signed-from-a-check-that-does-not-cover-it (synthesis) · raw/2026-10-04/0004/ledger.md#L23
- 2026-10-05 archived · insight actioned
- 2026-10-05 archived · cleanup
