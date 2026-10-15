"""`guppi ledger`: the `Stop` hook that lifts the lines of a LEDGER block into
`vault/raw/<hi date>/<hi HHMM>/ledger.md`, the session's folder, each with the time of
writing (case 103.1).

Every test feeds the payload through a stream, the shape a hook is really handed.
"""

import importlib
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
# The decision lines of these tests, each a line of the Case `case-guppi` stored (case 688.7).
STORED = (
    DECISION,
    PREVIEW,
    "- decision[case 3][create][estimate-x-holds]{ref:rule-x}{tags:harness}",
    "- decision[case 4][update][estimate-x-holds]{ref:estimate-x-holds}",
    "- decision[case 7][create][z-holds]{ref:rule-x}",
    "- decision[case 8.1][update][rule-x]{ref:rule-x}",
    "- decision[case 8.2][update][rule-y]{ref:rule-y}",
    "- decision[case 9][update][rule-z]{ref:rule-z}",
    "- decision[case 12][create][entity-sprint-next]{ref:entity-sprint}{tags:sprint}",
)


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
    plan = project_dir / ".claude" / "plans" / "plan.md"
    path.write_text(text + f"- 15:01:40 44c1aae1 tool Write: {plan}\n", encoding="utf-8")
    sprint_page(project_dir)
    store_cases(project_dir, *STORED)


def store_cases(project_dir, *lines):
    """The plan file of the session and its store `<plan>.checked.json`, one entry per Case
    holding these decision lines in its `ratification`, so the hook writes them (case 688.7)."""
    from guppi.casecheck import read_store, store_of

    plan = project_dir / ".claude" / "plans" / "plan.md"
    plan.parent.mkdir(parents=True, exist_ok=True)
    if not plan.exists():
        plan.write_text("# Spec\n", encoding="utf-8")
    cases: dict[str, list[str]] = {}
    for line in lines:
        cases.setdefault(ledger.BRACKET.search(line).group(1)[5:], []).append(line)
    store = read_store(plan)
    for case, own in cases.items():
        fence = "\n".join(f"> {line}" for line in own)
        store[case] = {
            "text": f"### Case {case} — x\n\n> **ratification:**\n> ```\n{fence}\n> ```",
            "findings": [],
            "agent_id": "a",
        }
    store_of(plan).write_text(json.dumps(store, ensure_ascii=False), encoding="utf-8")
    return plan


def sprint_page(project_dir, slug="entity-sprint-migration"):
    """A live sprint page, so a decision line is not refused for a missing sprint (case 628.3)."""
    path = project_dir / "vault" / "wiki" / "entities" / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\ntype: entity\nstatus: draft\n---\n", encoding="utf-8")
    return path


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
    reply = ledger_block(DECISION, LESSON)
    run(payload(last_assistant_message=reply, transcript_path=asked(working)), working)
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
    # the hi carries our stamp, so a foreign start before or after it is noise (case 111.3)
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
    # the fallback of 111.6 is gone — a stamped hi is the one opener (case 136.3)
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


# --- the hi window spans the dates of the session (case 55.1) ---------------------------

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
    # The shape before a ledger per session: a ledger at the date root still counts for the
    # dedupe (case 103).
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


# --- the Stop hook reads the whole session back (case 55.2) -----------------------------


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


def asked(project_dir, slug="lesson-x"):
    """A stretch in which the hook already asked for the mark of `lesson[<slug>]` (case
    682.1): the unmarked line written again lands as it stands."""
    held = ledger.held_message(slug)
    return write_transcript(project_dir, person(), own_refusal(held))


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


# --- a block followed by a tool_use record of the same turn is still collected (case 70) ---


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
    assert ledger.session_dir(tmp_path, NOW, "44c1aae1") is not None  # (case 111.3)


# --- what a session changes, it does not measure (case 428.1) ----------------------------
# `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`

READ_X = "- estimate[estimate-x-holds][passed] 2026-09-09, pytest; green"
CREATE_X = "- decision[case 3][create][estimate-x-holds]{ref:rule-x}{tags:harness}"
UPDATE_X = "- decision[case 4][update][estimate-x-holds]{ref:estimate-x-holds}"
DEFER_X = "- decision[case 5][defer][estimate-x-holds]"
REFUSAL = (
    "ledger: estimate[estimate-x-holds] not written — case {} creates or updates "
    "estimate-x-holds in this session; the reading is taken at the Retro of this session: "
    "write it in the reply that ends Retro.\n"
)


def seed_ledger(project_dir, *lines):
    path = ledger_file(project_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"- 15:01:50 {line[2:]}\n" for line in lines), encoding="utf-8")


@pytest.mark.parametrize("decision, case", [(CREATE_X, "3"), (UPDATE_X, "4")])
def test_a_reading_of_a_slug_the_session_changes_is_refused(working, decision, case):
    seed_ledger(working, decision)
    reply = ledger_block(READ_X, LESSON)
    path = asked(working)
    code, err = run(payload(last_assistant_message=reply, transcript_path=path), working)
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


# --- the reading waits for the Retro of the session (case 670.1) -------------------------

EVENT_LOG_WITH_RETRO = EVENT_LOG_WITH_HI + "- 15:01:55 44c1aae1 retro\n"


def stamped(text, at):
    """An assistant record of the transcript with its timestamp."""
    record = json.loads(transcript_line(text))
    record["timestamp"] = at
    return json.dumps(record, ensure_ascii=False)


def test_a_reading_of_a_changed_slug_is_written_once_retro_has_opened(working):
    write_event_log(working, EVENT_LOG_WITH_RETRO)
    seed_ledger(working, UPDATE_X)
    assert run(payload(last_assistant_message=ledger_block(READ_X)), working) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(READ_X)


def test_the_mark_of_another_session_or_before_the_hi_does_not_open_it(working):
    log = "- 15:00:30 44c1aae1 retro\n" + EVENT_LOG_WITH_HI + "- 15:01:55 deadbeef retro\n"
    write_event_log(working, log)
    seed_ledger(working, UPDATE_X)
    code, err = run(payload(last_assistant_message=ledger_block(READ_X)), working)
    assert (code, err) == (2, REFUSAL.format("4"))


def test_a_line_of_a_reply_before_the_mark_stays_refused_without_a_word(working):
    write_event_log(working, EVENT_LOG_WITH_RETRO)
    seed_ledger(working, UPDATE_X)
    early = (datetime(2026, 9, 9, 15, 1, 40).astimezone()).isoformat()
    transcript = write_transcript(working, stamped(ledger_block(READ_X), early))
    stdin = payload(last_assistant_message=ledger_block(READ_X), transcript_path=transcript)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working) == f"- 15:01:50 {UPDATE_X[2:]}\n"


def test_a_line_of_a_reply_after_the_mark_is_written(working):
    write_event_log(working, EVENT_LOG_WITH_RETRO)
    seed_ledger(working, UPDATE_X)
    late = (datetime(2026, 9, 9, 15, 2, 5).astimezone()).isoformat()
    transcript = write_transcript(working, stamped(ledger_block(READ_X), late))
    stdin = payload(last_assistant_message="Done.", transcript_path=transcript)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(READ_X)


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
    code, err = run(payload(last_assistant_message=reply, transcript_path=asked(working)), working)
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


# --- a lesson takes a tag of tags.md (case 703.2) ------------------------------------------
# `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`

TAGGED = "- lesson[error][lesson-t-u]{tags:hooks,nope} trigger: t root_cause: r"
LISTED = "- lesson[error][lesson-t-v]{tags:hooks} trigger: t root_cause: r"
DECLARE = "- decision[case 20][update][rule-x]{ref:rule-x}"
DECLARING_CASE = """## Case 20 — a tag declared

> **context:**
> Context.

> **problem:**
> Problem.

> **recommend:**
> Advice.

> **given:**
> `rule-x` — the rule.

> **when:**
> The agent runs `guppi x`.

> **then:**
> The page changes.

> **tasks:**
> - [ ] update `rule-x`
>   - change: `the tag nope declared (case 20)`
> - [ ] tag `nope`
>   - meaning: `a tag declared in the session`
>   - aliases: `тег`

> **ratification:**
> ```
> - decision[case 20][update][rule-x]{ref:rule-x}
> ```"""


def tags_md(project_dir, *tags):
    path = project_dir / "vault" / "wiki" / "tags.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = "".join(f"| {tag} | a tag | тег |\n" for tag in tags)
    path.write_text(f"# Tags\n\n| tag | meaning | aliases (ru) |\n|---|---|---|\n{rows}", "utf-8")


def declaring_case(project_dir):
    """The store holds Case `20`, whose tag line declares `nope`."""
    from guppi.casecheck import read_store, store_of

    plan = project_dir / ".claude" / "plans" / "plan.md"
    store = read_store(plan)
    store["20"] = {"text": DECLARING_CASE, "findings": [], "agent_id": "a"}
    store_of(plan).write_text(json.dumps(store, ensure_ascii=False), encoding="utf-8")


def test_unlisted_tag_in_the_finished_reply_is_refused_aloud_and_the_rest_lands(working):
    tags_md(working, "hooks")
    code, err = run(payload(last_assistant_message=ledger_block(ESTIMATE, TAGGED, LISTED)), working)
    assert (code, err) == (2, ledger.tag_message("lesson-t-u", ["nope"]) + "\n")
    assert "or declare the tag on the line by {newtag:<tag>|<meaning>|<aliases>}" in err
    assert "handoff" not in err
    assert ledger_text(working).splitlines() == [timed(ESTIMATE), timed(LISTED)]


# --- a lesson line declares its own new tag (case 827.1) -----------------------------------
# `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`

DECLARED = (
    "- lesson[error][lesson-t-w]{tags:hooks,nope}{newtag:nope|a tag a lesson declares|тег}"
    " trigger: t root_cause: r"
)


def test_unlisted_tag_declared_on_the_line_itself_lands(working):
    tags_md(working, "hooks")
    assert run(payload(last_assistant_message=ledger_block(DECLARED)), working) == (0, "")
    assert ledger_text(working).splitlines() == [timed(DECLARED)]


def test_unlisted_tag_declared_on_a_lesson_line_of_the_sessions_ledger_lands(working):
    tags_md(working, "hooks")
    seed_ledger(working, DECLARED)
    assert run(payload(last_assistant_message=ledger_block(TAGGED)), working) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(TAGGED)


def test_unlisted_tag_declared_on_another_line_of_the_same_stop_lands(working):
    tags_md(working, "hooks")
    assert run(payload(last_assistant_message=ledger_block(DECLARED, TAGGED)), working) == (0, "")
    assert ledger_text(working).splitlines() == [timed(DECLARED), timed(TAGGED)]


def test_unlisted_tag_a_block_outside_its_tags_or_with_empty_aliases_declares_nothing(working):
    tags_md(working, "hooks")
    outside = (
        "- lesson[error][lesson-t-x]{tags:hooks}{newtag:nope|a tag|тег} trigger: t root_cause: r"
    )
    code, err = run(payload(last_assistant_message=ledger_block(outside, TAGGED)), working)
    assert (code, err) == (2, ledger.tag_message("lesson-t-u", ["nope"]) + "\n")
    empty = "- lesson[error][lesson-t-y]{tags:nope}{newtag:nope|a tag| } trigger: t root_cause: r"
    code, err = run(payload(last_assistant_message=ledger_block(empty)), working)
    assert (code, err) == (2, ledger.tag_message("lesson-t-y", ["nope"]) + "\n")


def test_unlisted_tag_a_block_on_a_line_refused_for_its_prefix_declares_nothing(working):
    tags_md(working, "hooks")
    bare = (
        "- lesson[knowledge][harness-x]{tags:nope}{newtag:nope|a tag|тег} trigger: a root_cause: b"
    )
    code, err = run(payload(last_assistant_message=ledger_block(bare, TAGGED)), working)
    assert code == 2 and ledger.tag_message("lesson-t-u", ["nope"]) in err


def test_unlisted_tag_in_an_earlier_text_waits_without_a_word_then_lands(working):
    tags_md(working, "hooks")
    transcript = write_transcript(working, transcript_line(ledger_block(TAGGED)))
    stdin = payload(last_assistant_message="Nothing.", transcript_path=transcript)
    assert run(stdin, working) == (0, "")
    assert not ledger_file(working).exists()
    declaring_case(working)
    seed_ledger(working, DECLARE)
    stdin = payload(last_assistant_message="Nothing.", transcript_path=transcript)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(TAGGED)


def test_unlisted_tag_declared_by_a_case_ratified_in_the_same_stop_passes(working):
    tags_md(working, "hooks")
    declaring_case(working)
    reply = ledger_block(DECLARE, TAGGED)
    code, err = run(
        payload(last_assistant_message=reply, transcript_path=asked(working, "lesson-t-u")), working
    )
    assert (code, err) == (0, "")
    assert ledger_text(working).splitlines() == [timed(DECLARE), timed(TAGGED)]


def test_unlisted_tag_declared_by_a_case_with_no_decision_line_is_refused(working):
    tags_md(working, "hooks")
    declaring_case(working)
    code, err = run(payload(last_assistant_message=ledger_block(TAGGED)), working)
    assert (code, err) == (2, ledger.tag_message("lesson-t-u", ["nope"]) + "\n")


def test_unlisted_tag_a_line_refused_for_its_prefix_gets_that_refusal_alone(working):
    tags_md(working, "hooks")
    bare = "- lesson[knowledge][harness-x-renders-y]{tags:nope} trigger: a root_cause: b"
    code, err = run(payload(last_assistant_message=ledger_block(bare)), working)
    assert code == 2 and "starts with lesson-" in err and "tags.md" not in err


def test_unlisted_tag_no_tags_md_refuses_no_lesson(working):
    assert run(payload(last_assistant_message=ledger_block(TAGGED)), working) == (0, "")
    assert ledger_text(working) == f"{timed(TAGGED)}\n"


def test_unlisted_tag_estimate_and_decision_lines_are_not_judged(working):
    tags_md(working, "hooks")
    code, err = run(payload(last_assistant_message=ledger_block(ESTIMATE, PREVIEW)), working)
    assert (code, err) == (0, "")


# --- a lesson refused for its tag is not held for its mark (case 703.3) ----------------------
# `estimate-ledger-write-asks-for-the-mark-of-a-lesson`


def test_unlisted_tag_after_a_decision_line_is_not_held_and_does_not_land_again(working):
    tags_md(working, "hooks")
    seed_ledger(working, DECISION)
    code, err = run(payload(last_assistant_message=ledger_block(TAGGED)), working)
    assert (code, err) == (2, ledger.tag_message("lesson-t-u", ["nope"]) + "\n")
    assert ledger.held_message("lesson-t-u") not in err
    again = payload(
        last_assistant_message=ledger_block(TAGGED), transcript_path=asked(working, "lesson-t-u")
    )
    assert run(again, working)[0] == 2
    assert timed(TAGGED) not in ledger_text(working)


def test_unlisted_tag_a_listed_unmarked_lesson_is_held_as_before(working):
    tags_md(working, "hooks")
    seed_ledger(working, DECISION)
    code, err = run(payload(last_assistant_message=ledger_block(LISTED)), working)
    assert (code, err) == (2, ledger.held_message("lesson-t-v") + "\n")


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

    lines = [LESSON, SUB_1, MARK_PARENT, MARK_SUB, MARK_9, CASE_9]
    code, _ = run(payload(last_assistant_message=ledger_block(*lines)), working)
    assert code == 2
    written = {ledger.BRACKET.findall(line)[1] for line in ledger_text(working).splitlines()}
    hook_refused = {"lesson-a-b", "lesson-a-c", "lesson-a-d", "lesson-x"} - written

    unit = working / "vault" / "raw" / "2026-09-10"
    unit.mkdir(parents=True)
    (unit / "ledger.md").write_text(
        "".join(f"{timed(line)}\n" for line in lines), encoding="utf-8", newline="\n"
    )
    (working / "vault" / "wiki").mkdir(parents=True, exist_ok=True)
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
    "Write it again in the form of the table in ratification.md.\n"
)


def test_a_broken_line_in_the_finished_reply_is_refused_aloud(working):
    reply = ledger_block(DECISION, BROKEN, LESSON)
    code, err = run(payload(last_assistant_message=reply, transcript_path=asked(working)), working)
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
    path = write_transcript(
        working, person(), meta_refusal("uv run --project .guppi guppi onward --plan", "go")
    )
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
    path = stretch(
        project_dir, meta_refusal("uv run --project .guppi guppi onward --plan", "go on")
    )
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


# --- one judgment of the person's message, the turn and the stretch (case 592) -----------


def kind_records():
    """One transcript with each kind of `user` record, in the shapes Claude Code writes."""

    def call(size):
        usage = {"input_tokens": size, "output_tokens": 0}
        message = {"role": "assistant", "content": [{"type": "text", "text": "x"}]}
        return {"type": "assistant", "message": {**message, "usage": usage}}

    def user(content, **fields):
        return {"type": "user", "message": {"role": "user", "content": content}, **fields}

    refusal = "Stop hook feedback:\n[" + ledger.COMMAND + "]: "
    tool = [{"type": "tool_result", "tool_use_id": "t", "content": "ok"}]
    return [
        user("go on", origin={"kind": "human"}),  # 0 the person's message
        call(10_000),  # 1 a call
        user(refusal + "first", isMeta=True),  # 2 a refusal
        user("<result>done</result>", origin={"kind": "task-notification"}),  # 3 an answer
        call(12_000),  # 4 a call
        user("<command-name>/clear</command-name>"),  # 5 a local command, no origin
        user("from a peer", origin={"kind": "peer"}),  # 6 another Claude session
        user(tool),  # 7 a tool result
        user(refusal + "second", isMeta=True),  # 8 a refusal
        call(15_000),  # 9 a call
    ]


def test_kind_of_a_user_record_sets_the_turn_and_the_stretch(tmp_path):
    from guppi import casecheck, context

    records = kind_records()
    kinds = [ledger.user_kind(r) for r in records]
    assert kinds[0] == ledger.PERSON and kinds[3] == ledger.ANSWER
    assert [k for i, k in enumerate(kinds) if i not in (0, 3)] == [None] * 8
    # the turn starts after the returned answer; the stretch after the person's message
    assert casecheck.turn_of_reply(records) == records[4:]
    path = tmp_path / "transcript.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in records) + "\n", encoding="utf-8")
    payload = {"transcript_path": str(path)}
    assert ledger.own_refusals(payload, ledger.COMMAND) == ["first", "second"]
    assert context.sizes(records) == (15_000, 5_000)  # from the call before the answer
    # a transcript with neither kind is read whole as the turn and as the stretch
    neither = [r for i, r in enumerate(records) if i not in (0, 3)]
    assert casecheck.turn_of_reply(neither) == neither
    path.write_text("\n".join(json.dumps(r) for r in neither) + "\n", encoding="utf-8")
    assert ledger.own_refusals(payload, ledger.COMMAND) == ["first", "second"]
    assert context.sizes(neither) == (15_000, 15_000)


def test_refusals_of_two_hooks_after_two_replies_carry_the_reply_they_follow(tmp_path):
    def reply(text):
        return {"type": "assistant", "message": {"content": [{"type": "text", "text": text}]}}

    def refused(command, text):
        content = f"Stop hook feedback:\n[{command}]: {text}"
        return {"type": "user", "isMeta": True, "message": {"content": content}}

    onward = "uv run --project .guppi guppi onward"
    records = [
        reply("before the person"),
        refused(ledger.COMMAND, "earlier stretch"),
        {"type": "user", "origin": {"kind": "human"}, "message": {"content": "go on"}},
        reply("first"),  # 0 of the stretch
        refused(ledger.COMMAND, "a lesson"),
        refused(onward, "to the handoff"),
        reply("second"),  # 3 of the stretch
        refused(ledger.COMMAND, "a reading"),
        refused("uv run --project .guppi guppi onward --plan", "not this hook"),
    ]
    path = tmp_path / "transcript.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in records) + "\n", encoding="utf-8")
    payload = {"transcript_path": str(path)}
    found = ledger.refusals(payload, onward, ledger.COMMAND)
    assert found == {
        onward: [(0, "to the handoff")],
        ledger.COMMAND: [(0, "a lesson"), (3, "a reading")],
    }
    assert ledger.own_refusals(payload, ledger.COMMAND) == ["a lesson", "a reading"]
    assert ledger.refusals({"transcript_path": str(tmp_path / "none.jsonl")}, onward) is None


# --- the command with `--project .guppi` and without it (case 819.1) -------------------------


def stop_records(*records):
    """A stretch: the person's message, then `records`, each a reply's text or a refusal
    `(command, text)`."""
    out = [{"type": "user", "origin": {"kind": "human"}, "message": {"content": "go on"}}]
    for record in records:
        if isinstance(record, str):
            out.append(
                {"type": "assistant", "message": {"content": [{"type": "text", "text": record}]}}
            )
        else:
            content = f"Stop hook feedback:\n[{record[0]}]: {record[1]}"
            out.append({"type": "user", "isMeta": True, "message": {"content": content}})
    return out


def stop_payload(tmp_path, *records):
    path = tmp_path / "transcript.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in stop_records(*records)) + "\n", "utf-8")
    return {"transcript_path": str(path)}


@pytest.mark.parametrize("name", ["ledger", "onward", "ratified", "casecheck"])
def test_each_hook_finds_its_refusals_under_the_command_with_and_without_the_project(
    tmp_path, name
):
    command = importlib.import_module(f"guppi.{name}").COMMAND
    old = f"uv run guppi {name}"
    assert command == f"uv run --project .guppi guppi {name}"
    assert ledger.command_forms(command) == (command, old)
    payload = stop_payload(tmp_path, "first", (old, "before"), "second", (command, "after"))
    assert ledger.refusals(payload, command) == {command: [(0, "before"), (2, "after")]}
    assert ledger.own_refusals(payload, command) == ["before", "after"]
    for form in (old, command):
        payload = stop_payload(tmp_path, "first", (form, "sent back"), "second")
        assert ledger.sent_back_last(payload, command) is True


def test_a_plan_refusal_of_onward_is_its_own_in_either_form_and_not_that_of_onward(tmp_path):
    from guppi import onward

    old = "uv run guppi onward --plan"
    assert ledger.command_forms(onward.PLAN_COMMAND) == (onward.PLAN_COMMAND, old)
    payload = stop_payload(tmp_path, "first", (old, "go on"))
    assert ledger.own_refusals(payload, onward.PLAN_COMMAND) == ["go on"]
    assert ledger.own_refusals(payload, onward.COMMAND) == []


def test_a_command_without_the_project_has_one_form():
    assert ledger.command_forms("uv run guppi x") == ("uv run guppi x",)


# --- no sprint open (case 628.3) ---------------------------------------------------------

DEFER = "- decision[case 11][defer][rule-x]{ref:rule-x}"
OPENING = "- decision[case 12][create][entity-sprint-next]{ref:entity-sprint}{tags:sprint}"


def without_sprint(tmp_path):
    write_event_log(tmp_path, EVENT_LOG_WITH_HI)
    (tmp_path / "vault" / "wiki" / "entities" / "entity-sprint-migration.md").unlink()
    return tmp_path


def test_sprint_missing_refuses_a_decision_line_and_passes_a_defer_a_reading_a_lesson(tmp_path):
    without_sprint(tmp_path)
    reply = ledger_block(DECISION, DEFER, ESTIMATE, LESSON)
    path = asked(tmp_path)
    code, err = run(payload(last_assistant_message=reply, transcript_path=path), tmp_path)
    assert code == 2
    assert err.count("no sprint is open") == 1 and "rule-ledger-write" in err
    assert ledger_text(tmp_path) == f"{timed(DEFER)}\n{timed(ESTIMATE)}\n{timed(LESSON)}\n"


def test_sprint_create_in_the_same_reply_lets_the_lines_through(tmp_path):
    without_sprint(tmp_path)
    code, err = run(payload(last_assistant_message=ledger_block(OPENING, DECISION)), tmp_path)
    assert (code, err) == (0, "")
    assert ledger_text(tmp_path) == f"{timed(OPENING)}\n{timed(DECISION)}\n"


def test_sprint_create_in_the_ledger_lets_a_later_line_through(tmp_path):
    without_sprint(tmp_path)
    ledger_file(tmp_path).parent.mkdir(parents=True, exist_ok=True)
    ledger_file(tmp_path).write_text(timed(OPENING) + "\n", encoding="utf-8")
    code, err = run(payload(last_assistant_message=ledger_block(DECISION)), tmp_path)
    assert (code, err) == (0, "")
    assert ledger_text(tmp_path).endswith(f"{timed(DECISION)}\n")


# --- a sprint id is never taken twice (case 788.1) -----------------------------------------
# `estimate-skill-sprint-open-refuses-a-taken-sprint-id`

TAKEN = "the sprint id next is taken"


def test_taken_sprint_a_live_id_is_refused(tmp_path):
    without_sprint(tmp_path)
    sprint_page(tmp_path, "entity-sprint-next")
    code, err = run(payload(last_assistant_message=ledger_block(OPENING)), tmp_path)
    assert code == 2 and err.count(TAKEN) == 1
    assert not ledger_file(tmp_path).exists() or ledger_text(tmp_path) == ""


def test_taken_sprint_an_archived_id_is_refused_and_opens_no_sprint(tmp_path):
    without_sprint(tmp_path)
    archived = tmp_path / "vault" / "archive" / "next" / "2026-09-01" / "0900" / "entities"
    archived.mkdir(parents=True)
    (archived / "entity-sprint-next.md").write_text("---\ntype: entity\n---\n", encoding="utf-8")
    code, err = run(payload(last_assistant_message=ledger_block(OPENING, DECISION)), tmp_path)
    assert code == 2
    assert err.count(TAKEN) == 1 and err.count("no sprint is open") == 1
    assert not ledger_file(tmp_path).exists() or ledger_text(tmp_path) == ""


def test_taken_sprint_an_id_in_a_raw_folder_or_another_category_is_free(tmp_path):
    without_sprint(tmp_path)
    for folder in ("next/2026-09-01/0900/raw/entities", "next/2026-09-01/0900/rules"):
        stray = tmp_path / "vault" / "archive" / folder / "entity-sprint-next.md"
        stray.parent.mkdir(parents=True)
        stray.write_text("---\ntype: entity\n---\n", encoding="utf-8")
    code, err = run(payload(last_assistant_message=ledger_block(OPENING, DECISION)), tmp_path)
    assert (code, err) == (0, "")
    assert ledger_text(tmp_path) == f"{timed(OPENING)}\n{timed(DECISION)}\n"


def test_taken_sprint_a_free_id_is_written(tmp_path):
    without_sprint(tmp_path)
    code, err = run(payload(last_assistant_message=ledger_block(OPENING)), tmp_path)
    assert (code, err) == (0, "")
    assert ledger_text(tmp_path) == f"{timed(OPENING)}\n"


def test_sprint_live_page_accepts_a_decision_line(working):
    code, err = run(payload(last_assistant_message=ledger_block(DECISION)), working)
    assert (code, err) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n"


# --- a lesson after a Case is asked for its mark (case 682.1) -------------------------------
# `estimate-ledger-write-asks-for-the-mark-of-a-lesson`

SUB_2 = "- decision[case 8.2][update][rule-y]{ref:rule-y}"
LESSON_MARKED = "- lesson[error][lesson-x]{addressed_by:case 10} trigger: a root_cause: b"


def held_refusal(slug="lesson-x"):
    return ledger.held_message(slug) + "\n"


def asking(project_dir, reply):
    """A Stop in a stretch with no refusal of the hook yet."""
    return payload(last_assistant_message=reply, transcript_path=stretch(project_dir))


def test_an_unmarked_lesson_after_a_decision_line_is_held_once_and_asked(working):
    code, err = run(asking(working, ledger_block(DECISION, LESSON, ESTIMATE)), working)
    assert (code, err) == (2, held_refusal())
    assert err == (
        "ledger: lesson[lesson-x] held — did a Case of this session fix its cause? Then add "
        "{addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; "
        "otherwise repeat it unchanged.\n"
    )
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(ESTIMATE)]


def test_the_question_names_no_case_with_several_cases_before_the_lesson(working):
    """No Case is named when the lesson follows lines of several Cases (case 694.1)."""
    seed_ledger(working, SUB_2)
    other = SUB_1.replace("rule-x", "rule-w")
    store_cases(working, SUB_1, other)
    code, err = run(asking(working, ledger_block(SUB_1, CASE_9, other, LESSON, DECISION)), working)
    assert (code, err) == (2, held_refusal())
    assert "case 8" not in err and "case 9" not in err


def test_the_lesson_written_again_unchanged_lands_as_it_stands(working):
    seed_ledger(working, DECISION)
    stdin = payload(last_assistant_message=ledger_block(LESSON), transcript_path=asked(working))
    assert run(stdin, working) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(LESSON)


def test_the_lesson_written_again_with_its_mark_drops_the_unmarked_line(working):
    seed_ledger(working, DECISION)
    path = write_transcript(
        working,
        person(),
        transcript_line(ledger_block(LESSON)),
        own_refusal(held_refusal().rstrip("\n")),
    )
    reply = ledger_block(LESSON_MARKED)
    assert run(payload(last_assistant_message=reply, transcript_path=path), working) == (0, "")
    assert ledger_text(working).splitlines()[1:] == [timed(LESSON_MARKED)]
    stdin = payload(last_assistant_message="Nothing.", transcript_path=path)
    assert run(stdin, working) == (0, "")
    assert timed(LESSON) not in ledger_text(working).splitlines()


def test_an_unmarked_line_beside_a_marked_one_in_the_same_stop_is_dropped(working):
    code, err = run(asking(working, ledger_block(DECISION, LESSON, LESSON_MARKED)), working)
    assert (code, err) == (0, "")
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(LESSON_MARKED)]


def test_a_lesson_from_an_earlier_text_lands_without_a_word(working):
    path = write_transcript(working, person(), transcript_line(ledger_block(DECISION, LESSON)))
    stdin = payload(last_assistant_message="Done.", transcript_path=path)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(LESSON)]


def test_a_lesson_before_every_decision_line_is_not_asked(working):
    """It is not held; the reminder after the write tells it (case 685.1)."""
    code, err = run(asking(working, ledger_block(LESSON, DECISION)), working)
    assert (code, err) == (2, ledger.reminder_message("lesson-x") + "\n")
    assert ledger_text(working).splitlines() == [timed(LESSON), timed(DECISION)]


def test_a_held_line_keeps_back_no_other_line(working):
    code, _ = run(asking(working, ledger_block(DECISION, LESSON, ESTIMATE)), working)
    assert code == 2
    assert timed(ESTIMATE) in ledger_text(working).splitlines()


def test_a_lesson_refused_for_its_prefix_is_not_asked(working):
    code, err = run(asking(working, ledger_block(DECISION, BARE_LESSON)), working)
    assert (code, err) == (2, LESSON_REFUSAL)


def test_a_lesson_the_grammar_cannot_read_is_not_asked(working):
    unread = "- lesson[oops][lesson-y] trigger: a root_cause: b"
    code, err = run(asking(working, ledger_block(DECISION, unread)), working)
    assert (code, err) == (2, BROKEN_REFUSAL.format(unread[2:]))


def test_a_session_with_no_hi_gets_no_question(tmp_path):
    code, err = run(asking(tmp_path, ledger_block(DECISION, LESSON)), tmp_path)
    assert code == 2 and "no /hi recorded" in err and "held" not in err


def test_with_the_flag_and_no_readable_transcript_the_lesson_lands(working):
    stdin = payload(last_assistant_message=ledger_block(DECISION, LESSON), stop_hook_active=True)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(LESSON)]


def test_with_the_flag_and_a_readable_transcript_the_lesson_is_still_asked(working):
    code, err = run(flagged(working, ledger_block(DECISION, LESSON)), working)
    assert (code, err) == (2, held_refusal())
    assert ledger_text(working) == f"{timed(DECISION)}\n"


# --- a lesson before a Case is reminded of its mark (case 685.1) ---------------------------
# `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`

MARKED_AGAIN = DECISION + "{addresses:lesson-x}"


def reminder(slug):
    return ledger.reminder_message(slug) + "\n"


def test_reminder_comes_after_the_write(working):
    seed_ledger(working, LESSON)
    code, err = run(asking(working, ledger_block(DECISION)), working)
    assert (code, err) == (2, reminder("lesson-x"))
    assert err == (
        "ledger: lesson[lesson-x] has no mark — did a Case of this session fix its cause? Then write the "
        "decision line of the Case or sub-case that fixed it again with "
        "{addresses:lesson-x} added, alone in a LEDGER block; otherwise go on without it.\n"
    )
    assert ledger_text(working).splitlines() == [f"- 15:01:50 {LESSON[2:]}", timed(DECISION)]


def test_reminder_names_no_case_with_fresh_lines_of_several_cases(working):
    """The reminder names no Case with fresh lines of several Cases (case 694.2)."""
    seed_ledger(working, SUB_2, LESSON)
    code, err = run(asking(working, ledger_block(CASE_9, SUB_1, CASE_9)), working)
    assert (code, err) == (2, reminder("lesson-x"))


def test_reminder_is_told_once_a_stretch(working):
    """With no Case named, a ratification of other Cases in the same stretch
    gives the same line, already told (case 694.2)."""
    seed_ledger(working, LESSON)
    path = stretch(working, own_refusal(reminder("lesson-x").rstrip("\n")))
    assert run(
        payload(last_assistant_message=ledger_block(DECISION), transcript_path=path), working
    ) == (0, "")
    stdin = payload(last_assistant_message=ledger_block(CASE_9), transcript_path=path)
    assert run(stdin, working) == (0, "")


def test_reminder_ends_once_a_decision_line_carries_the_mark(working):
    from guppi import materialize

    seed_ledger(working, LESSON, DECISION)
    code, err = run(asking(working, ledger_block(MARKED_AGAIN)), working)
    assert (code, err) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(MARKED_AGAIN)
    assert run(asking(working, ledger_block(CASE_9)), working) == (0, "")
    lines = ledger_text(working).splitlines()
    assert materialize.unlinked_lessons(lines) == []
    record = materialize.parse_line(lines[0])
    assert record["slug"] == "lesson-x" and not record["addressed_by"]


def test_reminder_not_for_a_defer_line(working):
    seed_ledger(working, LESSON)
    defer = "- decision[case 5][defer][estimate-x-holds]"
    assert run(asking(working, ledger_block(defer)), working) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(defer)


def test_reminder_not_for_a_lesson_after_every_decision_line(working):
    code, err = run(
        payload(
            last_assistant_message=ledger_block(DECISION, LESSON), transcript_path=asked(working)
        ),
        working,
    )
    assert (code, err) == (0, "")
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(LESSON)]


def test_reminder_not_for_a_lesson_already_marked(working):
    seed_ledger(working, DECISION, LESSON_MARKED)
    assert run(asking(working, ledger_block(CASE_9)), working) == (0, "")


def test_reminder_not_for_a_fresh_lesson_the_same_stop_holds_back(working):
    code, err = run(asking(working, ledger_block(SUB_1, LESSON, CASE_9)), working)
    assert (code, err) == (2, held_refusal())
    assert ledger_text(working).splitlines() == [timed(SUB_1), timed(CASE_9)]


def test_reminder_not_for_a_decision_line_of_an_earlier_text(working):
    seed_ledger(working, LESSON)
    path = write_transcript(working, person(), transcript_line(ledger_block(DECISION)))
    stdin = payload(last_assistant_message="Nothing.", transcript_path=path)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(DECISION)


def test_reminder_not_without_hi(tmp_path):
    write_event_log(tmp_path, "- 15:01:00 44c1aae1 session-start startup\n")
    code, err = run(asking(tmp_path, ledger_block(LESSON, DECISION)), tmp_path)
    assert code == 2 and "no /hi recorded" in err and "has no mark" not in err


def test_reminder_with_the_flag_and_no_readable_transcript_says_nothing(working):
    seed_ledger(working, LESSON)
    stdin = payload(last_assistant_message=ledger_block(DECISION), stop_hook_active=True)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working).splitlines()[-1] == timed(DECISION)


def test_unlinked_lessons_reads_the_marks_of_both_kinds():
    from guppi.materialize import unlinked_lessons

    lines = [
        LESSON,
        DECISION,
        LESSON.replace("lesson-x", "lesson-y"),
        MARKED_AGAIN,
        LESSON_MARKED.replace("lesson-x", "lesson-z"),
    ]
    assert unlinked_lessons(lines) == [2]
    assert unlinked_lessons([LESSON, LESSON_MARKED]) == []


# --- a decision line is a copy of the stored Case (case 688.7) -----------------------------
# `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`

WRONG = DECISION.replace("{ref:rule-session-start}", "{ref:rule-ledger-write}")


def held_copy(case):
    return ledger.off_store_message(case) + "\n"


def test_copy_equal_to_the_store_lands(working):
    assert run(asking(working, ledger_block(DECISION, SUB_1)), working) == (0, "")
    assert ledger_text(working).splitlines() == [timed(DECISION), timed(SUB_1)]


def test_copy_that_differs_is_held_and_the_rest_lands(working):
    code, err = run(asking(working, ledger_block(WRONG, SUB_1, ESTIMATE)), working)
    assert (code, err) == (2, held_copy("10"))
    assert err == (
        "ledger: decision[case 10] not written — it is not a line of the ratification "
        "case-guppi stored for case 10: copy it again as the summary of case-guppi holds it, "
        "alone in a LEDGER block, or send the Case back to its case-guppi when the stored line "
        "is wrong.\n"
    )
    assert ledger_text(working).splitlines() == [timed(SUB_1), timed(ESTIMATE)]


def test_copy_of_a_case_the_store_holds_no_text_for_is_held(working):
    line = "- decision[case 77][update][rule-q]{ref:rule-q}"
    assert run(asking(working, ledger_block(line)), working) == (2, held_copy("77"))
    assert not ledger_file(working).exists()


def test_copy_of_a_session_with_no_plan_file_is_held(tmp_path):
    path = tmp_path / "vault" / "raw" / TODAY.isoformat() / "event_log.md"
    path.parent.mkdir(parents=True)
    path.write_text(EVENT_LOG_WITH_HI, encoding="utf-8")
    sprint_page(tmp_path)
    code, err = run(asking(tmp_path, ledger_block(DECISION, ESTIMATE)), tmp_path)
    assert (code, err) == (2, held_copy("10"))
    assert ledger_text(tmp_path) == f"{timed(ESTIMATE)}\n"


def test_copy_written_again_equal_lands(working):
    path = write_transcript(working, person(), transcript_line(ledger_block(WRONG)))
    stdin = payload(last_assistant_message=ledger_block(DECISION), transcript_path=path)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working) == f"{timed(DECISION)}\n"


def test_copy_with_the_addresses_mark_added_lands(working):
    assert run(asking(working, ledger_block(MARKED_AGAIN)), working) == (0, "")
    assert ledger_text(working) == f"{timed(MARKED_AGAIN)}\n"


def test_copy_rule_does_not_judge_a_defer_line(working):
    defer = "- decision[case 5][defer][estimate-x-holds]"
    assert run(asking(working, ledger_block(defer)), working) == (0, "")
    assert ledger_text(working) == f"{timed(defer)}\n"


def test_copy_held_in_an_earlier_text_stays_out_without_a_word(working):
    path = write_transcript(working, person(), transcript_line(ledger_block(WRONG)))
    stdin = payload(last_assistant_message="Nothing.", transcript_path=path)
    assert run(stdin, working) == (0, "")
    assert not ledger_file(working).exists()


def test_copy_reason_is_told_once_a_stretch(working):
    path = stretch(working, own_refusal(held_copy("10").rstrip("\n")))
    stdin = payload(last_assistant_message=ledger_block(WRONG), transcript_path=path)
    assert run(stdin, working) == (0, "")
    assert not ledger_file(working).exists()


def test_copy_with_the_flag_and_no_readable_transcript_stays_out_silently(working):
    stdin = payload(last_assistant_message=ledger_block(WRONG, ESTIMATE), stop_hook_active=True)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working) == f"{timed(ESTIMATE)}\n"


def test_copy_with_the_flag_and_a_readable_transcript_is_still_held(working):
    assert run(flagged(working, ledger_block(WRONG)), working) == (2, held_copy("10"))


# --- a line of a LEDGER block that is no record is refused aloud (case 695.1) ---------------
# `estimate-ledger-write-refuses-a-line-that-is-no-record`

NEAR_MISS = "- estimate-hi-no-read-calls[passed] all five"
NOTE = "A note of my own."


def stray(line):
    return ledger.stray_message(line) + "\n"


def test_stray_a_near_miss_and_a_note_are_refused_aloud_and_the_records_land(working):
    reply = ledger_block(ESTIMATE, NEAR_MISS, NOTE)
    code, err = run(asking(working, reply), working)
    assert (code, err) == (2, stray(NEAR_MISS) + stray(NOTE))
    assert err.startswith(
        "ledger: line not written — a LEDGER block holds only lines that open with - decision[, "
        "- estimate[ or - lesson[: - estimate-hi-no-read-calls[passed] all five. Write it again "
        "with that opening, or leave it out."
    )
    assert ledger_text(working).splitlines() == [timed(ESTIMATE)]


def test_stray_a_block_with_no_record_line_is_refused_too(working):
    code, err = run(asking(working, ledger_block(NEAR_MISS)), working)
    assert (code, err) == (2, stray(NEAR_MISS))
    assert not ledger_file(working).exists()


def test_stray_a_line_of_an_earlier_text_is_silent(working):
    path = write_transcript(working, person(), transcript_line(ledger_block(ESTIMATE, NEAR_MISS)))
    stdin = payload(last_assistant_message="Done.", transcript_path=path)
    assert run(stdin, working) == (0, "")
    assert ledger_text(working).splitlines() == [timed(ESTIMATE)]


def test_stray_a_blank_line_and_an_untagged_block_pass(working):
    reply = ledger_block(ESTIMATE, "", "   ") + "\n```\n" + NOTE + "\n```\n"
    assert run(asking(working, reply), working) == (0, "")
    assert ledger_text(working).splitlines() == [timed(ESTIMATE)]


def test_stray_a_repeat_already_told_is_silent(working):
    path = stretch(working, own_refusal(stray(NOTE).rstrip("\n")))
    stdin = payload(last_assistant_message=ledger_block(NOTE), transcript_path=path)
    assert run(stdin, working) == (0, "")


def test_stray_without_a_hi_no_line_is_judged(tmp_path):
    assert run(asking(tmp_path, ledger_block(NOTE)), tmp_path) == (0, "")


def test_stray_and_record_lines_share_one_reading_of_the_block():
    text = ledger_block(ESTIMATE, NEAR_MISS, "", NOTE) + "```\n" + NOTE + "\n```\n"
    assert ledger.ledger_lines(text) == [ESTIMATE]
    assert ledger.stray_lines(text) == [NEAR_MISS, NOTE]
