---
type: rule
kind: Leaf
purpose: Prevents a pull request into main from being merged without one Case that the owner ratified whole, or its review from judging each decision of its author again
status: draft
enforcement: render
governs: .claude/skills/pr-review/SKILL.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-skill-pr-review-takes-a-pull-request-whole]]"]
origin: raw/2026-10-12/2349/ledger.md#case-789.2
sprint: plugin
created: 2026-10-12
tags: [github, git, workflow, harness]
---

## Purpose

Prevents a pull request into main from being merged without one Case that the owner ratified whole, or its review from judging each decision of its author again. Others clone the project, run a sprint on their own branch with the harness and open a pull request of the whole branch into `main`; only the owner merges into `main`. Each decision on that branch was made by its author, and the owner does not ratify them one by one: the owner ratifies the pull request whole, in one review Case, which is the Decision of the pull request in the owner's vault (case 789.2). The skill loads only in the session that reviews a pull request, and the person starts it by the number of the pull request. The owner's own closed sprint reaches `main` by a pull request too, but through the opening Case of [[rule-skill-sprint-open]], with no review Case, since each of its changes was ratified in its own session (case 789.1).

## Render

<!-- rule-skill-pr-review -->
---
name: pr-review
description: "Review a pull request into main as one Case the owner ratifies whole. Run it when the person types /pr-review with the number of the pull request."
---

The person asks to review the pull request `$ARGUMENTS`, called `<n>` below, into `main` of the repository on GitHub. Its review is one Case of Plan Mode: the owner ratifies the pull request whole or drops it, and no decision of its author is reviewed one by one. The pull request is an item of the person in `frontier.md`, closed as `vault/wiki/orchestration.md` sets it.

1. Run `gh pr view <n> --json number,title,author,baseRefName,headRefName,headRefOid,mergeable,files,commits` and `gh pr checks <n>`. When a run of the checks waits for the owner's approval, as the run of a first-time contributor does, tell the person to approve it on GitHub, then run `gh pr checks <n> --watch` until the checks end. When the base is not `main`, when `mergeable` is `CONFLICTING`, or when a check is not green once the checks end, build no Case: tell the person why and that the author updates the pull request, and close its line `[x] … · work`.
2. Read the branch on GitHub, at the commit `headRefOid`, with no `git fetch`, so that nothing is written in the repository before a Case is ratified. For each path under `vault/wiki/estimates/` that `files` names, run `gh api -H "Accept: application/vnd.github.raw" "repos/{owner}/{repo}/contents/<path>?ref=<headRefOid>"`, for its `status`. Among `commits`, which holds only the commits of the pull request and none that `main` already holds, a commit whose headline opens with `merge: main` names, by `case N` at its end, a merge Case of `/merge-main`. That Case records each page that conflicted when the author merged `main` into the branch, and the joined text the author signed. Find the file `case-<N>.md` of that Case among the paths that `gh api "repos/{owner}/{repo}/git/trees/<headRefOid>?recursive=1" --jq '.tree[].path'` prints, under `vault/raw/` or `vault/archive/`, and read it by the same `contents` call.
3. Write the output of these commands, as they printed it, into `raw/<date>/<hi HHMM>/pr-<n>.md`, and dispatch `case-guppi` for the review Case as `vault/wiki/orchestration.md` sets it, with the path of that file in the prompt and these terms:
   - the `context` states, from that file, the result of each check, the rule and entity pages the pull request creates, changes or deletes, the code files it changes, and the `status` of each Estimate page it adds or changes, and names the checks and these Estimates as what checks the Case, which creates no Estimate;
   - when that file holds a merge Case of `/merge-main`, the review Case shows each conflicted page and the joined text the author signed, and the owner ratifies them whole with the pull request: the author settles the conflicts, and the owner decides whether the pull request is taken;
   - the Case judges the pull request whole and reviews no decision of its author one by one;
   - a pull request whose branch holds no session of the harness is reviewed the same way, and the review Case is its one Decision;
   - its one decision line is an `update` of the page `entity-sprint-<id>` of the live sprint, with only a `change` that names the pull request by its number;
   - its one task opens with `stop:` and runs `gh pr merge <n> --merge`: Work Mode stops before it, on the fourth condition of `vault/wiki/where-to-stop.md`, and runs it on the branch of the session after the person's word, so that `main` takes the pull request with a merge commit; a refusal is a stop on the sixth condition.
4. The person ratifies the review Case as any other, or drops it. On a drop nothing is merged and the agent writes nothing to GitHub: the person asks the author for changes on GitHub in their own words, and types `/pr-review <n>` again once the author has updated the pull request.
<!-- /rule-skill-pr-review -->

## History

- 2026-10-13 created · [[decision-case-789.2]]
- 2026-10-13 estimate estimate-skill-pr-review-takes-a-pull-request-whole added · [[decision-case-789.2]]
