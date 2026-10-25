---
type: decision
case: "886"
status: current
update: ["[[estimate-sprint-close-moves-old-event-logs]]", "[[rule-raw-archive]]"]
origin: raw/2026-10-17/2307/ledger.md#case-886
sprint: plugin
created: 2026-10-17
tags: [sprint, workflow, librarian, harness, ledger]
---

## Problem

The sprint close keeps the event logs from the day before the date of the `/hi` of the open session, while its hooks read back to the date it started, so a session that started days before its `/hi` loses logs it still reads.

## Recommend

- **How the close finds the start of the open session**
  - Recommended: (a) ask the window the hooks use: the stamp whose `hi` line `session_dir` takes to the newest session folder, and the first date `session_event_logs` gives for it.
  - Answer: agreed, (a).
- **When the close cannot tell which session is open**
  - Recommended: (a) move no log, and say so on stdout.
  - Answer: agreed, (a).
- **Where the stop on a tool line is fixed**
  - Recommended: (a) Case 884 fixes it.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) replace the Criterion of `estimate-sprint-close-moves-old-event-logs`; keep its purpose and method.
  - Answer: agreed, (a).
- **Whether the Purpose of `rule-sprint-close` changes**
  - Recommended: (a) the Purpose stands; the docstring and `rule-raw-archive` change.
  - Answer: agreed, (a).

## History

- 2026-10-26 created · raw/2026-10-17/2307/ledger.md#case-886
