---
title: "A note of intent compiled as if it were testimony produces pages describing things nobody built"
type: lesson
status: archived
authority: intent-vs-testimony
basis: inference
sprint: S1
created: 2026-08-14
sources: ["raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "scripts/vault-coverage.sh", "scripts/vault-check.sh"]
tags: [vault, testing, process]
---

# Two kinds of source, and only one of them is evidence

Every source in `raw/` before 2026-08-14 was a **journal**: a session's testimony about a tree it
had just changed. The owner's notes are not that. They are **specifications written in the present
tense about a store that did not exist**, and the grammar of the two is identical.

So a unit reading «wiki/index.md — автоматически обновляемый каталог всех страниц» compiles
effortlessly into a page saying the index is an automatically updated catalogue of every page.
That page would be well-formed, atomic, tagged, linked, sourced, and **false** — the index is a map
and was never a catalogue ([[the-index-is-a-map-not-a-catalogue]]).

## Nothing in the toolchain can see it

- `vault-check.sh` reads **structure**: fields, folders, links, orphans, tags. A page's claim is
  outside its vocabulary entirely.
- `vault-coverage.sh` reads **accounting**: does every unit carry one of the four verdicts. A
  verdict of `page:X` asserts that X exists, never that X is true. This is the same gap
  [[ingest-is-units-and-verdicts]] names as *coverage is not fidelity*, arriving from a new
  direction: there, a page had gone stale behind the code; here, the page was never true at all.
- The librarian's own habits do not help. `basis: human` is the correct marking for a page compiled
  from the owner's words, and it is the **highest** rank a page can carry short of code. An
  intention marked `human` outranks the working mechanism that contradicts it.

## The discipline that catches it

**Compile a note against the tree, never on its own.** For each unit, one of three verdicts in
prose before any page is written: built — and name the page or file that implements it; built
differently — and say how; unbuilt — and say so in those words, on the page.

The first ingest of a note did that in a table
([[the-owners-instructions-note-and-what-was-built-from-it]]), and the table is the shape to reuse:
the ask on the left, its fate on the right, one row per instruction. Written as prose it reads as a
description of a working system; written as two columns it cannot.

**Where the note asks for something the build refused, the disagreement is the finding.** It is
marked on both pages and left unresolved, because choosing between the owner's design and the
sessions' record is a judgement about the project ([[the-librarian-writes-unattended]]).

## The cost of getting it wrong is not a bad page

It is a **rule that never existed being obeyed**. A page saying `wiki/tasks/` holds task status
sends the next session looking for a folder, and, finding none, to create one — the vault growing
a limb from a sentence nobody ever acted on. The second note is still uncompiled and carries the
same hazard.
