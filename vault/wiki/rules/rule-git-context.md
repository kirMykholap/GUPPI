---
type: rule
kind: Leaf
purpose: Prevents a session from starting on a branch it does not know
status: built
enforcement: render
implementation_ref: [.guppi/guppi/gitstate.py, .guppi/tests/test_gitstate.py]
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: "[[rule-skill-hi]]"
estimates: ["[[estimate-git-context-current]]", "[[estimate-git-context-offers-git-init]]", "[[estimate-git-context-gitstate-exits-zero]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
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
Render: !`uv run --project .guppi guppi render --sync`
Branch: !`uv run --project .guppi guppi gitstate`

When the line `Branch:` above reads `none: this folder is no git repository`, take this step first, before `/sprint-open` and before the Frontier. Say that GUPPI works only in a git repository, and ask the person whether you run `git init -b main`, which names the first branch `main`. On the person's yes, run `git init -b main` with the Bash tool, say that the repository is made, and tell the person to type `/hi` again. On a no, tell the person to type `/hi` again after `git init -b main`. After either answer, start no `/sprint-open`, write no Frontier, and end the reply.
<!-- /rule-git-context -->

## History

- 2026-11-03 shipped with GUPPI
