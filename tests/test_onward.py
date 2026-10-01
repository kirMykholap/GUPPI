"""`guppi onward`: the `Stop` hook that sends the agent from the end of Retro to `/handoff`
(case 531.9). Rule page: `vault/wiki/rules/rule-retro-onward.md`."""

import io
import json
import os
from datetime import UTC, datetime

import pytest

from guppi import onward

NOW = datetime(2026, 9, 30, 12, 0, 0, tzinfo=UTC)
SESSION = "19037d1c-5d15"
START = "- 10:29:02 19037d1c session-start startup\n"
HI = "- 10:30:00 19037d1c hi\n"
RETRO = "- 11:50:00 19037d1c retro\n"
FOLDER = ("2026-09-30", "1030")


def payload(reply="Retro done.", **fields):
    fields.setdefault("session_id", SESSION)
    return io.StringIO(json.dumps({"last_assistant_message": reply, **fields}))


def with_event_log(project_dir, text):
    day = project_dir / "vault" / "raw" / FOLDER[0]
    day.mkdir(parents=True, exist_ok=True)
    (day / "event_log.md").write_text(text, encoding="utf-8")
    return day


def run(stdin, project_dir):
    err = io.StringIO()
    code = onward.run([], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def test_after_the_retro_mark_with_no_handoff_the_reply_is_refused(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    code, err = run(payload(), tmp_path)
    assert code == 2
    assert err == onward.REASON + "\n"
    assert "/handoff" in err and "STOP:" in err and "vault/wiki/where-to-stop.md" in err


def test_before_the_retro_mark_it_is_silent(tmp_path):
    with_event_log(tmp_path, START + HI)
    assert run(payload(), tmp_path) == (0, "")


def test_once_handoff_md_stands_it_is_silent(tmp_path):
    day = with_event_log(tmp_path, START + HI + RETRO)
    (day / FOLDER[1]).mkdir()
    (day / FOLDER[1] / "handoff.md").write_text("# Handoff\n", encoding="utf-8")
    assert run(payload(), tmp_path) == (0, "")


def test_on_the_re_fire_after_a_refusal_it_is_silent(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    assert run(payload(stop_hook_active=True), tmp_path) == (0, "")


@pytest.mark.parametrize("reply", ["STOP: the test cannot be fixed; revert it?", "\nSTOP: ask"])
def test_a_reply_that_opens_with_stop_is_let_through(tmp_path, reply):
    with_event_log(tmp_path, START + HI + RETRO)
    assert run(payload(reply), tmp_path) == (0, "")


def test_without_a_hi_it_is_silent(tmp_path):
    with_event_log(tmp_path, START + RETRO)
    assert run(payload(), tmp_path) == (0, "")


def test_a_retro_mark_of_another_session_does_not_count(tmp_path):
    with_event_log(tmp_path, START + HI + "- 11:50:00 aaaaaaaa retro\n")
    assert run(payload(), tmp_path) == (0, "")


def test_it_writes_nothing(tmp_path):
    day = with_event_log(tmp_path, START + HI + RETRO)
    before = sorted(p.relative_to(tmp_path) for p in tmp_path.rglob("*"))
    run(payload(), tmp_path)
    assert sorted(p.relative_to(tmp_path) for p in tmp_path.rglob("*")) == before
    assert (day / "event_log.md").read_text(encoding="utf-8") == START + HI + RETRO


def test_an_unreadable_payload_passes(tmp_path):
    assert run(io.StringIO("not json"), tmp_path) == (0, "")


# --- the hook's own error (case 555.3) ----------------------------------------------------


def boom(*args, **kwargs):
    raise RuntimeError("boom")


def test_error_an_error_of_its_own_exits_2_with_the_advice(tmp_path, monkeypatch):
    with_event_log(tmp_path, START + HI)
    monkeypatch.setattr(onward, "retro_marked", boom)
    code, err = run(payload(), tmp_path)
    assert code == 2
    assert err.startswith("onward: not checked: boom")
    assert "/handoff" in err and "handoff.md does not stand" in err


def test_error_the_re_fire_exits_0_and_prints_nothing(tmp_path, monkeypatch):
    with_event_log(tmp_path, START + HI)
    monkeypatch.setattr(onward, "retro_marked", boom)
    assert run(payload(stop_hook_active=True), tmp_path) == (0, "")


def test_error_an_empty_payload_exits_0(tmp_path, monkeypatch):
    monkeypatch.setattr(onward, "retro_marked", boom)
    assert run(io.StringIO(""), tmp_path) == (0, "")


# --- `--plan`: from the last ratification to /pre-spec and to the exit (case 561.5) ----

PRESPEC = "- 11:00:00 19037d1c prespec\n"
CLOSED = (
    "# Frontier\n\n## Cases\n\n- [x] C1 — one · brief · case 7\n\n## Work\n\n- [ ] W1 — r · brief\n"
)
OPEN = "# Frontier\n\n## Cases\n\n- [ ] C1 — one · brief\n"
RATIFIED = "```LEDGER\n- decision[case 7][update][rule-x]{ref:rule-x}\n```\n\n## Frontier"


def plan_session(project_dir, frontier=CLOSED, log=START + HI, ledger=""):
    day = with_event_log(project_dir, log)
    folder = day / FOLDER[1]
    folder.mkdir(exist_ok=True)
    (folder / "frontier.md").write_text(frontier, encoding="utf-8")
    (folder / "ledger.md").write_text(ledger, encoding="utf-8")
    return folder


def run_plan(stdin, project_dir):
    err = io.StringIO()
    code = onward.run(["--plan"], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def with_case_file(folder, case, mtime):
    (folder / "cases").mkdir(exist_ok=True)
    path = folder / "cases" / f"case-{case}.md"
    path.write_text("## Case\n", encoding="utf-8")
    os.utime(path, (mtime.timestamp(), mtime.timestamp()))


def test_plan_the_last_ratification_sends_the_agent_to_prespec(tmp_path):
    plan_session(tmp_path)
    code, err = run_plan(payload(RATIFIED), tmp_path)
    assert code == 2
    assert err == onward.TO_PRESPEC + "\n"
    assert "/pre-spec" in err and "STOP:" in err


def test_plan_after_prespec_sends_the_agent_to_the_check_and_the_exit(tmp_path):
    plan_session(tmp_path, log=START + HI + PRESPEC)
    code, err = run_plan(payload(RATIFIED), tmp_path)
    assert code == 2
    assert err == onward.TO_EXIT + "\n"
    assert "prespec --check" in err and "ExitPlanMode" in err


def test_plan_an_open_cases_line_is_silent(tmp_path):
    plan_session(tmp_path, frontier=OPEN)
    assert run_plan(payload(RATIFIED), tmp_path) == (0, "")


def test_plan_once_spec_md_stands_it_is_silent(tmp_path):
    folder = plan_session(tmp_path)
    (folder / "spec.md").write_text("# Spec\n", encoding="utf-8")
    assert run_plan(payload(RATIFIED), tmp_path) == (0, "")


def test_plan_a_reply_with_no_ledger_block_is_silent(tmp_path):
    plan_session(tmp_path)
    assert run_plan(payload("## Frontier"), tmp_path) == (0, "")


def test_plan_a_case_file_newer_than_its_last_decision_line_is_silent(tmp_path):
    ledger = "- 11:10:00 decision[case 5.1][update][rule-y]{ref:rule-y}\n"
    folder = plan_session(tmp_path, ledger=ledger)
    with_case_file(folder, "5", datetime(2026, 9, 30, 11, 20, 0, tzinfo=UTC))
    assert run_plan(payload(RATIFIED), tmp_path) == (0, "")


def test_plan_a_case_file_older_than_its_last_decision_line_is_no_case_out(tmp_path):
    ledger = "- 11:10:00 decision[case 5.1][update][rule-y]{ref:rule-y}\n"
    folder = plan_session(tmp_path, ledger=ledger)
    with_case_file(folder, "5", datetime(2026, 9, 30, 11, 0, 0, tzinfo=UTC))
    with_case_file(folder, "7", datetime(2026, 9, 30, 11, 30, 0, tzinfo=UTC))  # ratified now
    assert run_plan(payload(RATIFIED), tmp_path)[0] == 2


def test_plan_the_re_fire_is_silent(tmp_path):
    plan_session(tmp_path)
    assert run_plan(payload(RATIFIED, stop_hook_active=True), tmp_path) == (0, "")


def test_plan_a_reply_that_opens_with_stop_is_let_through(tmp_path):
    plan_session(tmp_path)
    assert run_plan(payload("STOP: a question\n" + RATIFIED), tmp_path) == (0, "")


def test_plan_without_a_hi_it_is_silent(tmp_path):
    plan_session(tmp_path, log=START)
    assert run_plan(payload(RATIFIED), tmp_path) == (0, "")


def test_plan_an_error_of_its_own_exits_2_with_the_advice(tmp_path, monkeypatch):
    plan_session(tmp_path)
    monkeypatch.setattr(onward, "plan_onward", boom)
    code, err = run_plan(payload(RATIFIED), tmp_path)
    assert code == 2
    assert err.startswith("onward: not checked: boom") and "/pre-spec" in err


def test_plan_the_run_without_the_flag_is_unchanged(tmp_path):
    plan_session(tmp_path, log=START + HI + RETRO)
    code, err = run(payload(RATIFIED), tmp_path)
    assert (code, err) == (2, onward.REASON + "\n")
