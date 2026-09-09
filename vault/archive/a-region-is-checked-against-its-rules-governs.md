---
title: "The fifth verdict: check each region against its own rule's `governs:`"
type: proposal
status: deprecated
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
superseded_by: [[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]
tags: [harness, testing]
---

# The hole, exactly

Rule 11 checks that a region's slug names a rule page that exists. The injector writes each current
rule into **the one file its `governs:` names**. Neither asks whether the region it found is *in
that file*.

**So a region carrying a rule's slug in a different governed file is untouched by the injector and
unremarked by rule 11.** It sits there with stale content, or with no content at all, and nothing
complains. The gate is green, the harness file states something nobody wrote, and rule 12 never
looks at it because rule 12 compares the region the injector wrote.

## Consequence of waiting

**The first rule migration is exactly when a region can land in the wrong file** — copy-pasting a
marker pair into the wrong `SKILL.md` is a one-keystroke error and it is the very operation the
next session performs. Every day this stands is a day the mechanism's first real use is unguarded.

## What it would take

**Roughly fifteen lines and two selftest cases**, and both halves already exist: rule 11 already
holds every region with its slug and its file, and the frontmatter pass already holds every current
rule's `governs:` ([[governs-is-a-path-from-the-repository-root]]). The comparison is a join
between two tables the check already builds.

- **red** — a region whose slug names a current rule that governs a different file.
- The two selftest cases: the region in the wrong file, and the region in the right file staying
  green.

Touches `scripts/vault-inject.sh` and `scripts/vault-check-selftest.sh`.

## Status

**Deferred by the owner on 2026-08-17, and it goes *before* the first migration next session** —
which makes it the only row on the register with an ordering constraint rather than a cost
([[what-the-harness-build-waits-on]]).

It is the verdict the design's own table never had: the four in
[[marked-regions-and-the-prose-outside-them]] all ask about the region's *existence*, and none asks
about its *address*.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

# Built on 2026-08-17, and retired — with three defects of its own on the record

**The verdict exists.** It went into **rule 11**, not rule 12 and not the injector, and it went in
before the first rule migration exactly as this page asked
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]],
[[the-address-verdict-joins-an-existing-rule-instead-of-becoming-its-own]]).

**Three things above are wrong, and they were found by a `/pre-task` before a line was written**
([[a-proposal-can-be-wrong-about-the-hole-it-describes]]):

1. **"Touches `scripts/vault-inject.sh`"** — it does not. The join belongs in `scripts/vault-check.sh`,
   which is where this page's own *What it would take* paragraph puts it. Giving the injector a table
   of regions found elsewhere would put a second copy of the swept governed set in the tree.
2. **"the fifth verdict of rule 12"**, in the last section — rule 12 contains no logic of its own; it
   asks by running the injector ([[a-check-asks-by-running-the-writer-it-checks]]). `sprint.md` and
   [[what-the-harness-build-waits-on]] repeated the misattribution from here.
3. **The hole as stated is already red.** *"A region carrying a rule's slug in a different governed
   file"* — the injector reports `ERR carries no region for it` for the governed file and rule 12
   fails. **What the verdict uniquely catches is the leftover duplicate**: the region in the right
   file *and also* in another. **A selftest case built from the sentence above would have passed with
   the new code reverted** ([[a-test-built-from-a-specification-can-pass-without-the-code]]).

**Nothing above is edited.** The page is the record of what was designed, including what it got wrong,
which is the reason a proposal is retired rather than rewritten
([[proposals-are-a-folder-not-a-status]]).
