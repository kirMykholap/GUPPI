"""`guppi ledger`: the `Stop` hook that lifts the lines of a LEDGER block into
`vault/raw/<hi date>/<hi HHMM>/ledger.md`, the session's folder, each with the time of
writing (case 103.1).

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
- 15:01:30 44c1aae1 hi
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


def ledger_file(project_dir, day=TODAY, session="1501"):
    """The session ledger: the `hi` of EVENT_LOG_WITH_HI is at 15:01 (case 103.1)."""
    return project_dir / "vault" / "raw" / day.isoformat() / session / "ledger.md"


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
    write_event_log(tmp_path, "- 14:00:00 44c1aae1 hi\n- 15:01:00 44c1aae1 session-start startup\n")
    code, _ = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2


def test_another_sessions_start_after_hi_leaves_the_window_open(tmp_path):
    # case 111.3: the hi carries our stamp, so a foreign start before or after it is noise
    write_event_log(tmp_path, EVENT_LOG_WITH_HI + "- 15:03:00 deadbeef session-start startup\n")
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert (code, err) == (0, "")
    assert ledger_text(tmp_path) == f"{timed(DECISION)}\n{timed(ESTIMATE)}\n"


def test_a_foreign_resume_between_our_start_and_our_hi_changes_nothing(tmp_path):
    # 2026-09-14, session M: a session restored in the same second took the unstamped hi
    write_event_log(
        tmp_path,
        "- 15:01:00 44c1aae1 session-start startup\n- 15:01:00 deadbeef session-start resume\n"
        "- 15:01:30 44c1aae1 hi\n",
    )
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert (code, err) == (0, "")
    assert ledger_file(tmp_path, session="1501").exists()


def test_a_foreign_hi_does_not_count(tmp_path):
    write_event_log(
        tmp_path,
        "- 15:01:00 44c1aae1 session-start startup\n- 15:02:00 deadbeef hi\n",
    )
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2 and "no /hi recorded for session 44c1aae1" in err


def test_an_unstamped_hi_under_our_start_is_refused(tmp_path):
    # case 136.3: the fallback of 111.6 is gone — a stamped hi is the one opener
    write_event_log(
        tmp_path,
        "- 15:01:00 44c1aae1 session-start startup\n- 15:01:30 -------- hi\n",
    )
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2 and "no /hi recorded for session 44c1aae1" in err
    assert not ledger_file(tmp_path, session="1501").exists()


def test_an_unstamped_hi_after_a_foreign_start_is_refused_and_a_stamped_one_opens(tmp_path):
    log = (
        "- 15:01:00 44c1aae1 session-start startup\n- 15:01:00 deadbeef session-start resume\n"
        "- 15:01:30 -------- hi\n"
    )
    write_event_log(tmp_path, log)
    code, _ = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2
    write_event_log(tmp_path, log + "- 15:09:00 44c1aae1 hi\n")
    code, _ = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 0
    assert ledger_file(tmp_path, session="1509").exists()


def test_the_first_stamped_hi_names_the_folder(tmp_path):
    write_event_log(tmp_path, EVENT_LOG_WITH_HI + "- 15:07:00 44c1aae1 hi\n")
    code, _ = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 0
    assert ledger_file(tmp_path, session="1501").exists()
    assert not ledger_file(tmp_path, session="1507").exists()


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


# --- case 55.1: the hi window spans the dates of the session ---------------------------

YESTERDAY = date(2026, 9, 8)
ONLY_TOOLS_TODAY = "- 00:12:00 44c1aae1 tool Bash: git status --short\n"


def test_a_start_and_hi_in_yesterdays_log_open_todays_window(tmp_path):
    # Across midnight the lines still land in the session's folder, under the hi date
    # (case 103.1): nothing is written under today.
    write_event_log(tmp_path, EVENT_LOG_WITH_HI, day=YESTERDAY)
    write_event_log(tmp_path, ONLY_TOOLS_TODAY)
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert (code, err) == (0, "")
    assert ledger_text(tmp_path, YESTERDAY) == f"{timed(DECISION)}\n{timed(ESTIMATE)}\n"
    assert not (tmp_path / "vault" / "raw" / TODAY.isoformat() / "1501").exists()


def test_a_line_already_in_a_date_level_ledger_is_not_written_again(working):
    # The shape before case 103: a ledger at the date root still counts for the dedupe.
    old = working / "vault" / "raw" / TODAY.isoformat() / "ledger.md"
    old.write_text("- 09:00:00 " + DECISION[2:] + "\n", encoding="utf-8")
    code, err = run(payload(last_assistant_message=REPLY), working)
    assert (code, err) == (0, "")
    assert ledger_text(working) == f"{timed(ESTIMATE)}\n"


def test_no_start_of_this_session_on_any_date_refuses(tmp_path):
    write_event_log(
        tmp_path,
        "- 15:01:00 deadbeef session-start startup\n- 15:01:30 -------- hi\n",
        day=YESTERDAY,
    )
    write_event_log(tmp_path, "- 00:12:00 -------- hi\n")
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2
    assert "no /hi recorded" in err


def test_another_sessions_start_today_leaves_yesterdays_window_open(tmp_path):
    write_event_log(tmp_path, EVENT_LOG_WITH_HI, day=YESTERDAY)
    write_event_log(tmp_path, "- 00:12:00 deadbeef session-start startup\n")
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert (code, err) == (0, "")
    assert ledger_text(tmp_path, YESTERDAY) == f"{timed(DECISION)}\n{timed(ESTIMATE)}\n"


def test_the_walk_stops_at_the_first_date_holding_this_sessions_start(tmp_path):
    # Two days ago: a hi under this session's start; yesterday: this session started again,
    # then another session's start closed the window. The older hi must not leak through.
    write_event_log(tmp_path, EVENT_LOG_WITH_HI, day=date(2026, 9, 7))
    write_event_log(
        tmp_path,
        "- 09:00:00 44c1aae1 session-start startup\n- 10:00:00 deadbeef session-start startup\n",
        day=YESTERDAY,
    )
    write_event_log(tmp_path, ONLY_TOOLS_TODAY)
    code, _ = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2


# --- case 55.2: the Stop hook reads the whole session back -----------------------------


def transcript_line(text, *, sidechain=False, session=SESSION, kind="assistant"):
    content = [{"type": "text", "text": text}] if kind == "assistant" else text
    return json.dumps(
        {
            "type": kind,
            "isSidechain": sidechain,
            "sessionId": session,
            "message": {"role": kind, "content": content},
        },
        ensure_ascii=False,
    )


def write_transcript(tmp_path, *lines):
    path = tmp_path / "transcript.jsonl"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(path)


def test_a_block_of_an_earlier_reply_lands_at_the_next_stop(working):
    earlier = f"Ratified.\n\n{ledger_block(DECISION)}\nRunning /pre-task now."
    transcript = write_transcript(
        working,
        transcript_line("Earlier still, no block."),
        transcript_line(earlier),
        transcript_line("user text", kind="user"),
        transcript_line("The current reply, no block."),
    )
    stdin = payload(
        last_assistant_message="The current reply, no block.", transcript_path=transcript
    )
    code, err = run(stdin, working)
    assert (code, err) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_the_transcript_and_the_last_message_are_read_once_each(working):
    transcript = write_transcript(working, transcript_line(REPLY))
    run(payload(last_assistant_message=REPLY, transcript_path=transcript), working)
    run(payload(last_assistant_message=REPLY, transcript_path=transcript), working)
    assert ledger_text(working) == f"{timed(DECISION)}\n{timed(ESTIMATE)}\n"


def test_the_current_reply_is_taken_from_the_payload_when_the_transcript_lags(working):
    transcript = write_transcript(working, transcript_line("Earlier, no block."))
    run(payload(last_assistant_message=REPLY, transcript_path=transcript), working)
    assert ledger_text(working) == f"{timed(DECISION)}\n{timed(ESTIMATE)}\n"


def test_a_subagents_block_in_the_transcript_is_ignored(working):
    transcript = write_transcript(working, transcript_line(ledger_block(LESSON), sidechain=True))
    code, err = run(payload(last_assistant_message="Nothing.", transcript_path=transcript), working)
    assert (code, err) == (0, "")
    assert not ledger_file(working).exists()


def test_a_line_in_an_earlier_days_ledger_is_not_written_again(working):
    path = ledger_file(working, YESTERDAY)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"- 20:50:18 {DECISION[2:]}\n", encoding="utf-8")
    transcript = write_transcript(working, transcript_line(ledger_block(DECISION)))
    run(payload(last_assistant_message=ledger_block(ESTIMATE), transcript_path=transcript), working)
    assert ledger_text(working) == f"{timed(ESTIMATE)}\n"


def test_a_missing_or_broken_transcript_falls_back_to_the_last_message(working):
    code, err = run(
        payload(last_assistant_message=REPLY, transcript_path=str(working / "absent.jsonl")),
        working,
    )
    assert (code, err) == (0, "")
    broken = working / "broken.jsonl"
    broken.write_text(
        "{not json\n" + transcript_line(ledger_block(LESSON)) + "\n", encoding="utf-8"
    )
    run(payload(last_assistant_message="Nothing.", transcript_path=str(broken)), working)
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(ESTIMATE), timed(LESSON)]


def test_the_refusal_counts_only_the_lines_not_yet_written(tmp_path):
    write_event_log(tmp_path, "- 15:01:00 44c1aae1 session-start startup\n")
    path = ledger_file(tmp_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"{DECISION}\n", encoding="utf-8")
    code, err = run(payload(last_assistant_message=REPLY), tmp_path)
    assert code == 2
    assert err.startswith("ledger: 1 line(s) not written")


# --- case 70: a block followed by a tool_use record of the same turn is still collected ---


def tool_use_line(session=SESSION):
    """An assistant record whose only block is a `tool_use`: the turn went on to a tool."""
    return json.dumps(
        {
            "type": "assistant",
            "isSidechain": False,
            "sessionId": session,
            "message": {
                "role": "assistant",
                "content": [
                    {
                        "type": "tool_use",
                        "id": "toolu_1",
                        "name": "Bash",
                        "input": {"command": "ls"},
                    }
                ],
            },
        }
    )


def test_a_block_followed_by_a_tool_use_record_of_the_same_turn_is_collected(working):
    text = f"Ratified.\n\n{ledger_block(DECISION)}\nRunning the tests now."
    transcript = write_transcript(
        working,
        transcript_line(text),
        tool_use_line(),
        transcript_line("tool result", kind="user"),
        transcript_line("The current reply, no block."),
    )
    fields = {
        "last_assistant_message": "The current reply, no block.",
        "transcript_path": transcript,
    }
    assert text in ledger.transcript_texts(fields)
    assert ledger.session_lines(fields) == [DECISION]
    code, err = run(payload(**fields), working)
    assert (code, err) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n"


# --- the session's folder (case 73) ------------------------------------------------------


def test_session_dir_is_the_date_and_hhmm_of_the_hi(tmp_path):
    write_event_log(tmp_path, EVENT_LOG_WITH_HI, day=YESTERDAY)
    write_event_log(tmp_path, ONLY_TOOLS_TODAY)
    folder = ledger.session_dir(tmp_path, NOW, "44c1aae1")
    assert folder == tmp_path / "vault" / "raw" / "2026-09-08" / "1501"


def test_session_dir_is_none_without_a_hi_and_survives_a_foreign_start(tmp_path):
    write_event_log(tmp_path, "- 15:01:00 44c1aae1 session-start startup\n")
    assert ledger.session_dir(tmp_path, NOW, "44c1aae1") is None
    write_event_log(tmp_path, EVENT_LOG_WITH_HI + "- 15:03:00 deadbeef session-start startup\n")
    assert ledger.session_dir(tmp_path, NOW, "44c1aae1") is not None  # case 111.3
