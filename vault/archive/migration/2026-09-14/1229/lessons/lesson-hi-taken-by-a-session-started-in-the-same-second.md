---
type: lesson
kind: error
root_cause: "the hi line carries no session id (CLAUDE_SESSION_ID is empty in the skill's shell), so hi_recorded ties it to the session-start lines around it; a second session, 19b07bbc, started by resume in the same second 07:30:30 and its start stood between our start and the hi, which went to it. A second /hi at 07:44 did not fix it: hi_recorded stays closed once a foreign start follows our own, until a new session-start of our session is logged; a resume of this session at 07:46:53 reopened the window, and the hi of 07:47 named the folder."
status: archived
insight: "[[insight-ledger-hi-tied-to-its-session-by-position]]"
origin: raw/2026-09-14/0747/ledger.md#L2
sprint: migration
created: 2026-09-14
tags: [harness, hooks, ledger]
---

## Trigger

the Stop hook refused the first ledger line of session fde37e7c, "no /hi recorded", although event_log.md held a hi line at 07:30:39.

## Root cause

the hi line carries no session id (CLAUDE_SESSION_ID is empty in the skill's shell), so hi_recorded ties it to the session-start lines around it; a second session, 19b07bbc, started by resume in the same second 07:30:30 and its start stood between our start and the hi, which went to it. A second /hi at 07:44 did not fix it: hi_recorded stays closed once a foreign start follows our own, until a new session-start of our session is logged; a resume of this session at 07:46:53 reopened the window, and the hi of 07:47 named the folder.

## Insight

- [[insight-ledger-hi-tied-to-its-session-by-position]]

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#L2
- 2026-09-14 updated: root_cause corrected (case 111.5) · [[decision-case-111.5]]
- 2026-09-14 updated: clustered under insight-ledger-hi-tied-to-its-session-by-position · raw/2026-09-14/0747/ledger.md#L2
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
