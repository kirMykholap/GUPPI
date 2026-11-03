"""`guppi test` and `guppi style`, `estimate-guppi-config-runs-the-test-and-style-commands`: each runs the commands of its key of `guppi.toml` in order, in the folder of
the project, with no shell and no stdin, each one even after a red one; the run is red when
any command is, green only when every one is; a missing `guppi.toml` or key is one line that
names the file and the key, with exit 1 and nothing run; with `--exit-zero` each prints the
exit code of the run on a last line and exits 0. A fake command, a Python script,
records each call: its words, its folder and what it read from stdin."""

import io
import json
import os
import shlex
import subprocess
import sys
import tomllib
from pathlib import Path

from guppi import config
from guppi.commands import run_style, run_test

FAKE = """\
import os, sys
read = sys.stdin.read()
words = " ".join(sys.argv[1:])
with open(os.environ["FAKE_LOG"], "a", encoding="utf-8") as log:
    log.write(f"{words} | {os.getcwd()} | stdin:{'read' if read else 'empty'}\\n")
print(f"fake: {words}", flush=True)
sys.exit(1 if sys.argv[1] == "red" else 0)
"""
LANGUAGES = 'documentation_lang = "en"\nchat_lang = "ru"\n'


def project(tmp_path, monkeypatch, settings: str | None):
    """A project whose `guppi.toml` holds `settings`, none when None; the fake command, as
    the start of a command line, and its log."""
    root = tmp_path / "project"
    root.mkdir()
    fake = tmp_path / "fake.py"
    fake.write_text(FAKE, encoding="utf-8")
    log = tmp_path / "calls.log"
    monkeypatch.setenv("FAKE_LOG", str(log))
    if settings is not None:
        (root / "guppi.toml").write_text(settings, encoding="utf-8")
    start = f"{shlex.quote(Path(sys.executable).as_posix())} {shlex.quote(fake.as_posix())}"
    return root, start, log


def toml_list(commands: list[str]) -> str:
    return "[" + ", ".join(f"'{c}'" for c in commands) + "]"


def calls(log: Path) -> list[str]:
    return log.read_text(encoding="utf-8").splitlines() if log.exists() else []


def run(command, root):
    stderr = io.StringIO()
    code = command([], stderr=stderr, project_dir=root)
    return code, stderr.getvalue().splitlines()


def test_the_commands_run_in_order_each_after_a_red_one_and_the_run_is_red(
    tmp_path, monkeypatch, capfd
):
    root, start, log = project(tmp_path, monkeypatch, None)
    commands = [f"{start} one", f"{start} red", f"{start} three"]
    (root / "guppi.toml").write_text(LANGUAGES + f"test = {toml_list(commands)}\n", "utf-8")
    code, err = run(run_test, root)
    assert code != 0
    assert err == []
    assert [line.split(" | ")[0] for line in calls(log)] == ["one", "red", "three"]
    assert capfd.readouterr().out.splitlines() == ["fake: one", "fake: red", "fake: three"]


def test_every_command_green_makes_the_run_exit_0(tmp_path, monkeypatch, capfd):
    root, start, log = project(tmp_path, monkeypatch, None)
    commands = [f"{start} one", f"{start} two"]
    (root / "guppi.toml").write_text(LANGUAGES + f"style = {toml_list(commands)}\n", "utf-8")
    assert run(run_style, root) == (0, [])
    assert [line.split(" | ")[0] for line in calls(log)] == ["one", "two"]


def test_a_command_runs_in_the_folder_of_the_project_with_no_shell(tmp_path, monkeypatch):
    root, start, log = project(tmp_path, monkeypatch, None)
    commands = [f"{start} one && exit 7 $HOME"]
    (root / "guppi.toml").write_text(LANGUAGES + f"test = {toml_list(commands)}\n", "utf-8")
    assert run(run_test, root) == (0, [])
    (words, folder, _) = calls(log)[0].split(" | ")
    assert words == "one && exit 7 $HOME"  # no shell read the words
    assert Path(folder).resolve() == root.resolve()


def test_no_command_reads_the_stdin_of_guppi_test(tmp_path, monkeypatch):
    root, start, log = project(tmp_path, monkeypatch, None)
    commands = [f"{start} one", f"{start} two"]
    (root / "guppi.toml").write_text(LANGUAGES + f"test = {toml_list(commands)}\n", "utf-8")
    done = subprocess.run(
        [sys.executable, "-P", "-m", "guppi.cli", "test"],
        check=False,
        cwd=root,
        env=dict(os.environ, CLAUDE_PROJECT_DIR=str(root)),
        input="a line no command may read\n",
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert done.returncode == 0, done.stderr
    assert [line.split(" | ")[2] for line in calls(log)] == ["stdin:empty", "stdin:empty"]


def test_a_missing_guppi_toml_is_one_line_and_exit_1(tmp_path, monkeypatch):
    root, _, log = project(tmp_path, monkeypatch, None)
    code, err = run(run_test, root)
    assert code == 1
    assert len(err) == 1
    assert "guppi.toml" in err[0] and "key test" in err[0]
    assert calls(log) == []


def test_a_missing_key_is_one_line_and_exit_1(tmp_path, monkeypatch):
    root, start, log = project(tmp_path, monkeypatch, None)
    (root / "guppi.toml").write_text(LANGUAGES + f"test = ['{start} one']\n", "utf-8")
    code, err = run(run_style, root)
    assert code == 1
    assert err == ["style: guppi.toml: no key style"]
    assert calls(log) == []


def run_exit_zero(command, root, capfd):
    """`command --exit-zero` over the project; the exit code, the lines of stdout and the
    lines of stderr."""
    stderr = io.StringIO()
    code = command(["--exit-zero"], stderr=stderr, project_dir=root)
    return code, capfd.readouterr().out.splitlines(), stderr.getvalue().splitlines()


def test_with_exit_zero_a_red_run_prints_its_exit_code_last_and_exits_0(
    tmp_path, monkeypatch, capfd
):
    """The lines of the run as before, then `exit code: 1`."""
    root, start, log = project(tmp_path, monkeypatch, None)
    commands = [f"{start} one", f"{start} red"]
    (root / "guppi.toml").write_text(LANGUAGES + f"test = {toml_list(commands)}\n", "utf-8")
    code, out, err = run_exit_zero(run_test, root, capfd)
    assert code == 0
    assert out == ["fake: one", "fake: red", "exit code: 1"]
    assert err == []
    assert [line.split(" | ")[0] for line in calls(log)] == ["one", "red"]


def test_with_exit_zero_a_green_run_prints_exit_code_0(tmp_path, monkeypatch, capfd):
    root, start, _ = project(tmp_path, monkeypatch, None)
    (root / "guppi.toml").write_text(LANGUAGES + f"style = ['{start} one']\n", "utf-8")
    code, out, _ = run_exit_zero(run_style, root, capfd)
    assert code == 0
    assert out == ["fake: one", "exit code: 0"]


def test_with_exit_zero_a_missing_key_prints_exit_code_1_and_exits_0(tmp_path, monkeypatch, capfd):
    root, _, log = project(tmp_path, monkeypatch, None)
    code, out, err = run_exit_zero(run_test, root, capfd)
    assert code == 0
    assert out == ["exit code: 1"]
    assert len(err) == 1 and "key test" in err[0]
    assert calls(log) == []


def test_the_keys_of_the_commands_do_not_stop_the_render():
    text = LANGUAGES + "test = ['uv run pytest']\nstyle = ['uv run ruff check .']\n"
    assert config.parse(text, "guppi.toml") == {"documentation_lang": "en", "chat_lang": "ru"}


PYTEST_SETTINGS = Path(__file__).resolve().parents[1] / "pyproject.toml"


def pytest_section() -> str:
    """The `[tool.pytest.ini_options]` of `.guppi/pyproject.toml`, as TOML text."""
    options = tomllib.loads(PYTEST_SETTINGS.read_text(encoding="utf-8"))["tool"]["pytest"]
    lines = [f"{key} = {json.dumps(value)}" for key, value in options["ini_options"].items()]
    return "[tool.pytest.ini_options]\n" + "\n".join(lines) + "\n"


def run_guppi_tests(root: Path) -> str:
    """The last line of `pytest -q .guppi/tests` run in the folder of the project."""
    done = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", ".guppi/tests"],
        check=False,
        cwd=root,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert done.returncode == 0, done.stdout + done.stderr
    return done.stdout.strip().splitlines()[-1]


def test_the_test_command_finds_the_settings_of_guppi_whatever_the_root_holds(tmp_path):
    """The key `test` names `.guppi/tests`: pytest starts its search for settings
    there and takes those of `.guppi/pyproject.toml`, the `live` marker included, with no
    root `pyproject.toml` and beside one that holds other pytest settings."""
    root = tmp_path / "project"
    tests = root / ".guppi" / "tests"
    tests.mkdir(parents=True)
    (root / ".guppi" / "pyproject.toml").write_text(pytest_section(), encoding="utf-8")
    (tests / "test_sample.py").write_text(
        "import pytest\n\n\ndef test_plain():\n    pass\n\n\n"
        "@pytest.mark.live\ndef test_live():\n    pass\n",
        encoding="utf-8",
    )
    alone = run_guppi_tests(root)
    assert "1 passed" in alone and "1 deselected" in alone
    (root / "pyproject.toml").write_text(
        '[tool.pytest.ini_options]\ntestpaths = ["elsewhere"]\naddopts = "-m live"\n',
        encoding="utf-8",
    )
    beside = run_guppi_tests(root)
    assert "1 passed" in beside and "1 deselected" in beside
