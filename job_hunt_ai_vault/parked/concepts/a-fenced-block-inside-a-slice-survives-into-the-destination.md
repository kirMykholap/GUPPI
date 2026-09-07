---
title: "A fenced block inside a `<!-- text -->` slice survives into the destination, and the fence flag now gates recognition only"
type: concept
status: current
authority: injector-fence-defect
basis: code
sprint: S2
created: 2026-08-18
supersedes: [[the-injector-drops-a-fenced-block-inside-a-slice]]
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-inject.sh"]
tags: [harness, testing, vault]
---

# Fixed at `e83ce28`

**A slice carrying a fenced code block renders whole.** Until that commit the two extractors in
`scripts/vault-inject.sh` opened with a fence toggle placed *before* the rule that accumulates slice
content, so every line between the fences was skipped along with the fences themselves — three
lines of slice rendered as one, and the injector reported `1 region(s) rewritten, 0 problem(s)`.
The old behaviour, its proof on an isolated copy, and what it blocked are on the retired
[[the-injector-drops-a-fenced-block-inside-a-slice]].

**The separation that fixes it is the one the retired page named**: a fence must stop a
`<!-- text -->` marker inside it from *opening* a slice, and must not stop the lines of an
already-open slice from *travelling*. Recognition and copying were one flag answering two
questions; they are two now.

## The original reason is intact, which is the half worth checking

Fence-stripping exists so that a documented example of a marker is not read as a marker — without
it this page, the vault's `CLAUDE.md` and the check's own header would each report the harness
broken for describing itself ([[an-example-inside-a-code-block-satisfies-a-search]],
[[a-region-is-a-paired-comment-named-for-a-rule]]).

**Two selftest cases hold the pair**: a slice carrying a fence renders it, and a marker inside a
fence inside a slice does not open a slice. The second is the one that keeps the original reason
intact, and it is the reason the fix is two cases rather than one.

## It was proved by reverting the code, not by reading the specification

Both cases were run against the **old** injector on the same fixture and watched to answer
`every rule agrees`. Written from the specification alone they would have passed with the defect in
place — the failure class this project has already recorded twice
([[a-test-built-from-a-specification-can-pass-without-the-code]],
[[reverting-the-code-tells-you-whether-a-test-tests-anything]]).

## What it unblocks, and what stays prose anyway

**The by-hand `rg` recipe in the repository's `CLAUDE.md` could now become a rendered record.** It
is a fenced block, and that was the mechanical reason it could not
([[the-repository-claude-md-after-the-rules-left-it]]).

**It stays prose on a different ground**, decided by the owner the same day: the routes are the one
part of that file which has never gone stale, and a mechanism that exists to end drift does not
improve text that has been correct since it was written
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]). The excuse is gone; the
decision does not rest on it.
