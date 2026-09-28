## Case 479 — Work Mode gets the skill /work: the fork asks for it, it writes a baseline and the marks of an expected red, and Retro reads both

> **context:**
> Some Cases change a check in code and also the page that the check reads. The new code runs as soon as it is written, but the page changes only at the librarian's run. Between those two moments `make lint` is red, and that is expected. Today one sentence of `rule-retro` (case 473.1) turns such a red into a note for the handoff. It does this by the agent's own judgment at `/retro`. Nothing marks the red at the moment it is caused. Nothing records which reds stood before the work either, so at Retro the agent cannot tell a red this session caused from a red it found. `rule-work-mode` should hold that part, but it is a `draft` with only a Purpose ("Prevents implementation starting before the plan, branch and baseline exist"). It has no text that a session loads, and 20 Cases defer it. After `ExitPlanMode` the hook `guppi spec` tells the agent to ask in words: Work Mode or `/carry`. `/carry` is a skill, and Work Mode is none.
> The person decided in two rounds. `rule-work-mode` is taken up with a minimum. It holds the Render of a new skill, `/work`. The skill stops on `main`. Before the first change it writes a baseline, the result of `make test` and `make lint`, into `raw/<date>/<hi HHMM>/work.md`. It runs the tasks in order and ticks each box. When a task changes a check that reads a page or a governed file the same Spec updates, it writes a line under `## Expected red` of the same file, naming the check and the page or file. The agent calls `/work` when the person picks it at the fork, and the person may type it to resume. The fork is asked by `AskUserQuestion` with the two options `/work` and `/carry`. Retro reads `work.md`. A red on a page or file that a mark names ends as a note for the handoff. A red line that the baseline already holds is not charged to the session, whatever the marks name. Any other red is debt. In a session with no `work.md`, the sentence of 473.1 stands as it is. `work.md` joins the allow list of `rule-permissions`.
> The person then changed 479.2. The skill takes the branch and the baseline through `!` substitutions that run when it loads. `insight-hi-skill-substitution-checked-by-a-model-call` records that a model call checks such a command before it runs, and that the substitution comes back empty when that call fails. In this session the permission classifier failed to answer several times. With an empty substitution, `## Baseline` would be empty, and Retro would charge every red to the session. So when a substitution is empty, the agent runs that command itself before it goes on. The Insight stays in the backlog as it is.
> At pre-spec the person accepted three fixes. First, a red counts as expected only on the page or file a mark names. Before this fix, one mark on `make lint` would have excused an unrelated new finding. Second, a line the Baseline holds is not debt under any mark. Before this fix, 479.3 and 479.4 contradicted each other. Third, the text of `rule-retro` keeps 473.1 for a session with no `work.md`.
> The vault's answer: every `create` carries a `ref`, so no vault query ran. A Glob of `vault/**/` finds no page for `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` or `estimate-retro-red-in-the-baseline-is-not-charged`. 479.2 names `rule-work-mode`, so it carries one `{supersedes:case N}` block for each of the 20 Cases in its `deferred_by`. The Backlog entry of `rule-work-mode` in `entity-sprint-migration` still names the sentence of `insight-workflow-code-live-before-the-page-it-reads` and case 238. Case 473 placed that sentence in `rule-retro` and 473.2 retired 238, so 479.2 rewrites the entry to the part of Work Mode that is left. `vault/wiki/sprint.md` does not show the Backlog, so no sprint render follows.
> The frame. The rule "never a picker tool" of `vault/wiki/case-schema.md` (case 355.1) is about the ratification of a Case. The fork is the end of a session, not a Case, so the rule stays true, and 479.1 says so in a `－` line. The Render of `rule-carry-over` says it runs "when the person answered the fork with 'conserve'". The `/carry` option is described as conserving the Spec, so that sentence and `estimate-carry-over-writes` stay true. The Criterion of `estimate-session-phases-in-order` lists the marks of a session and does not list `work.md`. A new mark of Work Mode makes no line of it false, so it is not touched. `estimate-guppi-tests-green` still wants `make test` with no failed test on the branch. A test that was red in the baseline stays red there, and 479.4 says so. `estimate-retro-loads` and `estimate-retro-report-holds-each-fact-once` promise the readings and the form of the report. They make no promise about the first read call of Retro, which 479.3 changes, so neither is touched. The glossary row for Work Mode describes the planned model with subagents and stays.
> The replaced Criteria carry their old lines word for word, except these lines, which change on purpose. In 479.1, the line on the stdout named "Work Mode on the Spec or `/carry`". It becomes the stdout line and the line on `AskUserQuestion` with `/work` and `/carry`. In 479.3, the line on the frontier item now requires a mark on the page or file. The line on a red test keeps "fixed or reverted into a patch" and loses "the handoff still needs green", because 479.4 lets the commit wait for no test that was red in the baseline. That exception follows from the person's answer that a baseline red is not charged. In 479.5, `when` adds `work.md`. The line on the allow list names the entries with `work.md` added and no count. The line "Nothing else under `wiki/` is allowed." is dropped, because the carried line on `deny` and `ask` says the same.
> Timing. `guppi/spec.py` runs from the working tree at once. `.claude/skills/work/SKILL.md`, the Retro text and the allow list land at the librarian's render. So an `ExitPlanMode` later in this session would offer `/work` before the skill exists, and the agent would then run Work Mode as it does today. No reader refuses anything, so nothing is lost and no old form is kept.
> Not done: subagents in Work Mode (`rule-subagent-guppi`), the test of each Estimate written first, the Spec box (`rule-spec-box`), and the full Work Mode model the person plans. No script compares a red with `work.md`. The agent reads the file by hand at Retro. 19 of the 20 superseded Decisions, cases 183 to 322, also defer `rule-subagent-guppi`. `generate` clears a defer only from the pages the superseding Case names, so those defers stay on `rule-subagent-guppi` and point at superseded Decisions. The person chose to leave them: the Case that takes up `rule-subagent-guppi` retires them.

> **problem:**
> Work Mode has no text a session loads. It takes no baseline and checks no branch, and it marks nothing when it causes an expected red. So Retro judges each red on its own: an expected red and a red that stood before the work cannot be told apart from a red the session caused. The fork after `ExitPlanMode` also names Work Mode as plain words while `/carry` is a skill.

> **recommend:**
> Five sub-cases, one promise each. 479.1 is the fork, asked by `AskUserQuestion` with `/work` and `/carry`. 479.2 takes up `rule-work-mode` as the Render of `/work`: the branch, the baseline (with the agent's own run when a substitution is empty), the tasks in order with their ticks, and the mark of an expected red. 479.3 is Retro reading `## Expected red` in place of the agent's own judgment, finding by finding. 479.4 is Retro not charging a red that `## Baseline` holds. 479.5 is `work.md` in the allow list. The rejected option was one Case with one Estimate: its conditions fail on their own and need different fixes.

### Case 479.1 — The fork after ExitPlanMode asks by AskUserQuestion: /work or /carry

> **given:**
> `guppi/spec.py` — `fork_line` and the docstring, the line the hook prints after the Spec is written
> **＋** `tests/test_spec.py` — the tests of the printed fork
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec, which the hook writes
> **＋** `/hi` — opens the session; without its `hi` line the hook writes no Spec
> **＋** `rule-spec-capture` — its Purpose, on the fork
> **＋** `.claude/skills/work/SKILL.md` and `.claude/skills/carry/SKILL.md` — the two skills of the fork
> **＋** `vault/wiki/case-schema.md` — a Case ends with a plain question, never a picker tool
> **＋** `estimate-spec-capture-appends` — the writing of the Spec, which stands
> **＋** `estimate-spec-capture-offers-the-fork` — its Criterion replaced whole

> **when:**
> `guppi spec` has run on `PostToolUse` of `ExitPlanMode` and written the Spec, or found it already there.

> **then:**
> The stdout of the hook is one JSON object, `hookSpecificOutput` with `hookEventName: PostToolUse` and `additionalContext`, that holds the fork line with the session folder and the Spec file.
> **＋** For `PostToolUse` Claude Code adds to the agent's context only `hookSpecificOutput.additionalContext` from a JSON object on stdout; plain stdout with exit 0 goes to the debug log.
> **＋** The agent sees this line in the `ExitPlanMode` result.
> **＋** The fork line tells the agent to ask the person by `AskUserQuestion` with two options, `/work` (Work Mode on the Spec now) and `/carry` (the Spec conserved for a later session), and to start nothing until the person answers.
> **＋** On the answer, the agent calls `.claude/skills/work/SKILL.md` or `.claude/skills/carry/SKILL.md`, the skill of the option picked.
> **－** A `PostToolUse` hook blocks nothing: the tool has run.
> **－** Without a Spec, nothing, as before.
> **－** The path "no `/hi` for this session" — stderr, exit 2 — does not change.
> **－** A Case is still ratified by the person's reply in the chat, never by a picker tool, as `vault/wiki/case-schema.md` says: the picker is for the end of the session only.
> **－** The writing of the Spec does not change: that is the promise of `estimate-spec-capture-appends`.

> **tasks:**
> - [ ] update `rule-spec-capture`
>   - old: `` into the context — Work Mode, or `/carry` to conserve the Spec — naming the session folder and the Spec file; it blocks nothing, the agent asks and the person chooses (case 190.5). ``
>   - new: `` into the context — `/work`, Work Mode on the Spec, or `/carry` to conserve it — naming the session folder and the Spec file; it blocks nothing: the agent asks the person by `AskUserQuestion` with the two options, the person picks, and the agent calls the skill picked (cases 190.5, 479.1). ``
>   - change: `the fork is asked by AskUserQuestion with the two options /work and /carry, and the agent calls the skill picked (case 479.1)`
> - [ ] update `estimate-spec-capture-offers-the-fork`
>   - set: `{status: pending, purpose: "The hook prints the fork after the Spec is written: the agent asks by AskUserQuestion with the options /work and /carry, and calls the skill picked", method: "uv run pytest tests/test_spec.py -k fork; by hand, the first ExitPlanMode of a session after the render: the fork asked by AskUserQuestion with /work and /carry, and the skill picked called"}`
>   - change: `the Criterion replaced whole — the fork is asked by AskUserQuestion with /work and /carry, and the skill picked is called (case 479.1)`
> - [ ] `guppi/spec.py` — `fork_line`: ask the person by `AskUserQuestion` with two options, `/work` (Work Mode on the Spec now) and `/carry` (conserve it for a later session, the brief rewritten, `carry.md` as the mark, a commit), start nothing until answered, then call the skill picked; the module docstring names `/work`
> - [ ] `tests/test_spec.py` — `-k fork`: the line holds `AskUserQuestion`, `/work` and `/carry`, the session folder and the Spec file; the fork printed again when the plan was already there; no fork without a Spec
> - [ ] read `estimate-spec-capture-offers-the-fork` — by hand, at the first `ExitPlanMode` of a session after the render

> **ratification:**
> ```
> - decision[case 479.1][update][rule-spec-capture]{ref:rule-spec-capture}
> - decision[case 479.1][update][estimate-spec-capture-offers-the-fork]{ref:estimate-spec-capture-offers-the-fork}
> ```

### Case 479.2 — rule-work-mode holds the skill /work: branch, baseline, tasks in order, the mark of an expected red

> **given:**
> `rule-work-mode` — the Rule of Work Mode, taken up; its Render is the skill
> **＋** `.claude/skills/work/SKILL.md` — the skill, rendered in full from `rule-work-mode`; its `!` substitutions run when it loads
> **＋** `raw/<date>/<hi HHMM>/work.md` — the baseline and the marks of an expected red, written by the skill
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec, its tasks and boxes
> **＋** `git branch --show-current`, `make test` and `make lint` — the commands of the branch check and of the baseline
> **＋** `vault/wiki/` — the pages, which only the librarian's run writes
> **＋** `entity-sprint-migration` — its Backlog entry on `rule-work-mode`
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — the new promise

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task.
> **＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.

> **tasks:**
> - [ ] update `rule-work-mode`
>   - set: `{kind: Leaf, enforcement: render, governs: .claude/skills/work/SKILL.md, render_mode: full, tags: [session, workflow, harness, render]}`
>   - sections.Purpose:
>     ```
>     Prevents implementation starting before the plan, branch and baseline exist. Work Mode runs the approved Spec of the session. Its skill `/work` starts after `ExitPlanMode`: the agent calls it when the person picks `/work` at the fork, and the person types it to resume a session that stopped in the middle. It stops on `main`. Before the first change it writes the baseline, the result of `make test` and `make lint`, into `raw/<date>/<hi HHMM>/work.md`, so that Retro charges to the session only a red the baseline does not hold. A substitution of the skill can come back empty when the model call that checks it fails, so the agent then runs the command itself. It runs the tasks in the order of the Spec and ticks each box. A task that changes a check that reads a page or a governed file the same Spec updates writes a mark of an expected red into the same file, naming the check and the page or file, and Retro reads it. Subagents in Work Mode, the test of each Estimate written first and the rest of the model are not decided yet (case 479.2).
>     ```
>   - sections.Render:
>     ````
>     <!-- rule-work-mode -->
>     ---
>     name: work
>     description: Work Mode on the approved Spec — check the branch, write the baseline, run the tasks in order and tick each box. The agent calls it when the person picks /work at the fork ExitPlanMode prints; the person types it to resume.
>     ---
>
>
>     Branch: !`git branch --show-current`
>
>     Tests: !`make test`
>
>     Lint: !`make lint`
>
>     A line above can come back empty when the check of its command fails. When Branch is empty, run `git branch --show-current` yourself before anything else. When Tests or Lint is empty, run `make test` and `make lint` yourself before the first change, and use their result for the Baseline.
>
>     Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder. If the branch is `main`, stop and say so: Work Mode does not start on `main`. Write and change nothing until the person moves to another branch and `/work` runs again.
>
>     Otherwise, before the first change, write `vault/raw/<date>/<hi HHMM>/work.md` with two sections. `## Baseline`: the exit code of `make test` and of `make lint`, then each failing test and each lint finding line as printed. `## Expected red`: empty for now. When `work.md` already stands, because the person typed `/work` to resume, keep its Baseline as it is: the baseline is taken once, before the first change.
>
>     Run the tasks of the Spec in the order the Spec holds them. Tick each box of code, a test, a migration or a `by hand` check in `spec.md` in the reply that finishes the task. The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian's scripts, not here.
>
>     When a task changes a check — `make lint` or one of its steps, or a hook of the working tree — that reads a page or a governed file this Spec updates, add one line under `## Expected red` in the same reply: the check, and the page or file it waits for. That check is red or refuses on that page or file until the librarian's run, and `/retro` ends that red as a note for the handoff.
>
>     Work Mode ends with `/retro`.
>     <!-- /rule-work-mode -->
>     ````
>   - change: `taken up: the skill /work — the branch, the baseline in work.md with the agent's own run when a substitution is empty, the tasks in order with their ticks, the mark of an expected red; every defer retired (case 479.2)`
> - [ ] create `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
>   - type: `estimate`
>   - ref: `rule-work-mode`
>   - kind: `QA`
>   - purpose: `Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec in order with their ticks, and marks an expected red under Expected red`
>   - method: `uv run guppi render --check; by hand, in a session after the render, the first /work the agent calls at the fork and the first /work the person types: the branch, work.md, the ticks of spec.md and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent's own run of its command, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] update `entity-sprint-migration`
>   - old: `` - [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; the sentence of [[insight-workflow-code-live-before-the-page-it-reads]] on a check that reads a page the same Spec changes; cases 183, 206, 238 ``
>   - new: `` - [[rule-work-mode]] — the rest of Work Mode past the skill `/work` of case 479.2: the test of each Estimate written first and turned green, and the full model the person plans; cases 183, 206 ``
>   - change: `the Backlog entry of rule-work-mode names what is left past the skill /work; the sentence on a red check stands in rule-retro (case 479.2)`
> - [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — by hand, in a session after the render

> **ratification:**
> ```
> - decision[case 479.2][update][rule-work-mode]{ref:rule-work-mode}{supersedes:case 183}{supersedes:case 206}{supersedes:case 218}{supersedes:case 231}{supersedes:case 242}{supersedes:case 248}{supersedes:case 252}{supersedes:case 254}{supersedes:case 260}{supersedes:case 263}{supersedes:case 269}{supersedes:case 276}{supersedes:case 281}{supersedes:case 285}{supersedes:case 289}{supersedes:case 293}{supersedes:case 303}{supersedes:case 307}{supersedes:case 322}{supersedes:case 447}
> - decision[case 479.2][create][estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]{ref:rule-work-mode}{tags:session,workflow,harness}
> - decision[case 479.2][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```

### Case 479.3 — Retro ends a red on a page or file that Expected red names as a note for the handoff

> **given:**
> `rule-retro` — its Render: the opening of the frontier, and the sentence on a check red before the librarian's run
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `raw/<date>/<hi HHMM>/work.md` — its `## Expected red` and `## Baseline`, written by `/work`
> **＋** `make lint` — the checks of the vault, run by the librarian after the render
> **＋** `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — its Criterion replaced whole

> **when:**
> The person invokes `/retro` in a session whose Spec updates a page or a governed file, and in Work Mode `make lint`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

> **then:**
> When it opens the frontier, the agent reads `raw/<date>/<hi HHMM>/work.md` if it stands, and makes no other read call.
> **＋** A red or a refusal of a check on a page or file that a line of `## Expected red` of `work.md` names with that check is an item of the frontier, and it ends as a note for the handoff that names the check and the page or file it waits for.
> **－** The red is not debt: the agent does not fix it or revert it into a patch.
> **＋** The reading of the check that counts is the `make lint` of the librarian's run, after the page is written and the file rendered.
> **＋** A red or a refusal on a page or file that no line of `## Expected red` names is debt, even when another line names the same check, unless `## Baseline` of `work.md` holds its line.
> **－** In a session with no `work.md`, a red or a refusal of such a check ends as a note for the handoff by the agent's judgment, as it did before `/work`.
> **－** A red test is never an expected red, even when `## Expected red` names it: it is fixed or reverted into a patch by the rule for red tests.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `Open with the frontier, in one message and with no read call.`
>   - new: `` Open with the frontier, in one message and with no read call but the Read of `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3). ``
>   - old: `such a red is an item of the frontier that ends as a note for the handoff, naming the check and the page or file it waits for, and it is not debt. A red test is not such a check: it is fixed or reverted as above (case 473.1).`
>   - new: `` `/work` marks such a red under `## Expected red` of `work.md` when the task that changes the check runs, one line naming the check and the page or file it waits for. A red or a refusal of that check on a page or file a line names is an item of the frontier that ends as a note for the handoff, naming the check and the page or file it waits for, and it is not debt; a red or a refusal on a page or file no line names is debt, even when another line names the same check, unless `## Baseline` holds its line. In a session with no `work.md`, such a red ends as a note for the handoff by your judgment, as before. A red test is never an expected red: it is fixed or reverted as above (cases 473.1, 479.3). ``
>   - change: `Retro reads work.md, and a red on a page or file that its Expected red names ends as a note for the handoff; any other such red is debt unless the Baseline holds it; with no work.md the judgment of case 473.1 stands (case 479.3)`
> - [ ] update `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
>   - set: `{status: pending, purpose: "Whether Retro reads work.md and ends a red or a refusal on a page or file that a line of its Expected red names as a note for the handoff, not as debt, while a red on a page or file no line names is debt unless the Baseline holds it, a session with no work.md keeps the judgment of case 473.1, and a red test is never an expected red", method: "one reading by hand at the first /retro after the render in a session whose work.md names a check under Expected red, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — the red is expected when a line of Expected red of work.md names its check and its page or file, not by the agent's judgment; with no work.md the judgment stands (case 479.3)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — by hand, at the first such `/retro` after the render

> **ratification:**
> ```
> - decision[case 479.3][update][rule-retro]{ref:rule-retro}
> - decision[case 479.3][update][estimate-retro-red-check-of-an-updated-page-is-a-handoff-note]{ref:estimate-retro-red-check-of-an-updated-page-is-a-handoff-note}
> ```

### Case 479.4 — Retro does not charge a red that the baseline already holds

> **given:**
> `rule-retro` — its Render: the paragraph on red tests, and the commit
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `raw/<date>/<hi HHMM>/work.md` — its `## Baseline` and `## Expected red`, written by `/work`
> **＋** `make test`, `make style` and `make lint` — the checks of the baseline and of the commit
> **＋** `estimate-guppi-tests-green` — `make test` with no failed test on the branch, which stands
> **＋** `estimate-retro-red-in-the-baseline-is-not-charged` — the new promise

> **when:**
> The person invokes `/retro` in a session whose `raw/<date>/<hi HHMM>/work.md` holds a `## Baseline`, and a test fails in the `make test` of Retro, or a lint finding stood in Work Mode.

> **then:**
> Retro counts each failing test and each lint finding line that `## Baseline` holds as red before the work, whatever `## Expected red` names, and writes it in the handoff as a note.
> **＋** It is not debt: nothing is fixed or reverted into a patch for it, and it gets no `lesson[error]` line.
> **＋** The commit of Retro needs `make style` clean and `make test` green, except for the failing tests that `## Baseline` holds.
> **＋** A failing test that `## Baseline` does not hold is fixed or reverted into a patch, as before.
> **－** Without `work.md` there is no baseline, and no red is excused as red before the work.
> **－** `estimate-guppi-tests-green` still wants `make test` with no failed test on the branch: a red test of the baseline stays red there.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `cause says why Retro was reached with a regression; the handoff still needs green.`
>   - new: `` cause says why Retro was reached with a regression; the handoff still needs green. A failing test or a lint finding line that `## Baseline` of `work.md` already holds was red before the work, whatever `## Expected red` names: it is an item of the frontier that ends as a note for the handoff, named as red before the work; it is not debt, nothing is fixed or reverted for it, and no lesson is written for it (case 479.4). ``
>   - old: `` commit (`make style` clean, `make test` green), then call `/handoff`. ``
>   - new: `` commit (`make style` clean, `make test` green but for the tests that `## Baseline` of `work.md` holds), then call `/handoff`. ``
>   - change: `a red that the Baseline of work.md holds is a note for the handoff under any Expected red, not debt, and the commit does not wait for it (case 479.4)`
> - [ ] create `estimate-retro-red-in-the-baseline-is-not-charged`
>   - type: `estimate`
>   - ref: `rule-retro`
>   - kind: `QA`
>   - purpose: `Whether Retro ends a failing test or a lint finding that the Baseline of work.md already holds as a note for the handoff, not debt, whatever Expected red names, and commits with make test green but for those tests`
>   - method: `one reading by hand at the first /retro after the render in a session whose work.md Baseline holds a failing test or a lint finding line, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-red-in-the-baseline-is-not-charged` — by hand, at the first such `/retro` after the render

> **ratification:**
> ```
> - decision[case 479.4][update][rule-retro]{ref:rule-retro}
> - decision[case 479.4][create][estimate-retro-red-in-the-baseline-is-not-charged]{ref:rule-retro}{tags:session,workflow,harness}
> ```

### Case 479.5 — work.md joins the working files the session writes without asking

> **given:**
> `rule-permissions` — its Purpose and its Render, the allow list
> **＋** `.claude/settings.json` — rendered in part from `rule-permissions`
> **＋** `tests/test_render.py` — the JSON case, which fixes the shape of the block
> **＋** `raw/<date>/<hi HHMM>/work.md` — the new working file of the session
> **＋** `frontier.md`, `spec.md`, `handoff.md` and `carry.md` under `vault/raw/**`, and `vault/wiki/brief.md` — the working files already allowed
> **＋** `estimate-permissions` — its Criterion replaced whole

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, and Edit and Write for `vault/wiki/brief.md`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit outside the plan file, allow list or not.
> **＋** A prompt in Plan Mode, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed.

> **tasks:**
> - [ ] update `rule-permissions`
>   - old: `` The Frontier, the Spec, the handoff, the carry mark and the brief of `/carry` are the session's own record of itself: `/hi` writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the Spec, ``
>   - new: `` The Frontier, the Spec, the work file, the handoff, the carry mark and the brief of `/carry` are the session's own record of itself: `/hi` writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the Spec and writes `work.md` (case 479.5), ``
>   - old: `"Write(vault/raw/**/handoff.md)",`
>   - new:
>     ```
>     "Write(vault/raw/**/handoff.md)",
>           "Edit(vault/raw/**/work.md)",
>           "Write(vault/raw/**/work.md)",
>     ```
>   - change: `work.md, the baseline and the marks of an expected red, joins the allow list (case 479.5)`
> - [ ] update `estimate-permissions`
>   - set: `{status: pending, method: "the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of work.md in Work Mode, recorded in the estimate line — never the agent's, which cannot see the prompt"}`
>   - change: `the Criterion replaced whole — Edit and Write for work.md join the allow list (case 479.5)`
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-permissions` — by hand, in a session after the render

> **ratification:**
> ```
> - decision[case 479.5][update][rule-permissions]{ref:rule-permissions}
> - decision[case 479.5][update][estimate-permissions]{ref:estimate-permissions}
> ```
