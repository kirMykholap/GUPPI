---
title: "The address verdict catches the leftover copy, not the region in the wrong file"
type: concept
status: current
authority: address-verdict
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-check.sh", "scripts/vault-inject.sh"]
tags: [harness, testing, vault]
supersedes: [[a-region-is-checked-against-its-rules-governs]]
---

# The hole is narrower than it first reads, and the difference is the whole page

**The pure wrong-file case was already red before this verdict existed.** A rule governing A whose
region sits only in B: the injector opens A, `region_of` returns `ERR carries no region for it`, and
rule 12 fails — naming the absence in the right file rather than the stray in the wrong one, but
failing.

**The case that survives every other verdict is the region present in A *and also* in B.**

| Verdict | Why it passes on the leftover |
|---|---|
| rule 11, `dupslug` | its key is `FILENAME SUBSEP slug` — **per file**, so two files each carrying the slug once is not a duplicate |
| rule 11, slug resolves | the page exists; the region is well formed |
| rule 12 | the injector never opens B, so the comparison never happens there |

**So B keeps whatever it was handed on the day it was copied, for good, while reading as governed
text.** The verdict added on 2026-08-17 joins the region's file against its rule's `governs:` and
reports it ([[the-address-verdict-joins-an-existing-rule-instead-of-becoming-its-own]]).

## What this cost to get right, and it was nearly not

**A selftest case built from the proposal as written would have passed with the new code reverted.**
The proposal stated the hole as *"a region carrying a rule's slug in a different governed file"*, and a
case built from that sentence is the pure wrong-file case — already red, for another reason. The case
that was built instead is **region in the right file and a copy in another**, which nothing else
reports ([[a-test-built-from-a-specification-can-pass-without-the-code]]).

The correction came from a `/pre-task` reading the code before a line was written, along with two other
defects in the same proposal ([[a-proposal-can-be-wrong-about-the-hole-it-describes]]).

## Two boundaries written into it deliberately

**Only a `current` rule answers.** A region naming a deprecated rule is left alone, because a
deprecated rule renders nothing and widening the join to archived pages would re-open a question closed
on 2026-08-17 ([[a-deprecated-rule-does-not-render]]).

**A rule with no `governs:` at all stays silent here**, because the frontmatter pass already reports it
and a check that says one thing twice teaches a reader to skip both
([[an-advisory-prints-one-line-and-sorts-what-it-names]]).

**A leading `./` is stripped from both sides.** The sweep never writes one, `governs:` may, and how a
path is spelled is not the question this asks ([[governs-is-a-path-from-the-repository-root]]).

## Why it went in before the first migration

**Copying a marker pair into the wrong `SKILL.md` is one keystroke**, and the first rule migration is
the operation that does exactly that kind of copying. The ordering was the owner's and was not a
preference ([[the-slice-execution-rule-migrates-first]]).
