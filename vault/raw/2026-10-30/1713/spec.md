<!-- approved 19:38:14 · session 5c343872 -->

# Session 1713 — the items of the brief of 0304

## Case 927 — The method of the Makefile Estimate names real targets

> **context:**
> `uv run --project .guppi guppi check` reads the `method` of each Estimate. On an Estimate of a MOC, `check_method` of `.guppi/guppi/lint.py` takes the first match of `MAKE_TARGET`, the word `make` and the word after it, and gives a finding when `holds_target` finds no such target in the `Makefile`. The method of `estimate-harness-make-runs-in-both-shells`, whose target `rule-harness` is a MOC with no parent, says "make with the targets help, style, test and lint", so the check reads `with` as a target and prints `estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`. The brief, `## Flags`, reports it among the 13 lines of `guppi check` at its last run (exit 1), and the work files of each session since 2026-10-15 hold it in their Baseline. Case 838 put this misreading off as a defer on `rule-lint`. The person chose to fix the wording of the page and leave the check as it is: the check keeps what `estimate-lint-checks-the-method` promises, that a `make <target>` the `Makefile` does not hold is a finding. The new method names `make help`, `make style`, `make test` and `make lint`. `MAKE_TARGET` then reads `help` first, and the `Makefile` holds `help:`, so the line goes. `ships` of `.guppi/guppi/ship.py` leaves out of the clean copy an Estimate whose method has a match of `MAKE_TARGET`; the new method still has one, so the Estimate stays out of the copy, as it should, since the copy holds no `Makefile`. I read `check_method`, `is_reading`, `names_a_moc_form`, `names_test_files`, `missing_test_files`, `holds_target` and `sibling_names_a_target` of `lint.py`, and `ships` of `ship.py`. The pytest part of the method names `.guppi/tests/test_lint.py`, which exists, and stands. The Criterion and the status `passed` of the Estimate stand, since only the `method` field changes. A Grep of `^method:.*\bmake [\w-]` over `vault/wiki` printed 11 methods; two more say "make with the target": `estimate-guppi-config-runs-the-test-and-style-commands` and `estimate-lint-runs-every-step`. Their targets are Leafs, where `by hand` passes before any make target is read, so lint gives them no finding; `ships` leaves them out of the clean copy for the same misread word, and this Case leaves that as it stands, by the person's choice of the page over the check. A Grep of `make-runs-in-both-shells` over `.guppi` printed nothing, so no test reads this page. The change is checked by `estimate-lint-checks-the-method`, whose Criterion says that on a MOC a `make <target>` of the `Makefile` passes whatever stands beside it; it stands, since the check does not change, and the `guppi check` of the librarian's run, which the brief reports, shows the line gone. The page changes at that run, so `guppi check` in Work Mode still prints the line. The update of `rule-lint` carries only a History line and retires the defer of case 838, so the librarian's run takes `rule-lint` off the backlog.

> **problem:**
> `guppi check` stays red on one line because the method of `estimate-harness-make-runs-in-both-shells` says "make with", and the check reads `with` as a target of the `Makefile`.

> **recommend:**
> - **Fix the page or the check**
>   - Recommended: (a) reword this one method so that it names the targets as `make help`, `make style`, `make test` and `make lint`.
>   - Answer: agreed, (a).
> - **The put-off decision on rule-lint**
>   - Recommended: (a) take it up and close it in this Case, by an update of `rule-lint` with a History line only.
>   - Answer: agreed, (a).

> **given:**
> `estimate-harness-make-runs-in-both-shells`: the Estimate whose `method` changes.
> **＋** `rule-lint`: the page that holds the defer of case 838.
> **＋** `.guppi/guppi/lint.py`: the check that reads a make target in a `method`.
> **＋** `.guppi/guppi/ship.py`: the copy that leaves out an Estimate with a make target in its `method`.
> **＋** `Makefile`: the file that holds the targets.
> **＋** `estimate-lint-checks-the-method`: the Estimate that checks the `method` of an Estimate.

> **when:**
> `uv run --project .guppi guppi check`, at the librarian's run, reads the `method` of `estimate-harness-make-runs-in-both-shells` with `.guppi/guppi/lint.py`.

> **then:**
> The check reads `make help` as the make target of the `method`, and the `Makefile` holds `help`.
> **＋** The check prints no `method` line for `estimate-harness-make-runs-in-both-shells`.
> **＋** `.guppi/guppi/ship.py` still leaves `estimate-harness-make-runs-in-both-shells` out of the clean copy.
> **－** The Criterion and the status of `estimate-harness-make-runs-in-both-shells` do not change.
> **－** `.guppi/guppi/lint.py` does not change.

```then
update:
- slug: estimate-harness-make-runs-in-both-shells
  set:
    method: 'uv run --project .guppi pytest .guppi/tests/test_lint.py -k makefile; by hand, after the Work Mode that builds this change: make help, make style, make test and make lint from PowerShell and from Git Bash on Windows, read against the Criterion'
  change: the method names the targets as make help, make style, make test and make lint, so lint reads no target with
- slug: rule-lint
  change: 'the defer of case 838 is taken up: the method of estimate-harness-make-runs-in-both-shells names real targets, and the check stands'
```

```tasks
- [ ] update `estimate-harness-make-runs-in-both-shells`
- [ ] update `rule-lint`
```

## Case 928 — The reading of the clean code runs by guppi ship --check --review

> **context:**
> `estimate-clean-branch-code-holds-pointers-only-in-brackets` checks that the code and the tests hold each pointer to a case in a bracket of its own. Its `method` builds the clean copy by `uv run --project .guppi guppi ship --review` into an empty folder. In `run` of `.guppi/guppi/ship.py`, a build into a folder first calls `drafts`, which lists each page that `is_draft_core` accepts. When the list is not empty and `--allow-draft` is not passed, `run` prints the list and returns 1 before it reads a tag or writes the copy. The brief reports the last `guppi check` (`## Flags` of `vault/wiki/brief.md`): "Lint (`guppi check`, exit 1, 13 lines): 12 pages with `core: true` stand `draft`". So the reading as its `method` writes it gives no lines. The handoff of session 0304 says that Retro ran it with `--allow-draft`, and "The `method` does not name the flag". The `When` of the Criterion has the same gap: it says that `ship --review <folder>` builds the clean version, which it does not do while such a page stands.
>
> The person chose to read by `uv run --project .guppi guppi ship --check --review`. In `run`, `--check` calls `check` and never calls `drafts` or `version`, and `--review` adds the bracket lines whatever the path. `check` and `settled` both judge a file by `judged`. For a file under `.guppi/`, `plan` maps its path in the copy to the same path in the tree, and `ship` copies it by `shutil.copyfile` and changes only `CLAUDE.md` and the manifest before it judges, so both paths list the same lines for those files. I read `run`, `check`, `ship`, `settled`, `judged`, `plan`, `drafts` and `version` of `.guppi/guppi/ship.py` whole for these claims. No test runs `--check` and `--review` together. A Grep of `"--check"` over `.guppi/tests/test_ship.py` printed 11 lines, and none of them passes `--review` beside `--check`. A Grep of `--check.*--review|--review.*--check` over `.guppi/tests/` printed `.guppi/tests/test_ship.py`, whose hit is its module docstring, which names the two options apart. The reading at Retro shows the pair live.
>
> The Case replaces the Criterion whole and sets the Estimate `pending`, and the reading of this session at Retro checks it. The new `When` names the new command. The `Then` lines stand as they were, with three changes. The first line speaks of a line on a pointer outside its bracket, since the run now prints the `--review` lines on the same files too. A new `－` line says that a draft page and a missing tag do not stop the run. The line on the rewording now names what it rewords, so that it reads without the earlier Case. The line on `.claude/` speaks of a line of the run rather than of `--check` alone. A Criterion line names `Makefile` and `pyproject.toml`. `plan` takes neither the `Makefile` nor the root `pyproject.toml` into the copy (`ROOT_FILES` holds `CLAUDE.md` and `.gitattributes`), so neither command judges them. That line was true before and stays true, so it stands. The `purpose` speaks of what `guppi ship --check` prints and of the brackets it removes, which both still hold, so it stands. The `method` is set anew.
>
> A Grep of `ship --review` over `vault/wiki/` and `.claude/` printed `vault/wiki/estimates/estimate-clean-branch-pages-hold-pointers-only-in-brackets.md`, `vault/wiki/estimates/estimate-clean-branch-refuses-a-draft-core-page.md`, `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`, `vault/wiki/estimates/estimate-clean-branch-code-holds-pointers-only-in-brackets.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/brief.md`. The Estimate of the pages reads the pages under `vault/`, which `--check` does not judge. Its `method` still names no `--allow-draft`, and by the person's answer this Case does not change it, so that defect stays open. The Estimate of the draft refusal and the Estimate of the clean copy set what the folder build does, and this Case does not change that. `rule-clean-branch` says that `--review` lists the brackets and that `--check` judges in place, and neither sentence ties `--review` to a folder, so both stand. The `brief.md` hit is not read. No test under `.guppi/tests/` reads this Estimate page live. The ledger of this session holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> The reading of the clean code, as its `method` and its Criterion write it, exits 1 and writes nothing while any page with `core: true` stands `draft`.

> **recommend:**
> - **How the reading of the clean code runs while a core page stands draft**
>   - Recommended: (c) read by `guppi ship --check --review` in the `method` and in the `When`.
>   - Answer: agreed, (c).
> - **Whether the Estimate of the pages gets the same fix**
>   - Recommended: (a) this Case changes only the Estimate of the code.
>   - Answer: agreed, (a).

> **given:**
> `estimate-clean-branch-code-holds-pointers-only-in-brackets`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/ship.py`: the command `guppi ship`, whose `--check` and `--review` the reading runs.
> **＋** `.guppi/guppi/` and `.guppi/tests/`: the code and the tests the reading judges.
> **＋** `.guppi/tests/test_casecheck.py`: the test whose docstring and comment the reading reads.
> **＋** `.claude/` and `CLAUDE.md`: the harness files the run also judges, outside this promise.
> **＋** `rule-retro`: sets Retro and what a red check of the handoff is.

> **when:**
> At Retro of the session, `uv run --project .guppi guppi ship --check --review` of `.guppi/guppi/ship.py` judges the working tree in place and writes no folder.

> **then:**
> It prints no line on a pointer outside its bracket in a file under `.guppi/guppi/` or `.guppi/tests/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`, a bare case number in a comment or a docstring included.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
> **＋** In `.guppi/tests/test_casecheck.py`, the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)` name the made-up Case of the test as the sibling Case, with no number.
> **－** A page with `core: true` that stands `draft` does not stop the run, and no tag `prod-x.y.z` is needed.
> **－** A rewording of a comment or a docstring in those files that moves a pointer into its bracket changes no other line, and `uv run --project .guppi guppi test` has no failing test that it did not have before the change.
> **－** A line of the run on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `uv run --project .guppi guppi check` it makes is a note for the handoff by `rule-retro`.

```then
update:
- slug: estimate-clean-branch-code-holds-pointers-only-in-brackets
  set:
    status: pending
    method: 'by hand, at Retro: the lines of uv run --project .guppi guppi ship --check --review over the working tree on .guppi/guppi/, .guppi/tests/, Makefile, pyproject.toml and .gitattributes, read against the Criterion'
  change: 'the Criterion replaced whole — the reading runs by guppi ship --check --review, which no draft page with core: true stops'
```

```tasks
- [ ] update `estimate-clean-branch-code-holds-pointers-only-in-brackets`
- [ ] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`
```

## Case 929 — The test command names the folder of the tests of GUPPI

> **context:**
> `uv run --project .guppi guppi test` runs each command of the key `test` of `guppi.toml` in the folder of the project, with no shell between (`run` and `run_test` of `.guppi/guppi/commands.py`, read whole). The key holds `uv run --project .guppi pytest -q`, with no folder. `uv run --project` does not change the working folder: the uv CLI reference (https://docs.astral.sh/uv/reference/cli/) says of `--project` that other arguments are resolved relative to the current working directory, and that `--directory` changes it. The pytest documentation (https://docs.pytest.org/en/stable/reference/customize.html) says that with no arguments pytest collects below the current folder and looks for its settings file there and upwards, and that a `pyproject.toml` matches when it holds a `[tool.pytest]` or `[tool.pytest.ini_options]` table; the pytest reference (https://docs.pytest.org/en/stable/reference/reference.html) gives `".*"` in the default of `norecursedirs` and says `testpaths` is used only when no folder, file or test id is given. So in a project that installs GUPPI, which has no root `pyproject.toml` of GUPPI, the command never reaches `.guppi/tests/`: it collects nothing, or the person's own tests under the person's own root settings. This was read in the documentation and not run. In the repository of GUPPI the command works only because the root `pyproject.toml` sets `testpaths = [".guppi/tests"]` and the `live` marker; the brief reports the last run, `uv run --project .guppi guppi test`: 1803 passed, 6 skipped, 1 deselected. With the folder given, pytest starts its search in `.guppi/tests` and finds `.guppi/pyproject.toml`, which holds `[tool.pytest.ini_options]` with the `live` marker and `addopts = '-m "not live"'`, whatever the root holds.
> This takes up the two defers of `rule-guppi-package`: case 834 (whether pytest collects `.guppi/tests/` from the root of a project with no root `pyproject.toml`; it does not, and this Case fixes it) and case 848 (whether the root `pyproject.toml` keeps its pytest settings until the Case that removes it; it does, since the `test` target of the `Makefile` still runs a bare `uv run --project .guppi pytest -q` that reads them). The root `pyproject.toml` and `uv.lock` stay, as the Purpose of `rule-guppi-package` sets them; a later Case removes them. Case 927 does not change the `Makefile`; it changes only the `method` of an Estimate that names its targets.
> The promise is checked by `estimate-guppi-config-runs-the-test-and-style-commands`: its Criterion names the old command of the key `test`, so this Case replaces it whole and adds the line on the folder; its `purpose` and `method` are set anew. The old `method` said "a Grep of make with the targets test and style", and `MAKE_TARGET` of `.guppi/guppi/lint.py`, `` `?make ([\w-]+)`? ``, reads `with` there as a target, the misreading that Case 927 fixes on `estimate-harness-make-runs-in-both-shells`; the new `method` names `make test` and `make style`, so the first match is `test`, which the `Makefile` holds (a finding of `/pre-spec`). `ships` of `.guppi/guppi/ship.py` still leaves the Estimate out of the clean copy for that match, as Case 927 leaves its own, since the copy holds no `Makefile`. Its sibling `estimate-guppi-config-fills-the-languages` speaks of the languages and stands. The Estimates of `rule-guppi-package` stand: `estimate-guppi-package-runs-from-its-own-folder` speaks of `uv run --project .guppi pytest`, still the head of the new command, and `estimate-guppi-package-is-ready-after-the-install` speaks of the steps of the install, which it stays open for at line A1 of the Frontier. A Grep for `pytest -q"|pytest -q`|pytest -q\]` over `vault/wiki/`, `.claude/`, `.guppi/guppi/`, `.guppi/tests/` and `.github/` printed three files: `rules/rule-guppi-config.md` and `estimates/estimate-guppi-config-runs-the-test-and-style-commands.md`, which this Case changes, and `estimates/estimate-guppi-tests-green.md`, whose When says that `guppi test` runs `uv run --project .guppi pytest -q` over `.guppi/tests/`; that stays true of the new command, and its promise is a green suite, so it stands. A Grep for `guppi\.toml` over `.guppi/tests/` printed seven files: `test_ship.py`, `test_render.py`, `test_case_schema.py`, `test_casecheck.py`, `test_prespec.py`, `test_commands.py` and `test_config.py`; at each hit read, the test writes its own `guppi.toml` under a temporary folder, so no test reads the live file. `.guppi/tests/test_guppi_package.py` reads the live pages for `uv run pytest` and for a path `tests/` outside `.guppi/`; the new texts hold neither. The new test runs pytest over a project it writes and makes no judgment of a text, so it adds no second copy of one. The ledger of the session holds no `error` lesson.

> **problem:**
> In a project that installs GUPPI, `guppi test` runs pytest from the root of the project with no folder, so pytest never reads `.guppi/pyproject.toml` and never collects `.guppi/tests/`; two defers of `rule-guppi-package` still wait on this.

> **recommend:**
> - **What this Case changes**
>   - Recommended: (a) the key `test` of `guppi.toml` becomes `uv run --project .guppi pytest -q .guppi/tests`; the root `pyproject.toml` and `uv.lock` of the repository of GUPPI stay for a later Case; both defers close, the second with the answer that the root file keeps its pytest settings until then.
>   - Answer: agreed, (a).

> **given:**
> `rule-guppi-config`: its Render, `guppi.toml`, sets the key `test` to `uv run --project .guppi pytest -q .guppi/tests`.
> **＋** `rule-guppi-package`: the rule whose two defers this Case takes up, and which names why the command names the folder.
> **＋** `estimate-guppi-config-runs-the-test-and-style-commands`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/commands.py`: `guppi test` and `guppi style`, which run the commands in the folder of the project.
> **＋** `.guppi/pyproject.toml`: the pytest settings of the tests of GUPPI.
> **＋** `.guppi/tests/test_commands.py`: the tests of `guppi test`, which gain the test of the folder.
> **＋** `.github/workflows/checks.yml`: the CI whose jobs `test` and `style` run the two commands.
> **＋** `.claude/`: the harness files, which call the tests and the style check by the two commands.

> **when:**
> Someone runs `uv run --project .guppi guppi test` or `uv run --project .guppi guppi style` in a project, as `rule-guppi-config` sets it: by hand, in Work Mode, in Retro, or in the jobs `test` and `style` of `.github/workflows/checks.yml`.

> **then:**
> It reads the list of commands of the key `test`, or of the key `style`, from `guppi.toml` at the root of the project.
> **＋** It runs each command of the list in order, in the folder of the project and with no shell between, each one even after a red one.
> **＋** The output of each command reaches the person whole, and no command gets the stdin of `guppi test` or `guppi style`.
> **＋** A single red command makes the run red; the run is green only when all the listed commands pass.
> **＋** In this repository, the key `test` holds `uv run --project .guppi pytest -q .guppi/tests`, and the key `style` holds `uv run --project .guppi ruff check .` and `uv run --project .guppi ruff format --check .`.
> **＋** That command of `test` runs the tests of `.guppi/tests/` with the settings of `.guppi/pyproject.toml`, the tests marked `live` left out, whether the root of the project holds a `pyproject.toml` of its own or none.
> **＋** The rules, entities and Estimates of the vault and the harness files of `.claude/` call the tests and the style check by these two commands, and never by make.
> **－** When `guppi.toml` is missing or holds no such key, it prints one line that names the file and the key, runs nothing and exits 1.
> **－** The render reads `documentation_lang` and `chat_lang` as before, and a key `test` or `style` does not stop it.

```then
update:
- slug: rule-guppi-config
  replace:
  - old: test = ["uv run --project .guppi pytest -q"]
    new: test = ["uv run --project .guppi pytest -q .guppi/tests"]
  change: the key test names the folder .guppi/tests, so pytest reads the settings of .guppi/pyproject.toml in any project
- slug: rule-guppi-package
  replace:
  - old: and the tests as `uv run --project .guppi pytest`.
    new: 'and the tests as `uv run --project .guppi pytest`. The key `test` of `guppi.toml` names the folder `.guppi/tests`, since pytest looks for its settings only in the folder it starts in and the folders above it, and skips a folder whose name starts with a dot: so it reads the settings of `.guppi/pyproject.toml` whatever the root of the project holds (as set in case 929).'
  change: 'taken up: the test command names .guppi/tests, so pytest finds the tests of GUPPI with no root pyproject.toml; the root pyproject.toml of the repository of GUPPI keeps its pytest settings until the Case that removes it'
- slug: estimate-guppi-config-runs-the-test-and-style-commands
  set:
    status: pending
    purpose: Whether guppi test and guppi style run the commands that the keys test and style of guppi.toml list, in order and each after a red one, exit non-zero when any is red, and exit 1 with one line when the file or the key is missing; and whether the command of the key test runs the tests of .guppi/tests with the settings of .guppi/pyproject.toml whatever the root of the project holds
    method: 'uv run --project .guppi pytest .guppi/tests/test_commands.py; by hand, after the librarian''s run that renders guppi.toml with the key test that names .guppi/tests: uv run --project .guppi guppi test and uv run --project .guppi guppi style in this repository, and a Grep for make test and make style over the live rules, entities and Estimates and over .claude/, read against the Criterion'
  change: the Criterion replaced whole — the key test names .guppi/tests, and its command runs those tests with the settings of .guppi/pyproject.toml whatever the root holds
```

```tasks
- [ ] update `rule-guppi-config`
- [ ] `uv run --project .guppi guppi render`: `guppi.toml`
- [ ] update `rule-guppi-package`
- [ ] update `estimate-guppi-config-runs-the-test-and-style-commands`
- [x] `.guppi/tests/test_commands.py`: a test writes a project with no root `pyproject.toml`, a `.guppi/pyproject.toml` with the pytest settings of `.guppi/pyproject.toml` (`testpaths`, the `live` marker, `addopts`) and `.guppi/tests/` with one plain test and one `live` test, runs pytest by `sys.executable -m pytest -q .guppi/tests` in the folder of that project, and asserts one passed and one deselected; a second run, with a root `pyproject.toml` that holds other pytest settings, answers the same.
- [ ] read `estimate-guppi-config-runs-the-test-and-style-commands`
```

## Case 931 — A page update drops a section

> **context:**
> `guppi generate` applies a page `update` by its keys `set`, `sections`, `replace`, `reword`, `change` and `rename`. None of them removes a section: `Generator.update` of `.guppi/guppi/generate.py` sets a named section's text, and `body` of the same module writes a section with no text as a bare heading. The schema of rules says a Leaf that still carries `## How it works` keeps it until its next touch, when the section leaves, but no form of an `update` makes it leave. Case 792 asked for such a form and was put off by case 793 when Case 787.2 could only change one sentence of that section on `rule-git-context`; case 897.3 took the put-off up and put it off again, and `rule-page-generation` holds it in `deferred_by`. A Grep of `^## How it works` over `vault/wiki` printed 15 rule pages; 11 of them are Leafs. The person chose a new `update` key, `drop`, with a list of section names, joined to `ITEM_KEYS` of `.guppi/guppi/materialize.py`, the one list of update keys: `_lift_item` copies each key of it into the entry, `item_keys` gives it for an `update`, and `put` of `.guppi/guppi/ratified.py` reads a sub-point whose value opens with `[` as a YAML list, so a sub-point `drop` reaches the entry with no other change to the reader. A name the page does not carry fails the entry, as a `replace` that misses does. A section that the schema of the page's category requires fails the entry too. That judgment already stands in `check_schema` of `.guppi/guppi/lint.py`, with `unmet_conditions`, `holds` and `load_schema`, which I read whole: it reports each section of `body.required` the page lacks, and each `required` section of a `conditional` of `body` whose `when` holds on the page's fields, such as `## Render` on a rule with `enforcement: render`. `generate.py` already imports from `lint.py`, so the task runs `check_schema` over the page with the section and without it, and adds no second copy of the judgment; `lint.py` does not change, which keeps Case 927 true, whose `then` says `lint.py` does not change. The key cannot be used in this session, since the check of a Case file runs the code that stands before Work Mode; the 11 Leafs keep the section until a later Case drops it, so the schema sentence on the next touch stands, now with a form behind it. A Grep of `next touch` over the repository outside `vault/raw` and `vault/archive` printed `vault/wiki/rules/rule-rules-schema.md` and `vault/wiki/rules/schema.yaml`; both say the section leaves at the next touch, which this Case makes possible, so both stand. The change is checked by `estimate-generate-writes`, which states what an `update` writes; its last line says a section the entry does not name under `sections` or reach by `replace` is not touched, which `drop` makes false, so its Criterion is replaced whole under `sections.Criterion`, with the lines of this Case's `then` in it; its `purpose` and `method` stand. The other Estimates of `rule-page-generation` speak of reword, rename, ticks, the cascade, the Decision page, dates, the leading indent and the failure of an entry in general, and stand. A Grep of `` `rename` `` over `vault/wiki` printed 11 files: `glossary.md`, `case-schema.md`, `entity-glossary.md`, `rule-page-generation.md`, `rule-case-protocol.md`, `rule-decisions-schema.md`, `rule-materialize.md`, `estimate-generate-renames.md`, `estimate-materialize-assembles.md`, `estimate-prespec-requires-a-task-line.md` and `estimate-spec-write-copies-the-ratified-case.md`. The pair on `rule-case-protocol` stands in one sentence of its Render, which I read whole: it names each key an `update` holds, `set`, `sections`, `replace`, `reword`, `change` and `rename`, each with its rule, and the pair adds `drop` with its rule between `change` and `rename`. The second pair, asked by a finding of `/pre-spec`, stands in the sentence of the same Render that I read whole: the Spec keeps its form, and the hook of `rule-spec-write` reads the chat form, a task line of a kind and a slug being an item and its sub-points its keys, each value one code span or a fenced block; the pair adds `drop` to that list of sub-point keys, which `put` reads as a YAML list. Cases 927 and 928 write into neither page this Case changes. The later sentence of that paragraph, that an `update` naming a part alone, such as a `replace` pair or a section other than `Criterion`, carries no `set.status`, stands: a `drop` is such a part, and a `drop` of `Criterion` fails, since the schema of Estimates requires it. The new Criterion of `estimate-generate-writes` carries each line of the old one word for word but two: the line that a section the entry does not name under `sections` or reach by `replace` is not touched now names `drop` beside `sections`, since a `drop` touches a section it names; and the line that an `update` of an Estimate whose `set` carries `method` drops no section now says that such a `set` removes no section by itself, as a finding of `/pre-spec` asked, since an item that carries both `set.method` and `drop` removes the sections `drop` names, and the old word "drops" would clash with the key; it adds the lines of this Case's `then` on `drop`, after the line on what an `update` applies and among the `－` lines. Of the other files the Grep of `` `rename` `` printed, each stands: the glossary row and `entity-glossary.md` name the kinds of decision, not every key; `rule-materialize.md` and `estimate-materialize-assembles.md` list keys the lift carries, and Case 935, whose finished file I read whole, adds `drop` to both in Case 935.1; its Case 935.2 makes `drop` a named part of an Estimate `update` and marks one whose `drop` names `Criterion` as `incomplete: [criterion]` at the lift, which agrees with this Case, where `generate` fails such a `drop` since the schema of Estimates requires `## Criterion`, and its tasks run after this Case adds `drop` to `ITEM_KEYS`, as its `context` says: by the person's choice the promise that the lift carries `drop` stands on `estimate-materialize-assembles` alone, so this Case keeps no line of it in its `then` or in the Criterion of `estimate-generate-writes`, and keeps the change of `ITEM_KEYS` in its tasks, since `Generator.update` reads that list; `estimate-spec-write-copies-the-ratified-case.md` refuses only a sub-point outside `item_keys`, which will hold `drop`; `rule-decisions-schema.md`, `estimate-generate-renames.md` and `estimate-prespec-requires-a-task-line.md` speak of `rename` alone. A Grep of `rule-page-generation|estimate-generate-writes|ITEM_KEYS|item_keys` over `.guppi/tests` printed `test_materialize.py`, `test_generate.py` and `test_prespec.py`; none reads a live page, and `test_item_keys_answers_for_each_kind_as_the_lift_does` of `test_materialize.py` asserts the set of update keys, which a task changes. The update of `rule-page-generation` carries `{supersedes:case 897.3}`, which clears the put-off and closes the backlog line; as with cases 793 and 839, which case 897.3 superseded, the Decision page of case 897.3 becomes `superseded`. The session's ledger holds no `error` lesson. By the sentence of the prompt, Case 929 changes `rule-guppi-config`, the defers of `rule-guppi-package` and `estimate-guppi-config-runs-the-test-and-style-commands`, no page this Case changes; Cases 929 and 932 are built at the same time as this one, and I read no file of them.

> **problem:**
> No form of a page `update` removes a section, so a Leaf rule cannot lose `## How it works` at its next touch without an edit by hand, and `rule-page-generation` carries the put-off of that form.

> **recommend:**
> - **What does this Case do with the put-off?**
>   - Recommended: (a) a new update key that names the sections to remove.
>   - Answer: (a).
> - **Which sections may the new key remove?**
>   - Recommended: (a) any section except the ones the page's schema requires.
>   - Answer: agreed, (a).
> - **What happens when a named section is not on the page?**
>   - Recommended: (a) the entry fails.
>   - Answer: agreed, (a).
> - **How is the new key checked?**
>   - Recommended: (b) the Criterion of `estimate-generate-writes` replaced as a whole.
>   - Answer: agreed, (b).
> - **What is the key called?**
>   - Recommended: (a) `drop`.
>   - Answer: agreed, (a).
> - **Where does the promise that the lift carries `drop` stand?**
>   - Recommended: (b) a new Case beside Case 931 carries the lift.
>   - Answer: agreed, (b).

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, which carries the put-off.
> **＋** `estimate-generate-writes`: the Estimate of what an `update` writes; its Criterion is replaced whole.
> **＋** `rule-case-protocol`: its Render, `vault/wiki/case-schema.md`, lists what an `update` holds.
> **＋** `.guppi/guppi/generate.py`: `Generator.update` applies the new key.
> **＋** `.guppi/guppi/materialize.py`: `ITEM_KEYS`, the one list of update keys.
> **＋** `.guppi/guppi/lint.py`: `check_schema`, the judgment of the sections a schema requires.
> **＋** `.guppi/guppi/ratified.py`: the `Stop` hook of `rule-spec-write`, which reads the sub-points of a task line.
> **＋** `.guppi/tests/test_generate.py`, `.guppi/tests/test_materialize.py` and `.guppi/tests/test_ratified.py`: the tests of the new key.

> **when:**
> `guppi generate` applies an `update` entry whose item carries `drop`, a list of section names, to a page.

> **then:**
> Each section that `drop` names leaves the page, its heading and its text, and the page gets the History line `updated: <change>`; an item that carries `drop` alone applies.
> **－** A name of a section the page does not carry fails the entry alone, with the name on stderr, and nothing of `set`, `sections`, `replace` or `drop` of the item is written to the page.
> **－** A name of a section that the schema of the page's category requires of the page fails the entry the same way: `check_schema` of `.guppi/guppi/lint.py`, run over the page with the section and without it, gives a finding without it that it does not give with it.
> **－** A section that `drop` does not name is not touched.

```then
update:
- slug: rule-page-generation
  replace:
  - old: too (as set in case 819). One bad
    new: too (as set in case 819). An `update` whose item carries `drop`, a list of section names, removes each named section, its heading and its text; a name the page does not carry, or a section that the schema of the page's category requires of the page, fails the entry, and nothing of the item is written to the page (as set in case 931). One bad
  change: an update drops a named section, heading and text; a section the page lacks or its schema requires fails the entry; the put-off of case 897.3 taken up
- slug: estimate-generate-writes
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      `guppi generate` applies one entry of a yaml to a page.

      Then:
      A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the `sprint` of the yaml, which `guppi materialize` takes from the first `## <id>` of `sprint.md` or, in a unit whose ledger creates `entity-sprint-<id>`, from that `<id>`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
      **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`, and `deferred_by` after `checked` once a `defer` marks it; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
      **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
      **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
      **＋** An `update` whose item carries `drop`, a list of section names, removes each section it names from the page, its heading and its text; an item that carries `drop` alone applies.
      **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
      **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
      **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
      **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight, estimate) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by` for a rule or an entity only.
      **＋** The folders whose page takes `deferred_by` are `DEFERRABLE` of `.guppi/guppi/materialize.py`, which `.guppi/guppi/generate.py` imports; they are the folders whose `schema.yaml` under `vault/wiki/` lists `deferred_by`.
      **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
      **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
      **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
      **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
      **－** A name under `drop` of a section the page does not carry fails the entry alone (`estimate-generate-fails-alone`), with the name on stderr, and nothing of `set`, `sections`, `replace` or `drop` of the item is written to the page.
      **－** A name under `drop` of a section that the schema of the page's category requires of the page fails the entry the same way: `check_schema` of `.guppi/guppi/lint.py`, run over the page with the section and without it, gives a finding without it that it does not give with it.
      **－** A `defer` of a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, whether its page stands or not, changes no page and appends nothing to `vault/wiki/log.md`: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it` on stderr.
      **－** A `defer` of an Estimate or an Insight whose page stands neither under `vault/wiki/<category>/` nor in a folder `<category>` under `vault/archive/` outside a `raw/` folder, by `defer_writes_no_page` of `.guppi/guppi/materialize.py`, which asks `has_page`, writes no page: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: an Estimate is deferred only with its page — defer the page it would check` on stderr for an Estimate, and `generate: <slug>: a placeholder is written only for a rule or an entity — defer a page that stands` for an Insight.
      **－** No body section is derived from a ref field; a section the entry does not name under `sections` or `drop`, or reach by `replace`, is not touched.
      **－** The `set` of an `update` of an Estimate that carries `method` removes no section by itself.
      **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).
  change: the Criterion replaced whole — an update drops a named section, and a section the page lacks or its schema requires fails the entry
- slug: rule-case-protocol
  replace:
  - old: '`change` (one line for History) and, when the page changes its slug, `rename`'
    new: '`change` (one line for History), `drop` (a list of section names, each removed with its heading and its text; a name the page does not carry, or a section that the schema of the page''s category requires of the page, fails the entry) and, when the page changes its slug, `rename`'
  - old: '`set`, `change`, `rename`, `sections.<Name>`, the fields of a `create`'
    new: '`set`, `change`, `rename`, `drop`, `sections.<Name>`, the fields of a `create`'
  change: an update holds drop, a list of sections to remove, and the hook of rule-spec-write reads it as a sub-point
```

```tasks
- [ ] update `rule-page-generation`
- [ ] update `estimate-generate-writes`
- [ ] update `rule-case-protocol`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
- [x] `.guppi/guppi/materialize.py`: `drop` joins `ITEM_KEYS["update"]`, and the comment above it names it.
- [x] `.guppi/guppi/generate.py`: `Generator.update` applies `drop` after `set`, `sections` and `replace` of the item and before `save`; for each name it fails the entry with `generate: <slug>: drop: <name> is not on the page`, or with `generate: <slug>: drop: <name> is required by the schema`, when `check_schema` of `.guppi/guppi/lint.py`, imported with `load_schema`, gives over a copy of the page without the section a finding it does not give over the page; a failure returns before `save`. The module docstring names `drop` beside `replace`.
- [x] `.guppi/guppi/ratified.py`: the docstring that lists the sub-points of an item names `drop`.
- [x] `.guppi/tests/test_generate.py`: tests that a `drop` of `How it works` on a Leaf removes the heading and the text and writes History `updated: <change>`; that an item with `drop` alone applies; that a name the page lacks fails the entry and leaves the page as it was; that `drop` of `Purpose` on a rule, of `Render` on a rule with `enforcement: render`, and of `Criterion` on an Estimate each fail the entry; that `drop` of `Render` on a rule with `enforcement: check` applies.
- [x] `.guppi/tests/test_materialize.py`: `test_item_keys_answers_for_each_kind_as_the_lift_does` holds `drop` among the update keys.
- [x] `.guppi/tests/test_ratified.py`: a test that `read_tasks` reads a sub-point `drop` with the value `[How it works]` of an update item into the list `["How it works"]`, with no error.
- [ ] read `estimate-generate-writes`
```

## Case 932 — An existing project sets its own files aside to install GUPPI

> **context:**
> `/guppi:install` copies the files of GUPPI into the project open in Claude Code. Today, step 3 of its skill, `plugin/skills/install/SKILL.md`, lists each file of the install that already stands in the project, writes nothing and stops. So a project with its own `CLAUDE.md` or `.claude/settings.json` cannot install GUPPI at all. Case 911 put this off with the words that it lets GUPPI install into an existing project that holds its own settings, hooks and `CLAUDE.md`. A plain copy over those files is no answer. `CLAUDE.md` and `.claude/settings.json` are rendered whole from the rule pages `rule-claude-md` and `rule-settings`, so any extra text of the project there is lost at the first render. `rule-claude-md` keeps any line nobody ratified out of the system prompt, and `rule-hook-registry` keeps any hook from being registered by hand. The settings documentation of Claude Code (https://code.claude.com/docs/en/settings) names one shared project file, `.claude/settings.json`, and a personal `.claude/settings.local.json` that stays out of git, so the settings of a project cannot move to a second shared file. The memory documentation (https://code.claude.com/docs/en/memory) says that a `CLAUDE.md` in a subfolder loads on demand when Claude works with files there, so the set-aside files take `.set-aside` on their names, which no file of Claude Code carries.
> The person chose that the install sets the clashing files aside and that the setup Case of `rule-morph` takes them in at the first `/hi`. Case 932.1 changes the install, and Case 932.2 changes the setup Case. The setup step of `rule-morph` is not built yet. As the Purpose of `rule-clean-branch` sets it, `guppi ship` writes nothing while a page with `core: true` stands `draft`, and `rule-morph` is such a page. So no project gets this install from the branch `prod` before the setup step is built, and the person chose no temporary step for installs by hand. The take-in also covers `.gitattributes` and `.github/workflows/checks.yml`. A Grep for `^governs:.*(\.gitattributes|checks\.yml)` over `vault/wiki/` printed nothing, and a Grep for `^(code_ref|implementation_ref|governs):.*(gitattributes|checks\.yml|\.github)` over `vault/wiki/` printed `rules/rule-clean-branch.md` and `rules/rule-github-repository.md`, whose `implementation_ref` lists `.github/workflows/checks.yml` as code. No page renders those two files, so a task of the setup Case writes a kept part into them.
> Of the Estimates of `rule-plugin-install`, two promise the refusal in a `－` line: `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-plugin-install-runs-no-hook-before-uv-sync`. Cases 932.3 and 932.4 replace each Criterion whole without that line, and add a `－` line that a file of the project at a path of the install is no part of its promise; the person chose two parts, and the check of the case file asked that these two Criteria stand in sub-cases of their own, since each is a promise of its own. The purpose of the first names the refusal, and its method reads a second project with a `CLAUDE.md` of its own, so both are set anew. Its When and Then name `guppi ship --allow-draft <folder>`, since `rule-clean-branch` sets it that `guppi ship <folder>` writes nothing while a page with `core: true` stands `draft`, and its method names the tag `prod-x.y.z` that `guppi ship <folder>` needs, as that rule sets it; both were findings of `/pre-spec`. The purpose and method of the second speak of empty projects and stand. `estimate-plugin-install-offers-to-install-uv` and `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` speak of an empty project, where nothing is set aside, and stand. The new Estimate of Case 932.1 checks the undo for a project with files set aside. In `estimate-morph-sets-up-the-project-at-the-first-hi`, the purpose and the `－` line say that the settings change only by the copy of `/guppi:install` and the render, and the setting aside of the project's `.claude/settings.json` is a move, not a copy; a finding of `/pre-spec` named it, so Case 932.5 replaces its Criterion whole with the setting aside beside the copy and sets its purpose anew, and its method, which waits for the build of the setup step, stands. Its line that the setup step reads no code of the project stands too, since the set-aside files are instructions and settings, not the code of the project. In the Purpose of `rule-morph`, the sentence that no settings file changes but by the copy of `/guppi:install` and the render would be made false by the setting aside, so Case 932.2 rewords it. A Grep for `guppi:install` over `vault/wiki/` printed `log.md`, `brief.md`, `sprint.md`, `entities/entity-sprint-plugin.md`, `lessons/lesson-hi-fails-outside-a-git-repository.md`, `lessons/lesson-plugin-install-hooks-of-the-copy-run-at-once.md`, `estimates/estimate-clean-branch-writes-the-session-files.md`, `rules/rule-plugin-install.md`, `rules/rule-morph.md`, `estimates/estimate-git-context-offers-git-init.md`, `estimates/estimate-guppi-package-is-ready-after-the-install.md`, `estimates/estimate-morph-sets-up-the-project-at-the-first-hi.md`, `estimates/estimate-sprint-plugin-installs-as-a-plugin.md` and the four Estimates of `rule-plugin-install`. Beside the pages this Case changes, the Estimates there speak of an empty project and stand; the two lessons record past events and were not read. The line of `entity-sprint-plugin` lists what remains of `rule-morph`, the setup skill among it, and stands. A Grep for `plugin/skills/install|rule-plugin-install|rule-morph|estimate-plugin-install|estimate-morph` over `.guppi/tests/` printed `test_ship.py`, whose hit is a sample string of an error, so no test reads these texts live. A Grep for `guppi-set-aside` over the repository outside `vault/raw/` printed nothing, so no step reads that folder yet. The new slugs are free: a Glob for each over `vault/wiki/**` printed nothing. Case 932.1 carries `{supersedes:case 911}`, the one defer of `rule-plugin-install`. The ledger of the session holds no `error` lesson.

> **problem:**
> `/guppi:install` refuses a project that already holds its own `CLAUDE.md`, `.claude/settings.json` or another file of the install, so GUPPI cannot install into an existing project. Its files cannot simply be joined to GUPPI's, since the render writes those files whole from ratified pages.

> **recommend:**
> - **What the install does in a project that already holds its own files**
>   - Recommended: (c) the install sets the clashing files aside, and the person brings back what they need by ordinary Cases later.
>   - Answer: (b) the install sets the files aside, and the setup Case at the first `/hi` shows what they hold, for the person to keep or drop each part. The person first chose (c), asked how the process would go, and then changed the answer to (b).
> - **How the first `/hi` learns of the set-aside folder**
>   - Recommended: (b) the install writes one line about the folder into the brief it copies.
>   - Answer: not answered; the round that asked it was never shown to the person, since the person changed the answer to the first question, and **Where a kept part of a set-aside file lands** and **What happens until the setup step is built** replaced it.
> - **Which clashing files the install sets aside**
>   - Recommended: (c) `CLAUDE.md`, the files under `.claude/`, `.gitattributes` and `.github/workflows/checks.yml`; a clash under `vault/` or `.guppi/` still stops the install.
>   - Answer: agreed, (c).
> - **Where the set-aside files go**
>   - Recommended: (b) the folder `guppi-set-aside/` at the root, each file under its old path with `.set-aside` added to its name.
>   - Answer: agreed, (b).
> - **When the project's own `.claude/settings.json` is set aside**
>   - Recommended: (a) just before GUPPI's copy, after `uv sync` passes.
>   - Answer: agreed, (a).
> - **Where a kept part of a set-aside file lands**
>   - Recommended: (a) into the pages of GUPPI that already write that file; the setup Case creates no page.
>   - Answer: agreed, (a).
> - **What happens to the set-aside folder after the setup Case**
>   - Recommended: (a) a task of the setup Case deletes it in the Work Mode of the same session.
>   - Answer: agreed, (a).
> - **What happens until the setup step is built**
>   - Recommended: (a) nothing extra, since the published version waits for the setup step anyway.
>   - Answer: agreed, (a).
> - **How the Case is checked**
>   - Recommended: (a) two parts, each with a new check, and the refusal lines of the two checks of the install rewritten.
>   - Answer: agreed, (a).
> - **Where a kept part lands when no page writes its file**
>   - Recommended: (a) the setup Case holds a task that writes the kept part into GUPPI's copy of that file, run in the Work Mode of the same session.
>   - Answer: (a).

### Case 932.1 — The install sets aside the files of the project that clash

> **given:**
> `rule-plugin-install`: its Purpose and its Render set what the install does with a file of the project at a path of the install.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install`, which the Render writes.
> **＋** `estimate-plugin-install-sets-aside-the-files-of-the-project`: the new check of the setting aside.
> **＋** `.claude/`: the folder whose files of the project the install sets aside.
> **＋** `.claude/settings.json`: the settings file, which the install sets aside only after `uv sync` passes.
> **＋** `.github/workflows/checks.yml`: a file of the project that the install sets aside.
> **＋** `guppi-set-aside/`: the folder that holds the set-aside files.
> **＋** `/hi`: the first session after the install, where the person keeps or drops the set-aside files.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in a project open in Claude Code, where `uv --version` passes, that holds a `CLAUDE.md`, a `.claude/settings.json` and a `.gitattributes` of its own and no other file of the install.

> **then:**
> Before it copies, the agent moves each file of the project at a path of the install that is `CLAUDE.md`, a file under `.claude/` but `.claude/settings.json`, `.gitattributes` or `.github/workflows/checks.yml` into `guppi-set-aside/`, under its old path with `.set-aside` added to its name.
> **＋** It moves the `.claude/settings.json` of the project into `guppi-set-aside/` the same way only after `uv sync` passes, just before it copies the `.claude/settings.json` of GUPPI.
> **＋** Its last message lists each file it set aside with its path under `guppi-set-aside/`, and says that none of them loads or runs until the person keeps or drops it at the first `/hi`.
> **＋** When `uv sync` fails, it deletes what it copied, moves each file it set aside back to its old path and deletes `guppi-set-aside/`, so that the project holds only what it held before.
> **－** It changes no text of a file it sets aside, and sets aside no file at a path that the install does not write.
> **－** In a project that holds a file of the install at any other path, or that already holds `guppi-set-aside/`, it lists them, writes and moves nothing, and stops.
> **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.

```then
create:
- slug: estimate-plugin-install-sets-aside-the-files-of-the-project
  ref: rule-plugin-install
  kind: QA
  purpose: Whether /guppi:install moves each file of the project at a path of the install that is CLAUDE.md, a file under .claude/, .gitattributes or .github/workflows/checks.yml into guppi-set-aside/ with .set-aside added, the settings file only after uv sync passes, lists them in its last message, puts them back when uv sync fails, and stops on a clash at any other path
  method: 'by hand, after the librarian''s run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in a project that holds a CLAUDE.md, a .claude/settings.json with a hook and a .gitattributes of its own, /guppi:install typed; in a second such project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, /guppi:install typed; in a third project with a file under vault/ of its own, /guppi:install typed; the transcripts and the files of the three projects before and after read against the Criterion'
  tags:
  - plugin
  - harness
update:
- slug: rule-plugin-install
  replace:
  - old: It writes nothing when one of those files already stands in the project, and it runs no `guppi` and no `git` command.
    new: Where the project already holds a file at one of those paths that is `CLAUDE.md`, a file under `.claude/`, `.gitattributes` or `.github/workflows/checks.yml`, it moves that file of the project, its text unchanged, to the same path under the folder `guppi-set-aside/`, with `.set-aside` added to its name, such as `guppi-set-aside/CLAUDE.md.set-aside`, so that Claude Code loads and runs none of it. It writes and moves nothing when the project holds a file of the install at any other path, such as under `vault/` or `.guppi/`, or already holds `guppi-set-aside/` (as set in case 932.1). It runs no `guppi` and no `git` command.
  - old: and none runs after a failed `uv sync` (as set in case 912).
    new: and none runs after a failed `uv sync` (as set in case 912). It sets aside a `.claude/settings.json` of the project only then, just before it copies the one of GUPPI, so that the hooks of the project run until then and a failed `uv sync` leaves that file in place (as set in case 932.1).
  - old: When `uv sync` fails, the skill shows its output, deletes each file it copied and each folder it made,
    new: When `uv sync` fails, the skill shows its output, deletes each file it copied and each folder it made, moves each file it set aside back to its old path and deletes `guppi-set-aside/`,
  - old: and [[rule-morph]] sets its settings there.
    new: and [[rule-morph]] sets its settings there. The last message of the install lists each file it set aside, and the setup Case of that first /hi shows what each holds, for the person to keep or drop each part (as set in case 932.1).
  - old: 3. Check which of those paths already stand in the project. When one or more stand, list them, say that the install writes nothing into a project that already holds one of its files, and stop. Write nothing.
    new: 3. Check which of those paths already stand in the project, and whether the folder `guppi-set-aside/` stands there. When that folder stands, or when one of those paths is not `CLAUDE.md`, a file under `.claude/`, `.gitattributes` or `.github/workflows/checks.yml`, such as a path under `vault/` or `.guppi/`, list them, say that the install writes nothing into a project that already holds them, and stop. Write and move nothing.
  - old: 4. Otherwise copy each file to its path in the project, with the folders it needs, but `.claude/settings.json`, which step 7 copies once `uv sync` passes, so that no hook of the project runs before then.
    new: '4. Otherwise set aside each of those paths that stands in the project, but `.claude/settings.json`: move the file of the project, its text unchanged, to the same path under `guppi-set-aside/`, with `.set-aside` added to its name, such as `guppi-set-aside/CLAUDE.md.set-aside`. Then copy each file to its path in the project, with the folders it needs, but `.claude/settings.json`, which step 7 copies once `uv sync` passes, so that no hook of GUPPI runs before then.'
  - old: included, so that the project holds only what it held before. Delete nothing else.
    new: included, move each file you set aside in step 4 back to its old path, and delete `guppi-set-aside/`, so that the project holds only what it held before. Delete nothing else.
  - old: 7. Copy `.claude/settings.json` from `${CLAUDE_PLUGIN_ROOT}` to its path in the project, and check that it stands.
    new: 7. When the project holds a `.claude/settings.json` of its own, move it, its text unchanged, to `guppi-set-aside/.claude/settings.json.set-aside`. Then copy `.claude/settings.json` from `${CLAUDE_PLUGIN_ROOT}` to its path in the project, and check that it stands.
  - old: 8. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`.
    new: 8. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`. When step 4 or step 7 set aside files, list each of them with its path under `guppi-set-aside/`, and say that the setup Case of the first `/hi` shows what each holds, for the person to keep or drop each part, and that until then none of them loads or runs.
  change: 'taken up: the install sets aside a CLAUDE.md, a file under .claude/, a .gitattributes or a .github/workflows/checks.yml of the project in guppi-set-aside/, the settings file only after uv sync passes, and stops only on a clash elsewhere'
```

```tasks
- [ ] update `rule-plugin-install`
- [ ] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
- [ ] create `estimate-plugin-install-sets-aside-the-files-of-the-project`
- [ ] read `estimate-plugin-install-sets-aside-the-files-of-the-project`
```

### Case 932.2 — The setup Case takes in the set-aside files

> **given:**
> `rule-morph`: its Purpose sets how the setup Case of the first `/hi` takes in the set-aside files.
> **＋** `estimate-morph-takes-in-the-set-aside-files`: the new check of the take-in.
> **＋** `rule-plugin-install`: the rule of the install.
> **＋** `/guppi:install`: the skill that sets the files of the project aside in `guppi-set-aside/`.
> **＋** `rule-claude-md`: the page that writes `CLAUDE.md`, an example of a page that writes a set-aside file.
> **＋** `guppi.toml`: its key marks the setup as done.
> **＋** `.gitattributes`: a file that no page writes.
> **＋** `.github/workflows/checks.yml`: a file that no page writes.

> **when:**
> In a project where `/guppi:install`, as `rule-plugin-install` sets it, set aside files of the project under `guppi-set-aside/`, and whose `guppi.toml` does not mark the setup of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

> **then:**
> The setup Case of `rule-morph` shows what each file under `guppi-set-aside/` holds, by its old path.
> **＋** In that one setup Case, the person keeps or drops each part of each file, such as an instruction, a hook or a permission.
> **＋** A kept part goes into the page that writes its file, such as `rule-claude-md` for an instruction of `CLAUDE.md`, and the render of the Work Mode of that session writes it into the file.
> **＋** For a file that no page writes, such as `.gitattributes` or `.github/workflows/checks.yml`, a task of the setup Case writes the kept part into that file, and the Work Mode of the same session runs it.
> **＋** A task of the setup Case deletes `guppi-set-aside/` in that Work Mode.
> **－** A dropped part reaches no file of the project.
> **－** The setup Case creates no page for a kept part.

```then
create:
- slug: estimate-morph-takes-in-the-set-aside-files
  ref: rule-morph
  kind: QA
  purpose: Whether the setup Case of the first /hi shows what each file that /guppi:install set aside holds, lets the person keep or drop each part, puts a kept part into the page that writes its file or, where none does, into the file by a task, creates no page and deletes guppi-set-aside/
  method: 'by hand, after the session whose Work Mode builds the setup skill of rule-morph and its step in /hi: in a project that holds a CLAUDE.md, a .claude/settings.json with a hook and a .gitattributes of its own, with a tag prod-x.y.z in the history of HEAD, the plugin guppi installed from a local copy written by uv run --project .guppi guppi ship --allow-draft, /guppi:install typed, Claude Code reopened and /hi typed, one part of each set-aside file kept and one dropped in the setup Case; the transcript of that session, its ledger and the files its Work Mode writes read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - harness
  - plugin
update:
- slug: rule-morph
  replace:
  - old: but by the copy of `/guppi:install` and the render that `/hi` runs
    new: but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs
  - old: as the clean version holds them ([[rule-ratification]]).
    new: as the clean version holds them ([[rule-ratification]]). Where `/guppi:install` set aside files of the project in the folder `guppi-set-aside/`, the setup Case also shows what each of them holds, by its old path, and the person keeps or drops each part of it, such as an instruction, a hook or a permission. A kept part goes into the page of GUPPI that writes its file, such as [[rule-claude-md]] for an instruction of `CLAUDE.md`, [[rule-hook-registry]] for a hook and [[rule-permissions]] for a permission, and the render writes it into the file; for a file that no page writes, such as `.gitattributes` or `.github/workflows/checks.yml`, a task of the setup Case writes the kept part into that file. A dropped part reaches no file, the setup Case creates no page for a kept part, and a task of it deletes `guppi-set-aside/` in the Work Mode of the same session (as set in case 932.2).
  change: the setup Case shows what the files that /guppi:install set aside hold; the person keeps or drops each part, a kept part goes into the page that writes its file or, where none does, into the file by a task, and guppi-set-aside/ is deleted
```

```tasks
- [ ] update `rule-morph`
- [ ] create `estimate-morph-takes-in-the-set-aside-files`
- [ ] read `estimate-morph-takes-in-the-set-aside-files`
```

### Case 932.3 — The check of an install into an empty project promises no refusal

> **given:**
> `estimate-plugin-install-writes-guppi-into-an-empty-project`: its Criterion is replaced whole by the text under `sections`.
> **＋** `/guppi:install`: the skill whose refusal of a project that holds a file of the install ends.

> **when:**
> Someone reads the Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project` to judge `/guppi:install`.

> **then:**
> Its reading still judges the clean version and the copy of `/guppi:install` into an empty project.
> **－** Its reading needs no second project with a `CLAUDE.md` of its own.

```then
update:
- slug: estimate-plugin-install-writes-guppi-into-an-empty-project
  set:
    status: pending
    purpose: Whether guppi ship puts the skill install into the clean version, and whether /guppi:install copies every file of the plugin but its own into a project that holds none of them
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, after the librarian''s run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft; in an empty project, that folder added as a catalogue by /plugin marketplace add, guppi installed by /plugin install guppi@guppi-marketplace, /guppi:install typed and the files of the project read against those of the plugin and against the Criterion'
  sections:
    Criterion: |-
      When:
      `uv run --project .guppi guppi ship --allow-draft <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
      **＋** The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in the project open in Claude Code, as `rule-plugin-install` sets it.

      Then:
      `uv run --project .guppi guppi ship --allow-draft <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
      **＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
      **＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
      **＋** In a project that holds none of the files it would write, `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/`, such as `CLAUDE.md`, `.claude/settings.json`, the code under `.guppi/` and the pages under `vault/wiki/`.
      **＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
      **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
      **－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
      **－** Which files a new project needs, what the install does about `uv` and the Python environment under `.guppi/`, and what it does with a file of the project that stands at one of its paths are no part of this promise.
  change: the Criterion replaced whole — the refusal of a project that holds a file of the install leaves it, since the install now sets such files aside
```

```tasks
- [ ] update `estimate-plugin-install-writes-guppi-into-an-empty-project`
- [ ] read `estimate-plugin-install-writes-guppi-into-an-empty-project`
```

### Case 932.4 — The check of the settings file before `uv sync` promises no refusal

> **given:**
> `estimate-plugin-install-runs-no-hook-before-uv-sync`: its Criterion is replaced whole by the text under `sections`.
> **＋** `/guppi:install`: the skill whose refusal of a project that holds a file of the install ends.

> **when:**
> Someone reads the Criterion of `estimate-plugin-install-runs-no-hook-before-uv-sync` to judge `/guppi:install`.

> **then:**
> Its reading still judges, in an empty project, that no hook runs before `uv sync` passes or after it fails.
> **－** Its Criterion keeps no line on a refusal by `/guppi:install`.

```then
update:
- slug: estimate-plugin-install-runs-no-hook-before-uv-sync
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes.

      Then:
      Until `uv sync --project .guppi` passes, the project holds no `.claude/settings.json`, so no hook of the copy runs.
      **＋** No hook of the copy has made `.guppi/.venv/` by the time `uv sync` runs.
      **＋** When `uv sync` fails, the project never holds `.claude/settings.json`, and no later command of that session shows a hook error.
      **－** What the install does with a file of the project that stands at one of its paths is no part of this promise.
  change: the Criterion replaced whole — the refusal of a project that holds a file of the install leaves it, since the install now sets such files aside
```

```tasks
- [ ] update `estimate-plugin-install-runs-no-hook-before-uv-sync`
- [ ] read `estimate-plugin-install-runs-no-hook-before-uv-sync`
```

### Case 932.5 — The check of the setup Case counts the setting aside among the changes of the install

> **given:**
> `estimate-morph-sets-up-the-project-at-the-first-hi`: its purpose and its Criterion, replaced whole by the text under `sections`, name the setting aside beside the copy.
> **＋** `/guppi:install`: the skill that copies the files of GUPPI and sets aside those of the project.

> **when:**
> Someone reads `estimate-morph-sets-up-the-project-at-the-first-hi` to judge which changes of the settings files come before the setup Case.

> **then:**
> Its purpose and its Criterion count the files that `/guppi:install` sets aside, beside the files it copies, among the changes that come before the setup Case.
> **－** Its promise on the setup Case itself does not change.

```then
update:
- slug: estimate-morph-sets-up-the-project-at-the-first-hi
  set:
    status: pending
    purpose: Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the setup as done, puts one setup Case first, before the opening of the first sprint, with the values it finds and the values the person gives, and whether the settings change only by the copy and the setting aside of /guppi:install, the render of /hi and the render after that Case is ratified
  sections:
    Criterion: |-
      When:
      In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` does not mark the setup of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

      Then:
      `/hi` opens the session as `rule-skill-hi` sets it, and puts the setup Case first, before the opening Case of `rule-skill-sprint-open` and before the Frontier.
      **＋** Once the person ratifies the setup Case, `/hi` starts `/sprint-open` in the same session, and the ledger hook of `rule-ledger-write` writes the decision lines of the setup Case though no sprint is open.
      **＋** The setup step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
      **＋** It asks the person only for the values it cannot find, such as `documentation_lang`, `chat_lang`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project.
      **＋** Every value stands in that one setup Case, which the person ratifies or corrects.
      **＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config`, the description of the project in `CLAUDE.md` from `rule-claude-md` and the read rules of the saved transcripts from `rule-permissions`, and `guppi.toml` then marks the setup as done.
      **－** `/guppi:install` is no Case, and the person ratifies nothing at it.
      **－** Between `/guppi:install` and the ratified setup Case, no settings file changes but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs.
      **－** The setup step is no skill named `install`.
      **－** The setup step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
      **－** The setup step reads no code of the project and creates no page for it.
      **－** A project whose `guppi.toml` marks the setup as done gets no setup Case at `/hi`.
  change: the Criterion replaced whole — the files that /guppi:install sets aside count beside its copy among the changes before the setup Case
```

```tasks
- [ ] update `estimate-morph-sets-up-the-project-at-the-first-hi`
- [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`
```

## Case 934 — The long-plan approval in the CLI is put off as a bug with a test

> **context:**
> At the end of Plan Mode the main agent calls `ExitPlanMode`, Claude Code shows the plan file and the person approves it in a dialog; the hook of `rule-spec-capture` then copies the plan into `spec.md` of the session folder. `decision-case-909` put off `rule-spec-capture` with the item of letting a Spec be approved in the Claude Code CLI, since `lesson-plugin-cli-withholds-approval-of-a-long-plan` records that a plan of 15347 bytes was not approved there, while a plan of 58861 bytes was approved in the VS Code extension. The lesson gives the cause as the CLI. Its source is the transcript of the test install, where the text of the refusal stands in line 870 as a user message, not as output of Claude Code. The person thinks the cause is the terminal, since the test install ran in a standalone PowerShell window and not in the terminal of the editor, and chose to keep the approval as it is and to put the item off again as a bug, with a test that finds the cause.
>
> The documentation of Claude Code names no size limit of a plan. `case-guppi` read https://code.claude.com/docs/en/permission-modes, which says that Shift+Tab leaves Plan Mode without approving a plan and that Ctrl+G opens the plan in a text editor, and names no limit. It read https://code.claude.com/docs/en/settings-reference, whose index names three settings of plans, `plansDirectory`, `useAutoModeDuringPlan` and `showClearContextOnPlanAccept`, none of them on the size shown. It read https://code.claude.com/docs/en/env-vars, which names no variable on plan approval. It read the first 100 000 of 1 120 755 characters of the changelog of Claude Code, at https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/CHANGELOG.md, which hold three fixes of the plan approval screen and none on its size; the rest was not read. So whether the fault lies in Claude Code or in the terminal is not known, and the test of this item is what settles it.
>
> The Case writes one `defer` of `rule-spec-capture` with the new item and carries `{supersedes:case 909}`, the form Case 876 used to move a defer. `case-guppi` read `defer`, `clear_deferred_by` and `decision` of `.guppi/guppi/generate.py` whole: `decision` sets `decision-case-909` `superseded` and calls `clear_deferred_by`, which drops only `decision-case-909` from the `deferred_by` of each page in its `defer` list that a line of this Case names, and `defer` adds the new Decision page to the `deferred_by` of `rule-spec-capture` when it is not there; so the page keeps one defer, the new one, whichever runs first. The line of `vault/wiki/backlog.md` shows the `purpose` of the page, by the Criterion of `estimate-backlog-renders`, so the text of the bug stands under `## Deferred` of the Decision page of this Case, which the session that takes up the item reads through `deferred_by`. The governing rule is `rule-backlog`, whose Purpose prevents a deferred item from dropping out of sight; the item stays on the list.
>
> `lesson-plugin-cli-withholds-approval-of-a-long-plan` stands as it is: it records what was seen, and its cause is the guess the test checks. The text of `rule-spec-capture` does not change, so neither of its Estimates is touched. No new Estimate is created, by the person's answer: `estimate-backlog-renders` already checks that `backlog.md` holds one line per live page with a `deferred_by` that is not empty; its Criterion speaks of that mechanism and of no single page, so it stands. The session's ledger holds no `error` lesson, so no line of this Case carries an `addresses` mark.

> **problem:**
> The item of `rule-spec-capture` asks how GUPPI approves a Spec too long for the CLI, but the cause of the refusal is not known, and the person wants the approval kept as it is until a test shows whether Claude Code or the terminal is at fault.

> **recommend:**
> - **How the person approves a long Spec in the CLI**
>   - Recommended: (a) the person approves in the chat, and the hook before `ExitPlanMode` answers it with allow, so no dialog opens.
>   - Answer: none of the options; keep the approval as it is, with the dialog of `ExitPlanMode` and the plan file unchanged; the cause is likely the terminal, since the test ran in a standalone PowerShell window and not in the terminal of the editor; rewrite the item as a bug with a test that finds the cause.
> - **What the test compares**
>   - Recommended: (a) one plan of the size that failed, approved in a standalone PowerShell window and in the terminal of VS Code, the size of each window and whether the dialog opened noted, the result recorded by a lesson line.
>   - Answer: agreed, (a).
> - **How this Case is checked**
>   - Recommended: (a) by `estimate-backlog-renders`, with no new Estimate.
>   - Answer: agreed, (a).

> **given:**
> `rule-spec-capture`: the rule of the approved Spec, put off again with the bug and its test.
> **＋** `decision-case-909`: the Decision page of the earlier item, superseded.
> **＋** `lesson-plugin-cli-withholds-approval-of-a-long-plan`: the record of the refusal in the CLI.
> **＋** `vault/wiki/backlog.md`: the list of put-off items that `guppi backlog` writes.
> **＋** `estimate-backlog-renders`: the check of the lines of `backlog.md`.
> **＋** `rule-backlog`: the rule that no put-off item drops out of sight.

> **when:**
> The librarian runs `uv run --project .guppi guppi generate` and then `uv run --project .guppi guppi backlog` over the Spec that holds this Case.

> **then:**
> `vault/wiki/backlog.md` holds a line for `rule-spec-capture`.
> **＋** The `deferred_by` of `rule-spec-capture` names the Decision page of this Case and not `decision-case-909`.
> **＋** The Decision page of this Case holds under `## Deferred` the bug and the test that compares a standalone PowerShell window with the terminal of VS Code.
> **＋** `decision-case-909` stands `superseded` or `archived`.
> **－** The text of `rule-spec-capture` and the page `lesson-plugin-cli-withholds-approval-of-a-long-plan` do not change.

```then
defer:
- slug: rule-spec-capture
  type: rule
  purpose: 'Bug: approval of a long plan is withheld in the Claude Code CLI, and the cause is not known: the Claude Code CLI or the terminal it runs in, since the refusal was seen in a standalone PowerShell window, with a plan of 15347 bytes, and the approval of a long plan stays as it is until the cause is known. Test: approve by ExitPlanMode one plan of that size in a standalone PowerShell window and in the terminal of VS Code, note the size of each window and whether the approval dialog opened, and record the result by a lesson line, so that the Case that fixes the bug knows where the fault lies (lesson-plugin-cli-withholds-approval-of-a-long-plan; moved here from the defer of case 909)'
```

```tasks
- [ ] defer `rule-spec-capture`
```

## Case 935 — The lift carries `drop` and guards the Criterion from it

> **context:**
> `guppi materialize` lifts each item of a Case's `then` block into an entry of `materialize.yaml`; for an `update`, `_lift_item` of `.guppi/guppi/materialize.py` copies each key of `ITEM_KEYS["update"]` that the item carries, and `generate` applies the entry. Case 931 adds `drop`, a list of section names, to `ITEM_KEYS`, and `generate` removes each named section and fails the entry when the page lacks the section or the schema of its category requires it, such as `## Criterion` of an Estimate; I read its finished file whole. Once `drop` stands in `ITEM_KEYS`, the loop of `_lift_item` carries it with no other code. Two texts name the keys one by one and miss `drop`: the Criterion of `estimate-materialize-assembles` lists the keys an entry takes from its `then` item, and the Purpose of `rule-materialize` lists the keys lifted from the `then` block; `/pre-spec` reported both on Case 931. In Case 931's round the person chose that a new Case, this one, holds the promise that the lift carries `drop`, on the Estimate of the code that keeps it, and that Case 931 keeps no line of it. The docstring of `.guppi/guppi/materialize.py` lists the fields an entry takes from the `then` block and says that a key the code writes and the list does not name is a finding of the reading of `estimate-materialize-assembles`, so a task adds `drop` there too. In my round the person chose a second part: the lift already marks an Estimate `update` whose `replace` pair stands inside `## Criterion` as `incomplete: [criterion]`, by `touches_criterion` and `lift_criterion`, which I read whole with `names_a_part`, and nothing there reads `drop`. An Estimate `update` whose `drop` names `Criterion` and carries no `set.status` passes `names_a_part` as a named part today and gets no mark; one that carries `set.status` gets a lifted Criterion and `pending`, and `generate` then fails it. `drop` names whole sections only, so the one part of the Criterion it can touch is the whole section; Case 935.2 marks such an item at the lift by a new predicate, `drops_criterion`, so that the librarian sees it in the yaml before `generate` runs. A Grep of `incomplete` over `.guppi/guppi/generate.py` printed nothing, so `generate` does not read the mark, and Case 931's failure stands as the second wall. The judgment of the two sides differs: `generate` asks by `check_schema` of `.guppi/guppi/lint.py` whether the schema requires the section, and the lift asks only whether `drop` names `Criterion` on an Estimate, so no shared function fits both; a Grep of `"drop"|\bdrop\b.*Criterion|Criterion.*\bdrop\b` over `.guppi/guppi` printed nothing, so no code judges `drop` today, and the new predicate is no second copy. A Grep of `touches_criterion|names_a_part` over `.guppi` printed `test_prespec.py`, `materialize.py` and `prespec.py`; `check_criterion_pairs` of `.guppi/guppi/prespec.py`, which I read whole, judges `replace` pairs only, and `/pre-spec` gains no judgment of `drop` here, since the lift and `generate` both catch it. The pair on `rule-materialize` in Case 935.2 adds `drop` to the list of named parts and one sentence on the mark; the sentence on a part inside the Criterion stands, since it names `replace` pairs only. The Criterion of `estimate-materialize-changes-a-named-part-alone` speaks of which `update` items replace a Criterion and which name a part, so Case 935.2 replaces it whole, every line kept but the list of named parts, which gains `drop`, and one `－` line added; its `purpose` and `method` stand. The new Criterion of `estimate-materialize-assembles` keeps every line of the old one and adds `drop` to the list of keys; its `purpose` and `method` do not state the list and stand. A Grep of `estimate-materialize-changes-a-named-part-alone|estimate-materialize-assembles` over `vault/wiki`, `.claude` and `.guppi` printed `log.md`, `materialize.py`, `rule-materialize.md` and `test_materialize.py`; none but the docstring line above states the list, and no test of `.guppi/tests` reads these pages live. The tasks of this Case run after Case 931 adds `drop` to `ITEM_KEYS` in the same Work Mode, since the lift carries no `drop` before it; `test_item_keys_answers_for_each_kind_as_the_lift_does` is changed by Case 931. The check of this file noted that one line of each old Criterion is not carried. Those are the two lines this Case changes on purpose: the first line of the `then` of `estimate-materialize-assembles` gains `drop` in its list of keys, and the line of `estimate-materialize-changes-a-named-part-alone` on a named part gains `drop` in its list of parts. The check also noted that a `then` line of Case 935.2 shares most of its words with one of Case 935.1. The two lines state different promises of two Estimates: the line of Case 935.2 says an item with `change` alone is not `incomplete`, and the line of Case 935.1 lists the keys of an entry, so both stand. The session's ledger holds no `error` lesson.

> **problem:**
> The lift will carry `drop`, but the Estimate and the rule that list its keys do not name it, and an Estimate `update` whose `drop` names its Criterion gets no mark at the lift.

> **recommend:**
> - **Who guards the Criterion against a drop**
>   - Recommended: (a) this Case adds the guard as a second part, judged by the lift.
>   - Answer: (a).

### Case 935.1 — The lift carries `drop` into the entry

> **given:**
> `estimate-materialize-assembles`: its Criterion is replaced whole.
> **＋** `rule-materialize`: its Purpose lists the keys the lift carries.
> **＋** `.guppi/guppi/materialize.py`: `guppi materialize`, which lifts a unit's `ledger.md` and `spec.md` into `materialize.yaml`.
> **＋** `.guppi/tests/test_materialize.py`: the test of the lift.

> **when:**
> `uv run --project .guppi guppi materialize` lifts the record lines of a unit's `ledger.md` against the `then` blocks of its `spec.md`.

> **then:**
> `materialize.yaml` holds one entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `addresses`, `origin`, `line`, `text`, `decision`; from the `then` item found by its slug — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `drop`, `impact`; what the block lacks is `incomplete`, never invented.
> **＋** `reword` is carried as a list of `{old, new}` pairs; a mapping or a scalar under it is `incomplete: [reword]`.
> **＋** An Estimate has its own line and its own entry, the `ref` of the line the Estimate itself; the entry of its `create` keeps `kind`, `purpose`, `method` and `tags` as fields.
> **＋** One decision record per Case: `decision`, `case_text`, `targets`; a sub-case reads a missing `context` and `given` from its parent, never `problem`, `recommend` or `when`, and carries `parent`, the `decision` of its parent.
> **＋** A Case whose sub-cases have decision lines in the unit gets one decision record of its own: its `decision` and its `origin` named by the id of the Case, `case_text` with its `context`, `problem` and `recommend`, and its `given` when it has one, `children` the `decision` of each of its sub-cases in ledger order, and no `targets`.
> **＋** An `estimate` line whose slug has a `create` in the same unit is folded into it; one for a page of an earlier unit is an `estimate` entry of its own.
> **＋** The `new_tags` of any Case reach the yaml once each; an existing `materialize.yaml` is extended with the lines it does not hold, never rewritten.
> **＋** A line the grammar does not parse goes under `unparsed`, and the run goes on.
> **－** No entry of an Estimate is derived from a key of the item of a rule or an entity: an Estimate comes only from its own line.
> **－** A sub-case record without `problem` carries no `incomplete: [problem]`.

```then
update:
- slug: rule-materialize
  replace:
  - old: '`set`, `sections`, `replace`, `change`, and `rename` or `reword` when the item carries it'
    new: '`set`, `sections`, `replace`, `change`, and `rename`, `reword` or `drop` when the item carries it'
  change: the lift carries drop, a list of section names, when the item carries it
- slug: estimate-materialize-assembles
  set:
    status: pending
  change: the Criterion replaced whole — an entry takes drop from its then item
```

```tasks
- [ ] update `rule-materialize`
- [ ] update `estimate-materialize-assembles`
- [x] `.guppi/guppi/materialize.py`: the docstring that lists the fields an entry takes from the `then` block names `drop`, a list of section names carried as written.
- [x] `.guppi/tests/test_materialize.py`: a test that an `update` item with `drop: [How it works]` gives its entry `drop` equal to `["How it works"]`, and an item without `drop` gives an entry with no `drop`.
- [ ] read `estimate-materialize-assembles`
```

### Case 935.2 — The lift marks a `drop` of the Criterion

> **given:**
> `estimate-materialize-changes-a-named-part-alone`: its Criterion is replaced whole.
> **＋** `rule-materialize`: its Purpose says which `update` of an Estimate changes a part alone.
> **＋** `.guppi/guppi/materialize.py`: `guppi materialize`, with `names_a_part`, `lift_criterion` and the new `drops_criterion`.
> **＋** `.guppi/guppi/generate.py`: applies the entry and writes its History line.
> **＋** `.guppi/guppi/prespec.py` and `.guppi/guppi/casecheck.py`: import `names_a_part` and its notes.
> **＋** `.guppi/tests/test_materialize.py`: the test of the lift.

> **when:**
> `uv run --project .guppi guppi materialize` lifts the `update` item of an Estimate.

> **then:**
> An item that carries `set.status` gets `sections.Criterion`, the text it writes under `sections: Criterion` or else the `when` and `then` of its Case, and keeps the status it set.
> **＋** An item that writes `sections: Criterion` keeps that text and gets `set: {status: pending}` unless it set a status itself.
> **＋** A written `sections.Criterion` beside any other part stands and sets `pending`.
> **＋** An item that carries `change` alone gets no `sections.Criterion` and no `set`: `.guppi/guppi/generate.py` writes its History line, and the Criterion and the status of the page stand.
> **＋** An item that names a part — `set` without `status`, a `replace` pair, `drop`, a section other than `Criterion` — and writes no Criterion carries that part alone: nothing is lifted and no status is set.
> **＋** `names_a_part` of `.guppi/guppi/materialize.py` is the one judgment of an item that replaces a Criterion: `.guppi/guppi/prespec.py` imports it and `.guppi/guppi/casecheck.py` imports its notes, so an item with `change` alone counts as no promise and gets no note on the lines of the old Criterion.
> **－** An item with `change` alone is not `incomplete`.
> **－** An item whose `drop` names `Criterion` gets `incomplete: [criterion]`, by `drops_criterion` of `.guppi/guppi/materialize.py`, and the lift adds no `sections.Criterion` and no `set.status` to it, whatever else the item carries.

```then
update:
- slug: rule-materialize
  replace:
  - old: '`set` without `status`, `replace`, a section other than `Criterion` — and writes no Criterion changes'
    new: '`set` without `status`, `replace`, `drop`, a section other than `Criterion` — and writes no Criterion changes'
  - old: on an Estimate as on any page (case 588.2). An `update` item's `reword`
    new: 'on an Estimate as on any page (case 588.2). An `update` of an Estimate whose `drop` names `Criterion` is `incomplete: [criterion]`, and the lift writes no Criterion and sets no status for it, since an Estimate keeps its Criterion (as set in case 935.2). An `update` item''s `reword`'
  change: 'a drop is a named part, and a drop of the Criterion of an Estimate is incomplete: [criterion]'
- slug: estimate-materialize-changes-a-named-part-alone
  set:
    status: pending
  change: the Criterion replaced whole — drop is a named part, and a drop of the Criterion is incomplete
```

```tasks
- [ ] update `rule-materialize`
- [ ] update `estimate-materialize-changes-a-named-part-alone`
- [x] `.guppi/guppi/materialize.py`: a function `drops_criterion(drop) -> bool`, True when `drop` is a list that holds the name `Criterion`; `lift_criterion` calls it first for an Estimate `update` and, when it is True, appends `criterion` to the entry's `incomplete` and returns before `names_a_part`. The docstrings of `lift_criterion` and of the module, where they list the named parts, name `drop` and the mark.
- [x] `.guppi/tests/test_materialize.py`: tests that an Estimate `update` with `drop: [Criterion]` and `change` gets `incomplete: [criterion]`, no `sections.Criterion` and no `set`; that one with `drop: [Criterion]` and `set: {status: pending}` gets `incomplete: [criterion]` and no `sections.Criterion`; that one with `drop: [Result]` and `change` gets no `incomplete`, no `sections.Criterion` and no `set`.
- [ ] read `estimate-materialize-changes-a-named-part-alone`
```
