---
title: "A check for the conceptual pages that are missing — the only one of the owner's lint checks that no grep could ever answer"
type: proposal
status: current
authority: missing-page-detection
basis: human
sprint: S1
created: 2026-08-15
sources: ["raw/notes/2026-08-13-owners-note-second-brain-info.md", "archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md", ".claude/skills/vault-lint/SKILL.md"]
decided_by: [[the-audits-findings-are-owed-to-the-owner]]
tags: [vault, retrieval]
---

# The ask, in the owner's words

From his method note of 2026-08-13, in the list of what `/lint` should find:

> «Битые ссылки и отсутствие необходимых концептуальных страниц.»

Broken links are rule 4 of `vault-check.sh` and run on every write. **The second half of that
sentence is built by nothing.** It is a *different* item from the reconciliation the other note
asks for ([[reconciling-entities-against-the-decision-register]]), so the two notes together ask
for five lint checks of which three exist
([[lint-waits-for-an-open-sprint]], [[the-owners-method-note-and-what-was-built-from-it]]).

*(The title read "A check for the conceptual pages that are missing — the only one of the five
that no grep could ever answer" until 2026-08-18, and the sentence above names the set it was
counting: the lint checks the owner's notes ask for. **Five was a closed set that cannot grow** —
the notes were written on 2026-08-13 and nothing can be added to them now. That reasoning stood in a
`quantity:` line until the field was rejected and the rule made unconditional over titles and
filenames alike ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]): an argument
that a number cannot drift is no longer a way to keep one in a title. The title now names the set
instead of counting it ([[a-title-names-what-is-counted-instead-of-counting-it]]), and that is a
correction in place rather than a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).)*

**Nothing here is decided.**

## Why it is the hard one

**A page that ought to exist leaves no trace to search for.** Every other check in this store works
by finding something and judging it: an orphan is a page, a dead tag is a line in the dictionary, a
stale count is a number beside a list. This one has to find an *absence*, and absence has no
address. It is the only one of the five that no `grep` could answer even in principle.

The store has already paid for this gap twice, both times caught by a human reading rather than by
any check:

- **the schema tag.** A whole-branch review found `rg -il "колонк|таблиц|миграц|схем"` returning
  nothing at all over the wiki — the corpus held schema knowledge and had no way in for a question
  about it. The fix was a tag, not a page, but the diagnosis was the same one.
- **the module map, the CLI and the data model.** Named as gaps on 2026-08-13, still uncompiled,
  and the 2026-08-15 finding sharpens it: they **have no source in `raw/` to be compiled from**, so
  no coverage run will ever report them missing. `INGEST COMPLETE` on all six sources is compatible
  with the layout of `src/jobhunt/` being written down nowhere ([[vault-scripts]]).

## Three shapes it could take, in rising cost

1. **Dangling-subject detection.** A subject named in *N* pages' prose that has no page of its own.
   Cheap, mechanical, and noisy — every common noun qualifies.
2. **Coverage against the tree.** Enumerate what exists in the repository — modules, scripts,
   tables, routes — and ask which have no page. This is the one that would have caught the module
   map, and it needs a definition of what deserves a page, which nothing here has.
3. **A librarian reading for holes**, which is what `/vault-lint` already is: given the categories
   and the corpus, name the concepts a reader would expect to find and does not. Judgement, one
   dispatch, no false-positive floor.

Shape 3 is the one the note's cadence implies and the only one that needs no new machinery.

## What is open

- **What "necessary" means.** Without a definition, shape 3 produces an unbounded list every time
  it runs — and an advisory that fires every run and cannot be acted on is one you learn not to
  read, which is stated inside `vault-check.sh` itself.
- **Whether the output is pages or a backlog.** A missing page is a `proposals/` entry only if
  someone designed it; otherwise it is known negative space, and this store has recorded such space
  in prose rather than as pages.
- **Whether it can distinguish "missing" from "deliberately not written".** The vault refuses a
  `tasks/` folder on purpose ([[the-wiki-has-five-folders-and-tasks-is-not-one]]); a check that
  cannot tell a refusal from a hole will report both for ever.

## What it would oblige

An item added to `.claude/skills/vault-lint/SKILL.md`, which the librarian does not write; and, if
shape 2 is chosen, a list of what in the repository deserves a page — a second register, which is
the thing [[the-index-is-a-map-not-a-catalogue]] argues against and
[[the-catalogue-is-generated-not-maintained]] shows is acceptable only when it is generated.
