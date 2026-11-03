---
type: estimate
kind: QA
status: passed
target: "[[rule-event-log]]"
method: pytest in .guppi/tests/test_event.py and .guppi/tests/test_gate.py with piped JSON payloads against a temp vault; by hand at Retro, git check-ignore on the event log of the day and one hook run through a pipe, timed, both written into the estimate line
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness]
core: true
---

## Criterion

When:
A session starts, a tool call completes, the person submits a prompt, or the agent calls a skill through `Skill`; `uv run --project .guppi guppi event <name>` and `uv run --project .guppi guppi gate` read the JSON payload through a pipe, its `session_id` the stamp.

Then:
After the start and one tool call, `raw/<date>/event_log.md` carries a `session-start` line with the session's stamp and a `tool` line after it.
**＋** On `/hi` whose `permission_mode` is `plan`, when no `hi` of this stamp follows its first `session-start`: the line `- HH:MM:SS <stamp> hi` and its `hi:` line on stdout, which names the session's folder; a second `/hi` writes nothing and prints `hi: already recorded`, with the time and the folder; exit 0.
**＋** On `/hi` whose `permission_mode` is any other value — `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions` — or is missing or empty, a second `/hi` included: no line, nothing on stdout, exit 2 with a reason on stderr that tells the person to turn plan mode on and type `/hi` again; Claude Code blocks the prompt, and the skill does not run.
**＋** Any other prompt is silent, and its `permission_mode` is not read: exit 0; an error goes to stderr only, exit 0.
**＋** A call of `pre-spec`, `retro` or `handoff` through `Skill` that the gate lets through appends `- HH:MM:SS <stamp> <mark>` — `prespec`, `retro`, `handoff` — in the form `guppi event` writes; a refusal writes no line; `hi` and other skills get no mark.
**＋** `git check-ignore` reports the log ignored by `vault/.gitignore`; a hook invocation with piped stdin that refuses nothing exits 0 and finishes under 2 s.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
