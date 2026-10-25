---
type: lesson
kind: error
root_cause: "`session_event_logs` of .guppi/guppi/ledger.py walks the event logs back from today and stops at the first date that holds any `session-start` of the stamp, a `resume` included, so the window of a session resumed on a later date no longer holds its `hi` or the Write of its plan file, and `session_dir`, `plan_path` and every reader of the window lose the session"
status: archived
insight: "[[insight-ledger-window-ends-at-any-start-text-of-the-stamp]]"
origin: raw/2026-10-17/2307/ledger.md#L26
sprint: plugin
created: 2026-10-17
tags: [session, hooks, ledger]
---

## Trigger

session 2307 (hi 2026-10-17 23:07) was resumed on 2026-10-24 after a pause of a week; the hook wrote `392fc00e session-start resume` into vault/raw/2026-10-24/event_log.md, and on 2026-10-25 `guppi caseid --next --session 392fc00e` printed `caseid: no plan file of session 392fc00e — no id printed`; the person removed the resume line by hand and the next run printed 882

## Root cause

`session_event_logs` of .guppi/guppi/ledger.py walks the event logs back from today and stops at the first date that holds any `session-start` of the stamp, a `resume` included, so the window of a session resumed on a later date no longer holds its `hi` or the Write of its plan file, and `session_dir`, `plan_path` and every reader of the window lose the session

## History

- 2026-10-26 created · raw/2026-10-17/2307/ledger.md#L26
- 2026-10-26 updated: clustered under insight-ledger-window-ends-at-any-start-text-of-the-stamp (synthesis) · raw/2026-10-17/2307/ledger.md#L26
- 2026-10-26 archived · insight actioned
- 2026-10-26 archived · cleanup
