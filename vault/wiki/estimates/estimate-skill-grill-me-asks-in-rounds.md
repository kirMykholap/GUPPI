---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-grill-me]]"
purpose: grill-me asks in rounds, finds facts itself and acts only after the shared understanding is confirmed, as the one text its rule page renders
method: uv run guppi render --check; by hand, one round read in the chat in a session after the render, of the person's /grill-me or of case-guppi
checked: 2026-09-29
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
**＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
**＋** Each option starts on its own line as a list item with its name in bold. Under it stands one nested `**After:**` item that says what holds with that option.
**＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
**＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
**－** An option carries nothing under it but its `**After:**` item: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
**－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `estimate-case-protocol-shows-the-built-case`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
**－** The Context paragraph of a round of `case-guppi` and the place of its case numbers are not read here. They are the promises of `estimate-case-build-writes-the-case` and `estimate-case-build-writes-a-plain-round`.
**－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

## Result

2026-09-29, uv run guppi render --check exit 0; by hand, the rounds of case-guppi in session 1134: each question opens with its ❓ Qn line, one Now line, options as bold items with one nested After item each, closes with the ➡️ line; facts looked up by the agent; nothing acted on before the person's word

## History

- 2026-09-27 created · [[decision-case-443.1]]
- 2026-09-28 updated: the Criterion replaced whole — a round of case-guppi reads the frontier rule, finding facts and the confirmation; the form of its questions stays with estimate-case-build-writes-the-case (case 470) · [[decision-case-470]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/1318/ledger.md#L37
- 2026-09-29 updated: the Criterion replaced whole — every question of /grill-me and of case-guppi takes the Now and After shape, an option with nothing else under it, a translated label the same label (case 501.1) · [[decision-case-501.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L49
