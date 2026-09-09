---
title: "The region-coverage figure is dated where it stands rather than patched into a new one"
type: decision
status: archived
authority: coverage-figure-repair
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-check.sh"]
tags: [vault, harness, retrieval]
---

# Deferred 2026-08-18, with the repair named and not applied

**Seven `current` pages carry `1 of 13` or `0 of 13`, plus `index.md`.** Measured 2026-08-18 with
`rg -l "1 of 13|0 of 13"` over the vault:
[[a-governed-file-with-no-region-is-an-advisory]], [[what-the-harness-build-waits-on]],
[[the-governed-set-is-swept-and-markdown-by-property]], [[vault-scripts]],
[[a-rule-over-every-page-makes-every-test-fragile]],
[[the-harness-is-built-by-a-script-and-guarded-by-a-gate]],
[[marked-regions-and-the-prose-outside-them]], and `index.md`.

**They go stale the day the AST rule moves to `.claude/rules/` and the denominator becomes 14**
([[moving-a-rule-into-claude-rules-with-a-paths-scope]]).

**Rejected: patch all eight into a new number.** That is extending a copy that has already drifted,
which this corpus repairs by deletion rather than correction
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]],
[[a-stated-count-drifts-from-the-list-it-heads]]). Eight copies patched today is eight copies to
patch again on the next move.

## The pattern to copy, and the one page the number is read from

**A count is written with its date, or it is not written.** The advisory itself is the only
non-stale source — `bash scripts/vault-check.sh` prints the fraction and names every file carrying
no region, sorted ([[an-advisory-prints-one-line-and-sorts-what-it-names]]). A page that needs the
number says when it measured it.

**Nothing is corrected here**, because correcting is the move being refused. The figure stands at
`1 of 13` on 2026-08-18 and the copies above are undated where they are not already inside a dated
section.

## What closes it

Deleting the number from the seven pages and letting each cite the advisory, or dating each in
place. **Either is a sweep across eight files and is the owner's to schedule**; what is decided here
is only that the third option — renumbering — is not taken. How the fraction is to be reported when
the denominator does move is
[[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]].

## The day arrived the same day — 2026-08-18, and nothing was renumbered

**The denominator moved before the AST rule did.** `.claude/rules/` was created for the probe, and
`vault-check.sh` now reports **`1 of 14`** ([[the-conditional-delivery-probe]],
[[the-governed-set-is-swept-and-markdown-by-property]]). The numerator did not move: the same twelve
unmarked files are unmarked, plus the probe file
([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

**So the eight copies of `1 of 13` are now stale rather than merely fragile**, and they are still not
patched — that is the decision above, unchanged. What is added here is that the predicted day has
happened, and that the probe is temporary: if the probe is cleared without the AST rule landing, the
fraction returns to `1 of 13` and any patch made today would have been wrong twice.
