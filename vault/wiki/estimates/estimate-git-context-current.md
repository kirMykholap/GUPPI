---
type: estimate
kind: QA
status: passed
target: "[[rule-git-context]]"
purpose: At /hi the context holds the render sync, the branch and the status, and the skill runs no git pull
method: "by hand, after the first /hi that follows the first push to GitHub: the first turn's context, the output of git remote -v and .claude/skills/hi/SKILL.md read against the Criterion, written into the estimate line"
checked: 2026-10-13
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness, git]
---

## Criterion

When:
The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the commands of `rule-git-context`.

Then:
The context holds `Render:` with the output of `uv run --project .guppi guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
**＋** `git remote -v` prints `origin` with the URL of the repository `GUPPI` on GitHub.
**－** The skill runs no `git pull`, and the context holds no `Pull:` line.

## Result

2026-10-13, Work Mode of session 1426, the first /hi after the first push to GitHub (session 2349): the first turn's context holds Render: (no output), Branch: plugin, Status: (no output); `git remote -v` prints origin https://github.com/kirMykholap/GUPPI.git (fetch) and (push); .claude/skills/hi/SKILL.md holds Render:, Branch:, Status: in the rule-git-context markers and no `git pull` and no `Pull:`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-14 criterion: case 115 added · [[decision-case-115]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L1
- 2026-09-28 updated: the Criterion replaced whole — one When and Then; the Frontier item left to estimate-hi-writes-frontier, the block bookkeeping out; purpose and method set, Context and Method out (case 485.3) · [[decision-case-485.3]]
- 2026-09-30 updated: the Criterion replaced whole — no Pull line, no git pull, no remote; the promise on a pull mid-session gone with the pull (case 528.1) · [[decision-case-528.1]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0248/ledger.md#L1
- 2026-10-13 updated: the Criterion replaced whole — git remote prints origin, the repository GUPPI on GitHub; /hi still runs no git pull · [[decision-case-787.2]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1426/ledger.md#L23
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
