"""`guppi gate`: `/handoff` through the Skill tool is refused while the tree is dirty, and
any skill is refused while a `then` item of the session's Spec or plan file has no
decision line in the ledger (case 122)."""

import io
import json
import subprocess
from datetime import UTC, datetime

from guppi import gate

NOW = datetime(2026, 9, 14, 11, 0, 0, tzinfo=UTC)
SESSION = "19037d1c-5d15-478c-87d3-2d0cf886f763"
START = "- 10:29:02 19037d1c session-start startup\n"
HI = "- 10:29:12 19037d1c hi\n"
PLAN = "## Case 5 — a rule\n\n> **when:**\n> x.\n\n```then\nupdate:\n  - slug: rule-x\n    contract: same\n    change: y\n```\n"
LINE = "- 10:40:00 decision[case 5][update][rule-x]{ref:rule-x}\n"


def payload(**fields):
    return io.StringIO(json.dumps(fields))


def skill(name="pre-task", session=SESSION):
    return payload(session_id=session, tool_name="Skill", tool_input={"skill": name})


def run(stdin, project_dir, status=None):
    err = io.StringIO()
    code = gate.run([], stdin=stdin, stderr=err, project_dir=project_dir, status=status, now=NOW)
    return code, err.getvalue()


def with_event_log(project_dir, text):
    folder = project_dir / "vault" / "raw" / "2026-09-14"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "event_log.md").write_text(text, encoding="utf-8", newline="\n")


def with_plan(project_dir, text=PLAN):
    folder = project_dir / ".claude" / "plans"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "quiet-plan.md"
    path.write_text(text, encoding="utf-8", newline="\n")
    return path


def with_ledger(project_dir, text):
    folder = project_dir / "vault" / "raw" / "2026-09-14" / "1029"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "ledger.md").write_text(text, encoding="utf-8", newline="\n")


# --- the tree (rule-retro-commit) ---------------------------------------------------------


def test_handoff_on_a_dirty_tree_is_refused_with_the_reason(tmp_path):
    code, err = run(skill("handoff"), tmp_path, status=" M a.py\n?? b.py")
    assert code == 2 and "commit first" in err and "2 path(s)" in err


def test_handoff_on_a_clean_tree_passes(tmp_path):
    assert run(skill("handoff"), tmp_path, status="") == (0, "")


def test_another_skill_or_tool_passes_whatever_the_tree(tmp_path):
    assert run(skill("retro"), tmp_path, status=" M a.py") == (0, "")
    assert run(
        payload(tool_name="Bash", tool_input={"command": "git status"}), tmp_path, status=" M a.py"
    ) == (0, "")
    assert run(io.StringIO(""), tmp_path, status=" M a.py") == (0, "")


def test_the_skill_name_may_carry_a_slash_or_arguments(tmp_path):
    assert (
        run(payload(tool_name="Skill", tool_input={"skill": "/handoff now"}), tmp_path, status="x")[
            0
        ]
        == 2
    )


def test_the_tree_is_read_from_git(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / "a.txt").write_text("x")
    code, err = run(skill("handoff"), tmp_path)
    assert code == 2 and "1 path(s)" in err


# --- the Spec (rule-ledger-write, case 122) ---------------------------------------------


def test_an_item_of_the_plan_without_its_line_refuses_the_skill(tmp_path):
    plan = with_plan(tmp_path)
    with_event_log(tmp_path, START + HI + f"- 10:35:00 19037d1c tool Write: {plan}\n")
    code, err = run(skill("pre-task"), tmp_path, status="")
    assert code == 2
    assert "/pre-task refused" in err and "1 item(s)" in err and "(case 5)" in err
    assert "end this reply in text with the LEDGER block" in err


def test_the_item_with_its_line_in_the_session_ledger_passes(tmp_path):
    plan = with_plan(tmp_path)
    with_event_log(tmp_path, START + HI + f"- 10:35:00 19037d1c tool Edit: {plan}\n")
    with_ledger(tmp_path, LINE)
    assert run(skill("pre-task"), tmp_path, status="") == (0, "")


def test_no_plan_path_in_the_log_and_no_spec_passes(tmp_path):
    with_plan(tmp_path)  # exists, but no log line names it
    with_event_log(tmp_path, START + HI + "- 10:35:00 19037d1c tool Edit: C:\\x\\notes.md\n")
    assert run(skill("pre-task"), tmp_path, status="") == (0, "")


def test_a_defer_item_of_the_session_spec_without_its_line_refuses(tmp_path):
    with_event_log(tmp_path, START + HI)
    folder = tmp_path / "vault" / "raw" / "2026-09-14" / "1029"
    folder.mkdir(parents=True)
    spec = "## Deferred\n\n## Case 7 — later\n\n```then\ndefer:\n  - slug: rule-y\n    type: rule\n    purpose: p\n```\n"
    (folder / "spec.md").write_text(spec, encoding="utf-8", newline="\n")
    code, err = run(skill("handoff"), tmp_path, status="")
    assert code == 2 and "/handoff refused" in err and "(case 7)" in err


def test_the_spec_check_precedes_the_tree_check(tmp_path):
    plan = with_plan(tmp_path)
    with_event_log(tmp_path, START + HI + f"- 10:35:00 19037d1c tool Write: {plan}\n")
    code, err = run(skill("handoff"), tmp_path, status=" M a.py")
    assert code == 2 and "no ledger line" in err and "commit first" not in err


def test_without_a_hi_the_spec_is_not_checked(tmp_path):
    plan = with_plan(tmp_path)
    with_event_log(tmp_path, START + f"- 10:35:00 19037d1c tool Write: {plan}\n")
    assert run(skill("pre-task"), tmp_path, status="") == (0, "")


def test_a_plan_path_of_another_session_does_not_count(tmp_path):
    plan = with_plan(tmp_path)
    with_event_log(tmp_path, START + HI + f"- 10:35:00 fde37e7c tool Write: {plan}\n")
    assert run(skill("pre-task"), tmp_path, status="") == (0, "")


def test_plan_path_takes_the_last_line_under_claude_plans(tmp_path):
    text = (
        "- 10:30:00 19037d1c tool Write: C:\\u\\.claude\\plans\\a.md\n"
        "- 10:31:00 19037d1c tool Edit: C:\\u\\.claude\\plans\\b.md\n"
        "- 10:32:00 19037d1c tool Edit: C:\\u\\src\\c.py\n"
    )
    logs = [("2026-09-14", text)]
    assert gate.plan_path(logs, "19037d1c").name == "b.md"
    assert gate.plan_path(logs, "aaaaaaaa") is None


# --- the mark (rule-event-log, case 136.1) ------------------------------------------------


def event_log(project_dir):
    return (project_dir / "vault" / "raw" / "2026-09-14" / "event_log.md").read_text(
        encoding="utf-8"
    )


def test_a_pretask_call_that_passes_leaves_the_stamped_mark(tmp_path):
    with_event_log(tmp_path, START + HI)
    assert run(skill("pre-task"), tmp_path, status="") == (0, "")
    assert event_log(tmp_path).endswith("- 11:00:00 19037d1c pretask\n")


def test_retro_and_handoff_leave_their_marks(tmp_path):
    with_event_log(tmp_path, START + HI)
    run(skill("retro"), tmp_path, status="")
    run(skill("handoff"), tmp_path, status="")
    assert event_log(tmp_path).endswith("19037d1c retro\n- 11:00:00 19037d1c handoff\n")


def test_a_refused_call_leaves_no_mark(tmp_path):
    with_event_log(tmp_path, START + HI)
    code, _ = run(skill("handoff"), tmp_path, status=" M a.py")
    assert code == 2 and "handoff" not in event_log(tmp_path)
    plan = with_plan(tmp_path)
    with_event_log(tmp_path, START + HI + f"- 10:35:00 19037d1c tool Edit: {plan}\n")
    code, _ = run(skill("pre-task"), tmp_path, status="")
    assert code == 2 and "pretask" not in event_log(tmp_path)


def test_another_skill_leaves_no_mark(tmp_path):
    with_event_log(tmp_path, START + HI)
    assert run(skill("hi"), tmp_path, status="") == (0, "")
    assert event_log(tmp_path) == START + HI


def test_the_mark_without_a_log_creates_the_day_folder(tmp_path):
    assert run(skill("pre-task"), tmp_path, status="") == (0, "")
    assert event_log(tmp_path) == "- 11:00:00 19037d1c pretask\n"


def test_cli_dispatches_to_gate(tmp_path, monkeypatch, capsys):
    from guppi import cli

    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", payload(tool_name="Skill", tool_input={"skill": "retro"}))
    assert cli.main(["gate"]) == 0
