---
type: rule
kind: Leaf
purpose: Prevents the next sprint from opening without a goal, a Definition of done, a first milestone, its close line and a look at the backlog, while the text that asks for them stays out of the sessions that open no sprint
status: built
enforcement: render
implementation_ref: [.guppi/guppi/sprint.py, .guppi/tests/test_sprint.py, .claude/settings.json]
governs: .claude/skills/sprint-open/SKILL.md
render_mode: full
parent: "[[rule-session-start]]"
estimates: ["[[estimate-skill-sprint-open-asks-the-opening-questions]]", "[[estimate-skill-sprint-open-starts-at-hi]]", "[[estimate-skill-sprint-open-merges-the-closed-sprint-branch]]", "[[estimate-skill-sprint-open-refuses-a-taken-sprint-id]]", "[[estimate-skill-sprint-open-asks-the-goal-as-an-open-question]]"]
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [sprint, workflow, harness]
core: true
---

## Purpose

Prevents the next sprint from opening without a goal, a Definition of done, a first milestone, its close line and a look at the backlog, while the text that asks for them stays out of the sessions that open no sprint. The skill sets what the opening Case asks, apart from `orchestration.md`, which every session loads. The skill loads only in the session that opens a sprint: the `UserPromptSubmit` hook `guppi sprint --hi` tells the agent at `/hi` to start it when `vault/wiki/sprint.md` marks the last sprint closed, as [[rule-sprint]] sets it, and the person may type it too. The sprint is built from the person's own account of the work, asked before anything else, and the main agent proposes the id from it. The backlog is not gone through: the opening Case says how many items it holds and asks whether to take any. The close line it writes starts [[rule-skill-sprint-close]] in the session that closes the sprint.

## Render

<!-- rule-skill-sprint-open -->
---
name: sprint-open
description: "Open the next sprint. Run it when the hook on /hi says that no sprint is open, or when the person types /sprint-open."
---

No sprint is open: the first heading of `vault/wiki/sprint.md` marks the last sprint closed. This session opens the next one. The ledger hook refuses each decision line but a `defer` until a `create` of a page `entity-sprint-<id>` stands, so the opening Case is the first Case the session ratifies, but for the setup Case of `rule-morph`: while `guppi.toml` holds `setup_done = false`, `/setup` builds that Case first, the ledger hook writes its lines, and the reply that acknowledges it asks the person the open question on what the sprint is to build, which this skill then takes as answered and does not ask again. It also refuses that `create` when a live or archived sprint page already holds the id: ask the person for another id, and send the opening Case back to its `case-guppi` to be built again under it.

1. Assemble no Frontier yet: the opening Case comes first, and no other item of the session is taken up before the person ratifies it.
2. Ask the person first, in one plain question with no options, what they want to build in this sprint, how they see it and what should happen; where the reply that acknowledges the setup Case of `rule-morph` asked that question in this session, take the person's answer to it and do not ask it again. Right after the answer, propose in one plain question an id of the sprint worded from the answer, which the person confirms or replaces with another; the id names the page `entity-sprint-<id>`, the branch of the sprint and every Case id of the sprint, starts with the GitHub name of its author that `gh api user --jq .login` prints, such as `kir-plugin`, and holds lower-case letters, digits and hyphens and no dot. Then dispatch `case-guppi` at once for the line `open the next sprint` of the brief, as `vault/wiki/orchestration.md` sets it, with the Case id `<id>-1`, the id of the sprint and the person's answer to the first question word for word, and write into the prompt of the call that the opening Case builds the sprint from that answer and asks the person, in its rounds, only what the answer leaves open:
   - its goal in one sentence, the `purpose` and the `## Purpose` of the page, which the opening Case words from the person's answer alone and puts to the person in no question of its rounds, since the person corrects it at the showing of the Case; no word of it comes from the vault or from the description of the project that `CLAUDE.md` holds;
   - its Definition of done, one Estimate per condition, which the page lists in `estimates`;
   - the first milestone and its items, under `## Milestones`;
   - whether to take any item of `vault/wiki/backlog.md` into the sprint: the Case says how many items the file holds, and goes through no item the person does not name.
3. Write into the same prompt that the opening Case writes, as the last item of the last milestone of the page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that the session that closes the sprint starts `/sprint-close` from the close line. Where `.claude/skills/merge-main/SKILL.md` stands in the project, write that the opening Case puts the line ``- the merge of `{{main_branch}}` into `<id>` — `/merge-main`, a session of its own`` just before the close line, so that `/merge-main` runs before the close.
4. The main branch of this project is `{{main_branch}}`, but in a session that ratified the setup Case of `rule-morph` it is the name that the `update` of `rule-guppi-config` of that Case sets, since `guppi.toml` and this skill take that name only at the librarian's run of the session; where this step names `{{main_branch}}`, it means the main branch so found. Write into the same prompt that name, the branch that `/hi` printed under `Branch:`, and whether the person is the owner of the repository: the login that `gh api user --jq .login` prints is the one that `gh repo view --json owner --jq .owner.login` prints. When the branch is not `{{main_branch}}`, the closed sprint ran on it, and the opening Case holds as its first task lines, in this order, `<id>` the id of the new sprint:
   - for the owner, one task line that opens with `stop:` and runs `git push -u origin <branch>`, `gh pr create --base {{main_branch}} --fill`, `gh pr checks <branch> --watch` and `gh pr merge <branch> --merge`, which push the closed branch, open its pull request into `{{main_branch}}`, wait until its checks pass and merge it with a merge commit, never with `--admin`; then `git fetch origin`, `git switch {{main_branch}}`, `git merge --ff-only origin/{{main_branch}}`, `git switch -c <id>` and `git branch -d <branch>`, so that the local `{{main_branch}}` follows `origin/{{main_branch}}`; no Case reviews this pull request, since each change of the closed sprint was ratified in its own session;
   - for an author who is not the owner, one task line that opens with `stop:` and runs `git push -u origin <branch>` and, when `gh pr view <branch>` shows no open pull request, `gh pr create --base {{main_branch}} --fill`; then `git switch -c <id>` and `git branch -d <branch>`, so that the branch `<id>` starts from the closed branch and keeps its work until the owner merges the pull request, by `/pr-review` where the project holds `.claude/skills/pr-review/SKILL.md`.

   The Spec holds the opening Case first, so Work Mode runs them before any other task, and the rest of Work Mode runs on the branch `<id>`. Work Mode stops before the task line that opens with `stop:` and runs it after the person's word. The opening Case does not merge `{{main_branch}}` into the closed branch: `/sprint-close` closes no sprint whose branch does not hold `{{main_branch}}`, so `{{main_branch}}` was merged into it before the close. A refusal of a `git` or `gh` command of these tasks, `gh pr checks --watch` on a red check and `gh pr merge` on a pull request that cannot be merged among them, is a stop on the sixth condition of `vault/wiki/where-to-stop.md`. When the branch is `{{main_branch}}`, the opening Case holds as its first task line one line that runs `git switch -c <id>`, and no merge or deletion task: Work Mode runs that line before any other task and the rest of the Spec on the branch `<id>`, and a refusal of it is a stop on the sixth condition of `vault/wiki/where-to-stop.md`; the line opens with no `stop:`, since git can undo a local branch. The opening Case puts no question on the merge or the branch to the person.
5. The skill decides none of the answers: the main agent asks the person what to build in the sprint and proposes the id, which the person confirms or corrects, and `case-guppi` puts each other question to the person, and the person ratifies the opening Case as any other. Before the reply that acknowledges it, assemble and write the Frontier as `/hi` sets it, the items of the first milestone of the opening Case among its Cases; that reply shows it, as `vault/wiki/orchestration.md` sets that reply.
<!-- /rule-skill-sprint-open -->

## History

- 2026-11-28 shipped with GUPPI
