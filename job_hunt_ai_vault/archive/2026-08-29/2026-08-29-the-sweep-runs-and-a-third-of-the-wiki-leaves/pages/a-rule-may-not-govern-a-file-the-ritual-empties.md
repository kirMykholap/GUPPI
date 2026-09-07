---
title: "A rule may not govern a file the ritual empties, or the injector locks the librarian out"
type: lesson
status: archived
authority: governs-target-liveness
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", "scripts/vault-inject.sh", ".claude/hooks/lock-the-librarian.ps1"]
tags: [harness, vault, process]
---

# The deadlock, found in a plan before it was built

**An approved plan gave the rewritten feedback rule `governs: .superpowers/sdd/vault-feedback.md`** —
the file the rule is about. It is git-ignored, and `/handoff` empties it back to its header every
session.

The chain, each link already built and each correct on its own:

1. `scripts/vault-inject.sh:159` reports a governed destination carrying no region for its rule, and
   `:577` exits 1;
2. a non-zero injector reddens rule 12 of `scripts/vault-check.sh`, which asks its question **by
   running the injector** ([[a-governed-file-with-no-region-is-an-advisory]]);
3. `lock-the-librarian.ps1` reads a red gate as a refusal to dispatch — **and the librarian is the
   only writer permitted to fix the rule page that caused it**
   ([[the-librarian-lock-hook]], [[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**The escape is a hand-write against the one-writer rule**, which this store has already recorded
happening once ([[the-session-wrote-wiki-by-hand-while-the-lock-held-its-only-writer-out]]).

# The general shape

**A `governs:` target must be a file that persists and that a marker pair can live in.** Two
properties, and the failing plan broke both: the file is emptied on a schedule, and it is
git-ignored, so nothing in the tree would show the region missing until the injector said so.

**A file a ritual rewrites wholesale is the same hazard**, whatever the reason for the rewrite. The
question to ask of a candidate destination is not *does the rule belong there* but *will the region
still be there next session*.

# What caught it

**A `/pre-task` on the second edition of the plan**, before approval — 182,599 tokens, 13m40s, 57
tool uses ([[a-pre-task-runs-between-the-plan-and-its-approval]]). Nothing else in the ritual reads
the injector's refusals against a proposed frontmatter field, and the plan had already been reviewed
without noticing.

# What it did instead

**The successor rule governs the three files the decision behind it obliges** — `CLAUDE.md`,
`/vault-ask` and `/handoff` — and says nothing to the file it writes about
([[speak-the-feedback-in-the-turn-and-the-hook-files-it]],
[[feedback-is-recorded-in-the-turn-it-is-noticed]]).
