---
type: estimate
kind: QA
status: passed
target: "[[rule-context-size]]"
purpose: Past 400 000 tokens of context the agent passes the person a note that the session is costly and more work is not recommended
method: uv run --project .guppi pytest .guppi/tests/test_context.py -k limit; the live reading by hand at the first prompt past 400 000 tokens
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, session]
core: true
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

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
