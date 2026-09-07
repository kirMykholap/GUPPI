---
title: "Reconciling entities/ against the decision register — the one of the owner's lint checks that was never made mechanical, asked for once and built by nothing"
type: proposal
status: current
authority: entity-decision-reconciliation
basis: human
sprint: S1
created: 2026-08-15
sources: ["raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md", ".claude/skills/vault-lint/SKILL.md"]
decided_by: [[the-audits-findings-are-owed-to-the-owner]]
tags: [vault, architecture]
---

# The ask, in the owner's words

From his instructions note of 2026-08-13, under `/lint`:

> «Сверить текущую архитектуру в `wiki/entities/` с реестром `wiki/decisions/`.»

Of the three checks that note lists for `/lint`, **two were made mechanical instead** and now run
on every write — orphans, and the `status:` vocabulary ([[vault-scripts]]). **This is the third,
and it exists in no skill and in no script.** It has lived since then as a clause inside
[[lint-waits-for-an-open-sprint]] and a table row inside
[[the-owners-instructions-note-and-what-was-built-from-it]]; this page is that clause given a page,
so that the design stops being a footnote to a deferral.

*(The title read "Reconciling entities/ against the decision register — the owner's third lint
check, asked for once and built by nothing" until 2026-08-18, and the paragraph above is where the
position is resolved: two of that note's checks were made mechanical, and this is the one that was
not. **A fourth check would have made the title stale** — an ordinal is a position in a list that
grows, and it drifts as the entries ahead of it move
([[a-rule-leaves-the-numbered-list-and-carries-no-ordinal]]). This page never carried a `quantity:`
line, because rule 10's word list does not read ordinals and so nothing flagged it: the owner ruled
them in on 2026-08-18 ([[ordinals-count-and-first-does-not]]), in the clean-up that also rejected
the field ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), and the word list is
tightened only after the corpus is repaired. The title now names the check by what became of it
rather than by its position ([[a-title-names-what-is-counted-instead-of-counting-it]]), and that is
a correction in place rather than a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).)*

**Nothing here is decided.**

## What it would actually be

Not a link check. Both halves of it are semantic:

- **`entities/` says what exists** — modules, tools, external systems, and what each is like.
- **`decisions/` says what we chose** and, in the field that matters here, **what it obliges**.

The reconciliation is the pair of questions those two folders can be asked about each other:

1. **Does an obligation have a subject?** A decision that obliges something about a module the
   `entities/` set does not describe is either a decision about vapour or an entity page nobody
   wrote. Both are findings.
2. **Does a subject contradict an obligation?** An entity page describing behaviour that a
   `decisions/` page forbids is the interesting half, and it is the one that catches drift rather
   than absence.

## Why no script can do it, and what would run it instead

`vault-check.sh` reads frontmatter and link structure; **a page's claim is outside its vocabulary
entirely**, and that limitation is stated on [[vault-scripts]] and again on
[[proposals-are-a-folder-not-a-status]]. A reconciliation compares *meanings*, so the runner is a
librarian dispatch reading two folders — which is what `/vault-lint` already is.

The size that makes it plausible: **15 pages in `entities/` and 44 in `decisions/`** at `14d3d51`.
That is a comparison a model performs in one pass, and it is the same argument
[[dynamic-tag-classification-by-a-skill]] makes for the tags — the classifier is already paid for.

## What is open

- **Which direction is authoritative when they disagree.** `basis` ranks the pages
  (`human` over `code` over `inference`), but the honest answer may be that a mismatch is a
  contradiction to mark rather than a defect to fix — and the librarian may not resolve one
  ([[the-librarian-writes-unattended]]).
- **Whether "the current architecture" means `entities/` at all.** In this vault the layering
  lives in [[architectural-boundaries]], which is a `concepts/` page, and the module map is
  uncompiled negative space with no source in `raw/` to compile from. The note's `entities/` and
  this store's `entities/` may not be the same folder.
- **Its cadence.** Item of `/vault-lint`, once per sprint, is the note's answer; an audit costs
  about what a large ingest does ([[agent-round-trip-cost]]).

## What it would oblige

`/vault-lint`'s item list grows by one, which means `.claude/skills/vault-lint/SKILL.md` is edited
— a file the librarian does not write ([[the-audits-findings-are-owed-to-the-owner]], finding
6, which names that same file for a different reason). And the first run would produce findings
against pages nobody touched that sprint, which is the judgement half of a lint and the owner's to
apply.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

## Deferred again on 2026-08-16, with the gap counted

`entities/` holds **fifteen pages and none of them is about the application** — no module map, no
CLI, no data model. The reconciliation this page designs compares `entities/` against `decisions/`,
and one of the two folders is empty of the product it is supposed to describe, so a first run would
report the absence of nearly everything rather than a drift.

**The obstacle is not effort, it is that those pages have no source in `raw/` to be compiled from**
— negative space, not an unfinished ingest ([[an-intent-note-compiled-as-testimony-describes-things-nobody-built]]).
Writing them from the code would make the librarian the author of what it then reconciles, which is
the one thing this design cannot afford.

Row and consequence: [[structure-work-agreed-and-not-executed]].
