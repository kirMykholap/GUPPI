---
type: estimate
kind: QA
status: pending
target: "[[rule-git-context]]"
purpose: At /hi the context holds the render sync, the branch and the status, and the skill runs no git pull
method: "by hand, after the first /hi that follows the first push to GitHub: the first turn's context, the output of git remote -v and .claude/skills/hi/SKILL.md read against the Criterion, written into the estimate line"
checked: 2026-09-30
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness, git]
---

## Criterion

When:
The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the commands of `rule-git-context`.

Then:
The context holds `Render:` with the output of `uv run guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
**＋** `git remote -v` prints `origin` with the URL of the repository `GUPPI` on GitHub.
**－** The skill runs no `git pull`, and the context holds no `Pull:` line.

## Result

2026-09-30, /hi of session 0248, the first turn's context, `git remote`, `.git/config`, `git rev-parse --abbrev-ref main@{upstream}`: the context holds Render: (empty), Branch: migration, Status: (empty); `git remote` printed nothing; `.git/config` has no [remote] section, its only `origin` text is `vscode-merge-base = origin/main` under [branch "main"] and [branch "migration"]; `main` has no upstream configured; `.claude/skills/hi/SKILL.md` holds no `git pull`, `gh` or `Pull:`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-14 criterion: case 115 added · [[decision-case-115]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L1
- 2026-09-28 updated: the Criterion replaced whole — one When and Then; the Frontier item left to estimate-hi-writes-frontier, the block bookkeeping out; purpose and method set, Context and Method out (case 485.3) · [[decision-case-485.3]]
- 2026-09-30 updated: the Criterion replaced whole — no Pull line, no git pull, no remote; the promise on a pull mid-session gone with the pull (case 528.1) · [[decision-case-528.1]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0248/ledger.md#L1
- 2026-10-13 updated: the Criterion replaced whole — git remote prints origin, the repository GUPPI on GitHub; /hi still runs no git pull · [[decision-case-787.2]]
