---
type: rule
kind: Leaf
purpose: Prevents the next sprint from opening without a goal, a Definition of done, a first milestone, its close line and a look at the backlog, while the text that asks for them stays out of the sessions that open no sprint
status: built
enforcement: render
implementation_ref: [guppi/sprint.py, tests/test_sprint.py, .claude/settings.json]
governs: .claude/skills/sprint-open/SKILL.md
render_mode: full
parent: "[[rule-session-start]]"
estimates: ["[[estimate-skill-sprint-open-asks-the-opening-questions]]", "[[estimate-skill-sprint-open-starts-at-hi]]", "[[estimate-skill-sprint-open-merges-the-closed-sprint-branch]]", "[[estimate-skill-sprint-open-refuses-a-taken-sprint-id]]"]
origin: raw/2026-10-08/2352/ledger.md#case-743.6
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, harness]
core: true
---

## Purpose

Prevents the next sprint from opening without a goal, a Definition of done, a first milestone, its close line and a look at the backlog, while the text that asks for them stays out of the sessions that open no sprint. The skill sets what the opening Case asks, apart from `orchestration.md`, which every session loads (until case 743 nothing set it, and the steps of the turn of a sprint stood in `orchestration.md`). The skill loads only in the session that opens a sprint: the `UserPromptSubmit` hook `guppi sprint --hi` tells the agent at `/hi` to start it when `vault/wiki/sprint.md` marks the last sprint closed, as [[rule-sprint]] sets it (case 743.5), and the person may type it too. The backlog is not gone through: the opening Case says how many items it holds and asks whether to take any (case 743.6). The close line it writes starts [[rule-skill-sprint-close]] in the session that closes the sprint.

## Render

<!-- rule-skill-sprint-open -->
---
name: sprint-open
description: "Open the next sprint. Run it when the hook on /hi says that no sprint is open, or when the person types /sprint-open."
---

No sprint is open: the first heading of `vault/wiki/sprint.md` marks the last sprint closed. This session opens the next one. The ledger hook refuses each decision line but a `defer` until a `create` of a page `entity-sprint-<id>` stands, so the opening Case is the first Case the session ratifies. It also refuses that `create` when a live or archived sprint page already holds the id: ask the person for another id, and send the opening Case back to its `case-guppi` to be built again under it (case 788.1).

1. Assemble no Frontier yet: the opening Case comes first, and no other item of the session is taken up before the person ratifies it (case 769.1).
2. Ask the person first, in one plain question, for the id of the sprint, which names the page `entity-sprint-<id>`, the branch of the sprint and every Case id of the sprint: it starts with the GitHub name of its author, such as `kir-plugin`, and holds lower-case letters, digits and hyphens and no dot. Then dispatch `case-guppi` at once for the line `open the next sprint` of the brief, as `vault/wiki/orchestration.md` sets it, with the Case id `<id>-1` and the id of the sprint, and write into the prompt of the call that the opening Case asks the person, in its rounds (case 788.3):
   - its goal in one sentence, the `purpose` and the `## Purpose` of the page;
   - its Definition of done, one Estimate per condition, which the page lists in `estimates`;
   - the first milestone and its items, under `## Milestones`;
   - whether to take any item of `vault/wiki/backlog.md` into the sprint: the Case says how many items the file holds, and goes through no item the person does not name.
3. Write into the same prompt that the opening Case writes, as the last two items of the last milestone of the page, the line ``- the merge of `main` into `<id>` — `/merge-main`, a session of its own`` and then the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that `/merge-main` runs before the close (case 789.1) and the session that closes the sprint starts `/sprint-close` from the close line.
4. Write into the same prompt the branch that `/hi` printed under `Branch:`, and whether the person is the owner of the repository: the login that `gh api user --jq .login` prints is the one that `gh repo view --json owner --jq .owner.login` prints. When the branch is not `main`, the closed sprint ran on it, and the opening Case holds as its first task lines, in this order, `<id>` the id of the new sprint:
   - for the owner, one task line that opens with `stop:` and runs `git push -u origin <branch>`, `gh pr create --base main --fill`, `gh pr checks <branch> --watch` and `gh pr merge <branch> --merge`, which push the closed branch, open its pull request into `main`, wait until its checks pass and merge it with a merge commit, never with `--admin`; then `git fetch origin`, `git switch main`, `git merge --ff-only origin/main`, `git switch -c <id>` and `git branch -d <branch>`, so that the local `main` follows `origin/main`; no Case reviews this pull request, since each change of the closed sprint was ratified in its own session;
   - for an author who is not the owner, one task line that opens with `stop:` and runs `git push -u origin <branch>` and, when `gh pr view <branch>` shows no open pull request, `gh pr create --base main --fill`; then `git switch -c <id>` and `git branch -d <branch>`, so that the branch `<id>` starts from the closed branch and keeps its work until the owner merges the pull request by `/pr-review`.

   The Spec holds the opening Case first, so Work Mode runs them before any other task, and the rest of Work Mode runs on the branch `<id>`. Work Mode stops before the task line that opens with `stop:` and runs it after the person's word. The opening Case does not merge `main` into the closed branch: `/merge-main` did so before the close (case 789.1). A refusal of a `git` or `gh` command of these tasks, `gh pr checks --watch` on a red check and `gh pr merge` on a pull request that cannot be merged among them, is a stop on the sixth condition of `vault/wiki/where-to-stop.md`. When the branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it. The opening Case puts no question on the merge or the branch to the person (case 775.1).
5. The skill decides none of the answers: the main agent asks the person for the id, and `case-guppi` puts each other question to the person, and the person ratifies the opening Case as any other. Before the reply that acknowledges it, assemble and write the Frontier as `/hi` sets it, the items of the first milestone of the opening Case among its Cases; that reply shows it, as `vault/wiki/orchestration.md` sets that reply (case 769.4).
<!-- /rule-skill-sprint-open -->

## History

- 2026-10-09 created · [[decision-case-743.6]]
- 2026-10-09 estimate estimate-skill-sprint-open-asks-the-opening-questions added · [[decision-case-743.6]]
- 2026-10-09 estimate estimate-skill-sprint-open-starts-at-hi added · [[decision-case-743.7]]
- 2026-10-09 updated: the parent is rule-session-start, as case 743.6 set it (case 746.1) · [[decision-case-746.1]]
- 2026-10-09 status: draft → built · cascade
- 2026-10-10 updated: the opening Case comes before any Frontier, and the reply that acknowledges it brings the Frontier (case 769.1) · [[decision-case-769.1]]
- 2026-10-10 deferred · [[decision-case-771]]
- 2026-10-11 defer by decision-case-771 superseded · [[decision-case-775.1]]
- 2026-10-11 updated: the opening Case of a sprint merges the closed sprint's branch into main by a fast-forward and moves the work to a branch named by the new sprint · [[decision-case-775.1]]
- 2026-10-11 estimate estimate-skill-sprint-open-merges-the-closed-sprint-branch added · [[decision-case-775.1]]
- 2026-10-13 updated: the ledger hook refuses the create of a sprint page whose id a live or archived sprint page holds, and the opening Case is built again under another id (case 788.1) · [[decision-case-788.1]]
- 2026-10-13 estimate estimate-skill-sprint-open-refuses-a-taken-sprint-id added · [[decision-case-788.1]]
- 2026-10-13 updated: the opening Case of a sprint pushes the closed sprint and opens its pull request into main; for the owner it merges it after its checks pass; the last milestone names /merge-main before the close · [[decision-case-789.1]]
- 2026-10-13 updated: the main agent asks the sprint id before the dispatch, and the opening Case is Case <id>-1 (case 788.3) · [[decision-case-788.3]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: each pointer stands in a bracket of its own, the link to rule-sprint outside it · [[decision-case-809]]
