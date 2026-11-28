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
created: 2026-11-28
tags: [session, harness, git]
core: true
---

## Purpose

Prevents a session from starting on a branch it does not know.

**Branch tells us what kind of start this is.** On the main branch or a working branch, no plan is
open. On a plan branch, unfinished work exists and becomes the first Frontier item. This is
never restated in `brief.md` — git already knows, and a second source of truth eventually
disagrees with the first.

## Render

<!-- rule-git-context -->
Render: !`uv run --project .guppi guppi render --sync`
Branch: !`uv run --project .guppi guppi gitstate`

When the line `Branch:` above reads `none: this folder is no git repository`, take this step first, before `/sprint-open` and before the Frontier. Say that GUPPI works only in a git repository, and tell the person to type `! git init -b {{main_branch}}`, which names the first branch `{{main_branch}}` and which Claude Code runs at once as the person's own shell command, in Plan Mode too, and then to type `/hi` again. Ask no question and run no `git init` yourself, since the session stands in Plan Mode and nothing is written before a ratified Case. Start no `/sprint-open`, write no Frontier, and end the reply.
<!-- /rule-git-context -->

## History

- 2026-11-28 shipped with GUPPI
