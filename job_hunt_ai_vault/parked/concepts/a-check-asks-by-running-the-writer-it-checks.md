---
title: "A check asks its question by running the writer, so writer and check cannot disagree"
type: concept
status: current
authority: check-by-regeneration
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-check.sh", "scripts/vault-inject.sh"]
tags: [harness, testing]
---

# Rule 12 does not compare anything itself

It runs `scripts/vault-inject.sh --check`, which prints every disagreement between a rule page's
marked slice and the region it governs, and writes nothing. Rule 12 reads those lines and fails on
them. **It contains no second implementation of the comparison.**

## Why that shape

**A comparison written twice is two answers waiting to differ.** The writer decides what the
correct content is; a check that decides the same thing independently is a second definition of
correct, and the day they disagree the tree is in a state where fixing either one breaks the other.

It is rule 9's shape, and it is the part of rule 9 that outlived rule 9
([[the-page-list-is-a-query-not-a-generated-file]]): regenerate, then compare against what is on
disk. That rule was retired because the artefact it guarded was replaced, not because the shape was
wrong.

## The comparison is byte for byte

Safe here because `*.md` is pinned `text eol=lf` in `.gitattributes`
([[markdown-is-pinned-to-lf]]). Without that pin a checkout on Windows would rewrite every rendered
region's line endings and the gate would fail on every clone — which is not hypothetical: the first
staleness check in this project fired on every single clone, for the analogous reason
([[staleness-checks-run-at-different-times-and-ask-different-questions]]).

**A new file class raises this question every time**, and `pages.base` is the current unpinned one,
deliberately ([[a-file-class-is-pinned-after-it-costs-something]]).

## What it still does not give

Agreement, never truth. A rule page that is wrong renders flawlessly and passes rule 12 —
[[a-gate-guarantees-agreement-never-truth]].

# Rule 13 was built to this shape, and for this reason — 2026-08-21

**It asks whether a page carries an `authority:` nothing can look up by running
`bash scripts/vault-authority.sh --orphans`**, and reads the lines that come back. It contains no
second implementation of what an orphan slug is
([[authority-becomes-the-index-and-is-required-outside-rules]]).

**The condition it delegates could not have been written into the gate anyway.** While `concepts/`
still admitted `governs:`, the honest statement was *required unless `governs:` is present* — a
condition a per-folder schema has no grammar for, and one the tool evaluates in a single pass it was
already making. The delegation was the cheap answer and the correct one at once.

**And the delegation has a cost this page did not carry until it was measured: a rule that asks by
running a script is silenced by a zero-byte stub.** With an empty `vault-authority.sh` the rule ran,
printed nothing, and reported nothing — every case written for it would have passed having tested
nothing. Rules 12 and 13 are both exposed, and a guard now refuses the suite if either tool is empty
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
