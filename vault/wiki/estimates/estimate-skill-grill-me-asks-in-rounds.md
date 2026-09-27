---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-grill-me]]"
purpose: grill-me asks in rounds, finds facts itself and acts only after the shared understanding is confirmed, as the one text its rule page renders
method: uv run guppi render --check; by hand, one /grill-me of the person in a session after the render, its rounds read in the chat
origin: raw/2026-09-26/2300/ledger.md#case-443.1
sprint: migration
created: 2026-09-26
tags: [harness, workflow]
---

## Criterion

When:
The person types `/grill-me` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

Then:
`uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
**＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, each numbered, with a title, a body and a recommended answer, and the agent waits for the answers before the next round.
**＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
**＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
**－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

## History

- 2026-09-27 created · [[decision-case-443.1]]
