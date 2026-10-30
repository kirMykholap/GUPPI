---
type: estimate
kind: QA
status: passed
target: "[[rule-event-log]]"
method: pytest in .guppi/tests/test_event.py and .guppi/tests/test_gate.py with piped JSON payloads against a temp vault; by hand at Retro, git check-ignore on the event log of the day and one hook run through a pipe, timed, both written into the estimate line
checked: 2026-10-30
origin: raw/2026-09-09/ledger.md#case-9
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness]
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

2026-10-30, Retro of session 2341: uv run --project .guppi pytest .guppi/tests/test_event.py .guppi/tests/test_gate.py 74 passed; git check-ignore -v vault/raw/2026-10-29/event_log.md prints vault/.gitignore:2:raw/*/event_log.md; one guppi event prompt run through a pipe with a made-up prompt payload exited 0 in 0.24 s

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-9
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-14 criterion: case 111.1 added · [[decision-case-111.1]]
- 2026-09-14 criterion: case 125 added · [[decision-case-125]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L23
- 2026-09-14 status: passed → passed · raw/2026-09-14/1029/ledger.md#L34
- 2026-09-14 status: passed → passed · raw/2026-09-14/1229/ledger.md#L1
- 2026-09-14 criterion: case 136.1 added · [[decision-case-136.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L25
- 2026-09-20 ref `rule-pretask` → `rule-prespec` · [[decision-case-261]]
- 2026-09-20 updated: the recut to the shape of case 193: the base text and the blocks 111.1, 125, 136.1 folded into one Criterion, the mark pretask now prespec, method as a field; pending for the reading (case 265.1) · [[decision-case-265.1]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L27
- 2026-09-27 updated: the Criterion replaced whole — a /hi outside plan mode writes no hi and exits 2; the Given folded into When (case 445.6) · [[decision-case-445.6]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L4
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-30 updated: the Criterion replaced whole — git check-ignore reports the log ignored by vault/.gitignore; the method drops the /hi readings by hand · [[decision-case-917.2]]
- 2026-10-30 status: pending → passed · raw/2026-10-29/2341/ledger.md#L36
