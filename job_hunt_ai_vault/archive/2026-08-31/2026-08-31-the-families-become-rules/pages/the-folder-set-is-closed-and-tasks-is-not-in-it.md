---
title: "The folder set is closed, `rules/` joined it on 2026-08-17, and `tasks/` is still not in it"
type: decision
status: archived
authority: wiki-categories
binding: prohibition
basis: code
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md", "scripts/vault-check.sh", "scripts/vault-catalogue.sh"]
tags: [vault, process]
supersedes: [[the-wiki-has-five-folders-and-tasks-is-not-one]]
---

# The set, and what it is closed against

`wiki/decisions/`, `wiki/concepts/`, `wiki/entities/`, `wiki/lessons/`, `wiki/proposals/`,
`wiki/rules/`. **The set is not a convention anybody may extend in passing**: rule 1 of
`vault-check.sh` names every folder and fails if one is missing, and rule 2 fails a page whose
`type:` disagrees with the folder it sits in.

**`wiki/rules/` was added on 2026-08-17** — a rule the harness *renders* rather than a reader
remembers. It was decided on 2026-08-16 ([[rules-becomes-a-type-of-its-own]]) and built the next
day. It is the one category whose text is written to be delivered somewhere else, which is why it
carries `governs:` and never `authority:`
([[governs-is-a-path-from-the-repository-root]],
[[what-travels-from-a-rule-page-is-a-marked-slice]]).

## This page replaces one whose count was its claim

**[[the-wiki-has-five-folders-and-tasks-is-not-one]] said *five*, in its H1 and in its first line**,
and the tree now holds six. The predecessor's own history is the precedent: it retired
[[the-wiki-has-no-tasks-folder]], which said *four*, for exactly this reason. **A count in the claim
is the claim**, so the page is superseded rather than edited — and that is the boundary against
[[a-title-corrected-in-place-is-not-a-supersession]], which governs a stale number in a *title*,
where nothing is being asserted about the world beyond how the page is addressed.

The owner took this verdict himself on 2026-08-17, and it is his call rather than an ingest's: two
`current` pages disagreeing about the folder set is a question about the project.

## Rejected: `wiki/tasks/` — both reasons carried forward unchanged

The owner's instructions note of 2026-08-13 asks for it by name — «статус и детализация задач
текущего и прошлых спринтов» ([[the-owners-instructions-note-and-what-was-built-from-it]]). **Both
grounds still stand, and neither is weakened by the set having grown twice since.**

- **The tracker owns task status; the vault owns what we learned from a task.** That division is
  the owner's own, restated on 2026-08-14 when he removed the brief's placeholder section
  ([[the-brief-has-no-active-tasks-section]]). A task list here would be a second copy of something
  that changes hourly, and it would be the copy people read.
- **Nothing would write it.** The librarian compiles from journals, and a journal's `State` section
  is the one section filed `journal` wholesale and never compiled
  ([[the-handoff-template-maps-onto-the-categories]]). A folder filled by hand in a store written
  by an agent goes stale in one sprint.

The test is not *is this page about something that does not exist yet*. It is: **does a source in
`raw/` produce it, and does it go stale between two edits or on its own?** A proposal passes both. A
rule passes both — it is compiled from a session like everything else, and it is superseded rather
than maintained. A task list fails both, with a folder, a status field or any other shape.

Also rejected in the earlier pass, and still: **`invariants/`**. A decision and the rule it produced
are one fact at two moments of its life. Note that `rules/` is *not* that folder returning: an
invariant nobody chose stays in `concepts/`, and a `rules` page exists because its text has a
**destination**, not because it is more binding.

## The price of a category, measured for the second time

The 2026-08-15 addition cost: rule 1 of `vault-check.sh`, the section loop in
`vault-catalogue.sh`, the vault's own `CLAUDE.md`, `index.md`, and the selftest — one change.
**The 2026-08-17 addition cost the same list minus `index.md`, plus the frontmatter pass, which had
to learn `governs:`.** `index.md` was deliberately *not* extended
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]), and the type rule again cost
nothing, because `want` is the folder name minus its trailing `s`.

**The folder set now exists in four places** — rule 1, `vault-catalogue.sh`, the vault's
`CLAUDE.md` and `index.md` — and that is the shape this page warned about: a category needing a new
list somewhere is a category that will be forgotten in one of the lists. It was, within a day.

Categories appear about once a year elsewhere; this store has taken three in three days. That is a
warning about the store being young, not a licence. **If a fourth seems needed soon, the thing being
classified is probably a tag.**

## The second witness, unchanged

The owner's *other* note of 2026-08-13 lists `entities/`, `concepts/`, `decisions/` and no `tasks/`
at all ([[the-owners-method-note-and-what-was-built-from-it]]). The folder set that exists is the
one he wrote down twice, minus a folder he wrote down once, plus `lessons/`, `proposals/` and
`rules/`, which no note has.

This is not marked as a contradiction, for the reason the predecessor gave and that still holds:
**a marking waits for the owner to speak again, and it is removed by nobody else** — and he has,
repeatedly, on this substance.

## What it obliges

When a tracker is installed, what has to be revisited is [[the-brief-has-no-active-tasks-section]]
— the brief quoting its output verbatim — and **not this page**. A tracker arriving is not an
argument for a `tasks/` folder; it is the argument against one.

# The owner has now stated the overturn, and this page stays `current` until somebody writes it — 2026-08-23

**He said where tasks live, and he scheduled the conversation rather than closing it:**

> **owner: задачи живут в wiki/tasks. Оттуда они подкрепляются к proposals, concepts. Это
> отдлеьная тема для обсуждения на s3.**

> **owner: да, задачи должны отмечаться.**

**Two claims and a schedule.** Tasks live in `wiki/tasks/` and attach from there to proposals and
concepts; a task is ticked. And it is *a separate topic for discussion* — which is why nothing here
is a supersession and this page is not `deprecated`.

**The overturn is scoped and deferred to S4**, with the `built` mark that depends on it: a mark
meaning *the design is complete and the task list is written* cannot be tested while there is
nowhere for a task list to be
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

## What the page overturning this one owes an answer to, written down so it is not rediscovered

- **Ground 2 of this prohibition — *nothing would write it*.** His decision names where tasks live
  and does not say who ticks them; the second block above says they are ticked and not by whom. The
  ground is not dissolved by either.
- **The folder-split rejection on [[a-decision-declares-whether-it-binds]]**, which cited the closed
  folder set as its ground. If the set opens, that argument has to be restated or withdrawn.
- **[[the-brief-has-no-active-tasks-section]] and [[the-retro-has-no-action-queue]]**, both live
  prohibitions of the same substance. They are superseded or carved out, and naming them is not an
  argument against the overturn — it is the list it owes an answer to.

## Beads is named again and has still never been put back to him

**Named once on 2026-08-17 as the tracker this project intends to adopt, with nothing designed.**
It revives ground 1 of this prohibition — that a tracker arriving is the argument against a
`tasks/` folder rather than for one — and it was not raised with him on 2026-08-23 either
([[a-question-asked-is-not-a-question-answered]]).
