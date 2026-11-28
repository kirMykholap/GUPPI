"""The code of GUPPI stands in `.guppi/` and every caller runs it there.

The package `guppi`, its `pyproject.toml`, its `uv.lock`, its tests and a `.gitignore` that
holds `.venv/` and `__pycache__/` stand under `.guppi/`, so the Python caches stay out of git. Each hook command of `.claude/settings.json` and of the frontmatter of
`.claude/agents/librarian-guppi.md` runs the code by `--project "${CLAUDE_PROJECT_DIR}/.guppi"`,
so a `cd` in a Bash call cannot break it, and passes by `--project .guppi` too until the render
of the librarian's run writes the new form. No file of `.claude/`, the `Makefile` or
`.github/workflows/` names `uv run guppi` or `uv run pytest`, and no live rule, entity or
Estimate names them, or a path that the pairs `guppi/` and `tests/` would change, in the
parts that a `reword` changes — each found by `reword_pattern` and `reword_text` of
`.guppi/guppi/generate.py`, the matching of the `reword` of `rule-guppi-package`, imported.
Each `COMMAND` of a hook that finds its own refusals by it stands in `.claude/settings.json`.
The clean version holds no `pyproject.toml` and no `uv.lock` at its root.

Between the Work Mode that moved the code and the librarian's run that rendered the harness
and applied the `reword`, the files of `.claude/` and the pages still named the old command,
so the tests over them were red then. A test like these now passes on the text
before the change and on the text after it until the text lands, as `rule-case-build` sets
it. Rule page: `vault/wiki/rules/rule-guppi-package.md`.
"""

import copy
import json
import shutil
import subprocess
import tomllib
from datetime import date
from pathlib import Path

import pytest

from guppi import casecheck, ledger, onward, ratified
from guppi.gate import dirty
from guppi.generate import REWORD_CATEGORIES, Vault, reword_pattern
from guppi.pages import read_vault, wiki_root

REPO = Path(__file__).resolve().parents[2]
PACKAGE = REPO / ".guppi"
OLD_COMMANDS = ("uv run guppi", "uv run pytest")  # the `old` of the command pairs
OLD_PATHS = ("guppi/", "tests/")  # the `old` of the path pairs
CALLERS = (".claude", ".github/workflows")  # each file under them, and the `Makefile`
HOOKS = (ledger, onward, ratified, casecheck)  # each finds its refusals by its `COMMAND`


def callers() -> list[Path]:
    # the clean version holds no `Makefile`
    files = [path for path in (REPO / "Makefile",) if path.is_file()]
    for top in CALLERS:
        files += sorted(
            path
            for path in (REPO / top).rglob("*")
            if path.is_file() and path.name != "settings.local.json"
        )
    return files


def live_pages():
    vault = read_vault(wiki_root(REPO))
    return [page for category in REWORD_CATEGORIES for page in vault[category] if not page.error]


def test_the_package_its_settings_its_lock_and_its_tests_stand_under_guppi():
    assert (PACKAGE / "guppi" / "__init__.py").is_file()
    assert (PACKAGE / "guppi" / "cli.py").is_file()
    assert (PACKAGE / "tests" / "conftest.py").is_file()
    assert (PACKAGE / "uv.lock").is_file()
    assert ".venv/" in (PACKAGE / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert not (REPO / "guppi").exists() and not (REPO / "tests").exists()
    settings = tomllib.loads((PACKAGE / "pyproject.toml").read_text(encoding="utf-8"))
    assert settings["project"]["name"] == "guppi"
    assert settings["project"]["scripts"]["guppi"] == "guppi.cli:main"
    dev = " ".join(settings["dependency-groups"]["dev"])
    assert "pytest" in dev and "ruff" in dev
    assert settings["tool"]["pytest"]["ini_options"]["testpaths"] == ["tests"]
    assert "ruff" in settings["tool"]


@pytest.mark.parametrize("old", OLD_COMMANDS)
def test_no_caller_runs_the_code_or_the_tests_without_the_project(old):
    word = reword_pattern(old)
    hits = [
        f"{path.relative_to(REPO).as_posix()}:{number}"
        for path in callers()
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
        if word.search(line)
    ]
    assert hits == []


@pytest.mark.parametrize("old", OLD_COMMANDS + OLD_PATHS)
def test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it(old):
    hits = []
    for page in live_pages():
        if Vault.reword_text(copy.deepcopy(page), old, old):
            hits.append(f"{page.category}/{page.slug}")
    assert hits == []


@pytest.mark.parametrize("hook", HOOKS, ids=lambda hook: hook.__name__)
def test_each_hook_command_stands_in_the_settings_in_the_new_form(hook):
    # the new form, or the form with `--project .guppi` until the render writes the new one
    assert hook.COMMAND.startswith(ledger.PROJECT_RUN + "guppi ")
    assert any(form in settings_commands() for form in ledger.command_forms(hook.COMMAND))


def settings_commands() -> list[str]:
    settings = json.loads((REPO / ".claude" / "settings.json").read_text(encoding="utf-8"))
    return [
        hook["command"]
        for matchers in settings["hooks"].values()
        for matcher in matchers
        for hook in matcher["hooks"]
        if "command" in hook
    ]


def librarian_commands() -> list[str]:
    text = (REPO / ".claude" / "agents" / "librarian-guppi.md").read_text(encoding="utf-8")
    front = text.split("---", 2)[1]
    return [
        line.split("command:", 1)[1].strip() for line in front.splitlines() if "command:" in line
    ]


def test_every_hook_command_runs_the_code_from_the_project_folder():
    # each hook command of the settings and of the frontmatter of the librarian runs the code
    # by `--project "${CLAUDE_PROJECT_DIR}/.guppi"`, or by `--project .guppi` until the render
    # of the librarian's run writes the new form
    commands = settings_commands() + librarian_commands()
    assert commands
    stray = [
        command
        for command in commands
        if " guppi " in command and not command.startswith((ledger.PROJECT_RUN, ledger.OLD_RUN))
    ]
    assert stray == []


def test_the_python_caches_stay_out_of_git(tmp_path):
    # the live `.guppi/.gitignore` keeps `__pycache__/` out of `git status`, so the gate of
    # `/handoff` sees only the staged ignore file
    if shutil.which("git") is None:
        pytest.skip("git is not installed")
    for args in (["init", "-q"], ["config", "user.email", "t@t"], ["config", "user.name", "t"]):
        subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)
    folder = tmp_path / ".guppi"
    folder.mkdir()
    (folder / ".gitignore").write_bytes((PACKAGE / ".gitignore").read_bytes())
    for part in ("guppi", "tests"):
        cache = folder / part / "__pycache__"
        cache.mkdir(parents=True)
        (cache / "x.cpython-312.pyc").write_bytes(b"\0")
    subprocess.run(["git", "add", ".guppi/.gitignore"], cwd=tmp_path, check=True)
    assert dirty(tmp_path) == "A  .guppi/.gitignore"


def test_the_clean_version_holds_no_pyproject_and_no_lock_at_its_root(tmp_path):
    # the build of `guppi ship --allow-draft <folder>`: a draft page with `core: true` stops
    # nothing, and no tag is read, since this repository need not carry one; the clean
    # version holds no `guppi.ship`, so there the test is skipped
    ship = pytest.importorskip("guppi.ship")
    ship.ship(REPO, tmp_path, date(2001, 1, 1), "0.0.0")
    assert (tmp_path / "CLAUDE.md").is_file()
    assert not (tmp_path / "pyproject.toml").exists()
    assert not (tmp_path / "uv.lock").exists()
