---
type: insight
pattern: guppi caseid --next printed an id and exited 0 when it found no plan file of the session — run without --session, or before the plan file stood — so the id was not held, and orchestration.md wrote the run without what it needs
status: actioned
children: ["[[lesson-caseid-held-no-id-without-the-session-option]]", "[[lesson-caseid-run-before-the-plan-file-held-no-id]]"]
severity: 0
addressed_by: "[[decision-case-812.1]]"
origin: raw/2026-10-14/0232/ledger.md#L15
sprint: plugin
created: 2026-10-14
tags: [harness, orchestration, session]
---

## Pattern

Twice in one day the command that numbers a new Case printed an id it did not hold. In session 0101 it ran without --session, so it found no session and no plan file; in session 0232 it ran with --session before the plan file stood. Both times it printed the id and exited 0, only a stderr line said the id was not held, and orchestration.md named the run without the option or set the plan file after it.

## Proposal

The command refuses, with no id and a non-zero exit, a run that cannot hold the id, and the page that names the command gives each thing the run needs before it.

## History

- 2026-10-14 created · raw/2026-10-14/0232/ledger.md#L15
- 2026-10-14 updated: born actioned, its cause closed by case 812.1 (synthesis) · raw/2026-10-14/0232/ledger.md#L15
