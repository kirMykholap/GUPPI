"""The pinned clock of the tests (case 145.1): a `run()` without `now` sees the year 2001."""

import io
import json
from datetime import UTC, datetime

from guppi import event, gate, ledger


def test_a_run_without_now_writes_under_the_pinned_date(tmp_path):
    stdin = io.StringIO(json.dumps({"session_id": "abc12345", "hook_event_name": "SessionStart"}))
    code = event.run(["session-start"], stdin=stdin, stderr=io.StringIO(), project_dir=tmp_path)
    assert code == 0
    path = tmp_path / "vault" / "raw" / "2001-01-01" / "event_log.md"
    assert path.exists()
    assert path.read_text(encoding="utf-8").startswith("- 00:00:00 abc12345 session-start")


def test_every_clock_module_is_pinned(pinned_clock):
    for module in (event, ledger, gate):
        assert module.datetime.__name__ == "PinnedDatetime"
        assert module.datetime.now().year == 2001
        assert module.datetime.now().astimezone() == pinned_clock


def test_the_pinned_class_keeps_the_rest_of_datetime():
    pinned = event.datetime
    assert pinned(2026, 9, 14, tzinfo=UTC) == datetime(2026, 9, 14, tzinfo=UTC)
    assert pinned.strptime("2026-09-14", "%Y-%m-%d").month == 9
    assert pinned.fromisoformat("2026-09-14T10:00:00").hour == 10
    assert pinned.now().astimezone(UTC) == datetime(2001, 1, 1, tzinfo=UTC)
    assert isinstance(pinned.now(), datetime)
