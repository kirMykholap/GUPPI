---
type: estimate
kind: QA
status: passed
target: "[[rule-context-size]]"
purpose: Past 400 000 tokens of context the agent passes the person a note that the session is costly and more work is not recommended
method: uv run --project .guppi pytest .guppi/tests/test_context.py -k limit; the live reading by hand at the first prompt past 400 000 tokens
checked: 2026-09-30
origin: raw/2026-09-24/1303/ledger.md#case-392.2
sprint: migration
created: 2026-09-24
tags: [hooks, harness, session]
---

## Criterion

When:
The person sends a prompt and the `UserPromptSubmit` hook `uv run --project .guppi guppi context --prompt` reads the transcript; after the reply the `Stop` hook `uv run --project .guppi guppi context` runs.

Then:
At N of 400 000 or more, the `UserPromptSubmit` hook prints to the agent's context `context: <N> tokens, past 400 000 — the session is already costly` and a note for the person, not an order: taking on more work is not recommended, and while the Frontier holds open items, deferring them is the better course.
**＋** The agent passes the note to the person in its reply and goes on with what the person asked.
**＋** At N of 400 000 or more, the line of the `Stop` hook ends with `— past 400 000: costly, better take no more work`.
**－** No text of either hook orders the agent or the person to close the session, and none names /retro or /handoff.
**－** Below 400 000 the `UserPromptSubmit` hook prints nothing, and the line of the `Stop` hook has no such end.

## Result

2026-09-30, `uv run pytest tests/test_context.py -k limit` (3 passed) and the bytes of the transcript of session 876c4080 read by grep: 6 UserPromptSubmit hook lines (hook_success and attachment) hold "past 400 000 — the session is already costly" with the dash as U+2014, 14 matches hold "— past 400 000: costly, better take no more work" of the Stop line, and the file holds no U+FFFD, neither as raw bytes nor escaped; the first prompt past the limit (22:15:59 UTC, 400 814 tokens), the note not an order, the agent passing it on and going on with the person's question, and no /retro or /handoff in either hook's text stand as the reading of session 0138 recorded them, not read again; the U+FFFD that reading reported came from its scratchpad script printing in cp1252 without PYTHONIOENCODING, not from the hook

## History

- 2026-09-24 created · [[decision-case-392.2]]
- 2026-09-25 status: pending → failed · raw/2026-09-25/1228/ledger.md#L45
- 2026-09-25 updated: the Criterion replaced whole — past 400 000 tokens a note for the person, not an order to close the session (case 430) · [[decision-case-430]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0138/ledger.md#L4
- 2026-09-30 status: passed → passed · raw/2026-09-30/0248/ledger.md#L10
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
