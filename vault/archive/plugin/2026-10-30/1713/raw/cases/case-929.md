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

> **tasks:**
> - [ ] update `rule-guppi-config`
>   - old: `test = ["uv run --project .guppi pytest -q"]`
>   - new: `test = ["uv run --project .guppi pytest -q .guppi/tests"]`
>   - change: `the key test names the folder .guppi/tests, so pytest reads the settings of .guppi/pyproject.toml in any project`
> - [ ] `uv run --project .guppi guppi render`: `guppi.toml`
> - [ ] update `rule-guppi-package`
>   - old: `` and the tests as `uv run --project .guppi pytest`. ``
>   - new: `` and the tests as `uv run --project .guppi pytest`. The key `test` of `guppi.toml` names the folder `.guppi/tests`, since pytest looks for its settings only in the folder it starts in and the folders above it, and skips a folder whose name starts with a dot: so it reads the settings of `.guppi/pyproject.toml` whatever the root of the project holds (as set in case 929). ``
>   - change: `taken up: the test command names .guppi/tests, so pytest finds the tests of GUPPI with no root pyproject.toml; the root pyproject.toml of the repository of GUPPI keeps its pytest settings until the Case that removes it`
> - [ ] update `estimate-guppi-config-runs-the-test-and-style-commands`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether guppi test and guppi style run the commands that the keys test and style of guppi.toml list, in order and each after a red one, exit non-zero when any is red, and exit 1 with one line when the file or the key is missing; and whether the command of the key test runs the tests of .guppi/tests with the settings of .guppi/pyproject.toml whatever the root of the project holds"
>     method: "uv run --project .guppi pytest .guppi/tests/test_commands.py; by hand, after the librarian's run that renders guppi.toml with the key test that names .guppi/tests: uv run --project .guppi guppi test and uv run --project .guppi guppi style in this repository, and a Grep for make test and make style over the live rules, entities and Estimates and over .claude/, read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the key test names .guppi/tests, and its command runs those tests with the settings of .guppi/pyproject.toml whatever the root holds`
> - [ ] `.guppi/tests/test_commands.py`: a test writes a project with no root `pyproject.toml`, a `.guppi/pyproject.toml` with the pytest settings of `.guppi/pyproject.toml` (`testpaths`, the `live` marker, `addopts`) and `.guppi/tests/` with one plain test and one `live` test, runs pytest by `sys.executable -m pytest -q .guppi/tests` in the folder of that project, and asserts one passed and one deselected; a second run, with a root `pyproject.toml` that holds other pytest settings, answers the same.
> - [ ] read `estimate-guppi-config-runs-the-test-and-style-commands`

> **ratification:**
> ```
> - decision[case 929][update][rule-guppi-config]{ref:rule-guppi-config}
> - decision[case 929][update][rule-guppi-package]{ref:rule-guppi-package}{supersedes:case 834}{supersedes:case 848}
> - decision[case 929][update][estimate-guppi-config-runs-the-test-and-style-commands]{ref:rule-guppi-config}
> ```
