"""`guppi onward`: the `Stop` hook that sends the agent from the end of Retro to `/handoff`
(case 531.9). Rule page: `vault/wiki/rules/rule-retro-onward.md`."""

import io
import json
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
