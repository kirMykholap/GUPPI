---
title: "The deprecated-link advisory prints one line per dead target, not per citing page and not per edge"
type: decision
status: archived
authority: deprecated-link-advisory-shape
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-check.sh"]
tags: [vault, retrieval, harness]
---

# The ruling, 2026-08-29

**Owner selected: one line per dead target.** Forty-three lines on the first reading.

**Rejected: one line per citing page**, which would have printed 212 lines, **and one line per edge**,
which would have printed 429. All three were put to him with their counts measured
([[an-advisory-prints-one-line-and-sorts-what-it-names]]).

**It lives behind `--lint`**, not in the bare gate run, which is where an advisory about the state of
the corpus belongs rather than about the run in front of you
([[the-tag-density-advisories-move-behind-lint]]).

# Why the target and not the edge

**The repair is per target.** A retired page is either given a live successor and its citations
repointed, or the citations are left as the vault's own rule permits — and either way the unit a
reader acts on is the target, not each of the sentences pointing at it.

**Forty-three is a list a person reads; 429 is a paragraph nobody reaches the end of.** That is the
same ground the filename advisory was given its shape on, by the same owner
([[the-filename-advisory-prints-one-name-per-line]]).

# The first reading, 2026-08-29

**43 retired pages are linked from live `wiki/` pages, and 3 of them are named in a `decided_by:`
field.** The three are not a defect to repair:
[[a-decided-by-target-in-the-archive-is-kept-and-becomes-a-lesson-candidate]] rules that such a pointer
is kept as it stands.

**A bare gate run is unchanged at 23.6 s and `--lint` costs 28.6 s**, so the advisory itself is about
five seconds — linear rather than the quadratic shape the comment above rules 4 and 5 warns about
([[a-link-pass-that-keeps-the-filename-beside-the-link-is-linear]]).

**Its input drifts within a single day.** Re-derived on the evening of 2026-08-28: 43 slugs, 429
occurrences, 336 page-target pairs, 212 live pages, against the 42 / 424 / 332 / 210 the proposal
recorded the same morning. **The method reproduces exactly; the denominators move**
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
