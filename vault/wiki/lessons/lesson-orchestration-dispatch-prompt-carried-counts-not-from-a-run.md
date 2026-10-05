---
type: lesson
kind: error
root_cause: the main agent wrote counts in a dispatch prompt from its glance at a transcript, not from a count it ran, and case-guppi took the prompt's facts as given
status: clustered
insight: "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"
origin: raw/2026-10-05/0109/ledger.md#L25
sprint: migration
created: 2026-10-05
tags: [workflow, session]
---

## Trigger

the prompt that dispatched case-guppi for Case 638 described the 636 confirmation answer as "a paragraph of two sentences" and "a paragraph of three sentences"; case-guppi put the counts in the context, and the ask-guppi run at /pre-spec found them not borne out (finding 3.1), which sent the Case back.

## Root cause

the main agent wrote counts in a dispatch prompt from its glance at a transcript, not from a count it ran, and case-guppi took the prompt's facts as given

## History

- 2026-10-05 created · raw/2026-10-05/0109/ledger.md#L25
- 2026-10-05 updated: clustered under insight-workflow-fact-signed-from-a-check-that-does-not-cover-it (synthesis) · raw/2026-10-05/0109/ledger.md#L25
