<!-- approved 13:06:19 · session 64d3e510 -->

# Session 2003 — Plan Mode of 2026-11-25

## Case 1058 — The plugin settings lesson names its source

> **context:**
> A `knowledge` lesson records outside material studied once, and the lesson schema of `rule-lessons-schema` makes `source` a required field for that kind. The librarian's run of session 0816 wrote `lesson-plugin-install-writes-a-project-settings-file` from line 32 of `raw/2026-11-25/0816/ledger.md`, which carried no `{source:...}`, so the page has no `source`. The brief reports the yaml entry `incomplete: [source]` and `guppi check` exit 1 with its one line, `schema: missing field source (given {'kind': 'knowledge'})`. The fact was seen in the test project p1-code of session 0816. Line 25 of the same ledger, the reading of `estimate-plugin-install-asks-one-approval-in-plan-mode`, names its transcript, `~/.claude/projects/C--tmp-guppi-1055-p1-code/66ad2c5f-8c5a-4bda-badd-8f13c00bfa47.jsonl`, and says the folder held a `.claude/settings.json` of enabledPlugins that `/plugin install` wrote. The Case sets that reference as the `source` of the page and keeps the kind. The ledger hook is not changed: `ratification.md` says a knowledge line with no source becomes `incomplete: [source]` and a lint finding, and the person chose to fix only this page. The page lists no Estimate, since a lesson has none. `estimate-lessons-schema-checked` already checks the change: its Criterion says a lesson page that meets the conditional that `knowledge` requires `source` has no `schema` finding, and its `method` takes the live reading of `guppi check`. Its Criterion stands, since the schema does not change. The `guppi check` of the librarian's run, reported in the brief, reads the page after the `update`. No `error` lesson stands in the ledger of session 2003, so no line carries `{addresses:...}`.

> **problem:**
> A `knowledge` lesson page has no `source`, so `guppi check` exits 1.

> **recommend:**
> - **How the page passes the check**
>   - Recommended: (a) add the source, the p1-code transcript of session 0816, and keep the kind.
>   - Answer: (a).
> - **Whether the ledger hook also refuses a knowledge lesson with no source**
>   - Recommended: (a) fix only this page.
>   - Answer: (a).

> **given:**
> `lesson-plugin-install-writes-a-project-settings-file`: the lesson page that gets its `source`.
> **＋** `rule-lessons-schema`: the schema that requires `source` on a `knowledge` lesson.
> **＋** `estimate-lessons-schema-checked`: the check of a lesson page against that schema.

> **when:**
> `uv run --project .guppi guppi check` reads `lesson-plugin-install-writes-a-project-settings-file`.

> **then:**
> The page carries `source`, the p1-code transcript of session 0816, and has no `schema` finding.
> **－** The `kind` of `lesson-plugin-install-writes-a-project-settings-file` stays `knowledge`.

```then
update:
- slug: lesson-plugin-install-writes-a-project-settings-file
  set:
    source: probe p1-code of session 0816, transcript ~/.claude/projects/C--tmp-guppi-1055-p1-code/66ad2c5f-8c5a-4bda-badd-8f13c00bfa47.jsonl (raw/2026-11-25/0816/ledger.md#L25)
  change: source set, which its knowledge kind requires
```

```tasks
- [ ] update `lesson-plugin-install-writes-a-project-settings-file`
```

## Case 1059 — The build line of the package holds the uv of today

> **context:**
> When `uv sync` builds the package `guppi` into its Python environment, at each install of GUPPI and in this repository, it uses the build tool that the line `requires = ["uv_build>=0.11,<0.12"]` of `.guppi/pyproject.toml` allows. The uv docs (https://docs.astral.sh/uv/concepts/build-backend/) say that uv carries a copy of that build tool and uses it only when its version is inside that range; otherwise a compatible `uv_build` package is used. The same page advises an upper bound so that the package keeps building as new versions ship, and shows `uv_build>=0.13.10,<0.14`; the versioning policy (https://docs.astral.sh/uv/reference/policies/versioning/) says the minor version is bumped for breaking changes. The brief, under `## Flags`, reports that at the install stop of session 0816 `uv sync` in each test project warned that the line does not hold uv 0.13.10, and that the build passed. The installer that `/guppi:install` offers in `plugin/skills/install/SKILL.md` installs the newest uv, so each new install meets the range from above. The person chose the range from 0.11 up to, but not including, 0.14: uv 0.11 to 0.13 each build with their own copy, and the warning comes back when uv 0.14 ships. The comment above the line says the build tool is fetched once; the task makes it say what the uv docs say. The rule that governs the file is `rule-guppi-package`, whose `implementation_ref` names `.guppi/pyproject.toml`; its Purpose says the file declares the version of Python, PyYAML, and pytest and ruff for the tests, and names no build tool, so no sentence of it turns false and the Case leaves the page as it stands. Of its Estimates, `estimate-guppi-package-is-ready-after-the-install` speaks of `uv sync` building `.guppi/.venv/`; its Criterion asks only that the environment is built and says nothing of a warning, so it held with the old line and holds with the new one, and it stands. The person chose a one-off check on the sprint page, `once: true`, read in Work Mode on the uv of this machine, so no test turns red when uv is updated; the choice of `entity-sprint-plugin` as its target follows from `once: true`, which the estimates schema ties to the live sprint page. The Purpose of that page names its main Estimates after its Done-when sentence and none of its other one-off Estimates, so it stands. The reading builds in a fresh copy of `.guppi/` rather than in `.guppi/.venv/`, since that is how the warning was seen and the uv docs read for this Case do not say whether `uv sync` rebuilds a package that is already installed. A Grep for `uv_build|uv-build|build-system|build_system` over `.guppi/`, `.venv/` left out, printed `.guppi/pyproject.toml` alone; so no code of the package reads the line. The tests that read `.guppi/pyproject.toml` live, `test_the_package_its_settings_its_lock_and_its_tests_stand_under_guppi` of `.guppi/tests/test_guppi_package.py` and `pytest_section` of `.guppi/tests/test_commands.py`, read its project, scripts, dev group, pytest and ruff keys and not the build line, so the change fails neither. `guppi test` exited 0 at the close of session 0816, as `## Readings at the close` of the brief reports. `estimate-clean-branch-code-holds-pointers-only-in-brackets` asks that a comment of `pyproject.toml` holds a pointer to a case only in a bracket of its own; the new comment holds no pointer, so it stands. `.guppi/guppi/ship.py` copies `.guppi/pyproject.toml` into the clean version and reads only its ruff settings there, so the new line ships as it stands. The other pages and files the check listed name `pyproject.toml` for where the settings stand, the test command or the root project of this repository, and none of them speaks of the build line. The ledger of this session holds no `error` lesson.

> **problem:**
> The build line of `.guppi/pyproject.toml` allows only the 0.11 build tool of uv, so every uv from 0.12 on warns at `uv sync` and builds with a downloaded 0.11 build tool instead of its own.

> **recommend:**
> - **Which bound `.guppi/pyproject.toml` sets for `uv_build`**
>   - Recommended: (a) widen the range to 0.11 up to, but not including, 0.14.
>   - Answer: agreed, (a).
> - **How the widened range is checked**
>   - Recommended: (b) a one-time reading on the sprint page, `once: true`, of the output of `uv sync` in Work Mode.
>   - Answer: agreed, (b).

> **given:**
> `.guppi/pyproject.toml`: the settings of the package, its build line among them.
> **＋** `estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine`: the new one-off check of the build line.
> **＋** `entity-sprint-plugin`: the sprint page that the check targets.
> **＋** `rule-guppi-package`: the rule of the package and its settings.
> **＋** `.guppi/.venv/`: the Python environment of the package, left out of the copy.

> **when:**
> The agent copies `.guppi/` without `.guppi/.venv/` into an empty folder and runs `uv sync --project` on that folder, with a `uv` whose version is 0.11 or later and before 0.14.

> **then:**
> `uv sync` builds the package `guppi` into the Python environment of that folder and exits 0.
> **＋** Its output holds no warning that the `build-system.requires` of `.guppi/pyproject.toml` does not hold the version of `uv`.
> **－** The range of `uv_build` in `.guppi/pyproject.toml` does not lose its upper bound.

```then
create:
- slug: estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether uv sync builds the package guppi from a fresh copy of .guppi/ with no warning that the build line of .guppi/pyproject.toml does not hold the version of uv, on a uv from 0.11 to before 0.14
  method: 'by hand, in Work Mode of the session that sets this Criterion, after the edit of .guppi/pyproject.toml: .guppi/ copied without .venv/ into an empty folder under the scratchpad of the session, and the output of uv --version and of uv sync --project on that folder, read against the Criterion, the outputs in the estimate line'
  tags:
  - sprint
  - plugin
  once: true
```

```tasks
- [x] `.guppi/pyproject.toml`: the build line reads `requires = ["uv_build>=0.11,<0.14"]`, and the comment above it says that uv builds with the copy of the build tool it carries when its version is inside the range, downloads one inside the range otherwise, and that the upper bound keeps out a later build tool with breaking changes.
- [ ] create `estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine`
- [ ] read `estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine`
```

## Case 1061 — Work Mode runs the style check before a stop task

> **context:**
> Work Mode stops before a task whose text opens with `stop:` and waits for the person's word. In session 0816 a task of Case 1055 wrote a copy of GUPPI by `guppi ship --allow-draft`, and the stop after it handed that copy to the person for install tests. `guppi ship` runs only `ruff format .guppi` over the copy, by `FORMAT` and the function `formatted` of `.guppi/guppi/ship.py`, which the build calls as its last step; it runs no `ruff check`. The key `style` of `guppi.toml` holds two commands, `ruff check .` and `ruff format --check .`. The module docstring of `ship.py` says the copy passes the commands of the key `style`. That holds only where the code of the working tree already passes `ruff check`, since the build fixes the format and nothing else. `estimate-clean-branch-copy-passes-its-style-and-tests` checks it that way: its test builds the copy from a clean working tree and runs the `style` commands over it. So the docstring and that Estimate stand, and the fix of this Case is the style check of Work Mode before the stop. Of the other files the check listed for `ship.py` and `guppi ship`, each speaks by its purpose line or path of other parts of the build, such as pointers, the license, the icon, the tests, the install or CI, and this Case does not change `ship.py`. Work Mode runs `guppi test` after its last task but no `guppi style` before a stop; so a ruff F811 finding of new code reached the test projects, and their Retro stopped on it, as `lesson-plugin-copy-shipped-before-the-style-check` records. The person chose that Work Mode runs `uv run --project .guppi guppi style` before every stop task. At `/pre-spec` the person chose that the agent fixes a finding only in a file the session changed and writes a finding in any other file as a line of `handoff.md`, so a red that the session did not make cannot hold the run in a loop before the stop. The reading of the new Estimate waits for the first `/work` that reaches a `stop:` task after the render, as the person chose, and the Estimate stays `pending` until then. The pairs on `rule-work-mode` change its Purpose and its Render; the render writes `.claude/skills/work/SKILL.md`. Of the Estimates of `rule-work-mode`, the purpose of `estimate-work-mode-takes-the-work-readings` speaks of readings and that of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` of the baseline, the order of the tasks and the full test run, not of a style check before a stop, so both stand, and a new Estimate checks the promise. `vault/wiki/where-to-stop.md` sets the stop before a `stop:` task and stays true: the style check comes before that stop, and `estimate-where-to-stop-stops-only-on-its-conditions`, whose Criterion says the agent stops before a `stop:` task, stands for the same reason. Case 1059 of this session changes `.guppi/pyproject.toml` and the sprint page and sets no step before a stop. Case 1060 was built again as Case 1063, whose finished file was read whole, as the main agent asked: it sets that a passed one-off Estimate is not read again and changes `rule-case-protocol`, `rule-case-build`, `rule-prespec`, `rule-estimates-schema`, `entity-sprint-plugin`, `rule-skill-merge-main` and two of their Estimates, and names `SKILL.md` files of `/pre-spec` and `/merge-main`, not of `/work`, so it sets nothing at a stop of Work Mode and stands beside this Case. The other files the check of this file listed were judged by their purpose lines and paths: they name `rule-work-mode`, `/work` or a `SKILL.md` for other things, such as the glossary, the sprint page, other skills and their Estimates, and none sets a step before a stop. A Grep of `.guppi/tests/` for `skills/work|rule-work-mode` printed only `test_glossary.py` and `test_sprint.py`, which write their own fixtures and read no live file. The second cause the lesson names, a second span pattern beside `lint.CODE_SPAN`, is a defect of code and not of the workflow; this Case does not cover it. The session ledger holds no `error` lesson, so no `{addresses:}` mark stands.

> **problem:**
> A copy or other work handed to the person at a stop can carry a style finding, since no style check runs before the stop.

> **recommend:**
> - **Where should the style check run before a copy reaches the person?**
>   - Recommended: (a) Work Mode runs the style check before every stop task.
>   - Answer: agreed, (a).
> - **What Work Mode does with a style finding in a file the session did not change**
>   - Recommended: (a) before a `stop:` task the agent fixes the findings in the files the session changed, writes a finding in any other file as a line of `handoff.md`, and stops as usual.
>   - Answer: agreed, (a).
> - **What the reading of the new Estimate takes**
>   - Recommended: (a) the `method` waits for the first `/work` with a `stop:` task that loads after the render and reads its transcript, as `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` does; it stays `pending` until then.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: `/pre-spec` found that the `context` says `guppi ship` runs no `ruff check`, while the docstring of `.guppi/guppi/ship.py` says the copy passes the commands of the key `style`.
>   - Taken: the code was read; `ship` runs only `ruff format .guppi`, and the docstring holds for a working tree whose code passes `ruff check`, so the `context` names the code and says why the docstring stands.

> **given:**
> `rule-work-mode`: the rule of Work Mode, which renders `.claude/skills/work/SKILL.md`.
> **＋** `estimate-work-mode-runs-the-style-check-before-a-stop`: the new check of the promise.
> **＋** `rule-where-to-stop`: sets the stop before a task that opens with `stop:`.
> **＋** `vault/wiki/where-to-stop.md`: the Render of `rule-where-to-stop`, read by `/work`.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the report of the session, which takes a finding in a file the session did not change.

> **when:**
> `/work` of `.claude/skills/work/SKILL.md`, rendered from `rule-work-mode`, reaches a task of the Spec whose text opens with `stop:`.

> **then:**
> Before it stops, the agent runs `uv run --project .guppi guppi style` and fixes each finding in a file that the session changed.
> **＋** The agent writes each finding in a file that the session did not change as a line of `raw/<date>/<hi HHMM>/handoff.md`.
> **＋** The agent then stops before that task as `vault/wiki/where-to-stop.md` sets it.
> **－** A task that does not open with `stop:` gets no style check from this step.

```then
create:
- slug: estimate-work-mode-runs-the-style-check-before-a-stop
  ref: rule-work-mode
  kind: QA
  purpose: Whether /work runs guppi style before it stops at a task that opens with stop:, fixes each finding in a file the session changed and writes each other finding into handoff.md
  method: 'by hand, after the first /work that loads after the librarian''s render of .claude/skills/work/SKILL.md from the Render of rule-work-mode and reaches a task that opens with stop:: its run of uv run --project .guppi guppi style before that stop, its fixes and its handoff.md read in the transcript of its session under ~/.claude/projects/ against the Criterion; recorded in the estimate line with the transcript named'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-work-mode
  replace:
  - old: It runs the tasks in the order of the Spec and ticks each box.
    new: It runs the tasks in the order of the Spec and ticks each box. Before a task that opens with stop:, it runs uv run --project .guppi guppi style, fixes each finding in a file the session changed and puts each finding in another file into handoff.md, so that no work of the session handed to the person at a stop carries a style finding (as set in case 1061).
  - old: Run the tasks of the Spec in the order the Spec holds them.
    new: Run the tasks of the Spec in the order the Spec holds them. Before a task whose text opens with stop:, run uv run --project .guppi guppi style; fix each finding in a file that the session changed and run it again, write each finding in a file that the session did not change as a line of handoff.md, and then stop as vault/wiki/where-to-stop.md sets it (as set in case 1061).
  change: Work Mode runs guppi style before a stop task, fixes the findings in the files the session changed and puts the others into handoff.md
```

```tasks
- [ ] update `rule-work-mode`
- [ ] create `estimate-work-mode-runs-the-style-check-before-a-stop`
- [ ] `uv run --project .guppi guppi render`: `.claude/skills/work/SKILL.md`
- [ ] read `estimate-work-mode-runs-the-style-check-before-a-stop`
```

## Case 1063 — A passed one-off Estimate is not read again

> **context:**
> A one-off Estimate carries `once: true` and targets the live sprint page. It checks one state of the data once, not a behaviour that lasts. Today `case-schema.md` makes no exception for it. A Case that changes a page must give an `update` to each Estimate whose Criterion speaks of the change. That `update` sets the Estimate `pending`, and it must be read again. `case-guppi.md` counts an Estimate that the Case does not name as a contradiction, and `/pre-spec` reports it as a finding (case 203.2). The merge Case of `/merge-main` sets each Estimate whose Criterion speaks of a joined text `pending` by a sub-case of its own. So a passed one-off Estimate, such as one that read the Purpose of `entity-sprint-plugin` once, would be read again each time a later Case changed that Purpose. Case 1057 put the question into the Backlog of `entity-sprint-plugin`. The person chose that a passed one-off Estimate is left alone. A one-off Estimate that is `pending` or `failed` is updated as before, since Case 1057 set that one is worked on until a reading passes. A Case that needs the same state checked again creates a new one-off Estimate. This Case builds Case 1060 again under a new number, since the findings of `/pre-spec` add two sub-cases and change what Case 1060 set, as the Splitting section of `case-schema.md` sets it; the file of Case 1060 keeps its ratified text, and the decision lines of Case 1063.1 retire it.
>
> Case 1063.1 adds one sentence to each of four rendered texts. In the Render of `rule-case-protocol`, the full rule goes after the sentence on the Estimates of a changed page. In the Render of `rule-case-build`, a sentence after its definition of a contradiction says that a passed one-off Estimate is none. In the Render of `rule-prespec`, the question on Estimates that a Case does not name sets that Estimate aside. In the description of the field `once` in the Render of `rule-estimates-schema`, a sentence says that such an Estimate is not read again. That last text speaks of one-off Estimates alone, so the `－` line on Estimates without `once` names the other three texts only (finding 2 of `/pre-spec`). Each new sentence keeps its pointer in a bracket at its end, since each of the four pages carries `core: true` (case 807.4). The Backlog line leaves `## Backlog` of `entity-sprint-plugin`. Nothing goes into `## Closed`, since the schema of entities keeps closed Slices there and no answered questions; that is a choice of form. The person chose a one-off reading of the four texts on the sprint page. The four files change only at the render of the librarian's run, as `orchestration.md` sets it, so the `method` waits for the librarian's run of this session. That is allowed for an Estimate of a sprint page (case 772.4).
>
> `/pre-spec` found two more texts that set the old rule (findings 1 and 3), and the person agreed to the fixes it proposed. `estimate-case-protocol-case-form` holds the sentence of `case-schema.md` that this Case qualifies, so Case 1063.2 replaces its Criterion whole, written under `sections`, with that line qualified and the other lines as they stand. Its `purpose` and `method` do not state the old line, so they stand. The Render of `rule-skill-merge-main` sets each Estimate of a joined text `pending` in other words, so Case 1063.3 qualifies that step. It also replaces the Criterion of `estimate-skill-merge-main-joins-a-conflicted-page`, the one Estimate of that rule, written under `sections`, with the same line qualified. That Estimate stays `pending`, and its `method` still waits for the first `/merge-main` that leaves a conflicted page. A Grep for `once: true|one-time Estimate|one-off Estimate` over `.claude/` found no file. So the step of `/merge-main` was missed by that search, since it does not use those words, and `/pre-spec` found it.
>
> Of the other Estimates, `estimate-case-protocol-loaded` promises only that `case-schema.md` equals its Render. `estimate-estimates-schema-checked` reads the lists of the schema, and the Case changes only the prose of the field `once`. `.guppi/tests/test_schemas.py` reads only the `properties` and `body` of the live `estimates/schema.yaml`, so it does not fail. `estimate-prespec-reconciles` names the question on Estimates that a Case does not name, and that question stays. The new one-off Estimate checks the exception, so the exception is not signed twice and that Criterion stands. Of `rule-case-build`, `estimate-case-build-reads-by-need-and-in-parts` and `estimate-case-build-writes-the-case` promise how `case-guppi` reads the `purpose` and the Criterion of the Estimates of a page. The Case does not change that reading, so their Criteria stand. `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` already says that it is not read again once a reading passes, so it agrees with the new rule. `estimate-sprint-plugin-done-counts-a-one-off-reading` is a `pending` one-off Estimate whose Criterion reads the Purpose of `entity-sprint-plugin`, and the Case changes only the Backlog of that page, so it stands. `entity-glossary` holds no term for a one-off Estimate or for the update of the Estimates of a changed page, so it stands. The other texts that the check of the file listed speak, by their purpose lines, of other things, such as the form of a round, the check of a Case file, the schemas of other categories and the steps of other skills. Of the texts listed for the merge step, `rule-documentation`, `rule-page-generation` and `rule-vault-layout` name `/merge-main` for the joined texts that a merge writes, not for the statuses it sets, and `estimate-clean-branch-refuses-a-draft-core-page` speaks of the build of the clean version, so they stand. The check notes that two lines of the replaced Criteria are not carried as they stood. Each of those is the one line that its sub-case qualifies, and the other lines are carried word for word. The `then` lines of the three sub-cases share words, but each one checks another text or agent: the four rendered texts, a Case that `case-guppi` builds, and a merge Case. So no promise is signed twice. The file of Case 1061, whose build has ended, was read whole: it changes `rule-work-mode` and sets a style check before a stop, so it sets nothing that this Case changes. Its `context` names this Case as built again as Case 1062, and that number no longer stands; Case 1061 needs that sentence to name Case 1063. The ledger of this session holds no `error` lesson.

> **problem:**
> A one-off Estimate checks one state once, but a later Case must set it `pending` and read it again whenever it changes what that Estimate checked. The person decided that a passed one-off Estimate is not read again.

> **recommend:**
> - **Is a passed one-off Estimate left alone by later Cases?**
>   - Recommended: (a) left alone once passed: no `update`, no `pending`, and no missed Estimate at `/pre-spec`; a `pending` or `failed` one is updated as before.
>   - Answer: (a).
> - **How the new rule is checked**
>   - Recommended: (b) a one-off reading of the four texts on the sprint page.
>   - Answer: agreed, (b); the reading waits for the librarian's run of this session, since the four files change at its render.
> - **Change**
>   - Asked: the findings of `/pre-spec`, which the person accepted. The step of `/merge-main` and `estimate-skill-merge-main-joins-a-conflicted-page` set every Estimate of a joined text `pending`. The `－` line asked `estimates/schema.yaml` for a sentence it does not hold. `estimate-case-protocol-case-form` holds the sentence that the Case qualifies.
>   - Taken: Case 1060 built again as Case 1063. Case 1063.1 holds its texts, with the `－` line narrowed to the other three texts. Case 1063.2 replaces the Criterion of `estimate-case-protocol-case-form`. Case 1063.3 qualifies the step of `/merge-main` and replaces the Criterion of its Estimate.

### Case 1063.1 — The texts say that a passed one-off Estimate is not read again

> **given:**
> `rule-case-protocol` and its Render `vault/wiki/case-schema.md`: the form of a Case.
> **＋** `rule-case-build` and its Render `.claude/agents/case-guppi.md`: the agent that builds a Case.
> **＋** `rule-prespec` and its Render `.claude/skills/pre-spec/SKILL.md`: the check of the plan before the Spec.
> **＋** `rule-estimates-schema` and its Render `vault/wiki/estimates/schema.yaml`: the form of an Estimate.
> **＋** `entity-sprint-plugin`: the sprint page, its Backlog and its one-off Estimates.
> **＋** `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again`: the new one-off check.

> **when:**
> The agent reads `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md` and `vault/wiki/estimates/schema.yaml` after the render of `rule-case-protocol`, `rule-case-build`, `rule-prespec` and `rule-estimates-schema`.

> **then:**
> `vault/wiki/case-schema.md` says that a later Case gives a passed Estimate with `once: true` no `update` and does not set it `pending`.
> **＋** `vault/wiki/case-schema.md` says that an Estimate with `once: true` that is `pending` or `failed` is updated as any other, and that a Case that needs the same state checked again creates a new one-off Estimate.
> **＋** `.claude/agents/case-guppi.md` says that a passed Estimate with `once: true` that the Case does not name is no contradiction.
> **＋** `.claude/skills/pre-spec/SKILL.md` says that a passed Estimate with `once: true` that the Case does not name is no finding.
> **＋** `vault/wiki/estimates/schema.yaml` says, in the description of the field `once`, that a passed one-off Estimate is not read again.
> **＋** The `## Backlog` of `entity-sprint-plugin` no longer asks whether a passed one-off Estimate is read again.
> **－** In `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md` and `.claude/skills/pre-spec/SKILL.md`, an Estimate without `once` whose Criterion speaks of what a Case changes still gets an `update` from that Case.

```then
create:
- slug: estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether the form of a Case, case-guppi, pre-spec and the schema of an Estimate say that a passed one-off Estimate gets no update from a later Case and is no missed Estimate, while a pending or failed one is updated as before; read once
  method: 'by hand, after the librarian''s run of session 2003: vault/wiki/case-schema.md, .claude/agents/case-guppi.md, .claude/skills/pre-spec/SKILL.md and vault/wiki/estimates/schema.yaml read against the Criterion, the sentences found in the estimate line'
  tags:
  - sprint
  - workflow
  once: true
update:
- slug: rule-case-protocol
  replace:
  - old: an Estimate whose Criterion speaks of something else is left alone, since naming a spare one replaces a sound Criterion (cases 53.2, 353 and 1011.3).
    new: 'an Estimate whose Criterion speaks of something else is left alone, since naming a spare one replaces a sound Criterion (cases 53.2, 353 and 1011.3). A one-off Estimate, one with `once: true`, that has passed is not read again: a later Case that changes what it checked gives it no `update` and does not set it `pending`, and `/pre-spec` does not report it as missed; one that is `pending` or `failed` is updated as any other, and a Case that needs the same state checked again creates a new one-off Estimate (as set in case 1063.1).'
  change: a passed one-off Estimate gets no update from a later Case and is not read again
- slug: rule-case-build
  replace:
  - old: and `/pre-spec` asks `ask-guppi` for one you missed (as set in case 1011.3).
    new: 'and `/pre-spec` asks `ask-guppi` for one you missed (as set in case 1011.3). A one-off Estimate, one with `once: true`, that has passed is no such Estimate: your Case gives it no `update`, while one that is `pending` or `failed` is one as any other (as set in case 1063.1).'
  change: a passed one-off Estimate that the Case does not name is no contradiction
- slug: rule-prespec
  replace:
  - old: one that does is a finding (case 203.2);
    new: 'one that does is a finding (case 203.2), but for a one-off Estimate, one with `once: true`, that has passed, which a Case gives no `update` (as set in case 1063.1);'
  change: a passed one-off Estimate that a Case does not name is no finding
- slug: rule-estimates-schema
  replace:
  - old: 'lint reports an Estimate with `once: true` whose `target` is not a sprint page (as set in case 969.1).'
    new: 'lint reports an Estimate with `once: true` whose `target` is not a sprint page (as set in case 969.1). Once it has passed it is not read again: a later Case that changes what it checked gives it no `update` and does not set it `pending`, and a Case that needs that state checked again creates a new one-off Estimate (as set in case 1063.1).'
  change: 'the field once: a passed one-off Estimate is not read again'
- slug: entity-sprint-plugin
  replace:
  - old: |-
      the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)
      - Whether a one-off Estimate that has passed once is never read again, so that a Case that changes its pages gives it no update and sets it `pending` no more, as `case-schema.md` would then set it; the person's view in session 0816 (case 1057)
    new: the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)
  change: 'the Backlog question whether a passed one-off Estimate is read again is decided: it is not'
```

```tasks
- [ ] update `rule-case-protocol`
- [ ] update `rule-case-build`
- [ ] update `rule-prespec`
- [ ] update `rule-estimates-schema`
- [ ] update `entity-sprint-plugin`
- [ ] create `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] `uv run --project .guppi guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/estimates/schema.yaml`
- [ ] read `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again`
```

### Case 1063.2 — A built Case gives a passed one-off Estimate no update

> **given:**
> `estimate-case-protocol-case-form`: the check of the form of a built Case, its Criterion replaced whole.
> **＋** `rule-case-protocol`: the form of a Case, whose Render `vault/wiki/case-schema.md` the Criterion reads.

> **when:**
> `case-guppi` writes a Case it built, which changes a page whose Criterion speaks of the change in an Estimate without `once` and in a passed Estimate with `once: true`.

> **then:**
> The Case gives an `update` to the Estimate without `once`.
> **－** The Case gives no `update` to the passed Estimate with `once: true`.

```then
update:
- slug: estimate-case-protocol-case-form
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      `case-guppi` writes a Case it built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the hook of `rule-case-check` checks it, and the main agent sends that file to the person, at its first showing or again.

      Then:
      The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
      **＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
      **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
      **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
      **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
      **＋** `tasks` holds no `by hand` box whose moment comes after Work Mode of the Case's own session — the librarian's run of that session or a later session; such a check stands as the reading of an Estimate or is left to the `uv run --project .guppi guppi check` of the librarian's run.
      **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change, but for a one-off Estimate, one with `once: true`, that has passed, which it gives none.
      **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification`, as `vault/wiki/orchestration.md` sets the showing, and the reply ends with a plain question.
      **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
      **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.
  change: the Criterion replaced whole — a built Case gives a passed one-off Estimate no update
```

```tasks
- [ ] update `estimate-case-protocol-case-form`
- [ ] read `estimate-case-protocol-case-form`
```

### Case 1063.3 — A merge Case sets no passed one-off Estimate pending

> **given:**
> `rule-skill-merge-main` and its Render `.claude/skills/merge-main/SKILL.md`: the merge of `main` into the branch of a sprint as one merge Case.
> **＋** `estimate-skill-merge-main-joins-a-conflicted-page`: the check of that merge, its Criterion replaced whole.

> **when:**
> The merge Case of `.claude/skills/merge-main/SKILL.md` holds a joined page whose text the Criterion of an Estimate without `once` and of a passed Estimate with `once: true` speaks of.

> **then:**
> A sub-case of its own sets the Estimate without `once` `pending`.
> **－** The merge Case gives no `update` to the passed Estimate with `once: true`.

```then
update:
- slug: rule-skill-merge-main
  replace:
  - old: 'each Estimate whose Criterion speaks of a joined text is set `pending` by a sub-case of its own:'
    new: 'each Estimate whose Criterion speaks of a joined text, but for a one-off Estimate, one with `once: true`, that has passed and is not read again (as set in case 1063.3), is set `pending` by a sub-case of its own:'
  change: a merge Case sets no passed one-off Estimate pending
- slug: estimate-skill-merge-main-joins-a-conflicted-page
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The person types `/merge-main` on `UserPromptSubmit` in Plan Mode, or the main agent calls it on `PreToolUse Skill`, in a session on the branch of an open sprint, `.claude/skills/merge-main/SKILL.md` rendered from `rule-skill-merge-main`; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

      Then:
      Writing nothing into the tree or into `.git` and running no `git fetch`, the main agent reads by `gh api` the commit of `main` on GitHub and the files that `main` changed since the last commit of `main` that the branch holds, and by `git` the files that the branch changed. It writes that output and the text on both sides of each file that both sides changed into `raw/<date>/<hi HHMM>/merge.md`, and dispatches `case-guppi` for the merge Case with that path.
      **＋** The merge Case is the one Case of the session; its tasks run `git fetch origin`, merge the commit of `main` that the session read into the branch, and commit the merge with a message that names the Case.
      **＋** Each conflicted file that a command writes takes the text of `main` and is written again by `uv run --project .guppi guppi render`, `uv run --project .guppi guppi glossary`, `uv run --project .guppi guppi sprint` or `uv run --project .guppi guppi backlog`, and `vault/wiki/brief.md` by the librarian; git keeps the lines of both sides of `vault/wiki/log.md` and `vault/wiki/tags.md` by their `merge=union` lines in `.gitattributes`.
      **＋** For each other file that both sides changed, the merge Case shows its text on the branch and on `main` and holds the joined text that the person signs or corrects; Work Mode writes that text into the file, and runs `git add` on each such path before the commit.
      **＋** Its decision lines update the live sprint page `entity-sprint-<id>` with only a `change` that names the merge, and each joined page under `vault/wiki/` with only a `change`; each Estimate whose Criterion speaks of a joined text, but for a one-off Estimate, one with `once: true`, that has passed, is set `pending` by a sub-case of its own, whose `when` and `then` are that Criterion; the librarian writes no other text of a joined page.
      **＋** `rule-page-generation`, `rule-vault-layout`, `rule-documentation`, `entity-glossary`, `.claude/agents/librarian-guppi.md` and `vault/wiki/glossary.md` name that joined text, and the lines of `log.md` and `tags.md` that git joins, as what a merge of `main` writes into `vault/wiki/` besides the script.
      **＋** `.claude/skills/merge-main/SKILL.md` says that the pull request into `main` follows `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, and that another person runs `git push` and `gh pr create --base main` after the close, for the owner to review by `/pr-review` of `.claude/skills/pr-review/SKILL.md`.
      **－** With no file that both sides changed, the update of the sprint page is the one decision line of the merge Case.
      **－** When the branch is `main`, when the first heading of `vault/wiki/sprint.md` marks the last sprint closed, or when the branch already holds `origin/main`, no Case is built and nothing is merged; the main agent tells the person why.
      **－** The merge Case archives nothing: what goes to the archive is what `/sprint-close` of `.claude/skills/sprint-close/SKILL.md` moves.
  change: the Criterion replaced whole — a merge Case sets no passed one-off Estimate pending
```

```tasks
- [ ] update `rule-skill-merge-main`
- [ ] update `estimate-skill-merge-main-joins-a-conflicted-page`
- [ ] `uv run --project .guppi guppi render`: `.claude/skills/merge-main/SKILL.md`
- [ ] read `estimate-skill-merge-main-joins-a-conflicted-page`
```
