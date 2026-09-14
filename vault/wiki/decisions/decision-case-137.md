---
type: decision
case: "137"
status: current
update: [insight-ledger-hook-reads-only-the-final-text]
origin: raw/2026-09-14/1229/ledger.md#case-137
sprint: migration
created: 2026-09-14
tags: [harness, hooks, ledger]
---

## Context

An Insight of severity 3, four children: blocks in replies that ended in a Skill call and in `ExitPlanMode` (session F); blocks in a text followed by tool calls in the same turn (I); the text before a tool call is absent from the transcript altogether (L); blocks lost in a reply ending in a Skill call with the Insight live (M). Pattern: the ledger writer sees the last text of a turn, not the turn. Proposal: settle whether an intermediate text is in the transcript; if present collect every text of the window, if absent the writer needs a second event beside `Stop`; and count blocks seen against lines written at `/hi`.

## Problem

The Proposal's question is settled by the third child: the text before a tool call is not in the transcript — Claude Code does not keep it. So "collect every text" is impossible, and there is nothing to count "blocks seen" from. A second event beside `Stop` does not help either: no hook sees a reply's text before its end. What was possible was done by Case 122: the rule in `CLAUDE.md` ("A reply that carries a `LEDGER` block ends in that text. No tool call follows it") and `guppi gate` on `PreToolUse Skill`, refusing a skill call while a `then` item of the Spec has no decision line — the very move that lost the lines in F and M. Decide: is the Insight actioned.

## Given

`insight-ledger-hook-reads-only-the-final-text`: `open`, `severity: 3`, children `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`, `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` (`archived`), `lesson-transcript-omits-text-emitted-before-tool-calls`, `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live`.
**＋** `rule-ledger-write` `built`, `estimate-ledger-write-lifts` `passed` with the block of 122: the gate on `PreToolUse Skill` refuses while a `then` item of the Spec or plan file has no line; 55.2 — every `Stop` reads every `LEDGER` block of the window's transcript, so the final text of any earlier turn is never lost.
**＋** `rule-case-protocol` → `CLAUDE.md`: "A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call is never kept, and the hook reads nothing" (122); `estimate-claude-md-rendered` passed today with that sentence.
**＋** 122 signed the limits: the gate does not see `estimate`/`lesson` lines, a loss is a Retro finding; `ExitPlanMode` is not gated, `/pre-task` before it is a Skill call.
**＋** This session: every block was the final text, the ledger of `1229/` holds every line.
**＋** The cascade of 104.2: the three live children go `archived`; the fourth is archived already.
**－** An Insight is not a Leaf: no `contract`, no Estimate.
**－** No live refusal of the gate observed yet (the test of 122 passed); that reading stays with `estimate-ledger-write-lifts`, the Insight does not wait for it — a ratified decision is enough by the schema.

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#case-137
