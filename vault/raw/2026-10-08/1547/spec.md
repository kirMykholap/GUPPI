<!-- approved 17:44:29 · session 8fb4a7ea -->

# Spec — session 1547, 2026-10-08

## Case 735 — The cart Estimate of the example names a make target

> **context:**
> Case 733 made `/pre-spec` judge the `method` of a MOC's Estimate by its form: only a `make <target>` or a reading `by hand` passes there, and a `tests/` path or `pytest` alone is a finding. Its code turned `make test` red at the Retro of session 0213, since the example Case of `rule-case-example`, rendered into `vault/wiki/case-example.md`, creates `entity-cart` with `kind: MOC` and gives its Estimate `estimate-cart-renders-in-time` a `method` that names only a `pytest` command; `tests/test_case_schema.py` runs the check of the Case file over that example and fails on any finding. The code was saved to `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff` and reverted, and `estimate-prespec-catches-a-method-without-a-form` stands `failed`. The brief plans to change the example and apply the patch in one session, but that order fails again: `guppi/guard.py` refuses a hand edit of a file a Rule page governs, so the new example reaches `vault/wiki/case-example.md` only at the render of the librarian's run, and in Work Mode the patched check would run over the old example; the Retro skill says that a red test is never an expected red and is fixed or reverted. The person chose to change only the example in this session, and to apply the patch, format it with `make style` and read `estimate-prespec-catches-a-method-without-a-form` in a later session, after the render; this Case does none of those three, `rule-prespec` stays `draft` until that reading, and the handoff of this session carries the work. The new `method` is `make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time`: it names a `make` target, so the form a MOC's Estimate takes, and the check judges the form only, not whether a Makefile holds the target. The first pair matches the `method` sub-point of the `create` of `estimate-cart-renders-in-time` in Case 1.2 of the example; the other three match the `kind`, `purpose` and `method` of the entry of the same Estimate in the `then` block example below it, which the person chose to make equal to the item of the example Case. The Criterion of `estimate-case-example-passes-the-check` stands: it promises that the check gives the example no finding and no note as the check stands, and the same test shows that the new example passes the stricter check once the patch applies; it is the one Estimate of `rule-case-example`. A Grep of `cart-renders-in-time|test_cart_view|measure the render` over the repository, `vault/raw/` and `vault/archive/` left out, printed `vault/wiki/brief.md`, `vault/wiki/case-example.md`, `vault/wiki/rules/rule-case-example.md`, `vault/wiki/rules/rule-estimates-schema.md`, `vault/wiki/estimates/estimate-prespec-catches-a-method-without-a-form.md` and `vault/wiki/estimates/schema.yaml`. The hit in `estimate-prespec-catches-a-method-without-a-form` is its Result, which records the failed reading and stands. The hits in `rule-estimates-schema` and its render `schema.yaml` are the example page of a `Research` Estimate, whose target `entity-cart` it gives no `kind`; it is another example, outside the item the person chose, and it stands.

> **problem:**
> The example Case that `case-guppi` copies gives a MOC's Estimate a `method` that names only a `pytest` command, which the stricter check of Case 733 reports, so that check cannot land while the example stands.

> **recommend:**
> - **When is the patch applied?**
>   - Recommended: (a) the example now, the patch in the next session, after the librarian's run renders the example; the pre-spec Estimate stays `failed` until then.
>   - Answer: agreed, (a).
> - **What method does the cart Estimate of the example name?**
>   - Recommended: (a) a make target: `make test-cart`, which runs the `pytest` command; the cart stays a MOC.
>   - Answer: agreed, (a).
> - **Is the cart Estimate in the Spec-block example fixed too?**
>   - Recommended: (a) the same entry as the Case: its `kind`, `purpose` and `method` as in the example Case.
>   - Answer: agreed, (a).
> - **Which Estimate checks the change to the example?**
>   - Recommended: (a) the Criterion of `estimate-case-example-passes-the-check` stands.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-example`: its Render holds the example Case and the `then` block example.
> **＋** `vault/wiki/case-example.md`: the file rendered from `rule-case-example`, which `case-guppi` reads.
> **＋** `estimate-cart-renders-in-time`: the Estimate the example creates, whose `method` changes; no page of the vault.
> **＋** `entity-cart`: the MOC the example creates, the target of that Estimate; no page of the vault.
> **＋** `estimate-case-example-passes-the-check`: the test of the example against the check of the Case file; its Criterion stands.
> **＋** `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff`: the stricter check the new `method` must pass.

> **when:**
> `case-guppi` reads `vault/wiki/case-example.md`, rendered from `rule-case-example`, before it first writes the file of a Case.

> **then:**
> The example Case creates `estimate-cart-renders-in-time` on the MOC `entity-cart` with a `method` that names the `make` target `make test-cart`, which runs the `pytest` command.
> **＋** The `then` block example creates the same Estimate with the `kind`, `purpose` and `method` of the example Case.
> **－** The `pytest` command does not stand alone in the `method` of the cart Estimate in either example.

```then
update:
- slug: rule-case-example
  replace:
  - old: 'method: `uv run pytest tests/test_cart_view.py -k render_time`'
    new: 'method: `make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time`'
  - old: 'kind: Research'
    new: 'kind: QA'
  - old: 'purpose: Whether the cart renders within 200ms, and what dominates the time if not'
    new: 'purpose: Whether the cart shows its items within 200 ms'
  - old: 'method: measure the render at 10, 50 and 200 line items, against a seeded database'
    new: 'method: make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time'
  change: the cart Estimate of both examples names a make target, the form a MOC's Estimate takes (case 735)
```

```tasks
- [ ] update `rule-case-example`
- [ ] `uv run guppi render`: `vault/wiki/case-example.md`
```

## Case 736 — A changed check is tried on the vault texts its tests run

> **context:**
> Some tests run a live text of the vault through a check: `tests/test_case_schema.py` reads the example Case of `vault/wiki/case-example.md`, rendered from `rule-case-example`, and runs the check of the Case file over it. In session 0213 Case 733 made the pre-spec check stricter; the test reaches that check through `guppi/casecheck.py`, which imports `guppi/prespec.py`. Neither `case-guppi` nor Work Mode looked at that example: Work Mode ran only `tests/test_prespec.py` and `tests/test_lint.py`, the full suite ran first at Retro, the example failed there, and Retro reverted the code into a patch (`lesson-case-build-misses-the-example-a-changed-check-runs-over`). Case 735 of this session fixes that example; this Case adds the step that was missing, in two places, and the stop the second place needs.
>
> Case 736.1 adds a step to the frame reading of `case-guppi`: for a Case that changes the code of a check, it reads each live file of `vault/` or `.claude/` that a test runs through that check, directly or through a module that imports it. A Grep of `ROOT\s*/\s*"vault"|ROOT / "\.claude"` over `tests/` printed `tests/test_case_schema.py` and `tests/test_orchestration.py`. The step works by reading and can miss a path through modules, so Case 736.2 makes `/work` run `make test` in full after its last task, before the Work readings, and hold each failing test against the Baseline of `work.md`. A new failing test whose fix needs a choice no ratified Case makes is a stop, which Case 736.3 adds to `vault/wiki/where-to-stop.md` as a seventh condition, since its closing paragraph says today that a red test is no stop. Any other new failing test — one whose ratified fix lands only at the librarian's run, as the example of Case 735 does — goes on to `/retro`, which fixes it or reverts it as today; `rule-retro` stands, and the new condition names the run of `/work`, so it never holds at Retro.
>
> The new Estimate of 736.1 is created with a `ref`, so no vault query was run for it; a Glob of its slug printed nothing. The other Estimates of `rule-case-build` stand: `estimate-case-build-writes-the-case` promises that `case-guppi` reads the frame the `given` names, which the new step extends and does not make false, and `estimate-case-build-checks-the-finished-case`, `estimate-case-build-reads-by-need-and-in-parts` and the rest speak of other steps. `estimate-work-mode-takes-the-work-readings` stands: the full run comes before the readings it checks, and its stop clause points to `vault/wiki/where-to-stop.md`. The Criteria of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` and `estimate-where-to-stop-stops-only-on-its-conditions` are replaced whole; the `purpose` and `method` of the first are set anew. The `purpose` of the second stands, since it speaks of each condition of the file and of no other. Its `method` waited for a run up to the librarian's report, which comes after this session. The run of this session also loads the old `vault/wiki/where-to-stop.md`, since the new Render is written only at the librarian's render, so the seventh condition cannot come up in it. The new `method` reads the text instead: the rendered file, or at the Retro of the session that changes it the new Render in the Spec, with the lines of the `/work` and `/box` skills that load it, against each line of the Criterion. This is how `estimate-work-mode-takes-the-work-readings` and the Estimates of `rule-case-build` read theirs. Its last `－` line changes: where it said that a red test is no stop, it now says that any other red test is no stop, at `/retro` too. `insight-workflow-contract-change-leaves-its-derived-text-stale` goes to `actioned` with `addressed_by: decision-case-736.1`; an Insight leaves `backlog.md` when it is not `open` and has no `deferred_by` (`guppi/backlog.py`, `deferred`).
>
> A Grep of `red test` over `vault/wiki/` printed `glossary.md`, `where-to-stop.md`, `log.md`, `estimates/estimate-retro-runs-on-to-the-handoff.md`, `rules/rule-retro.md`, `rules/rule-where-to-stop.md`, `entities/entity-glossary.md`, `rules/rule-handoff.md`, `estimates/estimate-handoff-holds-each-fact-once.md`, `estimates/estimate-where-to-stop-stops-only-on-its-conditions.md`, `estimates/estimate-retro-red-check-of-an-updated-page-is-a-handoff-note.md` and `estimates/estimate-retro-red-in-the-baseline-is-not-charged.md`; over `.claude/` it printed `skills/retro/SKILL.md` and `skills/handoff/SKILL.md`. The hits outside the pages this Case changes set what Retro and the handoff do with a red test, which stays as it is, and `log.md` is not read. A Grep of `where-to-stop` over the repository, `vault/raw/` and `vault/archive/` left out, printed 27 files; `rules/rule-spec-box.md` names condition 6 by its number, which the new seventh condition leaves in place. The entry `Work Mode` of `glossary.md` names the baseline, the tasks and the Work readings and stands: it names no step between them as the only one.

> **problem:**
> No step finds a live text of the vault that a test runs through a check a Case changes, and Work Mode runs only the test files the Spec names, so such a text breaks first at Retro, where the work can only be reverted.

> **recommend:**
> - **Where should the missing step go?**
>   - Recommended: (c) both, as two sub-cases: `case-guppi` reads the live texts a test runs through a changed check, and Work Mode runs `make test` in full after the last code task.
>   - Answer: agreed, (c).
> - **Does this Case also close the Insight?**
>   - Recommended: (a) yes, set `insight-workflow-contract-change-leaves-its-derived-text-stale` `actioned` with `addressed_by` naming this Case.
>   - Answer: agreed, (a).
> - **Which Estimate checks the new step of `case-guppi`?**
>   - Recommended: (a) a new Estimate, `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`; the existing one stays `passed`.
>   - Answer: agreed, (a).
> - **Which Estimate checks the full test run in Work Mode?**
>   - Recommended: (a) replace the Criterion of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, with its `purpose` and `method` naming the full run.
>   - Answer: agreed, (a).
> - **How does the stop on a new red test fit `where-to-stop.md`?**
>   - Recommended: (a) a seventh condition for Work Mode only, as a third sub-case, with the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` replaced; Retro keeps its revert.
>   - Answer: agreed, (a).

### Case 736.1 — case-guppi reads the vault texts a test runs through a changed check

> **given:**
> `rule-case-build`: the rule whose Render sets how `case-guppi` reads the frame of a Case.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `tests/`: the tests that read a live file of `vault/` or `.claude/`.
> **＋** `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`: the new check of the step.
> **＋** `lesson-case-build-misses-the-example-a-changed-check-runs-over`: the lesson whose cause the step closes.
> **＋** `insight-workflow-contract-change-leaves-its-derived-text-stale`: the Insight that lesson reopened; set `actioned`.
> **＋** `rule-insights-schema`: the rule that sets `addressed_by` of an `actioned` Insight to the latest decision.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case that changes the code of a check.

> **then:**
> It searches `tests/` for the tests that read a live file of `vault/` or `.claude/`, not a copy under a temporary folder.
> **＋** For each such test whose code reaches the changed code, directly or through a module that imports it, it reads that file against the new check.
> **＋** Each text of that file that the new check would refuse enters the Case, or its `context` says why it stands.
> **－** `insight-workflow-contract-change-leaves-its-derived-text-stale` stands `actioned` with `addressed_by: decision-case-736.1` and leaves the backlog.

```then
create:
- slug: estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi, for a Case that changes the code of a check, reads each live file of vault/ or .claude/ that a test runs through that check, directly or through a module that imports it, and puts each text the new check would refuse into the Case or says in context why it stands
  method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; and, for each Case of that session that changes the code of a check, the tests of the full make test run of Work Mode that fail on a live file of vault/ or .claude/ the Case does not name, counted in the estimate line
  tags:
  - workflow
  - harness
  - tests
update:
- slug: rule-case-build
  replace:
  - old: the hooks registered on the same event in `.claude/settings.json` and the rule of each.
    new: the hooks registered on the same event in `.claude/settings.json` and the rule of each. When the Case changes the code of a check, Grep `tests/` for the tests that read a live file of `vault/` or `.claude/`, not a copy under a temporary folder; for each one whose code reaches the changed code, directly or through a module that imports it, read that file against the new check, and each text the new check would refuse enters the Case, or `context` says why it stands (case 736.1).
  change: case-guppi reads, for a Case that changes the code of a check, each live file of the vault that a test runs through that check (case 736.1)
- slug: insight-workflow-contract-change-leaves-its-derived-text-stale
  set:
    status: actioned
    addressed_by: decision-case-736.1
  change: 'actioned: case-guppi reads the live texts a test runs through a changed check, and /work runs make test in full after its last task (case 736)'
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] create `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`
- [ ] update `insight-workflow-contract-change-leaves-its-derived-text-stale`
- [ ] read `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`
```

### Case 736.2 — Work Mode runs the whole test suite after its last task

> **given:**
> `rule-work-mode`: the rule whose Render is the skill `/work`.
> **＋** `.claude/skills/work/SKILL.md`: the skill file rendered from `rule-work-mode`.
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: the check of the baseline and the run of the tasks; its Criterion is replaced whole.
> **＋** `vault/wiki/where-to-stop.md`: the stops of the run, which `/work` loads.
> **＋** `/box`: the skill that calls `/work` with the folder of a conserved Spec.
> **＋** `vault/raw/<date>/<HHMM>/`: the folder of a conserved Spec.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose tasks `/work` runs.
> **＋** `raw/<date>/<hi HHMM>/work.md`: the file whose `## Baseline` holds the tests that failed before the work.
> **＋** `/retro`: the skill that fixes or reverts a red test, rendered from `rule-retro`.
> **＋** `rule-retro`: what Retro does with a red test; it stands.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
> **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.

> **then:**
> When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `make test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
> **＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
> **－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
> **－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.

```then
update:
- slug: rule-work-mode
  replace:
  - old: It runs the tasks in the order of the Spec and ticks each box.
    new: It runs the tasks in the order of the Spec and ticks each box. After the last task it runs `make test` in full against the baseline, and a new failing test whose fix needs a choice that no ratified Case makes stops the run for the person (case 736.2).
  - old: 'When the last task is done, delete the `carry.md` of a folder from `/box`, then take the Work readings before `/retro`:'
    new: 'When the last task is done, run `make test` in full and hold each failing test against `## Baseline` of `work.md`. A failing test that the Baseline holds was red before the work and goes on. Fix a new one when the fix finishes ratified work; when its fix needs a choice that no ratified Case makes, stop as the seventh condition of `vault/wiki/where-to-stop.md` sets; any other new failing test goes on to `/retro`, which fixes it or reverts it (case 736.2). Then delete the `carry.md` of a folder from `/box`, and take the Work readings before `/retro`:'
  change: /work runs make test in full after its last task and holds each failing test against the baseline (case 736.2)
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    status: pending
    purpose: Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, and after the last task runs make test in full and holds each failing test against the baseline, fixing a new one within ratified work
    method: 'uv run guppi render --check; by hand, a /work the agent calls at the fork, a /work that /box calls and the /work of a session that closes a sprint: the branch, work.md, the ticks of the Spec, the guppi sprint-close line neither run nor ticked, the carry.md of the folder, each Expected red line, and the full make test run after the last task with what followed each failing test, read against the Criterion, and, where a substitution came back empty, the agent''s own run of its command, recorded in the estimate line'
  sections:
    Criterion: |-
      When:
      The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
      **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.

      Then:
      `uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
      **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
      **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
      **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
      **＋** When `work.md` already stands, its `## Baseline` stays as it is.
      **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
      **＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
      **＋** When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `make test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
      **＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
      **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
      **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.
      **－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
      **－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.
  change: the Criterion replaced whole — /work runs make test in full after its last task and holds each failing test against the baseline; purpose and method name it (case 736.2)
```

```tasks
- [ ] update `rule-work-mode`
- [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [ ] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
```

### Case 736.3 — A new red test that needs a new Case stops Work Mode

> **given:**
> `rule-where-to-stop`: the rule whose Render is the list of stops.
> **＋** `vault/wiki/where-to-stop.md`: the file rendered from `rule-where-to-stop`, loaded by `/work`, `/box` and `/hi`.
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions`: the check of the stops; its Criterion is replaced whole.
> **＋** `rule-work-mode`: the skill `/work`, whose full test run after its last task the new condition names.
> **＋** `rule-retro`: the skill `/retro`, which fixes or reverts a red test and does not stop for it; it stands.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose tasks `/work` runs.
> **＋** `raw/<date>/<hi HHMM>/work.md`: the file whose `## Baseline` holds the tests that failed before the work.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
> **＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

> **then:**
> When the full `make test` run of `/work` after its last task finds a failing test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold, and its fix needs a choice that no ratified Case makes, the agent ends a reply with a question to the person that names the test and its failure.

```then
update:
- slug: rule-where-to-stop
  replace:
  - old: '6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; show what stopped it, and go on after the person''s word.'
    new: |-
      6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; show what stopped it, and go on after the person's word.
      7. The full `make test` run of `/work` after its last task finds a failing test that `## Baseline` of `work.md` does not hold, and its fix needs a choice that no ratified Case makes: name the test and its failure, and go on as the person's word says (case 736.3).
  - old: 'Nothing else is a stop: a red test, a reading'
    new: 'Nothing else is a stop: a red test other than that of the seventh condition, a reading'
  change: a new red test of the full run of /work whose fix needs a new Case is a stop (case 736.3)
- slug: estimate-where-to-stop-stops-only-on-its-conditions
  set:
    status: pending
    method: by hand, the text of vault/wiki/where-to-stop.md as rendered and the lines of .claude/skills/work/SKILL.md and .claude/skills/box/SKILL.md that load it, or, at the Retro of the session that changes it, the new Render of rule-where-to-stop in the Spec and those lines, read against each line of the Criterion, recorded in the estimate line; a line of the Criterion that the text does not set is named
  sections:
    Criterion: |-
      When:
      The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
      **＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

      Then:
      The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
      **＋** The context of `/box`, from `.claude/skills/box/SKILL.md`, holds the same text.
      **＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
      **＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
      **＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
      **＋** In a run of `/box`, the agent stops and asks when `uv run guppi box --check` prints a line, or when a `git merge --ff-only` of `/box` refuses.
      **＋** When the full `make test` run of `/work` after its last task finds a failing test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold, and its fix needs a choice that no ratified Case makes, the agent ends a reply with a question to the person that names the test and its failure.
      **＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
      **＋** After the person's answer the run goes on from where it stopped.
      **＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
      **－** No other point stops the run: any other red test, at `/retro` too, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.
  change: the Criterion replaced whole — a new red test of the full run of /work whose fix needs a new Case is a stop (case 736.3)
```

```tasks
- [ ] update `rule-where-to-stop`
- [ ] `uv run guppi render`: `vault/wiki/where-to-stop.md`
- [ ] update `estimate-where-to-stop-stops-only-on-its-conditions`
- [ ] read `estimate-where-to-stop-stops-only-on-its-conditions`
```

## Case 737 — The tags case-build and prespec are declared

> **context:**
> A tag is a short topic label on a vault page, and `vault/wiki/tags.md` lists the tags a page may carry. The ledger hook of `rule-ledger-write` refuses a fresh lesson line whose tag is not in that list, unless a ratified Case of the session declares it. At the Retro of session 0213 the agent wanted to tag the lesson `lesson-case-build-misses-the-example-a-changed-check-runs-over` with `case-build` and `prespec`. The hook refused both, and the lesson went in with `workflow, tests` (handoff of session 0213, For the next session). The list holds broad topics and has no tag for how `case-guppi` builds a Case or for the `/pre-spec` check of the ratified Cases. A Grep of `^tags:.*\bworkflow\b` over `vault/wiki/` printed 306 files, so `workflow` does not tell those topics apart.
>
> This Case declares the two tags by tag lines so that later lessons and pages can use them, and adds them to that lesson by an `update` of its `tags`. That lesson does not stay live. It is a `clustered` child of `insight-workflow-contract-change-leaves-its-derived-text-stale`, which Case 736.1 of this session sets `actioned`. The status field of `rule-lessons-schema` archives a Lesson when its Insight is `actioned`, and the cascade of `guppi/generate.py` sets each `clustered` child of an `actioned` Insight `archived` in the same librarian run. `rule-cleanup` then moves the page out of the live pages. The lesson therefore keeps the new tags under `vault/archive/`. The point of this Case is the declaration of the tags. The librarian's `guppi generate` writes a declared tag into `tags.md` by `register_tags` of `guppi/generate.py`. From the ratification on, the ledger hook and the check of a Case file take the two tags as listed in this session too (`ratified_tags` of `guppi/tags.py`). The person chose to tag only that lesson, so the other pages whose slugs name the two topics keep their tags. That includes the Estimate that Case 736.1 of this session creates on `rule-case-build` with `workflow, harness, tests`. A later Case or lesson may use the new tags.
>
> No new Estimate is made. `estimate-generate-writes` already checks the change, since its Criterion says that a tag of `new_tags` lands in `tags.md` and that an `update` applies `set` to the frontmatter. Its Criterion stands because this Case uses that behaviour and does not change it. `estimate-spec-write-reads-a-new-tag` stands for the same reason: it checks that the Spec hook turns a tag line of a Case file into an entry of `new_tags`, which is how the tags of this Case reach the Spec. `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` and `estimate-case-check-sends-back-an-unlisted-tag` stand too: they speak of the refusal of an unlisted tag, which stays as it is. No sentence of a live page becomes false. `tags.md` names no count of its rows, and the lesson page states its tags only in its `tags` field.

> **problem:**
> The tags the agent needs to mark lessons on how `case-guppi` builds a Case and on the `/pre-spec` check do not exist, so the ledger hook refuses them and the lesson that asked for them carries only broad tags.

> **recommend:**
> - **Should the two tags be added, and on which pages?**
>   - Recommended: (a) add both, and tag only `lesson-case-build-misses-the-example-a-changed-check-runs-over`, the lesson that asked for them.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: after the pre-spec findings, keep the target as it is, name `estimate-spec-write-reads-a-new-tag`, and say in `context` and `then` that the cascade of Case 736.1 archives the lesson in the same run and that the point of the Case is the declaration of the tags for later lessons and pages; no tags on rule pages.
>   - Taken: `context` names that Estimate and the archiving, and the `then` line on the lesson says that the cascade archives it and `rule-cleanup` moves it.

> **given:**
> `vault/wiki/tags.md`: the list of tags a page may carry.
> **＋** `lesson-case-build-misses-the-example-a-changed-check-runs-over`: the lesson that asked for the two tags.
> **＋** `insight-workflow-contract-change-leaves-its-derived-text-stale`: the Insight of that lesson, which Case 736.1 sets `actioned`.
> **＋** `guppi/generate.py`: `register_tags` writes a declared tag into `tags.md` at the librarian's run, and its cascade archives the `clustered` lessons of an `actioned` Insight.
> **＋** `rule-cleanup`: moves an archived page out of the live pages.
> **＋** `guppi/ledger.py`: the ledger hook, which refuses a lesson line with a tag that is not listed.
> **＋** `rule-ledger-write`: the rule of that refusal; it stands.

> **when:**
> `guppi generate` of `guppi/generate.py` applies the `then` block of this Case at the librarian's run.
> **＋** Or the ledger hook of `guppi/ledger.py` judges a fresh lesson line whose `{tags:...}` names `case-build` or `prespec`.

> **then:**
> `vault/wiki/tags.md` holds a row for `case-build` and a row for `prespec`, each with its meaning and its Russian aliases.
> **＋** `lesson-case-build-misses-the-example-a-changed-check-runs-over` carries the tags `workflow`, `tests`, `case-build` and `prespec`; in the same run the cascade of `guppi/generate.py` sets it `archived`, since `insight-workflow-contract-change-leaves-its-derived-text-stale` stands `actioned`, and `rule-cleanup` moves it out of the live pages.
> **＋** The ledger hook of `guppi/ledger.py` writes such a lesson line, in this session after the ratification of this Case and in each later session.
> **－** No other page changes its tags.

```then
new_tags:
- tag: case-build
  meaning: 'how case-guppi builds a Case: its rounds, its reading of the frame and the file it writes'
  aliases: сборка кейса, построение кейса
- tag: prespec
  meaning: 'the check of the ratified Cases before the Spec: /pre-spec, its hook and its findings'
  aliases: пре-спек, проверка плана
update:
- slug: lesson-case-build-misses-the-example-a-changed-check-runs-over
  set:
    tags:
    - workflow
    - tests
    - case-build
    - prespec
  change: tagged case-build and prespec, the tags the ledger hook refused at the Retro of session 0213 (case 737)
```

```tasks
- [ ] update `lesson-case-build-misses-the-example-a-changed-check-runs-over`
```
