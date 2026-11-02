---
type: lesson
kind: error
root_cause: the agent edited only the end of the line with an Edit whose old_string held the tail of the title, so the box at the start of the line, which marks the line closed, stayed as it was; a closer is the box and the tail together
status: clustered
insight: "[[insight-orchestration-frontier-closer-leaves-the-box-open]]"
origin: raw/2026-11-02/1548/ledger.md#L12
sprint: plugin
created: 2026-11-02
tags: [session, workflow]
---

## Trigger

in session 1548 the main agent closed C2, C3 and C5 of frontier.md by appending `· case 1005`, `· work` and `· case 1006` to each line and left its box `[ ]`, and the first run of guppi prespec --check printed `frontier: C2 is open`, `C3 is open` and `C5 is open`

## Root cause

the agent edited only the end of the line with an Edit whose old_string held the tail of the title, so the box at the start of the line, which marks the line closed, stayed as it was; a closer is the box and the tail together

## History

- 2026-11-02 created · raw/2026-11-02/1548/ledger.md#L12
- 2026-11-02 updated: clustered under insight-orchestration-frontier-closer-leaves-the-box-open (synthesis) · raw/2026-11-02/1548/ledger.md#L12
