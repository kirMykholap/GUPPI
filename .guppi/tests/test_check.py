"""`guppi check`, `estimate-lint-runs-every-step` (cases 587, 820.1): the six vault checks
run in order, each one even after a red one, each with its own output and no stdin; the run
is red when any step is, green only when every one is; nothing of the tree is written; and
where the module `guppi.ship` is missing, `guppi ship --check` is skipped with one line that
sets no exit code. A fake step, a Python script in place of the entry point of `guppi`,
records each call and what it read from stdin, so no step of the real vault runs."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from guppi import check
from guppi.pages import ship_stands

PACKAGE = Path(check.__file__).resolve().parent
# a test of all six steps needs the module `guppi.ship`, which the clean version does not
# hold (case 822)
NEEDS_SHIP = pytest.mark.skipif(not ship_stands(), reason="no module guppi.ship")
STEPS = [
    "render --check",
    "sprint --check",
    "backlog --check",
    "glossary --check",
    "lint",
    "ship --check",
]
FAKE = """\
import os, sys
read = sys.stdin.read()
step = " ".join(sys.argv[1:])
with open(os.environ["FAKE_LOG"], "a", encoding="utf-8") as log:
    log.write(f"{step} stdin:{'read' if read else 'empty'}\\n")
print(f"fake guppi: {step}", flush=True)
sys.exit(1 if step == os.environ.get("FAKE_FAIL") else 0)
"""


def project(tmp_path):
    """A project folder with a file in it, the fake step, and the log the fake writes."""
    root = tmp_path / "project"
    (root / "vault" / "wiki").mkdir(parents=True)
    (root / "vault" / "wiki" / "x.md").write_text("# x\n", encoding="utf-8")
    fake = tmp_path / "fake_guppi.py"
    fake.write_text(FAKE, encoding="utf-8")
    return root, fake, tmp_path / "calls.log"


def snapshot(root: Path) -> dict[str, bytes]:
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def run_check(tmp_path, monkeypatch, capfd, fail=""):
    """`guppi check` over a project, its steps the fake; the exit code, the calls the fake
    recorded, the lines printed, and the tree before and after."""
    root, fake, log = project(tmp_path)
    monkeypatch.setattr(check, "GUPPI", (sys.executable, str(fake)))
    monkeypatch.setenv("FAKE_LOG", str(log))
    monkeypatch.setenv("FAKE_FAIL", fail)
    before = snapshot(root)
    code = check.run([], project_dir=root)
    out = capfd.readouterr().out.splitlines()
    calls = log.read_text(encoding="utf-8").splitlines() if log.exists() else []
    return code, calls, out, before, snapshot(root)


@NEEDS_SHIP
def test_every_step_runs_in_order_after_a_red_backlog_step_and_the_run_is_red(
    tmp_path, monkeypatch, capfd
):
    code, calls, out, before, after = run_check(tmp_path, monkeypatch, capfd, "backlog --check")
    assert code != 0
    assert calls == [f"{step} stdin:empty" for step in STEPS]
    assert out == [f"fake guppi: {step}" for step in STEPS]
    assert after == before


@NEEDS_SHIP
def test_every_step_green_makes_the_run_exit_0(tmp_path, monkeypatch, capfd):
    code, calls, out, before, after = run_check(tmp_path, monkeypatch, capfd)
    assert code == 0
    assert calls == [f"{step} stdin:empty" for step in STEPS]
    assert out == [f"fake guppi: {step}" for step in STEPS]
    assert after == before


@NEEDS_SHIP
def test_a_red_last_step_makes_the_run_red(tmp_path, monkeypatch, capfd):
    code, calls, _, _, _ = run_check(tmp_path, monkeypatch, capfd, "ship --check")
    assert code != 0
    assert len(calls) == len(STEPS)


@NEEDS_SHIP
def test_no_step_reads_the_stdin_of_its_caller(tmp_path):
    """`guppi check` runs in a process of its own with a line on its stdin, from a copy of the
    package whose entry point is the fake; no step reads that line."""
    root, fake, log = project(tmp_path)
    code = (
        "import sys; from guppi import check; "
        f"check.GUPPI = (sys.executable, {str(fake)!r}); sys.exit(check.run([]))"
    )
    env = dict(os.environ, FAKE_LOG=str(log), FAKE_FAIL="", CLAUDE_PROJECT_DIR=str(root))
    done = subprocess.run(
        [sys.executable, "-P", "-c", code],
        check=False,
        cwd=root,
        env=env,
        input="a line no step may read\n",
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert done.returncode == 0, done.stderr
    calls = log.read_text(encoding="utf-8").splitlines()
    assert calls == [f"{step} stdin:empty" for step in STEPS]


def test_without_the_module_ship_the_ship_step_is_skipped_with_one_line(tmp_path):
    """A copy of the package without `ship.py`, as the clean version holds it, runs `guppi
    check` in a process of its own: five steps run, one line names the skip, and the run is
    green."""
    root, fake, log = project(tmp_path)
    copy = tmp_path / "code"
    shutil.copytree(PACKAGE, copy / "guppi", ignore=shutil.ignore_patterns("__pycache__"))
    (copy / "guppi" / "ship.py").unlink(missing_ok=True)
    code = (
        "import sys; from guppi import check; "
        f"check.GUPPI = (sys.executable, {str(fake)!r}); sys.exit(check.run([]))"
    )
    env = dict(
        os.environ,
        PYTHONPATH=str(copy),
        FAKE_LOG=str(log),
        FAKE_FAIL="",
        CLAUDE_PROJECT_DIR=str(root),
    )
    before = snapshot(root)
    done = subprocess.run(
        [sys.executable, "-P", "-c", code],
        check=False,
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert done.returncode == 0, done.stderr
    calls = log.read_text(encoding="utf-8").splitlines()
    assert calls == [f"{step} stdin:empty" for step in STEPS[:-1]]
    assert done.stdout.splitlines() == [f"fake guppi: {step}" for step in STEPS[:-1]] + [
        check.SKIPPED
    ]
    assert snapshot(root) == before


def test_without_the_module_ship_a_red_step_still_makes_the_run_red(tmp_path, monkeypatch, capfd):
    monkeypatch.setattr(check, "ship_stands", lambda: False)
    code, calls, out, _, _ = run_check(tmp_path, monkeypatch, capfd, "lint")
    assert code != 0
    assert calls == [f"{step} stdin:empty" for step in STEPS[:-1]]
    assert out[-1] == check.SKIPPED


def test_a_step_runs_the_entry_point_of_guppi():
    # the real way a step runs: the entry point lists the command check among its commands
    done = subprocess.run(
        [*check.GUPPI, "-h"],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120,
    )
    assert done.returncode == 0
    assert "check" in done.stderr.split("commands: ", 1)[1].split(", ")
