---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the opening Case merge the closed sprint's branch into main by a fast-forward as the first tasks of Work Mode and move the work to a branch named by the new sprint, with a stop on a refusal and no git task on main
method: by hand, at the Retro of the session of case 775, the new Render of rule-skill-sprint-open in its spec.md read against the Criterion
origin: raw/2026-10-10/2350/ledger.md#case-775.1
sprint: plugin
created: 2026-10-10
tags: [sprint, git, workflow]
---

## Criterion

When:
The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, and dispatches `case-guppi` for the opening Case of the next sprint; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

Then:
The prompt of the call names the branch that `/hi` printed under `Branch:` from `.claude/skills/hi/SKILL.md`.
**＋** When that branch is not `main`, the opening Case holds as its first tasks `git switch main`, `git merge --ff-only <branch>`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint.
**＋** Work Mode runs these tasks before any other task of the Spec: `main` moves to the last commit of the closed sprint's branch with no merge commit, that branch is deleted, and the rest of Work Mode runs on the branch `<id>`.
**－** When `git merge --ff-only` or `git branch -d` refuses, the agent stops on the sixth condition of `vault/wiki/where-to-stop.md`, shows the refusal, and goes on from where it stopped after the person's answer.
**－** When that branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it.
**－** The opening Case puts no question on the merge or the branch to the person.

## Result

2026-10-11, Retro of session 2350, by hand: the new Render of rule-skill-sprint-open in spec.md (case 775.1) against each line of the Criterion — the prompt of the case-guppi call names the Branch: of /hi; off main the opening Case holds git switch main, git merge --ff-only <branch>, git switch -c <id>, git branch -d <branch> as its first tasks, run first since the Spec holds the opening Case first; a refusal is a stop on the sixth condition; on main no git task and Work Mode stops; no question on the merge or the branch

## History

- 2026-10-11 created · [[decision-case-775.1]]
- 2026-10-11 status: pending → passed · raw/2026-10-10/2350/ledger.md#L10
