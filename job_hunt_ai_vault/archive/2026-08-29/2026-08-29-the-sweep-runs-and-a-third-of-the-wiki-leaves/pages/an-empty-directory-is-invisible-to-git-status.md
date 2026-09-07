---
title: "An empty directory is invisible to the check this project trusts the tree to"
type: lesson
status: archived
authority: empty-directory-blindness
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "log.md"]
tags: [process, testing]
---

# A stray `n/` sat in the repository root for two days

It appeared on 2026-08-15 and the owner spotted it **by eye** on 2026-08-17. **Git does not track
empty directories**, so it never appeared in `git status` — and `git status` is what every session
in this project reads, twice, before saying the tree is clean.

**It was said three times on 2026-08-17, and each time it was true of git and false of the disk.**

# Why it is a lesson and not a tidy-up

The sentence *"the tree is clean"* is used here as a fact about the working directory, and it is
sourced from a tool that answers a narrower question. That gap is exactly the one this project has
already been bitten by from the other side — `git status` **overstating** what changed, because of
line endings and a stale stat cache
([[line-endings-make-git-status-overstate-what-changed]], [[the-stale-stat-cache-behind-git-status]]).
**One instrument, two directions of error, and both were read as truth.**

**Origin is almost certainly a hand-typed command whose escape was eaten** — the same family of
defect that cost two debugging passes the same day
([[a-test-that-fails-for-its-own-reasons-proves-nothing]]).

# What would catch it

`git status` cannot, by design. Anything that answers *is the working directory clean* has to look
at the directory: `git clean -nd` lists untracked directories, and a check over the repository root
is one line. **Nothing is built**, and this is recorded rather than fixed — adding a rule is not an
ingest's act.

Until then the discipline is the honest wording: **say "git reports nothing", not "the tree is
clean"**.
