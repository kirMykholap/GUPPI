---
type: rule
kind: Leaf
purpose: Prevents a text the person did not understand from being explained again in the same dense words, or changed while it is explained
status: built
enforcement: render
governs: .claude/skills/wait-what/SKILL.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-skill-wait-what-re-pitches]]"]
origin: raw/2026-09-28/1318/ledger.md#case-477.2
sprint: migration
created: 2026-09-28
tags: [harness, workflow]
core: true
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

Give a little context first. Then say the mechanism in plain words, with one real example of where it goes wrong: a line of a page, a file, a ledger or the Case, quoted as it stands, with its path. Find the line yourself where you can read or search for it. When you cannot find it, ask the `case-guppi` of the Case by `SendMessage` which file and which line hold it, then read the file and quote the line yourself. Never make up an example, not even one marked as made up. When you find no real example, say so in one sentence, and give the mechanism without one.

Lay out each question of a round, and the options in the short text on a Case or in a reply, in the question shape of `.claude/skills/grill-me/SKILL.md`. Its labels may stand in {{chat_lang}}. Write short sentences, one idea per sentence, in the active voice.

Leave the case numbers and the history of a slug out of your own sentences. A quoted line keeps its case numbers as written. Use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.

When you need any other fact of a Case that you do not hold, ask the `case-guppi` of that Case by `SendMessage`. Do not guess it.

Change no option and no recommendation. End with the open question, asked again.
<!-- /rule-skill-wait-what -->

## History

- 2026-09-28 created · [[decision-case-477.2]]
- 2026-09-28 estimate estimate-skill-wait-what-re-pitches added · [[decision-case-477.2]]
- 2026-09-29 deferred · [[decision-case-496]]
- 2026-09-29 defer by decision-case-496 superseded · [[decision-case-502]]
- 2026-09-29 updated: the re-pitch quotes a real line with its path, found by the main agent or located through case-guppi, never a made-up one; options follow the question shape of the grill-me template (case 502) · [[decision-case-502]]
- 2026-09-30 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
