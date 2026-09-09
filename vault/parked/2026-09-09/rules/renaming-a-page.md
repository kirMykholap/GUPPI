---
title: "Renaming a page"
type: rule
status: current
authority: rename-cost
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[archive-is-rewritten-by-a-path-move-and-log-md-never-is]]
tags: [vault, harness, process]
---

# Renaming a page

What a move costs, what a sweep may touch, what it strands, and why a rewriter needs a detector. Answers "may I rename this, and what breaks if I do".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A path move rewrites `archive/` and never `log.md` ([[archive-is-rewritten-by-a-path-move-and-log-md-never-is]])
- The prose-path detector is refused on its own measurement, most of its findings being correct as written ([[the-prose-path-detector-is-refused-on-its-own-measurement]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *renaming a page* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, `path-rewrite-reach`, whose decision leaves for `archive/`. Three live concepts of this family were available; the slug carried is `rename-cost`, which [[a-page-rename-is-sed-and-verify]] carries and keeps. That concept answers the family's own question — may I rename this, and what does it cost — where `path-rewrite-mechanism` and `log-link-blindness` describe how the rewrite works and what it misses. `decided_by:` still names a member decision, which is what this folder requires.
