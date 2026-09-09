---
title: "A selector is one pass over the corpus, and never one pass per page"
type: concept
status: current
authority: sweep-selector-shape
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-archive.sh"]
tags: [vault, harness, testing]
---

# The invariant

**Every archival selector reads the corpus once.** The slugs it is asking about go into a pattern file
and `grep -oF -f` extracts every one that occurs, in a single walk of the tree.

**The naive shape is one full-tree grep per candidate page.** For `lessons/` on 2026-08-29 that was
182 candidates, so 182 recursive greps over a corpus the gate already spends 23 seconds walking once.

**The cost of the naive shape grows with the product of two numbers that both grow** — pages selected
times pages searched — while the pass shape grows with one.

# Where the time actually goes, measured

**The dry run costs 3m10s and the real run 5m16s over the live corpus**, and almost all of it is **not**
the selectors. It is the per-page citation count, which is one grep of `wiki/` and `archive/` for each
page actually selected ([[vault-archive-sh]]).

**So the invariant was applied where it was cheap and the expensive thing is elsewhere.** That is worth
saying plainly: the selectors are the part that would have been quadratic and were not written that
way, and the precondition check is the part that is per-page and stayed per-page — because it asks a
different question of each page rather than the same question of all of them.

**A sweep is a minutes-long operation, not a seconds-long one**, and any design that assumes otherwise
is pricing the selectors and forgetting the guard.

# Where else the same shape appears

**The deprecated-link advisory is one walk that keeps `FILENAME` beside each link**, for the same
reason and with the same result ([[a-link-pass-that-keeps-the-filename-beside-the-link-is-linear]]).

**Rule 5 of the gate carries a comment warning about 71 seconds at 75 pages**, and that figure
describes N recursive greps over the whole tree — a different shape, and not a bound on anything
written this way ([[vault-scripts]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
