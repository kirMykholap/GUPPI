"""`guppi guard`: the `PreToolUse` hook that refuses `Edit`, `Write` and `MultiEdit` on a
file a Rule page governs. Rule page: `vault/wiki/rules/rule-governed-files-hook.md`.

Every test feeds the payload through a stream, the shape a hook is really handed; the
vault is a temp folder with one governing page per file.
"""

import io
import json

import pytest

from guppi import guard

GOVERNED = ".claude/skills/hi/SKILL.md"
RULE = "rule-skill-hi"


def page(vault, slug, governs=None, status="built", mode="full"):
    lines = [
        "---",
        "type: rule",
        "kind: Leaf",
        "purpose: Prevents something",
        f"status: {status}",
        f"enforcement: {'render' if governs else 'hook'}",
    ]
    if governs:
        lines += [f"governs: {governs}", f"render_mode: {mode}"]
    lines += ["---", "", "## Purpose", "", "Something.", ""]
    folder = vault / "vault" / "wiki" / "rules"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def vault(tmp_path):
    page(tmp_path, RULE, GOVERNED)
    page(tmp_path, "rule-git-context", GOVERNED, mode="partial")  # sorts before the owner
    page(tmp_path, "rule-registry", ".claude/settings.json")
    page(tmp_path, "rule-hook")
    return tmp_path


def payload(tool="Edit", file_path=GOVERNED):
    fields = {
        "session_id": "44c1aae1-4076-4a58-a7c0-d20bc274047c",
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": {"file_path": file_path, "old_string": "a", "new_string": "b"},
    }
    return io.StringIO(json.dumps(fields))


def run(stdin, project_dir):
    err = io.StringIO()
    code = guard.run([], stdin=stdin, stderr=err, project_dir=project_dir)
    return code, err.getvalue()


@pytest.mark.parametrize("tool", ["Edit", "Write", "MultiEdit"])
def test_an_edit_tool_on_a_governed_path_is_refused_naming_rule_and_file(tmp_path, tool):
    vault(tmp_path)
    code, err = run(payload(tool=tool), tmp_path)
    assert code == 2
    assert RULE in err and GOVERNED in err
    assert "through a decision" in err


def test_the_full_page_is_named_over_a_partial_on_the_same_file(tmp_path):
    vault(tmp_path)
    _code, err = run(payload(), tmp_path)
    assert RULE in err and "rule-git-context" not in err


def test_a_partial_alone_is_named_when_no_full_page_owns_the_file(tmp_path):
    page(tmp_path, "rule-case-protocol", "CLAUDE.md", mode="partial")
    code, err = run(payload(file_path="CLAUDE.md"), tmp_path)
    assert code == 2
    assert "rule-case-protocol" in err and "CLAUDE.md" in err


def test_a_payload_with_a_utf8_bom_is_still_read(tmp_path):
    vault(tmp_path)
    stream = io.BytesIO(b"\xef\xbb\xbf" + payload().getvalue().encode("utf-8"))
    code, err = run(io.TextIOWrapper(stream, encoding="utf-8"), tmp_path)
    assert code == 2
    assert RULE in err


def test_an_absolute_path_to_a_governed_file_is_recognized(tmp_path):
    vault(tmp_path)
    absolute = str(tmp_path / ".claude" / "skills" / "hi" / "SKILL.md")  # backslashes on Windows
    code, err = run(payload(file_path=absolute), tmp_path)
    assert code == 2
    assert RULE in err and "SKILL.md" in err


def test_an_absolute_path_with_forward_slashes_is_recognized(tmp_path):
    vault(tmp_path)
    absolute = (tmp_path / ".claude" / "skills" / "hi" / "SKILL.md").as_posix()
    code, err = run(payload(file_path=absolute), tmp_path)
    assert code == 2
    assert RULE in err


def test_the_second_governed_file_names_its_own_rule(tmp_path):
    vault(tmp_path)
    code, err = run(payload(tool="Write", file_path=".claude/settings.json"), tmp_path)
    assert code == 2
    assert "rule-registry" in err and RULE not in err


def test_another_tool_passes(tmp_path):
    vault(tmp_path)
    assert run(payload(tool="Bash"), tmp_path) == (0, "")


def test_an_ungoverned_path_passes(tmp_path):
    vault(tmp_path)
    assert run(payload(file_path="guppi/render.py"), tmp_path) == (0, "")
    assert run(payload(file_path=str(tmp_path / "vault" / "wiki" / "brief.md")), tmp_path) == (
        0,
        "",
    )


def test_a_path_outside_the_project_passes(tmp_path):
    vault(tmp_path)
    outside = str(tmp_path.parent / "elsewhere" / "SKILL.md")
    assert run(payload(file_path=outside), tmp_path) == (0, "")


def test_an_archived_rule_page_governs_nothing(tmp_path):
    page(tmp_path, RULE, GOVERNED, status="archived")
    assert run(payload(), tmp_path) == (0, "")


def test_no_vault_passes(tmp_path):
    assert run(payload(), tmp_path) == (0, "")


def test_garbage_on_stdin_passes_with_one_line_on_stderr(tmp_path):
    vault(tmp_path)
    code, err = run(io.StringIO("not json"), tmp_path)
    assert code == 0
    assert err.startswith("guard:") and err.count("\n") == 1


def test_a_payload_without_file_path_passes(tmp_path):
    vault(tmp_path)
    fields = {"hook_event_name": "PreToolUse", "tool_name": "Edit", "tool_input": {}}
    assert run(io.StringIO(json.dumps(fields)), tmp_path) == (0, "")


def test_cli_dispatches_to_guard(tmp_path, monkeypatch, capsys):
    from guppi import cli

    vault(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", payload())
    assert cli.main(["guard"]) == 2
    assert RULE in capsys.readouterr().err
