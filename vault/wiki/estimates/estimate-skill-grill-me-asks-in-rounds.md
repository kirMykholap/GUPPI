---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-grill-me]]"
purpose: grill-me asks in rounds, finds facts itself and acts only after the shared understanding is confirmed, as the one text its rule page renders
method: uv run guppi render --check; by hand, one round read in the chat in a session after the render, of the person's /grill-me or of case-guppi
origin: raw/2026-09-26/2300/ledger.md#case-443.1
sprint: migration
created: 2026-09-26
tags: [harness, workflow]
---

## Criterion

When:
The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

Then:
`uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
**＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
**＋** On the person's `/grill-me`, each question is numbered, with a title, a body and a recommended answer.
**＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
**＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
**－** The form of a round of `case-guppi` is not read here: it is the promise of `estimate-case-build-writes-the-case`.
**－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

## History

- 2026-09-27 created · [[decision-case-443.1]]
- 2026-09-28 updated: the Criterion replaced whole — a round of case-guppi reads the frontier rule, finding facts and the confirmation; the form of its questions stays with estimate-case-build-writes-the-case (case 470) · [[decision-case-470]]
