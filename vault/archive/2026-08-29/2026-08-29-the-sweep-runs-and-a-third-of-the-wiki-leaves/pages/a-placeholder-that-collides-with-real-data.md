---
title: "A placeholder that collides with real data is a message that has to be decoded"
type: lesson
status: archived
authority: placeholder-collision
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "scripts/vault-check.sh", ".claude/templates/handoff.md"]
tags: [testing, vault]
---

# The message that read as a finding and was not

Rule 8 of `vault-check.sh` printed **`unexpected [none]`** when nothing was unexpected: the rule
built two halves of a message, and the empty half was filled with the word *none*.

**`none` is the exact word the handoff template tells a writer to put in an empty section.** So the
message read as though a section called *none* had appeared in the journal — a real, plausible
finding, and a reader has to know the script to rule it out.

**The fix is to print only the half that has content.** Absence is expressed by the half not being
there, which is unambiguous and shorter.

# Why this is worth writing down

**A diagnostic is read by someone who does not know the code**, and at the worst possible moment.
Every token in it competes with the reader's model of the domain — and *none*, *empty*, *default*,
*unknown* and *null* are all words that live in the data as well as in the message.

The rule: **an empty slot is not printed. If it must be, name it in words the domain does not use.**

This project has the neighbouring failure already — a check that passed because a placeholder in an
example satisfied a search ([[an-example-inside-a-code-block-satisfies-a-search]]). Both are the
same confusion between the language a tool speaks about data and the data itself.
