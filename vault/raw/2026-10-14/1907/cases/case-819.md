## Case 819 — The code of GUPPI stands in .guppi/ and every caller runs it there

> **context:**
> Every hook of `.claude/settings.json`, every skill and agent that calls the code, the `Makefile` and the workflow `.github/workflows/prod.yml` run GUPPI's code through `uv run` at the root of the project. That works only where GUPPI's `pyproject.toml` stands at the root, so Case 818 copies `guppi/`, `pyproject.toml` and `uv.lock` to the root of a user's project as a stopgap until this item. A Python project that has its own `pyproject.toml` cannot take that copy. The person chose a folder of its own: the package `guppi`, its `pyproject.toml`, its `uv.lock` and its tests move into `.guppi/`, and every caller runs them as `uv run --project .guppi guppi …` and `uv run --project .guppi pytest`. This repository moves its own code there too, so the command has one form here and in a user's project. A Grep `__file__` over `guppi/` printed nothing, and `project_root` of `guppi/event.py` takes the project from `CLAUDE_PROJECT_DIR` or the working folder, so the code reads the project's vault from wherever it stands. For now the root keeps a small development project that takes the package from `.guppi/`, so that a session whose hooks still name the old command keeps working between the move and the render; the person chose to remove it later, by a Case of a later session (Case 819.1). A `.guppi/.gitignore` keeps the environment `.guppi/.venv/` out of git. The tests move into `.guppi/tests/`. This Case ships none of them, since `guppi ship` cleans the whole text of a Python file, strings included. A Grep `[Cc]ases? \d|decision-case-\d|[Ss]ession \d{4}` over `tests/` printed 1725 places in 35 files, mostly sample data. Case 821.2 of this session ships them with only their comments and docstrings cleaned, their other strings kept as samples. Case 821 also ships the passed Estimates, the session files as skeletons and `.github/workflows/checks.yml`. So the Criterion that Case 819.3 writes for `estimate-clean-branch-writes-a-clean-copy` points to the Estimates of Cases 821.1, 821.2, 821.3 and 821.5 for those files, and its line on the brackets it removes leaves out the strings of a test file. Case 821.2 anchors on the words of Case 819.3 on `rule-clean-branch`, ``but not its tests `.guppi/tests/` or its Python environment `.guppi/.venv/`;``, and replaces them, so Case 819.3 keeps those words as they stand. The check of this file applies the pairs of the other Cases first, so it finds the `reword` of Case 819.1 in the sentence that Case 821.2 adds to `rule-clean-branch` on a test file under `.guppi/tests/`. In the ledger the decision lines of Case 819 come before those of Case 821, so `guppi generate` applies this `reword` first and the sentence of Case 821.2 lands after it, untouched. Under the matching of Case 819.2, a path that a `.` or a `/` comes before is not touched anyway. Two lines of the old Criterion of `estimate-clean-branch-writes-a-clean-copy` are changed on purpose. The line on brackets now leaves out the strings of a test file. The line on what is not written now lets in the passed Estimates and points to Cases 821.3 and 821.5 for `.github/` and the session files. Both changes follow what Case 821 ships. The person chose that every text names the new command, the pages and their Criteria included. A Grep `uv run guppi` over `vault/wiki/`, `log.md` and `brief.md` left out, printed 352 places in 204 files. One `reword` changes them as a phrase, on the new page `rule-guppi-package`, whose Purpose holds each `new`. A `reword` replaces text in place in `purpose`, `method` and every section but History and Result, the Criterion included, and sets no Estimate `pending`, so no reading is retired: each Estimate still promises the same thing under the new name of the command. Lessons, Insights and Decision pages keep the old words as records. The paths change too, from `guppi/` and `tests/` to `.guppi/guppi/` and `.guppi/tests/`, in the text and in the link fields `implementation_ref`, `governs` and `code_ref`, which `guppi lint` checks for existence. Today `reword_pattern` of `guppi/generate.py` matches only a whole word, so `tests/` never matches inside `tests/test_ship.py`, and `reword_text` changes only `purpose`, `method` and sections. Case 819.2 teaches it path prefixes. The same function serves the preview of `/pre-spec`, so both sides keep one judgment, and `rename` passes only slugs, which never end with `/`. The new code is live at the librarian's run of the session whose Work Mode builds it, which is the run that applies the pairs. The check of this file and `/pre-spec` in this session run the old matching. Under it, the pairs `guppi/` and `tests/` still hit, where a backtick or a space follows them, so no pair stands without a hit. No anchor of this Case depends on a path that only the new matching changes: the pairs of Case 819.3 anchor on `.guppi/guppi/`, which the old matching also writes in place of `` `guppi/` ``, and the new texts of Cases 819.2 to 819.4 are written in the new forms and come after the `reword` in the ledger. The check of this file previews the `reword` over Decision pages and lessons too, such as `decision-case-807` and `lesson-caseid-run-to-check-an-id-held-a-new-one`; `guppi generate` changes only rules, entities and Estimates, so those hits stand as records. A path prefix would also turn the examples of a user's own project into GUPPI's paths. A Grep `test_cart_view|test_new_client|test_pricing_sync` over the repository, `vault/raw/` and `vault/archive/` left out, printed `vault/wiki/case-example.md`, `vault/wiki/rules/rule-case-example.md`, `vault/wiki/rules/rule-estimates-schema.md`, `vault/wiki/rules/rule-rules-schema.md`, `vault/wiki/rules/schema.yaml` and `vault/wiki/estimates/schema.yaml`. So Case 819.1 rewrites those examples before the `reword` runs, into paths that no pair touches, and states the method forms of `rule-estimates-schema` for both kinds of test folder. The new rule carries `core: true`, since the layout holds in every project; its test ships with the other tests as Case 821.2 sets it. The words of the new texts avoid the old command and the old paths, since the `reword` would rewrite them. `lint.py` takes a test path by `TEST_PATH`, which would read `tests/test_ship.py` out of `.guppi/tests/test_ship.py` and look for it at the root; Case 819.1 makes it take both folders, and the texts of the code that `estimate-lint-checks-the-method` and `estimate-prespec-catches-a-method-without-a-form` quote follow the `reword` of their Criteria, so both stand. `interpreter` of `guppi/bashguard.py` skips each option after `uv run`, so under the new form it would read `.guppi` as the program and pass `uv run --project .guppi python` fed a heredoc; Case 819.1 makes it skip the value of `--project`, so `estimate-bash-guard` stands. A Grep `uv run guppi|uv run pytest|uv run ruff|uv run python` over the repository, `vault/` left out, printed 126 places in 35 files: `.claude/settings.json`, `.claude/agents/librarian-guppi.md`, eight skills, `Makefile`, `.github/workflows/prod.yml`, eight modules of `guppi/` and fifteen test files. `ledger.py`, `onward.py`, `ratified.py` and `casecheck.py` find their own refusals in the transcript by the text of their hook's command; they take both forms, the old one for a session that still runs the hooks it read at its start, and a test asserts that each new form stands in `.claude/settings.json`, as `rule-one-judgment-one-implementation` asks of two sides that cannot share code. The ticker of render lines, `command_line` of `guppi/render.py`, matches `guppi render` anywhere in the first code span and takes both forms as it stands; `OFF_FORM_LINE` of `guppi/prespec.py` would miss a line of the new form, so it takes both. A Grep `project_root\(\)|REPO\b|ROOT = |Path\(__file__\)` over `tests/` printed `test_generate.py`, `test_case_schema.py`, `test_orchestration.py`, `test_schemas.py`, `test_lint.py` and `test_materialize.py`, which read `case-schema.md`, `case-example.md`, `orchestration.md`, the `schema.yaml` files and the `Makefile` by a path counted from the test file; under `.guppi/tests/` each counts one step more. `test_lint.py` lists the steps of `make lint` as the fake `uv` records them, so they take `--project .guppi`. `test_case_schema.py` runs the check over the example Case, whose new method still names `make test-cart`, so `estimate-case-example-passes-the-check` stands. Whether Claude Code runs a hook in the project's folder after a Bash command changed folder was not read; the relative path `.guppi` rests on it, and the reading of Case 819.1 tests it. That `uv sync` installs the group dev, and that uv fetches Python 3.12 itself, were not read at a source; the readings of Cases 819.1 and 819.4 test them. Between the Work Mode that moves the code and the librarian's run, `.claude/settings.json` and the pages still hold the old command, so the new test is red; that red is a note for the handoff by `rule-retro`, and the root development project keeps each hook working. `estimate-clean-branch-writes-a-clean-copy` lists `pyproject.toml` and `uv.lock` among the files `guppi ship` writes, which becomes false, so Case 819.3 replaces its Criterion. `estimate-generate-rewords` says every pair is a whole word, which becomes false, so Case 819.2 replaces its Criterion rather than adding a second Estimate beside a false one. Case 816 changes `rule-clean-branch` in other sentences, and its pairs and those of Case 818.1 apply before this Case's `reword`; the pairs of Case 819.3 are written on the text that the `reword` leaves. Case 818.1 creates `rule-plugin-install`; Case 819.4 writes its Purpose and Render whole, keeping each sentence of Case 818 that still holds. Case 818.1 must change: its `then` and `given` name `guppi/` and `pyproject.toml` among the files the install copies, and after this Case the clean version holds `.guppi/` and no `pyproject.toml` at its root; the `reword` turns `guppi/` in its Criterion into `.guppi/guppi/` and leaves `pyproject.toml`, which a Case may not change inside a Criterion. Its lines should name `.guppi/` in place of `guppi/` and `pyproject.toml`, and the person agreed that Case 818 is built again. Its rebuild should leave the `uv` check and the `uv sync` step to Case 819.4, which writes the Purpose and the Render of `rule-plugin-install` whole after the `create` of Case 818. The check of those two steps stands on `rule-guppi-package`, as `estimate-guppi-package-is-ready-after-the-install`, since the check of this file finds no live page `rule-plugin-install` to put it on. Case 817 changes no text this Case touches. `estimate-clean-branch-code-holds-pointers-only-in-brackets` stands, since this repository keeps a root `pyproject.toml`. `estimate-hook-registry-rendered` stands, since it promises only that the file equals the Render. Case 820 of this session drops `make`: `guppi check`, `guppi test` and `guppi style` run the checks, a thin `Makefile` stays in this repository for now, the clean version writes no `Makefile` and no `.guppi/guppi/ship.py`, and the judgment of a pointer moves into `.guppi/guppi/pointers.py`. So Case 819.3 lists no `Makefile` among the files `guppi ship` writes, and for the module of `ship` it points to `estimate-clean-branch-ships-no-ship-command` of Case 820.5, which makes that promise. This Case changes only the commands inside the `Makefile`. The `reword` of Case 820.7 replaces `make lint`, `make test` and `make style`, and the pairs of this Case replace `uv run guppi`, `uv run pytest`, `guppi/` and `tests/`. No `old` of one set stands inside an `old` or a `new` of the other, and the pairs of this Case come first in the ledger, so where both hit one sentence each changes its own words. The check of this file names such sentences in `estimate-backlog-checks-the-file`, `estimate-carry-over-writes`, `estimate-clean-branch-code-holds-pointers-only-in-brackets`, `estimate-documentation-completes`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-guppi-tests-green`, `estimate-prespec-catches-a-method-without-a-form` and `decision-case-807`. Read side by side, each reads true with both changes: a target of make becomes a command of `guppi`, and a command or a path of the code takes `--project .guppi` or `.guppi/`. For example, the `When` of `estimate-guppi-tests-green` becomes `uv run --project .guppi guppi test` running `uv run --project .guppi pytest -q` over `.guppi/tests/`. In `estimate-prespec-catches-a-method-without-a-form`, Case 820.4 replaces the Criterion whole after both rewords. The Decision page `decision-case-807` is a record that `guppi generate` leaves alone. Case 820 changes other sentences of `rule-clean-branch`, `rule-estimates-schema`, `rule-lint` and `rule-guppi-config` than this Case does: on `rule-clean-branch` it adds a sentence after words this Case leaves alone; on `rule-estimates-schema` it changes the sentence on the form of a MOC, which this Case leaves alone; and it writes the Purpose of `rule-lint` and `rule-guppi-config` whole, in the new paths, after the `reword` of this Case.

> **problem:**
> GUPPI's code runs only where its `pyproject.toml` stands at the root of the project, so a user's project must take files at its root that it does not own, and a project with its own `pyproject.toml` cannot take GUPPI at all.

> **recommend:**
> - **Where the code that the hooks run lives**
>   - Recommended: (a) the project's own copy at its root, for this sprint.
>   - Answer: (d) a copy in its own folder `.guppi/`, called as `uv run --project .guppi guppi …`; this repository moves its own code there too.
> - **What the install does when `uv` is missing**
>   - Recommended: (a) the install checks for `uv` first.
>   - Answer: not answered; replaced by the question on what the install does about `uv` and the Python environment.
> - **What the install does about `uv` and the Python environment**
>   - Recommended: (a) check `uv`, then build the environment by `uv sync` after the copy.
>   - Answer: agreed, (a).
> - **What stays at the root of this repository**
>   - Recommended: (a) a development project stays at the root.
>   - Answer: (a) as a step in between, then (b), nothing at the root.
> - **Which texts change to the new command**
>   - Recommended: (a) the texts that run.
>   - Answer: (b) every text; the Estimates that go back to pending are read later by one Case of their own.
> - **Where GUPPI's own tests live**
>   - Recommended: (a) they stay at the root and do not ship.
>   - Answer: not answered; the person asked why not (b) and why one script cannot rewrite the paths; replaced by the question on where the tests live and whether they ship.
> - **Where GUPPI's own tests live, and whether they ship**
>   - Recommended: (b) move them into `.guppi/tests/` now, and leave how they ship to item C9.
>   - Answer: agreed, (b).
> - **Git and the Python environment of `.guppi/`**
>   - Recommended: (a) a `.gitignore` of its own inside `.guppi/`.
>   - Answer: agreed, (a).
> - **What checks that this is done**
>   - Recommended: (a) a new Estimate for each half, plus the sprint Estimate.
>   - Answer: agreed, (a).
> - **When the root development project goes**
>   - Recommended: (a) a Case of a later session removes it.
>   - Answer: agreed, (a).
> - **How the pages take the new command**
>   - Recommended: (a) one `reword` of the command.
>   - Answer: agreed, (a).
> - **Which page holds where GUPPI's code lives**
>   - Recommended: (a) a new rule, `rule-guppi-package`.
>   - Answer: agreed, (a).
> - **How the paths of the code and the tests change in the pages**
>   - Recommended: (a) `reword` learns path prefixes.
>   - Answer: agreed, (a).
> - **Which page carries the check of the `uv` step of the install**
>   - Recommended: (a) the check stands on `rule-guppi-package`.
>   - Answer: agreed, (a); Case 818 is built again too.
> - **Change**
>   - Asked: the person agreed to build this Case again after Case 820, which drops `make` and ships no command `ship`.
>   - Taken: Case 819.3 no longer lists the `Makefile` among the files that `guppi ship` writes, in its new text of `rule-clean-branch`, its `then` and its task on `ROOT_FILES`; its `then` points to `estimate-clean-branch-ships-no-ship-command` for the module of `ship`; the Purpose of `rule-guppi-package` names the `Makefile` as the one this repository keeps for now.
> - **Change**
>   - Asked: the person agreed to build this Case again after Case 821, which ships the tests, the passed Estimates, the session files and `.github/workflows/checks.yml`, and builds no `prod` while a page with `core: true` is `draft`.
>   - Taken: the Criterion of Case 819.3 drops its lines on the tests, `.github/` and the session files and points to the Estimates of Cases 821.1, 821.2, 821.3 and 821.5; its line on brackets leaves out the strings of a test file; its task on `guppi/ship.py` leaves the tests to Case 821.2; the method of `estimate-guppi-package-is-ready-after-the-install` waits for the first run that writes `prod`; the test of Case 819.1 builds with `--allow-draft`.

### Case 819.1 — The code stands in .guppi/ and every caller runs it there

> **given:**
> `rule-guppi-package`: the new rule of where the code of GUPPI stands and how it is called.
> **＋** `estimate-guppi-package-runs-from-its-own-folder`: the new check of that rule.
> **＋** `guppi/`, `tests/`, `pyproject.toml`, `uv.lock`, `.guppi/`, `.guppi/pyproject.toml`, `.guppi/uv.lock`, `.guppi/.gitignore`, `.guppi/tests/`, `.guppi/tests/test_guppi_package.py` and `.venv/`: the code, its tests, its settings and its Python environment, before and after the move.
> **＋** `rule-hook-registry`, `.claude/settings.json`, the skills and agents under `.claude/`, `Makefile` and `.github/workflows/prod.yml`: the callers of the code.
> **＋** `guppi/ledger.py`, `guppi/onward.py`, `guppi/ratified.py`, `guppi/casecheck.py`, `guppi/prespec.py`, `guppi/lint.py`, `guppi/bashguard.py` and `guppi/generate.py`: the modules that judge the command or a path, or carry the `reword`.
> **＋** `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema`: the examples of a project of the person's own, kept out of the `reword`.
> **＋** `rule-clean-branch` and `guppi/ship.py`: the rule and the code of the clean version.

> **when:**
> In this repository, after the move of the code and the render of the harness, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.
> **＋** `uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it.

> **then:**
> The package `guppi`, its `pyproject.toml`, its lock file `uv.lock`, its tests and a `.gitignore` that holds `.venv/` stand under `.guppi/`, and `.guppi/pyproject.toml` declares pytest and ruff for the tests.
> **＋** Each hook of `.claude/settings.json`, and each command of a skill, an agent, the `Makefile` and `.github/workflows/prod.yml` that runs the code of GUPPI or its tests, runs it through `uv run --project .guppi`, and no hook prints an error.
> **＋** No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` without `--project .guppi` outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
> **＋** `.guppi/tests/test_guppi_package.py` fails on such a command in a file of `.claude/`, the `Makefile`, `.github/workflows/` or a live rule, entity or Estimate, and on such a path in such a page, found by the matching of `reword` of `guppi generate`.
> **＋** Each module that finds its own refusals in the transcript by the command of its hook finds them under the command with `--project .guppi` and under the command without it.
> **＋** The Bash and PowerShell guards judge `uv run --project .guppi python` as they judge `uv run python`, and `guppi lint` takes a test path under `.guppi/tests/` in a `method` as it takes one in the folder of tests of the project's own code.
> **＋** The clean version holds no `pyproject.toml` and no `uv.lock` at its root.
> **－** This repository keeps at its root, until a Case of a later session removes them, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so a command without `--project .guppi` still runs at its root and no hook of a running session fails.
> **－** The Decision pages, the lessons and the Insights keep the old command and the old paths, since they are records.
> **－** The examples of a project of the person's own in `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` keep a path of tests of that project, with no `.guppi/`.

> **tasks:**
> - [ ] create `rule-guppi-package`
>   - type: `rule`
>   - ref: `rule-harness`
>   - kind: `Leaf`
>   - purpose: `Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in this repository`
>   - enforcement: `check`
>   - implementation_ref: `[.guppi/pyproject.toml, .guppi/tests/test_guppi_package.py]`
>   - core: `true`
>   - tags: `[harness, plugin]`
>   - sections.Purpose:
>     ```
>     Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in this repository. The code of GUPPI, the package `guppi`, stands in `.guppi/guppi/`, with its `.guppi/pyproject.toml`, its lock file `.guppi/uv.lock`, its tests in `.guppi/tests/` and a `.guppi/.gitignore` that keeps its Python environment `.guppi/.venv/` out of git. Each caller runs the code as `uv run --project .guppi guppi …` — the hooks of `.claude/settings.json`, the skills, the agents and the `Makefile` that this repository keeps for now — and the tests as `uv run --project .guppi pytest`. `.guppi/pyproject.toml` declares the version of Python, the one runtime dependency PyYAML, and pytest and ruff for the tests. The code finds the project by the folder that Claude Code was opened in, so it reads the vault of the project from there. The test `.guppi/tests/test_guppi_package.py` fails on a command that runs the code or the tests through `uv run` without `--project .guppi`, in a file of `.claude/`, the `Makefile`, `.github/workflows/` or a live rule, entity or Estimate, and on a path of the code or the tests outside `.guppi/` in such a page, found by the matching of `reword` of `guppi generate`. This repository keeps at its root, for now, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so that a session whose hooks still name the command without `--project .guppi` keeps working; `guppi ship` does not write them, and a later Case removes them (as set in case 819).
>     ```
> - [ ] create `estimate-guppi-package-runs-from-its-own-folder`
>   - ref: `rule-guppi-package`
>   - kind: `QA`
>   - purpose: `Whether the code, the settings, the lock and the tests of GUPPI stand under .guppi/, every hook, skill, agent, Makefile line and page runs them through uv run --project .guppi, the modules and the guards take that form, and the clean version holds no pyproject.toml at its root`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_guppi_package.py; by hand, after the librarian's run of the session whose Work Mode moves the code: a session opened in this repository, /hi typed there, and the output of its hooks read against the Criterion`
>   - tags: `[harness, plugin]`
> - [ ] update `rule-case-example`
>   - old: `` method: `make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time` ``
>   - new: `` method: `make test-cart, which runs pytest cart/tests/test_view.py -k render_time` ``
>   - old: `method: make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time`
>   - new: `method: make test-cart, which runs pytest cart/tests/test_view.py -k render_time`
>   - change: `the example Estimate names a test path of the example project that the reword of rule-guppi-package does not touch`
> - [ ] update `rule-estimates-schema`
>   - old: `` a path under `tests/`; or the words `by hand` ``
>   - new: `` a path under `.guppi/tests/` or under the folder of tests of the project's own code; or the words `by hand` ``
>   - old: `method: pytest tests/discounts/test_new_client.py`
>   - new: `method: pytest discounts/tests/test_new_client.py`
>   - old: `` `pytest tests/discounts/test_new_client.py`: 3 passed. ``
>   - new: `` `pytest discounts/tests/test_new_client.py`: 3 passed. ``
>   - change: `a method names a test path under .guppi/tests/ or in the tests of the project's own code; the example names a path that the reword of rule-guppi-package does not touch`
> - [ ] update `rule-rules-schema`
>   - old: `implementation_ref: [ruff.toml, tests/lint/test_pricing_sync.py]`
>   - new: `implementation_ref: [ruff.toml, lint/tests/test_pricing_sync.py]`
>   - change: `the example names a test path that the reword of rule-guppi-package does not touch`
> - [ ] update `rule-guppi-package`
>   - reword old: `uv run guppi`
>   - reword new: `uv run --project .guppi guppi`
>   - reword old: `uv run pytest`
>   - reword new: `uv run --project .guppi pytest`
>   - reword old: `guppi/`
>   - reword new: `.guppi/guppi/`
>   - reword old: `tests/`
>   - reword new: `.guppi/tests/`
>   - change: `every live rule, entity and Estimate names the command, the code and the tests of GUPPI under .guppi/`
> - [ ] Move, in an order where a command without `--project .guppi` still answers at the root after each step: `guppi/` to `.guppi/guppi/`, `tests/` to `.guppi/tests/`, the package's `pyproject.toml` and `uv.lock` to `.guppi/`, with pytest and ruff and their settings in `.guppi/pyproject.toml`; a new `.guppi/.gitignore` that holds `.venv/`; the root `pyproject.toml` and `uv.lock` rewritten as a development project that takes `guppi` from `.guppi/` as an editable path and holds pytest and ruff with the settings of the tests.
> - [ ] `.guppi/tests/test_guppi_package.py`: the layout of `.guppi/`; no `uv run guppi` and no `uv run pytest` by `reword_pattern` of `guppi/generate.py` in the files of `.claude/`, the `Makefile` and `.github/workflows/`, and none of those and no path that the pairs `guppi/` and `tests/` would change in the parts of a live rule, entity or Estimate that `reword_text` changes; each `COMMAND` of `ledger.py`, `onward.py`, `ratified.py` and `casecheck.py`, in the new form, stands in `.claude/settings.json`; a clean version built into a temporary folder, with `--allow-draft` where it builds from this repository, holds no `pyproject.toml` and no `uv.lock` at its root.
> - [ ] `.guppi/tests/`: each path counted from the test file in `test_generate.py`, `test_case_schema.py`, `test_orchestration.py`, `test_schemas.py`, `test_lint.py` and `test_materialize.py` takes one step more; `LINT_STEPS` of `test_lint.py` take `--project .guppi`; each test that names the command or a path of the code or the tests names it as the code does.
> - [ ] `guppi/ledger.py`, `guppi/onward.py`, `guppi/ratified.py` and `guppi/casecheck.py`: each `COMMAND` holds the command with `--project .guppi`, and the search for the module's own refusals takes the command without it too, until a Case of a later session removes the old form.
> - [ ] `guppi/prespec.py`: `OFF_FORM_LINE` takes a render or sprint line of the form with `--project .guppi` as it takes one without it.
> - [ ] `guppi/lint.py`: `TEST_PATH` takes a test path under `.guppi/tests/` whole, and one at the root of the project as before.
> - [ ] `guppi/bashguard.py`: `interpreter` skips the value of `--project` after `uv run`, so `uv run --project .guppi python` fed a script on stdin is judged as `uv run python` is; a test in `test_bashguard.py` and one in `test_powershellguard.py`.
> - [ ] `guppi/`: each docstring, comment and message that names the command, the code or the tests of GUPPI names them as the pages name them after the `reword`.
> - [ ] `Makefile`: each `uv run` line takes `--project .guppi`.
> - [ ] `.github/workflows/prod.yml`: the build runs `uv run --project .guppi guppi ship "$RUNNER_TEMP/clean"`.
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/box/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-close/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/merge-main/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
> - [ ] `uv run guppi render`: `vault/wiki/where-to-stop.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-example.md`
> - [ ] `uv run guppi render`: `vault/wiki/ratification.md`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] read `estimate-guppi-package-runs-from-its-own-folder`

> **ratification:**
> ```
> - decision[case 819.1][create][rule-guppi-package]{ref:rule-harness}{tags:harness,plugin}
> - decision[case 819.1][create][estimate-guppi-package-runs-from-its-own-folder]{ref:rule-guppi-package}{tags:harness,plugin}
> - decision[case 819.1][update][rule-case-example]{ref:rule-case-example}
> - decision[case 819.1][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 819.1][update][rule-rules-schema]{ref:rule-rules-schema}
> - decision[case 819.1][update][rule-guppi-package]{ref:rule-guppi-package}
> ```

### Case 819.2 — A reword pair that ends with / changes the start of a path

> **given:**
> `rule-page-generation`: the rule of `guppi generate` and its `reword`.
> **＋** `estimate-generate-rewords`: its Criterion is replaced whole.
> **＋** `guppi/generate.py`: `reword_pattern`, `reword_text` and `reword_pairs`.
> **＋** `guppi/prespec.py`: the preview of the pairs, which imports `reword_pattern` and `reword_text`.
> **＋** `tests/test_generate.py`: the tests of `guppi generate`.
> **＋** `tests/`, `tests/test_ship.py`, `.guppi/tests/`, `.guppi/tests/test_ship.py` and `cart/tests/`: the paths of the example of a pair that ends with `/`.
> **＋** `vault/wiki/`, `vault/archive/` and `vault/raw/`: the live pages a `reword` changes, and the folders it leaves alone.

> **when:**
> `guppi generate` applies an `update` entry whose item carries `reword`, a list of `{old, new}` pairs.

> **then:**
> A pair whose `old` does not end with `/` is replaced as a whole word, with no letter, digit, `_` or `-` right before or after it.
> **＋** A pair whose `old` ends with `/`, such as `tests/`, is replaced as the start of a path: where no letter, digit, `_`, `-`, `.` or `/` stands right before it, whatever follows it, so the pair `tests/` → `.guppi/tests/` turns `tests/test_ship.py` into `.guppi/tests/test_ship.py` and leaves `.guppi/tests/` and `cart/tests/` as they are.
> **＋** The replace runs on every live page of the folders `rules`, `entities` and `estimates` of `vault/wiki/`, in every section but History and Result and in the fields `purpose` and `method`, and a pair whose `old` ends with `/` runs in the fields `implementation_ref`, `governs` and `code_ref` too.
> **＋** Each page touched gets one History line `reworded: old → new · [[decision-case-N]]`, and stdout has one line per page with the count.
> **＋** The other keys of the item — `set`, `replace`, `sections`, `change` — apply to the page itself as before; an item that carries `reword` alone is content and applies.
> **＋** `uv run --project .guppi guppi prespec --check` previews each pair by the same matching as `guppi generate`.
> **－** A pair with no hit on any live page fails the entry with the reason, and so does a pair whose `new` is absent from the text of the page of the item: its `purpose`, `governs`, `implementation_ref`, Purpose and Render, compared without regard to case. Nothing is applied.
> **－** The Decision pages, the lessons and the Insights, `vault/archive/`, `vault/raw/`, `log.md`, `brief.md` and `sprint.md` are not touched; the status of no Estimate changes.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `` a slug goes through `rename`, not `reword` (case 274.1). ``
>   - new: `` a slug goes through `rename`, not `reword` (case 274.1). A pair whose `old` ends with `/`, such as `tests/`, is the start of a path: it matches wherever no letter, digit, `_`, `-`, `.` or `/` stands right before it, whatever follows it, and it is replaced in the link fields `implementation_ref`, `governs` and `code_ref` too (as set in case 819). ``
>   - change: `a reword pair whose old ends with / matches the start of a path and changes the link fields too`
> - [ ] update `estimate-generate-rewords`
>   - set:
>     ```
>     status: pending
>     purpose: An update item with reword replaces its pairs as whole words, or a pair whose old ends with / as the start of a path in the link fields too, on every live page but History and Result, one History line each, and fails on a pair with no hit or a new the owner does not carry
>     method: "uv run --project .guppi pytest .guppi/tests/test_generate.py on a temp vault whose pages hold paths in their text and their link fields; by hand, after the librarian's run that applies the reword of rule-guppi-package: the pages it touched and its stdout read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — a pair whose old ends with / matches the start of a path, in the link fields too`
> - [ ] `guppi/generate.py`: `reword_pattern` matches an `old` that ends with `/` as the start of a path, and stays the one matching of `reword`, `rename` and the preview of `/pre-spec`; `reword_text` changes `implementation_ref`, `governs` and `code_ref` for such a pair; the docstring says so.
> - [ ] `tests/test_generate.py`: a pair `tests/` on a temp vault turns `tests/test_x.py` into `.guppi/tests/test_x.py` in a section, in `method` and in `implementation_ref`, and leaves `.guppi/tests/` and `cart/tests/` alone; a pair that does not end with `/` still matches a whole word only.
> - [ ] read `estimate-generate-rewords`

> **ratification:**
> ```
> - decision[case 819.2][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 819.2][update][estimate-generate-rewords]{ref:rule-page-generation}
> ```

### Case 819.3 — guppi ship writes the code under .guppi/

> **given:**
> `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: its Criterion is replaced whole.
> **＋** `vault/raw/2026-10-14/1907/cases/case-816.md` and `vault/raw/2026-10-14/1907/cases/case-818.md`: the Cases of this session that change other sentences of `rule-clean-branch`.
> **＋** `guppi/ship.py`: `ROOT_FILES`, `TREES`, `SKIPPED_NAMES` and `NOT_CLEANED`.
> **＋** `tests/test_ship.py`: the tests of `guppi ship`.
> **＋** `.guppi/`, `.guppi/tests/`, `.guppi/.venv/`, `.guppi/uv.lock`, `.claude/` and `.github/`: folders and files that the clean version holds or leaves out.
> **＋** `vault/wiki/`, `vault/wiki/tags.md`, `vault/wiki/case-example.md`, `vault/archive/` and `vault/raw/`: the pages and files of the vault that the clean version holds or leaves out.
> **＋** `rule-case-example` and `decision-case-N`: the page whose Render holds the example Case, and the form of the id of a Decision page.
> **＋** `estimate-clean-branch-ships-no-ship-command` and `vault/raw/2026-10-14/1907/cases/case-820.md`: the check that the clean version holds no module of the command `ship`, and the Case of this session that creates it and leaves the `Makefile` out of the clean version.
> **＋** `estimate-clean-branch-ships-the-tests`, `estimate-clean-branch-ships-the-passed-estimates`, `estimate-clean-branch-ships-the-checks-workflow`, `estimate-clean-branch-writes-the-session-files` and `vault/raw/2026-10-14/1907/cases/case-821.md`: the checks of what else the clean version holds, and the Case of this session that creates them.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run --project .guppi guppi ship --review <folder>` does the same.
> **＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.

> **then:**
> It writes `.guppi/` — its tests, its environment and the module of the command `ship` as `estimate-clean-branch-ships-the-tests` and `estimate-clean-branch-ships-no-ship-command` set them — then `.claude/`, `CLAUDE.md`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
> **＋** In each file it writes, it removes whole each bracket that holds a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — with every word in it and the space before it, and each `[[decision-case-N]]` link, but in a string of a test file, as `estimate-clean-branch-ships-the-tests` sets it; a bracket that holds no pointer stays as it is.
> **＋** It writes each other `[[…]]` link of a Markdown file to a page or a file it does not write as the slug in a code span.
> **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
> **＋** It exits 1, and prints the file and the line, for each pointer that stands outside such a bracket, each id of a list of sessions included.
> **＋** In a comment or a docstring of a Python file it writes, it exits 1, and prints the file and the line, for each bracket that holds only case numbers, joined by a comma, a semicolon, `and` or a dash, such as `(274.1)` or `(513, 544.7)`.
> **＋** It does the same for each comment or docstring that opens with one or more case numbers joined the same way, followed by a colon, such as `# 169.1:`, `"""75.2:` or `# 387.4, 445.4:`, and for each comment whose whole text is one or more case numbers joined the same way, such as `# 786` or `# 387.4, 445.4`.
> **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
> **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
> **＋** With `--check` it judges each file it would write outside `vault/` — the code under `.guppi/`, `.claude/` and the files at the root of the project — but `.guppi/uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
> **－** It writes no page without `core: true` but the Estimates that `estimate-clean-branch-ships-the-passed-estimates` sets, nothing of `vault/raw/` or `vault/archive/`, and no `guppi.toml`; what it writes of `.github/` and in place of the session files is what `estimate-clean-branch-ships-the-checks-workflow` and `estimate-clean-branch-writes-the-session-files` set.
> **－** It writes no cache folder of Python, pytest or ruff, and `--check` does not judge one.
> **－** It writes no file that a page without `core: true` renders in full.
> **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
> **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed; in `vault/wiki/case-example.md` and the Render of `rule-case-example` only the fenced blocks, the example Case among them, are set aside so, and the text around them is judged and cleaned like the text of any other page.
> **－** It removes no bare case number: the copy holds it as written.
> **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number or a list of numbers that opens a comment with words and no colon after it, such as `# 3, 4 tries`, is no finding.

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old: `` into an empty folder: `.guppi/guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, ``
>   - new: `` into an empty folder: `.guppi/`, which holds the package `guppi` with its `pyproject.toml`, `uv.lock` and `.gitignore`, but not its tests `.guppi/tests/` or its Python environment `.guppi/.venv/`; `.claude/`, `CLAUDE.md`, `.gitattributes`, ``
>   - old: `` but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project. ``
>   - new: `` but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project, and the `pyproject.toml` and `uv.lock` at the root of this repository, which [[rule-guppi-package]] keeps for the development of GUPPI. ``
>   - change: `guppi ship writes the code under .guppi/ without its tests and its environment, and no pyproject.toml or uv.lock at the root`
> - [ ] update `estimate-clean-branch-writes-a-clean-copy`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether guppi ship writes the code under .guppi/ without its cache folders, the harness and the pages with core: true, removes whole each bracket that holds a pointer, writes a link to a page it leaves out as its slug, writes the shipped values, exits 1 on a pointer outside such a bracket and on a bare case number in a comment or a docstring of a Python file, lists the brackets with words under --review, and judges in place under --check each file outside vault/ that it writes"
>     method: uv run --project .guppi pytest .guppi/tests/test_ship.py
>     ```
>   - change: `the Criterion replaced whole — the code ships under .guppi/, and the root pyproject.toml and uv.lock do not ship`
> - [ ] `guppi/ship.py`: `ROOT_FILES` holds `CLAUDE.md` and `.gitattributes`; the tree `.guppi` replaces `guppi` in `TREES`; `.guppi/.venv/` and the cache folders of Python, pytest and ruff are skipped by the copy and by `--check`, and the tests under `.guppi/tests/` go as Case 821.2 sets; `.guppi/uv.lock` is not cleaned; the docstring says so.
> - [ ] `tests/test_ship.py`: the sample tree holds `.guppi/guppi/`, `.guppi/pyproject.toml`, `.guppi/uv.lock`, `.guppi/.gitignore`, a file under `.guppi/.venv/`, a cache folder of pytest under `.guppi/`, and a root `pyproject.toml`; the file set of `test_it_writes_the_code_the_harness_and_the_core_pages_only` takes the first four and no file of `.guppi/.venv/`, of the cache folder or the root `pyproject.toml`; the tests under `.guppi/tests/` are judged as Case 821.2 sets.
> - [ ] read `estimate-clean-branch-writes-a-clean-copy`

> **ratification:**
> ```
> - decision[case 819.3][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 819.3][update][estimate-clean-branch-writes-a-clean-copy]{ref:rule-clean-branch}
> ```

### Case 819.4 — /guppi:install checks uv and builds the environment

> **given:**
> `rule-plugin-install`: the rule of the skill `/guppi:install`.
> **＋** `estimate-guppi-package-is-ready-after-the-install`: the new check of the two steps.
> **＋** `plugin/skills/install/SKILL.md`: the skill as the Render writes it.
> **＋** `vault/raw/2026-10-14/1907/cases/case-818.md`: the Case of this session that creates `rule-plugin-install`.
> **＋** `rule-guppi-package` and `.guppi/.venv/`: the rule of the folder of the code, and the Python environment that `uv sync` builds there.
> **＋** `/hi`: the skill that opens a working session in the project.

> **when:**
> The person installs the plugin `guppi` from the catalogue of the branch `prod` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> Before it writes anything, `/guppi:install` runs `uv --version`.
> **＋** After it copies the files, it runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/` before it tells the person to reopen Claude Code and type `/hi`.
> **＋** The hooks of the project find that environment built at the first `/hi`.
> **－** When `uv --version` fails, it says that GUPPI needs the tool `uv`, and that the person installs it and types `/guppi:install` again, writes nothing and stops.
> **－** When `uv sync --project .guppi` fails, it shows its output and stops, and does not tell the person to type `/hi`.

> **tasks:**
> - [ ] update `rule-plugin-install`
>   - sections.Purpose:
>     ```
>     Prevents a project that installs the plugin `guppi` from getting a part of GUPPI, or from losing a file of its own to it. The plugin, which the catalogue `guppi-marketplace` on the branch `prod` lists, is an installer. It carries one skill of its own, `install`, which the person types as `/guppi:install` in the project to install into. `guppi ship` copies the skill from `plugin/skills/install/SKILL.md`, which the Render of this page writes, to `skills/install/SKILL.md` of the clean version ([[rule-clean-branch]]). The skill first runs `uv --version`; when the tool `uv` is missing, it says that GUPPI needs it and writes nothing. It copies into the project each file of the plugin but its own files, those under `.claude-plugin/`, `skills/` and `.git/`. Those files are the code of GUPPI in `.guppi/`, the harness `.claude/` and `CLAUDE.md`, the files at the root and the pages with `core: true`, as `guppi ship` built them. It writes nothing when one of those files already stands in the project, and it runs no `guppi` and no `git` command. After the copy it runs `uv sync --project .guppi`, which builds the Python environment `.guppi/.venv/`, so that the first hook of the project does not wait for it ([[rule-guppi-package]], case 819). The project then runs on its own copy: its first `/hi` renders the harness from its own rule pages, and [[rule-morph]] sets its settings there. The skills of the project keep their bare names, such as `/hi`; only the skill of the plugin carries the prefix of the plugin (case 818). This page has no `core: true`, so a project that installs GUPPI does not hold it. Which files a new project gets waits for a Case of its own.
>     ```
>   - sections.Render:
>     ````
>     <!-- rule-plugin-install -->
>     ---
>     name: install
>     description: "Install GUPPI into the project open in this session: check uv, copy its files from this plugin and build its Python environment, then the person reopens Claude Code and types /hi. Run it when the person types /guppi:install."
>     disable-model-invocation: true
>     ---
>
>     Install GUPPI into the project of this session, the folder that Claude Code was opened in. The files come from this plugin, at `${CLAUDE_PLUGIN_ROOT}`. Write nothing into that folder of the plugin.
>
>     1. Run `uv --version`. When it fails, say that GUPPI needs the tool `uv`, which installs Python and runs the code of GUPPI, and that the person installs `uv` and types `/guppi:install` again, and stop. Write nothing.
>     2. List each file under `${CLAUDE_PLUGIN_ROOT}`, but the files under `.claude-plugin/`, `skills/` and `.git/`. These are the files to install, each at the same path in the project.
>     3. Check which of those paths already stand in the project. When one or more stand, list them, say that the install writes nothing into a project that already holds one of its files, and stop. Write nothing.
>     4. Otherwise copy each file to its path in the project, with the folders it needs. Change no other file. Run no `guppi` command and no `git` command.
>     5. Check that each file now stands in the project. When one is missing, name it and stop.
>     6. Run `uv sync --project .guppi` in the project, which builds the Python environment of GUPPI in `.guppi/.venv/`. When it fails, show its output and stop.
>     7. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`.
>     <!-- /rule-plugin-install -->
>     ````
>   - change: `/guppi:install checks uv before it writes and builds the Python environment by uv sync after the copy`
> - [ ] create `estimate-guppi-package-is-ready-after-the-install`
>   - ref: `rule-guppi-package`
>   - kind: `QA`
>   - purpose: `Whether /guppi:install stops and writes nothing when uv is missing, and builds the Python environment .guppi/.venv/ by uv sync after the copy, before it sends the person to /hi`
>   - method: `by hand, after the first run of .github/workflows/prod.yml that writes prod from a commit that holds this change: in an empty project on a machine whose search path holds no uv, /guppi:install typed and its output and the files of the project read; in an empty project on a machine with uv, /guppi:install typed, .guppi/.venv/ read and Claude Code reopened there, read against the Criterion`
>   - tags: `[plugin, harness]`
> - [ ] `uv run guppi render`: `plugin/skills/install/SKILL.md`
> - [ ] read `estimate-guppi-package-is-ready-after-the-install`

> **ratification:**
> ```
> - decision[case 819.4][update][rule-plugin-install]{ref:rule-plugin-install}
> - decision[case 819.4][create][estimate-guppi-package-is-ready-after-the-install]{ref:rule-guppi-package}{tags:plugin,harness}
> ```
