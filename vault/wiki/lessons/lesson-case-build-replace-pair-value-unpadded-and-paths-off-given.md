---
type: lesson
kind: error
root_cause: case-schema.md stated both rules in prose but showed no example of the form case-guppi writes, and a fix after a finding meant a whole new answer
status: clustered
insight: "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"
origin: raw/2026-10-05/0311/ledger.md#L40
sprint: migration
created: 2026-10-05
tags: [workflow, session]
---

## Trigger

the first build of Case 644 in session 0311 was sent back by `guppi casecheck --subagent` for an `old` value holding a backtick in an unpadded span, a `new` with no `old` before it, and paths in `then` of 644.2, 644.5 and 644.6 that `given` did not name; case-guppi wrote the whole Case of about 30,000 characters again, and 644.3, 644.4 and 644.7 came back the same.

## Root cause

case-schema.md stated both rules in prose but showed no example of the form case-guppi writes, and a fix after a finding meant a whole new answer

## History

- 2026-10-05 created · raw/2026-10-05/0311/ledger.md#L40
- 2026-10-05 updated: clustered under insight-workflow-case-schema-silent-on-what-the-scripts-accept (synthesis) · raw/2026-10-05/0311/ledger.md#L40
