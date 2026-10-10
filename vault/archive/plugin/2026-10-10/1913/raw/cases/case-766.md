## Case 766 — The pull-request check of the sprint plugin targets the sprint branch

> **context:**
> `estimate-sprint-plugin-pull-requests-reviewed-on-github` is one of the five Estimates of the sprint page `entity-sprint-plugin`, created by case 756.4. It passes when a pull request against `main` comes from an account other than the owner's, the checks of CI run on it, and the owner reviews it and can merge it. Its method is a pull request from a second account, read on GitHub in a session of the sprint `plugin` before its close. No such pull request exists yet, and the milestone that sets up the repository on GitHub for pull requests from others is still open, so the reading cannot run in this session. The brief still listed the Estimate under `Work`, and it became the Frontier item W4; `rule-skill-hi` makes such a line a Cases line, which is C8. The person chose to keep the Estimate, and that a second GitHub account that the owner makes for the test counts as an account other than the owner's. The moment of its reading is left to the rule of Case 764 of this batch: an Estimate whose target is a sprint page is read at the Retro of the session that finishes its work or by the closing Case of `/sprint-close`, and its method may name a session of its sprint before its close; Case 764.2 lets Retro leave it `pending` while its work is not done. So the method stands. Pre-spec found two flaws in the first build of this Case. A History line alone cannot say that a second account of the owner counts, since a reading measures the Criterion the page carries and a promise changes only by a Criterion replaced whole (case 378.4). And the Criterion asked for a pull request against `main`, merged into `main`, read before the close of the sprint. The sprint commits to the branch `plugin`. The Criterion of `estimate-skill-sprint-close-leads-the-closing-session` sets that the closing Case of a sprint on a branch of its own holds a task line for the merge of that branch into the main branch, which Work Mode leaves unticked so that the brief gives it as Work to the session that opens the next sprint; it does not forbid `main` to move before the close. The work of the sprint stands on `plugin`, and that merge task brings it into `main` after the close, so a pull request against `plugin` is checked against the work of the sprint before the close. Case 767 moves its own check to `plugin` for the same reason. The person chose that the pull request goes against `plugin`, CI runs on it, and the owner reviews it and merges it into `plugin`. This Case replaces the Criterion whole with that, and the Estimate checks itself. Two lines of the old Criterion are not carried, on purpose: its `When:` line, whose pull request against `main` from an account other than the owner's is what this Case replaces, and the new `when` is that line with `plugin` in place of `main` and the second account of the owner named; and its line that the owner can merge the pull request into `main`, which the new `then` carries with `plugin` in place of `main`. Its `purpose` names a merge into main, so it is set anew; its `method` does not name `main`, so it stands. `entity-sprint-plugin` keeps its Purpose, which names a pull request from another account checked and reviewed on GitHub, and its milestone of a repository on GitHub ready for a pull request from another person; neither names `main`, and both stay true. A Grep for `pull-requests-reviewed-on-github` over the repository, `vault/raw/` left out, printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/entities/entity-sprint-plugin.md`. No test reads the page, and the sprint page only links it. Case 764 had no file when this Case was built, so this Case does not quote its text.

> **problem:**
> The pull-request Estimate of the sprint `plugin` cannot be read now, since no pull request from a second account exists. Its wording leaves open whether a second account of the owner counts as another account, and it asks for a pull request against `main`, which does not move before the sprint closes.

> **recommend:**
> - **What happens to the pull-request check?**
>   - Recommended: (a) keep the check; a second account of the owner counts, and the page gets a History line saying that it waits under the rule of Case 764.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: pre-spec found that a History line alone cannot make a second account of the owner count, since the kept Criterion still says an account other than the owner's, and that the Criterion asks for a pull request against `main`, which does not move before the close; the person chose (a), a pull request from the second account against `plugin`, CI on it, reviewed and merged into `plugin`, read before the close.
>   - Taken: the Criterion is replaced whole with the branch `plugin` and the second account of the owner, the `purpose` is set anew, and the Estimate is set `pending`.

> **given:**
> `estimate-sprint-plugin-pull-requests-reviewed-on-github`: the check of pull requests; its Criterion is replaced whole and its `purpose` set anew.
> **＋** `entity-sprint-plugin`: the sprint page that lists the Estimate.
> **＋** `estimate-skill-sprint-close-leads-the-closing-session`: sets when a sprint branch is merged into the main branch.

> **when:**
> In a session of the sprint `plugin` before its close, someone opens a pull request against the branch `plugin` of the repository of the project on GitHub from an account other than the owner's, such as a second account that the owner made for the test.

> **then:**
> The checks of CI run on the pull request and show their result on it.
> **＋** The owner reviews the pull request on GitHub and can merge it into `plugin`.
> **－** The pull request does not go into the main branch before the close; the main branch takes it with `plugin` as `estimate-skill-sprint-close-leads-the-closing-session` sets.

> **tasks:**
> - [ ] update `estimate-sprint-plugin-pull-requests-reviewed-on-github`
>   - set:
>     ```
>     status: pending
>     purpose: Whether a pull request from another account, a second account of the owner included, runs the checks of CI on GitHub and can be reviewed and merged into the branch plugin
>     ```
>   - change: `the Criterion replaced whole — the pull request goes against the branch plugin, and a second account of the owner counts as another account`
> - [ ] read `estimate-sprint-plugin-pull-requests-reviewed-on-github`

> **ratification:**
> ```
> - decision[case 766][update][estimate-sprint-plugin-pull-requests-reviewed-on-github]{ref:entity-sprint-plugin}
> ```
