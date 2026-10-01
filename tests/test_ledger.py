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


def test_stop_hook_active_still_writes_the_lines(working):
    """Claude Code keeps the flag set until the person's next message (case 577.3)."""
    code, err = run(payload(last_assistant_message=REPLY, stop_hook_active=True), working)
    assert (code, err) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n{timed(ESTIMATE)}\n"


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


def test_cli_dispatches_to_ledger(tmp_path, monkeypatch, capsys, pinned_clock):
    from guppi import cli

    today = pinned_clock.date()  # the CLI reads the clock, pinned by conftest (case 145.1)

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


def person(text="go on"):
    """A message of the person: a `user` record whose `origin.kind` is `human`."""
    record = {"type": "user", "origin": {"kind": "human"}, "message": {"content": text}}
    return json.dumps(record, ensure_ascii=False)


def meta_refusal(command, text):
    """A refusal of the `Stop` hook `command`, as Claude Code records it (session 1441)."""
    content = f"Stop hook feedback:\n[{command}]: {text}"
    record = {"type": "user", "isMeta": True, "message": {"content": content}}
    return json.dumps(record, ensure_ascii=False)


def own_refusal(text):
    return meta_refusal(ledger.COMMAND, text)


def write_transcript(tmp_path, *lines):
    path = tmp_path / "transcript.jsonl"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(path)


def test_a_block_of_an_earlier_reply_lands_at_the_next_stop(working):
    earlier = f"Ratified.\n\n{ledger_block(DECISION)}\nRunning /pre-spec now."
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


# --- what a session changes, it does not measure (case 428.1) ----------------------------
# `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`

READ_X = "- estimate[estimate-x-holds][passed] 2026-09-09, pytest; green"
CREATE_X = "- decision[case 3][create][estimate-x-holds]{ref:rule-x}{tags:harness}"
UPDATE_X = "- decision[case 4][update][estimate-x-holds]{ref:estimate-x-holds}"
DEFER_X = "- decision[case 5][defer][estimate-x-holds]"
REFUSAL = (
    "ledger: estimate[estimate-x-holds] not written — case {} creates or updates "
    "estimate-x-holds in this session; what a session changes it does not measure: take the "
    "reading in a later session and name it in the handoff.\n"
)


def seed_ledger(project_dir, *lines):
    path = ledger_file(project_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"- 15:01:50 {line[2:]}\n" for line in lines), encoding="utf-8")


@pytest.mark.parametrize("decision, case", [(CREATE_X, "3"), (UPDATE_X, "4")])
def test_a_reading_of_a_slug_the_session_changes_is_refused(working, decision, case):
    seed_ledger(working, decision)
    code, err = run(payload(last_assistant_message=ledger_block(READ_X, LESSON)), working)
    assert (code, err) == (2, REFUSAL.format(case))
    assert ledger_text(working).splitlines() == [f"- 15:01:50 {decision[2:]}", timed(LESSON)]


def test_a_decision_line_of_the_same_reply_refuses_it_too(working):
    code, err = run(payload(last_assistant_message=ledger_block(UPDATE_X, READ_X)), working)
    assert (code, err) == (2, REFUSAL.format("4"))
    assert ledger_text(working) == f"{timed(UPDATE_X)}\n"


def test_a_refused_line_of_an_earlier_text_is_skipped_without_a_word(working):
    seed_ledger(working, UPDATE_X)
    transcript = write_transcript(working, transcript_line(ledger_block(READ_X)))
    stdin = payload(last_assistant_message="Nothing.", transcript_path=transcript)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working) == f"- 15:01:50 {UPDATE_X[2:]}\n"


def test_a_reading_with_a_defer_line_only_or_another_sessions_line_is_written(working):
    seed_ledger(working, DEFER_X)
    other = ledger_file(working, YESTERDAY)
    other.parent.mkdir(parents=True, exist_ok=True)
    other.write_text(f"- 20:50:18 {UPDATE_X[2:]}\n", encoding="utf-8")
    assert run(payload(last_assistant_message=ledger_block(READ_X)), working) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(READ_X)


# --- a lesson slug carries its prefix (case 460.5) ----------------------------------------
# `estimate-ledger-write-refuses-a-lesson-without-its-prefix`

BARE_LESSON = "- lesson[knowledge][harness-x-renders-y] trigger: a root_cause: b"
LESSON_REFUSAL = (
    "ledger: lesson[harness-x-renders-y] not written — a lesson slug starts with lesson-, "
    "then the area, then the cause: write the line again with the prefix.\n"
)


def test_a_lesson_without_its_prefix_in_the_finished_reply_is_refused_aloud(working):
    reply = ledger_block(DECISION, BARE_LESSON, LESSON, ESTIMATE)
    code, err = run(payload(last_assistant_message=reply), working)
    assert (code, err) == (2, LESSON_REFUSAL)
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(LESSON), timed(ESTIMATE)]


def test_a_lesson_without_its_prefix_in_an_earlier_text_is_skipped_without_a_word(working):
    transcript = write_transcript(working, transcript_line(ledger_block(BARE_LESSON, DECISION)))
    stdin = payload(last_assistant_message="Nothing.", transcript_path=transcript)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_both_refusals_speak_in_one_stop(working):
    seed_ledger(working, UPDATE_X)
    code, err = run(payload(last_assistant_message=ledger_block(READ_X, BARE_LESSON)), working)
    assert (code, err) == (2, REFUSAL.format("4") + LESSON_REFUSAL)
    assert ledger_text(working) == f"- 15:01:50 {UPDATE_X[2:]}\n"


def test_a_lesson_line_already_in_a_ledger_is_not_judged(working):
    other = ledger_file(working, YESTERDAY)
    other.parent.mkdir(parents=True, exist_ok=True)
    other.write_text(f"- 20:50:18 {BARE_LESSON[2:]}\n", encoding="utf-8")
    code, err = run(payload(last_assistant_message=ledger_block(BARE_LESSON, DECISION)), working)
    assert (code, err) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_an_estimate_or_decision_line_without_a_prefix_is_not_refused_by_this_check(working):
    estimate = "- estimate[y-holds][passed] 2026-09-09, pytest; green"
    decision = "- decision[case 7][create][z-holds]{ref:rule-x}"
    code, err = run(payload(last_assistant_message=ledger_block(estimate, decision)), working)
    assert (code, err) == (0, "")
    assert ledger_text(working).splitlines() == [timed(estimate), timed(decision)]


# --- a lesson's mark names a decision line before it (case 497.1) -------------------------
# `estimate-ledger-write-refuses-a-mark-with-no-decision-line`

SUB_1 = "- decision[case 8.1][update][rule-x]{ref:rule-x}"
SUB_2 = "- decision[case 8.2][update][rule-y]{ref:rule-y}"
CASE_9 = "- decision[case 9][update][rule-z]{ref:rule-z}"
MARK_PARENT = (
    "- lesson[error][lesson-a-b]{tags:hooks}{addressed_by:case 8} trigger: t root_cause: r"
)
MARK_SUB = "- lesson[error][lesson-a-c]{tags:hooks}{addressed_by:case 8.1} trigger: t root_cause: r"
MARK_9 = "- lesson[error][lesson-a-d]{tags:hooks}{addressed_by:case 9} trigger: t root_cause: r"
BARE_MARKED = "- lesson[error][a-e]{addressed_by:case 8} trigger: t root_cause: r"


def mark_refusal(slug, case, subs=()):
    named = "; its sub-cases have " + ", ".join(f"case {s}" for s in subs) if subs else ""
    return (
        f"ledger: lesson[{slug}] not written — {{addressed_by:case {case}}} names no decision "
        f"line before it in this session{named}: write the line again after the decision line "
        "of the Case that closed the cause, naming that Case.\n"
    )


def test_a_mark_to_a_parent_with_sub_case_lines_is_refused_aloud(working):
    reply = ledger_block(SUB_1, SUB_2, MARK_PARENT)
    code, err = run(payload(last_assistant_message=reply), working)
    assert (code, err) == (2, mark_refusal("lesson-a-b", "8", ("8.1", "8.2")))
    assert ledger_text(working).splitlines() == [timed(SUB_1), timed(SUB_2)]


def test_a_mark_to_a_case_with_no_line_is_refused_aloud_with_no_sub_case_part(working):
    code, err = run(payload(last_assistant_message=ledger_block(DECISION, MARK_9)), working)
    assert (code, err) == (2, mark_refusal("lesson-a-d", "9"))
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_a_mark_above_its_decision_line_in_the_same_block_is_refused(working):
    code, err = run(payload(last_assistant_message=ledger_block(MARK_9, CASE_9)), working)
    assert (code, err) == (2, mark_refusal("lesson-a-d", "9"))
    assert ledger_text(working) == f"{timed(CASE_9)}\n"


def test_a_marked_line_of_an_earlier_text_waits_then_lands_without_a_word(working):
    transcript = write_transcript(working, transcript_line(ledger_block(MARK_9)))
    stdin = payload(last_assistant_message="Nothing.", transcript_path=transcript)
    assert run(stdin, working) == (0, "")
    assert not ledger_file(working).exists()  # its Case has no line yet
    stdin = payload(last_assistant_message=ledger_block(CASE_9), transcript_path=transcript)
    assert run(stdin, working) == (0, "")  # the decision line lands; the lesson stood above it
    assert ledger_text(working) == f"{timed(CASE_9)}\n"
    stdin = payload(last_assistant_message="Nothing.", transcript_path=transcript)
    assert run(stdin, working) == (0, "")  # the next Stop: its decision line stands before it
    assert ledger_text(working).splitlines() == [timed(CASE_9), timed(MARK_9)]


def test_a_mark_with_its_decision_line_before_it_is_written(working):
    seed_ledger(working, CASE_9)
    code, err = run(payload(last_assistant_message=ledger_block(SUB_1, MARK_SUB, MARK_9)), working)
    assert (code, err) == (0, "")
    assert ledger_text(working).splitlines()[1:] == [timed(SUB_1), timed(MARK_SUB), timed(MARK_9)]


def test_a_lesson_with_no_mark_is_written_whatever_the_marks(working):
    code, err = run(payload(last_assistant_message=ledger_block(LESSON)), working)
    assert (code, err) == (0, "")
    assert ledger_text(working) == f"{timed(LESSON)}\n"


def test_a_line_with_no_prefix_and_a_bad_mark_gets_the_prefix_line_alone(working):
    code, err = run(payload(last_assistant_message=ledger_block(BARE_MARKED, DECISION)), working)
    assert code == 2
    assert err == (
        "ledger: lesson[a-e] not written — a lesson slug starts with lesson-, then the area, "
        "then the cause: write the line again with the prefix.\n"
    )
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_a_marked_line_already_in_a_ledger_is_not_judged(working):
    other = ledger_file(working, YESTERDAY)
    other.parent.mkdir(parents=True, exist_ok=True)
    other.write_text(f"- 20:50:18 {MARK_PARENT[2:]}\n", encoding="utf-8")
    code, err = run(payload(last_assistant_message=ledger_block(MARK_PARENT, DECISION)), working)
    assert (code, err) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_the_hook_and_materialize_judge_a_mark_alike(working):
    """One ledger, two callers of `marks_without_decision`: the lessons the hook refuses are
    the lessons `materialize` leaves `incomplete: [addressed_by]` (case 497.1)."""
    import yaml

    from guppi import materialize

    lines = [SUB_1, MARK_PARENT, MARK_SUB, MARK_9, CASE_9, LESSON]
    code, _ = run(payload(last_assistant_message=ledger_block(*lines)), working)
    assert code == 2
    written = {ledger.BRACKET.findall(line)[1] for line in ledger_text(working).splitlines()}
    hook_refused = {"lesson-a-b", "lesson-a-c", "lesson-a-d", "lesson-x"} - written

    unit = working / "vault" / "raw" / "2026-09-10"
    unit.mkdir(parents=True)
    (unit / "ledger.md").write_text(
        "".join(f"{timed(line)}\n" for line in lines), encoding="utf-8", newline="\n"
    )
    (working / "vault" / "wiki").mkdir(parents=True)
    (working / "vault" / "wiki" / "sprint.md").write_text("# Sprint\n\n## migration\n")
    materialize.run(
        ["--date", "2026-09-10"], stdout=io.StringIO(), stderr=io.StringIO(), project_dir=working
    )
    data = yaml.safe_load((unit / "materialize.yaml").read_text(encoding="utf-8"))
    incomplete = {
        e["slug"]
        for e in data["entries"]
        if e.get("kind") == "lesson" and "addressed_by" in (e.get("incomplete") or [])
    }
    assert hook_refused == incomplete == {"lesson-a-b", "lesson-a-d"}


# --- a line the grammar does not read (case 552.2) ----------------------------------------
# `estimate-ledger-write-refuses-a-line-it-cannot-read`

BROKEN = "- estimate[estimate-x-holds] note [passed] 2026-09-09, pytest; green"
BROKEN_LESSON = "- lesson[wrong][harness-x] trigger: a root_cause: b {addressed_by:case 99}"
BROKEN_REFUSAL = (
    "ledger: line not written — the grammar of a ledger line does not read it: {}. "
    "Write it again in the form of the table in case-schema.md.\n"
)


def test_a_broken_line_in_the_finished_reply_is_refused_aloud(working):
    reply = ledger_block(DECISION, BROKEN, LESSON)
    code, err = run(payload(last_assistant_message=reply), working)
    assert (code, err) == (2, BROKEN_REFUSAL.format(BROKEN[2:]))
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(LESSON)]


def test_a_broken_line_of_an_earlier_text_is_skipped_without_a_word(working):
    transcript = write_transcript(working, transcript_line(ledger_block(BROKEN, DECISION)))
    stdin = payload(last_assistant_message="Nothing.", transcript_path=transcript)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_a_broken_lesson_line_gets_no_refusal_for_its_prefix_or_mark(working):
    code, err = run(payload(last_assistant_message=ledger_block(BROKEN_LESSON)), working)
    assert (code, err) == (2, BROKEN_REFUSAL.format(BROKEN_LESSON[2:]))
    assert not ledger_file(working).exists()


def test_a_space_between_brackets_is_written_as_a_record(working):
    spaced = READ_X.replace("][", "] [")
    assert run(payload(last_assistant_message=ledger_block(spaced)), working) == (0, "")
    assert ledger_text(working) == f"{timed(spaced)}\n"


# --- the hook's own error (case 552.4) ------------------------------------------------------
# `estimate-ledger-write-exits-2-on-an-error`


def fail_to_append(path, lines):
    raise OSError("disk full")


def test_an_error_after_the_payload_is_read_exits_2(working, monkeypatch):
    monkeypatch.setattr(ledger, "append", fail_to_append)
    code, err = run(payload(last_assistant_message=ledger_block(DECISION)), working)
    assert (code, err) == (2, "ledger: ledger.md not written: disk full\n")


def test_an_error_with_the_flag_and_no_readable_transcript_exits_0(working, monkeypatch):
    monkeypatch.setattr(ledger, "append", fail_to_append)
    stdin = payload(last_assistant_message=ledger_block(DECISION), stop_hook_active=True)
    assert run(stdin, working) == (0, "")
    assert not ledger_file(working).exists()


def test_an_error_with_its_own_refusal_in_the_stretch_exits_0(working, monkeypatch):
    monkeypatch.setattr(ledger, "append", fail_to_append)
    path = write_transcript(
        working, person(), own_refusal("ledger: ledger.md not written: disk full")
    )
    stdin = payload(last_assistant_message=ledger_block(DECISION), transcript_path=path)
    assert run(stdin, working) == (0, "")


def test_an_error_after_another_hooks_refusal_with_the_flag_exits_2(working, monkeypatch):
    monkeypatch.setattr(ledger, "append", fail_to_append)
    path = write_transcript(working, person(), meta_refusal("uv run guppi onward --plan", "go"))
    stdin = payload(
        last_assistant_message=ledger_block(DECISION), transcript_path=path, stop_hook_active=True
    )
    assert run(stdin, working) == (2, "ledger: ledger.md not written: disk full\n")


# --- the stretch: each refusal once from one message of the person to the next (case 577) --
# `estimate-ledger-write-lifts` and the four refusals


def stretch(project_dir, *records):
    """A transcript of the person's message, then the given records — refusals of hooks."""
    return write_transcript(project_dir, person(), *records)


def test_a_refused_line_already_told_is_silent_and_a_new_one_is_told(working):
    told = BROKEN_REFUSAL.format(BROKEN[2:]).rstrip("\n")
    path = stretch(working, own_refusal(told))
    stdin = payload(last_assistant_message=ledger_block(BROKEN), transcript_path=path)
    assert run(stdin, working) == (0, "")  # a repeat of the same faulty line
    stdin = payload(last_assistant_message=ledger_block(BARE_LESSON), transcript_path=path)
    assert run(stdin, working) == (2, LESSON_REFUSAL)  # a new faulty line in the stretch


def test_a_refusal_told_before_the_persons_last_message_is_told_again(working):
    told = BROKEN_REFUSAL.format(BROKEN[2:]).rstrip("\n")
    path = write_transcript(working, own_refusal(told), person())
    stdin = payload(last_assistant_message=ledger_block(BROKEN), transcript_path=path)
    assert run(stdin, working) == (2, BROKEN_REFUSAL.format(BROKEN[2:]))


def test_no_hi_is_told_once_a_stretch(tmp_path):
    stdin = payload(last_assistant_message=REPLY, transcript_path=stretch(tmp_path))
    code, err = run(stdin, tmp_path)
    assert code == 2 and "no /hi recorded" in err
    path = stretch(tmp_path, own_refusal(err.rstrip("\n")))
    assert run(payload(last_assistant_message=REPLY, transcript_path=path), tmp_path) == (0, "")
    assert not ledger_file(tmp_path).exists()


def test_with_the_flag_and_no_readable_transcript_it_writes_and_says_nothing(working):
    stdin = payload(last_assistant_message=ledger_block(DECISION, BROKEN), stop_hook_active=True)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def flagged(project_dir, reply):
    """A Stop with the flag set after another hook's refusal in the stretch."""
    path = stretch(project_dir, meta_refusal("uv run guppi onward --plan", "go on"))
    return payload(last_assistant_message=reply, transcript_path=path, stop_hook_active=True)


def test_flag_a_line_the_grammar_cannot_read_is_refused_aloud(working):
    code, err = run(flagged(working, ledger_block(DECISION, BROKEN)), working)
    assert (code, err) == (2, BROKEN_REFUSAL.format(BROKEN[2:]))
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_flag_a_reading_of_a_change_of_the_session_is_refused_aloud(working):
    seed_ledger(working, UPDATE_X)
    assert run(flagged(working, ledger_block(READ_X)), working) == (2, REFUSAL.format("4"))
    assert ledger_text(working) == f"- 15:01:50 {UPDATE_X[2:]}\n"


def test_flag_a_lesson_without_its_prefix_is_refused_aloud(working):
    code, err = run(flagged(working, ledger_block(DECISION, BARE_LESSON)), working)
    assert (code, err) == (2, LESSON_REFUSAL)
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_flag_a_mark_with_no_decision_line_waits_then_lands(working):
    code, err = run(flagged(working, ledger_block(MARK_9)), working)
    assert (code, err) == (2, mark_refusal("lesson-a-d", "9"))
    assert not ledger_file(working).exists()
    path = write_transcript(
        working,
        person(),
        transcript_line(ledger_block(MARK_9)),
        own_refusal(mark_refusal("lesson-a-d", "9").rstrip("\n")),
    )
    reply = ledger_block(CASE_9)
    stdin = payload(last_assistant_message=reply, transcript_path=path, stop_hook_active=True)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working) == f"{timed(CASE_9)}\n"
    assert run(payload(last_assistant_message="Nothing.", transcript_path=path), working) == (
        0,
        "",
    )
    assert ledger_text(working).splitlines() == [timed(CASE_9), timed(MARK_9)]


def test_a_payload_that_cannot_be_read_exits_0_with_the_error(working, monkeypatch):
    def fail(stdin):
        raise ValueError("not JSON")

    monkeypatch.setattr(ledger, "read_payload", fail)
    code, err = run(io.StringIO("{"), working)
    assert (code, err) == (0, "ledger: ledger.md not written: not JSON\n")
    assert not ledger_file(working).exists()
