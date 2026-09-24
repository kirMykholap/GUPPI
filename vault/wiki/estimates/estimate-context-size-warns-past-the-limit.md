---
type: estimate
kind: QA
status: pending
target: "[[rule-context-size]]"
purpose: Past 400 000 tokens of context the agent tells the person to close the session
method: uv run pytest tests/test_context.py -k limit; the live reading by hand at the first prompt past 400 000 tokens
origin: raw/2026-09-24/1303/ledger.md#case-392.2
sprint: migration
created: 2026-09-24
tags: [hooks, harness, session]
---

## Criterion

When:
The person sends a prompt and the `UserPromptSubmit` hook `uv run guppi context --prompt` reads the transcript; after the reply the `Stop` hook `uv run guppi context` runs.

Then:
At N of 400 000 or more, the `UserPromptSubmit` hook prints to the agent's context: `context: <N> tokens, past 400 000` and the order to tell the person to close the session with /retro, then /handoff, before the next Case.
**＋** The agent opens its reply with that recommendation.
**＋** At N of 400 000 or more, the line of the `Stop` hook ends with `— past 400 000: close the session`.
**－** Below 400 000 the `UserPromptSubmit` hook prints nothing.

## History

- 2026-09-24 created · [[decision-case-392.2]]
