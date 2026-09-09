---
title: "The wiki has four folders and tasks/ is not one of them — task status belongs to the tracker"
type: decision
status: deprecated
authority: wiki-categories
basis: code
sprint: S1
decided: 2026-08-13
created: 2026-08-14
sources: ["raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md", "docs/superpowers/specs/2026-08-13-second-brain-design.md", "scripts/vault-check.sh"]
tags: [vault, process]
superseded_by: [[the-wiki-has-five-folders-and-tasks-is-not-one]]
---

# Four folders, and the one that was asked for and not built

> [!WARNING] DEPRECATED 2026-08-15
> **The set is five, not four.** `wiki/proposals/` was added on 2026-08-15
> ([[proposals-are-a-folder-not-a-status]]), which makes the title and the first line of this page
> wrong — so it is retired rather than edited. The successor is
> [[the-wiki-has-five-folders-and-tasks-is-not-one]], and it carries **both reasons below
> unchanged**: `tasks/` is still refused, on the same two grounds. What it adds is the boundary
> this page could not have had — why the second reason, *nothing would write it*, does not also
> refuse `proposals/`: a proposal is compiled by the librarian from a source in `raw/`, like every
> other page here, and a task list is not compiled from anything. Kept because "what did the folder
> set look like before the fifth, and what was the argument then" is a real question.

`wiki/decisions/`, `wiki/concepts/`, `wiki/entities/`, `wiki/lessons/`. The set is not a
convention anybody may extend in passing: `vault-check.sh` rule 1 names all four and fails if one
is missing, and rule 2 fails a page whose `type:` disagrees with the folder it sits in.

**Rejected: `wiki/tasks/`**, which the owner's instructions note of 2026-08-13 asks for by name —
«статус и детализация задач текущего и прошлых спринтов»
([[the-owners-instructions-note-and-what-was-built-from-it]]). Two reasons, and they are of
different weights:

- **The tracker owns task status; the vault owns what we learned from a task.** That division is
  the owner's own, restated by him on 2026-08-14 when he removed the brief's placeholder section
  ([[the-brief-has-no-active-tasks-section]]). A task list inside the vault would be a second copy
  of something that changes hourly, and it would be the copy people read.
- **Nothing would write it.** The librarian compiles from journals, and a journal's §1 is state —
  the only section that is `journal` wholesale and never becomes a page
  ([[the-handoff-template-maps-onto-the-categories]]). A `tasks/` folder would be filled by hand or
  not at all, and a folder filled by hand in a store written by an agent goes stale in one sprint.

**Also rejected, in the same pass: `invariants/`.** A decision and the rule it produced are one
fact at two moments of its life, and two folders would have filed it twice on day one. That is why
`concepts/` holds invariants that grew from a decision *and* facts nobody chose — PostgreSQL's
`now()` being constant within a transaction was not decided by anyone.

**A second witness arrived on 2026-08-15, and it is on this page's side.** The owner's *other*
note of 2026-08-13 lists the categories as `entities/`, `concepts/`, `decisions/` — **no `tasks/`
at all** — and asks by name for the `concepts/` the instructions note never mentions
([[the-owners-method-note-and-what-was-built-from-it]]). So the folder set that was built is the
one he wrote down twice, minus a folder he wrote down once, plus `lessons/`, which neither note
has. `type: task` likewise appears in one note's enum and `type: concept` in the other's.

## Why this is not marked as a contradiction, while the index is

The note is `human` and this page is `code`, and on those markings alone the note would outrank the
build. It does not, because **the owner spoke again later on the same substance**: the 2026-08-14
decision above states the ownership rule in his own words. The `index.md` row of the same note has
no such later word behind it, which is why that one carries a
`> [!CAUTION] CONTRADICTION` and this one carries an explanation.

*(The last sentence was true from 2026-08-14 to 2026-08-15.)* **The `index.md` row got its later
word too**: the owner resolved that contradiction on 2026-08-15 by having the catalogue generated
([[the-catalogue-is-generated-not-maintained]]), and its block now records a resolution rather than
a standoff. The principle is unchanged and is the point worth keeping — **a marking waits for the
owner to speak again, and it is removed by nobody else.**

## What it obliges

A fifth category is a change to the map, not a page: it means editing `index.md`, the vault's
`CLAUDE.md` and rule 1 of `vault-check.sh` together. Categories appear about once a year; if one
seems needed twice in a sprint, the thing being classified is probably a tag.

When a tracker is installed, what has to be revisited is
[[the-brief-has-no-active-tasks-section]] — the brief quoting its output verbatim — and **not this
page**. A tracker arriving is not an argument for a `tasks/` folder; it is the argument against
one.
