---
title: "A refusal written as one glob can match none of the paths it guards"
type: lesson
status: archived
authority: glob-anchoring-failure
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "scripts/vault-inject.sh"]
tags: [harness, testing, process]
---

# The defect, 2026-08-20

**The new `paths:` condition was written as `*/.claude/rules/*`.** `governs:` is a path from the
repository root and arrives as `.claude/rules/x.md` **with nothing in front of it**
([[governs-is-a-path-from-the-repository-root]]), so the pattern matched none of the destinations it
was written to guard.

**The effect was silent and inverted:** `paths:` became optional in the one directory that requires
it ([[paths-is-required-where-it-is-read-and-nowhere-else]]). A rule generated there would name
nothing to match, and would never load.

# What caught it, and what had predicted it

**A selftest case turned over** — `caught 134, missed 1` — which is the instrument working as
designed. **And the pre-task run for this work had named it in advance** as the thing to watch
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

**The repair is a pair of cases, one per side.** A single case can only hold the half it asserts: a
case proving the refusal fires under `.claude/rules/` says nothing about the other spelling, and a
case proving silence elsewhere says nothing about the refusal. The condition now matches both
spellings and both are pinned.

# The general form

**A glob is anchored by whatever produced the string it is matched against**, and in this repository
two conventions coexist: a repository-root path with no prefix, and a path with a directory in front
of it. **A leading `*/` is not free** — it silently requires a prefix.

**The failure direction is the dangerous one.** A pattern that is too narrow makes a refusal
disappear, and a refusal that never fires is indistinguishable from a tree with nothing wrong in it
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).
