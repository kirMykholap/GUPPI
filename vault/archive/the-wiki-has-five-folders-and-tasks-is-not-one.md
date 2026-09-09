---
title: "`tasks/` is still not a folder of the wiki, and `proposals/` is not a way back to it"
type: decision
status: deprecated
authority: wiki-categories
basis: code
sprint: S1
decided: 2026-08-15
created: 2026-08-15
sources: ["raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md", "docs/superpowers/specs/2026-08-13-second-brain-design.md", "scripts/vault-check.sh", "scripts/vault-catalogue.sh"]
tags: [vault, process]
supersedes: [[the-wiki-has-no-tasks-folder]]
superseded_by: [[the-folder-set-is-closed-and-tasks-is-not-in-it]]
---

# Five folders, the one that was asked for and not built, and the one added on 2026-08-15

> [!WARNING] DEPRECATED 2026-08-17
> **The set is six, not five.** `wiki/rules/` was decided on 2026-08-16
> ([[rules-becomes-a-type-of-its-own]]) and built on 2026-08-17, which makes the H1 and the first
> line of this page wrong - so it is retired rather than edited, on this page's own precedent. The
> successor is [[the-folder-set-is-closed-and-tasks-is-not-in-it]], and it carries **both reasons
> against `tasks/` unchanged**, plus the boundary this page drew against `proposals/`, extended to
> `rules/`: a rule page is compiled from a source in `raw/` like every other page here, and it is
> superseded rather than maintained. **The owner took this verdict himself on 2026-08-17.** Kept
> because "what did the folder set look like before the sixth, and what was the argument then" is a
> real question - and because the price of a category, measured here for the first time, is the
> paragraph the successor measures against.

`wiki/decisions/`, `wiki/concepts/`, `wiki/entities/`, `wiki/lessons/`, `wiki/proposals/`. The set
is not a convention anybody may extend in passing: `vault-check.sh` rule 1 names all five and fails
if one is missing, and rule 2 fails a page whose `type:` disagrees with the folder it sits in.

**This page replaces [[the-wiki-has-no-tasks-folder]]**, which said *four*, in its title and in its
first line. The count was the claim, so the page was retired rather than edited — the schema's own
rule, and the reason a reader who greps `four folders` now arrives at an archived page that names
its successor instead of at a current page that is wrong.

**`wiki/proposals/` was added on 2026-08-15** — what was raised or deferred and never built. The
decision itself, and why it is a folder rather than a `status:` value, is
[[proposals-are-a-folder-not-a-status]].

## Rejected: `wiki/tasks/`

The owner's instructions note of 2026-08-13 asks for it by name — «статус и детализация задач
текущего и прошлых спринтов» ([[the-owners-instructions-note-and-what-was-built-from-it]]). Two
reasons, and they are of different weights. **Both still stand.**

- **The tracker owns task status; the vault owns what we learned from a task.** That division is
  the owner's own, restated by him on 2026-08-14 when he removed the brief's placeholder section
  ([[the-brief-has-no-active-tasks-section]]). A task list inside the vault would be a second copy
  of something that changes hourly, and it would be the copy people read.
- **Nothing would write it.** The librarian compiles from journals, and a journal's §1 is state —
  the only section that is `journal` wholesale and never becomes a page
  ([[the-handoff-template-maps-onto-the-categories]]). A `tasks/` folder would be filled by hand or
  not at all, and a folder filled by hand in a store written by an agent goes stale in one sprint.

## Why the second reason does not also refuse `proposals/`

It is the reason that matters here, because on a first reading it reaches the new folder too: a
proposal is about work not done, which is what a task list is about. **The two differ on who writes
the page and out of what**, and that is the whole boundary.

**A proposal is compiled, by the librarian, from what was said in a session** — exactly like every
other page in `wiki/`. Its source is a journal or a note in `raw/`, its writer is the same one
writer, and it is written once and then superseded, not maintained. Nothing about it is kept
current by hand; a proposal that was built or refused is retired with `superseded_by:`, which is a
single edit at a single moment.

**A task list is not compiled from anything.** It changes hourly, its truth is the state of work
this afternoon, and nothing in `raw/` produces it — so it could only be kept by hand, which is the
sentence above.

So the test is **not** "is this page about something that does not exist yet". It is: *does a
source in `raw/` produce it, and does it go stale between two edits or on its own?* A proposal
passes both. A task list fails both, and would fail them with a folder, a status field, or any
other shape anybody proposes for it.

## Also rejected, in the same pass: `invariants/`

A decision and the rule it produced are one fact at two moments of its life, and two folders would
have filed it twice on day one. That is why `concepts/` holds invariants that grew from a decision
*and* facts nobody chose — PostgreSQL's `now()` being constant within a transaction was not decided
by anyone.

## A second witness arrived on 2026-08-15, and it is on this page's side

The owner's *other* note of 2026-08-13 lists the categories as `entities/`, `concepts/`,
`decisions/` — **no `tasks/` at all** — and asks by name for the `concepts/` the instructions note
never mentions ([[the-owners-method-note-and-what-was-built-from-it]]). So the folder set that was
built is the one he wrote down twice, minus a folder he wrote down once, plus `lessons/`, which
neither note has, plus `proposals/`, which neither note has either and which he asked for by its
question rather than by its name. `type: task` likewise appears in one note's enum and
`type: concept` in the other's.

## Why this is not marked as a contradiction, while the index was

The note is `human` and this page is `code`, and on those markings alone the note would outrank the
build. It does not, because **the owner spoke again later on the same substance**: the 2026-08-14
decision above states the ownership rule in his own words. The `index.md` row of the same note had
no such later word behind it, which is why that one carried a `> [!CAUTION] CONTRADICTION` and this
one carries an explanation — until the owner supplied that later word too, on 2026-08-15, by having
the catalogue generated ([[the-catalogue-is-generated-not-maintained]]). The principle is the point
worth keeping: **a marking waits for the owner to speak again, and it is removed by nobody else.**

## What it obliges

A new category is a change to the map, not a page. The 2026-08-15 addition is the measured price of
one: **rule 1 of `vault-check.sh`, the section loop in `vault-catalogue.sh`, the vault's own
`CLAUDE.md`, `index.md`, and the selftest, all in one change** — and the type rule cost nothing,
because `want` is the folder name minus its trailing `s`, so a page in `proposals/` must carry
`type: proposal` and rule 2 enforces it for free. That is the shape to copy: a category that needs
a new list somewhere is a category that will be forgotten in one of the lists.

Categories appear about once a year. Two in one sprint would have been a warning; this is the
second in this vault's life, and if a third seems needed soon, the thing being classified is
probably a tag.

When a tracker is installed, what has to be revisited is [[the-brief-has-no-active-tasks-section]]
— the brief quoting its output verbatim — and **not this page**. A tracker arriving is not an
argument for a `tasks/` folder; it is the argument against one.
