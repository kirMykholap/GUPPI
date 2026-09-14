"""`guppi event`: one line per hook event into `vault/raw/<date>/event_log.md`.

Every test feeds the payload through a stream, the shape a hook is really handed
(the old vault's lesson: a process is measured with the stdin it will have).
"""

import io
import json
import re
from datetime import UTC, date, datetime

import pytest

from guppi import event

TODAY = date(2026, 9, 9)
NOW = datetime(2026, 9, 9, 15, 2, 11, tzinfo=UTC)
LINE = re.compile(r"^- \d\d:\d\d:\d\d [0-9a-f-]{8} \S+.*$")


def payload(**fields):
    return io.StringIO(json.dumps(fields))


def run(argv, stdin, project_dir):
    err = io.StringIO()
    code = event.run(argv, stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def run_out(argv, stdin, project_dir, now=NOW):
    out, err = io.StringIO(), io.StringIO()
    code = event.run(argv, stdin=stdin, stdout=out, stderr=err, project_dir=project_dir, now=now)
    return code, out.getvalue(), err.getvalue()


def log_lines(project_dir, day=TODAY):
    path = project_dir / "vault" / "raw" / day.isoformat() / "event_log.md"
    return path.read_text(encoding="utf-8").splitlines()


def test_session_start_line_carries_source_and_session(tmp_path):
    stdin = payload(session_id="abc12345-6789", hook_event_name="SessionStart", source="startup")
    code, err = run(["session-start"], stdin, tmp_path)
    assert (code, err) == (0, "")
    assert log_lines(tmp_path) == ["- 15:02:11 abc12345 session-start startup"]


def test_tool_line_names_the_tool_and_the_command(tmp_path):
    stdin = payload(session_id="abc12345", tool_name="Bash", tool_input={"command": "git status"})
    run(["tool"], stdin, tmp_path)
    assert log_lines(tmp_path) == ["- 15:02:11 abc12345 tool Bash: git status"]


def test_bash_detail_is_one_line_and_at_most_eighty_characters(tmp_path):
    command = "echo one\necho " + "x" * 200
    stdin = payload(session_id="abc12345", tool_name="Bash", tool_input={"command": command})
    run(["tool"], stdin, tmp_path)
    (line,) = log_lines(tmp_path)
    detail = line.split("tool Bash: ", 1)[1]
    assert "\n" not in detail
    assert len(detail) == 80
    assert detail.startswith("echo one echo ")


@pytest.mark.parametrize(
    ("tool_input", "expected"),
    [
        ({"subagent_type": "Explore", "description": "find x"}, "tool Agent: Explore"),
        ({"file_path": "C:/p/a.md"}, "tool Agent: C:/p/a.md"),
        ({}, "tool Agent"),
    ],
)
def test_other_tools_take_the_most_telling_field(tmp_path, tool_input, expected):
    stdin = payload(session_id="abc12345", tool_name="Agent", tool_input=tool_input)
    run(["tool"], stdin, tmp_path)
    assert log_lines(tmp_path) == [f"- 15:02:11 abc12345 {expected}"]


def test_hi_without_a_payload_has_no_session(tmp_path):
    code, err = run(["hi"], io.StringIO(""), tmp_path)
    assert (code, err) == (0, "")
    assert log_lines(tmp_path) == ["- 15:02:11 -------- hi"]


def test_session_option_overrides_the_payload(tmp_path):
    stdin = payload(session_id="abc12345")
    run(["hi", "--session", "fedcba98-0000"], stdin, tmp_path)
    assert log_lines(tmp_path) == ["- 15:02:11 fedcba98 hi"]


def test_empty_session_option_means_unknown(tmp_path):
    run(["hi", "--session", ""], io.StringIO(""), tmp_path)
    assert log_lines(tmp_path) == ["- 15:02:11 -------- hi"]


def test_free_detail_words_follow_the_event(tmp_path):
    run(["note", "probe", "registered"], io.StringIO(""), tmp_path)
    assert log_lines(tmp_path) == ["- 15:02:11 -------- note probe registered"]


def test_lines_append_in_order(tmp_path):
    run(["session-start"], payload(session_id="abc12345", source="startup"), tmp_path)
    run(["hi"], io.StringIO(""), tmp_path)
    run(["tool"], payload(session_id="abc12345", tool_name="Read"), tmp_path)
    assert [line.split(" ", 3)[3] for line in log_lines(tmp_path)] == [
        "session-start startup",
        "hi",
        "tool Read",
    ]
    assert all(LINE.match(line) for line in log_lines(tmp_path))


def test_utf8_payload_survives_a_locale_encoded_stdin(tmp_path):
    # The shape of a hook's stdin on Windows: a cp1252 text wrapper with surrogateescape
    # over UTF-8 bytes (measured 2026-09-09). The detail must come out as the UTF-8 it was.
    raw = json.dumps(
        {"session_id": "abc12345", "tool_name": "Bash", "tool_input": {"command": "echo — тест"}},
        ensure_ascii=False,
    ).encode("utf-8")
    stdin = io.TextIOWrapper(io.BytesIO(raw), encoding="cp1252", errors="surrogateescape")
    code, err = run(["tool"], stdin, tmp_path)
    assert (code, err) == (0, "")
    assert log_lines(tmp_path) == ["- 15:02:11 abc12345 tool Bash: echo — тест"]


def test_non_json_stdin_is_treated_as_no_payload(tmp_path):
    code, err = run(["tool"], io.StringIO("not json"), tmp_path)
    assert (code, err) == (0, "")
    assert log_lines(tmp_path) == ["- 15:02:11 -------- tool"]


def test_a_write_failure_never_fails_the_hook(tmp_path):
    blocker = tmp_path / "vault"
    blocker.write_text("a file where the folder should be", encoding="utf-8")
    code, err = run(["hi"], io.StringIO(""), tmp_path)
    assert code == 0
    assert "event_log" in err


def test_cli_dispatches_to_event(tmp_path, monkeypatch, capsys, pinned_clock):
    from guppi import cli

    today = pinned_clock.date()  # the CLI reads the clock, pinned by conftest (case 145.1)

    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", io.StringIO(""))
    assert cli.main(["event", "hi"]) == 0
    (line,) = log_lines(tmp_path, day=today)
    assert line.endswith(" -------- hi")
    assert capsys.readouterr().err == ""


# --- case 111.1: the hi line on UserPromptSubmit, stamped, once per session --------------


def prompt_payload(prompt, session="abc12345-6789"):
    return payload(session_id=session, hook_event_name="UserPromptSubmit", prompt=prompt)


def test_the_hi_prompt_writes_a_stamped_hi_line(tmp_path):
    run(["session-start"], payload(session_id="abc12345-6789", source="startup"), tmp_path)
    code, err = run(["prompt"], prompt_payload("/hi"), tmp_path)
    assert (code, err) == (0, "")
    assert log_lines(tmp_path)[-1] == "- 15:02:11 abc12345 hi"


def test_hi_with_arguments_and_surrounding_spaces_counts(tmp_path):
    run(["session-start"], payload(session_id="abc12345-6789", source="startup"), tmp_path)
    run(["prompt"], prompt_payload("  /hi again  "), tmp_path)
    assert log_lines(tmp_path)[-1] == "- 15:02:11 abc12345 hi"


def test_a_second_hi_of_the_same_session_writes_nothing(tmp_path):
    run(["session-start"], payload(session_id="abc12345-6789", source="startup"), tmp_path)
    run(["prompt"], prompt_payload("/hi"), tmp_path)
    run(
        ["tool"],
        payload(session_id="abc12345-6789", tool_name="Bash", tool_input={"command": "ls"}),
        tmp_path,
    )
    code, err = run(["prompt"], prompt_payload("/hi"), tmp_path)
    assert (code, err) == (0, "")
    assert [ln for ln in log_lines(tmp_path) if ln.endswith(" hi")] == ["- 15:02:11 abc12345 hi"]


def test_another_sessions_hi_does_not_stand_in_for_ours(tmp_path):
    run(["session-start"], payload(session_id="abc12345-6789", source="startup"), tmp_path)
    run(["session-start"], payload(session_id="deadbeef-0000", source="resume"), tmp_path)
    run(["prompt"], prompt_payload("/hi", session="deadbeef-0000"), tmp_path)
    run(["prompt"], prompt_payload("/hi"), tmp_path)
    assert [ln for ln in log_lines(tmp_path) if ln.endswith(" hi")] == [
        "- 15:02:11 deadbeef hi",
        "- 15:02:11 abc12345 hi",
    ]


@pytest.mark.parametrize("prompt", ["hello", "/history", "hi", "/retro", ""])
def test_any_other_prompt_writes_nothing(tmp_path, prompt):
    run(["session-start"], payload(session_id="abc12345-6789", source="startup"), tmp_path)
    code, err = run(["prompt"], prompt_payload(prompt), tmp_path)
    assert (code, err) == (0, "")
    assert len(log_lines(tmp_path)) == 1


def test_a_prompt_without_a_session_id_writes_nothing(tmp_path):
    code, err = run(["prompt"], payload(hook_event_name="UserPromptSubmit", prompt="/hi"), tmp_path)
    assert code == 0 and err == ""
    assert not (tmp_path / "vault" / "raw").exists()


def test_a_prompt_with_an_unreadable_payload_exits_zero(tmp_path):
    code, err = run(["prompt"], io.StringIO("not json"), tmp_path)
    assert code == 0 and err == ""
    assert not (tmp_path / "vault" / "raw").exists()


# --- the hi: line in the context (case 125) ------------------------------------------------


def test_the_hi_prompt_prints_the_line_and_the_folder_into_the_context(tmp_path):
    run(["session-start"], payload(session_id="abc12345-6789", source="startup"), tmp_path)
    code, out, err = run_out(["prompt"], prompt_payload("/hi"), tmp_path)
    assert (code, err) == (0, "")
    assert out == "hi: 15:02:11 abc12345 → raw/2026-09-09/1502/\n"
    assert log_lines(tmp_path)[-1] == "- 15:02:11 abc12345 hi"


def test_a_second_hi_prints_already_recorded_and_adds_no_line(tmp_path):
    run(["session-start"], payload(session_id="abc12345-6789", source="startup"), tmp_path)
    run(["prompt"], prompt_payload("/hi"), tmp_path)
    later = NOW.replace(hour=16, minute=30, second=0)
    code, out, err = run_out(["prompt"], prompt_payload("/hi"), tmp_path, now=later)
    assert (code, err) == (0, "")
    assert out == "hi: already recorded at 15:02:11 → raw/2026-09-09/1502/\n"
    assert [ln for ln in log_lines(tmp_path) if ln.endswith(" hi")] == ["- 15:02:11 abc12345 hi"]


def test_the_folder_across_midnight_is_the_hi_dates(tmp_path):
    run(["session-start"], payload(session_id="abc12345-6789", source="startup"), tmp_path)
    run(["prompt"], prompt_payload("/hi"), tmp_path)
    tomorrow = NOW.replace(day=10, hour=0, minute=5, second=0)
    code, out, _ = run_out(["prompt"], prompt_payload("/hi"), tmp_path, now=tomorrow)
    assert code == 0 and out == "hi: already recorded at 15:02:11 → raw/2026-09-09/1502/\n"


@pytest.mark.parametrize("prompt", ["hello", "/retro", ""])
def test_any_other_prompt_prints_nothing(tmp_path, prompt):
    run(["session-start"], payload(session_id="abc12345-6789", source="startup"), tmp_path)
    assert run_out(["prompt"], prompt_payload(prompt), tmp_path) == (0, "", "")


def test_a_hi_prompt_without_a_session_id_prints_nothing(tmp_path):
    assert run_out(
        ["prompt"], payload(hook_event_name="UserPromptSubmit", prompt="/hi"), tmp_path
    ) == (0, "", "")
