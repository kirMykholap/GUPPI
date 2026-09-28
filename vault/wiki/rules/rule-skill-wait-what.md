---
type: rule
kind: Leaf
purpose: Prevents a text the person did not understand from being explained again in the same dense words, or changed while it is explained
status: draft
enforcement: render
governs: .claude/skills/wait-what/SKILL.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-skill-wait-what-re-pitches]]"]
origin: raw/2026-09-28/1318/ledger.md#case-477.2
sprint: migration
created: 2026-09-28
tags: [harness, workflow]
---

## Purpose

Prevents a text the person did not understand from being explained again in the same dense words, or changed while it is explained. `/wait-what` writes the agent's last text again — a round of `case-guppi`, the short text on a Case, a reply — in the chat language, in plain words, with a concrete example and the terms of `vault/wiki/glossary.md`. It comes from the skill `wait-what` of github.com/mattpocock/skills and keeps its name. The upstream text asks for ASD-STE100 and `CONTEXT.md`: here they are short active sentences in the chat language and the glossary, since ASD-STE100 is a standard for English only. The main agent may start it too, when the person asks in words, so one text decides what a plain explanation holds. A request for it is its normal use, not a complaint about the agent's text (case 477.2).

## Render

<!-- rule-skill-wait-what -->
---
name: wait-what
description: "Stop. That last message did not land: re-pitch it. Run it when the person types /wait-what, or asks in words for a plain explanation of the agent's last text."
---

Wait, I don't understand where you've got to here. Re-pitch your last text — a round of questions, the short text on a Case, or a reply — in {{chat_lang}}.

Give a little context first. Then say the mechanism in plain words, with one concrete example of where it goes wrong. For each option, say what changes, as a before and after. Write short sentences, one idea per sentence, in the active voice.

Leave out case numbers and the history of a slug. Use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.

When you need a fact of a Case that you do not hold, ask the `case-guppi` of that Case by `SendMessage`. Do not guess it.

Change no option and no recommendation. End with the open question, asked again.
<!-- /rule-skill-wait-what -->

## History

- 2026-09-28 created · [[decision-case-477.2]]
- 2026-09-28 estimate estimate-skill-wait-what-re-pitches added · [[decision-case-477.2]]
