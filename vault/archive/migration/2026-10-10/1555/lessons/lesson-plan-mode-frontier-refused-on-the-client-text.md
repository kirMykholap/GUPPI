---
type: lesson
kind: error
root_cause: "the client's generic Plan Mode text — no edits but the plan file — was put above the project's rule and its harness: settings.json has carried defaultMode plan since 2026-08-20 with an allow list for Write and Edit of vault/raw/**/frontier.md, spec.md and handoff.md for exactly this, and the sessions of 2026-09-14 and 2026-09-15 wrote and ticked the frontier in Plan Mode; nothing in the harness refuses the write, the agent did"
status: archived
origin: raw/2026-09-16/1651/ledger.md#L19
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness]
---

## Trigger

sessions 1034 and 1651 of 2026-09-16 did not write raw/<date>/<hi HHMM>/frontier.md at /hi, the agent saying Plan Mode blocks every write but the plan file; 1034 wrote that as a flag into brief.md and its frontier, and 1651 leaned on the flag

## Root cause

the client's generic Plan Mode text — no edits but the plan file — was put above the project's rule and its harness: settings.json has carried defaultMode plan since 2026-08-20 with an allow list for Write and Edit of vault/raw/**/frontier.md, spec.md and handoff.md for exactly this, and the sessions of 2026-09-14 and 2026-09-15 wrote and ticked the frontier in Plan Mode; nothing in the harness refuses the write, the agent did

## History

- 2026-09-16 created · raw/2026-09-16/1651/ledger.md#L19
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
