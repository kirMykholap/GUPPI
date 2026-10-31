"""`guppi libreport`: the `SubagentStop` hook that copies the last output of `librarian-guppi`
into `report.md` of the session folder (case 956.1, `estimate-librarian-report-copy-writes-
the-file`). Rule page: `vault/wiki/rules/rule-librarian-report-copy.md`.

Every test feeds the payload through a stream, the shape a hook is really handed, over a
transcript and an event log under a temporary folder."""

import io
import json
from datetime import UTC, datetime

import pytest

from guppi import libreport

NOW = datetime(2026, 9, 9, 15, 20, 0, tzinfo=UTC)
SESSION = "44c1aae1-4076-4a58-a7c0-d20bc274047c"
EVENT_LOG = """- 15:01:00 44c1aae1 session-start startup
- 15:01:30 44c1aae1 hi
- 15:02:00 44c1aae1 tool Bash: git status --short
"""
REPORT = "# Report\n\n- Pages created: 2.\n- Lint total: 0.\n"


@pytest.fixture
def project(tmp_path):
    log = tmp_path / "vault" / "raw" / "2026-09-09" / "event_log.md"
    log.parent.mkdir(parents=True)
    log.write_text(EVENT_LOG, encoding="utf-8")
    (tmp_path / "vault" / "raw" / "2026-09-09" / "1501").mkdir()
    return tmp_path


def folder(project):
    return project / "vault" / "raw" / "2026-09-09" / "1501"


def text_block(text):
    return {"type": "text", "text": text}


def handback_block(message):
    return {"type": "tool_use", "name": "SubagentHandback", "input": {"message": message}}


def transcript(project, *blocks):
    path = project / "agent-librarian.jsonl"
    lines = [
        json.dumps({"type": "assistant", "isSidechain": True, "message": {"content": [block]}})
        for block in blocks
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(path)


def run(project, **fields):
    fields.setdefault("session_id", SESSION)
    fields.setdefault("hook_event_name", "SubagentStop")
    fields.setdefault("agent_type", "librarian-guppi")
    out, err = io.StringIO(), io.StringIO()
    stdin = io.StringIO(json.dumps(fields))
    code = libreport.run([], stdin=stdin, stdout=out, stderr=err, project_dir=project, now=NOW)
    return code, out.getvalue(), err.getvalue()


def report(project):
    return (folder(project) / "report.md").read_text(encoding="utf-8")


def test_the_last_text_of_the_librarian_is_written_whole(project):
    path = transcript(project, text_block("Running materialize."), text_block(REPORT))
    assert run(project, agent_transcript_path=path) == (0, "", "")
    assert report(project) == REPORT


def test_a_last_handback_message_is_written_and_replaces_a_file_that_stands(project):
    (folder(project) / "report.md").write_text("old\n", encoding="utf-8")
    path = transcript(project, text_block("Committed."), handback_block(REPORT))
    assert run(project, agent_transcript_path=path) == (0, "", "")
    assert report(project) == REPORT


def test_a_second_fire_writes_the_file_again_from_the_last_output(project):
    first = transcript(project, text_block("A first text."))
    run(project, agent_transcript_path=first)
    assert report(project) == "A first text.\n"
    second = transcript(project, text_block("A first text."), handback_block(REPORT))
    assert run(project, agent_transcript_path=second) == (0, "", "")
    assert report(project) == REPORT


def test_another_agent_writes_nothing(project):
    path = transcript(project, text_block(REPORT))
    assert run(project, agent_type="case-guppi", agent_transcript_path=path) == (0, "", "")
    assert not (folder(project) / "report.md").exists()


def test_no_readable_transcript_writes_nothing_with_one_line(project):
    code, out, err = run(project, agent_transcript_path=str(project / "missing.jsonl"))
    assert (code, out) == (0, "")
    assert len(err.splitlines()) == 1 and "not readable" in err
    assert not (folder(project) / "report.md").exists()


def test_no_output_writes_nothing_with_one_line(project):
    path = transcript(project, {"type": "tool_use", "name": "Bash", "input": {"command": "x"}})
    code, out, err = run(project, agent_transcript_path=path)
    assert (code, out) == (0, "")
    assert len(err.splitlines()) == 1 and "no output" in err
    assert not (folder(project) / "report.md").exists()


def test_no_session_folder_writes_nothing_with_one_line(project):
    path = transcript(project, text_block(REPORT))
    code, out, err = run(project, session_id="deadbeef-0000", agent_transcript_path=path)
    assert (code, out) == (0, "")
    assert len(err.splitlines()) == 1 and "no session folder" in err
    assert not (folder(project) / "report.md").exists()


def test_a_payload_that_is_not_json_blocks_nothing(project):
    err = io.StringIO()
    code = libreport.run(
        [],
        stdin=io.StringIO("not json"),
        stdout=io.StringIO(),
        stderr=err,
        project_dir=project,
        now=NOW,
    )
    assert code == 0 and len(err.getvalue().splitlines()) == 1
