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


def human(text="go on"):
    return {"type": "user", "origin": {"kind": "human"}, "message": {"content": text}}


def refusal(command, text="refused"):
    return {
        "type": "user",
        "isMeta": True,
        "message": {"content": f"Stop hook feedback:\n[{command}]: {text}"},
    }


def transcript(project_dir, *records):
    path = project_dir / "transcript.jsonl"
    path.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")
    return str(path)


def test_with_the_flag_set_and_no_readable_transcript_it_is_silent(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    assert run(payload(stop_hook_active=True), tmp_path) == (0, "")


def test_a_refusal_of_another_hook_in_the_stretch_does_not_silence_it(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    path = transcript(tmp_path, human(), refusal("uv run guppi onward --plan"))
    code, err = run(payload(stop_hook_active=True, transcript_path=path), tmp_path)
    assert (code, err) == (2, onward.REASON + "\n")


def test_its_own_refusal_in_the_stretch_silences_it(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    path = transcript(tmp_path, human(), refusal("uv run guppi onward", onward.REASON))
    assert run(payload(stop_hook_active=True, transcript_path=path), tmp_path) == (0, "")
    assert run(payload(transcript_path=path), tmp_path) == (0, "")


def test_after_a_later_message_of_the_person_it_refuses_again(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    path = transcript(tmp_path, refusal("uv run guppi onward", onward.REASON), human())
    code, err = run(payload(transcript_path=path), tmp_path)
    assert (code, err) == (2, onward.REASON + "\n")


def test_a_task_notification_does_not_open_a_new_stretch(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    notice = {"type": "user", "origin": {"kind": "task-notification"}, "message": {"content": "x"}}
    path = transcript(tmp_path, human(), refusal("uv run guppi onward"), notice)
    assert run(payload(transcript_path=path), tmp_path) == (0, "")


def reply(text="Retro done.", timestamp=None):
    record = {"type": "assistant", "message": {"content": [{"type": "text", "text": text}]}}
    if timestamp is not None:
        record["timestamp"] = timestamp
    return record


LEDGER = "uv run guppi ledger"


def test_a_ledger_refusal_of_the_same_reply_sends_it_on_again(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    path = transcript(
        tmp_path,
        human(),
        reply(),
        refusal(LEDGER, "ledger: lesson[x] not written"),
        refusal("uv run guppi onward", onward.REASON),
        reply("```LEDGER\n- lesson[...]\n```"),
    )
    code, err = run(payload(stop_hook_active=True, transcript_path=path), tmp_path)
    assert (code, err) == (2, onward.REASON + "\n")


def test_a_ledger_refusal_of_a_later_reply_sends_it_on_again(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    path = transcript(
        tmp_path,
        human(),
        reply(),
        refusal("uv run guppi onward", onward.REASON),
        reply("the rewrite"),
        refusal(LEDGER, "ledger: line not written"),
        reply("again"),
    )
    assert run(payload(transcript_path=path), tmp_path)[0] == 2


def test_a_ledger_refusal_only_before_its_own_refusal_leaves_it_spent(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    path = transcript(
        tmp_path,
        human(),
        reply(),
        refusal(LEDGER, "ledger: line not written"),
        reply("the rewrite"),
        refusal("uv run guppi onward", onward.REASON),
        reply("committed"),
    )
    assert run(payload(transcript_path=path), tmp_path) == (0, "")


def test_a_refusal_of_another_hook_after_its_own_leaves_it_spent(tmp_path):
    with_event_log(tmp_path, START + HI + RETRO)
    path = transcript(
        tmp_path,
        human(),
        reply(),
        refusal("uv run guppi onward", onward.REASON),
        reply("next"),
        refusal("uv run guppi casecheck", "casecheck: refused"),
        reply("again"),
    )
    assert run(payload(transcript_path=path), tmp_path) == (0, "")


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


def test_error_with_the_flag_and_no_readable_transcript_exits_0(tmp_path, monkeypatch):
    with_event_log(tmp_path, START + HI)
    monkeypatch.setattr(onward, "retro_marked", boom)
    assert run(payload(stop_hook_active=True), tmp_path) == (0, "")


def test_error_with_its_own_refusal_in_the_stretch_exits_0(tmp_path, monkeypatch):
    with_event_log(tmp_path, START + HI)
    monkeypatch.setattr(onward, "retro_marked", boom)
    path = transcript(tmp_path, human(), refusal("uv run guppi onward", "onward: not checked"))
    assert run(payload(transcript_path=path), tmp_path) == (0, "")


def test_error_with_its_own_refusal_and_a_later_ledger_refusal_exits_0(tmp_path, monkeypatch):
    with_event_log(tmp_path, START + HI)
    monkeypatch.setattr(onward, "retro_marked", boom)
    path = transcript(
        tmp_path,
        human(),
        reply(),
        refusal("uv run guppi onward", "onward: not checked"),
        reply("next"),
        refusal(LEDGER, "ledger: line not written"),
        reply("again"),
    )
    assert run(payload(transcript_path=path), tmp_path) == (0, "")


def test_error_after_another_hooks_refusal_with_the_flag_exits_2(tmp_path, monkeypatch):
    with_event_log(tmp_path, START + HI)
    monkeypatch.setattr(onward, "retro_marked", boom)
    path = transcript(tmp_path, human(), refusal("uv run guppi ledger"))
    code, err = run(payload(stop_hook_active=True, transcript_path=path), tmp_path)
    assert code == 2 and err.startswith("onward: not checked: boom")


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
    """A Case built again after the `prespec` line and ratified now (case 686.1)."""
    folder = plan_session(tmp_path, log=START + HI + PRESPEC)
    with_case_file(folder, "7", datetime(2026, 9, 30, 11, 30, 0, tzinfo=UTC))
    code, err = run_plan(payload(RATIFIED), tmp_path)
    assert code == 2
    assert err == onward.TO_EXIT + "\n"
    assert "prespec --check" in err and "ExitPlanMode" in err


# --- case 686.1: the loop after the findings told from its end --------------------------
# `estimate-prespec-onward-tells-the-loop-from-its-end`


def test_loop_no_case_file_after_prespec_sends_the_agent_on_with_the_loop(tmp_path):
    plan_session(tmp_path, log=START + HI + PRESPEC)
    code, err = run_plan(payload(RATIFIED), tmp_path)
    assert (code, err) == (2, onward.TO_LOOP + "\n")
    assert "case-guppi" in err and "prespec --check" in err and "ratified" not in err


def test_loop_only_case_files_older_than_the_prespec_line_send_it_on_with_the_loop(tmp_path):
    folder = plan_session(tmp_path, log=START + HI + PRESPEC)
    with_case_file(folder, "7", datetime(2026, 9, 30, 10, 50, 0, tzinfo=UTC))
    assert run_plan(payload(RATIFIED), tmp_path) == (2, onward.TO_LOOP + "\n")


def test_loop_a_case_built_again_and_not_ratified_keeps_it_silent(tmp_path):
    folder = plan_session(tmp_path, log=START + HI + PRESPEC)
    with_case_file(folder, "8", datetime(2026, 9, 30, 11, 20, 0, tzinfo=UTC))
    assert run_plan(payload(RATIFIED), tmp_path) == (0, "")


def test_loop_the_last_prespec_line_counts(tmp_path):
    later = "- 11:40:00 19037d1c prespec\n"
    folder = plan_session(tmp_path, log=START + HI + PRESPEC + later)
    with_case_file(folder, "7", datetime(2026, 9, 30, 11, 30, 0, tzinfo=UTC))
    assert run_plan(payload(RATIFIED), tmp_path) == (2, onward.TO_LOOP + "\n")


@pytest.mark.parametrize(
    "mtime, reason",
    [
        (datetime(2026, 9, 30, 0, 20, 0, tzinfo=UTC), onward.TO_EXIT),
        (datetime(2026, 9, 29, 23, 59, 0, tzinfo=UTC), onward.TO_LOOP),
    ],
)
def test_loop_a_session_across_midnight_reads_the_line_on_its_date(tmp_path, mtime, reason):
    first = tmp_path / "vault" / "raw" / "2026-09-29"
    first.mkdir(parents=True)
    (first / "event_log.md").write_text(
        "- 23:20:00 19037d1c session-start startup\n- 23:30:00 19037d1c hi\n", encoding="utf-8"
    )
    with_event_log(tmp_path, "- 00:10:00 19037d1c prespec\n")
    folder = first / "2330"
    folder.mkdir()
    (folder / "frontier.md").write_text(CLOSED, encoding="utf-8")
    with_case_file(folder, "7", mtime)
    assert run_plan(payload(RATIFIED), tmp_path) == (2, reason + "\n")


@pytest.mark.parametrize("block, code", [(True, 2), (False, 0)])
def test_loop_the_reply_after_a_reminder_of_the_ledger_hook(tmp_path, block, code):
    """Its reason and the reminder of case 685.1 stand at the same `Stop`; the answer with a
    `LEDGER` block is sent on again, the answer with none is not."""
    folder = plan_session(tmp_path, log=START + HI + PRESPEC)
    with_case_file(folder, "7", datetime(2026, 9, 30, 11, 30, 0, tzinfo=UTC))
    reminded = "ledger: lesson[lesson-x] has no mark — did case 7 fix its cause?"
    records = [human(), reply(), refusal(LEDGER, reminded), refusal(PLAN, onward.TO_EXIT)]
    path = transcript(tmp_path, *records, reply())
    marked = "```LEDGER\n- decision[case 7][update][rule-x]{ref:rule-x}{addresses:lesson-x}\n```\n"
    text = marked if block else "Case 7 fixed no cause of it."
    stdin = payload(text, stop_hook_active=True, transcript_path=path)
    assert run_plan(stdin, tmp_path)[0] == code


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


def test_plan_the_flag_with_a_transcript_it_cannot_read_is_silent(tmp_path):
    plan_session(tmp_path)
    assert run_plan(payload(RATIFIED, stop_hook_active=True), tmp_path) == (0, "")


PLAN = "uv run guppi onward --plan"


def test_plan_the_flag_and_another_hooks_refusal_send_it_on(tmp_path):
    plan_session(tmp_path)
    path = transcript(tmp_path, human(), reply(), refusal("uv run guppi casecheck"), reply())
    code, err = run_plan(payload(RATIFIED, stop_hook_active=True, transcript_path=path), tmp_path)
    assert (code, err) == (2, onward.TO_PRESPEC + "\n")


@pytest.mark.parametrize("later", [False, True])
def test_plan_a_ledger_refusal_after_its_own_sends_it_on_again(tmp_path, later):
    plan_session(tmp_path)
    records = [human(), reply(), refusal(LEDGER, "ledger: lesson[x] not written")]
    records.append(refusal(PLAN, onward.TO_PRESPEC))
    if later:
        records[2:4] = [records[3], reply("the rewrite"), records[2]]
    path = transcript(tmp_path, *records, reply())
    code, err = run_plan(payload(RATIFIED, stop_hook_active=True, transcript_path=path), tmp_path)
    assert (code, err) == (2, onward.TO_PRESPEC + "\n")


def test_plan_its_own_refusal_with_no_later_ledger_refusal_is_silent(tmp_path):
    plan_session(tmp_path)
    path = transcript(tmp_path, human(), reply(), refusal(PLAN, onward.TO_PRESPEC), reply())
    assert run_plan(payload(RATIFIED, stop_hook_active=True, transcript_path=path), tmp_path) == (
        0,
        "",
    )


def test_plan_an_error_with_its_own_refusal_in_the_stretch_exits_0(tmp_path, monkeypatch):
    plan_session(tmp_path)
    monkeypatch.setattr(onward, "plan_onward", boom)
    path = transcript(tmp_path, human(), reply(), refusal(PLAN, "onward: not checked"), reply())
    assert run_plan(payload(RATIFIED, transcript_path=path), tmp_path) == (0, "")


LESSON = (
    "```LEDGER\n- lesson[error][lesson-x-y]{tags:hooks} trigger: t root_cause: r\n```\n## Frontier"
)


def test_plan_a_case_ratified_by_an_earlier_reply_of_the_stretch_is_not_out(tmp_path):
    ledger = "- 11:10:00 decision[case 5.1][update][rule-y]{ref:rule-y}\n"
    folder = plan_session(tmp_path, ledger=ledger)
    with_case_file(folder, "5", datetime(2026, 9, 30, 11, 20, 0, tzinfo=UTC))
    ratified = "```LEDGER\n- decision[case 5.1][update][rule-y]{ref:rule-y}\n```"
    path = transcript(tmp_path, human(), reply(ratified, "2026-09-30T11:30:00Z"))
    assert run_plan(payload(LESSON, transcript_path=path), tmp_path)[0] == 2


def test_plan_a_case_ratified_before_the_persons_last_message_is_not_out(tmp_path):
    # case 604: the ratifying reply stands before the person's last message; its file was
    # written before that reply and after its line in ledger.md
    ledger = "- 11:10:00 decision[case 5.1][update][rule-y]{ref:rule-y}\n"
    folder = plan_session(tmp_path, ledger=ledger)
    with_case_file(folder, "5", datetime(2026, 9, 30, 11, 20, 0, tzinfo=UTC))
    ratified = "```LEDGER\n- decision[case 5.1][update][rule-y]{ref:rule-y}\n```"
    path = transcript(
        tmp_path,
        human(),
        reply(ratified, "2026-09-30T11:30:00Z"),
        human("C2"),
        reply("the next Case", "2026-09-30T11:40:00Z"),
    )
    assert run_plan(payload(LESSON, transcript_path=path), tmp_path)[0] == 2


def test_plan_a_case_with_no_reply_that_ratified_it_is_out(tmp_path):
    ledger = "- 11:10:00 decision[case 5.1][update][rule-y]{ref:rule-y}\n"
    folder = plan_session(tmp_path, ledger=ledger)
    with_case_file(folder, "5", datetime(2026, 9, 30, 11, 20, 0, tzinfo=UTC))
    path = transcript(tmp_path, human(), reply("no block", "2026-09-30T11:30:00Z"))
    assert run_plan(payload(LESSON, transcript_path=path), tmp_path) == (0, "")


def test_plan_a_record_with_no_readable_time_counts_none_of_its_lines(tmp_path):
    ledger = "- 11:10:00 decision[case 5.1][update][rule-y]{ref:rule-y}\n"
    folder = plan_session(tmp_path, ledger=ledger)
    with_case_file(folder, "5", datetime(2026, 9, 30, 11, 20, 0, tzinfo=UTC))
    ratified = "```LEDGER\n- decision[case 5.1][update][rule-y]{ref:rule-y}\n```"
    path = transcript(tmp_path, human(), reply(ratified, "not a time"))
    assert run_plan(payload(LESSON, transcript_path=path), tmp_path) == (0, "")


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
