---
type: lesson
kind: error
root_cause: the agent edited only the tail of a Frontier line, the old_string anchored after the box, and did not check the box after the edit; the closer and the box are two edits of one line
status: new
origin: raw/2026-10-05/0311/ledger.md#L31
sprint: migration
created: 2026-10-05
tags: [session, workflow]
---

## Trigger

at the close of Plan Mode of session 0311 the main agent closed C2 and C5 of frontier.md by an Edit that appended `· defer` and `· defer case 648` to the end of the line and left the box `[ ]`; the hook `guppi onward --plan` read two open lines under `## Cases` by `prespec.open_case_items` and did not send the agent to /pre-spec, and the person had to ask why the session stopped.

## Root cause

the agent edited only the tail of a Frontier line, the old_string anchored after the box, and did not check the box after the edit; the closer and the box are two edits of one line

## History

- 2026-10-05 created · raw/2026-10-05/0311/ledger.md#L31
