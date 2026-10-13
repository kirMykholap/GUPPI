"""`guppi powershellguard`: the `PreToolUse PowerShell` hook refuses a here-string piped
into an interpreter, judged by the one function of `guppi/bashguard.py`, and names Write and
Edit (case 796.2). Rule page: `vault/wiki/rules/rule-powershell-guard.md`."""

import io
import json
from datetime import UTC, datetime

import pytest

from guppi import powershellguard

NOW = datetime(2026, 9, 14, 12, 0, 0, tzinfo=UTC)

SINGLE_TO_PYTHON = "@'\nfrom pathlib import Path\n'@ | python -"
DOUBLE_TO_UV_PYTHON = '@"\nprint(1)\n"@ | uv run python -'
SINGLE_TO_NODE = "@'\nconsole.log(1)\n'@ | node"
TO_OUT_FILE = "@'\nhello\n'@ | Out-File notes.md"
TO_SCREEN = "@'\nhello\n'@"
QUOTED_TO_PYTHON = "'print(1)' | python -"
PYTHON_BY_PATH = "python script.py"

ADVICE = (
    "Write a whole file with the Write tool and change a file with Edit, never through "
    "PowerShell; only a script goes into the scratchpad, written with the Write tool and run "
    "by path. The refusal is this guard working as designed, not an event of the session: "
    "do not report it at Retro.\n"
)


def payload(**fields):
    return io.StringIO(json.dumps(fields))


def powershell(command, session="19037d1c-5d15"):
    return payload(session_id=session, tool_name="PowerShell", tool_input={"command": command})


def run(stdin, project_dir):
    err = io.StringIO()
    code = powershellguard.run([], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def log(project_dir):
    path = project_dir / "vault" / "raw" / "2026-09-14" / "event_log.md"
    return path.read_text(encoding="utf-8") if path.exists() else ""


# --- the refusals ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("command", "fed"),
    [
        (SINGLE_TO_PYTHON, "python"),
        (DOUBLE_TO_UV_PYTHON, "uv run python"),
        (SINGLE_TO_NODE, "node"),
    ],
)
def test_a_here_string_piped_into_an_interpreter_is_refused_and_logged(tmp_path, command, fed):
    code, err = run(powershell(command), tmp_path)
    assert code == 2
    assert err == f"powershellguard: here-string refused — it is piped into {fed}. {ADVICE}"
    assert log(tmp_path) == f"- 12:00:00 19037d1c powershellguard refused: it is piped into {fed}\n"


def test_the_interpreter_is_judged_by_the_function_of_the_bash_guard():
    from guppi import bashguard

    assert powershellguard.interpreter is bashguard.interpreter
    assert not hasattr(powershellguard, "INTERPRETERS")


# --- what passes ----------------------------------------------------------------------------


@pytest.mark.parametrize("command", [TO_OUT_FILE, TO_SCREEN, QUOTED_TO_PYTHON, PYTHON_BY_PATH])
def test_a_here_string_not_fed_a_quoted_string_or_a_script_by_path_passes(tmp_path, command):
    assert run(powershell(command), tmp_path) == (0, "")
    assert log(tmp_path) == ""


def test_a_bash_payload_passes(tmp_path):
    stdin = payload(tool_name="Bash", tool_input={"command": SINGLE_TO_PYTHON})
    assert run(stdin, tmp_path) == (0, "")


def test_an_unreadable_payload_passes_with_a_line_on_stderr(tmp_path):
    code, err = run(io.StringIO("not json"), tmp_path)
    assert code == 0 and "check skipped" in err


def test_cli_dispatches_to_powershellguard(tmp_path, monkeypatch):
    from guppi import cli

    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", powershell(SINGLE_TO_PYTHON))
    assert cli.main(["powershellguard"]) == 2
