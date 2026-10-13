---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-pr-review]]"
purpose: Whether /pr-review has a pull request into main reviewed as one Case on the facts of gh and git, the conflicted pages and joined texts of the author's merge Case of /merge-main among them when the branch holds one, ratified whole by the owner and merged with a merge commit after the person's word, with no review Case for a pull request in conflict or with a red check
method: "by hand, after the first pull request from an account other than the owner's is merged into main by /pr-review after the close of plugin: the review Case in its case file, its decision line, pr-<n>.md and the pull request on GitHub read against the Criterion"
origin: raw/2026-10-12/2349/ledger.md#case-789.2
sprint: plugin
created: 2026-10-12
tags: [github, git, workflow]
---

## Criterion

When:
The person types `/pr-review <n>` on `UserPromptSubmit` in Plan Mode, or the main agent calls it on `PreToolUse Skill`, for the pull request `<n>` into `main` of the repository on GitHub, `.claude/skills/pr-review/SKILL.md` rendered from `rule-skill-pr-review`; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

Then:
The main agent runs `gh pr view` and `gh pr checks` on the pull request, has the person approve a run of the checks that waits for the owner's approval and waits until the checks end, reads by `gh api` at the head commit of the pull request the `status` of each Estimate page it adds or changes, with no `git fetch`, writes that output into `raw/<date>/<hi HHMM>/pr-<n>.md`, and dispatches `case-guppi` for the review Case with that path in the prompt.
**＋** The `context` of the review Case states, from `raw/<date>/<hi HHMM>/pr-<n>.md`, the result of each CI check, the rule and entity pages the pull request creates, changes or deletes, the code files it changes and the `status` of each Estimate page it adds or changes, and names them as what checks it.
**＋** When a commit of the pull request, none that `main` already holds, names a merge Case of `/merge-main`, `raw/<date>/<hi HHMM>/pr-<n>.md` holds that Case too, and the review Case shows each conflicted page and the joined text that the author signed, which the owner ratifies whole with the pull request.
**＋** The review Case holds one decision line, an `update` of the live sprint page `entity-sprint-<id>` with only a `change` that names the pull request, and one task, which opens with `stop:` and runs `gh pr merge <n> --merge`.
**＋** Once the person ratifies the review Case, Work Mode stops before that task, runs it on the branch of the session after the person's word, and `main` on GitHub takes the pull request with a merge commit.
**－** When the base of the pull request is not `main`, GitHub shows a conflict with `main`, or a CI check is not green, no review Case is built: the main agent tells the person why, and the author updates the pull request.
**－** The review Case judges the pull request whole: no decision of its author is reviewed one by one.
**－** A pull request whose branch holds no session of the harness is reviewed the same way, and the review Case is its one Decision.
**－** When the person drops the review Case, nothing is merged, the agent writes nothing to GitHub, and the person asks the author for changes on GitHub.

## History

- 2026-10-13 created · [[decision-case-789.2]]
