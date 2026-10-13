## Case 789 — A pull request into main is one Case, and the closed sprint reaches main by a pull request

> **context:**
> The person plans a public repository on GitHub. Others clone the project, run a sprint on their own branch with the harness, and open a pull request of that whole branch into `main`, and only the owner merges into `main`. Today the owner's closed sprint reaches `main` in the first tasks of the opening Case of `/sprint-open`, the Render of `rule-skill-sprint-open`: `git switch main`, `git merge --ff-only <branch>`, `git switch -c <id>` and `git branch -d <branch>` (case 775.1). A fast-forward moves `main` only when `main` holds no commit that the branch lacks. Once another person's pull request lands in `main`, the fast-forward refuses and Work Mode stops on the sixth condition of `vault/wiki/where-to-stop.md`. No rule says how a pull request of another person is taken.
>
> The person chose three parts. Case 789.1 changes step 4 of the Render of `rule-skill-sprint-open`. By the person's later answer, this Case was built again to match Case 790, whose file did not stand when it was built again. The opening Case no longer merges `main` into the closed branch: by that answer, the merge of `main` into a branch is a session of its own while the sprint is still open, before its close, and it belongs to Case 790, so this Case sets no task for it. One task of the opening Case opens with `stop:`. For the owner it pushes the closed branch and opens its pull request into `main`. It then waits for the checks by `gh pr checks --watch` and merges with a merge commit, never with `--admin`, even though the owner is on the bypass list of the ruleset that Case 787.1 sets on `main`. For an author who is not the owner, the task only pushes and opens the pull request if none is open, and the new branch starts from the closed branch, so the unmerged work is not lost. The owner merges that pull request later by `/pr-review`. The prompt says which of the two the person is, by comparing the login of `gh api user` with the owner of the repository. A refused command, a red check among them, is a stop. To make `/merge-main` run before the close, the opening Case also writes the line of `/merge-main` just before the close line in the last milestone. `estimate-skill-sprint-open-asks-the-opening-questions` says the close line is the last item, which stays true, so it stands. The refusal of `/sprint-close` while `origin/main` is not in the branch is Case 790's. Then the local `main` follows `origin/main`, the branch `<id>` is made from it, and the old branch is deleted. No Case reviews that pull request, since each change of the closed sprint was ratified in its own session and nothing is signed twice. The Criterion of `estimate-skill-sprint-open-merges-the-closed-sprint-branch` speaks of these tasks and is replaced whole. Its `purpose` names the fast-forward and its `method` names the Retro of the session of case 775, so both are set anew. The other Estimates of that rule stand. `estimate-skill-sprint-open-asks-the-opening-questions` checks the questions of the opening, and the merge tasks answer no question. `estimate-skill-sprint-open-starts-at-hi` checks the hook on `/hi` alone. The step's sentence that the opening Case puts no question on the merge to the person stays true: the stop before the merge is a stop of Work Mode, not a question of the Case. Case 788 of this session also changes this Render. I read the Render whole, and both of its pairs on it. Case 788.1 adds a sentence after the preamble on a refused sprint id. Case 788.3 rewrites step 2 into a question on the sprint id, then the sentence that opens with "Then dispatch `case-guppi` at once for the line `open the next sprint` of the brief". That sentence runs on through the list of questions. Case 788.3 drops the item of that list on the id and changes step 5. Case 789.1 changes steps 3 and 4 and leaves steps 2 and 5 and the preamble as they are. Read side by side, the texts fit. Step 3 still writes into the prompt of the dispatch that 788.3 sets, and the close line stays the last item, as the new Criterion of `estimate-skill-sprint-open-asks-the-opening-questions` of 788.3 says. The `<id>` of the branch in step 4 is the sprint id that, by 788.3, names the branch of the sprint. Step 4 tells the owner from an author by the GitHub login, the name that 788.3 puts first in the sprint id. Neither Case changes a word of the other's pairs. The first line of the new Criterion of `estimate-skill-sprint-open-merges-the-closed-sprint-branch` is not the old one on purpose, since the prompt now also names whether the person is the owner. Case 789.2 creates `rule-skill-pr-review`, which renders the skill `/pr-review`, and its Estimate. The person names a pull request by its number. The main agent writes the output of `gh` and `git` on it into `raw/<date>/<hi HHMM>/pr-<n>.md`, so that `case-guppi` reads the facts of the review Case at a source. The review Case judges the pull request whole, on the CI result, the pages and code files it changes and the status of the Estimates it adds or changes. When the branch holds a merge Case of `/merge-main`, the skill of Case 790, the review Case also shows each conflicted page and the joined text that the author signed there. The owner ratifies those texts together with the pull request: the author settles the conflicts, and the owner decides whether the pull request is taken. Case 790 has the last task of a merge Case commit the merge with a message that opens with `merge: main` and names the Case. `/pr-review` finds that commit among the commits of the pull request, which leave out every commit that `main` already holds. It finds the Case file `case-<N>.md` in the tree of the head commit on GitHub. `rule-default-mode` keeps a session from writing anything before a Case is ratified. So `/pr-review` reads the branch through `gh api` and runs no `git fetch`, which would write into `.git`. The one file it writes is `pr-<n>.md`, a working file of the session folder, as `frontier.md` is written in Plan Mode. A first-time contributor's run waits for the owner's approval, which Case 787.1 sets. The skill has the person approve that run and waits for the checks before it judges them. Its one decision line updates the live sprint page with a `change` that names the pull request, and its one task, which opens with `stop:`, runs `gh pr merge <n> --merge` from the branch of the session, so no work runs on `main`. Case 789.3 rewrites the sixth condition of `rule-where-to-stop`. A refused `git` or `gh` command in these merge tasks is a stop. By the person's later answer, the sixth condition also names the tasks of a merge Case of `/merge-main`, the skill that Case 790 creates. Those tasks run `git merge --no-ff --no-commit <hash>`, `git checkout --theirs -- <path>` and `git commit`. A refusal of one of them, or a file left in conflict that the merge Case does not settle, is a stop. The conflicts that the merge Case settles are its work and are not a stop. The condition says so: a `git merge --no-ff --no-commit` that exits non-zero only on the files the merge Case settles is no refusal. Case 790 leaves the condition and its Criterion to this Case. The Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` is replaced whole, its line on the merge tasks of the opening Case changed and its other lines kept word for word. Its `purpose` and `method` name no command and stand. The three `then` blocks share words on the stop before a `stop:` task, on a refusal and on going on after the person's answer, but the promises differ and can fail apart. Case 789.1 checks that the text of `/sprint-open` puts the merge tasks into the opening Case, and Case 789.2 that the text of `/pr-review` puts the merge task into the review Case. Case 789.3 checks that the stop list of `vault/wiki/where-to-stop.md`, which `/work` loads, holds those stops and no other. The lines of the old Criteria on the fast-forward of the closed branch and on a refused `git merge --ff-only <branch>` are left out of the new Criteria on purpose, since this Case replaces them.
>
> The vault query found no page that reviews a pull request. `rule-skill-sprint-open` is near: it merges the owner's own branch, and Case 789.1 changes it. `estimate-sprint-plugin-pull-requests-reviewed-on-github` is near too. Its Criterion has the pull request go against the branch `plugin` and not into `main` before the close, which this Case makes false. The person chose that Case 787 replaces that Criterion, since it is the check of Case 787's sprint item on setting up GitHub, and Case 787.1 replaces it whole: the pull request goes against `main` and only the owner merges it. The context of Case 787 says that a session pushes nothing during a sprint. The owner pushes a sprint branch by hand, by `! git push`, a new sprint branch goes up at the owner's first push, and CI runs on it after that push. The `stop:` task of Case 789.1 pushes only the closed branch, at the opening of the next sprint, and pushes no new sprint branch. So the new branch `<id>` goes up at the owner's first push by hand, as Case 787 says, and the two Cases agree. The rules that bear here are the one rule of `rule-ratification`, which the owner's review Case keeps as the Decision of a pull request, and `rule-where-to-stop`, whose third condition already makes a push a stop. The tags `github`, `git`, `workflow` and `harness` fit. A Glob `vault/**/*pr-review*` printed nothing, so `rule-skill-pr-review` and `estimate-skill-pr-review-takes-a-pull-request-whole` are free.
>
> A Grep `ff-only` over `vault/wiki/` printed `vault/wiki/where-to-stop.md`, `estimate-where-to-stop-stops-only-on-its-conditions.md`, `rule-where-to-stop.md`, `rule-skill-sprint-open.md`, `estimate-skill-sprint-open-merges-the-closed-sprint-branch.md`, `estimate-skill-sprint-close-migration-merged-into-main.md`, `rule-spec-box.md` and `estimate-spec-box-runs-a-conserved-spec.md`. Over `.claude/` it printed `.claude/skills/box/SKILL.md` and `.claude/skills/sprint-open/SKILL.md`. The rule pages, their Renders and the two Estimates of this Case change. The `/box` part of the sixth condition is kept word for word. `rule-spec-box`, `estimate-spec-box-runs-a-conserved-spec` and `.claude/skills/box/SKILL.md` speak of `/box`, which fast-forwards a Spec branch onto the shared branch, and they stand. `estimate-skill-sprint-close-migration-merged-into-main` records the one merge of `migration`, a reading already taken, and stands. `rule-skill-sprint-close` and `estimate-skill-sprint-close-leads-the-closing-session` say that the opening Case of the next sprint holds the merge, which stays true. A Grep `sprint-open|where-to-stop|pr-review` over `tests/` printed `tests/test_sprint.py`, `tests/test_onward.py` and `tests/test_gate.py`. None reads a skill file or `vault/wiki/where-to-stop.md` live: `tests/test_sprint.py` checks the line that the hook on `/hi` prints, and the other two name the path of `vault/wiki/where-to-stop.md` in a string. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` stands. Its Baseline is taken on the closed branch, and the branch `<id>` is made from `origin/main`, which may hold work merged after it. A test that this work turns red is handled by its lines on a new failing test. Not done here: the GitHub ruleset on `main`, which is Case 787; the merge of `main` into a branch before the close of its sprint, which by the person's answer belongs to Case 790; and what the vault of a branch keeps, archives or settles at a merge. The copy of the closed branch on GitHub is not deleted by these tasks.

> **problem:**
> No rule says how a pull request of another person into `main` is taken. The owner's closed sprint reaches `main` by a fast-forward, which refuses as soon as `main` holds another person's work.

> **recommend:**
> - **Should this be one Case or two parts?**
>   - Recommended: (a) one Case with two sub-cases: the owner's sprint reaching `main` by a pull request, and the review of another person's pull request as one Case, each with its own check.
>   - Answer: agreed, (a); a third sub-case was added by the answer to the later question on where the stop on a refused merge step is written.
> - **Should the owner's own sprint get a second review when its pull request goes to `main`?**
>   - Recommended: (a) no second review: the opening Case pushes the closed branch, opens a pull request into `main` and merges it, then updates the local `main`, makes the new sprint branch and deletes the old one.
>   - Answer: agreed, (a).
> - **How should GitHub merge a pull request into `main`?**
>   - Recommended: (a) a merge commit, which keeps every commit of the branch and lets `git branch -d` delete the local branch.
>   - Answer: agreed, (a).
> - **Should the run stop before pushing to GitHub and merging there?**
>   - Recommended: (a) keep the stop: the task that pushes and merges opens with `stop:`, and Work Mode runs it after the person's word.
>   - Answer: agreed, (a).
> - **How should another person's pull request reach a session?**
>   - Recommended: (a) the person names it by `/pr-review` and its number, in Plan Mode of any session; a new skill loads only there and sends the review to `case-guppi`.
>   - Answer: agreed, (a).
> - **What should the review Case show the owner before they ratify it?**
>   - Recommended: (a) a summary: the CI result, the rule and entity pages the pull request creates, changes or deletes, the code files it changes, and the status of the Estimates of the author's sprint.
>   - Answer: agreed, (a).
> - **What should happen to a pull request made without the harness?**
>   - Recommended: (a) accept it: it is reviewed like any other, the owner's review Case is its one Decision, and CI must be green.
>   - Answer: agreed, (a).
> - **What happens when the owner does not take the pull request?**
>   - Recommended: (a) the Case is dropped and the owner asks for changes on GitHub in their own words; `/pr-review` runs again after the author updates the pull request.
>   - Answer: agreed, (a).
> - **Who settles a conflict between a pull request and `main`?**
>   - Recommended: (a) the author: no review Case is built while GitHub shows a conflict; for the owner's sprint the opening Case first merges `main` into the closed branch, a conflict there a stop, and the Case on the vault at a sprint's close says how pages are settled.
>   - Answer: agreed, (a).
> - **Which page should a review Case's ratification name?**
>   - Recommended: (a) the owner's current sprint page, by an `update` with one history line naming the pull request.
>   - Answer: agreed, (a).
> - **Who should fix the sprint check that sends pull requests into the branch `plugin`?**
>   - Recommended: (a) Case 787, the Case on setting up the repository, since the check belongs to its sprint item; this Case names the clash in its `context`.
>   - Answer: agreed, (a).
> - **How should each part be checked?**
>   - Recommended: (a) the Criterion of `estimate-skill-sprint-open-merges-the-closed-sprint-branch` replaced whole and read at this session's Retro; a new Estimate of `rule-skill-pr-review` read after a pull request from a second account is reviewed and merged.
>   - Answer: agreed, (a).
> - **Where should the stop on a refused merge step be written?**
>   - Recommended: (a) a third sub-case rewrites the sixth condition of `vault/wiki/where-to-stop.md`: a refused or conflicting `git` or `gh` command in the merge tasks of the opening Case of a sprint or of a review Case is a stop, and the Criterion of its check is replaced whole.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed that Case 789.1 is built again to match the answer to Case 790. The opening Case of the next sprint no longer merges `main` into the closed branch and no longer opens the pull request, since another step does both before the pull request.
>   - Taken: in Case 789.1 the opening Case only merges the open pull request of the closed branch, by one `stop:` task, then updates the local `main`, makes the branch `<id>` and deletes the old branch. The merge of `origin/main` into the closed branch, the push and `gh pr create` are gone, and its check is set anew. In Case 789.3 the sixth condition names a refused `git` or `gh` command of the merge tasks, and no conflict of a merge of `main`. The answers on the owner's sprint and on conflicts above stand as they were given. This change replaces only the parts of them on the opening Case.
> - **Change**
>   - Asked: the person said that the author settles conflicts, and that whether a pull request is taken is the owner's decision, in a separate Case. The person agreed that the review Case of `/pr-review` also shows the author's merge Case of `/merge-main`, when the branch has one: each conflicted page and the joined text that the author signed, so that the owner ratifies the pull request whole together with them.
>   - Taken: in Case 789.2 the skill writes the merge Case of the branch into `pr-<n>.md` too. The review Case states each conflicted page and its joined text, and the owner ratifies them whole with the pull request. Its check names this.
> - **Change**
>   - Asked: the person agreed that Case 789.1 is built again to match the later answers to Case 790. The merge of `main` into a branch runs in a session of its own before the close of the sprint, then the close, then the pull request. For the owner, the `stop:` task of the opening Case of the next sprint pushes the closed branch, opens its pull request and merges it. A contributor pushes and opens the pull request after the close, and the owner reviews it by `/pr-review`.
>   - Taken: in Case 789.1 the `stop:` task runs `git push -u origin <branch>`, `gh pr create --base main --head <branch> --fill` and `gh pr merge <branch> --merge`, followed by the local steps as before. Its check is set anew.
> - **Change**
>   - Asked: the person agreed that Case 789.3 is built again, so that the sixth condition also covers the tasks of a merge Case of `/merge-main`, as Case 790 sets them.
>   - Taken: in Case 789.3 the sixth condition and the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` name the tasks of a merge Case too. A refused `git` command there is a stop, and so is a file left in conflict that the merge Case does not settle. Case 789.2 finds the merge Case by the message of its merge commit, as Case 790 sets it.
> - **Change**
>   - Asked: the findings of `/pre-spec`, with the person's answers.
>     - The new sixth condition made any non-zero exit of `git merge --no-ff --no-commit` of a merge Case a stop, the conflicts the merge Case settles included.
>     - For an author who is not the owner, the opening Case only pushes and opens the pull request when none is open, and the new branch starts from the closed branch.
>     - The owner's merge waits for green checks, with no `--admin`.
>     - `/sprint-open` writes a `/merge-main` line before the close line.
>     - `/pr-review` has the person approve a first-time contributor's run and waits for it.
>     - It looks for merge Cases only among the commits of the pull request.
>     - The `method` of its check waits for the first pull request from another account merged after the close of `plugin`.
>     - `/pr-review` runs no `git fetch` before a Case is ratified, as `rule-default-mode` sets it.
>   - Taken: each finding is fixed in Case 789.1, 789.2 or 789.3 as asked. The refusal of `/sprint-close` while `origin/main` is not in the branch goes to Case 790.

### Case 789.1 — The closed sprint reaches main by a pull request

> **given:**
> `rule-skill-sprint-open`: the skill whose Render changes the merge step.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the file rendered from it.
> **＋** `estimate-skill-sprint-open-merges-the-closed-sprint-branch`: its Criterion is replaced whole.
> **＋** `.claude/skills/hi/SKILL.md`: prints the current branch under `Branch:`.
> **＋** `origin/main` and `git merge --ff-only origin/main`: the `main` of GitHub and the command that moves the local `main` to it.
> **＋** `gh api user --jq .login` and `gh repo view --json owner --jq .owner.login`: the login of the person and of the owner of the repository.
> **＋** `entity-sprint-<id>`, `/merge-main` and `/sprint-close`: the new sprint page, whose last milestone names the merge of `main` and the close.
> **＋** `/pr-review`: the skill by which the owner merges an author's pull request.
> **＋** `vault/wiki/where-to-stop.md`: the conditions on which Work Mode stops.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose tasks Work Mode runs.

> **when:**
> The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, and dispatches `case-guppi` for the opening Case of the next sprint; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

> **then:**
> The prompt of the call names the branch that `/hi` printed under `Branch:` from `.claude/skills/hi/SKILL.md`, and whether the person is the owner of the repository: the login that `gh api user --jq .login` prints is the one that `gh repo view --json owner --jq .owner.login` prints.
> **＋** The opening Case writes into the last milestone of `entity-sprint-<id>`, just before the close line of `/sprint-close`, the line ``- the merge of `main` into `<id>` — `/merge-main`, a session of its own``.
> **＋** When that branch is not `main` and the person is the owner, the opening Case holds as its first tasks, in this order, one task that opens with `stop:` and runs `git push -u origin <branch>`, `gh pr create --base main --fill`, `gh pr checks <branch> --watch` and `gh pr merge <branch> --merge`; then `git fetch origin`, `git switch main`, `git merge --ff-only origin/main`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint.
> **＋** When that branch is not `main` and the person is not the owner, the opening Case holds as its first tasks one task that opens with `stop:` and runs `git push -u origin <branch>` and, when `gh pr view <branch>` shows no open pull request, `gh pr create --base main --fill`; then `git switch -c <id>` and `git branch -d <branch>`, so that the branch `<id>` starts from the closed branch and keeps its work until the owner merges it by `/pr-review`.
> **＋** Work Mode runs these tasks before any other task of the Spec, stops before the task that opens with `stop:`, on the fourth condition of `vault/wiki/where-to-stop.md`, runs it after the person's word, and runs the rest of the Spec on the branch `<id>`.
> **－** The owner's pull request is merged only after its checks pass, with a merge commit and never with `--admin`, and no Case reviews it: each of its changes was ratified in its own session.
> **－** The opening Case does not merge `main` into the closed branch.
> **－** When a `git` or `gh` command of these tasks refuses, among them `gh pr checks --watch` on a red check and `gh pr merge` on a pull request that cannot be merged, the agent stops on the sixth condition of `vault/wiki/where-to-stop.md`, shows what stopped it, and goes on from where it stopped after the person's answer.
> **－** When that branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it.
> **－** The opening Case puts no question on the merge or the branch to the person.

> **tasks:**
> - [ ] update `rule-skill-sprint-open`
>   - old:
>     ```
>     3. Write into the same prompt that the opening Case writes, as the last item of the last milestone of the page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that the session that closes the sprint starts `/sprint-close` from it.
>     ```
>   - new:
>     ```
>     3. Write into the same prompt that the opening Case writes, as the last two items of the last milestone of the page, the line ``- the merge of `main` into `<id>` — `/merge-main`, a session of its own`` and then the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that `/merge-main` runs before the close (case 789.1) and the session that closes the sprint starts `/sprint-close` from the close line.
>     ```
>   - old:
>     ```
>     4. Write into the same prompt the branch that `/hi` printed under `Branch:`. When it is not `main`, the closed sprint ran on it, and the opening Case holds as its first task lines `git switch main`, `git merge --ff-only <branch>`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint. The Spec holds the opening Case first, so Work Mode runs them before any other task: `main` takes the work of the closed sprint by a fast-forward, and the rest of Work Mode runs on the branch `<id>`. A refusal of the merge or of the deletion is a stop on the sixth condition of `vault/wiki/where-to-stop.md`.
>     ```
>   - new:
>     ```
>     4. Write into the same prompt the branch that `/hi` printed under `Branch:`, and whether the person is the owner of the repository: the login that `gh api user --jq .login` prints is the one that `gh repo view --json owner --jq .owner.login` prints. When the branch is not `main`, the closed sprint ran on it, and the opening Case holds as its first task lines, in this order, `<id>` the id of the new sprint:
>        - for the owner, one task line that opens with `stop:` and runs `git push -u origin <branch>`, `gh pr create --base main --fill`, `gh pr checks <branch> --watch` and `gh pr merge <branch> --merge`, which push the closed branch, open its pull request into `main`, wait until its checks pass and merge it with a merge commit, never with `--admin`; then `git fetch origin`, `git switch main`, `git merge --ff-only origin/main`, `git switch -c <id>` and `git branch -d <branch>`, so that the local `main` follows `origin/main`; no Case reviews this pull request, since each change of the closed sprint was ratified in its own session;
>        - for an author who is not the owner, one task line that opens with `stop:` and runs `git push -u origin <branch>` and, when `gh pr view <branch>` shows no open pull request, `gh pr create --base main --fill`; then `git switch -c <id>` and `git branch -d <branch>`, so that the branch `<id>` starts from the closed branch and keeps its work until the owner merges the pull request by `/pr-review`.
>
>        The Spec holds the opening Case first, so Work Mode runs them before any other task, and the rest of Work Mode runs on the branch `<id>`. Work Mode stops before the task line that opens with `stop:` and runs it after the person's word. The opening Case does not merge `main` into the closed branch: `/merge-main` did so before the close (case 789.1). A refusal of a `git` or `gh` command of these tasks, `gh pr checks --watch` on a red check and `gh pr merge` on a pull request that cannot be merged among them, is a stop on the sixth condition of `vault/wiki/where-to-stop.md`.
>     ```
>   - change: `the opening Case of a sprint pushes the closed sprint and opens its pull request into main; for the owner it merges it after its checks pass; the last milestone names /merge-main before the close`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-open/SKILL.md`
> - [ ] update `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether /sprint-open has the opening Case name /merge-main before the close line, push the closed sprint's branch and open its pull request into main after the person's word, merge it with a merge commit after its checks pass when the person is the owner, and move the work to a branch named by the new sprint, as the first tasks of Work Mode, with a stop on a refusal and no git task on main"
>     method: "by hand, at the Retro of the session of case 789, the new Render of rule-skill-sprint-open in its spec.md read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the opening Case pushes the closed sprint and opens its pull request; the owner's is merged after its checks pass; /merge-main stands before the close line`
> - [ ] read `estimate-skill-sprint-open-merges-the-closed-sprint-branch`

> **ratification:**
> ```
> - decision[case 789.1][update][rule-skill-sprint-open]{ref:rule-skill-sprint-open}
> - decision[case 789.1][update][estimate-skill-sprint-open-merges-the-closed-sprint-branch]{ref:rule-skill-sprint-open}
> ```

### Case 789.2 — A pull request into main is reviewed as one Case

> **given:**
> `rule-skill-pr-review`: the new rule whose Render is the skill `/pr-review`.
> **＋** `.claude/skills/pr-review/SKILL.md`: the file rendered from it, started by `/pr-review <n>`.
> **＋** `estimate-skill-pr-review-takes-a-pull-request-whole`: the new check of the review.
> **＋** `raw/<date>/<hi HHMM>/pr-<n>.md`: the output of `gh` and `git` on the pull request, which `case-guppi` reads.
> **＋** `.claude/agents/case-guppi.md`: the agent that builds the review Case.
> **＋** `rule-default-mode`: keeps the session from writing before a Case is ratified.
> **＋** `/merge-main`: the skill whose merge Case, held by the branch, records the conflicted pages and their joined texts.
> **＋** `entity-sprint-<id>`: the live sprint page that the review Case updates.
> **＋** `vault/wiki/where-to-stop.md`: the conditions on which Work Mode stops.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose tasks Work Mode runs.

> **when:**
> The person types `/pr-review <n>` on `UserPromptSubmit` in Plan Mode, or the main agent calls it on `PreToolUse Skill`, for the pull request `<n>` into `main` of the repository on GitHub, `.claude/skills/pr-review/SKILL.md` rendered from `rule-skill-pr-review`; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

> **then:**
> The main agent runs `gh pr view` and `gh pr checks` on the pull request, has the person approve a run of the checks that waits for the owner's approval and waits until the checks end, reads by `gh api` at the head commit of the pull request the `status` of each Estimate page it adds or changes, with no `git fetch`, writes that output into `raw/<date>/<hi HHMM>/pr-<n>.md`, and dispatches `case-guppi` for the review Case with that path in the prompt.
> **＋** The `context` of the review Case states, from `raw/<date>/<hi HHMM>/pr-<n>.md`, the result of each CI check, the rule and entity pages the pull request creates, changes or deletes, the code files it changes and the `status` of each Estimate page it adds or changes, and names them as what checks it.
> **＋** When a commit of the pull request, none that `main` already holds, names a merge Case of `/merge-main`, `raw/<date>/<hi HHMM>/pr-<n>.md` holds that Case too, and the review Case shows each conflicted page and the joined text that the author signed, which the owner ratifies whole with the pull request.
> **＋** The review Case holds one decision line, an `update` of the live sprint page `entity-sprint-<id>` with only a `change` that names the pull request, and one task, which opens with `stop:` and runs `gh pr merge <n> --merge`.
> **＋** Once the person ratifies the review Case, Work Mode stops before that task, runs it on the branch of the session after the person's word, and `main` on GitHub takes the pull request with a merge commit.
> **－** When the base of the pull request is not `main`, GitHub shows a conflict with `main`, or a CI check is not green, no review Case is built: the main agent tells the person why, and the author updates the pull request.
> **－** The review Case judges the pull request whole: no decision of its author is reviewed one by one.
> **－** A pull request whose branch holds no session of the harness is reviewed the same way, and the review Case is its one Decision.
> **－** When the person drops the review Case, nothing is merged, the agent writes nothing to GitHub, and the person asks the author for changes on GitHub.

> **tasks:**
> - [ ] create `rule-skill-pr-review`
>   - ref: `rule-plan-mode`
>   - kind: `Leaf`
>   - purpose: `Prevents a pull request into main from being merged without one Case that the owner ratified whole, or its review from judging each decision of its author again`
>   - enforcement: `render`
>   - governs: `.claude/skills/pr-review/SKILL.md`
>   - render_mode: `full`
>   - tags: `[github, git, workflow, harness]`
>   - sections.Purpose:
>     ```
>     Prevents a pull request into main from being merged without one Case that the owner ratified whole, or its review from judging each decision of its author again. Others clone the project, run a sprint on their own branch with the harness and open a pull request of the whole branch into `main`; only the owner merges into `main`. Each decision on that branch was made by its author, and the owner does not ratify them one by one: the owner ratifies the pull request whole, in one review Case, which is the Decision of the pull request in the owner's vault (case 789.2). The skill loads only in the session that reviews a pull request, and the person starts it by the number of the pull request. The owner's own closed sprint reaches `main` by a pull request too, but through the opening Case of [[rule-skill-sprint-open]], with no review Case, since each of its changes was ratified in its own session (case 789.1).
>     ```
>   - sections.Render:
>     ````
>     <!-- rule-skill-pr-review -->
>     ---
>     name: pr-review
>     description: "Review a pull request into main as one Case the owner ratifies whole. Run it when the person types /pr-review with the number of the pull request."
>     ---
>
>     The person asks to review the pull request `$ARGUMENTS`, called `<n>` below, into `main` of the repository on GitHub. Its review is one Case of Plan Mode: the owner ratifies the pull request whole or drops it, and no decision of its author is reviewed one by one. The pull request is an item of the person in `frontier.md`, closed as `vault/wiki/orchestration.md` sets it.
>
>     1. Run `gh pr view <n> --json number,title,author,baseRefName,headRefName,headRefOid,mergeable,files,commits` and `gh pr checks <n>`. When a run of the checks waits for the owner's approval, as the run of a first-time contributor does, tell the person to approve it on GitHub, then run `gh pr checks <n> --watch` until the checks end. When the base is not `main`, when `mergeable` is `CONFLICTING`, or when a check is not green once the checks end, build no Case: tell the person why and that the author updates the pull request, and close its line `[x] … · work`.
>     2. Read the branch on GitHub, at the commit `headRefOid`, with no `git fetch`, so that nothing is written in the repository before a Case is ratified. For each path under `vault/wiki/estimates/` that `files` names, run `gh api -H "Accept: application/vnd.github.raw" "repos/{owner}/{repo}/contents/<path>?ref=<headRefOid>"`, for its `status`. Among `commits`, which holds only the commits of the pull request and none that `main` already holds, a commit whose headline opens with `merge: main` names, by `case N` at its end, a merge Case of `/merge-main`. That Case records each page that conflicted when the author merged `main` into the branch, and the joined text the author signed. Find the file `case-<N>.md` of that Case among the paths that `gh api "repos/{owner}/{repo}/git/trees/<headRefOid>?recursive=1" --jq '.tree[].path'` prints, under `vault/raw/` or `vault/archive/`, and read it by the same `contents` call.
>     3. Write the output of these commands, as they printed it, into `raw/<date>/<hi HHMM>/pr-<n>.md`, and dispatch `case-guppi` for the review Case as `vault/wiki/orchestration.md` sets it, with the path of that file in the prompt and these terms:
>        - the `context` states, from that file, the result of each check, the rule and entity pages the pull request creates, changes or deletes, the code files it changes, and the `status` of each Estimate page it adds or changes, and names the checks and these Estimates as what checks the Case, which creates no Estimate;
>        - when that file holds a merge Case of `/merge-main`, the review Case shows each conflicted page and the joined text the author signed, and the owner ratifies them whole with the pull request: the author settles the conflicts, and the owner decides whether the pull request is taken;
>        - the Case judges the pull request whole and reviews no decision of its author one by one;
>        - a pull request whose branch holds no session of the harness is reviewed the same way, and the review Case is its one Decision;
>        - its one decision line is an `update` of the page `entity-sprint-<id>` of the live sprint, with only a `change` that names the pull request by its number;
>        - its one task opens with `stop:` and runs `gh pr merge <n> --merge`: Work Mode stops before it, on the fourth condition of `vault/wiki/where-to-stop.md`, and runs it on the branch of the session after the person's word, so that `main` takes the pull request with a merge commit; a refusal is a stop on the sixth condition.
>     4. The person ratifies the review Case as any other, or drops it. On a drop nothing is merged and the agent writes nothing to GitHub: the person asks the author for changes on GitHub in their own words, and types `/pr-review <n>` again once the author has updated the pull request.
>     <!-- /rule-skill-pr-review -->
>     ````
> - [ ] `uv run guppi render`: `.claude/skills/pr-review/SKILL.md`
> - [ ] create `estimate-skill-pr-review-takes-a-pull-request-whole`
>   - ref: `rule-skill-pr-review`
>   - kind: `QA`
>   - purpose: `Whether /pr-review has a pull request into main reviewed as one Case on the facts of gh and git, the conflicted pages and joined texts of the author's merge Case of /merge-main among them when the branch holds one, ratified whole by the owner and merged with a merge commit after the person's word, with no review Case for a pull request in conflict or with a red check`
>   - method: `by hand, after the first pull request from an account other than the owner's is merged into main by /pr-review after the close of plugin: the review Case in its case file, its decision line, pr-<n>.md and the pull request on GitHub read against the Criterion`
>   - tags: `[github, git, workflow]`
> - [ ] read `estimate-skill-pr-review-takes-a-pull-request-whole`

> **ratification:**
> ```
> - decision[case 789.2][create][rule-skill-pr-review]{ref:rule-plan-mode}{tags:github,git,workflow,harness}
> - decision[case 789.2][create][estimate-skill-pr-review-takes-a-pull-request-whole]{ref:rule-skill-pr-review}{tags:github,git,workflow}
> ```

### Case 789.3 — A refused merge step is the sixth stop

> **given:**
> `rule-where-to-stop`: the rule whose sixth condition is rewritten.
> **＋** `vault/wiki/where-to-stop.md`: the file rendered from it, loaded by `/work` and `/box`.
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions`: its Criterion is replaced whole.
> **＋** `.claude/skills/work/SKILL.md`: Work Mode, which loads the file.
> **＋** `.claude/skills/box/SKILL.md`: the run of a conserved Spec, which loads the file.
> **＋** `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/pr-review/SKILL.md` and `.claude/skills/merge-main/SKILL.md`: the skills whose Cases hold the merge tasks.
> **＋** `raw/<date>/<hi HHMM>/spec.md`, `raw/<date>/<hi HHMM>/work.md` and `raw/<date>/<hi HHMM>/handoff.md`: the files of the session the run reads and writes.
> **＋** `vault/wiki/case-schema.md`: names a task that waits for the person's word.
> **＋** `/retro`: the skill from whose call a stop opens with `STOP:`.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
> **＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

> **then:**
> The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
> **＋** The context of `/box`, from `.claude/skills/box/SKILL.md`, holds the same text.
> **＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
> **＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
> **＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
> **＋** In a run of `/box`, the agent stops and asks when `uv run guppi box --check` prints a line, or when a `git merge --ff-only` of `/box` refuses.
> **＋** In the merge tasks that the opening Case of a sprint holds by `.claude/skills/sprint-open/SKILL.md`, in the merge task that a review Case holds by `.claude/skills/pr-review/SKILL.md`, and in the tasks that a merge Case holds by `.claude/skills/merge-main/SKILL.md`, the agent stops, shows what stopped it and asks when a `git` or `gh` command refuses, or when the merge of a merge Case leaves in conflict a file that the merge Case does not settle.
> **－** `git merge --no-ff --no-commit` of a merge Case of `.claude/skills/merge-main/SKILL.md` that exits non-zero only on files that the merge Case settles is no refusal, and the run goes on to the tasks that settle them.
> **＋** When the full `make test` run of `/work` after its last task finds a failing test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold, and its fix needs a choice that no ratified Case makes, the agent ends a reply with a question to the person that names the test and its failure.
> **＋** When the auto mode classifier of Claude Code refuses a tool call that the run needs, the agent ends a reply with a question to the person that gives the shell command doing what the refused call would do, for the person to type after `!` in the prompt.
> **＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
> **＋** After the person's answer the run goes on from where it stopped.
> **＋** After the person has run the command that a refusal of the auto mode classifier gave, the run goes on from where it stopped.
> **＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
> **－** No other point stops the run: any other red test, at `/retro` too, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

> **tasks:**
> - [ ] update `rule-where-to-stop`
>   - old: `` or, in the merge tasks of the opening Case of a sprint, `git merge --ff-only` or `git branch -d` refuses: show what stopped it, and go on after the person's word (case 775.3). ``
>   - new: `` or a `git` or `gh` command of the merge tasks of the opening Case of a sprint, of the merge task of a review Case of `/pr-review`, or of the tasks of a merge Case of `/merge-main` refuses, or the merge of a merge Case leaves in conflict a file that the merge Case does not settle: show what stopped it, and go on after the person's word; a `git merge --no-ff --no-commit` of a merge Case that exits non-zero only on files the merge Case settles is no refusal (cases 775.3, 789.3). ``
>   - change: `condition 6 covers a refused git or gh command in the merge tasks of the opening Case of a sprint, of a review Case and of a merge Case, and a conflict that a merge Case does not settle`
> - [ ] `uv run guppi render`: `vault/wiki/where-to-stop.md`
> - [ ] update `estimate-where-to-stop-stops-only-on-its-conditions`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a refused git or gh command in the merge tasks of the opening Case of a sprint, of a review Case or of a merge Case, and a conflict that a merge Case does not settle, is a stop`
> - [ ] read `estimate-where-to-stop-stops-only-on-its-conditions`

> **ratification:**
> ```
> - decision[case 789.3][update][rule-where-to-stop]{ref:rule-where-to-stop}
> - decision[case 789.3][update][estimate-where-to-stop-stops-only-on-its-conditions]{ref:rule-where-to-stop}
> ```
