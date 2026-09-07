---
title: "The `governs:` destination-uniqueness verdict is removed, and uniqueness moves onto the file-and-slug pair"
type: decision
status: archived
authority: governs-uniqueness
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-check.sh", "scripts/vault-inject.sh"]
tags: [harness, vault, testing]
---

# Decided by the owner on 2026-08-17, at `e478c19`

**The verdict forbade two current rules from governing one file.** It is gone from
`scripts/vault-check.sh`. **Rejected alternative: keep it and stop the migration**, since all four
rules of the repository's `CLAUDE.md` share that destination and the second page to be written was
already illegal.

**The verdict was stricter than the schema it guarded.** The schema says a rule names the one
destination **its** text is injected into; it says nothing about a destination taking one rule. A
check that refuses input its own written rule permits is the shape of
[[the-hook-was-stricter-than-the-rule-it-enforced]], happening a second time in this project.

**Its stated argument was false, and that was measured rather than argued.** The comment said the
uniqueness was needed because a renderer would otherwise *have to pick*. It does not:
`scripts/vault-inject.sh` keys on the pair of file and slug, and at four rules rendering into one
file it produced four regions and `0 problem(s)`. Nine rules render into that file today.

## What it obliges

**Uniqueness now lives on the pair, and it is held in two places rather than one:**

| The case | Where it is caught |
|---|---|
| one slug marking two regions in one file | rule 11's `dupslug` verdict ([[a-region-is-a-paired-comment-named-for-a-rule]]) |
| a region sitting in a file its rule does not govern | the fifth verdict, inside rule 11 ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]) |

**And two harness files had to be corrected**, because a removed rule leaves its arguments behind:
the vault's own `CLAUDE.md` still documented `governs:` as *"required, and unique across current
rules"*, and the check still carried the comment arguing the uniqueness where no verdict printed any
more. Both were fixed by the session at `ba998a0` — they are harness files, not the librarian's
([[the-one-writer-rule-covers-the-registers-too]]).

**The selftest case flipped rather than disappearing**: two rules on one file with two regions is now
asserted **green**, where it was asserted red. A case removed leaves no evidence that the old
behaviour is gone; a case inverted does ([[a-test-green-under-any-implementation]]).

## How it was found, and why that is the recorded part

**It surfaced on the mechanism's first real use, not in review.** The design was written on
2026-08-16, the rule was built the same day, and the day after it blocked the exact migration it had
been built to support. Nothing in the design read as wrong until a real tree was put through it
([[a-proposal-must-be-rechecked-when-the-frame-changes]]).

The librarian marked this as a contradiction on both halves rather than choosing, and the owner
resolved it in the same turn ([[the-librarian-writes-unattended]]). The marked blocks stand on
[[a-deprecated-rule-does-not-render]], [[rules-becomes-a-type-of-its-own]] and
[[marked-regions-and-the-prose-outside-them]] with a dated resolution appended under each — the
alarm is the record of how the decision was reached, and deleting it would delete that.
