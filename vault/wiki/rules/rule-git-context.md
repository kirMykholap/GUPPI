---
type: rule
kind: Leaf
purpose: Prevents a session from starting on a branch it does not know
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

The `Render:` line runs `uv run guppi render --sync` once more inside `/hi`, after the `SessionStart` hook has run it; a diff on that line is a Frontier item like the one of the session start (case 115). The repository has no remote since case 528: `origin` was the product repository this vault was split from and `migration` had no upstream, so the pull that stood first in this block failed at every session start. `/hi` runs no `git pull`; a Case that adds a remote writes its pull line and its rule again.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-10 status: draft → built · cascade
- 2026-09-14 updated: a Render line after Pull runs guppi render --sync inside /hi; supersedes case 106 (case 115) · [[decision-case-115]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
- 2026-09-17 deferred · [[decision-case-220]]
- 2026-09-18 deferred · [[decision-case-243]]
- 2026-09-20 updated: a failing pull is a Frontier item unless sprint.md names its decision (case 268.2) · [[decision-case-268.2]]
- 2026-09-28 status: built → draft · cascade
- 2026-09-30 defer by decision-case-220 superseded · [[decision-case-528.1]]
- 2026-09-30 defer by decision-case-243 superseded · [[decision-case-528.1]]
- 2026-09-30 updated: taken up: the pull leaves /hi with the remote; the rule keeps the render, the branch and the status; the defers of cases 220 and 243 retired (case 528.1) · [[decision-case-528.1]]
- 2026-09-30 status: draft → built · cascade
