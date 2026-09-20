---
type: estimate
kind: QA
status: passed
target: "[[rule-event-log]]"
method: pytest in tests/test_event.py and tests/test_gate.py with piped JSON payloads against a temp vault; the git-ignore and timing readings once by hand, through a pipe, written into the estimate line
checked: 2026-09-20
origin: raw/2026-09-09/ledger.md#case-9
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness]
---

## Criterion

Given:
The hooks `uv run guppi event <name>` and `uv run guppi gate` run through a pipe with a JSON payload; `session_id` is the stamp.
**＋** `raw/<date>/event_log.md` is in `.gitignore`; the ledger hook reads the session's `hi` from it.

When:
A session starts, a tool call completes, the person submits a prompt, the agent calls a skill through `Skill`.

Then:
After the start and one tool call the log carries a `session-start` line with the session's stamp and a `tool` line after it.
**＋** On `/hi` (trimmed, or `/hi …`), when no `hi` of this stamp follows its first `session-start`: the line `- HH:MM:SS <stamp> hi` and stdout `hi: HH:MM:SS <stamp> → raw/<date>/<HHMM>/`; a second `/hi` writes nothing, stdout `hi: already recorded at HH:MM:SS → raw/<date>/<HHMM>/`; any other prompt is silent; exit 0 either way, an error on stderr only.
**＋** A call of `pre-spec`, `retro` or `handoff` through `Skill` that the gate lets through appends `- HH:MM:SS <stamp> <mark>` — `prespec`, `retro`, `handoff` — in the form `guppi event` writes; a refusal writes no line; `hi` and other skills get no mark.
**＋** `git check-ignore` reports the file ignored; a hook invocation with piped stdin exits 0 and finishes under 2 s.

## Result

2026-09-20, `uv run pytest -q tests/test_event.py tests/test_gate.py` 63 green; live, `raw/2026-09-20/event_log.md` of session c27cd9be: `09:58:36 session-start startup`, `09:58:48 hi` with the tool line after it and the `hi:` line in the first turn's context, no second hi line after the second `/hi` of the day, `12:23:17 prespec` written by guppi gate on the typed `/pre-spec`; `git check-ignore -v` names `.gitignore:47`; `uv run guppi event prompt` through a pipe on a plain prompt exited 0 in 164 ms and wrote no line

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
