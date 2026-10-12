## Case 775 — The opening Case of a sprint merges the closed sprint's branch

> **context:**
> When a sprint ran on a branch of its own, its work must reach `main` after the close. Today step 4 of `/sprint-close`, the Render of `rule-skill-sprint-close`, has the closing Case leave one unticked task line for that merge. The line is left for the session that opens the next sprint, and the brief is to give it under `Work`. `/sprint-open`, the Render of `rule-skill-sprint-open`, says nothing of the merge. After the close of `migration`, the Frontier of session 1713 took the line from the brief under `Cases`, and the line was not enough to run: Case 762 had to decide a fast-forward only, the new branch `plugin` and the deletion of `migration`. Case 771 put off both pages, so each carries `deferred_by: decision-case-771`, and each sub-case here carries `{supersedes:case 771}` on its `update` of that page. The person chose to put the merge into the opening Case, to run it as a fast-forward with a stop on a refusal, and to move the work to a new branch named by the id of the new sprint. With no leftover line, the question of which list of the brief carries it goes away. The rule of the brief in `.claude/agents/librarian-guppi.md`, which gives the unticked boxes of the Specs under `Work`, stands as it is. On `main` the opening Case holds no git task, since Work Mode stops on `main` before its first task (`vault/wiki/where-to-stop.md`, condition 5). The person makes the new branch there.
>
> Case 775.1 adds a step to the Render of `rule-skill-sprint-open` and creates `estimate-skill-sprint-open-merges-the-closed-sprint-branch`. The other Estimates of that rule stand. `estimate-skill-sprint-open-asks-the-opening-questions` checks the questions of the opening, and its line that the skill decides none of the answers stays true, because the merge tasks answer no question. `estimate-skill-sprint-open-starts-at-hi` checks the hook on `/hi` alone. Case 775.2 removes the merge sentence from step 4 of the Render of `rule-skill-sprint-close`. It replaces the Criterion of `estimate-skill-sprint-close-leads-the-closing-session`, whose line on the unticked merge line becomes false. The new Criterion leaves out on purpose its line `When the sprint ran on a branch of its own, the closing Case holds a task line for the merge of that branch into the main branch`, and puts in its place a `－` line that the closing Case holds no such task line. Its other lines are kept word for word, and the line on the close line of `entity-sprint-migration` is now read under `vault/archive/migration/`. That Estimate's `purpose` does not state the merge and stands. Its `method` names the Retro of the session of case 746, so it is set anew. `estimate-skill-sprint-close-migration-merged-into-main` checked the one merge of `migration`, stands `passed`, and is not touched. Pre-spec found that a refused merge does not fit the first condition of `vault/wiki/where-to-stop.md`, a fork that needs a new Case. Its sixth condition names a refused `git merge --ff-only`, but for `/box` alone, and the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` ties that refusal to `/box` too. By the person's answer, Case 775.3 widens the sixth condition to the merge tasks of the opening Case and replaces that Criterion. Its other lines are kept word for word. The `then` of Case 775.3 shares words with the `then` of Case 775.1 on the refusal and on going on after the person's answer, but the promises differ and can fail apart. Case 775.1 checks that the text of `/sprint-open` puts the merge tasks and their stop into the opening Case. Case 775.3 checks that the stop list of `vault/wiki/where-to-stop.md`, which `/work` loads, holds that stop and no other. Its line on going on after the person's answer is kept from the old Criterion. The `purpose` and `method` of that Estimate do not state the `/box` limit and stand. `.claude/skills/box/SKILL.md` and `rule-spec-box` name condition 6 for the stops of `/box`, which stay in it. `estimate-skill-sprint-close-migration-merged-into-main` records the first condition for the one merge of `migration`, a reading already taken, and stands. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` stands, as case 762 found: Work Mode starts on the closed sprint's branch and writes its Baseline there, and after the fast-forward the new branch holds the same tree. In the two skill pages the Case changes, the merge is stated only by step 4 of `rule-skill-sprint-close`. The step of `rule-skill-sprint-open` that leaves every answer to the person stays true.
>
> A Grep `first work of the session that opens` over `vault/wiki/` and `.claude/` printed `.claude/skills/sprint-close/SKILL.md` and `vault/wiki/rules/rule-skill-sprint-close.md`. The first is rendered anew and the second changes by Case 775.2. A Grep `sprint-open|sprint-close|skill-sprint` over `tests/` printed `tests/test_sprint.py` and `tests/test_sprint_close.py`. Neither reads either skill file or either rule page live: in `tests/test_sprint.py` the hits are a comment and the line the hook on `/hi` prints, and a docstring and a fixture line on the command `guppi sprint-close`. A Grep `where-to-stop|where_to_stop` over `tests/` printed `tests/test_gate.py` and `tests/test_onward.py`, which name the path of `vault/wiki/where-to-stop.md` in a string and do not read the file. A Glob `vault/**/estimate-skill-sprint-open-merges*` printed nothing, so the new slug is free. Case 774 of this session removes the note on the opening and the close from `entity-sprint-plugin`, a page this Case does not change.

> **problem:**
> No rule sets where the merge of a closed sprint's own branch into `main` stands at the opening of the next sprint. The closing Case leaves an unticked line that does not hold the choices the merge needs, `/sprint-open` does not name the merge, and the brief gave that line under `Cases` while `/sprint-close` says `Work`.

> **recommend:**
> - **Where should the merge step be written?**
>   - Recommended: (a) in the opening Case: `/sprint-close` writes no merge line, and the opening Case holds the merge tasks when the session is not on `main`, so no leftover line reaches the brief.
>   - Answer: agreed, (a).
> - **How should the merge run?**
>   - Recommended: (a) a fast-forward only, `git merge --ff-only`, with a stop for the person on a refusal, as the first condition of `vault/wiki/where-to-stop.md` sets it.
>   - Answer: agreed, (a).
> - **Which branch does the new sprint work on?**
>   - Recommended: (a) always a new branch named by the sprint id, made from `main` after the merge, and the old branch deleted by `git branch -d`, a refusal a stop.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) two sub-cases: a new Estimate on the merge tasks of the opening Case, and the Criterion of the closing check replaced so that the closing Case holds no merge line, both read by hand at the Retro of this session against the new Renders in its Spec.
>   - Answer: agreed, (a).
> - **What if the session that opens a sprint is already on `main`?**
>   - Recommended: (a) no merge, only the new branch: the opening Case makes the branch `<new sprint id>` from `main` and switches to it.
>   - Answer: agreed, (a); replaced by the question on what the opening Case holds when the session is on `main`, since Work Mode stops on `main` before that task runs.
> - **What does the opening Case hold when the session is on `main`?**
>   - Recommended: (a) no git task on `main`: Work Mode stops on `main` as it always does, and the person makes the branch `<new sprint id>` and moves to it.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the findings of `/pre-spec`. A refused merge is no fork that needs a new Case, so it does not fit the first condition of `vault/wiki/where-to-stop.md`, and its sixth condition covers `/box` alone. The person chose (a): widen the sixth condition to a refusal of `git merge --ff-only` or `git branch -d` in the merge tasks of the opening Case, and replace the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` to take it in. Two facts of `context` were also corrected: the hits of `tests/test_sprint.py`, and the claim on where the merge is stated.
>   - Taken: Case 775.1 names the sixth condition in its step and its `－` line. The widened condition and the replaced Criterion stand as Case 775.3, since they are a promise of their own on `rule-where-to-stop`. `context` is corrected.

### Case 775.1 — The opening Case merges the closed sprint's branch

> **given:**
> `rule-skill-sprint-open`: the skill whose Render gains the merge step.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the file rendered from it.
> **＋** `estimate-skill-sprint-open-merges-the-closed-sprint-branch`: the new check of the merge step.
> **＋** `.claude/skills/hi/SKILL.md`: prints the current branch under `Branch:`.
> **＋** `vault/wiki/where-to-stop.md`: the conditions on which Work Mode stops.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose tasks Work Mode runs.

> **when:**
> The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, and dispatches `case-guppi` for the opening Case of the next sprint; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

> **then:**
> The prompt of the call names the branch that `/hi` printed under `Branch:` from `.claude/skills/hi/SKILL.md`.
> **＋** When that branch is not `main`, the opening Case holds as its first tasks `git switch main`, `git merge --ff-only <branch>`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint.
> **＋** Work Mode runs these tasks before any other task of the Spec: `main` moves to the last commit of the closed sprint's branch with no merge commit, that branch is deleted, and the rest of Work Mode runs on the branch `<id>`.
> **－** When `git merge --ff-only` or `git branch -d` refuses, the agent stops on the sixth condition of `vault/wiki/where-to-stop.md`, shows the refusal, and goes on from where it stopped after the person's answer.
> **－** When that branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it.
> **－** The opening Case puts no question on the merge or the branch to the person.

> **tasks:**
> - [ ] update `rule-skill-sprint-open`
>   - old: `4. The skill decides none of the answers:`
>   - new:
>     ```
>     4. Write into the same prompt the branch that `/hi` printed under `Branch:`. When it is not `main`, the closed sprint ran on it, and the opening Case holds as its first task lines `git switch main`, `git merge --ff-only <branch>`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint. The Spec holds the opening Case first, so Work Mode runs them before any other task: `main` takes the work of the closed sprint by a fast-forward, and the rest of Work Mode runs on the branch `<id>`. A refusal of the merge or of the deletion is a stop on the sixth condition of `vault/wiki/where-to-stop.md`. When the branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it. The opening Case puts no question on the merge or the branch to the person (case 775.1).
>     5. The skill decides none of the answers:
>     ```
>   - change: `the opening Case of a sprint merges the closed sprint's branch into main by a fast-forward and moves the work to a branch named by the new sprint`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-open/SKILL.md`
> - [ ] create `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
>   - ref: `rule-skill-sprint-open`
>   - kind: `QA`
>   - purpose: `Whether /sprint-open has the opening Case merge the closed sprint's branch into main by a fast-forward as the first tasks of Work Mode and move the work to a branch named by the new sprint, with a stop on a refusal and no git task on main`
>   - method: `by hand, at the Retro of the session of case 775, the new Render of rule-skill-sprint-open in its spec.md read against the Criterion`
>   - tags: `[sprint, git, workflow]`
> - [ ] read `estimate-skill-sprint-open-merges-the-closed-sprint-branch`

> **ratification:**
> ```
> - decision[case 775.1][update][rule-skill-sprint-open]{ref:rule-skill-sprint-open}{supersedes:case 771}
> - decision[case 775.1][create][estimate-skill-sprint-open-merges-the-closed-sprint-branch]{ref:rule-skill-sprint-open}{tags:sprint,git,workflow}
> ```

### Case 775.2 — The closing Case leaves no merge line

> **given:**
> `rule-skill-sprint-close`: the skill whose Render loses the merge line.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the file rendered from it.
> **＋** `estimate-skill-sprint-close-leads-the-closing-session`: its Criterion is replaced whole.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the skill whose opening Case now holds the merge.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose lines the skill closes.
> **＋** `vault/wiki/orchestration.md`: names the two skills of the sprint turn.
> **＋** `.claude/agents/librarian-guppi.md`: runs the close line.
> **＋** `entity-sprint-migration`: the closed sprint page whose close line the check reads.

> **when:**
> The person takes up on the Frontier the line of the sprint that names `/sprint-close`, and the main agent starts the skill `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, rendered from `rule-skill-sprint-close`, on `PreToolUse Skill`, or the person types `/sprint-close` on `UserPromptSubmit`.

> **then:**
> When the session's ledger holds a decision line other than a `defer`, the main agent closes the close line `[-] … · sprint · defer`, tells the person that the close needs a session of its own, and the skill stops.
> **＋** Otherwise the main agent closes each other open line under `## Cases` of `frontier.md` by the closer of its source put off, the person's pick of the close line standing as the words that ratify each short-form defer, leaves the lines under `## Work` and `## Ask` open, and shows the Frontier.
> **＋** It sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names and dispatches `case-guppi` for the closing Case with the groups in the prompt, and the closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choice for each Estimate still unread.
> **＋** Work Mode takes each reading whose moment came and neither runs nor ticks the close line; the librarian runs it, as `.claude/agents/librarian-guppi.md` sets it.
> **＋** `vault/wiki/orchestration.md` holds no paragraph on the closing session, names the two skills in one sentence, and counts the start of `/sprint-close` among the moments of a short-form defer.
> **＋** The close line of `entity-sprint-migration` reads ``- the close of `migration` — `/sprint-close`, a session of its own``, and its `## Backlog` holds no line on the merge.
> **－** Besides the closing Case, the session ratifies only the Cases that prepare its readings.
> **－** The closing Case holds no task line for the merge of the sprint's branch into `main`: the opening Case of the next sprint holds the merge, as `.claude/skills/sprint-open/SKILL.md` sets it.

> **tasks:**
> - [ ] update `rule-skill-sprint-close`
>   - old:
>     ```
>     When the sprint ran on a branch of its own, the closing Case holds too the task line ``the merge of `<branch>` into `main` — the first work of the session that opens the next sprint, after its opening Case``, which Work Mode leaves unticked, so that the brief gives it under `Work` to that session.
>     ```
>   - new:
>     ```
>     The closing Case holds no task line for the merge of the sprint's branch into `main`: the opening Case of the next sprint holds the merge, as `/sprint-open` sets it (case 775.2).
>     ```
>   - change: `the closing Case leaves no merge line; the opening Case of the next sprint holds the merge`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-close/SKILL.md`
> - [ ] update `estimate-skill-sprint-close-leads-the-closing-session`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at the Retro of the session of case 775, the new Render of rule-skill-sprint-close in its spec.md, vault/wiki/orchestration.md and entity-sprint-migration under vault/archive/migration/ read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the closing Case holds no merge line, the opening Case of the next sprint holds the merge`
> - [ ] read `estimate-skill-sprint-close-leads-the-closing-session`

> **ratification:**
> ```
> - decision[case 775.2][update][rule-skill-sprint-close]{ref:rule-skill-sprint-close}{supersedes:case 771}
> - decision[case 775.2][update][estimate-skill-sprint-close-leads-the-closing-session]{ref:rule-skill-sprint-close}
> ```

### Case 775.3 — A refused merge at the opening of a sprint is the sixth stop

> **given:**
> `rule-where-to-stop`: the rule whose sixth condition widens.
> **＋** `vault/wiki/where-to-stop.md`: the file rendered from it, loaded by `/work` and `/box`.
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions`: its Criterion is replaced whole.
> **＋** `.claude/skills/work/SKILL.md`: Work Mode, which loads the file.
> **＋** `.claude/skills/box/SKILL.md`: the run of a conserved Spec, which loads the file.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the skill whose opening Case holds the merge tasks.
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
> **＋** In the merge tasks that the opening Case of a sprint holds by `.claude/skills/sprint-open/SKILL.md`, the agent stops, shows what stopped it and asks when `git merge --ff-only` or `git branch -d` refuses.
> **＋** When the full `make test` run of `/work` after its last task finds a failing test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold, and its fix needs a choice that no ratified Case makes, the agent ends a reply with a question to the person that names the test and its failure.
> **＋** When the auto mode classifier of Claude Code refuses a tool call that the run needs, the agent ends a reply with a question to the person that gives the shell command doing what the refused call would do, for the person to type after `!` in the prompt.
> **＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
> **＋** After the person's answer the run goes on from where it stopped.
> **＋** After the person has run the command that a refusal of the auto mode classifier gave, the run goes on from where it stopped.
> **＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
> **－** No other point stops the run: any other red test, at `/retro` too, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

> **tasks:**
> - [ ] update `rule-where-to-stop`
>   - old: `` 6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; show what stopped it, and go on after the person's word. ``
>   - new: `` 6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; or, in the merge tasks of the opening Case of a sprint, `git merge --ff-only` or `git branch -d` refuses: show what stopped it, and go on after the person's word (case 775.3). ``
>   - change: `condition 6 also covers a refused merge or branch deletion in the merge tasks of the opening Case of a sprint`
> - [ ] `uv run guppi render`: `vault/wiki/where-to-stop.md`
> - [ ] update `estimate-where-to-stop-stops-only-on-its-conditions`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a refused merge or branch deletion in the merge tasks of the opening Case of a sprint is a stop`
> - [ ] read `estimate-where-to-stop-stops-only-on-its-conditions`

> **ratification:**
> ```
> - decision[case 775.3][update][rule-where-to-stop]{ref:rule-where-to-stop}
> - decision[case 775.3][update][estimate-where-to-stop-stops-only-on-its-conditions]{ref:rule-where-to-stop}
> ```
