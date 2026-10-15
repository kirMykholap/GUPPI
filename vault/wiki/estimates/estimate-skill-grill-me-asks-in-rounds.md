---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-grill-me]]"
purpose: grill-me asks in rounds, finds facts itself and acts only after the shared understanding is confirmed, as the one text its rule page renders
method: by hand, the Render of rule-skill-grill-me as the Spec of the session holds it, read at Retro against the Criterion
checked: 2026-10-09
origin: raw/2026-09-26/2300/ledger.md#case-443.1
sprint: migration
created: 2026-09-26
tags: [harness, workflow]
---

## Criterion

When:
The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run --project .guppi guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

Then:
`uv run --project .guppi guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
**＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
**＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer, together with the lines of a list under it. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
**＋** The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark `🔹` and its name in bold. Directly under its name stands one `**After:**` line, indented two spaces with no list dash before the label, that says what holds with that option.
**＋** A list stands one item per line, never inside a sentence. This covers items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things. Under an `**After:**` line a list stands on the lines after it, indented as far as the label.
**＋** A quotation, words taken from a page, a file or a reply, stands as a blockquote on its own line under the sentence that introduces it and names its source, a fragment of a few words too; it never stands inside a sentence in quote marks. Under an `**After:**` line it stands on the line after it, indented as far as the label.
**＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
**＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
**－** An option carries nothing under it but its `**After:**` line: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
**－** A short series of words inside a sentence stays in the sentence.
**－** No line of a question except an option starts with `🔹`.
**－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `rule-orchestration`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
**－** The `**Context:**` paragraph of a round of `case-guppi`, its lists and quotations included, and the place of its case numbers are not read here. They are the promises of the Estimates of the rule of `.claude/agents/case-guppi.md`.
**－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

## Result

2026-10-09, by hand at Retro, the Render of rule-skill-grill-me with the five replaces of Case 744.1 in the Spec read against the Criterion: the After line stands two spaces under the option name with no dash, a list and a quotation under it indented as far as the label, the other lines of the Criterion unchanged

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
- 2026-10-03 status: failed → passed · raw/2026-10-03/0115/ledger.md#L7
- 2026-10-09 updated: the Criterion replaced whole — the After line of an option stands with no list dash (case 744.1) · [[decision-case-744.1]]
- 2026-10-09 status: pending → passed · raw/2026-10-08/2352/ledger.md#L36
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
