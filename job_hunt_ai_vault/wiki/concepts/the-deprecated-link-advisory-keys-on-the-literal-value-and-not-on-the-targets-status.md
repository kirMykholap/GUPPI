---
title: "The deprecated-link advisory keys on the literal value, not on \"the target's status\""
type: concept
status: current
authority: deprecated-link-advisory-key
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-check.sh"]
tags: [vault, retrieval, record-schema]
---

# The distinction

**The verdict fires on a link whose target carries the literal value `deprecated`.** It does not fire
on "a target whose status marks it as out of the working set", which is the phrasing the proposal used
and which reads as the same thing.

**They stopped being the same thing on the day the sweep first ran.** About **240 pages in `archive/`
now carry `status: archived`**, and a verdict phrased about the status in general would have grown
**from 43 lines to hundreds** in that one operation.

**Two items shipped on 2026-08-29 and this is where they touch** — the sweep and the advisory were
designed on different days by different reasoning, and only the ordering of the build made the
collision visible ([[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]],
[[the-deprecated-link-advisory-prints-one-line-per-dead-target]]).

# Why `deprecated` is the right literal and `archived` is not

**They mean opposite things about the claim on the page.** A `deprecated` page was replaced *because it
went false*, so a live page still pointing at it is pointing at something wrong. An `archived` page is
merely out of the working set and **what it asserts is still true**
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**A link into `archive/` is normal and expected**, and after 2026-08-29 the corpus is full of them:
every page an older page cited as a source or a successor may now live there, and every one of those
links still resolves ([[the-vault-directory]]).

**A mark that opens a state is not a mark that names a place**, which is the ruling this rests on
([[a-status-value-is-either-an-address-or-a-stage-and-the-gate-treats-them-oppositely]]).

# What it leaves unsaid

**A `refused` or `implemented` proposal in `archive/` is not covered either**, by the same literal
test. Neither went false, so a link into one is not a broken claim.

**And three of the 43 dead targets are named in a `decided_by:` field**, which is kept as it stands
rather than repaired ([[a-decided-by-target-in-the-archive-is-kept-and-becomes-a-lesson-candidate]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
