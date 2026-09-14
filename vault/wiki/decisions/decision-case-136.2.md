---
type: decision
case: "136.2"
status: current
update: ["[[rule-pretask-hook]]"]
origin: raw/2026-09-14/1229/ledger.md#case-136.2
sprint: migration
created: 2026-09-14
tags: [session, workflow, hooks, harness]
---

## Context

An Insight of severity 3, three children: the `hi` lost at midnight (session H), the `hi` taken by a session started in the same second (M), and the `pretask` line unstamped and bound by position (N). One cause: a mark in the event log without a session id, and a reader that binds it to a session by the `session-start` lines around it. The `hi` half is closed by Case 111: the `UserPromptSubmit` hook writes `<stamp> hi`, the readings 111.1/111.3/111.6 and 125 passed — today `12:29:47 07a95bd2 hi`. What remains: (1) the marks `pretask`, `retro`, `handoff` are still written through a `!` substitution with an empty `CLAUDE_SESSION_ID` — `--------` — and `pretask.window` counts any `pretask` after our `hi`; (2) `ledger.py` keeps the fallback of 111.6 — a `--------` `hi` by position, kept for the sessions opened before the hook; no such session is open, and since 111.4 nothing writes a `--------` `hi`.

## Problem

Close the pattern whole: every mark of a session carries its stamp, and no reader binds by position. Who writes the marks of the three skills, and whether the fallback goes.

## Given

`rule-event-log` (`Leaf`, `hook`, `built`, `estimate-event-log-records` `passed`, `implementation_ref: [guppi/event.py, guppi/cli.py, .claude/settings.json]`): `guppi event <name> [--session ID]` writes the line, the stamp from `--session` or the payload's `session_id`, `--------` with neither.
**＋** `rule-pretask`, `rule-retro`, `rule-handoff` (`Leaf`, `render`): line 32/33/32 of the Render — `Recorded: !`uv run guppi event <name> --session "${CLAUDE_SESSION_ID:-}"``; the variable is empty there, every mark reads `--------` (event log 08:48:57, 09:23:25, 09:55:47, 11:26:29, 11:55:48, 12:10:50).
**＋** `rule-pretask` (`built`, `estimate-pretask-reconciles` `passed`): the hook `guppi pretask` on `ExitPlanMode`, `window()` at `guppi/pretask.py:76` — a `hi` of our session, then any `pretask`, a foreign `session-start` resets.
**＋** `rule-ledger-write` (`built`, `estimate-ledger-write-lifts` `passed`, `implementation_ref` holds `guppi/gate.py`): `hi_moment` by stamp (111.3), `unstamped_hi_moment` — the fallback of 111.6 (`ledger.py:187`); `rule-retro-commit` also points at `gate.py`.
**＋** `guppi gate` (`PreToolUse Skill`, 122 and `rule-retro-commit`): reads the payload with `session_id` and `tool_input.skill`; on a refusal the skill does not expand, so today its `!` line is not written — a refused call leaves no mark.
**＋** All three skills come through the Skill tool (event log: `tool Skill: pre-task`, `tool Skill: handoff`; `retro` in session N never reached the call — the skill failed to load).
**＋** The criteria of `estimate-retro-loads` and `estimate-handoff-dispatches` say "event_log.md carries a retro/handoff line" — still true, the writer is not named.
**＋** Every session opened before the hook of 111 (dates ≤ 09-13) is closed and archived; `raw/` holds 2026-09-14 only.
**－** `estimate-retro-loads` is `failed` (109.1) — this Case does not touch its criterion; the reading of 126 is at `/retro`.
**－** `hi` is not touched: 111 stands.

## Criterion

- [[estimate-pretask-hook-gates]] § case 136.2

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#case-136.2
