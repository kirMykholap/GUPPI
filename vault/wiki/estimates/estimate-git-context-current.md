---
type: estimate
kind: QA
status: passed
target: "[[rule-git-context]]"
purpose: At /hi the context holds the render sync, the branch and the status, and the skill runs no git pull
method: "by hand, after a /hi: the first turn's context and .claude/skills/hi/SKILL.md read against the Criterion, written into the estimate line"
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness, git]
core: true
---

## Criterion

When:
The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the commands of `rule-git-context`.

Then:
The context holds `Render:` with the output of `uv run --project .guppi guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
**－** The skill runs no `git pull`, and the context holds no `Pull:` line.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
