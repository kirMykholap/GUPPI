---
type: decision
case: "917"
status: current
children: ["[[decision-case-917.1]]", "[[decision-case-917.2]]"]
origin: raw/2026-10-29/2341/ledger.md#case-917
sprint: plugin
created: 2026-10-29
tags: [sprint, workflow, librarian, session, hooks, harness]
---

## Problem

Two shipped Estimates, and the docstring of the close code, name a bare `.gitignore`. The lines that ignore the event logs stand in `vault/.gitignore`. So a reader of the `method` of `estimate-sprint-close-moves-old-event-logs` opens the root `.gitignore` and finds no such line, in this repository and in a project that installed GUPPI.

## Recommend

- **How the Estimate names the ignore file**
  - Recommended: (a) replace the Criterion whole and set the method, both naming `vault/.gitignore`; read at the Retro of this session.
  - Answer: agreed, (a).
- **The docstring of the close code**
  - Recommended: (a) name `vault/.gitignore` there too.
  - Answer: agreed, (a).
- **The event log Estimate with the same bare name**
  - Recommended: (a) leave it out of this Case.
  - Answer: (b), a sub-case replaces the Criterion of `estimate-event-log-records` with `vault/.gitignore`.
- **When the event log check can be read**
  - Recommended: (a) drop the two `/hi` readings by hand from the `method`, so that the pytest and the ignore and timing readings all run at the Retro of this session.
  - Answer: agreed, (a).

## History

- 2026-10-30 created · raw/2026-10-29/2341/ledger.md#case-917
