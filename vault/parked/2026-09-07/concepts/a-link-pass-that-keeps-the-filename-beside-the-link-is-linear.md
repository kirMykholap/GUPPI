---
title: "A link pass that keeps the filename beside each link is linear, and the warning the link rules carry is about a different shape"
type: concept
status: current
authority: link-pass-shape
basis: measurement
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-check.sh"]
tags: [vault, retrieval, harness]
---

# The mechanism

**One walk of `wiki/` emits every `[[wikilink]]` with the file it was found in.** Target and citer come
out of the same pass, so the join that answers *which live pages link into a retired page* is done
afterwards over a list, not by going back to the tree.

**The alternative is to look each target up**, which is one recursive grep per target and is the shape
that gets expensive.

# What it costs, measured 2026-08-29

**A bare gate run is 23.6 s and `--lint` is 28.6 s**, so the deprecated-link advisory costs about
**five seconds** over a 523-page `wiki/` producing 43 dead targets, 336 page-target pairs and 429
occurrences ([[the-deprecated-link-advisory-prints-one-line-per-dead-target]]).

**The comment above rules 4 and 5 warns about 71 seconds at 75 pages.** That figure describes **N
recursive greps over the whole tree** and does not bound anything written this way. Reading it as a
bound on any link work is what would have stopped this advisory being built at all
([[a-cost-measured-on-a-script-is-not-the-cost-it-adds-to-what-runs-it]]).

# Why it matters beyond this one advisory

**It is the same invariant the archival selectors are built on** — one pass over the corpus, never one
pass per item ([[a-selector-is-one-pass-over-the-corpus-and-never-one-pass-per-page]]).

**And it is why the advisory could ship the same day as the sweep.** The corpus grew a third of a
`wiki/` worth of `archive/` in one operation, and a per-target lookup would have made the advisory's
cost move with it.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
