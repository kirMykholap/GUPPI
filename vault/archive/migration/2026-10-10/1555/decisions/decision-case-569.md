---
type: decision
case: "569"
status: archived
children: ["[[decision-case-569.1]]", "[[decision-case-569.2]]"]
origin: raw/2026-10-01/1237/ledger.md#case-569
sprint: migration
created: 2026-10-01
tags: [session, workflow, harness, render]
---

## Problem

The skill forbids a report but sets only the end of the reply that ends Retro, so a report in English stood before the `LEDGER` block. The skill also tells the agent to read `work.md` without saying whether a file it wrote itself in the same turn counts as read. The question was what that reply may hold, what enforces it, and what reading `work.md` means.

## Recommend

- **What does reading `work.md` mean when the agent wrote it in the same turn?**
  - Recommended: (a) Retro opens `work.md` with the Read tool as its first step, always, even when the agent wrote it in this turn; the event log shows the Read.
  - Answer: (b) what the agent already holds counts: the Read is needed only when the agent did not write or change the file in this turn. While one agent does the work and the report, this counts; once the work and the report are split between agents, reading the file becomes required.

## History

- 2026-10-01 created · raw/2026-10-01/1237/ledger.md#case-569
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
