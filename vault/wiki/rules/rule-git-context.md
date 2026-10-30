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
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
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

When the line `Branch:` above reads `none: this folder is no git repository`, take this step first, before `/sprint-open` and before the Frontier (as set in case 851.1). Say that GUPPI works only in a git repository, and ask the person whether you run `git init -b main`, which names the first branch `main`. On the person's yes, run `git init -b main` with the Bash tool, say that the repository is made, and tell the person to type `/hi` again. On a no, tell the person to type `/hi` again after `git init -b main`. After either answer, start no `/sprint-open`, write no Frontier, and end the reply.
<!-- /rule-git-context -->

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
- 2026-10-13 updated: the remote is the repository GUPPI on GitHub; /hi still runs no git pull · [[decision-case-787.2]]
- 2026-10-13 status: built → draft · cascade
- 2026-10-13 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the history of the remote stands in the bracket of its pointers · [[decision-case-809]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-16 updated: the branch and the status come from guppi gitstate, and outside a git repository /hi asks to run git init -b main and ends · [[decision-case-851.1]]
- 2026-10-16 estimate estimate-git-context-offers-git-init added · [[decision-case-851.1]]
- 2026-10-16 estimate estimate-git-context-gitstate-exits-zero added · [[decision-case-851.3]]
- 2026-10-16 status: built → draft · cascade
- 2026-10-26 updated: the history of the git commands and the merge by /merge-main stand in brackets with their case · [[decision-case-881.1]]
- 2026-10-29 status: draft → built · cascade
- 2026-10-30 updated: ## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/gitstate.py · [[decision-case-942.1]]
