"""`guppi test` and `guppi style`, `estimate-guppi-config-runs-the-test-and-style-commands`
(case 820.2): each runs the commands of its key of `guppi.toml` in order, in the folder of
the project, with no shell and no stdin, each one even after a red one; the run is red when
any command is, green only when every one is; a missing `guppi.toml` or key is one line that
names the file and the key, with exit 1 and nothing run. A fake command, a Python script,
records each call: its words, its folder and what it read from stdin."""

import io
import os
import shlex
import subprocess
import sys
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


def test_the_keys_of_the_commands_do_not_stop_the_render():
    text = LANGUAGES + "test = ['uv run pytest']\nstyle = ['uv run ruff check .']\n"
    assert config.parse(text, "guppi.toml") == {"documentation_lang": "en", "chat_lang": "ru"}
