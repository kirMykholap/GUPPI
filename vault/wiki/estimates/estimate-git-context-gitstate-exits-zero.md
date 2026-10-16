---
type: estimate
kind: QA
status: passed
target: "[[rule-git-context]]"
purpose: Whether guppi gitstate prints the branch and the status in a git repository, and one line in a folder that is no git repository, and exits 0 in each case
method: uv run --project .guppi pytest .guppi/tests/test_gitstate.py
origin: raw/2026-10-16/0342/ledger.md#case-851.3
sprint: plugin
created: 2026-10-16
tags: [session, harness, git]
---

## Criterion

When:
`uv run --project .guppi guppi gitstate` of `.guppi/guppi/gitstate.py` runs in a folder, from the `Branch:` line of `.claude/skills/hi/SKILL.md`, from a test or by hand.

Then:
In a git repository, it prints the current branch, then a line `Status:` and the lines of `git status --short` under it, and exits 0.
**＋** In a folder that is no git repository, it prints the one line `none: this folder is no git repository` and exits 0.
**－** It writes nothing in the folder.

## Result

2026-10-16, Retro of session 0342: `uv run --project .guppi pytest .guppi/tests/test_gitstate.py` 4 passed — outside a repository the one line `none: this folder is no git repository` and exit 0, a missing git the same; after `git init -b main` the lines `main`, `Status:`, `?? notes.txt` and exit 0; nothing written in the folder; in this repository the command printed `plugin`, `Status:` and the status, exit 0

## History

- 2026-10-16 created · [[decision-case-851.3]]
- 2026-10-16 status: pending → passed · raw/2026-10-16/0342/ledger.md#L19
