---
type: rule
kind: Leaf
purpose: Prevents a sprint branch from reaching main with a conflict its author did not settle, or with a joined text the person did not sign
status: draft
enforcement: render
governs: .claude/skills/merge-main/SKILL.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-skill-merge-main-joins-a-conflicted-page]]"]
origin: raw/2026-10-12/2349/ledger.md#case-790
sprint: plugin
created: 2026-10-12
tags: [git, workflow, sprint, harness]
---

## Purpose

Prevents a sprint branch from reaching `main` with a conflict its author did not settle, or with a joined text the person did not sign. Others clone the project and run a sprint on their own branch, and each branch carries its own copy of `vault/`. When a branch and `main` changed one page, git stops on a conflict, and the author of the branch settles it (case 790). The author runs `/merge-main` in a session of its own, after the work of the sprint and before `/sprint-close`, while the sprint page is live. The ledger then takes the lines of the merge Case, and the close settles each check that the merge Case set `pending`. Files that a command writes are written again rather than joined, and git keeps both sides of `log.md` and `tags.md`, which only gain lines. Every other conflicted file takes a joined text that the person signs in the merge Case and Work Mode writes. These are what a merge of `main` writes into `vault/wiki/` besides the script ([[rule-page-generation]], [[rule-vault-layout]]). The close archives what it archived before ([[rule-sprint-close]]). The pull request follows the close: for the owner's sprint the opening Case of the next sprint opens and merges it ([[rule-skill-sprint-open]]), and the owner reviews the pull request of another person by `/pr-review`.

## Render

<!-- rule-skill-merge-main -->
---
name: merge-main
description: "Merge main into the branch of the open sprint as one merge Case, before the close of the sprint. Run it when the person types /merge-main."
---

This session merges `origin/main` into the branch of the open sprint, after the work of the sprint and before `/sprint-close`, so that the pull request of the closed sprint reaches `main` with no conflict. The merge Case is the one Case of this session (case 790).

1. When `/hi` printed `main` under `Branch:`, or the first heading of `vault/wiki/sprint.md` marks the last sprint closed, build no Case and merge nothing: tell the person that `/merge-main` runs on the branch of an open sprint, before its close.
2. Until the merge Case is ratified, only read: write nothing into the tree or into `.git`, so run no `git fetch` (`rule-default-mode`). `gh api repos/{owner}/{repo}/commits/main --jq .sha` prints `<hash>`, the commit of `main` on GitHub. When `git merge-base --is-ancestor <hash> HEAD` exits 0, the branch already holds `main`: build no Case, and tell the person so.
3. `git merge-base HEAD origin/main` prints `<base>`, the last commit of `main` that the branch holds. `gh api repos/{owner}/{repo}/compare/<base>...<hash> --jq '.files[].filename'` names each file that `main` changed since, and `git diff --name-only <base> HEAD` each file that the branch changed. Write the output of these commands, as they printed it, into `raw/<date>/<hi HHMM>/merge.md`. Under it, for each file that both lists name and that the terms below do not settle by a command or by git, write its text on this branch by `git show HEAD:<path>` and on `main` by `gh api "repos/{owner}/{repo}/contents/<path>?ref=<hash>" -H "Accept: application/vnd.github.raw"`.
4. Dispatch `case-guppi` for the merge Case as `vault/wiki/orchestration.md` sets it, with the path of that file in the prompt and these terms:
   - its first tasks run `git fetch origin` and `git merge --no-ff --no-commit <hash>`, so that Work Mode merges the commit this session read, and its last task runs `git commit -m "merge: main <hash> into <branch> — case N"`;
   - each file that a command writes — a file that a live rule page names in `governs`, `vault/wiki/glossary.md`, `vault/wiki/sprint.md`, `vault/wiki/backlog.md` and `vault/wiki/brief.md` — takes the text of `main` by `git checkout --theirs -- <path>` when git leaves it in conflict; the tasks `uv run guppi render`, `uv run guppi glossary`, `uv run guppi sprint` and `uv run guppi backlog` write them again, and the librarian of the session writes `brief.md` again;
   - `vault/wiki/log.md` and `vault/wiki/tags.md` are joined by git itself, by their `merge=union` lines in `.gitattributes`, which keep the lines of both sides; no task writes them;
   - for each other file that both sides changed, a page or code, the Case shows its text on the branch and on `main` from `merge.md`, and holds one task that writes the joined text into the file, the text as a sub-point; the person signs or corrects that text, and Work Mode writes it into the file itself, whether or not git left the file in conflict;
   - after the tasks that settle these files, one task runs `git add` on each of their paths, so that no path stands unmerged before the commit;
   - its decision lines are an `update` of the live sprint page `entity-sprint-<id>` with only a `change` that names the merge and `<hash>`, and an `update` with only a `change` of each joined page under `vault/wiki/`;
   - each Estimate whose Criterion speaks of a joined text is set `pending` by a sub-case of its own: its `when` and `then` are that Criterion as the page holds it, and its one decision line is an `update` of the Estimate with `set: {status: pending}`, so that each sub-case holds one promise;
   - with no file that both sides changed, the `update` of the sprint page is its one decision line;
   - the merge Case archives nothing: what goes to the archive is what `/sprint-close` moves.
5. The person ratifies the merge Case as any other. Work Mode runs its tasks, and the full test run of `/work` runs over the merged code. The librarian writes the Decision page, the History lines and the statuses set `pending`, and no other text of a joined page. The joined texts of the conflicted pages, and the lines of `log.md` and `tags.md` that git joins, are what a merge of `main` writes into `vault/wiki/` besides the script.
6. The pull request into `main` follows `/sprint-close`, so that it holds the whole closed sprint. For the owner's sprint, the opening Case of the next sprint opens and merges it, as `.claude/skills/sprint-open/SKILL.md` sets it. Another person runs `git push` and `gh pr create --base main` after the close, and the owner reviews it by `/pr-review`.
<!-- /rule-skill-merge-main -->

## History

- 2026-10-13 created · [[decision-case-790]]
- 2026-10-13 estimate estimate-skill-merge-main-joins-a-conflicted-page added · [[decision-case-790]]
