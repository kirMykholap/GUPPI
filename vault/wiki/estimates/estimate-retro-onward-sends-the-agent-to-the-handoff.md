---
type: estimate
kind: QA
status: pending
target: "[[rule-retro-onward]]"
purpose: Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a turn and not on a reply that opens with STOP:, and is silent otherwise, counting nothing
method: "uv run pytest tests/test_onward.py; by hand at the first run from /work to the librarian after the render: the event log, the replies of the turn and handoff.md, recorded in the estimate line"
origin: raw/2026-09-29/2024/ledger.md#case-531.9
sprint: migration
created: 2026-09-29
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run guppi onward` receives the payload of the end of a reply of the main agent.

Then:
It exits 2 when the event log of the session's window holds the mark `retro` of this session, `raw/<date>/<hi HHMM>/handoff.md` does not stand, `stop_hook_active` is false, and the reply that ended does not open with `STOP:`.
**＋** Its reason on stderr tells the agent to commit the session folder and call `/handoff`, and, when a condition of `vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person instead.
**＋** In every other case with no error of its own it exits 0 and prints nothing: before the mark `retro`, once `handoff.md` stands, on a reply that follows a refusal of a `Stop` hook, and on a reply that opens with `STOP:`.
**＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck` and `uv run guppi context`.
**－** It counts nothing, reads no test result and calls no model: its judgment is the mark, the file, the flag and the first word of the reply.
**－** Without a `hi` of the session in the event log, and with no error of its own, it exits 0.
**－** It writes no file and no mark.

## History

- 2026-09-30 created · [[decision-case-531.9]]
- 2026-09-30 updated: the Criterion replaced whole — the exits 0 of the judgment hold with no error of the hook's own (case 555.4) · [[decision-case-555.4]]
