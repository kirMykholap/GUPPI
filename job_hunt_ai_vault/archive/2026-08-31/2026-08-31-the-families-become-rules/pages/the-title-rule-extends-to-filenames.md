---
title: "The no-quantity rule extends to filenames, and the renames wait on the rewriter-and-detector pair"
type: decision
status: archived
authority: filename-quantities
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-check.sh"]
tags: [retrieval, vault, harness]
---

# Decided by the owner on 2026-08-17: the rule covers both

**A filename carrying a measurable quantity is a violation, exactly as a title is**
([[a-title-names-what-is-counted-instead-of-counting-it]]). Rule 10 of `scripts/vault-check.sh` reads
only `title:`, **by design**, and the reasoning written into it is that the filename is the address:
renaming moves something and retitling does not
([[a-title-corrected-in-place-is-not-a-supersession]]). **He decided the rule covers the address too.**

**Rejected: leaving the filename out** on the ground that a stale filename costs nothing because
nobody reads it. In this vault the filename *is* the search surface — retrieval is `ripgrep` plus
links — so a filename that counts is a false claim in the one place a reader greps
([[filenames-carry-no-category-prefix]]).

## Two pieces of work follow, and they are not the same size

| Work | Size | Blocked on |
|---|---|---|
| a verdict in the check for a filename carrying a quantity | **small** — the same predicate rule 10 already applies to `title:`, over a different string | nothing |
| the renames themselves | **large** | the rewriter-and-detector pair: **a filename is what every `[[wikilink]]` resolves to**, and the worst offender carries **23 inbound links** ([[a-rewriter-must-be-paired-with-a-detector]]) |

**At least four filenames carry a count today**, and some of those counts are invariants that ask for
no rename at all — the same distinction the title check refuses to make lexically, for the same reason
([[the-title-check-asks-and-does-not-judge]]).

## The instance that produced it

The brief reported `the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here` as *"still false in its
title"*. Measured at `ed239f2`, that was wrong: the `title:` had already been corrected and carries no
quantity, so rule 10 was silent and correct. **What is stale is the filename**, which rule 10
deliberately does not cover — and the owner's question was *why has the rule fired again*, when it had
not ([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

**So the extension came out of a false alarm about a real defect**, which is worth noting: the brief
was wrong about the mechanism and right about the file.

## What it obliges

- **The verdict goes in before the renames**, or the check goes red on a corpus nobody can legally
  fix — the same ordering argument that put the fifth verdict before the first migration
  ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).
- **A rename is a supersession of the address and nothing else.** The claim does not change, so
  neither the page nor its history does; what changes is every link into it.

# The two halves are separated, and the detector goes first — owner, 2026-08-18

**owner: yes, next session, and separately from the renames.** Only address-moving waits on the
rewriter-and-detector pair; **the detector waits on nothing**
([[a-rewriter-must-be-paired-with-a-detector]]).

**Rule 10 asks rather than judges**, so a flagged filename answers in `quantity:` or waits for its
rename, and **a twelfth is never minted silently** — which is the whole value of landing the check
before the sweep ([[the-title-check-asks-and-does-not-judge]]). Selftest cases are owed with it.

## The measurement that made the ordering urgent

**11 filenames of 259 carry a quantity**, measured 2026-08-18. *("At least four" above was the
figure on 2026-08-17 and is left standing.)* **Nine predate the rule entirely; two were created
2026-08-17**, the day it was extended; **none was minted on 2026-08-18** — the two that git dates
that day were added by `e51d390` at 00:00:38, which is the previous day's ingest.

**So the filenames are where the titles were before they were checked**, and the rule's author is
the party producing the violations ([[knowing-a-rule-is-not-a-mechanism]]).

**The renames are the first customer of the rewriter-and-detector pair**, and that belongs in
`sprint.md` rather than in a brief: it has arrived in two consecutive briefs, and a brief is not a
destination ([[the-growth-signal-is-the-brief]]).

# The check half landed on 2026-08-18, and three things on this page are corrected

**Rule 10 now reads the filename with the predicate it reads the title with** (`2772439`), and it is
an **advisory** rather than a red verdict — the asymmetry is the owner's and is priced on
[[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]. Its output shape is his too
([[the-filename-advisory-prints-one-name-per-line]]). **Six names print**, each a page whose title
had already been repaired.

**Correction, measured: the "23 inbound links" price does not reproduce.** At `c521a10`, over the
link set the check actually reads, the highest inbound count among the six is **20** and the page
the figure was written about carries **14** ([[a-page-rename-is-sed-and-verify]]). The figure is
left standing in the table above as what was believed, and it is not the price of anything.

**Correction: "blocked on the rewriter-and-detector pair" was overpriced.** All six renames, done in
an isolated worktree, took **10.1 seconds including a full gate run** across 51 files, and the gate
returned to exactly its baseline. The detector is complete for the link set; what is genuinely
outside it is `log.md` ([[log-md-is-outside-the-link-set-the-check-reads]]), which is now part of
the rename work rather than a reason to wait.

**Correction: answering in `quantity:` is no longer available.** The owner rejected the field on
2026-08-18 and the rule stands unconditional in both halves
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[the-title-check-asks-and-the-answer-is-a-retitle]]). The seven filenames silent on a declaration
today are silent on a field that is being removed, and the renames are ordered after the corpus
clean-up for that reason.

# Closed 2026-08-19: the renames landed, and no rewriter was ever built

**Every clause on this page about work still to come is finished.** *"The renames are ordered after
the corpus clean-up"* — they were, and in that order: the titles were repaired on 2026-08-18 and the
sixteen addresses underneath them were renamed on 2026-08-19, so the tightening reddened nothing.
*"The seven filenames silent on a declaration"* are silent on a field that no longer exists —
`grep -rc '^quantity:' wiki archive` sums to 0, and rule 10 stopped reading the key on 2026-08-19
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).

**"The renames are the first customer of the rewriter-and-detector pair" is false in both halves.**
The pair was never built. The sweep was `git mv`, one `sed -f` over every reference in `wiki/`,
`archive/`, `index.md`, `tags.md` and `sprint.md`, and a verification pass, with `log.md` swept by
hand ([[a-page-rename-is-sed-and-verify]], [[log-md-is-outside-the-link-set-the-check-reads]]).
**Measured on the sweep so the next one is priced from a reading rather than from a fear**: sixteen
renames moved **148** inbound wikilinks inside the set rules 4 and 5 read, and **14** more in
`log.md`, which is outside it. The `23 inbound links` in the table above was never the price of
anything, and the table is left as written because what a session believed the work would cost is
the reason it waited two days.

**"Six names print" is replaced by the command, not by another number.** That count has been
four, eleven, six and thirteen across three days, each reading correct when it was taken and none of
them still true:

```
bash scripts/vault-check.sh | grep 'filename(s) count'      # empty on 2026-08-19
```

Run beside this sentence it prints nothing, the run exits 0, and nineteen advisories stand — the
decrease from twenty is the whole of this line going quiet.

**The two earlier figures are not comparable to each other, and that is worth saying rather than
reconciling.** *11 filenames of 259* was measured on 2026-08-18 while `quantity:` lines were still
silencing pages; *thirteen* is what the advisory named at `1520164` after the field was stripped;
*sixteen* is what was renamed, because **three of the offenders were invisible to the check** —
their names were built on *second*, *fourth* and *fifth*, and the word list held no ordinals. The
owner ruled them in, and the ruling has a page ([[ordinals-count-and-first-does-not]]).

**What the sweep cost that nothing predicted**: `sed` cannot tell an address from a quotation, and
it rewrote two slugs that pages were quoting as examples. One of those sentences came to say the
opposite of what it was written to say
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]],
[[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]). A rename ends in a
read of its own diff, not in a clean exit code.
