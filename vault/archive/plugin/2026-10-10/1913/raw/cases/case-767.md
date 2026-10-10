## Case 767 — The clean-branch check starts on the sprint branch

> **context:**
> `estimate-sprint-plugin-ci-writes-a-clean-branch` is one of the five Estimates of `entity-sprint-plugin`, created by case 756.5. It checks that CI on GitHub writes a clean version of the project to a branch of its own, with no case reference and no session data, and fails the run when one remains. Its method reads it in a session of the sprint `plugin` before its close, so `/hi` could not read it now and made its Work line a Cases line: `.git/config` holds no remote, `.git/refs/heads/` holds only `main` and `plugin`, no `.github/` folder stands, and the milestone `The clean branch` of `vault/wiki/sprint.md` is the second and not reached. The moment of the reading is left to the rule of Case 764, which the person ratified in the same answer: an Estimate of a sprint page is read at the Retro of the session that finishes its work or by the closing Case of `/sprint-close`, and only an Estimate whose target is an `entity-sprint-<id>` page may name a session of that sprint before its close. The method of this page names such a session and its target is `entity-sprint-plugin`, so the method stands. The file of Case 764 did not stand when this Case was built. The frame showed a second flaw. The trigger of the Criterion is a commit that lands on `main` before the close. The sprint commits to the branch `plugin`. The Criterion of `estimate-skill-sprint-close-leads-the-closing-session` sets that the closing Case of a sprint on a branch of its own holds a task line for the merge of that branch into the main branch, which Work Mode leaves unticked so that the brief gives it as Work to the session that opens the next sprint; it does not forbid `main` to move before the close. The work of the sprint lands on `plugin` and reaches `main` by that merge, so a trigger on `main` waits for a commit that the work of the sprint does not make before its close, and the check could go to the archive unread. This Case replaces the Criterion whole, with the trigger on the branch `plugin` and the rest of the promise unchanged; the page checks itself. The one line of the old Criterion that the new one does not carry is its `When:` line, on purpose: its words on a commit that lands on `main` are what this Case replaces, and the new `when` is that line with `plugin` in place of `main`. Its `purpose` and `method` do not name `main`, so both stand. A Grep for `estimate-sprint-plugin-ci-writes-a-clean-branch` over the repository outside `vault/raw/` printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/entities/entity-sprint-plugin.md`; the sentences of `entity-sprint-plugin` name CI and a branch of its own but not `main`, and stand. A Grep for `sprint-plugin|ci-writes` over `tests/` printed nothing, so no test reads the page.

> **problem:**
> The check starts on a commit to `main`, which does not happen before the sprint closes, so the check cannot be read in time.

> **recommend:**
> - **Who sets when this check is read**
>   - Recommended: (a) the general rule of Case 764 decides it; the method stays, and this Case covers only the trigger.
>   - Answer: agreed, (a).
> - **What starts the check: a commit on `main`, or on the sprint branch**
>   - Recommended: (a) the trigger names the branch `plugin`; the rest of the promise stays.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: pre-spec found that `context` gave the Criterion of `estimate-skill-sprint-close-leads-the-closing-session` as wider than it is, with an "only" it does not hold; the person agreed to fix the wording.
>   - Taken: `context` gives that Criterion as it stands: the merge task line is left unticked for the session that opens the next sprint, and it does not forbid `main` to move before the close.

> **given:**
> `estimate-sprint-plugin-ci-writes-a-clean-branch`: the check of the clean branch; its Criterion is replaced whole.
> **＋** `estimate-skill-sprint-close-leads-the-closing-session`: sets when a sprint branch is merged into the main branch.

> **when:**
> In a session of the sprint `plugin` before its close, a commit lands on the branch `plugin` of the repository of the project on GitHub, and CI runs on it.

> **then:**
> CI writes a clean version of the project to a branch of its own.
> **＋** No text of the clean version holds a reference to a case or a decision.
> **＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
> **＋** A check of CI fails the run when a case reference or session data remains in the clean version.

> **tasks:**
> - [ ] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — CI starts on a commit to the branch plugin, where the sprint commits`
> - [ ] read `estimate-sprint-plugin-ci-writes-a-clean-branch`

> **ratification:**
> ```
> - decision[case 767][update][estimate-sprint-plugin-ci-writes-a-clean-branch]{ref:entity-sprint-plugin}
> ```
