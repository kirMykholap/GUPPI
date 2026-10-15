"""`guppi shellwrite`: the `PostToolUse` hook on `Bash` and `PowerShell` that repairs CRLF line
endings and a UTF-8 byte-order mark in the changed and new files of the repository and names
each file it repaired, and names without a change a file in UTF-16 or not valid UTF-8 (case
710.1). Rule page: `vault/wiki/rules/rule-shell-write-check.md`.
`estimate-shell-write-check-repairs-and-reports`

Every test feeds the payload through a stream, the shape a hook is really handed, in a
temporary git repository.
"""

import io
import json
import subprocess

import pytest

from guppi import cli, shellwrite


def git(project, *args):
    subprocess.run(["git", *args], cwd=project, check=True, capture_output=True)


@pytest.fixture
def repo(tmp_path):
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.email", "t@example.com")
    git(tmp_path, "config", "user.name", "t")
    git(tmp_path, "config", "core.autocrlf", "false")
    (tmp_path / ".gitignore").write_text("ignored.md\n", encoding="utf-8")
    (tmp_path / "kept.md").write_bytes(b"one\ntwo\n")
    (tmp_path / "clean.md").write_bytes(b"clean\n")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-q", "-m", "seed")
    return tmp_path


def run(project, tool="Bash", raw=None):
    stdin = io.StringIO(raw if raw is not None else json.dumps({"tool_name": tool}))
    out, err = io.StringIO(), io.StringIO()
    code = shellwrite.run([], stdin=stdin, stdout=out, stderr=err, project_dir=project)
    return code, out.getvalue(), err.getvalue()


def context(out):
    data = json.loads(out)
    assert data["hookSpecificOutput"]["hookEventName"] == "PostToolUse"
    return data["hookSpecificOutput"]["additionalContext"].splitlines()


@pytest.mark.parametrize("tool", ["Bash", "PowerShell"])
def test_a_changed_file_with_crlf_and_a_new_file_with_a_mark_are_repaired_and_named(repo, tool):
    (repo / "kept.md").write_bytes(b"one\r\ntwo\r\nthree\r\n")
    (repo / "new.md").write_bytes(shellwrite.UTF8_MARK + "тире — x\n".encode())
    code, out, err = run(repo, tool)
    assert (code, err) == (0, "")
    assert (repo / "kept.md").read_bytes() == b"one\ntwo\nthree\n"
    assert (repo / "new.md").read_bytes() == "тире — x\n".encode()
    lines = context(out)
    assert len(lines) == 2
    kept = next(line for line in lines if "kept.md" in line)
    new = next(line for line in lines if "new.md" in line)
    assert "CRLF line endings into LF" in kept and "Edit or Write" in kept
    assert "byte-order mark" in new and "check its characters" in new


def test_a_utf16_file_and_one_not_valid_utf8_are_named_and_unchanged(repo):
    utf16 = "текст\r\n".encode("utf-16")
    latin = "caf\xe9\r\n".encode("latin-1")
    (repo / "wide.md").write_bytes(utf16)
    (repo / "latin.md").write_bytes(latin)
    code, out, _ = run(repo, "PowerShell")
    assert code == 0
    assert (repo / "wide.md").read_bytes() == utf16
    assert (repo / "latin.md").read_bytes() == latin
    lines = context(out)
    assert any("wide.md" in line and "UTF-16" in line and "Write" in line for line in lines)
    assert any("latin.md" in line and "not valid UTF-8" in line for line in lines)


def test_an_ignored_a_binary_and_a_clean_file_are_not_touched_and_give_no_output(repo):
    (repo / "ignored.md").write_bytes(b"x\r\n")
    (repo / "blob.bin").write_bytes(b"\x00\x01\r\n")
    (repo / "fresh.md").write_bytes(b"sound\n")
    assert run(repo) == (0, "", "")
    assert (repo / "ignored.md").read_bytes() == b"x\r\n"
    assert (repo / "blob.bin").read_bytes() == b"\x00\x01\r\n"


def test_a_faulty_file_is_named_again_at_the_next_call(repo):
    (repo / "latin.md").write_bytes("caf\xe9\n".encode("latin-1"))
    assert "latin.md" in run(repo)[1]
    assert "latin.md" in run(repo)[1]


def test_a_deleted_file_is_skipped(repo):
    (repo / "kept.md").unlink()
    assert run(repo) == (0, "", "")


def test_another_tool_passes(repo):
    (repo / "kept.md").write_bytes(b"one\r\n")
    assert run(repo, "Write") == (0, "", "")
    assert (repo / "kept.md").read_bytes() == b"one\r\n"


@pytest.mark.parametrize("raw", ["", "not json", "[1]"])
def test_an_unreadable_payload_gives_exit_0_and_one_line(repo, raw):
    code, out, err = run(repo, raw=raw)
    assert (code, out) == (0, "")
    assert err == "shellwrite: payload not readable, nothing checked\n"


def test_a_failed_git_gives_exit_0_and_one_line(tmp_path):
    code, out, err = run(tmp_path / "missing")
    assert (code, out) == (0, "")
    assert err.startswith("shellwrite: files not checked:") and err.count("\n") == 1


def test_cli_dispatches_to_shellwrite():
    assert cli.COMMANDS["shellwrite"] is shellwrite.run
