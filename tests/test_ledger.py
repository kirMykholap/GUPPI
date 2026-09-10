"""`guppi ledger`: the `Stop` hook that lifts the lines of a LEDGER block into
`vault/raw/<date>/ledger.md`, each with the time of writing.

Every test feeds the payload through a stream, the shape a hook is really handed.
"""

import io
import json
from datetime import UTC, date, datetime

import pytest

from guppi import ledger

TODAY = date(2026, 9, 9)
NOW = datetime(2026, 9, 9, 15, 2, 11, tzinfo=UTC)
SESSION = "44c1aae1-4076-4a58-a7c0-d20bc274047c"

DECISION = "- decision[case 10][create][rule-ledger-write]{ref:rule-session-start}"
ESTIMATE = "- estimate[estimate-hi-no-read-calls][passed] all five in context, no read call"
LESSON = "- lesson[error][lesson-x] trigger: a root_cause: b"
PREVIEW = "- decision[case 10][create][estimate-ledger-write-lifts]{ref:rule-ledger-write}"
REPLY = f"""Ratified. Recording:

```LEDGER
{DECISION}
{ESTIMATE}
```

The preview in `then` was:

```
{PREVIEW}
```

{PREVIEW}
"""

EVENT_LOG_WITH_HI = """- 15:01:00 44c1aae1 session-start startup
- 15:01:30 -------- hi
- 15:02:00 44c1aae1 tool Bash: git status --short
"""


def timed(line):
    return "- 15:02:11 " + line[2:]


def ledger_block(*lines):
    return "```LEDGER\n" + "\n".join(lines) + "\n```\n"


def payload(**fields):
    fields.setdefault("session_id", SESSION)
    fields.setdefault("hook_event_name", "Stop")
    return io.StringIO(json.dumps(fields, ensure_ascii=False))


def write_event_log(project_dir, text, day=TODAY):
    path = project_dir / "vault" / "raw" / day.isoformat() / "event_log.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def ledger_file(project_dir, day=TODAY):
    return project_dir / "vault" / "raw" / day.isoformat() / "ledger.md"


def ledger_text(project_dir, day=TODAY):
    return ledger_file(project_dir, day).read_text(encoding="utf-8")


def run(stdin, project_dir):
    err = io.StringIO()
    code = ledger.run([], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


@pytest.fixture
def working(tmp_path):
    write_event_log(tmp_path, EVENT_LOG_WITH_HI)
    return tmp_path


def test_ledger_block_lines_land_timed_and_other_lines_never(working):
    code, err = run(payload(last_assistant_message=REPLY), working)
    assert (code, err) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n{timed(ESTIMATE)}\n"


def test_the_tag_is_case_insensitive_and_may_follow_spaces(working):
    reply = f"``` ledger\n{DECISION}\n```\n"
    run(payload(last_assistant_message=reply), working)
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_a_block_with_another_tag_is_a_preview(tmp_path):
    reply = f"```text\n{DECISION}\n```\n```markdown\n{ESTIMATE}\n```\n"
    code, err = run(payload(last_assistant_message=reply), tmp_path)
    assert (code, err) == (0, "")
    assert not ledger_file(tmp_path).exists()


def test_running_twice_on_the_same_reply_adds_nothing(working):
    run(payload(last_assistant_message=REPLY), working)
    run(payload(last_assistant_message=REPLY), working)
    assert ledger_text(working) == f"{timed(DECISION)}\n{timed(ESTIMATE)}\n"


def test_a_line_repeated_in_a_later_reply_adds_nothing(working):
    run(payload(last_assistant_message=REPLY), working)
    run(payload(last_assistant_message=ledger_block(DECISION, LESSON)), working)
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(ESTIMATE), timed(LESSON)]


def test_a_line_written_by_hand_without_a_time_counts_as_present(working):
    path = ledger_file(working)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"<!-- by hand -->\n{DECISION}\n", encoding="utf-8")
    run(payload(last_assistant_message=REPLY), working)
    assert ledger_text(working).splitlines() == ["<!-- by hand -->", DECISION, timed(ESTIMATE)]


def test_without_hi_the_hook_refuses_with_count_and_session(tmp_path):
    write_event_log(tmp_path, "- 15:01:00 44c1aae1 session-start startup\n")
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2
    assert err == (
        "ledger: 2 line(s) not written — no /hi recorded for session 44c1aae1. "
        "Tell the person; run /hi, then repeat the lines.\n"
    )
    assert not ledger_file(tmp_path).exists()


def test_without_an_event_log_the_hook_refuses(tmp_path):
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2
    assert "no /hi recorded" in err


def test_hi_before_this_sessions_start_does_not_count(tmp_path):
    write_event_log(tmp_path, "- 14:00:00 -------- hi\n- 15:01:00 44c1aae1 session-start startup\n")
    code, _ = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2


def test_another_sessions_start_after_hi_closes_the_window(tmp_path):
    write_event_log(tmp_path, EVENT_LOG_WITH_HI + "- 15:03:00 deadbeef session-start startup\n")
    code, _ = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2


def test_a_compact_or_resume_of_the_same_session_keeps_the_window_open(tmp_path):
    write_event_log(
        tmp_path,
        EVENT_LOG_WITH_HI
        + "- 15:03:00 44c1aae1 session-start compact\n- 15:04:00 44c1aae1 session-start resume\n",
    )
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert (code, err) == (0, "")
    assert ledger_text(tmp_path) == f"{timed(DECISION)}\n{timed(ESTIMATE)}\n"


def test_stop_hook_active_exits_zero_and_writes_nothing(tmp_path):
    code, err = run(payload(last_assistant_message=REPLY, stop_hook_active=True), tmp_path)
    assert (code, err) == (0, "")
    assert not ledger_file(tmp_path).exists()


def test_a_reply_without_a_ledger_block_creates_no_ledger(tmp_path):
    reply = f"Nothing here.\n{DECISION}\n  - decision[case 1][create][x]\n```\n{LESSON}\n```\n"
    code, err = run(payload(last_assistant_message=reply), tmp_path)
    assert (code, err) == (0, "")
    assert not ledger_file(tmp_path).exists()


def test_a_tilde_ledger_block_records_too(working):
    run(payload(last_assistant_message=f"~~~LEDGER\n{DECISION}\n~~~\n{ESTIMATE}\n"), working)
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_a_utf8_line_is_written_verbatim(working):
    line = "- lesson[error][lesson-hooks-windows-stdin-encoding] trigger: пустой файл — «probe»"
    raw = json.dumps(
        {"session_id": SESSION, "last_assistant_message": ledger_block(line)}, ensure_ascii=False
    )
    stdin = io.TextIOWrapper(
        io.BytesIO(raw.encode("utf-8")), encoding="cp1252", errors="surrogateescape"
    )
    run(stdin, working)
    assert ledger_text(working) == timed(line) + "\n"


def test_empty_stdin_is_a_reply_with_no_lines(tmp_path):
    code, err = run(io.StringIO(""), tmp_path)
    assert (code, err) == (0, "")


def test_cli_dispatches_to_ledger(tmp_path, monkeypatch, capsys):
    from guppi import cli

    today = datetime.now().astimezone().date()  # the CLI reads the real clock

    write_event_log(tmp_path, EVENT_LOG_WITH_HI, day=today)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", payload(last_assistant_message=ledger_block(DECISION)))
    assert cli.main(["ledger"]) == 0
    assert capsys.readouterr().err == ""
    written = ledger_text(tmp_path, day=today).splitlines()[0]
    assert written.startswith("- ") and written.endswith(DECISION[2:])
