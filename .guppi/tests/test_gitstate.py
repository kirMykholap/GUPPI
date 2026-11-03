"""`guppi gitstate` prints the state of git or one line outside a repository.

`estimate-git-context-gitstate-exits-zero`: in a git repository the command prints the branch,
the line `Status:` and the status, in a folder that is no git repository the one line, and it
exits 0 in each case.
"""

import io
import subprocess

import pytest

from guppi import gitstate


@pytest.fixture
def folder(tmp_path, monkeypatch):
    """An empty folder with no git repository above it."""
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))
    work = tmp_path / "project"
    work.mkdir()
    return work


def run(folder):
    out = io.StringIO()
    code = gitstate.run([], stdout=out, project_dir=folder)
    return code, out.getvalue()


def test_outside_a_repository_it_prints_one_line_and_exits_zero(folder):
    code, text = run(folder)
    assert code == 0
    assert text == "none: this folder is no git repository\n"


def test_in_a_repository_it_prints_the_branch_and_the_status(folder):
    subprocess.run(["git", "init", "-b", "main"], cwd=folder, check=True, capture_output=True)
    (folder / "notes.txt").write_text("x", encoding="utf-8")
    code, text = run(folder)
    assert code == 0
    assert text.splitlines() == ["main", "Status:", "?? notes.txt"]


def test_it_writes_nothing(folder):
    run(folder)
    assert list(folder.iterdir()) == []


def test_a_missing_git_counts_as_no_repository(folder, monkeypatch):
    def missing(*args, **kwargs):
        raise FileNotFoundError("git")

    monkeypatch.setattr(gitstate.subprocess, "run", missing)
    code, text = run(folder)
    assert code == 0
    assert text == "none: this folder is no git repository\n"
