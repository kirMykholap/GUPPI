---
title: "The archive sweep that walks each folder and collects its refusals"
type: proposal
status: implemented
authority: archive-sweep-design
basis: human
sprint: S3
created: 2026-08-28
decided_by: [[the-archive-sweep-continues-past-a-refused-move-and-collects-its-refusals]]
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", "scripts/vault-archive.sh", "archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md"]
tags: [vault, harness, process]
---

> [!NOTE] BUILT 2026-08-29
> `scripts/vault-archive.sh --sweep <date> <session>` exists and its first run moved 239 pages. What
> exists now is recorded on [[vault-archive-sh]] and
> [[the-sweep-is-a-mode-of-the-archiver-and-inherits-its-refusals]]; the order it ran in is
> [[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]]. The design below is kept
> as written. `implemented` opens a state rather than naming a place: this page stays in `wiki/` while
> it is tested for a live page pointing at it, and moves only once it passes.

# What it would be

**A sweep mode inside `scripts/vault-archive.sh`**, run at the lint stage, that walks a folder,
applies that folder's archival criterion, writes `status: archived` on each page it moves, and moves
it into `archive/<date>/<session>/pages/`
([[the-archive-mover-is-a-sweep-inside-the-archive-script-at-the-lint-stage]]).

**It does not stop at a refusal.** It collects them, prints them as a list at the end, and exits
non-zero if the list is not empty — which is what makes the `archived` value necessary in every
folder's schema, because a page can be left in `wiki/` wearing the mark of a move that did not
finish ([[a-status-value-is-either-an-address-or-a-stage-and-the-gate-treats-them-oppositely]]).

# The criteria it would apply, each already decided

| folder | when a page leaves |
|---|---|
| `lessons/` | a page outside `lessons/` cites it ([[the-lessons-cycle-is-the-owners-and-a-lesson-leaves-when-a-page-outside-lessons-cites-it]]) |
| `decisions/` | `binding: divergence`, or a live page names it in `decided_by:` ([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]], [[a-decisions-archival-condition-is-read-off-its-binding]]) |
| `proposals/` | `status: implemented` or `status: refused` ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]], [[a-refused-proposal-is-archived-and-takes-status-refused]]) |
| `entities/`, `concepts/` | **nothing** — deferred ([[entities-and-concepts-get-no-archival-criterion-today]]) |

# What the tree is today

**`scripts/vault-archive.sh` has no sweep mode.** It takes an explicit file list, lines 38–41 and
117. Its precondition for `kind=pages`, lines 145–161, requires a live page under `wiki/` naming the
slug — which under a `decided_by:` criterion is identically true and can never refuse, so the sweep
brings its own selection and inherits a guard that will not fire
([[vault-archive-sh]]).

# What is open

**Which refusals are worth continuing past and which should stop the run.** The ruling says the
sweep continues; it does not say whether a destination collision is the same class of event as a
missing citer.

**Whether the mark is written before or after the move.** The gate reads `wiki/` alone, so the order
decides which of the two states a half-finished move leaves behind
([[the-gates-frontmatter-pass-reads-wiki-alone-and-archive-is-validated-by-no-schema]]).

**And what it does about the pages it would move first.** The `lessons/` criterion selected 144 of
157 on 2026-08-26; nobody has read that list.
