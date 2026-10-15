## Case 820 — GUPPI runs its checks without make

> **context:**
> GUPPI runs its checks through `make`, a system program that reads the `Makefile`: `make test` runs GUPPI's own tests, `make style` runs the style checker ruff, and `make lint` runs six vault checks in a row. `make` is no Python package, so it cannot come in GUPPI's Python environment; Windows has none by default, and the `Makefile` also looks for the shell of Git for Windows. So a person who installs GUPPI cannot run the checks that Work Mode, Retro and the librarian run. The person chose to drop `make` everywhere. `guppi check` runs the vault checks (Case 820.1). `guppi test` and `guppi style` run the commands that two new keys of `guppi.toml` set, each a list of commands run with no shell, here `uv run --project .guppi pytest -q` and the two ruff commands; in a user's project the install Case of `rule-morph` will ask for them in a later session, and until then the command says that no command is set and exits 1, so a project with no command set never reads as tested (Case 820.2). `parse` of `guppi/config.py` checks only the two language keys, so the new keys do not stop the render. The person also chose that a project that installs GUPPI gets no command `ship`, which only builds the clean version of this repository. `guppi/prespec.py` imports its judgment of a pointer, `outside`, from `guppi/ship.py`, so that judgment and the functions it calls move into a module of their own, `guppi/pointers.py`, which both sides import, and `guppi check` skips `guppi ship --check` where the module is missing (Cases 820.5 and 820.6). A Grep `ship` over `guppi/`, `ship.py` left out, printed `guppi/cli.py`, `guppi/prespec.py` and `guppi/pages.py`; the hit in `pages.py` is a docstring, so no other module needs `ship.py`. A Grep `guppi\.ship|ship\.` over `tests/` printed `tests/test_ship.py` and `tests/test_prespec.py`; the second asserts that `prespec.outside` is `ship.outside`, and Case 820.6 makes it assert the same of `pointers.outside`. Each group rule page, a MOC, has an Estimate whose method names a make target of its pipeline, such as `make test-harness`. The person chose the form of a pytest command with the test files of the pipeline. Today `names_a_moc_form` of `guppi/lint.py` refuses that form on a MOC, and `prespec.judge`, which the check of this file runs, calls it; so this Case teaches `guppi lint` and `/pre-spec` the new form beside the make target (Cases 820.3 and 820.4), and a Case of a later session moves the group Estimates and the example of `rule-case-example` to it and removes the make form, the group targets and the `Makefile`. The person chose that the three new commands are forms of a method too: after the replace below, the method of `estimate-guppi-tests-green` names `guppi test` and no other form. A Grep `names_a_moc_form|names_a_form` over `guppi/` printed `guppi/lint.py` and `guppi/prespec.py`: the forms stay one predicate each in `lint.py`, which `prespec.py` imports, so the change adds no second copy, as `rule-one-judgment-one-implementation` asks. No code but the `Makefile` runs the steps of the vault checks, and `guppi/config.py` stays the one reader of `guppi.toml`. The `Makefile` stays for now, since the rendered `/work` and `/retro` load the old commands until the librarian's render, which runs after Retro. Its target `lint` calls `guppi check`, which is code and runs as soon as Work Mode writes it; its targets `test` and `style` keep their own commands, since `guppi test` reads a key that `guppi.toml` gets only at that render (Case 820.7). The person will conserve this Spec with `/carry`, so its Work Mode, Retro and render run in a later session. At the last close the brief reports `make test`: 1620 passed, 6 skipped, and `make lint`: 0 lines, exit 0. Every live rule, entity and Estimate takes the new commands by one `reword` per command, which sets no Estimate `pending`, as the `reword` of Case 819 does. `reword_pairs` of `guppi/generate.py` needs the `new` of a pair in the text of its owner and runs before the other keys of its own item, and `/pre-spec` refuses two items of one target in one Case or sub-case; so the `reword` stands in Case 820.7, on `rule-lint` and `rule-guppi-config`, whose new Purposes Cases 820.1 and 820.2 write first. No other new text of this Case holds an old command, since the `reword` would rewrite it. A Grep `make (test|lint|style)\b[^-]` over the repository, `vault/raw/` and `vault/archive/` left out, printed 215 places in 85 files. The pair is a whole word, so `make test-harness` and `make test-cart` stay. Each match on a live rule, entity or Estimate reads true with the new command but the Criterion of `estimate-harness-make-runs-in-both-shells`, which names the old commands as targets of the `Makefile`; the person chose to replace it in words the `reword` leaves alone (Case 820.7). The Criterion of `estimate-sprint-plugin-pull-requests-reviewed-on-github` says that CI runs the three old commands of the `Makefile`, which after the `reword` would name the new commands as targets of the `Makefile`; it stays `pending` and Case 820.8 replaces it with the same promise and the commands that CI runs, each other line word for word. `estimate-skill-sprint-close-migration-merged-into-main` passed on a run of the old test command, which ran the same pytest that `guppi test` runs here, so its Criterion reads true under the new name. The `reword` also previews over Decision pages, lessons and Insights, such as `decision-case-807` and `lesson-obsidian-cli-needs-the-running-app`; `guppi generate` changes only rules, entities and Estimates, so those stand as records. Where the `reword` of Case 819.1 and this one hit the same sentence of an Estimate, each changes its own words, a command of the code against a target of make, so the two compose. Case 819.1 changes the first sentence of the field `method` of the Render of `rule-estimates-schema`, the list of the four forms, so the pair of Case 820.3 leaves that sentence alone and adds the three commands in a sentence of their own before the sentence on the form of a MOC, which no other Case of the session changes. Before that pair, the field `method` goes on to say that a path must exist and a make target must stand in the `Makefile`, which still holds, since the three commands need no file of their own. In `entity-glossary`, the `reword` changes the row of Lint, which then says that `guppi check` runs `guppi lint` after the render, sprint, backlog and glossary checks, and the row of Work Mode, whose baseline then holds `guppi test` and `guppi check`; both read true. The pair of Case 820.5 on `rule-clean-branch` adds a sentence before the sentence on `guppi ship --check` that Case 818.1 changes, and neither touches the words of the other. Lessons, Insights, Decision pages, `log.md` and `brief.md` keep the old words as records. `rule-documentation` names the `Makefile` among the files of the scripts, which stays true while it stands. The Criteria of `estimate-lint-runs-every-step`, `estimate-lint-checks-the-method` and `estimate-prespec-catches-a-method-without-a-form` are replaced whole, with their `purpose` and `method` where these state the old promise. The Criterion of `estimate-prespec-hook-reports-a-pointer-outside-a-bracket` says that the judgment is imported from `guppi/ship.py`, so Case 820.6 replaces it. Each line of the four replaced Criteria that the check of this file notes as not carried stands in the new Criterion with the new command, the new paths or the new forms. Case 820.7 adds no Estimate for the `reword` and for `.github/workflows/checks.yml`: the lines on the texts and the CI jobs in the Criteria of Cases 820.1 and 820.2 check them. `estimate-harness-pipeline` and `estimate-guppi-tests-green` stand, since after the `reword` they promise the same under the new command. `estimate-guppi-config-fills-the-languages` stands, since its Criterion speaks of the render of the languages, which the new keys do not change. `estimate-clean-branch-code-holds-pointers-only-in-brackets` stands: it names the `Makefile` among the files on which `guppi ship --check` prints no line, which holds when the clean version no longer holds that file. CI runs the new commands; a push between the Work Mode and the librarian's run would see the job `test` red, since `guppi.toml` gets its keys at that run. A Grep `__file__|project_root\(\)|ROOT|REPO` over `tests/` printed `test_case_schema.py`, `test_orchestration.py`, `test_schemas.py`, `test_lint.py`, `test_materialize.py` and `test_generate.py`. `test_lint.py` runs the target `lint` of the live `Makefile` and lists the six steps, so Case 820.7 makes it expect `guppi check` alone. `test_case_schema.py` runs the check over the example Case, whose method names `make test-cart`, a form both sides still take. The others read the lists of the `schema.yaml` files, and Case 820.3 changes only the prose of the `method` field of the estimates schema. Case 819 must change: Case 819.3 lists the `Makefile` among the files that `guppi ship` writes, in its new text of `rule-clean-branch`, in its `then` and in its task on `ROOT_FILES`, and its `then` says that it writes `.guppi/` but its tests and its environment, which leaves `.guppi/guppi/ship.py` written. Its rebuild should drop the `Makefile` from those three places, and for `ship.py` point to `estimate-clean-branch-ships-no-ship-command`, which makes that promise here. Case 820.5 adds its sentence of `rule-clean-branch` after words that Cases 816, 818 and 819 leave alone. Cases 816, 817 and 818 change no text this Case touches; `rule-morph`, which Case 817 changes, names the languages as values the install Case asks for, and stays true with the two new keys.

> **problem:**
> GUPPI runs its tests, its style check and its vault checks through `make`, which a project that installs GUPPI may not have and cannot get from GUPPI's Python environment, and it gives every such project a command `ship` that only this repository can use.

> **recommend:**
> - **What runs the vault checks in place of `make lint`**
>   - Recommended: (a) a new command `guppi check` that runs the same steps in the same order, each one even after a red step, red if any is.
>   - Answer: agreed, (a).
> - **Whether `guppi check` judges GUPPI's clean version in every project**
>   - Recommended: (b) only where the folder `plugin/` stands.
>   - Answer: (c) the user does not get `ship`: the clean version holds no `guppi/ship.py`, the judgment of a pointer moves into a module that `/pre-spec` and `guppi ship` both import, the list of commands has no `ship` when its module is missing, and `guppi check` skips that step then.
> - **What runs the tests in place of `make test`**
>   - Recommended: (a) `guppi test` runs a command set in `guppi.toml`.
>   - Answer: agreed, (a).
> - **What runs the style check in place of `make style`**
>   - Recommended: (a) `guppi style` runs a second command set in `guppi.toml`.
>   - Answer: agreed, (a).
> - **What a group rule's Estimate names in place of a make target**
>   - Recommended: (a) the method lists the test files.
>   - Answer: agreed, (a).
> - **When the `Makefile` leaves this repository**
>   - Recommended: (a) a thin `Makefile` stays here until a Case of a later session removes it, and the clean version stops writing it now.
>   - Answer: agreed, (a).
> - **How the pages and the harness take the new commands**
>   - Recommended: (a) one `reword` per command, and real changes only where make itself is the promise.
>   - Answer: agreed, (a).
> - **When the group Estimates switch to the list of test files**
>   - Recommended: (a) this Case teaches the checks the new form, and a Case of a later session moves the Estimates.
>   - Answer: agreed, (a).
> - **Whether a method may name `guppi test`, `guppi check` or `guppi style`**
>   - Recommended: (a) the three new commands count as a form.
>   - Answer: agreed, (a).
> - **What `guppi test` and `guppi style` do where `guppi.toml` sets no command**
>   - Recommended: (a) say so and exit non-zero.
>   - Answer: agreed, (a).
> - **The form of the two settings in `guppi.toml`**
>   - Recommended: (a) two keys, `test` and `style`, each a list of commands run in order.
>   - Answer: agreed, (a).
> - **What checks that this is done**
>   - Recommended: (a) new Estimates where nothing checks the change, and the replaced Criteria where one does.
>   - Answer: agreed, (a).
> - **What the thin `Makefile` runs for `test` and `style` until the next session**
>   - Recommended: (a) `lint` calls `guppi check`; `test` and `style` keep their own commands.
>   - Answer: agreed, (a).
> - **The check of the `Makefile` under both shells**
>   - Recommended: (a) replace its Criterion, naming the targets in words that the replace leaves alone.
>   - Answer: agreed, (a).

### Case 820.1 — guppi check runs the vault checks

> **given:**
> `rule-lint`: the rule of `guppi lint` and of the command that runs the vault checks.
> **＋** `estimate-lint-runs-every-step`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/check.py`, `.guppi/guppi/cli.py` and `.guppi/tests/test_check.py`: the new command `guppi check`, the list of commands of `guppi`, and the tests of the new command.
> **＋** `.guppi/guppi/ship.py`: the module of the command `ship`, which a project that installed GUPPI does not hold.
> **＋** `.claude/agents/librarian-guppi.md`, `.claude/skills/work/SKILL.md` and `.github/workflows/checks.yml`: the librarian's run, the Baseline of `/work` and the CI job that run the vault checks.
> **＋** `.claude/`: the harness files that name the command of the vault checks.

> **when:**
> Someone runs `uv run --project .guppi guppi check` in a project: by hand, in the Baseline of `/work`, in the librarian's run of `.claude/agents/librarian-guppi.md`, or in the job `lint` of `.github/workflows/checks.yml`.
> **＋** Or `.guppi/tests/test_check.py` runs it in a temporary project whose steps record each call: once with the step `guppi backlog --check` failing, once with every step exiting 0, and once with no module `.guppi/guppi/ship.py`.

> **then:**
> It runs `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint` and `guppi ship --check`, in that order, whether an earlier step exited 0 or not.
> **＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
> **＋** It exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
> **＋** No live rule, entity or Estimate outside History and Result, and no file of `.claude/`, names make with the target `lint` as the way to run the vault checks.
> **－** Where the module `.guppi/guppi/ship.py` is missing, as in a project that installed GUPPI, it runs the other five steps and prints one line that it skips `guppi ship --check`, and that skip sets no exit code.
> **－** No step reads the stdin of its caller, and it writes nothing to the tree.

> **tasks:**
> - [ ] update `rule-lint`
>   - set:
>     ```
>     implementation_ref: [.guppi/guppi/lint.py, .guppi/guppi/check.py, .guppi/tests/test_lint.py, .guppi/tests/test_check.py]
>     ```
>   - sections.Purpose:
>     ```
>     Prevents a page that breaks its schema, points at nothing, claims a status its
>     Estimates do not support, or waits for a reading nobody took from sitting in the vault
>     unnoticed. Pages are written by the generator;
>     both drift, and nothing else reads the whole graph at once. Red is a signal, not a
>     gate: a `pending` Estimate is red until its reading, but for one whose `method` waits for a later moment — an event it names, a later session, a session of a sprint, the session that closes one, the librarian or `/hi` — since the brief lists it under Readings due and puts it under Work once its moment comes, and a `failed` one is red until it is read again (cases 182, 799); a placeholder is red with the count of its defers (case 186.3).
>     `uv run --project .guppi guppi check` runs it after `guppi render --check`, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check`, and runs `guppi ship --check` after it, which finds a pointer outside its bracket in each file outside `vault/` that the clean version holds (case 807.2). Where the command `ship` is missing, as in a project that installed GUPPI, it prints one line that it skips that step and runs the other five (case 820). All six only report, so no step writes to the tree (cases 147.7, 227). It runs every step even when one of them is red, so a red step hides no finding of a later one, and it exits non-zero when any step is red (case 587). It needs no tool but `uv`, so a project runs it on any machine (case 820). `parent: rule-harness` names the
>     MOC of the harness tools: lint runs with the renderer, in no phase of the session. The
>     classes and their order live in the docstring of `.guppi/guppi/lint.py`.
>     ```
>   - change: `guppi check runs the six vault checks, and skips guppi ship --check where the command ship is missing`
> - [ ] update `estimate-lint-runs-every-step`
>   - set:
>     ```
>     status: pending
>     purpose: Whether guppi check runs every step, guppi ship --check last, when an earlier one is red, prints the lines of each, exits non-zero when any step is red, and skips guppi ship --check where the command ship is missing
>     method: uv run --project .guppi pytest .guppi/tests/test_check.py
>     ```
>   - change: `the Criterion replaced whole — guppi check runs the vault checks in place of the target lint of the Makefile`
> - [ ] `.guppi/guppi/check.py`: `run` runs the six steps in order, each even after a red one, each with its own output and no stdin, exits non-zero when any is red, and skips `guppi ship --check` with one line when the module `guppi.ship` cannot be found; the docstring says so and names `rule-lint`.
> - [ ] `.guppi/guppi/cli.py`: the command `check` in `COMMANDS`.
> - [ ] `.guppi/tests/test_check.py`: the order of the steps, every step after a red `guppi backlog --check`, the exit code with one red step and with none, no stdin read, the tree unchanged, and the skip of `guppi ship --check` with its one line when the module is missing.
> - [ ] read `estimate-lint-runs-every-step`

> **ratification:**
> ```
> - decision[case 820.1][update][rule-lint]{ref:rule-lint}
> - decision[case 820.1][update][estimate-lint-runs-every-step]{ref:rule-lint}
> ```

### Case 820.2 — guppi test and guppi style run the commands of guppi.toml

> **given:**
> `rule-guppi-config`: the rule of `guppi.toml`, which now also sets the commands of the tests and of the style check.
> **＋** `estimate-guppi-config-runs-the-test-and-style-commands`: the new check of the two commands.
> **＋** `guppi.toml`: the settings file, rendered from the Render of `rule-guppi-config`.
> **＋** `.guppi/guppi/commands.py`, `.guppi/guppi/config.py`, `.guppi/guppi/cli.py` and `.guppi/tests/test_commands.py`: the two new commands, the reader of `guppi.toml`, the list of commands of `guppi`, and the tests of the new commands.
> **＋** `.claude/skills/work/SKILL.md`, `.claude/skills/retro/SKILL.md` and `.github/workflows/checks.yml`: the Baseline of `/work`, Retro and the CI jobs that run the tests and the style check.
> **＋** `.claude/`: the harness files that name the commands of the tests and of the style check.
> **＋** `rule-morph`: the install Case that sets the settings of a new project.

> **when:**
> Someone runs `uv run --project .guppi guppi test` or `uv run --project .guppi guppi style` in a project, as `rule-guppi-config` sets it: by hand, in the Baseline of `/work`, in Retro, or in the jobs `test` and `style` of `.github/workflows/checks.yml`.

> **then:**
> It reads the list of commands of the key `test`, or of the key `style`, from `guppi.toml` at the root of the project.
> **＋** It runs each command of the list in order, in the folder of the project and with no shell between, each one even after a red one.
> **＋** The output of each command reaches the person whole, and no command gets the stdin of `guppi test` or `guppi style`.
> **＋** A single red command makes the run red; the run is green only when all the listed commands pass.
> **＋** In this repository, the key `test` holds `uv run --project .guppi pytest -q`, and the key `style` holds `uv run --project .guppi ruff check .` and `uv run --project .guppi ruff format --check .`.
> **＋** The rules, entities and Estimates of the vault and the harness files of `.claude/` call the tests and the style check by these two commands, and never by make.
> **－** When `guppi.toml` is missing or holds no such key, it prints one line that names the file and the key, runs nothing and exits 1.
> **－** The render reads `documentation_lang` and `chat_lang` as before, and a key `test` or `style` does not stop it.

> **tasks:**
> - [ ] update `rule-guppi-config`
>   - set:
>     ```
>     implementation_ref: [.guppi/guppi/config.py, .guppi/guppi/commands.py, .guppi/tests/test_config.py, .guppi/tests/test_commands.py]
>     ```
>   - sections.Purpose:
>     ```
>     Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision. This page's Render is `guppi.toml`, guppi's one settings file: a change is an `update` of the Render, and the governed-files hook refuses a hand edit of the file. It sets the language of the repository, `documentation_lang`, and the language of the chat with the owner, `chat_lang`, as codes; `.guppi/guppi/config.py` holds the table of each code's name and script. The render reads the codes from this Render and puts the name where another Render writes `{{documentation_lang}}` or `{{chat_lang}}`; the checks, such as the pre-spec finding, read `guppi.toml`.
>
>     It also sets how the project tests its code and checks its style: the key `test` and the key `style`, each a list of commands. `uv run --project .guppi guppi test` runs the commands of `test`, and `uv run --project .guppi guppi style` the commands of `style`, which `.guppi/guppi/commands.py` reads from `guppi.toml` through `.guppi/guppi/config.py`. Each runs its commands in order, in the folder of the project and with no shell between, runs each one even after a red one, lets each print its own lines, and exits non-zero when any of them does. When `guppi.toml` or the key is missing, it prints one line that names the file and the key, runs nothing and exits 1, so a project with no command set never reads as tested. Work Mode, Retro and the CI of the project run these two commands, so a project needs no tool but `uv` (case 820). The questions asked at install, these two commands among them, stay with `rule-morph` (cases 476.1, 802); the category set as data waits as a line of the `## Backlog` of `entity-sprint-plugin` (case 802).
>     ```
>   - sections.Render:
>     ````
>     <!-- rule-guppi-config -->
>     # guppi settings, rendered from vault/wiki/rules/rule-guppi-config.md
>     documentation_lang = "en"
>     chat_lang = "ru"
>     test = ["uv run --project .guppi pytest -q"]
>     style = ["uv run --project .guppi ruff check .", "uv run --project .guppi ruff format --check ."]
>     <!-- /rule-guppi-config -->
>     ````
>   - change: `guppi.toml sets the commands of the tests and of the style check, which guppi test and guppi style run`
> - [ ] create `estimate-guppi-config-runs-the-test-and-style-commands`
>   - ref: `rule-guppi-config`
>   - kind: `QA`
>   - purpose: `Whether guppi test and guppi style run the commands that the keys test and style of guppi.toml list, in order and each after a red one, exit non-zero when any is red, and exit 1 with one line when the file or the key is missing`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_commands.py; by hand, after the librarian's run that renders guppi.toml with the keys test and style: uv run --project .guppi guppi test and uv run --project .guppi guppi style in this repository, read against the Criterion`
>   - tags: `[harness, tests]`
> - [ ] `.guppi/guppi/config.py`: one function reads the list of commands of a key of `guppi.toml`, and names the file and the key when either is missing; `parse` still checks only the two language keys; the docstring says so.
> - [ ] `.guppi/guppi/commands.py`: `guppi test` and `guppi style` read their key through `.guppi/guppi/config.py`, split each command into its words and run it in the folder of the project with no shell and no stdin, each after a red one, and exit non-zero when any is red, or exit 1 with one line when the file or the key is missing; the docstring names `rule-guppi-config`.
> - [ ] `.guppi/guppi/cli.py`: the commands `test` and `style` in `COMMANDS`.
> - [ ] `.guppi/tests/test_commands.py`: the order of the commands, every command after a red one, the exit code with one red command and with none, no stdin read, no shell, and the one line with exit 1 for a missing `guppi.toml` and for a missing key.
> - [ ] `uv run guppi render`: `guppi.toml`
> - [ ] read `estimate-guppi-config-runs-the-test-and-style-commands`

> **ratification:**
> ```
> - decision[case 820.2][update][rule-guppi-config]{ref:rule-guppi-config}
> - decision[case 820.2][create][estimate-guppi-config-runs-the-test-and-style-commands]{ref:rule-guppi-config}{tags:harness,tests}
> ```

### Case 820.3 — guppi lint takes the new forms of a method

> **given:**
> `rule-estimates-schema`: the schema of an Estimate, whose field `method` names the forms that lint classifies.
> **＋** `estimate-lint-checks-the-method`: its Criterion is replaced whole.
> **＋** `vault/wiki/estimates/schema.yaml`: the Render of `rule-estimates-schema`, which `guppi lint` reads.
> **＋** `.guppi/guppi/lint.py`: `names_a_form`, `names_a_moc_form`, `sibling_names_a_target` and `check_method`.
> **＋** `.guppi/tests/test_lint.py`: the tests of the method check.
> **＋** `Makefile`: the targets of the pipelines of the MOCs, which this repository keeps for now.
> **＋** `estimate-claude-md-rendered`: the Estimate that gets no `method` finding.

> **when:**
> `uv run --project .guppi guppi lint` reads the `method` field of each live Estimate.

> **then:**
> For an Estimate of a Leaf, a test file that exists, the word `pytest`, a `make <target>` of the `Makefile`, one of the commands `guppi test`, `guppi check` and `guppi style`, or `by hand` passes; else the finding "method: names no test file, pytest, guppi command or make target and is not a reading".
> **＋** A named test file that does not exist, or a `make <target>` that the `Makefile` does not hold, is a finding.
> **＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it, and so does the word `pytest` with one or more test files, each of which exists.
> **＋** For an Estimate of a MOC, `by hand` without either passes when every counted Estimate of the children is a reading or a sibling Estimate names either; else a finding.
> **＋** On a MOC with `render_mode: full`, the Estimates of a child with `enforcement: render` are not counted.
> **＋** `estimate-claude-md-rendered` gets no `method` finding.
> **－** On a MOC, the word `pytest` with no test file, a test file with no `pytest`, and a command `guppi test`, `guppi check` or `guppi style` alone are each a finding.
> **－** On a MOC with `render_mode: full`, the Estimates of a child without `enforcement: render` are counted.
> **－** On a MOC without `render_mode: full`, the Estimates of every child are counted, a child with `enforcement: render` included.
> **－** A `## Method` section is not read as the `method` of a page.

> **tasks:**
> - [ ] update `rule-estimates-schema`
>   - old: `` On the Estimate of a MOC the form is a `make <target>` of the Makefile alone — there `pytest` or a path by itself earns a finding, and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a target; ``
>   - new: `` Besides these four forms, the Estimate of a Leaf may name one of the commands `guppi test`, `guppi check` and `guppi style`, which run the tests, the vault checks and the style check of the project. On the Estimate of a MOC the form is a `make <target>` of the Makefile, or the word `pytest` with the test files of its pipeline, each of which must exist — there `pytest` without a test file, a path without `pytest`, or one of the commands of the project alone earns a finding, and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a form; ``
>   - change: `a method may name guppi test, guppi check or guppi style, and the Estimate of a MOC may name pytest with the test files of its pipeline`
> - [ ] update `estimate-lint-checks-the-method`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the commands guppi test, guppi check and guppi style are forms, and on a MOC pytest with test files that exist passes`
> - [ ] `.guppi/guppi/lint.py`: `names_a_form` takes the commands `guppi test`, `guppi check` and `guppi style`; `names_a_moc_form` takes the word `pytest` with one or more test paths; `check_method` checks on a MOC that each such path exists, and `sibling_names_a_target` takes a sibling that names such a form; the finding names the new forms; the docstrings say so.
> - [ ] `.guppi/tests/test_lint.py`: on a Leaf each of the three commands passes; on a MOC `pytest` with test files that exist passes, a missing one is a finding, and `pytest` alone, a path alone and a command alone are findings; a sibling with `pytest` and test files lets `by hand` pass; the tests of a `make <target>` stand.
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] read `estimate-lint-checks-the-method`

> **ratification:**
> ```
> - decision[case 820.3][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 820.3][update][estimate-lint-checks-the-method]{ref:rule-lint}
> ```

### Case 820.4 — /pre-spec takes the new forms of a method

> **given:**
> `estimate-prespec-catches-a-method-without-a-form`: its Criterion is replaced whole.
> **＋** `rule-prespec`: the rule of `/pre-spec`, the target of that Estimate.
> **＋** `.guppi/guppi/prespec.py`: `NO_FORM`, `MOC_NO_FORM` and the method check of the plan.
> **＋** `.guppi/guppi/lint.py`: `names_a_form` and `names_a_moc_form`, which `/pre-spec` imports, and `check_method`.
> **＋** `.guppi/tests/test_prespec.py`: the tests of `/pre-spec`.
> **＋** `Makefile`: the targets of the pipelines that a MOC's `method` may name.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks before the Spec is approved.

> **then:**
> A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the forms lint classifies (a `make <target>`, the word `pytest`, a test path, one of the commands `guppi test`, `guppi check` and `guppi style`, or the words `by hand`) gives one line `case N: <create|update> <slug>: method names no form`, which goes on to name those forms.
> **＋** A `create` of an Estimate with no `method` at all gives the same finding.
> **＋** When the target of the Estimate is a MOC as the plan leaves it — the live page, or a `create` or an `update` of the plan that writes `kind: MOC` — a `method` that names neither a `make <target>`, nor the word `pytest` with a test path, nor `by hand` gives one line `case N: <create|update> <slug>: method of a MOC's Estimate names no make target or test files and is not a reading`, in place of the line of no form.
> **＋** The predicate is one, lifted out of `.guppi/guppi/lint.py`; `/pre-spec` writes no second one.
> **＋** The form of a MOC's `method` is one predicate too, in `.guppi/guppi/lint.py`, which `check_method` of `guppi lint` calls as well.
> **－** Existence is not checked in the plan: the test file is written in Work Mode, and lint checks it later.
> **－** Whether the `Makefile` holds the `make <target>` that a MOC's `method` names is left to lint.
> **－** Whether every counted Estimate of the MOC's children is a reading, or a sibling Estimate names a form of a MOC, is left to lint.
> **－** An `update` of an Estimate that writes no `method` gives no line of the form of a MOC's `method`.

> **tasks:**
> - [ ] update `estimate-prespec-catches-a-method-without-a-form`
>   - set:
>     ```
>     status: pending
>     purpose: Whether pre-spec refuses an Estimate whose method names none of the forms lint classifies, or, on a MOC, neither a make target, nor pytest with a test path, nor by hand
>     method: uv run --project .guppi pytest .guppi/tests/test_prespec.py on a temp plan — a create with a prose method, a create with no method, each of the five forms clean, and on a MOC a test path alone, pytest alone and guppi test alone as findings, a make target, pytest with a test path and by hand clean
>     ```
>   - change: `the Criterion replaced whole — the commands guppi test, guppi check and guppi style are forms, and on a MOC pytest with a test path is one`
> - [ ] `.guppi/guppi/prespec.py`: `NO_FORM` and `MOC_NO_FORM` name the new forms; the method check of the plan calls `names_a_form` and `names_a_moc_form` of `.guppi/guppi/lint.py` as before; the docstring says so.
> - [ ] `.guppi/tests/test_prespec.py`: each of the five forms clean on a Leaf; on a MOC `pytest` with a test path clean, and a test path alone, `pytest` alone and `guppi test` alone each the line of a MOC; the lines name the new forms.
> - [ ] read `estimate-prespec-catches-a-method-without-a-form`

> **ratification:**
> ```
> - decision[case 820.4][update][estimate-prespec-catches-a-method-without-a-form]{ref:rule-prespec}
> ```

### Case 820.5 — The clean version holds no command ship

> **given:**
> `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `estimate-clean-branch-ships-no-ship-command`: the new check that the clean version holds no command `ship`.
> **＋** `.guppi/guppi/ship.py`, `.guppi/guppi/pointers.py` and `.guppi/guppi/cli.py`: the command `ship`, the new module of the judgment of a pointer, and the list of commands of `guppi`.
> **＋** `.guppi/tests/test_ship.py`: the tests of `guppi ship`.
> **＋** `vault/raw/2026-10-14/1907/cases/case-816.md`, `vault/raw/2026-10-14/1907/cases/case-818.md` and `vault/raw/2026-10-14/1907/cases/case-819.md`: the Cases of this session that change other sentences of `rule-clean-branch`.

> **when:**
> `uv run --project .guppi guppi ship <folder>` builds the clean version of this repository into an empty folder, as `rule-clean-branch` sets it.
> **＋** Then `guppi` runs from the code of that folder, with no argument and with the argument `ship`.

> **then:**
> The clean version holds `.guppi/guppi/pointers.py` and no `.guppi/guppi/ship.py`.
> **＋** Run from the code of the clean version, `guppi` lists no command `ship`, and `guppi ship` prints that the command is unknown and exits 2.
> **＋** `guppi ship` removes and refuses a pointer by the functions of `.guppi/guppi/pointers.py`, and holds no copy of them.
> **－** `guppi ship --check` does not judge `.guppi/guppi/ship.py`, which the clean version does not hold.
> **－** In this repository, `guppi` lists the command `ship`, and `guppi ship` runs as `rule-clean-branch` sets it.

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old: `a Case rewords that text at its source.`
>   - new: `` a Case rewords that text at its source. It does not write `.guppi/guppi/ship.py`, so a project that installs GUPPI, which builds no clean version, gets no command `ship`, and `guppi check` skips its step `guppi ship --check` there; the judgment of a pointer outside its bracket, which `guppi ship` and `/pre-spec` share, lives in `.guppi/guppi/pointers.py`, which it writes (case 820). ``
>   - change: `the clean version holds no guppi/ship.py, and the judgment of a pointer lives in guppi/pointers.py`
> - [ ] create `estimate-clean-branch-ships-no-ship-command`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether the clean version holds the module of the judgment of a pointer and no module of the command ship, so that guppi there lists no command ship, while guppi ship of this repository judges by that module`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k ship_command`
>   - tags: `[plugin, ci]`
> - [ ] `.guppi/guppi/pointers.py`: `outside` and the functions and patterns it calls, moved from `.guppi/guppi/ship.py` unchanged; the docstring names it the one judgment of a pointer, which `guppi ship` and `/pre-spec` import.
> - [ ] `.guppi/guppi/ship.py`: imports the judgment of a pointer from `.guppi/guppi/pointers.py` and keeps no copy of it; the copy and `--check` skip `.guppi/guppi/ship.py`; the docstring says so.
> - [ ] `.guppi/guppi/cli.py`: `COMMANDS` holds `ship` only when the module `guppi.ship` can be found.
> - [ ] `.guppi/tests/test_ship.py`: a clean version built into a temporary folder holds `.guppi/guppi/pointers.py` and no `.guppi/guppi/ship.py`; the code of that folder lists no command `ship`, and `guppi ship` there exits 2 with its line; `--check` prints no line for `.guppi/guppi/ship.py`; the names of these tests hold `ship_command`.
> - [ ] read `estimate-clean-branch-ships-no-ship-command`

> **ratification:**
> ```
> - decision[case 820.5][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 820.5][create][estimate-clean-branch-ships-no-ship-command]{ref:rule-clean-branch}{tags:plugin,ci}
> ```

### Case 820.6 — /pre-spec judges a pointer by the module it shares with guppi ship

> **given:**
> `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`: its Criterion is replaced whole.
> **＋** `rule-prespec-hook`: the rule of the hook at `ExitPlanMode`, the target of that Estimate.
> **＋** `.guppi/guppi/prespec.py` and `.guppi/guppi/pointers.py`: `/pre-spec`, and the module whose judgment of a pointer it imports.
> **＋** `.guppi/tests/test_prespec.py`: the test that asserts that both sides share one judgment.
> **＋** `decision-case-N`: the form of the id of a Decision page.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan>` checks the plan of a session, or the hook of `rule-prespec-hook` runs the same judgment when the agent calls `ExitPlanMode`.

> **then:**
> It prints a finding for each pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — that stands outside a bracket of its own in the `new` of a `replace` pair, the text of a `sections` value or the `purpose` of an item for a page that carries `core: true`, on the live page or as the plan leaves it.
> **＋** The finding names the Case, the page and the pointer.
> **＋** It judges each text by `outside` of `.guppi/guppi/pointers.py`, imported, the judgment that `guppi ship` runs over the files it writes.
> **－** A pointer inside such a bracket, a code span or a fenced block is no finding.
> **－** An item for a page without `core: true`, the `change` line of an item, and the `context`, `problem` and `recommend` of a Case are not judged.

> **tasks:**
> - [ ] update `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the judgment of a pointer is imported from guppi/pointers.py`
> - [ ] `.guppi/guppi/prespec.py`: imports `outside` from `.guppi/guppi/pointers.py`; the docstrings name that module.
> - [ ] `.guppi/tests/test_prespec.py`: the test that asserted `prespec.outside is ship.outside` asserts `prespec.outside is pointers.outside`.
> - [ ] read `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`

> **ratification:**
> ```
> - decision[case 820.6][update][estimate-prespec-hook-reports-a-pointer-outside-a-bracket]{ref:rule-prespec-hook}
> ```

### Case 820.7 — The Makefile stays for now and every text names the new commands

> **given:**
> `rule-harness`: the MOC of the harness tools, whose Purpose names the `Makefile` that stays for now.
> **＋** `estimate-harness-make-runs-in-both-shells`: its Criterion is replaced whole.
> **＋** `Makefile` and `.guppi/tests/test_lint.py`: the targets that this repository keeps until a later Case removes the file, and the test that runs its target `lint`.
> **＋** `rule-lint` and `rule-guppi-config`: the owners of the replace of the old commands over every live rule, entity and Estimate.
> **＋** `.github/workflows/checks.yml` and `rule-github-repository`: the CI jobs and their rule.
> **＋** `.claude/`, `vault/wiki/where-to-stop.md`, `vault/wiki/case-schema.md` and `vault/wiki/glossary.md`: the rendered files whose pages the replace changes.
> **＋** `.guppi/guppi/`: the docstrings that name the old commands.
> **＋** `C:/ProgramData/chocolatey/bin/make.exe`, `/dev/null` and `/usr/bin/sh`: the make of Windows that reads the `Makefile`, the stdin of each recipe, and the shell of the `Makefile` outside Windows.

> **when:**
> On Windows, someone runs make with each of the targets `help`, `style`, `test` and `lint` of the `Makefile` from PowerShell and from Git Bash. `C:/ProgramData/chocolatey/bin/make.exe` reads the `Makefile`.
> **＋** Or `.guppi/tests/test_lint.py` runs make with the target `lint` of the `Makefile` in a temporary folder, with a fake `uv` first on the search path that records each call.

> **then:**
> Make runs each recipe under a POSIX `sh`, with stdin read from `/dev/null`, and each target gives the same exit code from PowerShell as from Git Bash.
> **＋** The target `lint` runs `uv run --project .guppi guppi check` and nothing else.
> **＋** The target `test` runs pytest over the tests of `.guppi/tests/`, and the target `style` runs ruff, both as they did before this change.
> **＋** The targets of the pipelines of the MOCs stand as before.
> **＋** When make finds no POSIX `sh` on Windows, it stops before any recipe runs, with one message that names the missing shell and the places it searched.
> **－** Make never runs a recipe of the `Makefile` under `cmd.exe`.
> **－** Running a target changes no file of the working tree.
> **－** Outside Windows, the `SHELL` of the `Makefile` stays `/usr/bin/sh`.

> **tasks:**
> - [ ] update `rule-harness`
>   - old: `(cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1, 640, 710.1, 796).`
>   - new: `` (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1, 640, 710.1, 796). This repository keeps, for now, a `Makefile`: its target `lint` runs `uv run --project .guppi guppi check`, its target `test` runs pytest, its target `style` runs ruff, and one target runs the tests of each pipeline of a MOC, each under a POSIX shell on Windows too; a project that installs GUPPI gets no `Makefile`, and a later Case removes it (case 820). ``
>   - change: `the Makefile stays for now: its target lint runs guppi check, and its other targets stand`
> - [ ] update `estimate-harness-make-runs-in-both-shells`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the Makefile that this repository keeps for now runs its targets help, style, test and lint under a POSIX sh from PowerShell as from Git Bash, its target lint runs guppi check alone, and it stops with a message when no sh is found
>     method: "uv run --project .guppi pytest .guppi/tests/test_lint.py -k makefile; by hand, after the Work Mode that builds this change: make with the targets help, style, test and lint from PowerShell and from Git Bash on Windows, read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the Makefile stays for now, and its target lint runs guppi check`
> - [ ] update `rule-lint`
>   - reword old: `make lint`
>   - reword new: `uv run --project .guppi guppi check`
>   - change: `every live rule, entity and Estimate names guppi check in place of the target lint of the Makefile`
> - [ ] update `rule-guppi-config`
>   - reword old: `make test`
>   - reword new: `uv run --project .guppi guppi test`
>   - reword old: `make style`
>   - reword new: `uv run --project .guppi guppi style`
>   - change: `every live rule, entity and Estimate names guppi test and guppi style in place of the targets test and style of the Makefile`
> - [ ] `Makefile`: the target `lint` runs `uv run --project .guppi guppi check` alone; the targets `help`, `test`, `style` and those of the pipelines keep their recipes; the comment at the top says that the file stays until a later Case removes it, that `guppi check`, `guppi test` and `guppi style` are the commands of the checks, and that the clean version does not hold it.
> - [ ] `.guppi/tests/test_lint.py`: the test of the target `lint` of the `Makefile` records one call, `run --project .guppi guppi check`, and its name holds `makefile`; the tests of the steps move to `.guppi/tests/test_check.py`.
> - [ ] `.github/workflows/checks.yml`: the jobs `style`, `test` and `lint` run `uv run --project .guppi guppi style`, `uv run --project .guppi guppi test` and `uv run --project .guppi guppi check`, with no step that installs make; the comment at the top says so.
> - [ ] `.guppi/guppi/`: each docstring, comment and message that names the old commands names `guppi check`, `guppi test` or `guppi style`.
> - [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/box/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] `uv run guppi render`: `vault/wiki/where-to-stop.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `uv run guppi glossary`
> - [ ] read `estimate-harness-make-runs-in-both-shells`

> **ratification:**
> ```
> - decision[case 820.7][update][rule-harness]{ref:rule-harness}
> - decision[case 820.7][update][estimate-harness-make-runs-in-both-shells]{ref:rule-harness}
> - decision[case 820.7][update][rule-lint]{ref:rule-lint}
> - decision[case 820.7][update][rule-guppi-config]{ref:rule-guppi-config}
> ```

### Case 820.8 — The sprint's check of a pull request names the commands that CI runs

> **given:**
> `estimate-sprint-plugin-pull-requests-reviewed-on-github`: its Criterion is replaced whole.
> **＋** `entity-sprint-plugin`: the sprint page, the target of that Estimate.
> **＋** `.github/workflows/checks.yml` and `rule-github-repository`: the CI jobs and their rule.
> **＋** `GUPPI`, `main`, `prod` and `plugin`: the repository on GitHub and its branches.

> **when:**
> In a session of the sprint `plugin` before its close, someone opens a pull request against the branch `main` of the repository `GUPPI` on GitHub, which `rule-github-repository` describes, from an account other than the owner's, such as a second account that the owner made for the test.

> **then:**
> The workflow `.github/workflows/checks.yml` runs its jobs `test`, `lint` and `style` on `windows-latest` on the pull request, by `uv run --project .guppi guppi test`, `uv run --project .guppi guppi check` and `uv run --project .guppi guppi style`, and shows each result on it.
> **＋** A run of a first-time contributor waits until the owner approves it.
> **＋** The owner reviews the pull request on GitHub, and only the owner can merge it.
> **＋** A merge into `main` waits until the jobs `style` and `test` pass, except for the owner, who is on the bypass list of the ruleset on `main`.
> **＋** The other account cannot push to `main` or to `prod`, and a pull request against `prod` cannot be merged.
> **－** A red result of the job `lint` does not block a merge into `main`.
> **－** The workflow does not run on the event `pull_request_target`, so the code of the pull request reaches no secret of the repository.
> **－** The test pull request is closed without a merge, so `main` takes no commit before `plugin` closes.

> **tasks:**
> - [ ] update `estimate-sprint-plugin-pull-requests-reviewed-on-github`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the jobs of CI run guppi test, guppi check and guppi style in place of the targets of the Makefile`
> - [ ] read `estimate-sprint-plugin-pull-requests-reviewed-on-github`

> **ratification:**
> ```
> - decision[case 820.8][update][estimate-sprint-plugin-pull-requests-reviewed-on-github]{ref:entity-sprint-plugin}
> ```
