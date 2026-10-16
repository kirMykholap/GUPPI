## Case 850 — The tag prod-0.2.0 is pushed after the install readings, on the person's word

> **context:**
> Work Mode runs the tasks of the Spec in the order the Spec holds them, as `.claude/skills/work/SKILL.md` says. Case 841 placed the `stop:` task that pushes the tag `prod-0.2.0` in its own Case, before the install readings of Cases 843 to 846, so the push would run before them. The person chose to read the install before the push. At `/pre-spec` the person agreed that Case 846 holds one `stop:` task for every install by hand, and that the push follows after it. The push is a behaviour with a promise of its own, and Case 847, which sets the milestone line of `entity-sprint-plugin`, already has a decision line in the ledger of this session. So the push stands in this new Case, beside Case 847 and after it, and Case 847 stays as it is. Its milestone line already says that the owner pushes a tag of the form `prod-x.y.z` and that the run writes nothing to `prod` while a page with `core: true` stands `draft`. The push is the third condition of `rule-where-to-stop`: an action that git in this repository cannot undo, such as a push to a remote. So the task opens with `stop:` and runs on the person's word, as Case 841 set it (its answer to the question on the push). A push of a tag `prod-*` starts `.github/workflows/prod.yml`. Its build runs without `--allow-draft`, so while the draft pages with `core: true` that the brief lists under `## Flags` stand `draft`, the run fails and writes nothing to `prod`. The Estimate that checks the push is `estimate-sprint-plugin-ci-writes-a-clean-branch`. Its Criterion already covers the run on a tag `prod-x.y.z` and a run that writes nothing when `guppi ship` exits 1, and its `method` waits for a run that writes `prod` before the close of `plugin`. So its Criterion, `purpose` and `method` stand, its `update` here carries only `change`, and it stays `pending`; this Case adds no `read` line, since this run cannot write `prod`.

> **problem:**
> The push of the tag would run before the install readings that the person wants first, because Work Mode runs the tasks in the order of the Spec.

> **recommend:**
> - **How should the line name the tag?**
>   - Recommended: (a) only the form `prod-x.y.z`, with no number, in the milestone line that Case 847 sets.
>   - Answer: agreed, (a).
> - **What should the line list as the work left?**
>   - Recommended: (a) the tag, the CI run read by its Estimate, and the draft core pages that stop the run.
>   - Answer: agreed, (a).
> - **Which check confirms this change?**
>   - Recommended: (a) the existing `estimate-sprint-plugin-ci-writes-a-clean-branch`, its Criterion unchanged.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person agreed that the `stop:` task that pushes `prod-0.2.0` moves out of Case 841 and runs after the one `stop:` task of Case 846 for every install by hand, on the person's word.
>   - Taken: the push stands in this Case, beside Case 847 and after it, since Case 847 already has a decision line; Case 847 stays as it is.

> **given:**
> `estimate-sprint-plugin-ci-writes-a-clean-branch`: the Estimate of the run on a tag, its Criterion kept.
> **＋** `.github/workflows/prod.yml`: the workflow that a push of a tag `prod-*` starts.
> **＋** `rule-clean-branch`: the rule of the workflow that writes `prod`, and its refusal of a draft page with `core: true`.
> **＋** `rule-where-to-stop`: the rule that makes a push to a remote a stop.
> **＋** `.claude/skills/work/SKILL.md`: Work Mode, which runs the tasks in the order of the Spec.

> **when:**
> In Work Mode of this session, after the install readings by hand, on the person's word at a `stop:` task, the owner pushes the tag `prod-0.2.0` to the repository of the project on GitHub, and `.github/workflows/prod.yml` runs on the tagged commit.

> **then:**
> The push of the tag starts the run of `.github/workflows/prod.yml` on the tagged commit.
> **－** While a page with `core: true` stands `draft`, the run fails and writes nothing to `prod`, as `rule-clean-branch` sets it.
> **－** The tag stays local until the person's word, and when the person says no at the stop, the push is left to a Case of a later session.

> **tasks:**
> - [ ] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
>   - change: `the push of the tag prod-0.2.0 runs after the install readings, on the person's word; the Criterion stands, and the reading waits for a run that writes prod`
> - [ ] stop: on the person's word, `git push origin prod-0.2.0`; then `gh run list --workflow prod.yml` and `gh run view` of the run it starts: it fails at the step that builds the clean version, on the draft pages with `core: true`, and `git ls-remote origin prod` shows no new commit; the result goes into the handoff.

> **ratification:**
> ```
> - decision[case 850][update][estimate-sprint-plugin-ci-writes-a-clean-branch]{ref:entity-sprint-plugin}
> ```
