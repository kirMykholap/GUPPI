---
type: insight
pattern: the event log cuts the detail of a tool line at DETAIL_LIMIT = 80 characters, and plan_path takes the session's plan file from that line as a source of truth, so a plan path longer than 80 characters names no file and every reader of the plan finds none
status: actioned
children: ["[[lesson-gate-plan-path-cut-by-the-event-log-detail-limit]]", "[[lesson-event-log-cuts-the-path-of-the-plan-file]]"]
severity: 0
addressed_by: "[[decision-case-1045]]"
origin: raw/2026-11-25/0605/ledger.md#L4
sprint: plugin
created: 2026-11-25
tags: [hooks, harness]
---

## Pattern

Two lessons, one cause. The knowledge lesson of 2026-09-14 recorded that guppi gate finds the plan file by the tool Write and tool Edit lines of the event log, which event.py cuts at DETAIL_LIMIT 80 characters, while the paths of that time were 51 to 54 characters. At the first Case of session 2026-11-25/0605 the plan path of the session, 106 characters since Claude Code names a plan file with the id of the session after "-of-", stood cut in the log, plan_path found no plan file and guppi caseid printed no id.

## Proposal

Case 1045 keeps a file path whole in the tool line of the event log while every other detail is still cut. A reader that takes a fact from a record kept for debugging could be checked for each limit that record puts on its lines. A suggestion, not a decision.

## History

- 2026-11-25 created · raw/2026-11-25/0605/ledger.md#L4
- 2026-11-25 updated: born actioned, its cause closed by case 1045 (synthesis) · raw/2026-11-25/0605/ledger.md#L4
