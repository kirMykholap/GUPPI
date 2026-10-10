## Case 762 — The branch migration merges into main

> **context:**
> The sprint `migration` ran on a branch of its own. Step 4 of `/sprint-close`, the Render of `rule-skill-sprint-close`, has the closing Case hold a task line for the merge of that branch into `main`, which Work Mode leaves unticked for the session that opens the next sprint. Case 755 left that line open in `vault/raw/2026-10-10/1555/spec.md`, and this session opened the sprint `plugin` by Case 756. Git's own record of the two branches, `.git/logs/refs/heads/main` and `.git/logs/refs/heads/migration`, shows that `migration` was cut from the commit `main` still points at, so `main` can move to the last commit of `migration` by a fast-forward. `.git/config` holds no `[remote]` section, so nothing is pushed. Work Mode stops on `main` (`.claude/skills/work/SKILL.md`), so the session cannot merge there and stay there. This Case replaces Case 757. The findings of `/pre-spec` showed that the Estimate of Case 757 promised the merge at every opening after a sprint with a branch of its own, while no Render of `rule-skill-sprint-close` or `rule-skill-sprint-open` sets those steps. The person chose to narrow the Estimate to this merge alone, so it takes a new slug and this Case a new number. Steps of the sprint turn that merge a branch at each opening stay work of the first milestone of `entity-sprint-plugin`. That also covers the sentence of step 4 that says the brief gives the merge line under `Work`, while the brief gave it under `Cases`. A refusal of `git merge --ff-only` or of `git branch -d` here is the first condition of `vault/wiki/where-to-stop.md`. It is a fork that changes a contract: the merge as ratified cannot run, and the next step needs a choice that no ratified Case makes. The run goes on after the person's answer, as the closing paragraph of that file sets it. So `estimate-where-to-stop-stops-only-on-its-conditions` stands: its Criterion already stops on such a fork, and this Case adds no other stop. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` stands too. Work Mode starts on `migration` and writes its Baseline there before the first change. The task leaves `main` as soon as the fast-forward is done. After it `main`, `migration` and `plugin` are one commit, so the Baseline describes the same tree. The extra `make test` is a task of the Spec, and the full run after the last task still runs. The reading of the new Estimate is taken at the Retro of this session, as `/work` leaves the reading of an Estimate that its session creates, from what Work Mode printed. A Grep for `merge` over `.claude/` printed four files: `.claude/skills/box/SKILL.md`, `.claude/skills/sprint-close/SKILL.md`, `.claude/skills/handoff/SKILL.md` and `.claude/agents/librarian-guppi.md`; none of them is `/sprint-open`. A Glob `vault/**/*merge*` printed two files, `vault/wiki/estimates/estimate-index-check-merges.md` and `vault/archive/migration/2026-10-10/1555/estimates/estimate-sprint-migration-merges.md`, so the new slug is free.

> **problem:**
> The work of `migration` is not on `main`, and the session must merge it without leaving Work Mode on `main`. No check says when this merge is done.

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
> - **Change**
>   - Asked: the findings of `/pre-spec`: the stop on a refusal named as the first condition of `vault/wiki/where-to-stop.md`; the Estimate narrowed to the merge of `migration` in this session, the person's choice (a), since no Render sets the steps for later openings; and `estimate-where-to-stop-stops-only-on-its-conditions` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` named with why they stand.
>   - Taken: built again as Case 762 in place of Case 757, the Estimate under the new slug `estimate-skill-sprint-close-migration-merged-into-main` with `when` and `then` on this merge alone, the `－` line on the first condition, and the two Estimates named in `context`.

> **given:**
> `estimate-skill-sprint-close-migration-merged-into-main`: the new check of this merge.
> **＋** `rule-skill-sprint-close`: the skill that wrote the merge line into the closing Case of `migration`.
> **＋** `vault/raw/2026-10-10/1555/spec.md`: the Spec of the closing session of `migration`, which holds the merge line.
> **＋** the branches `migration`, `main` and `plugin` of the repository.
> **＋** `vault/raw/2026-10-10/1713/work.md`: the Baseline of this session's Work Mode.
> **＋** `vault/wiki/where-to-stop.md`: the conditions on which Work Mode stops.

> **when:**
> In Work Mode of the session that opens the sprint `plugin`, the agent runs the merge of `migration` into `main`, the task line that the closing Case of `migration` left unticked in `vault/raw/2026-10-10/1555/spec.md`.

> **then:**
> `main` moves to the last commit of `migration` by `git merge --ff-only`, and no merge commit is made.
> **＋** The agent makes the branch `plugin` from `main`, switches to it, and deletes `migration` by `git branch -d`.
> **＋** The rest of Work Mode runs on `plugin`.
> **＋** `make test` on `plugin`, right after the switch, fails no test that `## Baseline` of `vault/raw/2026-10-10/1713/work.md` does not hold.
> **＋** The merge line in `vault/raw/2026-10-10/1555/spec.md` stands ticked.
> **－** When `git merge --ff-only` or `git branch -d` refuses, the agent stops on the first condition of `vault/wiki/where-to-stop.md`, a fork that no ratified Case decides, shows the refusal, and the run goes on from where it stopped after the person's answer.

> **tasks:**
> - [ ] create `estimate-skill-sprint-close-migration-merged-into-main`
>   - ref: `rule-skill-sprint-close`
>   - kind: `QA`
>   - purpose: `Whether the session that opens the sprint plugin moves main to the last commit of migration by a fast-forward, goes on on the branch plugin, deletes migration and ticks the merge line of the closing Spec`
>   - method: `by hand, at the Retro of the session that opens the sprint plugin: git branch --list, git log -1 main against the last commit of migration that Work Mode printed, the make test run of its Work Mode against work.md, and vault/raw/2026-10-10/1555/spec.md`
>   - tags: `[sprint, git, workflow]`
> - [ ] by hand: as the first task of Work Mode, run `git switch main`, `git merge --ff-only migration`, `git switch -c plugin` and `git branch -d migration`; a refusal of the merge or of the deletion is a stop on the first condition of `vault/wiki/where-to-stop.md`.
> - [ ] by hand: run `make test` on `plugin` right after the switch, and hold each failing test against `## Baseline` of `vault/raw/2026-10-10/1713/work.md`.
> - [ ] by hand: tick the line ``the merge of `migration` into `main` — the first work of the session that opens the next sprint, after its opening Case`` in `vault/raw/2026-10-10/1555/spec.md`.
> - [ ] read `estimate-skill-sprint-close-migration-merged-into-main`

> **ratification:**
> ```
> - decision[case 762][create][estimate-skill-sprint-close-migration-merged-into-main]{ref:rule-skill-sprint-close}{tags:sprint,git,workflow}{supersedes:case 757}
> ```
