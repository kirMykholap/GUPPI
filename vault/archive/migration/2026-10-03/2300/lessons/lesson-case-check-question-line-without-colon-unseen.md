---
type: lesson
kind: error
root_cause: QUESTION_LINE in guppi/casecheck.py requires the colon after the bold title, so a question line without it is no question to the round checks of rule-case-check, and the shape of that question goes unchecked
status: archived
insight: "[[insight-case-form-chat-form-read-by-no-script]]"
origin: raw/2026-10-02/2049/ledger.md#L25
sprint: migration
created: 2026-10-02
tags: [hooks, workflow]
---

## Trigger

in session 2049 the round of case-guppi on Case 599 opened its question with a title line that had no colon after the bold title, and no check refused the round or its showing in the chat

## Root cause

QUESTION_LINE in guppi/casecheck.py requires the colon after the bold title, so a question line without it is no question to the round checks of rule-case-check, and the shape of that question goes unchecked

## History

- 2026-10-02 created · raw/2026-10-02/2049/ledger.md#L25
- 2026-10-03 updated: clustered under insight-case-form-chat-form-read-by-no-script (case 605) · [[decision-case-605]]
- 2026-10-03 archived · insight actioned
- 2026-10-03 archived · cleanup
