---
type: decision
case: "111.2"
status: current
update: [rule-hook-registry]
origin: raw/2026-09-14/0747/ledger.md#case-111.2
sprint: migration
created: 2026-09-14
tags: [hooks, harness, render]
---

## Context

Today at 07:30:30 two sessions started in one second: this one, `fde37e7c`, and `19b07bbc`, session L, restored by `resume`. The `hi` of 07:30:39 carries `--------` — `CLAUDE_SESSION_ID` is empty in the `!` substitution of the skill — so the ledger hook tied it to the start nearest before it, the foreign one, and refused every line of this session. A second `/hi` did not help: `hi_recorded` sets `ours = False` on the foreign start and only a new `session-start` of our own sets it back; a `resume` of this session at 07:46:53 did. The lesson line of 07:44 ends "A second /hi at 07:44 fixed the window", which is false.

## Problem

The window of a session is inferred from the order of starts around an unstamped `hi`. One foreign start between our start and our `hi` — a restored tab is enough — takes the `hi` away, and the session cannot recover by any command of its own. `rule-event-log` names this as a known limit since Case 9. The lesson page will be born with a wrong root cause.

## Given

`guppi event <name>` (`guppi/event.py`) writes `- HH:MM:SS <stamp> <event> <detail>`, the stamp from `--session` or the payload's `session_id`, `--------` when neither; registered on `SessionStart` and `PostToolUse` (`rule-hook-registry`, `.claude/settings.json`). The `/hi` skill (`rule-skill-hi`, `render_mode: full`) writes its `hi` through a `Recorded:` `!` substitution of `guppi event hi --session "${CLAUDE_SESSION_ID:-}"`; the variable is empty there, every `hi` in the logs is `--------`.
**＋** `hi_recorded` and `hi_moment` (`guppi/ledger.py:126-146, 176-196`): a `hi` after a `session-start` of this stamp with no other session's start in between; a `resume` or `compact` of our own does not close the window (case 14). `session_dir` — used by `ledger`, `gate`, `pretask`, `spec`, `cleanup` — takes the first such `hi`.
**＋** `UserPromptSubmit` hooks receive `session_id` and `prompt` on stdin; no matcher on the prompt text, so the filter is the script's. Not yet measured in this repository: whether the event fires for a slash command; the reading of 111.1 at the next `/hi` says.
**＋** `rule-event-log` (`built`, `estimate-event-log-records` `passed`): "Known limit" paragraph, lines 47–49. `rule-ledger-write` (`built`, `estimate-ledger-write-lifts` `passed`): the window paragraph, lines 41–46. `rule-hook-registry` (`built`, `estimate-hook-registry-rendered` `passed`), the Render is the `hooks` section of `settings.json`. `rule-skill-hi` (`draft`, `deferred_by: decision-case-106`).
**＋** The lesson line `lesson-hi-taken-by-a-session-started-in-the-same-second` is in the ledger of this session (07:47); its page is created by the next librarian run, and an `update` in the same yaml applies after it, in ledger order.
**－** The `--------` lines of the older logs are not rewritten; `event_log.md` is gitignored and no page points at a `hi` line.
**－** Case 106 (a render inside `/hi`) is not touched; it stays deferred on `rule-skill-hi`.
**－** The Frontier line F12 closes on this Case.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-111.2
