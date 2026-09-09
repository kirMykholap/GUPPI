"""`guppi pretask`: the `PreToolUse ExitPlanMode` hook that holds Plan Mode open until
`/pre-task` has run in this session. Rule page: `vault/wiki/rules/rule-pretask-hook.md`.

Every test feeds the payload through a stream, the shape a hook is really handed.
"""

import io
import json
from datetime import UTC, date, datetime

from guppi import pretask

TODAY = date(2026, 9, 9)
NOW = datetime(2026, 9, 9, 18, 40, 5, tzinfo=UTC)
SESSION = "44c1aae1-4076-4a58-a7c0-d20bc274047c"
START = "- 15:01:00 44c1aae1 session-start startup\n"
HI = "- 15:01:30 -------- hi\n"
PRETASK = "- 16:20:00 -------- pretask\n"
OTHER_START = "- 14:00:00 99999999 session-start startup\n"


def payload(tool="ExitPlanMode", session=SESSION):
    fields = {"session_id": session, "hook_event_name": "PreToolUse", "tool_name": tool}
    return io.StringIO(json.dumps(fields))


def with_event_log(project_dir, text):
    folder = project_dir / "vault" / "raw" / TODAY.isoformat()
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "event_log.md").write_text(text, encoding="utf-8", newline="\n")


def run(stdin, project_dir):
    err = io.StringIO()
    code = pretask.run([], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def test_pretask_after_hi_lets_the_plan_close(tmp_path):
    with_event_log(tmp_path, START + HI + PRETASK)
    assert run(payload(), tmp_path) == (0, "")


def test_hi_without_pretask_holds_plan_mode_open(tmp_path):
    with_event_log(tmp_path, START + HI)
    code, err = run(payload(), tmp_path)
    assert code == 2
    assert "/pre-task" in err and "44c1aae1" in err


def test_a_pretask_of_an_earlier_session_does_not_count(tmp_path):
    with_event_log(tmp_path, OTHER_START + HI + PRETASK + START + HI)
    code, err = run(payload(), tmp_path)
    assert code == 2
    assert "/pre-task" in err


def test_an_ordinary_session_without_hi_is_not_gated(tmp_path):
    with_event_log(tmp_path, START)
    assert run(payload(), tmp_path) == (0, "")


def test_another_tool_is_ignored(tmp_path):
    with_event_log(tmp_path, START + HI)
    assert run(payload(tool="Write"), tmp_path) == (0, "")


def test_no_event_log_means_an_ordinary_session(tmp_path):
    assert run(payload(), tmp_path) == (0, "")


def test_garbage_on_stdin_never_fails_the_session(tmp_path):
    with_event_log(tmp_path, START + HI)
    assert run(io.StringIO("not json"), tmp_path) == (0, "")


def test_cli_dispatches_to_pretask(tmp_path, monkeypatch, capsys):
    from guppi import cli

    with_event_log(tmp_path, START + HI)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", payload())
    assert cli.main(["pretask"]) == 2
    assert "/pre-task" in capsys.readouterr().err
