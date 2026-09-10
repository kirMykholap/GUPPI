"""`guppi gate`: `/handoff` through the Skill tool is refused while the tree is dirty."""

import io
import json
import subprocess

from guppi import gate


def payload(**fields):
    return io.StringIO(json.dumps(fields))


def run(stdin, project_dir, status=None):
    err = io.StringIO()
    code = gate.run([], stdin=stdin, stderr=err, project_dir=project_dir, status=status)
    return code, err.getvalue()


def test_handoff_on_a_dirty_tree_is_refused_with_the_reason(tmp_path):
    code, err = run(
        payload(tool_name="Skill", tool_input={"skill": "handoff"}),
        tmp_path,
        status=" M a.py\n?? b.py",
    )
    assert code == 2 and "commit first" in err and "2 path(s)" in err


def test_handoff_on_a_clean_tree_passes(tmp_path):
    code, err = run(
        payload(tool_name="Skill", tool_input={"skill": "handoff"}), tmp_path, status=""
    )
    assert (code, err) == (0, "")


def test_another_skill_or_tool_passes_whatever_the_tree(tmp_path):
    assert run(
        payload(tool_name="Skill", tool_input={"skill": "retro"}), tmp_path, status=" M a.py"
    ) == (0, "")
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
    code, err = run(payload(tool_name="Skill", tool_input={"skill": "handoff"}), tmp_path)
    assert code == 2 and "1 path(s)" in err


def test_cli_dispatches_to_gate(tmp_path, monkeypatch, capsys):
    from guppi import cli

    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", payload(tool_name="Skill", tool_input={"skill": "retro"}))
    assert cli.main(["gate"]) == 0
