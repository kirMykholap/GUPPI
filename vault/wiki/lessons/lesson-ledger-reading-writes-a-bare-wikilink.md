---
type: lesson
kind: error
root_cause: "the main agent wrote a bare `[[slug]]` into the text of an estimate line at the Retro of session 1831, generate copied that text into the ## Result as it stood, and nothing checks the text of a reading for a bare wikilink before it reaches a page, so the librarian's flag guessed a cause from the page instead of reading the line"
status: new
origin: raw/2026-10-31/2307/ledger.md#L19
sprint: plugin
created: 2026-10-31
tags: [ledger, librarian]
---

## Trigger

guppi check reported "estimates/estimate-link-graph-prints-the-neighbours: ref: body names slug, which no live or archived page carries", and the brief of session 1831 put the cause in the code spans of its Criterion

## Root cause

the main agent wrote a bare `[[slug]]` into the text of an estimate line at the Retro of session 1831, generate copied that text into the ## Result as it stood, and nothing checks the text of a reading for a bare wikilink before it reaches a page, so the librarian's flag guessed a cause from the page instead of reading the line

## History

- 2026-11-01 created · raw/2026-10-31/2307/ledger.md#L19
- 2026-11-01 updated: the bare link of the root cause put in a code span, in the section and the field, so lint reads no link to a page · [[decision-case-978]]
