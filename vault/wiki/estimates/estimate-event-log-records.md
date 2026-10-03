---
type: estimate
kind: QA
status: passed
target: "[[rule-event-log]]"
method: pytest in tests/test_event.py and tests/test_gate.py with piped JSON payloads against a temp vault; the git-ignore and timing readings once by hand, through a pipe, written into the estimate line; by hand, one /hi outside plan mode and one in it, the permission_mode of each payload written into the reading
checked: 2026-10-03
origin: raw/2026-09-09/ledger.md#case-9
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness]
---

## Criterion

When:
A session starts, a tool call completes, the person submits a prompt, or the agent calls a skill through `Skill`; `uv run guppi event <name>` and `uv run guppi gate` read the JSON payload through a pipe, its `session_id` the stamp.

Then:
After the start and one tool call, `raw/<date>/event_log.md` carries a `session-start` line with the session's stamp and a `tool` line after it.
**＋** On `/hi` whose `permission_mode` is `plan`, when no `hi` of this stamp follows its first `session-start`: the line `- HH:MM:SS <stamp> hi` and its `hi:` line on stdout, which names the session's folder; a second `/hi` writes nothing and prints `hi: already recorded`, with the time and the folder; exit 0.
**＋** On `/hi` whose `permission_mode` is any other value — `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions` — or is missing or empty, a second `/hi` included: no line, nothing on stdout, exit 2 with a reason on stderr that tells the person to turn plan mode on and type `/hi` again; Claude Code blocks the prompt, and the skill does not run.
**＋** Any other prompt is silent, and its `permission_mode` is not read: exit 0; an error goes to stderr only, exit 0.
**＋** A call of `pre-spec`, `retro` or `handoff` through `Skill` that the gate lets through appends `- HH:MM:SS <stamp> <mark>` — `prespec`, `retro`, `handoff` — in the form `guppi event` writes; a refusal writes no line; `hi` and other skills get no mark.
**＋** `git check-ignore` reports the log ignored by `.gitignore`; a hook invocation with piped stdin that refuses nothing exits 0 and finishes under 2 s.

## Result

2026-10-03, at the /hi of session 1416: `uv run pytest -q tests/test_event.py tests/test_gate.py` 74 passed; `git check-ignore -v` names `.gitignore:47` for vault/raw/2026-10-03/event_log.md; `uv run guppi event prompt` through a pipe on a plain prompt exited 0 in 187 ms and wrote no line; by hand, session 682b0e2f: the /hi of 14:16:36 came in permission mode `auto`, the hook refused it telling the person to turn plan mode on and type /hi again, Claude Code blocked the prompt, the skill did not run and the event log holds no line for it; the /hi of 14:16:59 in plan mode wrote `14:16:59 682b0e2f hi` after `14:16:26 682b0e2f session-start startup` with a tool line after it, and its `hi:` line names raw/2026-10-03/1416/; the `prespec` mark of session 26e79919 stands at 14:08:34 beside its Skill call; not exercised: a second /hi printing `hi: already recorded`

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
