---
type: decision
case: "125"
status: current
update: [rule-event-log, rule-skill-hi]
origin: raw/2026-09-14/1029/ledger.md#case-125
sprint: migration
created: 2026-09-14
tags: [session, hooks, harness]
---

## Context

Case 111.4 removed the `Recorded:` line from the `/hi` skill: the `hi` is now written by the `UserPromptSubmit` hook (`guppi event prompt`, 111.1) with the session's stamp. Today it worked: `- 10:29:12 19037d1c hi`. But the skill's text still says "`HHMM` the time of the `hi` line above (case 73)" — and there is no line above any more. To name the folder `raw/2026-09-14/1029/` the agent read `event_log.md` through Bash.

## Problem

The skill points at a line nobody prints. The agent either guesses the time or makes a read call — against the purpose of `rule-skill-hi` ("prevents a session from being loaded piecemeal by read-tool calls"). The time of the `hi` needs a source in the context, without a read.

## Given

`rule-event-log` (`Leaf`, `draft`, `estimate-event-log-records` `pending` on block 111.1): "the log gains `- HH:MM:SS <stamp> hi` … a second `/hi` of the same session and any other prompt write nothing (case 111.1)"; `prompt_line` (`event.py:127-136`) returns the line or None, the hook is silent on stdout; `hi_written` already knows whether a `hi` of this session exists.
**＋** `rule-skill-hi` (`MOC`, `built`, `estimate-hi-no-read-calls` `passed` on 101.3, `estimate-hi-writes-frontier` `passed`): line 41 of the Render — "`HHMM` the time of the `hi` line above (case 73)". The folder and the time come from `ledger.session_dir`; in a `!` substitution of the skill `CLAUDE_SESSION_ID` is empty (111), so a substitution cannot name the session — the hook can, its payload carries `session_id`. A `UserPromptSubmit` hook's stdout on exit 0 is added to the context (Claude Code hooks reference).
**＋** The order "the `UserPromptSubmit` hook → the expansion of the skill" is not measured; it does not matter here: the line reaches the context with the prompt, before the agent's reply.
**－** Other prompts: the hook stays silent; exit 0 always, errors on stderr only.
**－** `estimate-hi-no-read-calls` gets no block: its criterion (no read call) does not change, the way to meet it does; its reading is by 101.3 at the next `/hi`.
**－** The Frontier line F4 closes on this Case.

## Criterion

- [[estimate-event-log-records]] § case 125

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-125
