---
type: decision
case: "213.3"
status: current
update: ["[[rule-prespec]]", "[[estimate-prespec-reconciles]]"]
origin: raw/2026-09-16/2238/ledger.md#case-213.3
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness]
---

## Context

The Insight `insight-ledger-hi-tied-to-its-session-by-position` (`open`, severity 1, four lessons, deferred by 192 and 205) describes one fault: a `hi` was bound to its session by the `session-start` lines around it in the event log, and a foreign start or midnight broke the binding. Half of it is closed: `UserPromptSubmit` writes the `hi` with the session's stamp (case 111), the ledger hook finds the window by the stamp and walks back across midnight (`hi_moment`, `session_event_logs`), the binding by position left with case 136.3. Two readers keep the old logic: `guppi pretask --check` — without `--session` and without `CLAUDE_SESSION_ID` (empty in the agent's Bash, checked in this session) it takes the last `session-start` of today's log — a foreign one beside a parallel session, none after midnight (`lesson-pretask-check-session-fallback-stops-at-midnight`); and the hook `PreToolUse ExitPlanMode` — it reads today's log only, so after midnight it sees no `hi` and lets Plan Mode close without `/pre-task`. The stamp is in the context: the line `hi: HH:MM:SS <stamp> → raw/…` the hook prints at `/hi`. The Case touches `estimate-prespec-checks-the-plan` (`rule-prespec`), `estimate-prespec-hook-gates` (`rule-prespec-hook`) and `estimate-prespec-reconciles` (the Render of `rule-prespec`) — one per sub-case; `rule-ledger-write` and `rule-event-log` it does not touch. `estimate-prespec-hook-gates` is of the old shape: its `update` carries `set.method` (case 211) and its Criterion is written whole in the form of the model, the block of 136.2 folded in.

## Problem

Two readers guess the session where the ledger hook knows it. Guessing by position is the cause the Insight names; while it lives in `pretask`, the Insight cannot close, and `/pre-task` after midnight checks the wrong session or nothing, in silence.

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-213.3
