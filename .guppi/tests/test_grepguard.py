"""`guppi grepguard`: the `PreToolUse Grep` hook that ends the glob of every search over the
wiki with `!**/decisions/**` (case 664.1, `estimate-search-leaves-out-decisions-by-the-grep-
hook`). Rule page: `vault/wiki/rules/rule-search-leaves-out-decisions.md`.

Every test feeds the payload through a stream, the shape a hook is really handed."""

import io
import json

import pytest

from guppi import grepguard


@pytest.fixture
def project(tmp_path):
    decisions = tmp_path / "vault" / "wiki" / "decisions"
    decisions.mkdir(parents=True)
    (decisions / "decision-case-1.md").write_text("---\ntype: decision\n---\n", encoding="utf-8")
    (tmp_path / "vault" / "wiki" / "rules").mkdir()
    (tmp_path / "vault" / "wiki" / "brief.md").write_text("# Brief\n", encoding="utf-8")
    (tmp_path / "guppi").mkdir()
    return tmp_path


def run(project, tool_input, tool="Grep", **fields):
    payload = {
        "session_id": "s",
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": tool_input,
        "cwd": str(project),
        **fields,
    }
    out, err = io.StringIO(), io.StringIO()
    stdin = io.StringIO(json.dumps(payload))
    code = grepguard.run([], stdin=stdin, stdout=out, stderr=err, project_dir=project)
    return code, out.getvalue(), err.getvalue()


def changed(out):
    data = json.loads(out)["hookSpecificOutput"]
    assert data["hookEventName"] == "PreToolUse"
    assert "permissionDecision" not in data  # the call runs as changed, nothing is asked
    return data["updatedInput"]


def test_a_grep_over_the_wiki_gets_the_exclusion_as_its_glob(project):
    code, out, _ = run(project, {"pattern": "x", "path": str(project / "vault" / "wiki")})
    assert code == 0
    assert changed(out) == {
        "pattern": "x",
        "path": str(project / "vault" / "wiki"),
        "glob": "!**/decisions/**",
    }


def test_a_grep_with_no_path_searches_the_working_directory(project):
    code, out, _ = run(project, {"pattern": "x"})
    assert code == 0 and changed(out)["glob"] == "!**/decisions/**"


def test_a_relative_path_is_read_from_the_working_directory(project):
    _, out, _ = run(project, {"pattern": "x", "path": "vault"})
    assert changed(out)["glob"] == "!**/decisions/**"


def test_another_filter_gets_the_exclusion_after_a_space(project):
    _, out, _ = run(project, {"pattern": "x", "path": str(project), "glob": "*.md"})
    assert changed(out)["glob"] == "*.md !**/decisions/**"


def test_a_glob_that_ends_with_the_exclusion_is_not_changed(project):
    code, out, err = run(project, {"pattern": "x", "glob": "*.md !**/decisions/**"})
    assert (code, out, err) == (0, "", "")


def test_the_exclusion_first_is_put_again_at_the_end(project):
    _, out, _ = run(project, {"pattern": "x", "glob": "!**/decisions/** *.md"})
    assert changed(out)["glob"] == "!**/decisions/** *.md !**/decisions/**"


def test_a_call_of_the_librarian_is_changed_the_same_way(project):
    _, out, _ = run(project, {"pattern": "x"}, agent_type="librarian-guppi")
    assert changed(out)["glob"] == "!**/decisions/**"


@pytest.mark.parametrize(
    "where",
    [
        ("vault", "wiki", "decisions"),  # the folder itself: a search for a reason of the frame
        ("vault", "wiki", "decisions", "decision-case-1.md"),  # a file inside it
        ("vault", "wiki", "brief.md"),  # one file
        ("guppi",),  # a folder that does not hold the Decision pages
        ("vault", "wiki", "rules"),
    ],
)
def test_a_grep_that_does_not_cover_the_decision_pages_passes_unchanged(project, where):
    code, out, err = run(project, {"pattern": "x", "path": str(project.joinpath(*where))})
    assert (code, out, err) == (0, "", "")


def test_another_tool_passes_unchanged(project):
    assert run(project, {"file_path": str(project)}, tool="Read") == (0, "", "")


def test_a_payload_it_cannot_read_passes_unchanged(project):
    out, err = io.StringIO(), io.StringIO()
    stdin = io.StringIO("not json")
    assert grepguard.run([], stdin=stdin, stdout=out, stderr=err, project_dir=project) == 0
    assert out.getvalue() == ""


def test_an_error_lets_the_call_pass_with_one_line(project, monkeypatch):
    def broken(*_):
        raise OSError("disk")

    monkeypatch.setattr(grepguard, "searched_folder", broken)
    code, out, err = run(project, {"pattern": "x"})
    assert (code, out) == (0, "") and err.startswith("grepguard: passed unchanged: disk")
