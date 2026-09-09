---
title: "The handoff splits: it stays a handoff, and everything that outlives a session becomes a knowledge base"
type: decision
status: archived
authority: vault-origin
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-12
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md", "raw/notes/2026-08-13-owners-note-second-brain-instructions.md"]
tags: [vault, process]
---

# Why this vault exists at all

**The owner's diagnosis, 2026-08-12:** `docs/HANDOFF.md` had become **a knowledge base wearing a
handoff's name**, and an agent had to read all of it before it could start. It was ~120 KB — 129 KB
by the time it was copied into `raw/`.

**The cost he objected to is not storage, it is the toll.** That file was read at the beginning of
**every** session, by **every** agent, whatever the task. A document that must be read in full
before any work begins is charged to work that has nothing to do with most of it.

This is a different complaint from the one
[[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]] records. That page is about
the document being **untrue** — appended to for weeks, carrying two versions of the same thing.
This one is about it being **expensive** even when true. Both point the same way, and the second is
what was actually said out loud.

## The shape he asked for

- **The handoff stays a handoff and nothing else** — what was done last session, what was not, what
  is handed over, what to watch. One page. **The test he gave: if it does not change between
  sessions, it does not belong in the handoff.** That test is now the journal's boundary
  ([[journal-vault-brief-each-artefact-has-one-owner]], [[the-handoff-template-maps-onto-the-categories]]).
- **Everything else becomes a knowledge base of several documents.**

## The categories were not invented; they were already in the file

His own list of what needed homes is the reason the four folders are the four they are: §6
«Известные ограничения» — deliberate deferrals, each with its consequence; §7 «Уроки процесса» —
classes of failure rather than incidents; §0.1 environment; §0.6 the process measurements; the
invariants scattered through §1–§5; and **the decisions-not-to-relitigate, which at that point lived
in three separate places in one file.**

Read against `CLAUDE.md`'s category rules, that list is `decisions`, `lessons`, `entities` and
`concepts` in the order he happened to say them. The material was already sorted by kind and only
needed addresses.

## The method question was answered in writing, and the answer is in `raw/notes/`

He named **Obsidian** as the reader and «second brain by Karpathy» as the method, and the source
said to ask him what he meant before designing the layout. **He had already answered, in two notes
of his own** — `raw/notes/2026-08-13-owners-note-second-brain-info.md` and
`…-second-brain-instructions.md`, which sat in `docs/` unread while this page said the question
still had to be asked. What they ask for:

- **compilation rather than RAG.** Knowledge is «вплавляется» into an existing structure by
  synthesis, not retrieved afresh from raw chunks at each query; the store is written by an agent
  for an agent to read;
- **three layers**: `raw/` as immutable truth, `wiki/` as compiled atomic notes
  (`entities/`, `concepts/`, `decisions/`, plus a `tasks/`), and `CLAUDE.md` as the constitution
  holding naming, the YAML schema, conflict handling and archiving;
- **`index.md` as an automatically updated catalogue of every page**;
- frontmatter of `title`, `type`, `status: active | deprecated`, `created`, `sources`, `tags`;
  kebab-case filenames; `[[wikilinks]]`; deprecate and move to `archive/`, never delete;
- **`/ingest`, `/lint` and `/pre-task`** by those names, with their triggers; a sprint closes by
  moving that sprint's handoffs into `archive/sprints/sprint-N/`; a git commit after each ingest,
  so an ingest can be undone;
- on a contradiction: mark it `> [!CAUTION] CONTRADICTION` **and ask the owner**.

**What was built differs from that in five places, each of them decided rather than drifted**: a
fourth category `lessons/` and no `tasks/` ([[the-wiki-has-five-folders-and-tasks-is-not-one]], which superseded [[the-wiki-has-no-tasks-folder]] on 2026-08-15 when a fifth category was added — this clause pointed
at [[active-tasks-stay-empty-until-a-tracker-exists]] until 2026-08-14, which is about the brief
and has since been retired);
`status: current` instead of `active`; four more frontmatter fields (`basis`, `authority`,
`sprint`, `decided`); an index that is a map rather than a catalogue
([[the-index-is-a-map-not-a-catalogue]], which now says whose conclusion that was); and ingest
redefined from «read the handoff and update the wiki» to units with verdicts
([[ingest-is-units-and-verdicts]]). The contradiction rule kept his marking and dropped the asking:
an answer given in chat leaves no artefact, so the marking *is* the artefact.

**A sixth divergence, decided 2026-08-13 by measurement:** closing a sprint does **not** move that
sprint's handoffs into `archive/sprints/sprint-N/`, because 31 pages cited `raw/handoffs/…` and the
first close would break every one of them — **95 of 111 when re-measured on 2026-08-15** —
[[a-sprint-closes-on-its-goal]].

**The instructions note has now been ingested — 2026-08-14, the vault's first compiled note** — and
the accounting the paragraph below asked for is
[[the-owners-instructions-note-and-what-was-built-from-it]], one row per instruction. It found the
six divergences above intact and **three more the single reading had missed**: filenames were to
carry a `[category]-` prefix and do not; `index.md` was to live under `wiki/` and lives at the
vault root; and `/lint` was to reconcile `entities/` against `decisions/`, which nothing does.
Reading a note is also its own hazard — [[an-intent-note-compiled-as-testimony-describes-things-nobody-built]].

*(This paragraph read «Neither note has been ingested» until 2026-08-14.)* **The method note,
`raw/notes/2026-08-13-owners-note-second-brain-info.md`, still has not been**: no sidecar, no
verdicts, nothing checked against it line by line.

**It was, on 2026-08-15** — [[the-owners-method-note-and-what-was-built-from-it]], and it is the
last source in `raw/` to be compiled. **The bullet list above is the finding.** Every clause of it
is true of the two notes taken together and **no single note says any of it**: `concepts/` is in
the method note only, `tasks/` in the instructions note only, and "kebab-case filenames" flattens a
straight conflict — one note asks for a `[category]-` prefix, the other's own example carries none.
Read as one voice, two sources stopped being two, and the cost was a divergence recorded against
the owner that was really a choice between two things he had written:
[[summarised-sources-lose-the-disagreement-between-them]],
[[filenames-carry-no-category-prefix]]. The clause on `index.md` as an automatic catalogue is
accurate for both notes and was met rather than refused
([[the-catalogue-is-generated-not-maintained]]).

## The rule that keeps the two documents from lying about each other

**`CLAUDE.md` holds the rules that are *enforced*; the knowledge base holds what is *known*. Do not
duplicate.** The reason is measured rather than tidy: *«a fact in both places will disagree with
itself within two slices — this file has done it three times already, each one recorded in §7».*

That is the same failure as a hand-edited brief ([[journal-vault-brief-each-artefact-has-one-owner]]) and as one
instruction copied into two skills ([[one-librarian-behind-every-caller]]): every copy of a rule is a
place where the rule can be corrected without the other copy noticing.

## What it obliges

The old entry point is not retired on a feeling that the migration is done — the gate is mechanical
and is [[handoff-retires-only-when-every-unit-has-a-verdict]]. And the directory this all lives in
is named by the owner, because Obsidian shows him that name: [[the-vault-directory]].
