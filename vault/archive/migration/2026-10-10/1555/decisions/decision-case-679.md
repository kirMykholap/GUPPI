---
type: decision
case: "679"
status: archived
update: ["[[insight-hi-skill-substitution-checked-by-a-model-call]]"]
supersedes: ["[[decision-case-448]]"]
origin: raw/2026-10-05/2249/ledger.md#case-679
sprint: migration
created: 2026-10-05
tags: [harness, session, hooks]
---

## Problem

An open Insight names a lapsed login as the cause and `/login` as the cure. Later lessons refuted both. The failure comes from Claude Code's server, and the harness has nothing to fix.

## Recommend

- **What the closed Insight says is the cause**
  - Recommended: (a) rewrite the cause, then close: the `pattern` and `## Pattern` name the server-side check that gives no verdict, the `/login` cure goes, and the Insight is set `actioned` as rejected.
  - Answer: agreed, (a).
- **What happens to the Proposal section**
  - Recommended: (a) replace its text with the outcome: the harness has nothing to fix, and `/hi` gets past the check because its `!` commands are allowed in `rule-skill-hi`.
  - Answer: agreed, (a).

## History

- 2026-10-06 created · raw/2026-10-05/2249/ledger.md#case-679
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
