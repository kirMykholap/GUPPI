---
type: rule
kind: Leaf
purpose: Prevents a session from starting on a branch it does not know
status: built
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: "[[rule-skill-hi]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, harness, git]
core: true
---

## Purpose

Prevents a session from starting on a branch it does not know.

**Branch tells us what kind of start this is.** On `main` or a working branch, no plan is
open. On a plan branch, unfinished work exists and becomes the first Frontier item. This is
never restated in `brief.md` — git already knows, and a second source of truth eventually
disagrees with the first.

## Render

<!-- rule-git-context -->
Render: !`uv run guppi render --sync`
Branch: !`git branch --show-current`
Status: !`git status --short`
<!-- /rule-git-context -->

## How it works

The `Render:` line runs `uv run guppi render --sync` once more inside `/hi`, after the `SessionStart` hook has run it; a diff on that line is a Frontier item like the one of the session start. `/hi` runs no `git pull`. The local `main` follows `origin/main` in the opening Case of a sprint, by `git fetch origin` and `git merge --ff-only origin/main`, and a sprint branch takes `main` by the merge Case of `/merge-main`.

## History

- 2026-10-14 shipped with GUPPI
