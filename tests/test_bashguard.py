"""`guppi bashguard`: the `PreToolUse Bash` hook refuses a heredoc whose body carries a
backslash, or one that writes a file, and names Write and Edit (case 127). Rule page:
`vault/wiki/rules/rule-bash-guard.md`."""

import io
import json
from datetime import UTC, datetime

import pytest

from guppi import bashguard

NOW = datetime(2026, 9, 14, 12, 0, 0, tzinfo=UTC)

BACKSLASH_BODY = "python - <<'EOF'\nprint('a\\nb')\nEOF"
CLEAN_PIPE = "python - <<'EOF' | head -3\nprint(1)\nEOF"
CLEAN_SCREEN = "cat <<EOF\nhello\nEOF"
FILE_WRITE = "cat > out.txt <<EOF\nhello\nEOF"
APPEND_WRITE = "cat >> C:/x/plan.md <<'EOF'\n## Case\nEOF"
TEE_WRITE = "cat <<EOF | tee notes.md\nhello\nEOF"
DASH_MARKER = "cat <<-EOF\n\thello\n\tEOF\necho done"
NULL_ONLY = "python - <<'EOF' 2>/dev/null\nprint(1)\nEOF"
HERE_STRING = "grep x <<< 'a\\tb'"
NO_HEREDOC = "printf '%s\\n' a b > out.txt"


def payload(**fields):
    return io.StringIO(json.dumps(fields))


def bash(command, session="19037d1c-5d15"):
    return payload(session_id=session, tool_name="Bash", tool_input={"command": command})


def run(stdin, project_dir):
    err = io.StringIO()
    code = bashguard.run([], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def log(project_dir):
    path = project_dir / "vault" / "raw" / "2026-09-14" / "event_log.md"
    return path.read_text(encoding="utf-8") if path.exists() else ""


# --- the refusals ---------------------------------------------------------------------------


def test_a_backslash_in_the_body_is_refused_and_names_write(tmp_path):
    code, err = run(bash(BACKSLASH_BODY), tmp_path)
    assert code == 2
    assert "bashguard: heredoc refused — a backslash in its body." in err
    assert "Write tool" in err and "Edit" in err
    # case 384: the refusal says it is by design, so it is no finding for Retro
    assert (
        "The refusal is this guard working as designed, not an event of the session: "
        "do not report it at Retro." in err
    )


def test_a_heredoc_that_writes_a_file_is_refused_with_the_path(tmp_path):
    code, err = run(bash(FILE_WRITE), tmp_path)
    assert code == 2 and "it writes out.txt" in err
    code, err = run(bash(APPEND_WRITE), tmp_path)
    assert code == 2 and "it writes C:/x/plan.md" in err
    code, err = run(bash(TEE_WRITE), tmp_path)
    assert code == 2 and "it writes notes.md" in err


def test_the_refusal_is_logged_before_it_is_said(tmp_path):
    run(bash(BACKSLASH_BODY), tmp_path)
    assert log(tmp_path) == "- 12:00:00 19037d1c bashguard refused: a backslash in its body\n"


# --- what passes ----------------------------------------------------------------------------


@pytest.mark.parametrize(
    "command", [CLEAN_PIPE, CLEAN_SCREEN, DASH_MARKER, NULL_ONLY, HERE_STRING, NO_HEREDOC]
)
def test_a_clean_heredoc_a_here_string_or_no_heredoc_passes(tmp_path, command):
    assert run(bash(command), tmp_path) == (0, "")
    assert log(tmp_path) == ""


def test_another_tool_passes(tmp_path):
    stdin = payload(tool_name="Write", tool_input={"file_path": "x.py", "content": "a\\nb"})
    assert run(stdin, tmp_path) == (0, "")


def test_an_unreadable_payload_passes_with_a_line_on_stderr(tmp_path):
    code, err = run(io.StringIO("not json"), tmp_path)
    assert code == 0 and "check skipped" in err


# --- the parser -------------------------------------------------------------------------------


def test_heredocs_finds_every_marker_quoted_or_not_with_its_body():
    command = "a <<X\n1\nX\nb <<-'Y' && c <<\"Z\"\n\t2\n\tY\n3\nZ"
    assert bashguard.heredocs(command) == [
        ("a <<X", "1"),
        ("b <<-'Y' && c <<\"Z\"", "\t2"),
        ("b <<-'Y' && c <<\"Z\"", "3"),
    ]


def test_an_unclosed_heredoc_runs_to_the_end():
    assert bashguard.heredocs("cat <<EOF\na\nb") == [("cat <<EOF", "a\nb")]


def test_file_write_ignores_dev_null_and_descriptor_redirects():
    assert bashguard.file_write("python - <<'EOF' 2>/dev/null 2>&1") is None
    assert bashguard.file_write("python - <<'EOF' > /dev/null") is None
    assert bashguard.file_write("python - <<'EOF' >> log.txt") == "log.txt"


def test_cli_dispatches_to_bashguard(tmp_path, monkeypatch):
    from guppi import cli

    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", bash(BACKSLASH_BODY))
    assert cli.main(["bashguard"]) == 2
