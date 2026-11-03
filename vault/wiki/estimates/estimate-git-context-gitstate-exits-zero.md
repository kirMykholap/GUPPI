---
type: estimate
kind: QA
status: passed
target: "[[rule-git-context]]"
purpose: Whether guppi gitstate prints the branch and the status in a git repository, and one line in a folder that is no git repository, and exits 0 in each case
method: uv run --project .guppi pytest .guppi/tests/test_gitstate.py
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness, git]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi gitstate` of `.guppi/guppi/gitstate.py` runs in a folder, from the `Branch:` line of `.claude/skills/hi/SKILL.md`, from a test or by hand.

Then:
In a git repository, it prints the current branch, then a line `Status:` and the lines of `git status --short` under it, and exits 0.
**＋** In a folder that is no git repository, it prints the one line `none: this folder is no git repository` and exits 0.
**－** It writes nothing in the folder.

## Result

2026-10-16, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
