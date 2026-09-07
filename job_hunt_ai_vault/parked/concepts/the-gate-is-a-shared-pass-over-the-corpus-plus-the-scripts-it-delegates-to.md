---
title: "The gate is a shared pass over the corpus plus the scripts it delegates to, and the shared pass dominates"
type: concept
status: current
authority: gate-cost-decomposition
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-check.sh"]
tags: [harness, vault, testing]
---

# The shape

**Rules 1 through 10 ride one `awk` pass over every page.** Rule 12 delegates to
`scripts/vault-inject.sh` and rule 13 to `scripts/vault-authority.sh`. Those two are the separable
part; the shared pass is not separable at all.

# The reading, taken on a quiet machine on 2026-08-24

**A 15.3 s run**, of which rule 12 is 3.57 s, rule 13 is 1.5 s, and the gate's own passes over the
corpus are 10.2 s. **Two thirds of the cost is the part that cannot be narrowed one rule at a time.**

**This is the argument against the arithmetic.** Twenty rules and one of them wanted does not mean a
twentieth of the time: rules 1 through 10 are decided in the same traversal, so skipping nine of
them saves nothing.

**An earlier reading said the separable part was larger.** It was taken on a contended machine and
is withdrawn ([[a-measurement-taken-while-other-work-runs-against-the-same-disk-measures-nothing]]).

# What it decides

**The ceiling on narrowing the gate is far below what the rule count suggests**, which is why the
second step of [[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]] stays deferred with the
measurement in hand ([[the-suite-gets-a-narrowed-fast-mode-and-one-full-run-at-the-end]]).

**And it is why the flag that would skip rules 12 and 13 is the larger prize** — those two are the
only part of the run that can be lifted out whole
([[the-injector-is-cheapened-instead-of-adding-a-flag-and-the-prohibition-is-not-lifted]]).
