---
title: "`git status` reports a file modified from a cached stat size, and renormalising never refreshes it"
type: concept
status: current
authority: git-status-stat-cache
basis: measurement
sprint: S1
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md"]
tags: [process, vault]
---

# The cause, identified 2026-08-16

The index caches each entry's **stat data, including its size**. Rewriting a file into the other
line-ending form leaves the blob identical, so **`git add --renormalize` never restats the entry**
and the cached size stays at the old form's. `git status` compares that cached size against the
file on disk, finds a mismatch, and reports the file modified — for as long as the cache stands.

Measured on one file:

```
git ls-files --debug   size: 2496        against a 2455-byte file
worktree hash          26800c3a
index hash             26800c3a          identical
```

**`git status` and `git update-index --refresh` then report it modified forever.** Reading `git
status` twice — the ritual this project had adopted — never helped, and could not have: a second
read cannot fix a stale cache.

**`git add -A` restats and settles it.** That is the whole remedy.

## `git checkout-index -f` does not force what it looks like it forces

**It does not overwrite an existing file** whose normalised content already matches the index. The
`-f` is not enough; **the file has to be removed first**. Forcing a working tree to match its
attributes is therefore *delete, then checkout*, not *checkout with a flag*.

That cost twenty minutes of believing a refresh had run while the working copy was untouched — the
same failure shape as a check that passes for the wrong reason
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

## What this replaces

[[line-endings-make-git-status-overstate-what-changed]] recorded the overstatement, measured it
three times, and said the cause **remained unidentified**. It is identified here; the lesson page
keeps its measurements and its advice — quote `git diff --numstat`, distrust `git status --short`
— and now names this page for the mechanism. The policy half is
[[markdown-is-pinned-to-lf]].

## The other direction of the same trust — 2026-08-17

This page explains `git status` **overstating** what changed. It also **understates**, and in a way
no cache flush repairs: **git does not track empty directories**, so a stray empty directory in the
working tree is invisible to it forever — [[an-empty-directory-is-invisible-to-git-status]]. One
instrument, two directions of error, and every session in this project reads it and says *the tree
is clean*.
