---
type: decision
case: "111.1"
status: current
update: ["[[rule-event-log]]"]
origin: raw/2026-09-14/0747/ledger.md#case-111.1
sprint: migration
created: 2026-09-14
tags: [session, hooks, harness]
---

## Context

Today at 07:30:30 two sessions started in one second: this one, `fde37e7c`, and `19b07bbc`, session L, restored by `resume`. The `hi` of 07:30:39 carries `--------` — `CLAUDE_SESSION_ID` is empty in the `!` substitution of the skill — so the ledger hook tied it to the start nearest before it, the foreign one, and refused every line of this session. A second `/hi` did not help: `hi_recorded` sets `ours = False` on the foreign start and only a new `session-start` of our own sets it back; a `resume` of this session at 07:46:53 did. The lesson line of 07:44 ends "A second /hi at 07:44 fixed the window", which is false.

## Problem

The window of a session is inferred from the order of starts around an unstamped `hi`. One foreign start between our start and our `hi` — a restored tab is enough — takes the `hi` away, and the session cannot recover by any command of its own. `rule-event-log` names this as a known limit since Case 9. The lesson page will be born with a wrong root cause.

## Given

`UserPromptSubmit` fires on every prompt; there is no matcher on the prompt text, so the filter is the script's. The payload carries `session_id` and `prompt`. The `!` substitution of the skill sees no session id (`--------` on every `hi` line today); a `PreToolUse Skill` hook does not see a command the person types (`rule-skill-hi`, Purpose). `guppi event tool` already runs once per tool call, on `PostToolUse` with no matcher.
**＋** `hi_moment` takes the first `hi` of the window; a second `hi` line of the same session changes nothing there, it is log noise.
**＋** The `hi` of this session in the logs walked: `session_event_logs` from today back to the first date holding this session's `session-start` (case 55.1).

## Criterion

- [[estimate-event-log-records]] § case 111.1

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-111.1
