---
type: estimate
kind: QA
status: failed
target: "[[rule-skill-grill-me]]"
purpose: grill-me asks in rounds, finds facts itself and acts only after the shared understanding is confirmed, as the one text its rule page renders
method: uv run guppi render --check; by hand, one round read in the chat in a session after the render, of the person's /grill-me or of case-guppi
checked: 2026-10-02
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
**＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer, together with the lines of a list under it. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
**＋** The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark `🔹` and its name in bold. Under it stands one nested `**After:**` item that says what holds with that option.
**＋** A list stands one item per line, never inside a sentence. This covers items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things. Under an `**After:**` item a list stands nested inside that item.
**＋** A quotation, words taken from a page, a file or a reply, stands as a blockquote on its own line under the sentence that introduces it and names its source, a fragment of a few words too; it never stands inside a sentence in quote marks. Under an `**After:**` item it stands indented to the text of the item, inside that item, and is no second item.
**＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
**＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
**－** An option carries nothing under it but its `**After:**` item: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
**－** A short series of words inside a sentence stays in the sentence.
**－** No line of a question except an option starts with `🔹`.
**－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `rule-orchestration`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
**－** The `**Context:**` paragraph of a round of `case-guppi`, its lists and quotations included, and the place of its case numbers are not read here. They are the promises of the Estimates of the rule of `.claude/agents/case-guppi.md`.
**－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

## Result

2026-10-02, session 2049: `uv run guppi render --check` exit 0; by hand, the rounds of case-guppi on Cases 596, 597, 598, 599 and 600 read in the chat: each question has its Now line, the Options label alone, each option with one After item, quotations as blockquotes under a sentence naming their source, the recommended answer on the arrow line, the person asked only for decisions; but the round on Case 599 opened its one question with `❓ **Q1** - **Should the Insight be marked closed now, and which decision should it name as the fix?**` with no colon after the title, against the numbered title line the Criterion sets

## History

- 2026-09-27 created · [[decision-case-443.1]]
- 2026-09-28 updated: the Criterion replaced whole — a round of case-guppi reads the frontier rule, finding facts and the confirmation; the form of its questions stays with estimate-case-build-writes-the-case (case 470) · [[decision-case-470]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/1318/ledger.md#L37
- 2026-09-29 updated: the Criterion replaced whole — every question of /grill-me and of case-guppi takes the Now and After shape, an option with nothing else under it, a translated label the same label (case 501.1) · [[decision-case-501.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L49
- 2026-09-29 updated: the Criterion replaced whole — the Options label, the 🔹 mark and a list one item per line (case 511.1) · [[decision-case-511.1]]
- 2026-09-29 updated: the Criterion replaced whole — a quotation stands as a blockquote on its own line (case 524.1) · [[decision-case-524.1]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/0248/ledger.md#L39
- 2026-09-30 status: failed → passed · raw/2026-09-30/1736/ledger.md#L20
- 2026-10-02 updated: the Criterion replaced whole - the main agent shows a round by rule-orchestration (case 595.19) · [[decision-case-595.19]]
- 2026-10-02 status: pending → failed · raw/2026-10-02/2049/ledger.md#L24
