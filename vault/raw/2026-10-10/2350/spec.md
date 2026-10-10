<!-- approved 01:16:38 · session a54efc99 -->

# Session 2350 — sprint plugin

## Case 773 — A superseded page takes its History line once

> **context:**
> When a later Case supersedes an earlier one, `guppi generate` marks the earlier Decision page `superseded`, adds the new page to its `superseded_by` and writes one History line `superseded by decision-case-<N>`; each History line is copied into `vault/wiki/log.md`. The same step marks the pages of the earlier Case's sub-cases. In `guppi/generate.py` the step for a page named in `supersedes` adds the slug to `superseded_by` only when it is not there, but writes the History line either way; the step for a sub-case writes it only when it adds the slug. Last session one decision line of the ledger `raw/2026-10-10/1913/ledger.md` superseded case 764 and case 764.1 together: the parent step marked `decision-case-764.1` first, then the named step wrote its line again. A Grep `decision-case-764.1 superseded` over `vault/wiki/log.md` printed two lines, and the archived page `vault/archive/plugin/2026-10-10/1913/decisions/decision-case-764.1.md` holds the line twice in its History. The person chose to leave those two lines as the record of that run; only later runs change. The code breaks a promise that already stands: the Criterion of `estimate-generate-writes-the-decision-page` says a page whose `superseded_by` already names the new page gets no second History line, and the Purpose of `rule-page-generation` says an archived page takes one History line. The person chose to replace that Criterion whole, the line made explicit for a page marked earlier in the same record, so that the Estimate goes `pending` and the Retro of this session reads it again; the old line on a page whose `superseded_by` already names the new page is not carried as it stood, since its new form in `then` says the same and adds the `log.md` line and the earlier step of the same record. Its `method` ends with a live reading in the librarian's run, which the check of `/pre-spec` refuses on a Criterion replaced whole as a method that waits for another session, so the update sets the method to the test run alone; its `purpose` names no supersede and stands. A Grep `superseded by` over `guppi/` printed `guppi/generate.py` and `guppi/prespec.py`; the hits in `guppi/prespec.py` are the text of a finding on a Case still in the plan, not this judgment, so the check of `superseded_by` before the History line lives in `guppi/generate.py` alone and the task moves both its copies there into one helper. A Grep `estimate-generate-writes-the-decision-page` over `tests/` printed `tests/test_generate.py`, a comment line, so no test reads that page live. A Grep `one History line|superseded_by` over `vault/wiki/rules/` printed `rule-raw-archive.md`, `rule-page-generation.md`, `rule-materialize.md` and `rule-decisions-schema.md`, and over `.claude/` printed nothing; the hits in `rule-page-generation.md` and `rule-decisions-schema.md` already state one mark per page, the other two speak of the marks of the yaml, and none is made false.

> **problem:**
> `guppi generate` writes the History line `superseded by` a second time, and a second line in `vault/wiki/log.md`, when one record supersedes an earlier page that an earlier step of the same record already marked, such as a sub-case whose parent the same line supersedes.

> **recommend:**
> - **How should the doubled line be prevented?**
>   - Recommended: (a) write the line only when the name is new; one helper holds the check and both steps call it; a test supersedes a parent and one of its sub-cases in one line.
>   - Answer: agreed, (a).
> - **What about the two doubled lines already written?**
>   - Recommended: (a) leave them as the record of that run.
>   - Answer: agreed, (a).
> - **Which check confirms the fix?**
>   - Recommended: (b) replace the Criterion of `estimate-generate-writes-the-decision-page` whole, its line made explicit for a page marked earlier in the same run, so it goes `pending` and the Retro of this session reads it again.
>   - Answer: agreed, (b).

> **given:**
> `estimate-generate-writes-the-decision-page`: its Criterion is replaced whole and its method set anew.
> **＋** `rule-page-generation`: the rule the Estimate checks.
> **＋** `rule-one-judgment-one-implementation`: one check of `superseded_by` in one place.
> **＋** `guppi/generate.py`: writes the Decision pages and the `superseded by` History lines.
> **＋** `tests/test_generate.py`: the tests of the Decision page.
> **＋** `materialize.yaml`: the yaml whose entries and `decisions` records `generate` applies.
> **＋** `vault/wiki/decisions/decision-case-<N>.md`: a Decision page, live in `vault/wiki/decisions/` or archived under `vault/archive/`.
> **＋** `vault/wiki/log.md`: the feed that takes a copy of each History line.

> **when:**
> `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

> **then:**
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
> **＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded`, unless it stands `archived`, and appends to its `superseded_by`, and does the same to each page in the `children` of the earlier page, at any depth, that stands `current`, a page of an earlier session too. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
> **＋** An earlier page that stands `archived`, under `vault/archive/` or under `vault/wiki/decisions/`, keeps `status: archived` and its place; it takes the new page into its `superseded_by` with one History line `superseded by decision-case-<N>`, and it removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, as for a page that stands `current`.
> **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`; neither does a page reached only through `children` clear a `deferred_by`.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
> **－** The Decision pages already written are not rewritten.
> **－** A page whose `superseded_by` already names the new page gets no second History line and no second line in `vault/wiki/log.md`, whether an earlier run put the name there or an earlier step of the same record did, such as a sub-case page reached through the `children` of its parent and named in `supersedes` too.
> **－** A page in `children` that stands `archived` or `superseded` is left as it is.
> **－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.

```then
update:
- slug: estimate-generate-writes-the-decision-page
  set:
    status: pending
    method: uv run pytest tests/test_generate.py, the tests of the Decision page
  change: the Criterion replaced whole — a page whose superseded_by already names the new page, by an earlier step of the same record too, gets no second History line and no second log line; the method is the test run alone
```

```tasks
- [x] `guppi/generate.py`: one helper adds the superseding page to `superseded_by` and writes the History line only when it adds it; the step for a page named in `supersedes` and the step for a sub-case both call it.
- [x] `tests/test_generate.py`: a record supersedes a parent and one of its sub-cases; the sub-case page holds one `superseded by` History line and `vault/wiki/log.md` one line for it; the test fails without the change of `guppi/generate.py`.
- [ ] update `estimate-generate-writes-the-decision-page`
- [ ] read `estimate-generate-writes-the-decision-page`
```

## Case 774 — The opening-and-close note leaves the current milestone

> **context:**
> The sprint page `entity-sprint-plugin` lists its milestones in order, and `guppi sprint` renders them into `vault/wiki/sprint.md`. A milestone line that names no page is a note: it is never ticked, and it keeps its milestone open until a Case removes it or cuts it into items (`rule-sprint`). The current milestone `The sprint turn and GitHub` opens with the note on the opening and the close of a sprint. That note can end only when `plugin` closes, so the milestone would stay open to the end of the sprint. The person found this odd and asked to decide now what can be decided. The close is already held twice: the last milestone `The plugin` ends with the close line, and the Done-when Estimate `estimate-sprint-plugin-close-steps-run-from-the-line` checks the closing session from that line. The skill `/sprint-close` puts off every other open line of the closing session (`rule-skill-sprint-close`, step 2), so a note moved there would only be put off. The next opening of a sprint comes after `plugin` closes, so none of the five Done-when Estimates of `entity-sprint-plugin` checks an opening. Its one known flaw, the merge step deferred by case 771, is the Frontier item C9 of this session, ratified as Case 775: its sub-case 775.1 creates `estimate-skill-sprint-open-merges-the-closed-sprint-branch`, a check of the text of the skill `/sprint-open` read at the Retro of this session, which targets `rule-skill-sprint-open` and not the sprint page. The person chose to remove the note, and to make the Purpose name only the close, since none of the Done-when Estimates of `entity-sprint-plugin` covers the opening. The pair on the Purpose and the `set` of `purpose` change the one sentence of the page that names the opening. The Done-when sentence of the Purpose already names only the close and stands. The close line of `The plugin` stands as it is, so the Criterion of `estimate-sprint-plugin-close-steps-run-from-the-line`, which quotes that line, stands. The Criterion of `estimate-sprint-renders-the-backlog` states how a note renders and keeps its milestone open, for any sprint page. It checks the render of this change and stands. A Grep `opening and (the )?close of a sprint` over the repository, `vault/raw/` left out, printed `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/entities/entity-sprint-plugin.md` and `vault/wiki/lessons/lesson-hi-brief-line-judged-apart-from-a-broad-milestone-line.md`. `sprint.md` is rendered anew by the task of this Case. The brief is written anew by the librarian's next run. The lesson's trigger records what happened in an earlier session and stays true. The current milestone does not close by this Case: its line on the repository on GitHub keeps it open.

> **problem:**
> The current milestone of `entity-sprint-plugin` holds a note that can end only at the close of the sprint, which is already the last line of the last milestone, so the current milestone cannot close before the sprint does.

> **recommend:**
> - **Where does the opening-and-close note go?**
>   - Recommended: (a) remove the note; the close line of the last milestone and its Done-when check hold the close, and the other Case of this batch holds the known flaw of the opening.
>   - Answer: agreed, (a).
> - **Does the sprint Purpose still name the opening?**
>   - Recommended: (b) change the Purpose and its `purpose` field to name only the close, since nothing in this sprint checks the opening.
>   - Answer: agreed, (b).

> **given:**
> `entity-sprint-plugin`: the sprint page whose milestone note and Purpose change.
> **＋** `vault/wiki/sprint.md`: the file `guppi sprint` writes from the sprint page.
> **＋** `estimate-sprint-plugin-close-steps-run-from-the-line`: the Done-when check of the close, which quotes the close line.
> **＋** `estimate-sprint-renders-the-backlog`: the check of the render of `vault/wiki/sprint.md`.
> **＋** `rule-sprint`: a note leaves its milestone only by a Case.

> **when:**
> `uv run guppi sprint` writes `vault/wiki/sprint.md` from `entity-sprint-plugin`, and someone reads the page or the file.

> **then:**
> The milestone `The sprint turn and GitHub` of `entity-sprint-plugin` holds the line on the repository on GitHub alone.
> **＋** The Purpose of `entity-sprint-plugin` and its `purpose` field say that the close of a sprint works with no fix by hand, and do not name the opening.
> **－** The close line of the milestone `The plugin` stays as it was, as `estimate-sprint-plugin-close-steps-run-from-the-line` quotes it.
> **－** The milestone `The sprint turn and GitHub` does not close by this change: its line on the repository on GitHub keeps it open.

```then
update:
- slug: entity-sprint-plugin
  replace:
  - old: and the opening and close of a sprint work with no fix by hand.
    new: and the close of a sprint works with no fix by hand.
  - old: |-
      - the opening and the close of a sprint run with no fix by hand and each flaw found in them is fixed
      - the repository on GitHub set up so that a pull request from another person is easy to review
    new: '- the repository on GitHub set up so that a pull request from another person is easy to review'
  set:
    purpose: 'GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand'
  change: the note on the opening and the close of a sprint leaves the milestone The sprint turn and GitHub; the Purpose names only the close
```

```tasks
- [ ] update `entity-sprint-plugin`
- [ ] `uv run guppi sprint`
```

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

```then
create:
- slug: estimate-skill-sprint-open-merges-the-closed-sprint-branch
  ref: rule-skill-sprint-open
  kind: QA
  purpose: Whether /sprint-open has the opening Case merge the closed sprint's branch into main by a fast-forward as the first tasks of Work Mode and move the work to a branch named by the new sprint, with a stop on a refusal and no git task on main
  method: by hand, at the Retro of the session of case 775, the new Render of rule-skill-sprint-open in its spec.md read against the Criterion
  tags:
  - sprint
  - git
  - workflow
update:
- slug: rule-skill-sprint-open
  replace:
  - old: '4. The skill decides none of the answers:'
    new: |-
      4. Write into the same prompt the branch that `/hi` printed under `Branch:`. When it is not `main`, the closed sprint ran on it, and the opening Case holds as its first task lines `git switch main`, `git merge --ff-only <branch>`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint. The Spec holds the opening Case first, so Work Mode runs them before any other task: `main` takes the work of the closed sprint by a fast-forward, and the rest of Work Mode runs on the branch `<id>`. A refusal of the merge or of the deletion is a stop on the sixth condition of `vault/wiki/where-to-stop.md`. When the branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it. The opening Case puts no question on the merge or the branch to the person (case 775.1).
      5. The skill decides none of the answers:
  change: the opening Case of a sprint merges the closed sprint's branch into main by a fast-forward and moves the work to a branch named by the new sprint
```

```tasks
- [ ] update `rule-skill-sprint-open`
- [ ] `uv run guppi render`: `.claude/skills/sprint-open/SKILL.md`
- [ ] create `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
- [ ] read `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
```

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

```then
update:
- slug: rule-skill-sprint-close
  replace:
  - old: When the sprint ran on a branch of its own, the closing Case holds too the task line ``the merge of `<branch>` into `main` — the first work of the session that opens the next sprint, after its opening Case``, which Work Mode leaves unticked, so that the brief gives it under `Work` to that session.
    new: 'The closing Case holds no task line for the merge of the sprint''s branch into `main`: the opening Case of the next sprint holds the merge, as `/sprint-open` sets it (case 775.2).'
  change: the closing Case leaves no merge line; the opening Case of the next sprint holds the merge
- slug: estimate-skill-sprint-close-leads-the-closing-session
  set:
    status: pending
    method: by hand, at the Retro of the session of case 775, the new Render of rule-skill-sprint-close in its spec.md, vault/wiki/orchestration.md and entity-sprint-migration under vault/archive/migration/ read against the Criterion
  change: the Criterion replaced whole — the closing Case holds no merge line, the opening Case of the next sprint holds the merge
```

```tasks
- [ ] update `rule-skill-sprint-close`
- [ ] `uv run guppi render`: `.claude/skills/sprint-close/SKILL.md`
- [ ] update `estimate-skill-sprint-close-leads-the-closing-session`
- [ ] read `estimate-skill-sprint-close-leads-the-closing-session`
```

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

```then
update:
- slug: rule-where-to-stop
  replace:
  - old: '6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; show what stopped it, and go on after the person''s word.'
    new: '6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; or, in the merge tasks of the opening Case of a sprint, `git merge --ff-only` or `git branch -d` refuses: show what stopped it, and go on after the person''s word (case 775.3).'
  change: condition 6 also covers a refused merge or branch deletion in the merge tasks of the opening Case of a sprint
- slug: estimate-where-to-stop-stops-only-on-its-conditions
  set:
    status: pending
  change: the Criterion replaced whole — a refused merge or branch deletion in the merge tasks of the opening Case of a sprint is a stop
```

```tasks
- [ ] update `rule-where-to-stop`
- [ ] `uv run guppi render`: `vault/wiki/where-to-stop.md`
- [ ] update `estimate-where-to-stop-stops-only-on-its-conditions`
- [ ] read `estimate-where-to-stop-stops-only-on-its-conditions`
```
