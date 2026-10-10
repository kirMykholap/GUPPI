## Case 757 — The branch migration merges into main

> **context:**
> The sprint `migration` ran on a branch of its own. Step 4 of `/sprint-close`, the Render of `rule-skill-sprint-close`, has the closing Case hold a task line for the merge of that branch into `main`, which Work Mode leaves unticked for the session that opens the next sprint. Case 755 left that line open in `vault/raw/2026-10-10/1555/spec.md`, and this session opened the sprint `plugin` by Case 756. Git's own record of the two branches, `.git/logs/refs/heads/main` and `.git/logs/refs/heads/migration`, shows that `migration` was cut from the commit `main` still points at, so `main` can move to the last commit of `migration` by a fast-forward. `.git/config` holds no `[remote]` section, so nothing is pushed. Work Mode stops on `main` (`.claude/skills/work/SKILL.md`), so the session cannot merge there and stay there. The person chose a fast-forward only, a new branch `plugin` with `migration` deleted, a new Estimate under `rule-skill-sprint-close`, the old line ticked by hand, and this merge alone. A refusal of `git merge --ff-only` or of `git branch -d` in Work Mode outside `/box` falls under the first condition of `vault/wiki/where-to-stop.md`, a fork that changes a contract, so the stop needs no new condition. A Grep for `merge` over `.claude/` printed four files: `.claude/skills/box/SKILL.md`, `.claude/skills/handoff/SKILL.md`, `.claude/agents/librarian-guppi.md` and `.claude/skills/sprint-close/SKILL.md`. None of them is `/sprint-open`, so no step of the opening merges a branch. That stays out of this Case by the person's answer, as does the sentence of step 4 that says the brief gives the merge line under `Work`, while the brief gave it under `Cases`. Both are left for the milestone of the sprint turn of `entity-sprint-plugin`. The Criterion of `estimate-skill-sprint-close-leads-the-closing-session` speaks of the closing Case that writes the merge line, not of the merge, so it stands. A Glob `vault/**/*merge*` printed two files, `vault/wiki/estimates/estimate-index-check-merges.md` and `vault/archive/migration/2026-10-10/1555/estimates/estimate-sprint-migration-merges.md`, so the new slug is free.

> **problem:**
> The work of `migration` is not on `main`, and the session must merge it without leaving Work Mode on `main`. No check says when the merge is done.

> **recommend:**
> - **How should `main` take the work of `migration`?**
>   - Recommended: (a) fast-forward only, a refusal a stop for the person's word.
>   - Answer: agreed, (a).
> - **Which branch does the work go on after the merge?**
>   - Recommended: (a) a new branch `plugin` made from `main`, and `migration` deleted by `git branch -d`.
>   - Answer: agreed, (a).
> - **What checks that the merge is done?**
>   - Recommended: (a) a new Estimate under `rule-skill-sprint-close`, read by hand in this session and at each later opening after a sprint with a branch of its own.
>   - Answer: agreed, (a).
> - **What happens to the unticked merge line in the old Spec?**
>   - Recommended: (a) a task of this Case ticks it by hand after the merge.
>   - Answer: agreed, (a).
> - **Does this Case also make the merge a step of opening a sprint?**
>   - Recommended: (a) this merge only; a merge step of the sprint turn stays for the milestone that fixes the opening and the close.
>   - Answer: agreed, (a).

> **given:**
> `estimate-skill-sprint-close-branch-merged-at-the-next-opening`: the new check of the merge.
> **＋** `rule-skill-sprint-close`: the skill that writes the merge line into the closing Case.
> **＋** `vault/raw/2026-10-10/1555/spec.md`: the Spec of the closing session of `migration`, which holds the merge line.
> **＋** the branches `migration`, `main` and `plugin` of the repository.
> **＋** `raw/<date>/<hi HHMM>/work.md`: the Baseline of Work Mode.
> **＋** `vault/wiki/where-to-stop.md`: the conditions on which Work Mode stops.

> **when:**
> In Work Mode of the session that opens a sprint after a sprint that ran on a branch of its own, the agent runs the merge of that branch into `main`, the task line that the closing Case of that sprint left unticked in its `spec.md`.

> **then:**
> `main` moves to the last commit of the branch of the closed sprint by `git merge --ff-only`, and no merge commit is made.
> **＋** The agent makes from `main` a branch named by the id of the new sprint, switches to it, and deletes the branch of the closed sprint by `git branch -d`.
> **＋** The rest of Work Mode runs on the branch of the new sprint.
> **＋** `make test` on the branch of the new sprint, right after the switch, fails no test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold.
> **＋** The merge line in the `spec.md` of the closing session stands ticked.
> **－** When `git merge --ff-only` or `git branch -d` refuses, the agent stops on the first condition of `vault/wiki/where-to-stop.md`, shows the refusal, and goes on after the person's word.

> **tasks:**
> - [ ] create `estimate-skill-sprint-close-branch-merged-at-the-next-opening`
>   - ref: `rule-skill-sprint-close`
>   - kind: `QA`
>   - purpose: `Whether the session that opens a sprint after one that ran on a branch of its own moves main to that branch by a fast-forward, goes on on a branch named for the new sprint, deletes the old branch and ticks the merge line`
>   - method: `by hand, at the Retro of a session that opens a sprint after one that ran on a branch of its own: git branch --list, git log -1 main against the last commit of the old branch, the make test run of its Work Mode against work.md, and the spec.md of the closing session`
>   - tags: `[sprint, git, workflow]`
> - [ ] by hand: as the first task of Work Mode, run `git switch main`, `git merge --ff-only migration`, `git switch -c plugin` and `git branch -d migration`; a refusal of the merge or of the deletion is a stop for the person's word.
> - [ ] by hand: run `make test` on `plugin` right after the switch, and hold each failing test against `## Baseline` of `vault/raw/2026-10-10/1713/work.md`.
> - [ ] by hand: tick the line ``the merge of `migration` into `main` — the first work of the session that opens the next sprint, after its opening Case`` in `vault/raw/2026-10-10/1555/spec.md`.
> - [ ] read `estimate-skill-sprint-close-branch-merged-at-the-next-opening`

> **ratification:**
> ```
> - decision[case 757][create][estimate-skill-sprint-close-branch-merged-at-the-next-opening]{ref:rule-skill-sprint-close}{tags:sprint,git,workflow}
> ```
