---
type: decision
case: "789"
status: current
children: ["[[decision-case-789.1]]", "[[decision-case-789.2]]", "[[decision-case-789.3]]"]
origin: raw/2026-10-12/2349/ledger.md#case-789
sprint: plugin
created: 2026-10-12
tags: [github, git, workflow, harness, sprint, session, render]
---

## Problem

No rule says how a pull request of another person into `main` is taken. The owner's closed sprint reaches `main` by a fast-forward, which refuses as soon as `main` holds another person's work.

## Recommend

- **Should this be one Case or two parts?**
  - Recommended: (a) one Case with two sub-cases: the owner's sprint reaching `main` by a pull request, and the review of another person's pull request as one Case, each with its own check.
  - Answer: agreed, (a); a third sub-case was added by the answer to the later question on where the stop on a refused merge step is written.
- **Should the owner's own sprint get a second review when its pull request goes to `main`?**
  - Recommended: (a) no second review: the opening Case pushes the closed branch, opens a pull request into `main` and merges it, then updates the local `main`, makes the new sprint branch and deletes the old one.
  - Answer: agreed, (a).
- **How should GitHub merge a pull request into `main`?**
  - Recommended: (a) a merge commit, which keeps every commit of the branch and lets `git branch -d` delete the local branch.
  - Answer: agreed, (a).
- **Should the run stop before pushing to GitHub and merging there?**
  - Recommended: (a) keep the stop: the task that pushes and merges opens with `stop:`, and Work Mode runs it after the person's word.
  - Answer: agreed, (a).
- **How should another person's pull request reach a session?**
  - Recommended: (a) the person names it by `/pr-review` and its number, in Plan Mode of any session; a new skill loads only there and sends the review to `case-guppi`.
  - Answer: agreed, (a).
- **What should the review Case show the owner before they ratify it?**
  - Recommended: (a) a summary: the CI result, the rule and entity pages the pull request creates, changes or deletes, the code files it changes, and the status of the Estimates of the author's sprint.
  - Answer: agreed, (a).
- **What should happen to a pull request made without the harness?**
  - Recommended: (a) accept it: it is reviewed like any other, the owner's review Case is its one Decision, and CI must be green.
  - Answer: agreed, (a).
- **What happens when the owner does not take the pull request?**
  - Recommended: (a) the Case is dropped and the owner asks for changes on GitHub in their own words; `/pr-review` runs again after the author updates the pull request.
  - Answer: agreed, (a).
- **Who settles a conflict between a pull request and `main`?**
  - Recommended: (a) the author: no review Case is built while GitHub shows a conflict; for the owner's sprint the opening Case first merges `main` into the closed branch, a conflict there a stop, and the Case on the vault at a sprint's close says how pages are settled.
  - Answer: agreed, (a).
- **Which page should a review Case's ratification name?**
  - Recommended: (a) the owner's current sprint page, by an `update` with one history line naming the pull request.
  - Answer: agreed, (a).
- **Who should fix the sprint check that sends pull requests into the branch `plugin`?**
  - Recommended: (a) Case 787, the Case on setting up the repository, since the check belongs to its sprint item; this Case names the clash in its `context`.
  - Answer: agreed, (a).
- **How should each part be checked?**
  - Recommended: (a) the Criterion of `estimate-skill-sprint-open-merges-the-closed-sprint-branch` replaced whole and read at this session's Retro; a new Estimate of `rule-skill-pr-review` read after a pull request from a second account is reviewed and merged.
  - Answer: agreed, (a).
- **Where should the stop on a refused merge step be written?**
  - Recommended: (a) a third sub-case rewrites the sixth condition of `vault/wiki/where-to-stop.md`: a refused or conflicting `git` or `gh` command in the merge tasks of the opening Case of a sprint or of a review Case is a stop, and the Criterion of its check is replaced whole.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed that Case 789.1 is built again to match the answer to Case 790. The opening Case of the next sprint no longer merges `main` into the closed branch and no longer opens the pull request, since another step does both before the pull request.
  - Taken: in Case 789.1 the opening Case only merges the open pull request of the closed branch, by one `stop:` task, then updates the local `main`, makes the branch `<id>` and deletes the old branch. The merge of `origin/main` into the closed branch, the push and `gh pr create` are gone, and its check is set anew. In Case 789.3 the sixth condition names a refused `git` or `gh` command of the merge tasks, and no conflict of a merge of `main`. The answers on the owner's sprint and on conflicts above stand as they were given. This change replaces only the parts of them on the opening Case.
- **Change**
  - Asked: the person said that the author settles conflicts, and that whether a pull request is taken is the owner's decision, in a separate Case. The person agreed that the review Case of `/pr-review` also shows the author's merge Case of `/merge-main`, when the branch has one: each conflicted page and the joined text that the author signed, so that the owner ratifies the pull request whole together with them.
  - Taken: in Case 789.2 the skill writes the merge Case of the branch into `pr-<n>.md` too. The review Case states each conflicted page and its joined text, and the owner ratifies them whole with the pull request. Its check names this.
- **Change**
  - Asked: the person agreed that Case 789.1 is built again to match the later answers to Case 790. The merge of `main` into a branch runs in a session of its own before the close of the sprint, then the close, then the pull request. For the owner, the `stop:` task of the opening Case of the next sprint pushes the closed branch, opens its pull request and merges it. A contributor pushes and opens the pull request after the close, and the owner reviews it by `/pr-review`.
  - Taken: in Case 789.1 the `stop:` task runs `git push -u origin <branch>`, `gh pr create --base main --head <branch> --fill` and `gh pr merge <branch> --merge`, followed by the local steps as before. Its check is set anew.
- **Change**
  - Asked: the person agreed that Case 789.3 is built again, so that the sixth condition also covers the tasks of a merge Case of `/merge-main`, as Case 790 sets them.
  - Taken: in Case 789.3 the sixth condition and the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` name the tasks of a merge Case too. A refused `git` command there is a stop, and so is a file left in conflict that the merge Case does not settle. Case 789.2 finds the merge Case by the message of its merge commit, as Case 790 sets it.
- **Change**
  - Asked: the findings of `/pre-spec`, with the person's answers.
    - The new sixth condition made any non-zero exit of `git merge --no-ff --no-commit` of a merge Case a stop, the conflicts the merge Case settles included.
    - For an author who is not the owner, the opening Case only pushes and opens the pull request when none is open, and the new branch starts from the closed branch.
    - The owner's merge waits for green checks, with no `--admin`.
    - `/sprint-open` writes a `/merge-main` line before the close line.
    - `/pr-review` has the person approve a first-time contributor's run and waits for it.
    - It looks for merge Cases only among the commits of the pull request.
    - The `method` of its check waits for the first pull request from another account merged after the close of `plugin`.
    - `/pr-review` runs no `git fetch` before a Case is ratified, as `rule-default-mode` sets it.
  - Taken: each finding is fixed in Case 789.1, 789.2 or 789.3 as asked. The refusal of `/sprint-close` while `origin/main` is not in the branch goes to Case 790.

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#case-789
