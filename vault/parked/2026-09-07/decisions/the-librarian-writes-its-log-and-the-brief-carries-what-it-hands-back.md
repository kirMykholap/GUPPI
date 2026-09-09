---
title: "The librarian writes its own log, and the brief carries what it hands back to a session"
type: decision
status: current
authority: librarian-feedback-write
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-25

> **owner:** «это немного странно, что ingest пишет туда свои записи. Зачем? нужно улучшить этот
> механизм, потому что сейчас он выглядит плохо»

And on the destination:

> **owner:** «Библиотекарь пусть пишет только в свой log. Но то, что нужно передать нам - он пишет
> в брифе. Чтобы мы не потеряли его запрос к нам»

**The librarian stops writing `.superpowers/sdd/vault-feedback.md`.** Its findings go to `log.md`,
which is its own register, and what is addressed to the session reaches the brief.

**The session's correction, which he accepted: the brief is derived and is never written by hand.**
So the librarian writes `log.md`, and whatever generates `brief.md` surfaces from there what is
addressed to the session — **by generation, not by a hand-written line**
([[the-brief-is-stamped-with-its-commit]]).

# The defect this removes is structural, and it is not a matter of taste

**`/handoff` runs before `/ingest`, by the ritual's own order.** So anything an ingest writes into the
feedback file is drained by the *next* session's handoff and filed under the wrong session
([[a-session-ends-with-retro-then-handoff-then-ingest]]).

**Measured on the day of the ruling: the file held 115 records, and roughly a third had been written
by the previous session's ingest** — after that session's handoff had already emptied it.

**A page here calls that lag the order rather than a defect**
([[a-feedback-line-written-during-an-ingest-reaches-the-vault-one-session-late]]). The owner's ruling
goes the other way about the same arrangement, and the disagreement is named rather than settled
here: that page reasons about a line the *session* files late, while what he objected to is the
librarian filing into a channel it does not own.

# What it obliges

**`.claude/skills/ingest/SKILL.md` stops instructing the librarian to write that file**, and the
brief generator learns to read the log. **Neither is done**, and the rule about who empties a
feedback line is untouched for a session's own lines
([[whoever-filed-a-feedback-line-empties-it]]).

# The obligation above names an instruction that never existed — corrected 2026-08-26

**Nothing ever instructed the librarian to write that file.** Not `.claude/skills/ingest/SKILL.md`,
not `.claude/agents/vault-librarian.md`, not the vault's own `CLAUDE.md`. **It was practice with no
written source**, checked across all three on 2026-08-26.

**So the repair is not the deletion this page describes.** It is a **written prohibition** plus the
**replacement channel**, and both were built that day: the prohibition stands in
`.claude/skills/ingest/SKILL.md` beside a `## From the librarian` section in the brief's shape,
generated from `log.md`, so the two are read together
([[the-harness-changes-nobody-asked-for-stand]]).

**The sentence above is left standing because it is what the ruling was compiled into**, and the
correction is dated where the text became false
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]). **A page that names an
obligation as *removing an instruction* sends the executing session looking for a line that does not
exist**, which is the cost this note removes.

**No rule page governs `.claude/skills/ingest/SKILL.md`**, so the prohibition now lives in a copy
nothing checks — the durable defect that file's own text already records
([[no-rule-reads-a-harness-file]], [[the-harness-is-compiled-not-maintained]]).
