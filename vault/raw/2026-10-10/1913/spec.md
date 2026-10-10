<!-- approved 21:05:20 · session 57f8857a -->

# Spec — session 1913, 2026-10-10

## Case 765 — The README check names its moment

> **context:**
> `estimate-sprint-plugin-readme-describes-the-project`, one of the five Estimates of `entity-sprint-plugin` (case 756.3), asks the person whether `README.md` says what GUPPI is, names its main parts and says how to install and use it. Its `method` reads "by hand, the person's answer on README.md, in a session of the sprint plugin before its close". Each session of the sprint is such a session, so `/hi` takes the reading as due at every opening. The README is not written yet: `README.md` still opens with the heading `# Vault harness`, and the README is a line of the milestone The plugin, the last of the page. So `/hi` of this session could not run the reading and wrote it as line C7 of the Frontier (case 670.6), and it would do so again at each opening until that milestone. The `purpose` and the Criterion of the page are sound and stand: they check what the README says, not when it is read. This Case changes only the `method`, so that it names the moment of the reading: the `/hi` of the session after the one whose Work Mode writes `README.md` under the milestone The plugin, before the close of the sprint. The first build named the Retro of the session that writes the README; pre-spec found that `rule-retro` does not let Retro take it, since `/retro` reads "A reading whose `method` names the person's word is not yours to take: it is a line of `## Ask the person` of `handoff.md`" and its reply "asks the person nothing (case 569.1)". So the Retro of the session that writes the README puts the check under `## Ask the person` of its handoff, the brief carries it into `Ask the person` of Next session, and `/hi` of the next session puts the question to the person. Case 764 of this batch sets what the brief, `/hi` and `/retro` do with a check of the live sprint page before its moment, and this Case does not cover that moment. Its file, as read at this build, keeps under 764.1 every reading of the live sprint page out of `Ask the person` of Next session; the person's answer on the pre-spec report rebuilds Case 764 so that 764.1 lets in a check of the live sprint page whose work is finished, and this Case rests on that change. This Case adds no Estimate: a `set` of the `method` alone leaves the Criterion and the status of the page as they stand (case 378.4), and what checks that the moment is kept is the rule of Case 764, through the Estimates whose Criteria it replaces. The new `method` names the person, so `lint.waits_for_another_session` of `guppi/lint.py`, which `pre-spec` runs over the plan, does not report it. A Grep `estimate-sprint-plugin-readme-describes-the-project` over `vault/wiki/` printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/entities/entity-sprint-plugin.md`; the brief and the log are not read, and the page lists the Estimate in `estimates` and in History only, and its Purpose, that each Estimate of the page is read before the close of the sprint, stays true. A Grep `sprint-plugin|readme` over `tests/` printed nothing, so no test reads this page live.

> **problem:**
> The `method` of the README check names no moment closer than any session of the sprint before its close, so each opening of the sprint takes as due a reading that cannot run until the README is written.

> **recommend:**
> - **What does this Case change on the README check?**
>   - Recommended: (a) name the moment in the method: the person reads `README.md` in the session of the sprint plugin that writes the README of the last milestone, before the close; the Criterion and the purpose stay.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: pre-spec found that Retro cannot take the person's answer, since Retro asks the person nothing; the person took its recommended fix: the answer is taken at the `/hi` of the session after the one whose Work Mode writes `README.md`, where the Retro of that session puts the check under `## Ask the person` of the handoff and the brief carries it into `Ask the person`.
>   - Taken: the `method` names the `/hi` of the session after the one that writes `README.md`, before the close of the sprint; Case 764 is rebuilt so that the brief lets in such a check.

> **given:**
> `estimate-sprint-plugin-readme-describes-the-project`: the README check, whose `method` changes.
> **＋** `entity-sprint-plugin`: the sprint page, whose milestone The plugin holds the README line.
> **＋** `README.md`: the description of the project at the root of the repository.
> **＋** `rule-retro`: Retro, which puts a reading that needs the person's word under `## Ask the person` of the handoff.
> **＋** `/hi`: the skill that puts the questions of `Ask the person` to the person.
> **＋** `vault/raw/2026-10-10/1913/cases/case-764.md`: the rule of this batch for the checks of a sprint page that wait for their moment.

> **when:**
> In a session of the sprint `plugin`, the agent reads the `method` of `estimate-sprint-plugin-readme-describes-the-project` to judge whether its reading is due.

> **then:**
> The `method` names the moment of the reading: the `/hi` of the session after the one whose Work Mode writes `README.md` under the milestone The plugin of `entity-sprint-plugin`, before the close of the sprint.
> **＋** The reading is the person's answer on `README.md`, by hand, to the question that the Retro of `rule-retro` in the session that writes `README.md` puts under `## Ask the person` of its handoff.
> **－** The Criterion and the `purpose` of `estimate-sprint-plugin-readme-describes-the-project` do not change.

```then
update:
- slug: estimate-sprint-plugin-readme-describes-the-project
  set:
    method: by hand, the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint
  change: 'the method names the moment of the reading: the /hi of the session after the one that writes the README'
```

```tasks
- [x] update `estimate-sprint-plugin-readme-describes-the-project`
```

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

```then
update:
- slug: estimate-sprint-plugin-pull-requests-reviewed-on-github
  set:
    status: pending
    purpose: Whether a pull request from another account, a second account of the owner included, runs the checks of CI on GitHub and can be reviewed and merged into the branch plugin
  change: the Criterion replaced whole — the pull request goes against the branch plugin, and a second account of the owner counts as another account
```

```tasks
- [x] update `estimate-sprint-plugin-pull-requests-reviewed-on-github`
- [ ] read `estimate-sprint-plugin-pull-requests-reviewed-on-github`
```

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

```then
update:
- slug: estimate-sprint-plugin-ci-writes-a-clean-branch
  set:
    status: pending
  change: the Criterion replaced whole — CI starts on a commit to the branch plugin, where the sprint commits
```

```tasks
- [x] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
- [ ] read `estimate-sprint-plugin-ci-writes-a-clean-branch`
```

## Case 768 — The install check waits for the plugin milestone

> **context:**
> `estimate-sprint-plugin-installs-as-a-plugin` is one of the five Estimates of `entity-sprint-plugin`, created by case 756.6. It checks that the clean branch installs as a Claude Code plugin into an empty project and that `/hi` opens a session there. Its method waits for an install of the clean branch in a session of the sprint `plugin` before its close. No clean branch exists today: a Glob `.git/refs/**/*` printed only `.git/refs/heads/main` and `.git/refs/heads/plugin`, and `.git/packed-refs` holds only the tag `vault-v1`. The plugin is the third milestone of `entity-sprint-plugin`, and the first milestone is not done: `entity-sprint-plugin` is still `draft`, and the Frontier of this session puts both items of that milestone off, C1 and C2 closed `· sprint · defer`. So `/hi` could not take the reading of W6, and `rule-skill-hi` made it the Cases line C10. Case 764 of this session, built in the same batch, sets when an Estimate of a sprint page is read and that Retro leaves it `pending`. That rule decides this item: the method of this Estimate already names a session of its sprint before its close, so neither the method nor the Criterion changes. This Case adds only a History line on the page that says why the reading waits. The promise does not change, so the Criterion stands and the status stays `pending`; the install itself is read by this same Estimate at its moment. A Grep `installs-as-a-plugin|entity-sprint-plugin` over `tests/` printed no file, so no test reads the page live.

> **problem:**
> The install check cannot be read now, since no clean branch exists before the plugin milestone, and its open reading came onto the Frontier as an item that needs a decision.

> **recommend:**
> - **What does this Case do with the install check?**
>   - Recommended: (a) keep the check as it stands, and record why it waits.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: pre-spec found that `context` said the first milestone stands open on the Frontier, while the Frontier puts both its items off; the person agreed to fix the wording.
>   - Taken: `context` says the milestone is not done, the sprint page still `draft` and both its items put off on the Frontier.

> **given:**
> `estimate-sprint-plugin-installs-as-a-plugin`: the check of the install, whose History gains a line.
> **＋** `entity-sprint-plugin`: the sprint page, whose third milestone makes the plugin.

> **when:**
> Someone reads `estimate-sprint-plugin-installs-as-a-plugin` before the third milestone of `entity-sprint-plugin` is reached.

> **then:**
> The page keeps its method, its Criterion and its status.
> **＋** Its History says that the reading waits for the third milestone of `entity-sprint-plugin`, since no clean branch exists to install before it.
> **－** The History line does not set the session of the reading.

```then
update:
- slug: estimate-sprint-plugin-installs-as-a-plugin
  change: the reading waits for the milestone The plugin of entity-sprint-plugin; no clean branch exists to install before it
```

```tasks
- [x] update `estimate-sprint-plugin-installs-as-a-plugin`
```

## Case 769 — The opening of a sprint comes before the Frontier

> **context:**
> When the last sprint is closed, the hook `guppi sprint --hi` tells the agent at `/hi` to start `/sprint-open` before the Frontier. But step 1 of `/sprint-open` assembles the Frontier first, with the line `open the next sprint` of the brief as its first Cases line, and `/hi` puts no milestone item on the Frontier while that line stands. So in session 1713 the opening was one Frontier line among six, and the first milestone of `plugin` could not be taken up in the session that opened it; the handoff of that session records that the person felt the opening was one more Frontier item rather than a step of its own. The person chose this: the opening Case comes first, before any Frontier; before the reply that acknowledges it the agent assembles and writes the whole Frontier and takes the readings that `/hi` takes, and that reply shows the Frontier and puts the Ask questions; the Frontier of that session takes the items of the first milestone from the opening Case, since `vault/wiki/sprint.md` shows the new sprint only after the librarian's run; the close of a sprint waits for the close of `plugin`, where `estimate-sprint-plugin-close-steps-run-from-the-line` judges it; the questions of the opening Case stay. Case 769.1 changes `/sprint-open`, Case 769.2 what the Frontier holds at an opening, Case 769.3 the moment of the readings of `/hi`, Case 769.4 the acknowledging reply of the opening Case, and Case 769.5 the check of the session after a close; each replaces the Criterion of the one Estimate whose Criterion speaks of its change, or creates one. Not this Case: the merge of the branch of the closed sprint at the opening (Frontier item C4) and the archive folder `guppi cleanup` picks for the pages of the opening session (C6). The hook needs no change: `hi_hook` of `guppi/sprint.py` already prints that `/sprint-open` starts before the Frontier, so `estimate-skill-sprint-open-starts-at-hi` stands. A milestone item of the opening session closes `case N` only with an `update` of the sprint page under Case N, by `updates_the_sprint` of `guppi/prespec.py`, and `apply` of `guppi/generate.py` applies the entries of a ledger in their order, so such an `update` lands after the `create` of the same session. A Grep `` open the next sprint|628\.7|before the Frontier `` over `vault/wiki/`, `log.md` and `brief.md` left out, printed `rules/rule-skill-hi.md`, `rules/rule-skill-sprint-open.md` and `estimates/estimate-skill-sprint-open-asks-the-opening-questions.md`, `estimates/estimate-hi-writes-frontier.md` and `estimates/estimate-hi-takes-its-readings.md`, which this Case changes; `rules/rule-brief.md` and `estimates/estimate-brief-written.md`, which set that the brief writes the line, still true; `estimates/estimate-sprint-close-next-session-opens-the-sprint.md`, whose Criterion line that `/hi` writes the opening line first under `## Cases` becomes false, so Case 769.5 replaces its Criterion and points to `estimate-hi-writes-frontier` for where the line stands; its old `method` named the transcript of an earlier session and the session after a close, which the person in Case 764 left for a later Case before the close of `plugin`; the check of a kept method refused it once its Criterion is replaced, so the person chose that Case 769.5 sets it anew to the tests and a reading by hand at the Retro of this session, and the live look at the next opening stays with the person's answer that `estimate-hi-writes-frontier` asks; `estimates/estimate-hi-takes-a-conserved-spec.md`, whose trigger is the brief line and whose promise, no conserved Spec at an opening, Case 769.2 keeps; and `estimates/estimate-skill-sprint-open-starts-at-hi.md`, which stands as said. A Grep `` first reply of `?/hi|its first reply|in the first reply `` over `vault/wiki/rules/`, `vault/wiki/estimates/` and `.claude/` printed `rules/rule-case-protocol.md` and `rules/rule-skill-hi.md` in History lines; `rules/rule-orchestration.md`, whose sentence that the first reply of `/hi` keeps the form `rule-skill-hi` sets stays true; `estimates/estimate-hi-takes-its-readings.md`, which Case 769.3 changes; and `estimates/estimate-orchestration-shows-the-frontier-after-a-closed-line.md`, whose trigger is a reply with no ratification, so the acknowledging reply of the opening Case is not under it and it stands. In `rule-orchestration`, read whole, the sentence that the Frontier is written at `/hi` becomes false and Case 769.4 changes it; the four parts of the acknowledging reply stay, the Ask questions standing after the checklist and before the last question, so `estimate-orchestration-acknowledging-reply` stands. In `rule-session-start`, read whole, the sentence that the Frontier is assembled from `brief.md` and `sprint.md` and the sentence that the first turn presents it become false at an opening, and Case 769.2 replaces both; the method of `estimate-hi-writes-frontier` named the `/hi` of the session after a close, where no Frontier now stands, and Case 769.2 sets it to the reply that acknowledges the opening Case; its Estimate `estimate-session-start-context` speaks of the loaded context and stands. A Grep `` skills.{0,3}(hi|sprint-open)|rule-skill-hi|rule-skill-sprint-open|estimate-hi-writes-frontier|estimate-skill-sprint-open `` over `tests/` printed `tests/test_prespec.py`, `tests/test_guard.py`, `tests/test_ratified.py`, `tests/test_sprint.py` and `tests/test_lint.py`; they use the paths under a temporary folder or as strings, or the line of the hook, which does not change. `tests/test_orchestration.py` reads `vault/wiki/orchestration.md` live, only its blocks tagged `showing` and `defer`, and the pairs of Case 769.4 add no block. Each Criterion this Case replaces drops on purpose the lines it changes: the first two lines of the old Criterion of `estimate-skill-sprint-open-asks-the-opening-questions`, which put the Frontier before the dispatch; the lines of `estimate-hi-writes-frontier` that set the opening line open, no milestone item at an opening and the checklist of the first reply, reworded with the old closer lines joined into one line and Pre-spec named `/pre-spec`; the line of `estimate-hi-takes-its-readings` that set the readings in the first reply; and the line of `estimate-sprint-close-next-session-opens-the-sprint` that had `/hi` write the opening line. The `then` lines of the sub-cases share words, since each speaks of the same Frontier, but each signs another moment: the dispatch (769.1), what the Frontier holds (769.2), the reply in which `/hi` reads (769.3) and the reply that acknowledges the opening Case (769.4). The files of Cases 764 and 767 were read: Case 764 changes neither `rule-skill-hi` nor these Estimates, and its sentences that keep a check of a sprint close off the Frontier stay in the new Criterion of `estimate-hi-takes-its-readings`.

> **problem:**
> The opening of a sprint is one Frontier line among others, so the session that opens a sprint cannot take up the first milestone of that sprint, and the opening is not a step of its own.

> **recommend:**
> - **Is the opening a Frontier line, a step before the Frontier, or a session of its own?**
>   - Recommended: (b) a step before the Frontier: `/sprint-open` runs first, and once the opening Case is ratified the Frontier is built with the items of the new first milestone.
>   - Answer: agreed, (b).
> - **Does the close change now, or wait for the close of `plugin`?**
>   - Recommended: (a) the close waits; it is judged at the close of `plugin`, and a flaw seen then becomes a Case.
>   - Answer: agreed, (a).
> - **Do the questions of the opening Case stay as they are?**
>   - Recommended: (a) keep the questions.
>   - Answer: agreed, (a).
> - **Where do the readings and the Ask questions of `/hi` go in the session that opens a sprint?**
>   - Recommended: (a) all of it after the opening: the reply that confirms the opening Case writes the whole Frontier, takes the readings and puts the Ask questions before the question which item is next.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the fixes of the findings of `/pre-spec`: one wording across the sub-cases for when `frontier.md` is written; the sentences of `rule-session-start` that become false replaced; the method of `estimate-hi-writes-frontier` set to the new moment; and the Criterion of `estimate-sprint-close-next-session-opens-the-sprint` replaced, its method left as it is.
>   - Taken: every sub-case says the Frontier is assembled and written before the reply that acknowledges the opening Case, which shows it; Case 769.2 replaces the sentences of `rule-session-start` on the sources and the first turn and sets the method; Case 769.5 replaces the Criterion of `estimate-sprint-close-next-session-opens-the-sprint`.
> - **How is the check of the session after a close read, now that it cannot wait for that session?**
>   - Recommended: (a) the tests of the ledger refusal and of the sprint id on the pages, and a reading by hand at the Retro of this session of the new texts of `/hi` and `/sprint-open` in its Spec.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the confirmation of `/pre-spec` found that the `purpose` of the new Estimate of Case 769.4 and the `change` line of its `rule-orchestration` update still said that the acknowledging reply writes the Frontier; the person chose to fix them.
>   - Taken: both say that the Frontier is written and the readings taken before that reply, which shows the Frontier.

### Case 769.1 — The opening Case comes before any Frontier

> **given:**
> `rule-skill-sprint-open`: the skill of the opening, rendered into `.claude/skills/sprint-open/SKILL.md`.
> **＋** `estimate-skill-sprint-open-asks-the-opening-questions`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-skill-hi`: the skill `/hi`, whose Frontier waits for the opening Case.
> **＋** `vault/wiki/sprint.md`: the rendered sprint, whose first heading marks the last sprint closed.
> **＋** `vault/wiki/brief.md`: the brief, whose first line of `Cases` opens the next sprint.
> **＋** `vault/wiki/backlog.md`: the items without a turn.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/sprint-close`: the skill that the close line of the new sprint page starts.

> **when:**
> The main agent starts the skill `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, in a session whose `vault/wiki/sprint.md` marks the last sprint closed.

> **then:**
> Before any Frontier is assembled, the main agent dispatches `case-guppi` for the line `open the next sprint` of the `Cases` of Next session in `vault/wiki/brief.md`, with the questions of the opening in the prompt of the call: the id of the sprint, its goal in one sentence, its Definition of done as Estimates, and the first milestone and its items.
> **＋** The prompt asks that the opening Case say how many items `vault/wiki/backlog.md` holds and ask the person whether to take any of them.
> **＋** The prompt asks that the opening Case write, as the last item of the last milestone of the new sprint page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``.
> **＋** The opening Case is the first Case the session ratifies.
> **－** No Frontier is assembled, written to `raw/<date>/<hi HHMM>/frontier.md` or shown, and no other item is taken up, before the person ratifies the opening Case.
> **－** The opening Case goes through no item of `vault/wiki/backlog.md` that the person does not name.
> **－** The skill decides none of the answers: `case-guppi` puts each to the person in a round.

```then
update:
- slug: rule-skill-sprint-open
  replace:
  - old: '1. Assemble the Frontier as `/hi` sets it: the line `open the next sprint` of the brief stands first under `## Cases`, and no item of the closed sprint and no conserved Spec stands there.'
    new: '1. Assemble no Frontier yet: the opening Case comes first, and no other item of the session is taken up before the person ratifies it (case 769.1).'
  - old: 2. When the person takes up that line, dispatch `case-guppi` for it as
    new: 2. Dispatch `case-guppi` at once for the line `open the next sprint` of the brief, as
  - old: and the person ratifies the opening Case as any other.
    new: and the person ratifies the opening Case as any other. Before the reply that acknowledges it, assemble and write the Frontier as `/hi` sets it, the items of the first milestone of the opening Case among its Cases; that reply shows it, as `vault/wiki/orchestration.md` sets that reply (case 769.4).
  change: the opening Case comes before any Frontier, and the reply that acknowledges it brings the Frontier (case 769.1)
- slug: estimate-skill-sprint-open-asks-the-opening-questions
  set:
    status: pending
    purpose: Whether /sprint-open has the opening Case of a sprint dispatched before any Frontier, ask its id, its goal, its Definition of done, its first milestone and whether to take an item of the backlog, and write the close line
    method: by hand, at the Retro of the session of case 769, the new Render of rule-skill-sprint-open in its spec.md read against the Criterion
  change: the Criterion replaced whole — the opening Case is dispatched before any Frontier
```

```tasks
- [x] update `rule-skill-sprint-open`
- [x] update `estimate-skill-sprint-open-asks-the-opening-questions`
- [x] `uv run guppi render`: `.claude/skills/sprint-open/SKILL.md`
- [x] read `estimate-skill-sprint-open-asks-the-opening-questions`
```

### Case 769.2 — At an opening the Frontier takes the first milestone from the opening Case

> **given:**
> `rule-skill-hi`: the skill `/hi`, rendered into `.claude/skills/hi/SKILL.md`.
> **＋** `rule-session-start`: the start of a working session, whose first turn presents the Frontier.
> **＋** `estimate-hi-writes-frontier`: its Criterion is replaced whole.
> **＋** `rule-skill-sprint-open`: the skill of the opening, `/sprint-open`, whose opening Case comes first.
> **＋** `vault/wiki/orchestration.md`: the take-back of a ratified Case, which a closed line may follow.
> **＋** `entity-sprint-<id>`: the new sprint page that the opening Case creates.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the case file of the opening Case.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`: the sources of the Frontier.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/pre-spec`: the check that fails on an open Cases line.

> **when:**
> The person invokes `/hi` of `rule-skill-hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md`, the output of the skill's commands and, in the session that opens a sprint, the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of the opening Case, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line, closed `[x] … · case N` by the opening Case of `/sprint-open`; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone of `vault/wiki/sprint.md`, or, while that opening line stands, the items of the first milestone that the `create` of `entity-sprint-<id>` writes under `## Milestones` in the case file of the opening Case, with the source `sprint`; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an open `W` line whose reading cannot run now, written by the reading step of `/hi`; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** A line of the `Cases` of the brief's Next session that names the same item as a line of the current milestone makes no line of its own. The milestone line stands as the sprint page, or the opening Case, gives it, with the source `sprint` alone. The agent judges the sameness by meaning, with no page opened.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`. An item closed `defer` or `kept` has no short Case and no ledger line, but for the short Case of a take-back of a ratified Case, as `vault/wiki/orchestration.md` sets it, and a sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** When the first reply of `/hi` shows the Frontier, the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`, and a `C` that needs none closes `· work`.
> **－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of `vault/wiki/sprint.md` is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** `/pre-spec` finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: Assemble the Frontier from the above in three lists, the kind of each item by its source and no page opened (case 268.2).
    new: 'When the first line of the `Cases` of the brief''s Next session opens with `open the next sprint`, start `/sprint-open` first, as the hook on `/hi` says: the opening Case comes before the Frontier; before the reply that acknowledges it, assemble and write the Frontier below and take its readings, and that reply shows it and puts the questions of its `A` lines, as `vault/wiki/orchestration.md` sets that reply (case 769.2). Assemble the Frontier from the above in three lists, the kind of each item by its source and no page opened (case 268.2).'
  - old: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line (`rule-sprint-close`, case 628.7);
    new: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line, closed `[x] … · case N` by the opening Case (`rule-sprint-close`, cases 628.7, 769.2);
  - old: and none of a later milestone, of the Backlog or of Closed (case 229.3), and none at all while that opening line stands (case 628.7);
    new: and none of a later milestone, of the Backlog or of Closed (case 229.3); while that opening line stands, no item of `sprint.md`, which shows the new sprint only after the librarian's run, but the items of the first milestone that the `create` of `entity-sprint-<id>` writes under `## Milestones` in the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of the opening Case, each with the source `sprint` (case 769.2);
  change: at the opening of a sprint the Frontier comes after the opening Case and takes the first milestone from it (case 769.2)
- slug: rule-session-start
  replace:
  - old: 'Assembled from what was loaded: `brief.md` + `sprint.md` + the git state and the tail, plus the unfinished plan if we are on a plan branch.'
    new: 'Assembled from what was loaded: `brief.md` + `sprint.md` + the git state and the tail, plus the unfinished plan if we are on a plan branch; in the session that opens a sprint, the first milestone comes from the case file of the opening Case of `/sprint-open` instead of `sprint.md` (case 769.2).'
  - old: The agent's first turn presents it as a list — tasks, problems, debt carried over, where the sprint stands.
    new: 'The agent''s first turn presents it as a list — tasks, problems, debt carried over, where the sprint stands —, but in the session that opens a sprint, whose first turn starts the opening Case of `/sprint-open`: there the Frontier is assembled and written before the reply that acknowledges that Case, and that reply presents it (case 769.2).'
  change: in the session that opens a sprint the Frontier takes the first milestone from the opening Case and the reply that acknowledges that Case presents it (case 769.2)
- slug: estimate-hi-writes-frontier
  set:
    status: pending
    method: 'by hand: the person''s answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open, on whether the Frontier came out as the Criterion says, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py'
  change: the Criterion replaced whole — at an opening the Frontier takes the first milestone from the opening Case, and the opening line stands closed
```

```tasks
- [x] update `rule-skill-hi`
- [x] update `rule-session-start`
- [x] update `estimate-hi-writes-frontier`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-writes-frontier`
```

### Case 769.3 — The readings of /hi come with the Frontier

> **given:**
> `estimate-hi-takes-its-readings`: its Criterion is replaced whole and its `purpose` set anew.
> **＋** `rule-skill-hi`: the skill `/hi`, rendered into `.claude/skills/hi/SKILL.md`, whose readings come with the Frontier.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `vault/wiki/brief.md`: the brief, whose Next session gives the `W` and `A` lines.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
> **＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
> **＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
- slug: estimate-hi-takes-its-readings
  set:
    status: pending
    purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, writes the answer as its reading line, and opens no page but the Estimates it reads
  change: the Criterion replaced whole — the readings come with the Frontier, which at an opening is not the first reply
```

```tasks
- [x] update `estimate-hi-takes-its-readings`
- [x] read `estimate-hi-takes-its-readings`
```

### Case 769.4 — The reply that acknowledges the opening Case brings the Frontier

> **given:**
> `rule-orchestration`: what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-acknowledges-the-opening-with-the-frontier`: the new check of the reply that acknowledges the opening Case.
> **＋** `estimate-orchestration-acknowledging-reply`: the four parts of an acknowledging reply, which stand.
> **＋** `rule-skill-sprint-open`: the skill of the opening, rendered into `.claude/skills/sprint-open/SKILL.md`.
> **＋** `rule-skill-hi`: the skill `/hi`, which sets the Frontier, its readings and its Ask questions.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.

> **when:**
> The person ratifies the opening Case of `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> Before that reply, the agent writes `raw/<date>/<hi HHMM>/frontier.md` as `rule-skill-hi` sets it, and takes each reading of an open `W` line whose whole method runs now.
> **＋** The reply keeps the four parts of an acknowledging reply, in their order.
> **＋** Its `LEDGER` block holds the decision lines of the opening Case, then the `estimate[...]` line of each reading taken.
> **＋** Its `## Frontier` shows the lines of the new `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** After the lines of the Frontier and before the question which item is next, the reply puts each open `A` line to the person as `rule-skill-hi` sets it: the Estimate by slug and its question.
> **－** No tool call follows the `LEDGER` block in the same reply.

```then
create:
- slug: estimate-orchestration-acknowledges-the-opening-with-the-frontier
  ref: rule-orchestration
  kind: QA
  purpose: Whether the Frontier is written and the readings of /hi taken before the reply that acknowledges the opening Case of a sprint, and whether that reply shows the Frontier, holds the readings in its LEDGER block and puts the Ask questions before the question which item is next
  method: by hand, at the Retro of the session of case 769, the new Render of rule-orchestration in its spec.md read against the Criterion
  tags:
  - session
  - workflow
  - sprint
update:
- slug: rule-orchestration
  replace:
  - old: The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`;
    new: The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`, or, in the session that opens a sprint, before the reply that acknowledges the opening Case of `/sprint-open` (case 769.4);
  - old: Headings and labels in the language of the chat (case 167, supersedes 157).
    new: 'Headings and labels in the language of the chat (case 167, supersedes 157). The reply that acknowledges the opening Case of `/sprint-open` brings the Frontier, as `rule-skill-hi` sets it: before that reply the agent writes `frontier.md` and takes each reading that `/hi` takes; its `LEDGER` block holds the reading lines after the decision lines; its `## Frontier` shows the new Frontier; and after the lines of the Frontier and before the question which item is next it puts each open `A` line to the person, as `/hi` does (case 769.4).'
  change: the Frontier and the readings of /hi come before the reply that acknowledges the opening Case of a sprint, which shows that Frontier and puts its Ask questions (case 769.4)
```

```tasks
- [x] update `rule-orchestration`
- [x] create `estimate-orchestration-acknowledges-the-opening-with-the-frontier`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] read `estimate-orchestration-acknowledges-the-opening-with-the-frontier`
```

### Case 769.5 — The opening line reaches the Frontier closed by the opening Case

> **given:**
> `estimate-sprint-close-next-session-opens-the-sprint`: its Criterion is replaced whole and its `method` set anew.
> **＋** `estimate-hi-writes-frontier`: sets where the opening line stands on the Frontier.
> **＋** `rule-skill-sprint-open`: the skill of the opening, `/sprint-open`, whose opening Case comes first.
> **＋** `entity-sprint-<id>`: the sprint page that the session closes.
> **＋** `entity-sprint-<new id>`: the sprint page that the next session creates.
> **＋** `/hi`: the skill that opens the next session.
> **＋** `vault/wiki/brief.md`: the brief, whose first line of `Cases` opens the next sprint.
> **＋** `vault/wiki/sprint.md`: the rendered sprint, which shows no live sprint after the close.
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `guppi ledger`, `guppi materialize`, `tests/test_ledger.py` and `tests/test_materialize.py`: the refusal of decision lines and the `sprint` field of the pages.

> **when:**
> The librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page, and the next session opens with `/hi`; someone reads `vault/wiki/brief.md`, that session's `vault/raw/<date>/<hi HHMM>/frontier.md`, the refusals of `uv run guppi ledger` in its transcript, its ledger, and the pages of its librarian's run.
> **＋** Or `tests/test_ledger.py` and `tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

> **then:**
> The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
> **＋** `/hi` starts `/sprint-open` and writes no `frontier.md` before the opening Case is ratified; then `frontier.md` holds that line first under `## Cases`, closed `[x] … · case N` by the opening Case, and no item of `vault/wiki/sprint.md`, as `estimate-hi-writes-frontier` sets it.
> **＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
> **＋** Each page that the librarian's run writes from the ledger of that session, which holds the `create` decision line of `entity-sprint-<new id>`, carries `sprint: <new id>`.
> **－** An `estimate` or `lesson` line is not refused for this reason.
> **－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

```then
update:
- slug: estimate-sprint-close-next-session-opens-the-sprint
  set:
    status: pending
    method: pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the Retro of the session of case 769, the new Renders of rule-skill-hi and rule-skill-sprint-open in its spec.md read against the Criterion
  change: the Criterion replaced whole — the opening line reaches frontier.md after the opening Case, closed by it; the method runs in the session of case 769
```

```tasks
- [x] update `estimate-sprint-close-next-session-opens-the-sprint`
- [x] read `estimate-sprint-close-next-session-opens-the-sprint`
```

## Case 770 — Cleanup files a page under the sprint of the session of its run

> **context:**
> At the librarian's run `guppi cleanup` moves each live page with `status: archived` to `vault/archive/<sprint>/<date>/<HHMM>/<category>/`, and takes `<sprint>` from the first `## <id>` heading of `vault/wiki/sprint.md` by `sprint_id` of `guppi/materialize.py`. The librarian runs cleanup at step 3 and `guppi sprint`, which rewrites `sprint.md`, only at step 5. So in the session that opens a sprint, `sprint.md` still names the closed sprint when cleanup runs. In session 1713, which opened `plugin`, cleanup moved `decision-case-757` and `decision-case-759` to `vault/archive/migration/2026-10-10/1713/decisions/`, while the `materialize.yaml` of 1713 holds `sprint: plugin`, which `guppi materialize` sets in a unit whose ledger creates `entity-sprint-<id>` (case 628.3). `guppi archive` had the same fault for the folders of `raw/` and takes the `sprint` field of the unit's own yaml since case 743.2, by `unit_sprint` of `guppi/archive.py`. The person chose the same source for cleanup, one shared function for the judgment, the move of the two pages in Work Mode, and a new Estimate. A Grep `` sprint_id|unit_sprint|\.sprint\b|"sprint" `` over `guppi/` printed `cli.py`, `cleanup.py`, `backlog.py`, `archive.py`, `generate.py`, `materialize.py`, `sprint_close.py`, `sprint.py` and `prespec.py`; the same judgment, the `sprint` field of a unit's yaml and else `sprint_id`, stands in `unit_sprint` of `archive.py` and inline in `generate_date` of `generate.py`, so the task moves it into one function of `materialize.py` that all three import, and adds no second copy. A Grep `` first `## <id>` heading|first heading of `?(vault/wiki/)?sprint\.md|sprint_id|heading of sprint\.md `` over `vault/wiki/`, `log.md` and `brief.md` left out, printed `rules/rule-sprint.md`, `rules/rule-skill-sprint-open.md`, `rules/rule-raw-archive.md`, `rules/rule-materialize.md`, `estimates/estimate-sprint-marks-a-closed-sprint.md` and `estimates/estimate-raw-archive-files-a-session-by-its-sprint.md`. The sentence of `rule-sprint` that the heading is the id that `cleanup` and `archive` read stays true, since both still read it when the yaml holds no sprint; the other hits speak of `sprint.md` itself, of `materialize` or of `archive`, whose behaviour does not change, and stand. The docstring of `guppi/cleanup.py` says the sprint is the first heading of `sprint.md`; the code task rewrites it. `rule-cleanup` keeps its mechanism in that docstring (case 632.1), and its `## Purpose` names no sprint, so the page needs no `update`; the new Estimate joins its `estimates` by its `ref`. The Criterion of `estimate-cleanup-moves` writes the folder as `<sprint>` and does not say where the name comes from, so it stays true and stands; `estimate-raw-archive-files-a-session-by-its-sprint` checks the move of `guppi archive`, whose behaviour the shared function keeps, and stands, its test run again in `tasks`. The Criterion of `estimate-generate-writes` says a created page's `sprint` is the `sprint` of the yaml, which `guppi materialize` takes from the first heading of `sprint.md` or from the `<id>` of `entity-sprint-<id>`; the shared function strips the field, as `unit_sprint` does and `generate_date` does not today, but `sprint_id` returns its id stripped and `opened_sprint` cuts it from a slug, which holds no space, so for each yaml `guppi materialize` writes the stripped field is the field itself, and that Criterion stays true and stands; `test_a_created_page_takes_the_sprint_of_its_yaml_over_the_heading` of `tests/test_generate.py`, run again in `tasks`, checks that generate still takes the yaml's sprint over the heading. A Grep `guppi cleanup` over `vault/wiki/rules/` and `.claude/` printed `.claude/agents/librarian-guppi.md` and `rules/rule-documentation.md`; both set the order of the steps of the librarian's run, which this Case keeps. Case 769 changes neither the librarian's run nor `guppi cleanup`. A Grep `` parents\[1\]|parent\.parent|ROOT\s*=|REPO\s*=|project_root\(\) `` over `tests/` printed `test_schemas.py`, `test_orchestration.py`, `test_lint.py`, `test_materialize.py`, `test_generate.py` and `test_case_schema.py`; they read live the schemas, the `Makefile`, `orchestration.md`, `case-schema.md` and `case-example.md`, none of which the sprint of a unit reaches, so no live test changes.

> **problem:**
> In the session that opens a sprint, `guppi cleanup` files archived pages under the closed sprint, since it reads `sprint.md` before `guppi sprint` rewrites it.

> **recommend:**
> - **Where does cleanup take the sprint name from?**
>   - Recommended: (a) the session's own record, as `guppi archive` does: the `sprint` field of the `materialize.yaml` of the session of the run, else `sprint.md`, in one function that `guppi archive`, `guppi cleanup` and `guppi generate` import.
>   - Answer: agreed, (a).
> - **What happens to the two pages already filed under `migration`?**
>   - Recommended: (a) move them in Work Mode to `vault/archive/plugin/2026-10-10/1713/decisions/`.
>   - Answer: agreed, (a).
> - **How is the fix checked?**
>   - Recommended: (a) a new check of its own, `estimate-cleanup-files-a-session-by-its-sprint`, by `uv run pytest tests/test_cleanup.py -k sprint`; `estimate-cleanup-moves` stays as it is.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the fix of a finding of `/pre-spec`: name `estimate-generate-writes`, whose Criterion says a created page takes the `sprint` of the yaml, and keep it true.
>   - Taken: `given` names it, and `context` says why its Criterion stays true under the shared function.

> **given:**
> `estimate-cleanup-files-a-session-by-its-sprint`: the new check of the sprint folder that cleanup picks.
> **＋** `rule-cleanup`: the rule of `guppi cleanup`, whose mechanism lives in the docstring of `guppi/cleanup.py`.
> **＋** `guppi/cleanup.py`: the move of archived pages.
> **＋** `guppi/materialize.py`: `sprint_id`, and the one function of the sprint of a unit.
> **＋** `guppi/archive.py` and `guppi/generate.py`: the other readers of the sprint of a unit.
> **＋** `estimate-generate-writes`: the check that a created page takes the `sprint` of its yaml, which stands.
> **＋** `tests/test_cleanup.py`, `tests/test_archive.py`, `tests/test_generate.py` and `tests/test_sprint_close.py`: the tests of cleanup and of the other readers.
> **＋** `vault/raw/<date>/<HHMM>/materialize.yaml`: the yaml of the session, with its `sprint` field.
> **＋** `vault/wiki/sprint.md`: the rendered sprint, whose first heading is the fallback.
> **＋** `vault/archive/` and its folder `vault/archive/<sprint>/`: where cleanup files an archived page.

> **when:**
> `uv run guppi cleanup` of `guppi/cleanup.py` moves a live page with `status: archived` under `vault/archive/`, or `tests/test_cleanup.py` runs that move over a made-up vault.

> **then:**
> The page goes under `vault/archive/<sprint>/`, `<sprint>` being the value of the `sprint` field of the `vault/raw/<date>/<HHMM>/materialize.yaml` of the session of the run.
> **＋** A run whose session has no `materialize.yaml`, or whose yaml holds no `sprint` field, or a run with no session folder, takes the first `## <id>` heading of `vault/wiki/sprint.md`, as before.
> **－** The date and session folders under the sprint folder, the History and `log.md` lines and the rest of the move do not change.

```then
create:
- slug: estimate-cleanup-files-a-session-by-its-sprint
  ref: rule-cleanup
  kind: QA
  purpose: Whether guppi cleanup moves an archived page under the sprint that the materialize.yaml of the session of its run records, and under the sprint of sprint.md only when that yaml or its field is missing
  method: uv run pytest tests/test_cleanup.py -k sprint
  tags:
  - harness
  - librarian
  - sprint
```

```tasks
- [x] create `estimate-cleanup-files-a-session-by-its-sprint`
- [x] `guppi/materialize.py`: one function gives the sprint of a unit, the `sprint` field of its yaml stripped, else `sprint_id`; `unit_sprint` of `guppi/archive.py` and the inline judgment in `generate_date` of `guppi/generate.py` are replaced by imports of it.
- [x] `guppi/cleanup.py`: `run` takes the sprint of the unit `<date>/<HHMM>` that `session_of_run` names, by that function, and `sprint_id` when no session folder exists; the docstring says so.
- [x] `tests/test_cleanup.py`: a test whose session yaml holds `sprint: a` while `sprint.md` names `b`, and the page lands under `vault/archive/a/`; a test whose session has no yaml, and the page lands under `b`; both names hold `sprint`.
- [x] `uv run pytest tests/test_cleanup.py tests/test_archive.py tests/test_generate.py tests/test_sprint_close.py`
- [x] one-off migration: `git mv` `vault/archive/migration/2026-10-10/1713/decisions/decision-case-757.md` and `decision-case-759.md` to `vault/archive/plugin/2026-10-10/1713/decisions/`, and remove the folders left empty.
- [x] read `estimate-cleanup-files-a-session-by-its-sprint`
```

## Case 772 — The checks that wait for a moment of the sprint stay off Work and the Frontier

> **context:**
> This Case replaces Case 764 of this session, ratified and then reported by pre-spec; it keeps its shape and its answers and fixes four findings the person agreed to. The brief lists every `pending` check (Estimate) under `Work` of its Next session, and `/hi` copies each one onto the Frontier as a `W` line; a `W` line that cannot be read now becomes a Cases line that asks to fix, replace or archive the check. So the five checks of `entity-sprint-plugin`, the Definition of done of the sprint, stood as W2 to W6 of this session, and four of them again as C7 to C10, though the work they check is not done; W1, `estimate-sprint-close-next-session-opens-the-sprint`, waits for the session after the close of a sprint. Three texts also hold no exception for a check of a sprint page. `case-schema.md` lets a `method` hold only what runs in the Case's own session (case 670.4). `/retro` sets each Estimate its session creates or updates and cannot read `failed` with `Retro, not read`, while the Retro of session 1713 left the five checks `pending`, as the context of Case 756 said. `waits_for_another_session` of `guppi/lint.py` does not match "a session of the sprint plugin before its close" or "the session that closes", as `lesson-prespec-method-predicate-misses-a-sprint-session` records. The person chose this: a check of the live sprint page stands in no list of Next session while its work is not done, and is read at the Retro of the session that finishes its work or by the closing Case of `/sprint-close`; a check whose `method` names the close of a sprint stands in no list until the brief of the run that closes the sprint, Ask lines included; Retro leaves a sprint check whose work is not done `pending`, and the handoff names it; only a check whose target is a sprint page may wait for a later session of its sprint; and pre-spec catches the new words and spares such a check. Pre-spec then found four gaps in Case 764, and the person took the recommended fix of each. First, `/retro` charges as debt a `read` box with no reading in the Tail, and the brief takes every unticked box of the Specs into `Work`, so the open `read` box of a waiting sprint check, such as the one of Case 767, would come back as debt and as a `Work` line; Cases 772.1 and 772.2 cover that box. Second, a sprint check whose `method` names the person's answer, such as the README check of Case 765, is read at the `/hi` after the session whose Work Mode finished its work: the Retro of that session names it under `## Ask the person` of the handoff, as `/retro` already does for a reading that needs the person's word, and the brief carries it into `Ask the person`; so Case 772.1 keeps a sprint check out of `Ask the person` only while its work is not done. Third, the judgment that a slug is a sprint page stood in several modules: a Grep `"entity-sprint-"` over `guppi/` printed `guppi/ledger.py`, `guppi/materialize.py`, `guppi/prespec.py`, `guppi/sprint.py` and `guppi/sprint_close.py`, each with a constant of its own. `guppi/materialize.py`, `guppi/prespec.py`, `guppi/sprint.py` and `guppi/sprint_close.py` import from `guppi/ledger.py`, directly or through `guppi/materialize.py`, and `guppi/ledger.py` imports none of them, so Case 772.4 puts the constant and one predicate in `guppi/ledger.py` and the other four modules import them. Fourth, the new tests carry `waits` or `kept_method` in their names, so that the methods of the two pre-spec Estimates run them. `vault/wiki/sprint.md` keeps showing the checks of the sprint page under `Done when`, and Readings due of the brief keeps every `pending` check, so none is lost while it waits. Case 772.1 changes the brief, Case 772.2 Retro, Case 772.3 the handoff, Case 772.4 the rule of case 670.4 and the pre-spec check of a written method, and Case 772.5 the pre-spec check of a method kept on the page; each replaces the Criterion of the one Estimate whose Criterion speaks of its change, and sets anew a `purpose` or `method` that states the old promise. Not done, by the person's choice: the method of W1 names a transcript of an earlier session, which `/hi` may not read (case 670.5), and it waits for a Case before the close of `plugin`; and `make lint` keeps its `unread: pending` line for each waiting check. `rule-skill-hi` and `estimate-hi-takes-its-readings` are changed by Case 769 of this session, which sets what `/hi` does; this Case sets only what the brief, Retro, the handoff and pre-spec do, and covers no moment of `/hi`. `rule-sprint` and `entity-sprint` say that the Estimates of a sprint page are read before its close, which stays true. Step 3 of `/sprint-close` sorts every `pending` or `failed` Estimate by the kind of its moment, so a check that waits for the session that closes a sprint needs no list of Next session. A Grep `` Retro, not read|set it `failed`|pending` reading|reading cannot be taken yet `` over `vault/wiki/rules/` and `.claude/` printed `vault/wiki/rules/rule-brief.md`, `vault/wiki/rules/rule-handoff.md`, `vault/wiki/rules/rule-retro.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/handoff/SKILL.md` and `.claude/skills/retro/SKILL.md`: the three rules this Case changes and their renders. A Grep `670\.4` over `vault/wiki/rules/` printed `vault/wiki/rules/rule-case-protocol.md`, whose two sentences Case 772.4 changes, and `vault/wiki/rules/rule-prespec-hook.md`, where it stands in a History line alone. A Grep `ANOTHER_SESSION|closes a sprint|session of the sprint|session that closes` over `guppi/` printed `guppi/lint.py` and `guppi/prespec.py`: the one judgment of the words of a waiting method is `ANOTHER_SESSION` of `guppi/lint.py`, which Case 772.4 widens, and the hit in `guppi/prespec.py` is a finding on a Frontier line, no such judgment. A Grep `parents\[1\]|parent\.parent` over `tests/` printed `tests/test_generate.py`, `tests/test_case_schema.py`, `tests/test_orchestration.py`, `tests/test_schemas.py`, `tests/test_lint.py` and `tests/test_materialize.py`; they read the `schema.yaml` files, `orchestration.md` and the `Makefile`, and `case-schema.md` only while `case-example.md` does not stand, so no test reads live a file this Case changes. A Grep `session\s+(of\s+(the\s+)?sprint|that\s+closes)` over `tests/` printed nothing, so no test holds a method that the wider predicate judges anew. Of the other Cases of this batch, Cases 766, 767 and 768 point to this rule and change no page this Case changes; Case 767 replaces the Criterion of a sprint-page check and keeps its method, which Case 772.5 spares; Case 765 sets the README check to the person's answer, which Case 772.1 lets into `Ask the person` once its work is done.

> **problem:**
> Checks that cannot be read before a later moment of the sprint stand under `Work` and on the Frontier in every session, and turn into decision items though nothing is wrong with them. The rule that a check is read in its own session, Retro and pre-spec hold no exception for the checks of a sprint page.

> **recommend:**
> - **When do the sprint page's own checks come back to be read?**
>   - Recommended: (a) no new trigger: the Retro of the session that finishes the work, or the closing Case of `/sprint-close`.
>   - Answer: agreed, (a).
> - **Do Ask lines that wait for a sprint close leave the Frontier too?**
>   - Recommended: (a) yes, the same rule: such a line is left out until the brief written at a sprint close.
>   - Answer: agreed, (a).
> - **What does Retro do with a sprint-page check it cannot read?**
>   - Recommended: (a) it stays pending, and the handoff names it as a check that waits for its work.
>   - Answer: agreed, (a).
> - **Which checks may name a later session of the sprint?**
>   - Recommended: (a) only checks whose target is a sprint page.
>   - Answer: agreed, (a).
> - **How does pre-spec judge the new wording?**
>   - Recommended: (a) the predicate catches a session of a sprint and the session that closes one, and pre-spec spares a check of a sprint page.
>   - Answer: agreed, (a).
> - **What happens to W1, whose reading needs an old transcript?**
>   - Recommended: (a) leave it out of this Case; a later Case fixes its method before the close of `plugin`.
>   - Answer: agreed, (a).
> - **Do the red lines of `make lint` stay for these checks?**
>   - Recommended: (a) they stay.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: pre-spec found that the open `read` box of a waiting sprint check would be debt at Retro and a `Work` line of the brief; the person agreed to the recommended fix.
>   - Taken: Retro leaves that box waiting, neither debt nor the librarian's, and the brief takes no `Work` line from it.
> - **Change**
>   - Asked: pre-spec asked how a sprint check whose method names the person's answer is read; the person chose that the Retro of the session that finished its work names it under `## Ask the person` of the handoff, and the brief carries it into `Ask the person`.
>   - Taken: the brief keeps a sprint check out of `Ask the person` only while its work is not done, and Retro names it there once its work is done.
> - **Change**
>   - Asked: pre-spec found that the judgment that a slug is a sprint page stands in more than one module; the person agreed to put it in one module that the others import.
>   - Taken: `guppi/ledger.py` holds the constant and one predicate, and `guppi/materialize.py`, `guppi/prespec.py`, `guppi/sprint.py` and `guppi/sprint_close.py` import them.
> - **Change**
>   - Asked: pre-spec found that the test tasks did not require the names that the methods of the two pre-spec Estimates select; the person agreed to name them.
>   - Taken: the new tests carry `waits` or `kept_method` in their names.

### Case 772.1 — The brief keeps the waiting checks out of Next session

> **given:**
> `rule-brief`: the rule of the brief, rendered into `.claude/agents/librarian-guppi.md`.
> **＋** `estimate-brief-written`: its Criterion is replaced whole and its method set anew.
> **＋** `vault/wiki/brief.md`: the brief the librarian writes.
> **＋** `entity-sprint-<id>`: the live sprint page, whose checks wait.
> **＋** `vault/wiki/sprint.md`: the rendered sprint, which shows the checks of the sprint page.
> **＋** `vault/wiki/backlog.md`: where the deferred items stand.
> **＋** `vault/archive/`: where the pages of a closed sprint stand.
> **＋** `/hi`: the skill that takes the lists of Next session onto the Frontier.
> **＋** `rule-carry-over`: the second writer of the brief.

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items; they stand in `vault/wiki/backlog.md`. Where things stand, Readings due and Readings at the close are as before, and Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
> **＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, an item in one list only, a list with no item the line "none". `Cases` is what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>`; a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, each contradiction of Flags, one between pages that stand in `vault/archive/` too, a defect the librarian found; with what and from where.
> **＋** `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page `entity-sprint-<id>`, and one whose `method` names the close of a sprint — the session that closes a sprint, its librarian's run or the session after it; the unticked boxes of the Specs but the `read` box of such a reading; a ledger line this run did not apply, a dirty tree.
> **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them — but one whose `method` names the close of a sprint. A check of the live sprint page whose `method` names the person's answer stands there once the Retro of the session that finished its work named it in `handoff.md`.
> **＋** In the run whose `guppi sprint-close --apply` moved the sprint page, each `pending` reading whose `method` names the session after that close, or its `/hi`, stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer.
> **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
> **－** A reading left out of `Work` and `Ask the person` keeps its line under Readings due.
> **－** A contradiction of Flags that a line of `## For the next session` of `handoff.md` already carries gets no second line in `Cases`.
> **－** The brief states no decision: the sort by kind is not a judgment of the work.

```then
update:
- slug: rule-brief
  replace:
  - old: '`Work`, what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs'
    new: '`Work`, what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page and one whose `method` names the close of a sprint, the unticked boxes of the Specs but the `read` box of such a reading'
  - old: '`Ask the person`, a reading only the person can take: each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.'
    new: '`Ask the person`, a reading only the person can take: each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them — but one whose `method` names the close of a sprint. A `method` names the close of a sprint when it names the session that closes a sprint, its librarian''s run or the session after it. A reading of an Estimate whose `target` is the live sprint page `entity-sprint-<id>`, or whose `method` names the close of a sprint, stands in Readings due and in no list of Next session, its `read` box in the Specs included, until its moment: the first is read at the Retro of the session that finishes its work or by the closing Case of `/sprint-close`, and, when its `method` names the person''s answer, stands in `Ask the person` once that Retro named it under `## Ask the person` of `handoff.md`; the second at its moment. In the run whose `guppi sprint-close --apply` moved the sprint page, each `pending` reading whose `method` names the session after that close, or its `/hi`, stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person''s answer (case 772.1).'
  change: Work and Ask the person of Next session leave out a reading of the live sprint page whose work is not done, its read box included, and one whose method names the close of a sprint, until its moment (case 772.1)
- slug: estimate-brief-written
  set:
    status: pending
    method: 'by hand, the person''s answer at the /hi after the librarian''s run of the session that closes a sprint, on vault/wiki/brief.md of that run and the brief of the run before it: whether Cases hold each contradiction of Flags, one between archived pages too, and once where a line of For the next session carries it, and whether Work and Ask the person leave out a reading of the live sprint page whose work is not done and one whose method names the close of a sprint but in the brief of the closing run, recorded in the estimate line'
  change: the Criterion replaced whole — Work and Ask the person leave out a reading that waits for a moment of the sprint, its read box included; the method reads it too
```

```tasks
- [x] update `rule-brief`
- [x] update `estimate-brief-written`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-brief-written`
```

### Case 772.2 — Retro leaves a sprint check whose work is not done pending

> **given:**
> `rule-retro`: the rule of Retro, rendered into `.claude/skills/retro/SKILL.md`.
> **＋** `estimate-retro-loads`: its Criterion is replaced whole.
> **＋** `entity-sprint-<id>`: the live sprint page, whose checks wait.
> **＋** `/work`: the skill that calls Retro.
> **＋** `/sprint-close`: the skill whose closing Case reads the checks still pending.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose Criteria and boxes Retro reads.
> **＋** `raw/<date>/<hi HHMM>/work.md`: the file of Work Mode that may name a conserved Spec.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose `W` lines Retro closes.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the report of Retro.

> **when:**
> The agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built.
> **＋** Each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — is read in the reply that ends Retro, on the Criterion of `raw/<date>/<hi HHMM>/spec.md`: the `when` and `then` of its Case, or the Criterion its item writes.
> **＋** For an Estimate of a rule whose Render a Case of the Spec changes, the reading reads the new text of the Render in `raw/<date>/<hi HHMM>/spec.md` against that Criterion.
> **＋** Each such Estimate that Retro cannot read gets a `failed` line in the same `LEDGER` block, whose result opens with the date and says that Retro did not read it and why.
> **＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec is the `spec.md` of the folder that section names, and the decision lines of that folder's `ledger.md` count as this session's for its boxes, for the scope of an edit and for the readings above.
> **＋** Retro closes the open `W` line of each Estimate it reads or sets `failed` `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`.
> **－** An Estimate whose `target` is the live sprint page `entity-sprint-<id>` and whose work is not done yet is neither read, nor put to the person, nor set `failed`: it stays `pending` for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, and its `read` box in `raw/<date>/<hi HHMM>/spec.md` waits for that moment, neither debt nor the librarian's.
> **－** Once its work is done, the Retro of that session reads it, or, when its `method` names the person's answer, names it under `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** An Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`.
> **－** A reading whose `method` names the person's word is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question, and its `read` line is neither debt nor the librarian's.
> **－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

```then
update:
- slug: rule-retro
  replace:
  - old: 'A reading whose `method` names the person''s word is not yours to take:'
    new: 'An Estimate whose `target` is the live sprint page, `entity-sprint-<id>`, and whose work is not done yet is neither read, nor put to the person, nor set `failed`: it stays `pending` for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, its `read` line waits for that moment and is neither debt nor the librarian''s, and `handoff.md` names it with that moment; once its work is done, the Retro of that session reads it, or, when its `method` names the person''s answer, names it under `## Ask the person` as below (case 772.2). A reading whose `method` names the person''s word is not yours to take:'
  change: Retro leaves an Estimate of the live sprint page whose work is not done pending, its read line neither debt nor the librarian's, and names it under Ask the person once its work is done when the person's answer reads it (case 772.2)
- slug: estimate-retro-loads
  set:
    status: pending
  change: the Criterion replaced whole — an Estimate of the live sprint page whose work is not done stays pending, its read line no debt
```

```tasks
- [x] update `rule-retro`
- [x] update `estimate-retro-loads`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [x] read `estimate-retro-loads`
```

### Case 772.3 — The handoff names a sprint check that waits for its work

> **given:**
> `rule-handoff`: the rule of the handoff, rendered into `.claude/skills/handoff/SKILL.md`.
> **＋** `estimate-handoff-holds-each-fact-once`: its Criterion is replaced whole.
> **＋** `rule-retro`: the Retro whose report the handoff is.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff the agent writes.
> **＋** `entity-sprint-<id>`: the live sprint page, whose checks wait.
> **＋** `rule-brief`: the rule of the brief, which reads the handoff.

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent runs `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff` and writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats. `## Direct instructions to the librarian` holds only what to check first and what may duplicate what, and lists no reading that waits.
> **＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
> **＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
> **＋** An Estimate this session creates or updates has no such line in `## Debt`: the Retro of `rule-retro` read it or set it `failed`, unless the person's answer is its reading. An Estimate of the live sprint page `entity-sprint-<id>` whose work is not done, which that Retro left `pending`, has its line, its moment the Retro of the session that finishes its work or the close of the sprint.
> **＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
> **＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
> **－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
> **－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

```then
update:
- slug: rule-handoff
  replace:
  - old: an Estimate this session creates or updates has no such line, since Retro read it or set it `failed`;
    new: 'an Estimate this session creates or updates has no such line, since Retro read it or set it `failed`, but for an Estimate of the live sprint page whose work is not done, which Retro left `pending`: its line names the Retro of the session that finishes its work or the close of the sprint (case 772.3);'
  change: Debt names an Estimate of the live sprint page that Retro left pending, with its moment (case 772.3)
- slug: estimate-handoff-holds-each-fact-once
  set:
    status: pending
  change: the Criterion replaced whole — Debt names an Estimate of the live sprint page that Retro left pending
```

```tasks
- [x] update `rule-handoff`
- [x] update `estimate-handoff-holds-each-fact-once`
- [x] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
- [x] read `estimate-handoff-holds-each-fact-once`
```

### Case 772.4 — A check of a sprint page may wait for a later session of its sprint

> **given:**
> `rule-case-protocol`: the form of a Case, rendered into `vault/wiki/case-schema.md`, whose rule of case 670.4 gains the exception.
> **＋** `guppi/lint.py`: `ANOTHER_SESSION` and `waits_for_another_session`, the one predicate of a waiting method.
> **＋** `guppi/prespec.py`: the check of the form of an Estimate item, `updates_the_sprint` and the module docstring.
> **＋** `guppi/ledger.py`: the module that holds the one judgment that a slug is a sprint page.
> **＋** `guppi/materialize.py`, `guppi/sprint.py` and `guppi/sprint_close.py`: the modules that import that judgment in place of their own constant.
> **＋** `tests/test_lint.py` and `tests/test_prespec.py`: the tests of the predicate and of the finding.
> **＋** `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`: its Criterion and its `purpose` are set anew.
> **＋** `entity-sprint-<id>`: a sprint page, the target that the exception names.
> **＋** `/hi`: a moment a method may name, which the predicate catches.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

> **then:**
> A `method` with a part between two `;` that names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi` gives one line `case N: <create|update> <slug>: method waits for another session — a method holds only what runs in its own session`.
> **＋** The judgment is one predicate in `guppi/lint.py`, which `guppi/prespec.py` imports.
> **＋** Whether the target is a sprint page is judged by one predicate in `guppi/ledger.py`, which `guppi/prespec.py`, `guppi/materialize.py`, `guppi/sprint.py` and `guppi/sprint_close.py` import.
> **－** A part that names the person, such as the person's answer at `/hi`, gives no such line.
> **－** An Estimate whose target is a sprint page `entity-sprint-<id>` — the `ref` of a `create`, or the `target` that an `update` sets or that the live page holds — gives no such line.
> **－** `uv run guppi lint` of `guppi/lint.py` over the live Estimate pages gives no finding by this predicate.
> **－** The line does not replace the finding of a `method` that names no form or that ties its reading to a one-off moment.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: a problem seen live in a later session is a lesson, and pre-spec reports a `method` that waits for a later session, the librarian or a `/hi` (case 670.4).
    new: 'a problem seen live in a later session is a lesson, and pre-spec reports a `method` that waits for a later session, a session of a sprint, the session that closes one, the librarian or a `/hi` (case 670.4). An Estimate whose target is a sprint page, `entity-sprint-<id>`, is the exception: the sprint page is the Definition of done of its sprint, read before its close, so its `method` may wait for a later session of that sprint, up to the session that closes it (case 772.4).'
  - old: which the Retro of the Case's own session takes on the Criterion of the Spec (case 670.4),
    new: which the Retro of the Case's own session takes on the Criterion of the Spec (case 670.4), or, for an Estimate of the live sprint page whose work is not done, the Retro of the session that finishes its work or the closing Case of `/sprint-close` (case 772.4),
  change: an Estimate of a sprint page may wait for a later session of its sprint, and pre-spec catches a session of a sprint and the session that closes one (case 772.4)
- slug: estimate-prespec-hook-reports-a-method-that-waits-for-another-session
  set:
    status: pending
    purpose: Whether pre-spec reports a method in the plan that waits for a later session, a session of a sprint, the session that closes one, the librarian or a /hi, by one predicate of guppi/lint.py, and leaves alone a method that names the person, the method of an Estimate of a sprint page, and the live pages
  change: the Criterion replaced whole — the predicate catches a session of a sprint and the session that closes one, and an Estimate of a sprint page gives no finding
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`
- [x] `guppi/lint.py`: `ANOTHER_SESSION` also matches a session of a sprint and the session that closes, such as "a session of the sprint plugin before its close" and "the session that closes entity-sprint-plugin"; the docstring of `waits_for_another_session` names them.
- [x] `guppi/ledger.py`: the constant of the prefix `entity-sprint-` and one predicate that tells whether a slug, or a wikilink to it, names a sprint page, with its docstring.
- [x] `guppi/materialize.py`, `guppi/prespec.py`, `guppi/sprint.py` and `guppi/sprint_close.py`: each drops its own constant `entity-sprint-` and imports the constant and the predicate of `guppi/ledger.py`; `opened_sprint`, `updates_the_sprint` and `sprint_pages_live` judge a sprint page by that predicate.
- [x] `guppi/prespec.py`: the check of the form gives no `WAITS` line on a `create` whose `ref`, or an `update` whose target by `estimate_target`, is a sprint page, by the predicate of `guppi/ledger.py`; the module docstring names the new words and the exception.
- [x] `tests/test_lint.py`: `test_waits_the_one_predicate_names_another_session` holds a method that names a session of a sprint and one that names the session that closes it among the methods that wait.
- [x] `tests/test_prespec.py`: a test whose name opens with `test_waits_` shows that a `create` and an `update` of an Estimate of a sprint page whose method names a session of the sprint before its close give no line, and that the same method on an Estimate of a rule gives the line.
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`
```

### Case 772.5 — Pre-spec spares a kept method of a sprint check

> **given:**
> `guppi/prespec.py`: `kept_method_waits`, the check of a method kept on the page.
> **＋** `guppi/lint.py`: `waits_for_another_session`, the one predicate of a waiting method.
> **＋** `guppi/ledger.py`: the one predicate that a slug is a sprint page.
> **＋** `tests/test_prespec.py`: the tests of the finding.
> **＋** `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`: its Criterion and its `purpose` are set anew.
> **＋** `entity-sprint-<id>`: a sprint page, the target that the exception names.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads an `update` of an Estimate in the `then` blocks of the plan file that replaces its Criterion whole and carries no `set: {method: …}`, and the `method` of that Estimate's live page.

> **then:**
> When a part of that `method` between two `;` names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or /hi, and does not name the person, the check gives one line `case N: update <slug>: the method on the page waits for another session — set a method that runs in this session`.
> **＋** The judgment is `waits_for_another_session` of `guppi/lint.py`, the same predicate that judges a `method` the plan writes.
> **－** An Estimate whose live page holds a sprint page `entity-sprint-<id>` as its `target`, by the predicate of `guppi/ledger.py`, gives no such line.
> **－** An `update` that sets the Estimate `passed` or `failed` by the person's decision gives no such line.
> **－** An `update` that names a part of the page alone, such as a `set` of another field or a `replace` pair, gives no such line.
> **－** A `method` on the page that waits for no other session, or whose part names the person, gives no such line.

```then
update:
- slug: estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session
  set:
    status: pending
    purpose: Whether pre-spec reports a Case that replaces the Criterion of an Estimate whole, writes no method and keeps one on the page that waits for another session, by the one predicate of guppi/lint.py, but for an Estimate of a sprint page
  change: the Criterion replaced whole — a kept method of an Estimate of a sprint page gives no finding, and the predicate names a session of a sprint and the session that closes one
```

```tasks
- [x] update `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`
- [x] `guppi/prespec.py`: `kept_method_waits` returns false when the `target` of the live page is a sprint page, by the predicate of `guppi/ledger.py`; its docstring says so.
- [x] `tests/test_prespec.py`: a test whose name opens with `test_kept_method_` shows that an `update` that replaces the Criterion of an Estimate of a sprint page whole and keeps a method that names a session of the sprint gives no line, and that the same kept method on an Estimate of a rule gives the line.
- [x] read `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`
```

## Deferred

## Case 771 — The merge step at the opening of a sprint put off

> **context:**
> The person moved on to Work Mode with C4 of the Frontier open. The item comes from the brief of session 1713: after a sprint with a branch of its own, the branch is merged into the main branch at the opening of the next sprint, and the brief gave the merge line under `Cases` while step 4 of `/sprint-close` says `Work`. No Case of this session sets where the merge step stands.

> **problem:**
> No Case of this session decides where the merge of the closed sprint's branch stands at the opening of the next sprint, nor which list of the brief carries its line.

```then
defer:
  - slug: rule-skill-sprint-open
    type: rule
    purpose: "Where the merge of a closed sprint's own branch into the main branch stands at the opening of the next sprint; put off at the close of Plan Mode"
  - slug: rule-skill-sprint-close
    type: rule
    purpose: "Which list of the brief carries the merge line that step 4 of /sprint-close sets; put off at the close of Plan Mode"
```
