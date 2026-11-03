"""`guppi frontierguard`: the `PreToolUse` hook that refuses an `Edit`, a `Write` or a
`MultiEdit` of a session's `frontier.md` which leaves an open box beside a closer (case 1012).
Rule page: `vault/wiki/rules/rule-frontier-hook.md`.

Every test feeds the payload through a stream, the shape a hook is really handed; the session
folder stands under a temporary folder, and the clock is pinned.
"""

import io
import json
from datetime import UTC, datetime

from guppi import frontierguard

NOW = datetime(2026, 11, 3, 1, 2, 3, tzinfo=UTC)
OPEN = "- [ ] C2 — The threshold of the note · brief"
FRONTIER = f"""# Frontier — session 2155

## Cases

- [x] C1 — The clean branch · sprint · work
{OPEN}

Backlog: 11 items

## Work

## Ask
"""


def frontier(project, text=FRONTIER, folder="vault/raw/2026-11-02/2155"):
    path = project / folder / "frontier.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return path


def payload(tool, file_path, **tool_input):
    fields = {
        "session_id": "c818d971-be31-4157-ab5d-802bd511827f",
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": {"file_path": str(file_path), **tool_input},
    }
    return io.StringIO(json.dumps(fields))


def edit(path, old, new, **more):
    return payload("Edit", path, old_string=old, new_string=new, **more)


def run(stdin, project_dir):
    err = io.StringIO()
    code = frontierguard.run([], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def log(project):
    path = project / "vault" / "raw" / "2026-11-03" / "event_log.md"
    return path.read_text(encoding="utf-8").splitlines() if path.is_file() else []


def test_an_edit_that_appends_a_closer_to_an_open_line_is_refused(tmp_path):
    path = frontier(tmp_path)
    code, err = run(edit(path, "note · brief", "note · brief · case 7"), tmp_path)
    assert code == 2
    assert "C2 (· case 7)" in err and "[x] for an item ended" in err


def test_the_same_edit_with_the_box_closed_passes(tmp_path):
    path = frontier(tmp_path)
    closed = OPEN.replace("[ ]", "[x]") + " · case 7"
    assert run(edit(path, OPEN, closed), tmp_path) == (0, "")


def test_a_write_that_leaves_such_a_line_anywhere_is_refused(tmp_path):
    path = frontier(tmp_path)
    text = FRONTIER.replace("## Ask\n", "## Ask\n\n- [ ] A1 — `x` — a question · brief · work\n")
    code, err = run(payload("Write", path, content=text), tmp_path)
    assert code == 2 and "A1 (· work)" in err


def test_a_multiedit_that_leaves_such_a_line_is_refused(tmp_path):
    path = frontier(tmp_path)
    edits = [
        {"old_string": "sprint · work", "new_string": "sprint · work"},
        {"old_string": "note · brief", "new_string": "note · brief · defer case 9"},
    ]
    code, err = run(payload("MultiEdit", path, edits=edits), tmp_path)
    assert code == 2 and "C2 (· defer case 9)" in err


def test_a_replace_all_edit_is_judged_on_every_match(tmp_path):
    path = frontier(tmp_path, FRONTIER.replace(OPEN, f"{OPEN}\n- [ ] C3 — Another · brief"))
    code, err = run(edit(path, " · brief", " · brief · kept", replace_all=True), tmp_path)
    assert code == 2 and "C2 (· kept)" in err and "C3 (· kept)" in err


def test_an_open_line_with_no_closer_passes(tmp_path):
    path = frontier(tmp_path)
    added = f"{OPEN}\n- [ ] C3 — work on the hook · brief"
    assert run(edit(path, OPEN, added), tmp_path) == (0, "")


def test_a_frontier_outside_a_session_folder_passes(tmp_path):
    path = frontier(tmp_path, folder="vault/raw/2026-11-02")
    assert run(edit(path, "note · brief", "note · brief · case 7"), tmp_path) == (0, "")


def test_another_file_and_another_tool_pass(tmp_path):
    path = frontier(tmp_path)
    other = path.with_name("spec.md")
    other.write_text(FRONTIER, encoding="utf-8")
    assert run(edit(other, "note · brief", "note · brief · case 7"), tmp_path) == (0, "")
    assert run(payload("Read", path), tmp_path) == (0, "")


def test_a_missing_old_string_or_a_missing_file_passes(tmp_path):
    path = frontier(tmp_path)
    assert run(edit(path, "not there", "x · case 7"), tmp_path) == (0, "")
    path.unlink()
    assert run(edit(path, "note · brief", "note · brief · case 7"), tmp_path) == (0, "")


def test_an_old_string_found_twice_without_replace_all_passes(tmp_path):
    path = frontier(tmp_path, FRONTIER.replace(OPEN, f"{OPEN}\n- [ ] C3 — Another · brief"))
    assert run(edit(path, " · brief", " · brief · case 7"), tmp_path) == (0, "")


def test_an_unreadable_payload_passes_with_one_line(tmp_path):
    code, err = run(io.StringIO("not json"), tmp_path)
    assert code == 0 and err.strip() == "frontierguard: payload not readable, check skipped"


def test_a_relative_path_is_read_from_the_project(tmp_path):
    frontier(tmp_path)
    rel = "vault/raw/2026-11-02/2155/frontier.md"
    code, _ = run(edit(rel, "note · brief", "note · brief · case 7"), tmp_path)
    assert code == 2


def test_a_refusal_writes_one_line_to_the_event_log(tmp_path):
    path = frontier(tmp_path)
    run(edit(path, "note · brief", "note · brief · case 7"), tmp_path)
    lines = log(tmp_path)
    assert len(lines) == 1 and "frontierguard refused Edit" in lines[0]
    assert run(edit(path, "Backlog", "Backlog"), tmp_path) == (0, "")
    assert len(log(tmp_path)) == 1  # a call that passes writes no line
