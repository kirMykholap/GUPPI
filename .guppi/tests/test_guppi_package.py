"""The code of GUPPI stands in `.guppi/` and every caller runs it there (case 819.1).

The package `guppi`, its `pyproject.toml`, its `uv.lock`, its tests and a `.gitignore` that
holds `.venv/` stand under `.guppi/`. No file of `.claude/`, the `Makefile` or
`.github/workflows/` names `uv run guppi` or `uv run pytest`, and no live rule, entity or
Estimate names them, or a path that the pairs `guppi/` and `tests/` would change, in the
parts that a `reword` changes — each found by `reword_pattern` and `reword_text` of
`.guppi/guppi/generate.py`, the matching of the `reword` of `rule-guppi-package`, imported.
Each `COMMAND` of a hook that finds its own refusals by it stands in `.claude/settings.json`.
The clean version holds no `pyproject.toml` and no `uv.lock` at its root.

Between the Work Mode that moves the code and the librarian's run that renders the harness
and applies the `reword`, the files of `.claude/` and the pages still name the old command,
so the tests over them are red; that red is a note for the handoff. Rule page:
`vault/wiki/rules/rule-guppi-package.md`.
"""

import copy
import tomllib
from datetime import date
from pathlib import Path

import pytest

from guppi import casecheck, ledger, onward, ratified
from guppi.generate import REWORD_CATEGORIES, Vault, reword_pattern
from guppi.pages import read_vault, wiki_root

REPO = Path(__file__).resolve().parents[2]
PACKAGE = REPO / ".guppi"
OLD_COMMANDS = ("uv run guppi", "uv run pytest")  # the `old` of the command pairs
OLD_PATHS = ("guppi/", "tests/")  # the `old` of the path pairs
CALLERS = (".claude", ".github/workflows")  # each file under them, and the `Makefile`
HOOKS = (ledger, onward, ratified, casecheck)  # each finds its refusals by its `COMMAND`


def callers() -> list[Path]:
    # the clean version holds no `Makefile` (case 822)
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
    assert hook.COMMAND.startswith("uv run --project .guppi guppi ")
    settings = (REPO / ".claude" / "settings.json").read_text(encoding="utf-8")
    assert f'"command": "{hook.COMMAND}"' in settings


def test_the_clean_version_holds_no_pyproject_and_no_lock_at_its_root(tmp_path):
    # the build of `guppi ship --allow-draft <folder>`: a draft page with `core: true` stops
    # nothing, and no tag is read, since this repository need not carry one; the clean
    # version holds no `guppi.ship`, so there the test is skipped
    ship = pytest.importorskip("guppi.ship")
    ship.ship(REPO, tmp_path, date(2001, 1, 1), "0.0.0")
    assert (tmp_path / "CLAUDE.md").is_file()
    assert not (tmp_path / "pyproject.toml").exists()
    assert not (tmp_path / "uv.lock").exists()
