---
title: "`archive/` is dated by session and holds everything that left the working set that day"
type: decision
status: archived
authority: archive-scope
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
tags: [vault, process]
---

# Decided 2026-08-16: one folder, dated by session, and `raw/` becomes an inbox

**`archive/<session date>/` holds everything that left the working set on that day** — the journal,
its `.coverage.tsv` sidecar, the specs and plans of that session, **and the wiki pages retired that
day**, dated by the day they were retired.

**`raw/` becomes an inbox that is empty between sessions.** That is the owner's stated want: the
uncompiled set becomes visible **by looking** rather than by running `vault-coverage.sh` over every
file. The want, and the wall it hit, are [[moving-raw-into-a-dated-archive]]; this is the decision
that answers it.

**Dated by session**, not by sprint and not by the date of compilation. Batching separates those
three dates, and the boundary worth reading is the day's.

## Rejected: a separate `sessions/` folder beside `archive/`

It would keep `archive/` single-meaning — only retired pages — at the cost of the one entry point
for a search by date. **The owner chose the single entry point**, and the cost is paid down by
dating the retired pages too, so the folder means one thing again: *everything that left the
working set on that day.*

A side effect worth naming: this **retires stale claim #3 by making it inapplicable** rather than
by editing it. The vault's own `CLAUDE.md` describes `archive/` as holding the handoffs of closed
sprints, and they never moved there ([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

## What it obliges

- **One migration wave, not two.** 115 of 124 pages cite `raw/` in `sources:` and 13 cite a spec
  under `docs/superpowers/`; both are the same job — a mechanical rewrite over `sources:`, where
  the detector is complete, plus a read of the prose mentions, where no detector exists
  ([[a-rewriter-must-be-paired-with-a-detector]], [[raw-holds-testimony-and-artefacts-are-frozen]]).
- **Filenames already carry their dates**, so every target folder is derivable without a judgement.
- Nothing may hard-code the vault's directory name on the way through ([[the-vault-directory]]).
- **Nothing of this is built**, and the two questions the proposal left open — what "dated" means,
  and whether `raw/` gains internal structure first — are answered and unanswered respectively
  ([[moving-raw-into-a-dated-archive]], [[structure-work-agreed-and-not-executed]]).

## The day gains a level — 2026-08-19

**This page settled `archive/<session date>/` and left the day flat. The owner refined it**:
`archive/<date>/<session>/`, a folder per session inside the date, with the files laid out as they
lie in `raw/` and the session folder named from the journal's own filename
([[the-archive-gains-a-folder-per-session-inside-the-date]]).

**The occasion is that a day holds several sessions** — three already on 2026-08-19 — which is
exactly the property the flat shape could not express. It is a refinement rather than a reversal:
*dated by session* is unchanged, and so is the single entry point for a search by date.

**Two things this page says are confirmed rather than moved.** Filenames already carry their dates,
so every target folder is derivable without a judgement — and now so is every session folder,
because the journal's filename carries a slug unique to the session. And nothing hard-codes the
vault's directory name on the way through ([[the-vault-directory]]).

**How it is executed is a separate ruling**, and it is a script rather than a hand
([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]],
[[emptying-raw-by-a-script-that-moves-and-rewrites-its-citations]]). **The order is fixed too**:
`raw/` gains its internal structure before the move
([[raw-gains-its-internal-structure-before-the-move]]), which closes the second of the two questions
this page reported as unanswered.

## A retirement now has a fourth step, and nothing in the corpus said so — 2026-08-22

**The supersession procedure is three steps**: write the successor with `supersedes:`, set the old
page to `status: deprecated` with `superseded_by:`, and move it into `archive/`. **Since 2026-08-21
there is a fourth, and it is unwritten anywhere: remove the retired page's slug from
`authority.md`.**

**It is not optional and it is not cosmetic.** `authority:` became required outside `wiki/rules/` on
2026-08-21, and `bash scripts/vault-authority.sh --check` compares the register against the tree in
**both** directions ([[authority-becomes-the-index-and-is-required-outside-rules]]). A slug that left
`wiki/` with its page leaves a register row no page carries, and the gate reddens on it — which is
the check working, not a defect.

**The failure mode is the ordering.** The move is the last of the three steps, so the register goes
stale at exactly the moment the retirement looks finished, and the next thing that happens is a red
gate on a run the retirer believes was clean. **It was met on 2026-08-22**, retiring
`advisory-is-the-default-for-a-hook`: the row for `hook-blocking-default` had to be taken out of the
family *the hooks that stand around a session* before the tree was green again.

**The deletion is the repair the tool's own header prescribes**, and it is the one removal this
store's *nothing is ever deleted* clause does not reach: what is taken out is a register row, and the
page it named is intact in `archive/` with every word it asserted
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**Stated here rather than added to the procedure.** The procedure lives in the vault's own
`CLAUDE.md`, which the gate reads as its own input and which is the session's to edit, not the
librarian's ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]],
[[hand-edits-of-the-wiki-are-a-recorded-divergence]]). **So this is a report of a gap and an
instruction to whoever edits that file next**, and until then the fourth step is written down here
and nowhere else.

## The fourth step is now decided rather than reported — 2026-08-22

**The section above says the fourth step is *"written down here and nowhere else"*.** It was ruled by
the owner later the same day, with a rejected alternative of its own, and it has a page:
[[retiring-a-page-removes-its-slug-from-the-authority-register]].

**What moved is its standing, not its content.** Removing the retired page's slug from `authority.md`
was a gap the librarian had met inside a red gate; it is now an obligation with a date, and the
alternative he turned down was teaching `scripts/vault-archive.sh` to edit the register — which would
give a one-writer file a second writer ([[the-librarian-writes-unattended]]).

**The paragraph above is not edited.** It was true when it was written, and the sentence that a
retirement met the gap before anybody had written it down is the evidence for the ruling
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

# The folder is history, not a record of replacement — 2026-08-26

> **owner:** «Архив - это не только то, что заменили. Это история всех страниц»

**A page in `archive/` is not thereby outdated**, and a live page citing one is legal behaviour. The
folder is where inactive pages go, whatever made them inactive.

**This corrects a narrower reading a session had been reasoning from for two rounds** — that
`archive/` holds what was superseded — and several of that session's conclusions rested on it. It is
also what the refusal of a live-to-archive citation advisory rests on
([[the-live-to-archive-citation-advisory-is-refused-in-full]]).

**It does not contradict this page's opening**, which already said *everything that left the working
set on that day*. What it strikes is the inference, made elsewhere, that leaving the working set
means having been replaced.

**Two consequences are already decided against it.** A lesson leaves for `archive/` when a page
outside `lessons/` cites it — nothing about that page is false when it moves
([[the-lessons-cycle-is-the-owners-and-a-lesson-leaves-when-a-page-outside-lessons-cites-it]]) — and
the archiver writes `status: archived` on what it moves, a value that is neither `deprecated` nor
`implemented` ([[the-archiver-sets-status-archived-and-the-value-enters-the-schema-first]]).

**Measured the same day: `archive/` holds 50 pages — 38 `deprecated` and 12 with no status**, the
latter being journals nothing cites by slug. So today the wide reading and the narrow one still
select nearly the same set; **they diverge the first time the lessons sweep runs.**
