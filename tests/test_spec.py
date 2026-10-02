"""`guppi spec`: the `PostToolUse ExitPlanMode` hook that copies the approved plan into
the session's folder, `vault/raw/<hi date>/<hi HHMM>/spec.md` (case 73.2). Rule page:
`vault/wiki/rules/rule-spec-capture.md`.

Every test feeds the payload through a stream, the shape a hook is really handed.
"""

import io
import json
from datetime import UTC, date, datetime

from guppi import spec

TODAY = date(2026, 9, 9)
NOW = datetime(2026, 9, 9, 18, 40, 5, tzinfo=UTC)
SESSION = "44c1aae1-4076-4a58-a7c0-d20bc274047c"
PLAN = "# Slice 2\n\n## Context\n\nThe plan text.\n"
STAMP = "<!-- approved 18:40:05 · session 44c1aae1 -->"
EVENT_LOG_WITH_HI = "- 15:01:00 44c1aae1 session-start startup\n- 15:01:30 44c1aae1 hi\n"
EVENT_LOG_WITHOUT_HI = "- 15:01:00 44c1aae1 session-start startup\n"
HI_FOLDER = "1501"  # the `hi` at 15:01:30 names the session's folder


def payload(tool="ExitPlanMode", plan=PLAN, session=SESSION, **extra):
    fields = {"session_id": session, "hook_event_name": "PostToolUse", "tool_name": tool}
    if plan is not None:
        fields["tool_response"] = {"plan": plan}
    fields.update(extra)
    return io.StringIO(json.dumps(fields))


def raw(project_dir):
    folder = project_dir / "vault" / "raw" / TODAY.isoformat()
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def session_folder(project_dir, hhmm=HI_FOLDER):
    folder = raw(project_dir) / hhmm
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def with_event_log(project_dir, text=EVENT_LOG_WITH_HI):
    (raw(project_dir) / "event_log.md").write_text(text, encoding="utf-8", newline="\n")


def run(stdin, project_dir):
    err = io.StringIO()
    code = spec.run([], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def spec_text(project_dir, hhmm=HI_FOLDER):
    return (session_folder(project_dir, hhmm) / "spec.md").read_text(encoding="utf-8")


def spec_files(project_dir):
    return sorted(p.relative_to(project_dir).as_posix() for p in project_dir.rglob("spec.md"))


def test_plan_is_appended_after_a_separator_and_a_stamp(tmp_path):
    with_event_log(tmp_path)
    (session_folder(tmp_path) / "spec.md").write_text(
        "# Earlier\n\nold.\n", encoding="utf-8", newline="\n"
    )
    code, err = run(payload(), tmp_path)
    assert (code, err) == (0, "")
    assert spec_text(tmp_path) == f"# Earlier\n\nold.\n\n---\n\n{STAMP}\n\n{PLAN}"


def test_first_plan_creates_the_folder_and_the_file_without_a_separator(tmp_path):
    with_event_log(tmp_path)
    code, err = run(payload(), tmp_path)
    assert (code, err) == (0, "")
    assert spec_files(tmp_path) == ["vault/raw/2026-09-09/1501/spec.md"]
    assert spec_text(tmp_path) == f"{STAMP}\n\n{PLAN}"


def test_the_spec_lands_in_the_folder_of_the_hi_time(tmp_path):
    # case 73.2: a hi at 11:56 puts the Spec at raw/<date>/1156/spec.md
    with_event_log(tmp_path, "- 11:55:00 44c1aae1 session-start startup\n- 11:56:22 44c1aae1 hi\n")
    run(payload(), tmp_path)
    assert spec_files(tmp_path) == ["vault/raw/2026-09-09/1156/spec.md"]
    assert spec_text(tmp_path, "1156") == f"{STAMP}\n\n{PLAN}"


def test_a_second_approval_of_the_session_appends_in_the_same_folder(tmp_path):
    with_event_log(tmp_path)
    run(payload(), tmp_path)
    run(payload(plan="# Slice 3\n\nMore.\n"), tmp_path)
    assert spec_files(tmp_path) == ["vault/raw/2026-09-09/1501/spec.md"]
    assert spec_text(tmp_path) == f"{STAMP}\n\n{PLAN}\n---\n\n{STAMP}\n\n# Slice 3\n\nMore.\n"


def test_a_hi_of_yesterday_names_yesterdays_folder(tmp_path):
    # the window the ledger hook walks (case 55.1): the folder is the hi's date, not today's
    yesterday = tmp_path / "vault" / "raw" / "2026-09-08"
    yesterday.mkdir(parents=True)
    (yesterday / "event_log.md").write_text(EVENT_LOG_WITH_HI, encoding="utf-8", newline="\n")
    with_event_log(tmp_path, "- 00:10:00 44c1aae1 tool Bash: git status\n")
    assert run(payload(), tmp_path) == (0, "")
    assert spec_files(tmp_path) == ["vault/raw/2026-09-08/1501/spec.md"]


def test_the_same_plan_is_not_appended_twice(tmp_path):
    with_event_log(tmp_path)
    run(payload(), tmp_path)
    run(payload(), tmp_path)
    assert spec_text(tmp_path).count("# Slice 2") == 1


def test_without_hi_the_hook_refuses_and_writes_nothing(tmp_path):
    with_event_log(tmp_path, EVENT_LOG_WITHOUT_HI)
    code, err = run(payload(), tmp_path)
    assert code == 2
    assert "44c1aae1" in err and "/hi" in err
    assert spec_files(tmp_path) == []


def test_another_tool_is_ignored(tmp_path):
    with_event_log(tmp_path)
    code, err = run(payload(tool="Write"), tmp_path)
    assert (code, err) == (0, "")
    assert spec_files(tmp_path) == []


def test_a_payload_without_a_plan_is_ignored(tmp_path):
    with_event_log(tmp_path)
    code, err = run(payload(plan=None), tmp_path)
    assert (code, err) == (0, "")
    assert spec_files(tmp_path) == []


def test_a_write_failure_never_fails_the_hook(tmp_path):
    with_event_log(tmp_path)
    (session_folder(tmp_path) / "spec.md").mkdir()
    code, err = run(payload(), tmp_path)
    assert code == 0
    assert "spec.md" in err


def run_with_stdout(stdin, project_dir):
    out, err = io.StringIO(), io.StringIO()
    code = spec.run([], stdin=stdin, stdout=out, stderr=err, project_dir=project_dir, now=NOW)
    return code, out.getvalue(), err.getvalue()


# the fork after the Spec is written (case 190.5), as `additionalContext` (case 255):
# `estimate-spec-capture-offers-the-fork`


def fork_of(out):
    """The one JSON object on stdout, the shape a `PostToolUse` hook speaks to the agent in."""
    assert out.count("\n") == 1
    data = json.loads(out)
    assert data["hookSpecificOutput"]["hookEventName"] == "PostToolUse"
    return data["hookSpecificOutput"]["additionalContext"]


def test_after_the_spec_the_hook_prints_the_fork_as_additional_context(tmp_path):
    with_event_log(tmp_path)
    code, out, err = run_with_stdout(payload(), tmp_path)
    assert (code, err) == (0, "")
    line = fork_of(out)
    assert "vault/raw/2026-09-09/1501/spec.md" in line
    assert "vault/raw/2026-09-09/1501/carry.md" in line
    assert "AskUserQuestion" in line
    assert "/work" in line and "/carry" in line
    assert "start nothing until it is answered" in line
    assert "call the skill picked" in line


def test_the_fork_is_printed_again_when_the_plan_was_already_there(tmp_path):
    with_event_log(tmp_path)
    run(payload(), tmp_path)
    code, out, _ = run_with_stdout(payload(), tmp_path)
    line = fork_of(out)
    assert code == 0 and "/work" in line and "/carry" in line and "AskUserQuestion" in line


def box_plan(folder="2026-09-01/0900"):
    return f"# Session 1501 — runs the conserved Spec vault/raw/{folder}/spec.md\n"


def test_box_a_plan_naming_a_conserved_spec_leads_to_box_and_asks_nothing(tmp_path):
    # case 591.3: the person took the conserved Spec at the Frontier
    with_event_log(tmp_path)
    conserved = tmp_path / "vault" / "raw" / "2026-09-01" / "0900"
    conserved.mkdir(parents=True)
    (conserved / "carry.md").write_text("conserved\n", encoding="utf-8")
    code, out, err = run_with_stdout(payload(plan=box_plan()), tmp_path)
    assert (code, err) == (0, "")
    line = fork_of(out)
    assert "call /box with vault/raw/2026-09-01/0900/" in line
    assert "ask the person nothing" in line
    assert "AskUserQuestion" not in line and "/carry" not in line


def test_box_a_folder_without_carry_or_no_such_path_gets_the_fork(tmp_path):
    with_event_log(tmp_path)
    (tmp_path / "vault" / "raw" / "2026-09-01" / "0900").mkdir(parents=True)
    code, out, _ = run_with_stdout(payload(plan=box_plan()), tmp_path)
    assert code == 0 and "AskUserQuestion" in fork_of(out) and "/box" not in fork_of(out)
    code, out, _ = run_with_stdout(payload(plan=box_plan("2026-09-02/1000")), tmp_path)
    assert code == 0 and "AskUserQuestion" in fork_of(out)


def test_no_fork_without_a_spec(tmp_path):
    with_event_log(tmp_path, EVENT_LOG_WITHOUT_HI)
    code, out, _ = run_with_stdout(payload(), tmp_path)
    assert (code, out) == (2, "")
    with_event_log(tmp_path)
    code, out, _ = run_with_stdout(payload(tool="Write"), tmp_path)
    assert (code, out) == (0, "")


def test_cli_dispatches_to_spec(tmp_path, monkeypatch, capsys):
    from guppi import cli

    with_event_log(tmp_path, EVENT_LOG_WITHOUT_HI)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", payload())
    assert cli.main(["spec"]) == 2
    assert "/hi" in capsys.readouterr().err
