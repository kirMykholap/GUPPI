---
title: "Moving `raw/` into a dated `archive/`, and the path rewriter it is blocked on"
type: proposal
status: current
authority: raw-archive-migration
basis: human
sprint: S1
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md"]
decided_by: [[structure-work-agreed-and-not-executed]]
tags: [vault, process]
---

# The want, and the wall

**The owner wants compiled sources out of `raw/` and into a dated `archive/`.** `raw/` would then
hold what has not been compiled yet, which makes the uncompiled set visible by looking rather than
by running `vault-coverage.sh` over every file.

**It is blocked on a path rewriter.** Measured 2026-08-16: **115 of 124 pages cite `raw/` in
`sources:`.** Moving the directory turns rule 5 of `vault-check.sh` red on all 115 at once — the
same arithmetic that stopped handoffs being moved on sprint close
([[a-sprint-closes-on-its-goal]], and the `archive/` claim in the vault's own `CLAUDE.md` that has
been stale ever since).

**Nothing here is decided.**

## The cheaper shape, agreed the same day

Split the work in two, and let the ordinary flow carry most of it:

1. **The ingest that compiles a source moves it**, and fixes the citations it has just written —
   they are its own output, in the same dispatch, with the gate run afterwards.
2. **One migration pass** for the 115 pages that already exist.

That converts an all-at-once migration into a one-off backlog plus a per-ingest habit, and the
per-ingest half needs no rewriter at all.

## What it would oblige

- **`/ingest` gains a step**, which is a skill file the librarian does not write
  ([[the-audits-findings-are-owed-to-the-owner]], finding 6).
- **The one migration pass needs the pairing** that [[a-rewriter-must-be-paired-with-a-detector]]
  names: `sources:` is where the detector is complete, so a mechanical rewrite there is safe and
  its misses are caught by the next `vault-check.sh` run. Prose mentions of `raw/` are not covered
  by any detector and would have to be read.
- **Nothing may hard-code the vault's directory name** on the way through
  ([[the-vault-directory]]).

## What is open

- **What "dated" means** — by source date, by sprint, or by the date of compilation. The sprint
  answer is the one that would let a closed sprint's journals move as a set, and it is also the one
  that was already tried and abandoned.
- **Whether `raw/` gains internal structure first** (`plans/`, `specs/`, `notes/`), which is agreed
  as nearly free and also not done ([[structure-work-agreed-and-not-executed]]). Doing that before
  the move would make the rewriter run twice.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

## Decided 2026-08-16, later the same day — and still not built

The two open questions above are now answered, by the owner, in the second session of that day:
[[archive-is-dated-by-session-and-holds-what-left-the-working-set]].

- **"Dated" means by session date** — not by sprint and not by the date of compilation. Batching
  separates those three, and the boundary worth reading is the day's.
- **The destination is `archive/<session date>/`, not a separate `sessions/` folder.** The owner
  chose one entry point for a search by date over keeping `archive/` single-meaning, and the cost is
  paid down by dating the retired pages too.
- **It carries more than the journal**: the sidecar, and the specs and plans of that session, which
  is a second decision — [[raw-holds-testimony-and-artefacts-are-frozen]].
- **The migration is one wave, not two.** The 115 pages citing `raw/` and the 13 citing a spec under
  `docs/superpowers/` are the same job, and filenames already carry their dates, so every target
  folder is derivable without a judgement.

**The cheaper shape above survives**, and so does everything under *what it would oblige*: the
rewriter still does not exist, and the second open question — whether `raw/` gains internal
structure first — is still open ([[structure-work-agreed-and-not-executed]]).

**This page stays `current` because nothing is built.** A proposal is retired when it is built or
refused, not when it is decided ([[proposals-are-a-folder-not-a-status]]).

## Re-measured 2026-08-17 at `b6fc6d8`: the cost grew with the corpus

**150 of 165 pages in `wiki/` name `raw/handoffs`, and 23 of those mentions sit in prose** rather
than in `sources:`.

The figure above — 115 of 124 — was true when it was written; the corpus grew and the ratio grew
with it. **The prose figure is the one that matters**, because a rewriter is complete for `sources:`
and blind in prose ([[a-rewriter-must-be-paired-with-a-detector]]), so those 23 are the ones a
migration would leave pointing at a directory that no longer exists — silently, since nothing checks
a path written in a sentence.

**Recorded as a slice of its own** on [[what-the-harness-build-waits-on]], with the consequence
stated: the number is monotonic, so every session that does not do this makes it larger. Quoted with
its commit, because a number carried across an edit drifts
([[a-stated-count-drifts-from-the-list-it-heads]]).

## Both of the questions this page left open are now closed — 2026-08-19

**The one still standing was *whether `raw/` gains internal structure first*.** It does
([[raw-gains-its-internal-structure-before-the-move]]), for the reason this page itself gave —
doing it after would make the rewriter run twice.

**And the shape gained a level**: `archive/<date>/<session>/`, files laid out as they lie in `raw/`,
the session folder named from the journal's filename
([[the-archive-gains-a-folder-per-session-inside-the-date]]).

**The cheaper shape this page proposed is now the decided one**: the ingest that compiles a source
moves it and fixes the citations it has just written, and the mechanical half is a **script the
ingest calls** rather than an agent's hands
([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]]). The design of that script is
[[emptying-raw-by-a-script-that-moves-and-rewrites-its-citations]].

**This page stays `current` because nothing is built** — no structure, no script, no move
([[proposals-are-a-folder-not-a-status]]). What is left open is not design: whether the trigger is a
hook, whether the check is a hook, or both.

**Still open too, and not this page's**: the prose half cannot be automated
([[sed-cannot-tell-an-address-from-a-quotation]]), and the nearest mechanical help is an advisory
detector that has been prototyped and measured and not built
([[a-path-detector-for-prose-references]]).
