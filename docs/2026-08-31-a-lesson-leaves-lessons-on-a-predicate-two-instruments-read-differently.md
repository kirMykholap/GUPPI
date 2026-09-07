# A lesson leaves `wiki/lessons/` on a predicate two instruments read differently

**Draft proposal, prepared by the lessons agent on 2026-08-31 from
`raw/handoffs/2026-08-31-the-families-become-rules.md` and from the tree as it stands.
Not written into the vault. The librarian decides whether it becomes a `wiki/proposals/` page and
what its `authority:` is.**

This is the retirement proposal for `wiki/lessons/`, and its first finding is that the folder
already has a retirement mechanism, that a second instrument reports on the same folder, and that
the two disagree about five pages.

## What is measured, today, at the tree as it stands

**`wiki/lessons/` holds 28 live pages.**

**`scripts/vault-archive.sh --sweep` would take 16 of them.** Its `lessons/` arm is
`slugs_cited_outside lessons` at line 366: a fixed-string `grep` for the filename across every
`wiki/` page that is not in `lessons/`. Any page of any type mentioning the slug anywhere — body,
`Links:`, `sources:` — selects it.

**`scripts/lessons-queue.py` says 17 are in the queue and 1 has landed.** Its predicate is
narrower and deliberately so: `CITED` means a **rule, a proposal or a decision** names the slug;
`LANDED` means a `rules/` page names it or a proposal naming it carries `status: implemented`.

**Five pages satisfy the first and fail the second:**

- `a-fixture-pinned-to-the-end-of-a-file-expires-when-a-block-is-appended-below-it`
- `an-advisory-word-on-a-continuation-line-inflates-the-count-the-brief-reports`
- `backgrounding-a-task-that-reads-standard-input-is-what-hangs-it`
- `grep-q-on-the-right-of-a-pipeline-under-pipefail-inverts-the-test`
- `the-corpus-is-mostly-about-itself-and-the-owner-noticed-before-any-instrument-did`

**Each is cited only by a concept or an entity.** On the next sweep each leaves `wiki/lessons/`
for `archive/`, and the progress number that exists to say whether anything was acted on still
counts every one of them as untouched — from a folder it can no longer see, since the script's own
docstring records that it scans `wiki/` and never `archive/`.

## What it would be

**One predicate, named on one page, read by both instruments.**

The two candidate readings are already written and neither is wrong on its own:

1. **A mention is enough** — the archiver's. It is wide on purpose: the docstring of
   `lessons-queue.py` says the wide reading is what stops a collector re-proposing the same family
   for ever.
2. **A rule, a proposal or a decision must name it** — the queue's, ruled by the owner on
   2026-08-26 as two numbers rather than one, on the ground that *a citation is not an action*.

**The proposal is that reading 2 becomes the archiver's predicate as well**, so that a page leaves
`lessons/` when something that can *act* names it, and not when something that merely *describes*
mentions it.

## What it would take

- **`scripts/vault-archive.sh`, `sweep_candidates()`, the `lessons/` arm at lines 419–428.**
  `slugs_cited_outside lessons` takes a folder filter, or a sibling that restricts the citing set
  to `decisions/`, `proposals/` and `rules/`.
- **One `wiki/decisions/` page** recording that the predicate narrowed and what it rejected, since
  the current wide reading was the owner's on 2026-08-26 and narrowing it is his call, not a
  session's.
- **Nothing in `lessons-queue.py`**, which already holds the narrow reading and would become the
  single definition.

## What is open

- **Which of the two readings the owner wants.** He ruled the wide one for the queue's `CITED`
  number and the narrow one for `LANDED`, in the same conversation. Which of the two governs
  *departure from the folder* has never been put to him, and this draft does not assume it.
- **Whether the answer is instead that `lessons/` should not be swept at all.** The folder is the
  smallest in `wiki/`, its whole content is failure classes, and `archive/` is read by nothing —
  not `/pre-task`, not `vault-catalogue.sh`, not the gate. A lesson moved to `archive/` has left
  the store rather than been filed in it, and this journal already defers the
  `vault-catalogue.sh` blind spot for the 129 decisions moved today.
- **What the five pages do in the meantime.** They are the population the decision is about, and
  a sweep run before it is taken decides the question by accident.
- **Whether `LANDED: 1` is a defect of the corpus or of the predicate.** One of 28 is either an
  honest reading that the loop does not close, or an artefact of `implemented` not being marked.
  Nobody has separated the two.

## What it would oblige

- **A reading of both numbers on the same day, recorded together.** They are only comparable
  when taken over one tree, and the gap between them is the quantity this proposal exists to close.
- **`scripts/vault-check-selftest.sh` gains a case for the narrowed arm** if it narrows —
  `wiki/rules/every-rule-in-wiki-rules-owes-a-mechanical-instrument` applies, and the archiver's
  refusals already carry cases.
- **The `authority.md` row lands in the same pass as any page this produces.** Writing a page
  into `wiki/` with an unregistered slug reddens rule 13, `lock-the-librarian.ps1` reads a red gate
  as a refusal to dispatch, and the librarian is the only writer of the register
  (`one-page-written-into-the-wiki-reaches-the-register-deadlock`,
  `the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages`).

## What it would retire

**Nothing in `wiki/lessons/`.** This proposal is about how the folder empties, not about what it
holds, and it is named first precisely so that the four drafts below are not read as the only way a
lesson leaves.

**What it would retire is a false reading**: that `lessons/` is drained when the sweep takes a page.
