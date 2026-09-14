---
type: decision
case: "117"
status: current
defer: [rule-ledger-write]
origin: raw/2026-09-14/0747/ledger.md#case-117
sprint: migration
created: 2026-09-14
tags: [session, hooks, harness, ledger]
---

## Context

Four lessons on one writer: `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (F), `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` (I, archived), `lesson-transcript-omits-text-emitted-before-tool-calls` (L), and today's `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live`. The `Stop` hook reads the final text of a turn; a reply that ends in `Skill`, `ExitPlanMode` or any tool call has no `Stop` and its text is not in the transcript. The Insight's Proposal has stood unactioned since session I.

## Problem

The rule "a reply with ledger lines ends in text" lives in the agent's memory only, and the agent broke it with the lesson live. Either the hook reaches those lines — a `PreToolUse` hook on `Skill|ExitPlanMode` that reads the reply under way, if the payload carries it — or the harness makes the agent's rule mechanical: `CLAUDE.md` says it, and `guppi gate` refuses a `Skill` call while the reply holds an unwritten `LEDGER` block. Which of the two is measurable is a Plan Mode of its own.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-117
