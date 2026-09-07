---
title: "`log.md` is outside the link set the check reads, so a rename can strand it silently"
type: concept
status: current
authority: log-link-blindness
basis: measurement
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-check.sh"]
tags: [vault, harness, retrieval]
---

# The set, and what falls outside it

Rules 4 and 5 of `vault-check.sh` build one set of linked page names and ask two questions of it —
does every link resolve, and is any page unreachable. **The set is built from `wiki/`, `archive/`,
`index.md`, `tags.md` and `sprint.md`.** `log.md` is not in it.

**Demonstrated rather than read off the source.** In a throwaway worktree a deliberately incomplete
rename left **13 dangling `[[wikilinks]]` in `log.md`, and the gate exited 0 saying nothing**.

**`raw/` is outside the set too, and correctly so.** A journal naming an old slug is history
recording what was true at the time, and `raw/` is immutable — a link check over it could only be
satisfied by editing a file the schema forbids editing, or by writing a page nobody wanted
([[raw-holds-testimony-and-artefacts-are-frozen]]).

**`log.md` is a different case.** It is the librarian's own register, it is written after every
ingest, and it is full of `[[wikilinks]]` that a reader is expected to follow. It is current text,
not testimony, and nothing checks it.

# What it costs, and when

**Only a rename can produce it.** A link is written correctly or it is not; the way `log.md` goes
wrong is that an address moves and the sweep stops at the edge of the checked set
([[a-page-rename-is-sed-and-verify]]). That makes this a property of the rename work rather than a
standing defect, which is why it is filed with that work
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).

**Two repairs, and neither is chosen here**: add `log.md` to the set rules 4 and 5 read, or grep the
old slug to zero as a mandatory step of every rename. The first makes the gate see it; the second
makes the procedure see it. Both are work items against `scripts/vault-check.sh`.

**The general shape is one this store has met before**: a check whose denominator is a set, and a
real member of the world that is not in the set ([[a-denominator-is-walked-off-the-input-list]],
[[the-governed-set-is-swept-and-markdown-by-property]]).

# The rename it predicted happened on 2026-08-19, and the numbers are worse than the shape suggested

**Fourteen references in `log.md` had to be swept by hand** across sixteen renames, against 148 inside
the checked set ([[a-page-rename-is-sed-and-verify]]). Nothing printed for them, exactly as this page
says.

**And the linked form is the minority there.** Counted before the sweep: **28 bare slug mentions
against 14 wikilinks** in `log.md`. So the first of the two repairs named above — *add `log.md` to the
set rules 4 and 5 read* — **would have caught a third of the problem**, because rules 4 and 5 read
wikilinks and a log entry names a page as a subject far more often than it links to it
([[a-bare-slug-mention-is-an-inbound-link-that-no-wikilink-counter-sees]]).

**That reprices the two repairs against each other.** The second — *grep the old slug to zero as a
mandatory step of every rename* — is the one that covers both forms, and it is the one that was
actually run. The first is still worth having, and it is no longer the more complete of the two.

## It is now outside by decision as well as by mechanism — 2026-08-20

**owner: `log.md` is never rewritten, at all.**

> «Лог — это то, что было и как это записали. Мы могли неправильно записать, окей, бывает.»

Until this ruling, the log was outside a rewrite by an accident of the gate's rules, and the gap was
paid for by hand sweeps at every rename ([[a-page-rename-is-sed-and-verify]]). **It is now outside
by decision**, and the consequence is the opposite of what the hand sweeps assumed: **the old paths
in `log.md` are correct as written rather than stale**
([[archive-is-rewritten-by-a-path-move-and-log-md-never-is]]).

**`scripts/vault-archive.sh` implements it** — it rewrites `wiki/` and `archive/`, and never this
file ([[vault-archive-sh]]). Verified on its first run: `log.md` was not touched at all.

**What this page still records unchanged is the mechanical fact**, and it now matters for a second
reason: nothing will ever notice if a per-session rotation of this file loses a day
([[log-md-rotates-per-session-into-the-dated-archive]]).

# A second file is outside the sweep, and it was never counted: the coverage sidecars — 2026-08-21

**Measured by running `bash scripts/vault-coverage.sh` over every source in `raw/`**, which no
ritual called until it became step 11 of the ingest
([[the-tag-density-advisories-run-at-every-ingest]]):

| | |
|---|---|
| sources reporting `verdicts are not verdicts` | 12 of 22 |
| bad verdicts in total | 65 |
| distinct page names they point at | 16 |
| of those names, how many carry a quantity | **all of them** |

**So they are not typos: they are the renames.** `three-artefacts-three-owners`,
`one-librarian-two-entry-points`, `two-staleness-checks-at-two-times`,
`the-audits-six-findings-are-owed-to-the-owner`, `the-three-tags-are-not-split-and-five-advisories-stand`
— every one is a filename retired under the no-quantity rule on 2026-08-18 and 2026-08-19
([[the-title-rule-extends-to-filenames]], [[a-page-rename-is-sed-and-verify]]).

**A `.coverage.tsv` is the third thing outside the checked set, after `log.md` and `raw/`** — and it
is the case this page's own reasoning does not cover. It is **not** immutable testimony the way a
journal is: it is the librarian's own accounting, written after the source, and a verdict pointing
at a page that no longer exists is a broken index rather than a record of what was true.

**It fails in the direction this store cares about**: `vault-coverage.sh` reports it as
`BAD VERDICT ... does not exist in the wiki`, so the reading is *this ingest was never finished*
when what happened is *the page it finished into was renamed*. **The journal of 2026-08-21 reported
one of the twelve** and read it as unfinished work ([[an-instrument-that-fails-towards-nothing-to-do]]).

**Not repaired here, and the reason is the one this page already gives.** The second repair —
grep the old slug to zero as a mandatory step of every rename — is the one that covers this, and it
covers it only for renames that have not happened yet. The 65 standing lines are a sweep, and a
sweep is scheduled rather than folded into an ingest
([[order-a-split-change-against-its-failure-not-for-convenience]],
[[a-rewriter-must-be-paired-with-a-detector]]). **Whether they are swept at all is the owner's**:
these are not links a reader follows, and the argument for leaving them is the one he gave about
`log.md` — a record of how it was written down at the time.

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`, and from the step-11 run at that ingest.)*

# The sidecar sweep landed — 2026-08-21

**The stale slugs the section above left standing were swept in `340ccb0`**, from a map built out of
git history rather than by hand. The commit reports **66 across twelve `.coverage.tsv` files**
against the **65** counted at the ingest that found them; the earlier figure is left as it was read
([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

**The coverage loop that `/ingest` now runs went from twelve noisy sources to none**, so the
instrument stopped reading *unfinished ingest* where the truth was *renamed page*
([[an-instrument-that-fails-towards-nothing-to-do]]).

**What is unchanged is the property this page is about.** A sidecar is still outside the rename
sweep, exactly as `log.md` is; the sweep repaired the standing lines and not the blindness that
produced them ([[a-rewriter-must-be-paired-with-a-detector]], [[a-page-rename-is-sed-and-verify]]).

*(Compiled from the feedback file drained into `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`, and verified against `340ccb0` at that ingest.)*
