---
type: estimate
kind: QA
status: passed
target: "[[rule-context-size]]"
purpose: Past 400 000 tokens of context the agent passes the person a note that the session is costly and more work is not recommended
method: uv run pytest tests/test_context.py -k limit; the live reading by hand at the first prompt past 400 000 tokens
checked: 2026-09-30
origin: raw/2026-09-24/1303/ledger.md#case-392.2
sprint: migration
created: 2026-09-24
tags: [hooks, harness, session]
---

## Criterion

When:
The person sends a prompt and the `UserPromptSubmit` hook `uv run guppi context --prompt` reads the transcript; after the reply the `Stop` hook `uv run guppi context` runs.

Then:
At N of 400 000 or more, the `UserPromptSubmit` hook prints to the agent's context `context: <N> tokens, past 400 000 — the session is already costly` and a note for the person, not an order: taking on more work is not recommended, and while the Frontier holds open items, deferring them is the better course.
**＋** The agent passes the note to the person in its reply and goes on with what the person asked.
**＋** At N of 400 000 or more, the line of the `Stop` hook ends with `— past 400 000: costly, better take no more work`.
**－** No text of either hook orders the agent or the person to close the session, and none names /retro or /handoff.
**－** Below 400 000 the `UserPromptSubmit` hook prints nothing, and the line of the `Stop` hook has no such end.

## Result

2026-09-30, uv run pytest tests/test_context.py -k limit (3 passed) and by hand on the transcript of session 876c4080: at the first prompt past the limit (22:15:59 UTC) the UserPromptSubmit hook printed "context: 400 814 tokens, past 400 000 … the session is already costly" and the note, not an order; the agent passed the note to the person in its reply and went on with Case 527 and the question the person had asked; the Stop line read "context: 400 814 tokens (+4 419 since the last reply) — past 400 000: costly, better take no more work"; no text named /retro or /handoff. Seen: in the UserPromptSubmit output the dash after "400 000" reached the context as U+FFFD, while the Stop line kept it

## History

- 2026-09-24 created · [[decision-case-392.2]]
- 2026-09-25 status: pending → failed · raw/2026-09-25/1228/ledger.md#L45
- 2026-09-25 updated: the Criterion replaced whole — past 400 000 tokens a note for the person, not an order to close the session (case 430) · [[decision-case-430]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0138/ledger.md#L4
