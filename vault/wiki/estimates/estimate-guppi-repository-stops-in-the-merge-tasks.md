---
type: estimate
kind: QA
status: passed
target: "[[entity-guppi-repository]]"
purpose: Whether the run stops for the person when a git or gh command of the merge tasks of pr-review or merge-main refuses, or when a merge leaves in conflict a file that its merge Case does not settle, and on no refusal of a merge whose conflicts the merge Case settles
method: "by hand: vault/wiki/where-to-stop.md as rendered and the merge tasks that .claude/skills/pr-review/SKILL.md and .claude/skills/merge-main/SKILL.md set, read against the Criterion, written into the estimate line"
origin: raw/2026-10-17/1805/ledger.md#case-880.20
sprint: plugin
created: 2026-10-17
tags: [session, workflow, git]
---

## Criterion

When:
In the repository of GUPPI, with `vault/wiki/where-to-stop.md` rendered from `rule-where-to-stop`, the agent runs the merge task that a review Case holds by `.claude/skills/pr-review/SKILL.md`, or the tasks that a merge Case holds by `.claude/skills/merge-main/SKILL.md`.

Then:
The agent stops, shows what stopped it and asks when a `git` or `gh` command refuses, or when the merge of a merge Case leaves in conflict a file that the merge Case does not settle.
**－** `git merge --no-ff --no-commit` of a merge Case of `.claude/skills/merge-main/SKILL.md` that exits non-zero only on files that the merge Case settles is no refusal, and the run goes on to the tasks that settle them.

## Result

2026-10-17, Retro of session 1805: condition 6 of vault/wiki/where-to-stop.md stops on a refusing git or gh command of the merge task of a review Case of /pr-review and of the tasks of a merge Case of /merge-main, and on a conflict the merge Case does not settle, and takes a git merge --no-ff --no-commit that exits non-zero only on files the merge Case settles for no refusal; .claude/skills/pr-review/SKILL.md holds the merge task gh pr merge, .claude/skills/merge-main/SKILL.md the tasks git fetch origin and git merge --no-ff --no-commit

## History

- 2026-10-17 created · [[decision-case-880.20]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L77
