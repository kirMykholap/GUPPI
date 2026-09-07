---
title: "`governs:` is read on any page, and the red moved to a `<!-- text -->` slice that names no destination"
type: concept
status: current
authority: governs-outside-rules
basis: code
sprint: S2
created: 2026-08-18
supersedes: [[a-page-outside-wiki-rules-carrying-governs-is-silently-inert]]
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, record-schema, vault]
---

# What changed at `e83ce28`, and why the silence had to move rather than disappear

**`scripts/vault-inject.sh` walks `wiki/*/*.md`, pre-filtered by `grep -l '^governs:'`.** A page in
any folder that names a destination is opened and rendered. Until that commit the injector globbed
`wiki/rules/` alone and every `governs:` branch of the check was gated on `folder == "rules"`, so
the field was legal, spelled correctly and did nothing outside that folder — the state described on
the retired [[a-page-outside-wiki-rules-carrying-governs-is-silently-inert]].

**"No `governs:`" changed meaning with the glob.** Under `wiki/rules/*.md` a page with no
destination was broken. Under `wiki/*/*.md` most of the corpus delivers nothing by design, so the
absence is a **silent skip** — and it has to be, or the field becomes required on every page in the
vault.

**So the red moved to the inverse.** A `<!-- text -->` slice on a page carrying no `governs:` is
red: it marks text that nothing delivers while reading, to its author and to every later reader, as
though it were governed. That is the same failure this vault names most often — a green that
examined nothing ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]) — pointed at the
half of the pair that still had it.

## The pre-filter is what makes the wider walk affordable

`grep -l '^governs:'` over the glob costs **113 ms**, measured 2026-08-18, and the widened walk from
9 pages to 258 came out *faster* than the narrow one. The cost of this loop was never the page
count ([[measure-before-optimising-and-count-processes-not-pages]]).

## The first page to use it is not a rule

[[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]] is a `concepts/` page carrying
`governs: CLAUDE.md`, and its region is the first in this project rendered from outside
`wiki/rules/`. The decision that any page may carry the field is
[[governs-becomes-a-property-of-any-page]]; what the marker had to gain for it to resolve is
[[a-marker-with-its-type-is-a-complete-address]].

## One gate deliberately did not widen with it

`nogoverns` — a page in `wiki/rules/` that names no destination — **stays rules-only**, because
widening it would make `governs:` required on all 258 pages. `ruleclaim` stays rules-only too, and
what that leaves undecided is [[authority-beside-governs-on-a-non-rule-page-is-unruled]]. The
reasoning for each of the three branches is [[the-governs-branch-widens-and-the-others-stay-rules-only]].
