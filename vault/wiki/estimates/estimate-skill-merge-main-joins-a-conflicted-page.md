---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-merge-main]]"
purpose: Whether /merge-main merges main into the branch of an open sprint as one merge Case, writes again the files a command writes, keeps both sides of the files that only gain lines, and writes the joined text the person signed into each other conflicted file
method: "by hand, after the first /merge-main whose merge of main leaves a conflicted page: its merge.md, the merge Case in its case file, its decision lines, the merge commit, the joined pages and the Render of rule-skill-merge-main read against the Criterion"
origin: raw/2026-10-12/2349/ledger.md#case-790
sprint: plugin
created: 2026-10-12
tags: [git, workflow, sprint]
---

## Criterion

When:
The person types `/merge-main` on `UserPromptSubmit` in Plan Mode, or the main agent calls it on `PreToolUse Skill`, in a session on the branch of an open sprint, `.claude/skills/merge-main/SKILL.md` rendered from `rule-skill-merge-main`; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

Then:
Writing nothing into the tree or into `.git` and running no `git fetch`, the main agent reads by `gh api` the commit of `main` on GitHub and the files that `main` changed since the last commit of `main` that the branch holds, and by `git` the files that the branch changed. It writes that output and the text on both sides of each file that both sides changed into `raw/<date>/<hi HHMM>/merge.md`, and dispatches `case-guppi` for the merge Case with that path.
**＋** The merge Case is the one Case of the session; its tasks run `git fetch origin`, merge the commit of `main` that the session read into the branch, and commit the merge with a message that names the Case.
**＋** Each conflicted file that a command writes takes the text of `main` and is written again by `uv run --project .guppi guppi render`, `uv run --project .guppi guppi glossary`, `uv run --project .guppi guppi sprint` or `uv run --project .guppi guppi backlog`, and `vault/wiki/brief.md` by the librarian; git keeps the lines of both sides of `vault/wiki/log.md` and `vault/wiki/tags.md` by their `merge=union` lines in `.gitattributes`.
**＋** For each other file that both sides changed, the merge Case shows its text on the branch and on `main` and holds the joined text that the person signs or corrects; Work Mode writes that text into the file, and runs `git add` on each such path before the commit.
**＋** Its decision lines update the live sprint page `entity-sprint-<id>` with only a `change` that names the merge, and each joined page under `vault/wiki/` with only a `change`; each Estimate whose Criterion speaks of a joined text is set `pending` by a sub-case of its own, whose `when` and `then` are that Criterion; the librarian writes no other text of a joined page.
**＋** `rule-page-generation`, `rule-vault-layout`, `rule-documentation`, `entity-glossary`, `.claude/agents/librarian-guppi.md` and `vault/wiki/glossary.md` name that joined text, and the lines of `log.md` and `tags.md` that git joins, as what a merge of `main` writes into `vault/wiki/` besides the script.
**＋** `.claude/skills/merge-main/SKILL.md` says that the pull request into `main` follows `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, and that another person runs `git push` and `gh pr create --base main` after the close, for the owner to review by `/pr-review` of `.claude/skills/pr-review/SKILL.md`.
**－** With no file that both sides changed, the update of the sprint page is the one decision line of the merge Case.
**－** When the branch is `main`, when the first heading of `vault/wiki/sprint.md` marks the last sprint closed, or when the branch already holds `origin/main`, no Case is built and nothing is merged; the main agent tells the person why.
**－** The merge Case archives nothing: what goes to the archive is what `/sprint-close` of `.claude/skills/sprint-close/SKILL.md` moves.

## History

- 2026-10-13 created · [[decision-case-790]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
