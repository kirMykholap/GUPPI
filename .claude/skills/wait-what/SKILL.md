---
name: wait-what
description: "Stop. That last message did not land: re-pitch it. Run it when the person types /wait-what, or asks in words for a plain explanation of the agent's last text."
---

Wait, I don't understand where you've got to here. Re-pitch your last text — a round of questions, the short text on a Case, or a reply — in Russian.

Give a little context first. Then say the mechanism in plain words, with one real example of where it goes wrong: a line of a page, a file, a ledger or the Case, quoted as it stands, with its path. Find the line yourself where you can read or search for it. When you cannot find it, ask the `case-guppi` of the Case by `SendMessage` which file and which line hold it, then read the file and quote the line yourself. Never make up an example, not even one marked as made up. When you find no real example, say so in one sentence, and give the mechanism without one.

Lay out each question of a round, and the options in the short text on a Case or in a reply, in the question shape of `.claude/skills/grill-me/SKILL.md`. Its labels may stand in Russian. Write short sentences, one idea per sentence, in the active voice.

Leave the case numbers and the history of a slug out of your own sentences. A quoted line keeps its case numbers as written. Use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.

When you need any other fact of a Case that you do not hold, ask the `case-guppi` of that Case by `SendMessage`. Do not guess it.

Change no option and no recommendation. End with the open question, asked again.
