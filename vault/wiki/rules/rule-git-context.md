---
type: rule
kind: Leaf
purpose: Prevents a session from starting on a branch it does not know, or pulling mid-session
status: built
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: "[[rule-skill-hi]]"
estimates: ["[[estimate-git-context-current]]"]
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness, git]
---

## Purpose

Prevents a session from starting on a branch it does not know, or pulling mid-session.

**Branch tells us what kind of start this is.** On `main` or a working branch, no plan is
open. On a plan branch, unfinished work exists and becomes the first Frontier item. This is
never restated in `brief.md` — git already knows, and a second source of truth eventually
disagrees with the first.

**`git pull` happens here and only here.** Pulling mid-session, after the plan is written
and half the tasks are ticked, breaks the session.

## Render

<!-- rule-git-context -->
Pull: !`git pull --ff-only 2>&1 || true`
Render: !`uv run guppi render --sync`
Branch: !`git branch --show-current`
Status: !`git status --short`
<!-- /rule-git-context -->

## How it works

`--ff-only` so a pull can never open a merge inside a session start. The `Render:` line after it runs `uv run guppi render --sync` once more, so what the pull brought reaches its governed files in the same session; a diff on that line is a Frontier item like the one of the session start (case 115). A failing pull — no
upstream, a remote that is not this project, a conflict — prints its message into the
context and becomes a Frontier item; `|| true` keeps the skill going. As of 2026-09-09 the
remote is the product repository this vault was split from and `migration` has no upstream;
the owner left both as they are until Slice 5.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-10 status: draft → built · cascade
- 2026-09-14 updated: a Render line after Pull runs guppi render --sync inside /hi; supersedes case 106 (case 115) · [[decision-case-115]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
