---
type: rule
kind: Leaf
purpose: Prevents the librarian's writes from landing in the session's own commit, or from ending without a commit at all
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: "[[rule-documentation]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, workflow, git, librarian]
core: true
---

## Purpose

Prevents the librarian's writes from landing in the session's own commit, or from
ending without a commit at all. The Retro commit is the baseline. What the librarian
changed must be readable as one separate diff, six months on.

## Render

<!-- rule-close -->
Close. Run `make lint` and keep its output for the report. Commit the vault with the
files the render wrote: `git add vault CLAUDE.md .claude guppi.toml && git commit -m
"docs(vault): librarian, <date>"`, never `--amend`, never a path outside those four. After the commit, no file the render wrote stands untracked. Then return a report of at most twenty
lines: pages created and updated per category, entries marked incomplete or failed,
pages archived, the flags you raised, the lint total. Nothing else.
<!-- /rule-close -->

## History

- 2026-10-14 shipped with GUPPI
