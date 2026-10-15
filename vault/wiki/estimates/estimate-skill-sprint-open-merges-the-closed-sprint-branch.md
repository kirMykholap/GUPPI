---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the opening Case name /merge-main before the close line, push the closed sprint's branch and open its pull request into main after the person's word, merge it with a merge commit after its checks pass when the person is the owner, and move the work to a branch named by the new sprint, as the first tasks of Work Mode, with a stop on a refusal and no git task on main
method: by hand, at the Retro of the session whose Spec set the new Render of rule-skill-sprint-open that the Criterion describes, that Render in its spec.md read against the Criterion (the session of case 789)
checked: 2026-10-13
origin: raw/2026-10-10/2350/ledger.md#case-775.1
sprint: plugin
created: 2026-10-10
tags: [sprint, git, workflow]
---

## Criterion

When:
The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, and dispatches `case-guppi` for the opening Case of the next sprint; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

Then:
The prompt of the call names the branch that `/hi` printed under `Branch:` from `.claude/skills/hi/SKILL.md`, and whether the person is the owner of the repository: the login that `gh api user --jq .login` prints is the one that `gh repo view --json owner --jq .owner.login` prints.
**＋** The opening Case writes into the last milestone of `entity-sprint-<id>`, just before the close line of `/sprint-close`, the line ``- the merge of `main` into `<id>` — `/merge-main`, a session of its own``.
**＋** When that branch is not `main` and the person is the owner, the opening Case holds as its first tasks, in this order, one task that opens with `stop:` and runs `git push -u origin <branch>`, `gh pr create --base main --fill`, `gh pr checks <branch> --watch` and `gh pr merge <branch> --merge`; then `git fetch origin`, `git switch main`, `git merge --ff-only origin/main`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint.
**＋** When that branch is not `main` and the person is not the owner, the opening Case holds as its first tasks one task that opens with `stop:` and runs `git push -u origin <branch>` and, when `gh pr view <branch>` shows no open pull request, `gh pr create --base main --fill`; then `git switch -c <id>` and `git branch -d <branch>`, so that the branch `<id>` starts from the closed branch and keeps its work until the owner merges it by `/pr-review`.
**＋** Work Mode runs these tasks before any other task of the Spec, stops before the task that opens with `stop:`, on the fourth condition of `vault/wiki/where-to-stop.md`, runs it after the person's word, and runs the rest of the Spec on the branch `<id>`.
**－** The owner's pull request is merged only after its checks pass, with a merge commit and never with `--admin`, and no Case reviews it: each of its changes was ratified in its own session.
**－** The opening Case does not merge `main` into the closed branch.
**－** When a `git` or `gh` command of these tasks refuses, among them `gh pr checks --watch` on a red check and `gh pr merge` on a pull request that cannot be merged, the agent stops on the sixth condition of `vault/wiki/where-to-stop.md`, shows what stopped it, and goes on from where it stopped after the person's answer.
**－** When that branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it.
**－** The opening Case puts no question on the merge or the branch to the person.

## Result

2026-10-13, Retro by hand: the Render of rule-skill-sprint-open in spec.md (case 789.1) names the owner by gh api user against gh repo view, writes the /merge-main line before the close line, holds the stop: task with push, pr create, pr checks --watch and pr merge --merge for the owner and push and pr create for an author, then fetch, ff-only from origin/main, the new branch and the deletion; no merge of main into the closed branch; a refusal is the sixth stop

## History

- 2026-10-11 created · [[decision-case-775.1]]
- 2026-10-11 status: pending → passed · raw/2026-10-10/2350/ledger.md#L10
- 2026-10-13 updated: the Criterion replaced whole — the opening Case pushes the closed sprint and opens its pull request; the owner's is merged after its checks pass; /merge-main stands before the close line · [[decision-case-789.1]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L54
- 2026-10-15 updated: the pointer of the method stands in a bracket at its end · [[decision-case-823.1]]
