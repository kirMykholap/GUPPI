<!-- approved 18:38:54 · session 5d2b5538 -->

# Session 1713 — opens the next sprint

## Case 756 — The sprint plugin opens

> **context:**
> A sprint is one page, `entity-sprint-<id>`, a Leaf under `entity-sprint`. Its `estimates` are its Definition of done and its `## Milestones` are the work in order. `guppi sprint` renders `vault/wiki/sprint.md` from it. Since the close of `migration` no live sprint page stands, and `vault/wiki/sprint.md` reads that no sprint is open. The ledger hook refuses each decision line but a `defer` until a `create` of an `entity-sprint-` page stands, so this opening Case, run under `/sprint-open` (`rule-skill-sprint-open`), is the first Case the session ratifies. The person set the id `plugin` and a goal of five lines of work: the opening and the close of a sprint fixed, a final README, the repository on GitHub ready for pull requests from others, CI that writes a clean version of the project to a branch of its own, and that clean version made into a Claude Code plugin. Each line becomes one condition of the Definition of done, one Estimate each, in Case 756.2 to Case 756.6; Case 756.1 creates the page. `vault/wiki/backlog.md` holds 3 items, and the person took none of them. A Glob `vault/**/*plugin*` printed only `vault/.obsidian/core-plugins.json`, so the new slugs are free. Case 756.1 adds no Estimate: `estimate-sprint-renders-the-backlog` already checks the render of a live sprint page, and the pending `estimate-sprint-close-next-session-opens-the-sprint` checks that the pages written from this session's ledger carry the new sprint id; their Criteria speak of any sprint page and stand. `estimate-skill-sprint-open-asks-the-opening-questions` checks the questions of the opening, which this Case asked, and stands. `case-schema.md` says that a `method` holds only what runs in the Case's own session. The methods of Case 756.2 to Case 756.6 are read in a later session of the sprint, before its close, since `rule-sprint` and `entity-sprint` set that the Estimates of a sprint page are read before its close. Neither page states an exception to case 670.4; the exception for a sprint page stands on their words that its Estimates are read before its close, and on the precedent of `entity-sprint-migration`, whose Estimate `estimate-sprint-migration-merges` was read in Work Mode of session 1555, the session that closed it. The read lines of these Estimates stay open at the Retro of this session and are carried until their moment. The sprint-turn condition is read at the end of Work Mode of the closing session, since the move to the archive runs later, in the librarian's run (Q7). No separate reading of that run comes at the close of `plugin`: `estimate-sprint-close-runs-in-the-librarian-run` was read `passed` at the `/hi` of this session over the close of `migration`, line 1 of this session's ledger, and the move of the sprint page and its Estimates is held by the tests of `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`. Case 756.2 signs only what is new, no step done or fixed by hand; the steps of the skill stand in the Criteria of `estimate-skill-sprint-close-leads-the-closing-session` and `estimate-sprint-close-takes-the-readings-in-groups`, which are not signed again. `README.md` exists at the root of the repository with the heading `# Vault harness`; a Grep for `README` over `vault/wiki/`, `log.md` left out, printed nothing, so no page governs it yet. The person added that the form of the sprint opening may be discussed later, and asked no change for it now.

> **problem:**
> No sprint is open, and the session can ratify no other Case until a sprint page stands. The next sprint needs its id, its goal, its Definition of done, its milestones and an answer on the backlog.

> **recommend:**
> - **What is the goal of the sprint?**
>   - Recommended: (a) your own goal; failing one, (b) settle what `migration` left.
>   - Answer: (a), the sprint's own goals: make sure the opening and the close of a sprint work correctly and fix every flaw; write the final README on the main parts of the project, why it is needed and how to use it; connect GitHub and set it up so that pull requests from other people are easy to review; set up CI/CD so that a branch of its own holds a clean version of the project, with no case references in its texts and a clean Frontier, sprint and the like; that clean version becomes the Claude plugin. The rest comes as the work goes.
> - **Do you take any backlog item into the sprint?**
>   - Recommended: (a) take none now.
>   - Answer: (a), nothing now; to be thought about later.
> - **What is the id of the sprint?**
>   - Recommended: (a) `plugin`.
>   - Answer: agreed, (a).
> - **How is the goal written in one sentence?**
>   - Recommended: (a) the whole list in one sentence.
>   - Answer: agreed, (a).
> - **Which conditions make the Definition of done?**
>   - Recommended: (a) five conditions, one per line of the list.
>   - Answer: agreed, (a).
> - **How are the milestones cut?**
>   - Recommended: (b) three milestones in the order of the work.
>   - Answer: agreed, (b).
> - **When is the condition on the sprint turn read?**
>   - Recommended: (a) read the steps up to Work Mode; the archive run stays with the check of the close rule.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: pre-spec found that the methods of Case 756.2 to Case 756.6 wait for a later session against case 670.4; the person agreed to name in `context` where the exception for a sprint page stands and its precedent.
>   - Taken: `context` names `rule-sprint`, `entity-sprint` and the reading of `estimate-sprint-migration-merges` in session 1555.
> - **Change**
>   - Asked: pre-spec found that the `then` of Case 756.2 signs again the steps that `estimate-skill-sprint-close-leads-the-closing-session` and `estimate-sprint-close-takes-the-readings-in-groups` hold; the person agreed to keep only what is new.
>   - Taken: the `then` of Case 756.2 holds only that no step is done or fixed by hand, and names the two Estimates for the rest.
> - **Change**
>   - Asked: pre-spec found that the alias of the new tag `ci` would also point at the tag `case-build`; the person agreed to another alias.
>   - Taken: the aliases of `ci` are CI, CI/CD and continuous integration in Russian.
> - **Change**
>   - Asked: pre-spec found that `context` and Case 756.2 say a reading of `estimate-sprint-close-runs-in-the-librarian-run` comes at the close of `plugin`, and none is due; the person chose (a), keep that Estimate as it stands and correct the text.
>   - Taken: `context` and the `－` line of Case 756.2 say that the run was read `passed` at the close of `migration` and that `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` holds the move of the pages.

### Case 756.1 — The sprint page plugin

> **given:**
> `entity-sprint-plugin`: the new page of the sprint.
> **＋** `entity-sprint`: the sprint as a kind, the parent of the page.
> **＋** `guppi/sprint.py`: the script that renders the sprint page.
> **＋** `vault/wiki/sprint.md`: the file the script writes.
> **＋** `vault/wiki/backlog.md`: the items put off.
> **＋** `rule-sprint`: the guard of the sprint page and its render.

> **when:**
> `uv run guppi sprint` of `guppi/sprint.py` runs in the librarian's run of this session with the live page `entity-sprint-plugin`.

> **then:**
> `vault/wiki/sprint.md` names the sprint `plugin`, with its Purpose and its Done when.
> **＋** The milestone `The sprint turn and GitHub` stands whole as the current one.
> **＋** The milestones `The clean branch` and `The plugin` stand one line each, and the close line is the last item of `The plugin`.
> **＋** Each page written from the ledger of this session carries `sprint: plugin`.
> **－** No item of `vault/wiki/backlog.md` enters `entity-sprint-plugin`.

```then
create:
- slug: entity-sprint-plugin
  type: entity
  kind: Leaf
  ref: entity-sprint
  purpose: 'GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the opening and close of a sprint work with no fix by hand'
  tags:
  - sprint
  - workflow
  sections:
    Purpose: 'GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the opening and close of a sprint work with no fix by hand. Done when every Estimate of this page passes: the close steps run from the close line, the README describes the project, a pull request from another account is checked and reviewed on GitHub, CI writes the clean branch, and the clean branch installs as a plugin. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (rule-sprint-close).'
    Milestones: |-
      ### The sprint turn and GitHub

      - the opening and the close of a sprint run with no fix by hand and each flaw found in them is fixed
      - the repository on GitHub set up so that a pull request from another person is easy to review

      ### The clean branch

      - CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint

      ### The plugin

      - the clean version made into a Claude Code plugin
      - the README on what the project is and what it is for and on its main parts and its use
      - the close of `plugin` — `/sprint-close`, a session of its own
```

```tasks
- [x] create `entity-sprint-plugin`
- [x] `uv run guppi sprint`
```

### Case 756.2 — The close steps run from the close line

> **given:**
> `estimate-sprint-plugin-close-steps-run-from-the-line`: the new check of the steps of the close.
> **＋** `entity-sprint-plugin`: the sprint page that holds the close line.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the skill the close line starts.
> **＋** `estimate-skill-sprint-close-leads-the-closing-session`: the check of the steps of the skill.
> **＋** `estimate-sprint-close-takes-the-readings-in-groups`: the check of the readings of the closing session.
> **＋** `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`: the check of the move of the sprint page to the archive.

> **when:**
> In the session that closes `entity-sprint-plugin`, the person takes up the line ``the close of `plugin` — `/sprint-close`, a session of its own`` of its `## Milestones`; at the end of Work Mode someone reads that session's `frontier.md`, ledger, `spec.md` and transcript.

> **then:**
> From that line to the end of Work Mode, no step of `/sprint-close` of `.claude/skills/sprint-close/SKILL.md` is done or fixed by hand outside what the skill sets.
> **－** The steps the skill sets are not part of this promise: `estimate-skill-sprint-close-leads-the-closing-session` and `estimate-sprint-close-takes-the-readings-in-groups` hold them.
> **－** The move of the pages to the archive in the librarian's run is not part of this promise: `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` holds it.

```then
create:
- slug: estimate-sprint-plugin-close-steps-run-from-the-line
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether the session that closes sprint plugin runs /sprint-close from the close line up to the end of Work Mode with no step done or fixed by hand
  method: 'by hand, at the end of Work Mode of the session that closes entity-sprint-plugin: its frontier.md, ledger, spec.md and transcript'
  tags:
  - sprint
  - workflow
```

```tasks
- [x] create `estimate-sprint-plugin-close-steps-run-from-the-line`
- [ ] read `estimate-sprint-plugin-close-steps-run-from-the-line`
```

### Case 756.3 — The README describes the project

> **given:**
> `estimate-sprint-plugin-readme-describes-the-project`: the new check of the README.
> **＋** `entity-sprint-plugin`: the sprint page.
> **＋** `README.md`: the description of the project at the root of the repository.

> **when:**
> In a session of the sprint `plugin` before its close, the person reads `README.md`.

> **then:**
> `README.md` says what GUPPI is and what it is for.
> **＋** It names the main parts of the project and what each one does.
> **＋** It says how to install GUPPI and how to use it.
> **＋** The person says that it describes the project as it stands.

```then
new_tags:
- tag: readme
  meaning: 'the README of the repository: what the project is, its parts and how to use it'
  aliases: ридми, описание проекта
create:
- slug: estimate-sprint-plugin-readme-describes-the-project
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether README.md says what GUPPI is and what it is for, its main parts and how to install and use it, as the person confirms
  method: by hand, the person's answer on README.md, in a session of the sprint plugin before its close
  tags:
  - sprint
  - readme
```

```tasks
- [x] create `estimate-sprint-plugin-readme-describes-the-project`
- [ ] read `estimate-sprint-plugin-readme-describes-the-project`
```

### Case 756.4 — A pull request is checked and reviewed on GitHub

> **given:**
> `estimate-sprint-plugin-pull-requests-reviewed-on-github`: the new check of pull requests.
> **＋** `entity-sprint-plugin`: the sprint page.
> **＋** the repository of the project on GitHub, with its branch `main`.

> **when:**
> In a session of the sprint `plugin` before its close, someone opens a pull request against `main` of the repository of the project on GitHub from an account other than the owner's.

> **then:**
> The checks of CI run on the pull request and show their result on it.
> **＋** The owner reviews the pull request on GitHub and can merge it into `main`.

```then
create:
- slug: estimate-sprint-plugin-pull-requests-reviewed-on-github
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether a pull request from another account runs the checks of CI on GitHub and can be reviewed and merged into main
  method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close
  tags:
  - sprint
  - github
  - git
```

```tasks
- [x] create `estimate-sprint-plugin-pull-requests-reviewed-on-github`
- [ ] read `estimate-sprint-plugin-pull-requests-reviewed-on-github`
```

### Case 756.5 — CI writes the clean branch

> **given:**
> `estimate-sprint-plugin-ci-writes-a-clean-branch`: the new check of the clean version.
> **＋** `entity-sprint-plugin`: the sprint page.
> **＋** the repository of the project on GitHub, with its branch `main` and its CI.

> **when:**
> In a session of the sprint `plugin` before its close, a commit lands on `main` of the repository of the project on GitHub, and CI runs on it.

> **then:**
> CI writes a clean version of the project to a branch of its own.
> **＋** No text of the clean version holds a reference to a case or a decision.
> **＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
> **＋** A check of CI fails the run when a case reference or session data remains in the clean version.

```then
new_tags:
- tag: ci
  meaning: 'the continuous integration of the repository on GitHub: its runs, its checks and the branches it writes'
  aliases: CI, CI/CD, непрерывная интеграция
create:
- slug: estimate-sprint-plugin-ci-writes-a-clean-branch
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data, and fails when one remains
  method: by hand, a CI run on GitHub and the clean branch it wrote, read in a session of the sprint plugin before its close
  tags:
  - sprint
  - ci
  - git
```

```tasks
- [x] create `estimate-sprint-plugin-ci-writes-a-clean-branch`
- [ ] read `estimate-sprint-plugin-ci-writes-a-clean-branch`
```

### Case 756.6 — The clean branch installs as a plugin

> **given:**
> `estimate-sprint-plugin-installs-as-a-plugin`: the new check of the plugin.
> **＋** `entity-sprint-plugin`: the sprint page.
> **＋** the clean branch that CI writes in the repository of the project on GitHub.
> **＋** `/hi`: the command that opens a working session, run in the project the plugin goes into.

> **when:**
> In a session of the sprint `plugin` before its close, someone installs the clean branch as a Claude Code plugin into an empty project, opens Claude Code there and types `/hi`.

> **then:**
> The plugin installs with no error.
> **＋** `/hi` opens a working session in that project.

```then
new_tags:
- tag: plugin
  meaning: 'GUPPI as a Claude Code plugin: its clean version, its install and its use in another project'
  aliases: плагин
create:
- slug: estimate-sprint-plugin-installs-as-a-plugin
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether the clean branch installs as a Claude Code plugin into an empty project and /hi runs there
  method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close
  tags:
  - sprint
  - plugin
```

```tasks
- [x] create `estimate-sprint-plugin-installs-as-a-plugin`
- [ ] read `estimate-sprint-plugin-installs-as-a-plugin`
```

## Case 761 — Each contradiction of the brief stands in Cases

> **context:**
> At the end of its run the librarian rewrites `vault/wiki/brief.md`. Its section Next session sorts the open items into three lists, and `Cases` is what needs a decision. The Render of `rule-brief` puts "a contradiction" there, and the Criterion of `estimate-brief-written` says the same. At the /hi of this session the reading of that Estimate failed: the brief of the run ab8be60f holds under Flags the contradiction that the handoff of session 1555 gave under Observations — the `－` line of `estimate-sprint-migration-merges` puts the merge on a `## Backlog` line of `entity-sprint-migration` that the page does not hold — and no line of `Cases` holds it. Both pages stand under `vault/archive/migration/2026-10-10/1555/`. The other contradiction of those Flags, on `estimate-sprint-close-settles-unread-estimates`, reached `Cases` through a line of `## For the next session` of the handoff. The Render does not say that each contradiction of Flags is meant, or what a contradiction between archived pages is, so the librarian could leave one out by a judgment the Render forbids elsewhere. The contradiction itself needs no work: the merge it speaks of is the work of Case 757. The person chose that the Render say it outright, the Criterion kept at first. The person first chose to read the Estimate at the /hi after each run of the librarian; the check of this file refused that `method`, since a `method` holds only what runs in its own session, and the person then kept the `method` as it stands, a reading at the /hi after the librarian's run of the session that closes a sprint. The Criterion of `estimate-brief-written` held the same words as the Render, "a `failed` Estimate, a contradiction, a defect the librarian found", so it did not state the two new promises; at `/pre-spec` the person chose to replace it whole. The new Criterion is the old one with the `Cases` line naming each contradiction of Flags, archived pages too, and one `－` line for a contradiction that `## For the next session` already carries; the rest stands word for word. The page goes `pending`. The person first kept its `method`, a reading at the /hi after the close of a sprint; the check of this file refused a `pending` page whose `method` waits for another session, and the person chose a reading of the rendered `.claude/agents/librarian-guppi.md` at the Retro of this session. That reading cannot run then: the `update` of `rule-brief` reaches the page at `guppi generate` and `guppi render` writes the frame after `guppi cleanup`, both in the librarian's run (steps 2 to 4 of `.claude/agents/librarian-guppi.md`), and `render` ticks the render line of this Case there (`orchestration.md`). The person then chose their own answer, on the brief the librarian writes, at the /hi after the close of `plugin`; `lint.waits_for_another_session`, the predicate the check of this file calls, leaves to another session a part of a `method` that names the person. The page has no `purpose` field that states the old promise. In `rule-brief`, read whole, the sentences that state what goes into `Cases` are the `Cases` sentence of the Render, which the pair changes; "Write facts and flags only. Add no decision and no judgment of the work." and the Purpose's "nothing in the brief is a decision", which the change follows and which stand; and the paragraph of the skill `carry`, whose `Cases` is always the line "none", which stands, since the new sentence is in the librarian's list alone. The Criterion of `estimate-brief-carries-the-run-facts` speaks of Readings due, not of `Cases`, and stands. A Grep `Next session` over `vault/wiki/rules/` printed `rule-documentation.md`, `rule-skill-hi.md`, `rule-brief.md` and `rule-carry-over.md`, and over `.claude/` printed `.claude/skills/hi/SKILL.md`, `.claude/agents/librarian-guppi.md` and `.claude/skills/carry/SKILL.md`; `rule-skill-hi` and `.claude/skills/hi/SKILL.md` take the lines of `Cases` into the Frontier and read any line, `rule-documentation` names the reads the brief needs, and the carry pages set the short shape, so none of them sets the form of a contradiction line and all stand. A Grep `librarian-guppi|rule-brief|estimate-brief` over `tests/` printed one line, in `tests/test_grepguard.py`, which names the agent and reads no live file of it, so no test reads the new text.

> **problem:**
> The brief left a contradiction of its Flags out of `Cases`, though the brief rule puts a contradiction there, because the rule does not say that each contradiction is meant, archived pages too.

> **recommend:**
> - **What should change after the brief missed the contradiction?**
>   - Recommended: (a) the rule says it outright: each contradiction of Flags also gets a line in `Cases`, one between archived pages too, and one that a line of the handoff's For the next session already carries stands once; the check keeps its wording and stays failed until its next reading.
>   - Answer: agreed, (a).
> - **When should the check be read next?**
>   - Recommended: (a) keep the current timing, since the check of the Case file refuses a method that waits for another session: the check stays failed and is read next at the start of the session after the close of `plugin`.
>   - Answer: agreed, (a).
> - **What method should the check use once its wording is replaced?**
>   - Recommended: (a) read the rule text at the end of this session: the rendered librarian instructions read by hand against the new wording.
>   - Answer: agreed, (a).
> - **How can the check be read when the new rule text reaches the instructions only after this session?**
>   - Recommended: (c) your own answer on the brief at the start of the session after the close of `plugin`.
>   - Answer: agreed, (c).
> - **Change**
>   - Asked: at `/pre-spec`, replace the Criterion of `estimate-brief-written` so that it holds both new promises, the page set `pending`, its method and moment unchanged.
>   - Taken: the Case adds an `update` of `estimate-brief-written` with its Criterion replaced whole, and a reading of it; its method changes as the answer on the method of the check sets it.

> **given:**
> `rule-brief`: the rule of the brief, whose Render sets the lists of Next session.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian's frame, which holds that Render.
> **＋** `estimate-brief-written`: the check of the brief, whose Criterion is replaced whole.
> **＋** `vault/wiki/brief.md`: the brief the librarian writes.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff the brief reads.
> **＋** `vault/archive/`: the folder of the pages a sprint close moves.

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run, and its Flags hold a contradiction.

> **then:**
> `Cases` of Next session holds a line for each contradiction of Flags, with what and from where.
> **＋** A contradiction between pages that stand in `vault/archive/` gets its line too.
> **－** A contradiction that a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md` already carries gets no second line in `Cases`.

```then
update:
- slug: rule-brief
  replace:
  - old: a `failed` Estimate, a contradiction, a defect you found — what and from where.
    new: a `failed` Estimate, each contradiction of Flags (one between pages in `vault/archive/` too; one that a line of `## For the next session` already carries stands in that line alone), a defect you found — what and from where (case 761).
  change: Cases of Next session hold each contradiction of Flags, one between archived pages too, once (case 761)
- slug: estimate-brief-written
  set:
    status: pending
    method: by hand, the person's answer at the /hi after the librarian's run of the session that closes a sprint, on vault/wiki/brief.md of that run, whether Cases hold each contradiction of Flags, one between archived pages too, and once where a line of For the next session carries it, recorded in the estimate line
  sections:
    Criterion: |-
      When:
      The librarian rewrites `vault/wiki/brief.md` at the end of its run.

      Then:
      The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
      **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
      **＋** Where things stand, Readings due and Readings at the close are as before.
      **＋** Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
      **＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and add one kind: a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
      **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>`; a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, each contradiction of Flags, one between pages that stand in `vault/archive/` too, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
      **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
      **＋** An item stands in one list only. A list with no item is the line "none".
      **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
      **－** A contradiction of Flags that a line of `## For the next session` of `handoff.md` already carries gets no second line in `Cases`.
      **－** The brief states no decision: the sort by kind is not a judgment of the work.
  change: the Criterion replaced whole — Cases hold each contradiction of Flags, one between archived pages too, once; read by the person's answer on the brief after a sprint close (case 761)
```

```tasks
- [x] update `rule-brief`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] update `estimate-brief-written`
- [ ] read `estimate-brief-written`
```

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

```then
create:
- slug: estimate-skill-sprint-close-migration-merged-into-main
  ref: rule-skill-sprint-close
  kind: QA
  purpose: Whether the session that opens the sprint plugin moves main to the last commit of migration by a fast-forward, goes on on the branch plugin, deletes migration and ticks the merge line of the closing Spec
  method: 'by hand, at the Retro of the session that opens the sprint plugin: git branch --list, git log -1 main against the last commit of migration that Work Mode printed, the make test run of its Work Mode against work.md, and vault/raw/2026-10-10/1555/spec.md'
  tags:
  - sprint
  - git
  - workflow
```

```tasks
- [x] create `estimate-skill-sprint-close-migration-merged-into-main`
- [x] by hand: as the first task of Work Mode, run `git switch main`, `git merge --ff-only migration`, `git switch -c plugin` and `git branch -d migration`; a refusal of the merge or of the deletion is a stop on the first condition of `vault/wiki/where-to-stop.md`.
- [x] by hand: run `make test` on `plugin` right after the switch, and hold each failing test against `## Baseline` of `vault/raw/2026-10-10/1713/work.md`.
- [x] by hand: tick the line ``the merge of `migration` into `main` — the first work of the session that opens the next sprint, after its opening Case`` in `vault/raw/2026-10-10/1555/spec.md`.
- [x] read `estimate-skill-sprint-close-migration-merged-into-main`
```

## Case 763 — A failed Estimate outside the sprint page is settled only by name

> **context:**
> At the close of a sprint, `uv run guppi sprint-close` lists each Estimate that stands `pending` or `failed`, and the close refuses to move a page until each listed Estimate is settled. `guppi/sprint_close.py` settles a `failed` Estimate without a name only when the sprint page lists it. For any other listed Estimate, `failed` or `pending`, it wants a name by `--carry` or `--archive-unread`. The function `settled` holds this rule, and `tests/test_sprint_close.py` pins it: an unnamed `failed` Estimate outside the sprint page is refused. The Criterion of `estimate-sprint-close-settles-unread-estimates`, which stands `passed`, promises otherwise: such an Estimate, read now with a `failed` result, counts as settled and is carried with no name. The code cannot keep that promise as written, because a page that failed in the closing session looks the same as one that has stood `failed` since an earlier sprint. The handoff of session 1555 reported the disagreement under Observations. The person chose to make the check follow the code, so no code and no test changes.
>
> This Case replaces Case 759, which changed only that Estimate. Pre-spec found two faults in it. First, the `－` line of `estimate-sprint-close-takes-the-readings-in-groups` allows the close line to name only an Estimate still unread after Work Mode. Under the new rule, the close line must also name an Estimate read `failed` in Work Mode that the sprint page does not list. Second, the preview over the live vault in the `method` of the first Estimate cannot run in this session. `Close.__init__` of `guppi/sprint_close.py` stops with no live `entity-sprint-<id>` page, a Glob of `vault/wiki/entities/entity-sprint-*.md` printed no file, and `entity-sprint-migration` stands only under `vault/archive/migration/2026-10-10/1555/`. So Case 763.1 replaces the Criterion of `estimate-sprint-close-settles-unread-estimates` and sets its `purpose` and its `method`. The `method` becomes the `pytest -k settle` run alone. The `When` keeps its line on the preview over the live vault for a later reading. The new Criterion keeps each old line but two. It leaves out on purpose the line that a `failed` reading counts as settled, and puts in its place one line for an Estimate of the sprint page and one for any other Estimate. It keeps the rule that no page moves before the person has chosen for each listed Estimate. Case 763.2 replaces the Criterion of `estimate-sprint-close-takes-the-readings-in-groups` and sets its `purpose`, which states the old promise in its last clause. By the person's answer it sets the `method` to a reading, in this session, of the closing Case and the ledger of the last session that closed a sprint, `vault/raw/2026-10-10/1555/`. That close named five Estimates by `--carry` and none stood `failed`, so the reading passes without testing the new case; the close of `plugin` is its first real test. The new Criterion leaves out on purpose the old `－` line and keeps the other lines. The `then` of the two sub-cases shares words, but the promises differ and can fail apart. Case 763.1 checks what the command `uv run guppi sprint-close` settles. Case 763.2 checks what the closing session writes into its closing Case and its close line.
>
> Step 4 of the Render of `rule-skill-sprint-close` has the closing Case name by `--carry` or `--archive-unread` each Estimate still unread after Work Mode. A closing Case built from that step would leave out an Estimate read `failed` in Work Mode outside the sprint page, and the close would refuse. So Case 763.2 adds that Estimate to the step by a `replace` pair and renders `.claude/skills/sprint-close/SKILL.md`. No other Estimate of that rule reads the live file. A Grep for `still unread` over `vault/wiki/`, `.claude/` and `guppi/` printed `.claude/skills/sprint-close/SKILL.md`, `vault/wiki/rules/rule-skill-sprint-close.md`, `vault/wiki/estimates/estimate-skill-sprint-close-leads-the-closing-session.md` and `vault/wiki/estimates/estimate-sprint-close-takes-the-readings-in-groups.md`. The Criterion of `estimate-skill-sprint-close-leads-the-closing-session` stands. It asks for the person's choice for each Estimate still unread and does not say that only those are named, so naming one more stays true under it. No test reads `.claude/skills/sprint-close/SKILL.md` or either Estimate page live. A Grep for `skills.{0,10}sprint-close|still unread` over `tests/` printed nothing. A Grep for either Estimate slug over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-sprint-close.md`. The rule page only lists them in `estimates` and stands. The docstring of `guppi/sprint_close.py` already states the code's rule and stands. Case 757 creates an Estimate under `rule-skill-sprint-close` and does not change its Render. Case 756 creates `estimate-sprint-plugin-close-steps-run-from-the-line` on the flow of the closing session as a whole and does not cover this settling.

> **problem:**
> The Criterion of `estimate-sprint-close-settles-unread-estimates` promises that a `failed` reading of an Estimate outside the sprint page settles that Estimate with no name. `guppi/sprint_close.py` and its tests require a name by `--carry` or `--archive-unread` for it. A signed check that the code does not keep stands `passed`, and the check of the closing session and its skill would leave such an Estimate unnamed.

> **recommend:**
> - **Which side follows the other**
>   - Recommended: (a) the check follows the code. The Criterion is replaced so that a `failed` Estimate outside the sprint page must still be named by `--carry` or `--archive-unread`, its `purpose` is reworded, and no code changes.
>   - Answer: agreed, (a).
> - **How the check of the grouped readings is read in this session**
>   - Recommended: (a) read the last close now. The line is fixed so that the close line names an Estimate still unread after Work Mode, or one read `failed` in Work Mode that the sprint page does not list, and the method becomes a reading by hand, in this session, of the closing plan and ledger of the last session that closed a sprint.
>   - Answer: agreed, (a).

### Case 763.1 — The close settles a failed Estimate outside the sprint page only by name

> **given:**
> `estimate-sprint-close-settles-unread-estimates`: the check of the settling step of the close; its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-sprint-close`: the rule the Estimate checks.
> **＋** `guppi/sprint_close.py`: the command `uv run guppi sprint-close` that the Criterion reads.
> **＋** `tests/test_sprint_close.py`: the made-up vault and the `settle` tests the Criterion runs.
> **＋** `entity-sprint-<id>`: the sprint page whose `estimates` the close reads.
> **＋** `vault/wiki/estimates/`: the live Estimates the close lists.
> **＋** `vault/archive/`: where the moved pages stand.

> **when:**
> `uv run guppi sprint-close --sprint <id>` closes the sprint `entity-sprint-<id>` of the made-up vault of `tests/test_sprint_close.py`, its preview first and then its run with `--apply`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.
> **＋** Or the preview `uv run guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/estimates/`.

> **then:**
> Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
> **＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
> **＋** An Estimate read now has its reading in the ledger.
> **＋** A listed Estimate that `entity-sprint-<id>` lists and that stands `failed` counts as settled: it stands under `vault/archive/` with the sprint page, and the record of the close keeps its status.
> **＋** A listed Estimate that `entity-sprint-<id>` does not list counts as settled only when the close names it by `--carry` or `--archive-unread`, also when a reading read now came out `failed`.
> **＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
> **＋** An Estimate archived unread stands under `vault/archive/`, and the page that listed it no longer lists it in `estimates`.
> **－** No page of the close moves before the person has chosen for each listed Estimate.
> **－** An Estimate that `entity-sprint-<id>` lists is not carried into the next sprint: the person reads it now or archives it unread.

```then
update:
- slug: estimate-sprint-close-settles-unread-estimates
  set:
    status: pending
    purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves; an Estimate of the sprint page is read or archived with the sprint page and never carried, and one that stands failed goes with the sprint page; any other Estimate, one whose reading came out failed included, is settled only when the close names it to be carried or archived
    method: pytest tests/test_sprint_close.py -k settle
  change: the Criterion replaced whole — a failed Estimate outside the sprint page is settled only when --carry or --archive-unread names it, as guppi/sprint_close.py does; the purpose set anew; the method the pytest run alone, since no sprint page is live to preview
```

```tasks
- [x] update `estimate-sprint-close-settles-unread-estimates`
- [x] read `estimate-sprint-close-settles-unread-estimates`
```

### Case 763.2 — The close line names a failed reading outside the sprint page

> **given:**
> `estimate-sprint-close-takes-the-readings-in-groups`: the check of the closing session; its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-skill-sprint-close`: the skill whose step 4 has the closing Case write the close line.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the rendered skill.
> **＋** `entity-sprint-<id>`: the sprint page whose `estimates` the close reads.
> **＋** `vault/wiki/estimates/`: the Estimates the closing Case sorts.
> **＋** `vault/raw/<date>/<hi HHMM>/spec.md` and `vault/raw/<date>/<hi HHMM>/ledger.md`: the closing Case and the readings of the closing session.

> **when:**
> The session that closes `entity-sprint-<id>` runs its Plan Mode and its Work Mode; someone reads its closing Case in `vault/raw/<date>/<hi HHMM>/spec.md` and its `vault/raw/<date>/<hi HHMM>/ledger.md` after its Work Mode.

> **then:**
> The `context` of the closing Case sorts each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed` into groups by the kind of moment its `method` names.
> **＋** The `tasks` of the closing Case hold one `by hand` task per moment that Work Mode sets up, and one `read` line per Estimate of each group.
> **＋** Work Mode sets up each such moment, and the ledger holds a reading of each Estimate whose moment came.
> **＋** The close line names by `--carry` or `--archive-unread` each Estimate read `failed` in Work Mode that `entity-sprint-<id>` does not list.
> **－** The close line names by `--carry` or `--archive-unread` only an Estimate still unread after Work Mode, or one read `failed` in Work Mode that `entity-sprint-<id>` does not list.

```then
update:
- slug: estimate-sprint-close-takes-the-readings-in-groups
  set:
    status: pending
    purpose: Whether the session that closes a sprint sorts the pending and failed Estimates into groups by the kind of moment their method names, sets up each moment it can in its Work Mode, and carries or archives unread only those still unread and those read failed that the sprint page does not list
    method: 'by hand, in the session that changes this page: the closing Case in the spec.md and the ledger.md of the last session that closed a sprint, now vault/raw/2026-10-10/1555/, read against the Criterion'
  change: the Criterion replaced whole — the close line also names an Estimate read failed in Work Mode that the sprint page does not list; the purpose and the method set anew
- slug: rule-skill-sprint-close
  replace:
  - old: for each Estimate still unread after Work Mode; an Estimate of the sprint page is never carried.
    new: for each Estimate still unread after Work Mode and each one read `failed` in Work Mode that the sprint page does not list; an Estimate of the sprint page is never carried.
  change: 'step 4: the close line also names an Estimate read failed in Work Mode that the sprint page does not list'
```

```tasks
- [x] update `estimate-sprint-close-takes-the-readings-in-groups`
- [x] update `rule-skill-sprint-close`
- [x] `uv run guppi render`: `.claude/skills/sprint-close/SKILL.md`
- [x] read `estimate-sprint-close-takes-the-readings-in-groups`
```

## Deferred

## Case 758 — rule-morph put off into the sprint plugin

> **context:**
> At Plan Mode of session 1713 the person put off `rule-morph` again, as the handoff of session 1555 proposed. Its stale-defer lint line, `rules/rule-morph: deferred: 3 times since case 239`, goes with it into the sprint `plugin`. No Case of this session changes the categories of the project or the read rules of `rule-permissions`.

> **problem:**
> No Case of this session decides how the person sets the category set of the project at install.

```then
defer:
  - slug: rule-morph
    type: rule
    purpose: "The initiation at install: the person sets the category set of the project, held as data, and the folder of saved transcripts in the read rules of rule-permissions; put off again at Plan Mode of session 1713"
```
