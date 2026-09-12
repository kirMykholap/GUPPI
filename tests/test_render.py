"""`guppi render`: every `enforcement: render` Rule page written into the file it governs.

Rule page: `vault/wiki/rules/rule-render-harness.md`. The tests build a small vault in a
temp folder; nothing here touches the repository's own pages.
"""

import io
import json

import pytest

from guppi import render

FRAME = """<!-- rule-frame -->
---
name: frame
---
Recorded: yes

<!-- rule-one -->
<!-- rule-two -->

Tail line.
<!-- /rule-frame -->"""

ONE = """<!-- rule-one -->
@one
<!-- /rule-one -->"""

TWO = """<!-- rule-two -->
Two: !`echo two`
<!-- /rule-two -->"""

EXPECTED_FULL = """---
name: frame
---
Recorded: yes

<!-- rule-one -->
@one
<!-- /rule-one -->

<!-- rule-two -->
Two: !`echo two`
<!-- /rule-two -->

Tail line.
"""


def page(vault, slug, props, render_text=None, category="rules"):
    lines = ["---"]
    for key, value in props.items():
        if isinstance(value, list):
            value = "[" + ", ".join(value) + "]"
        lines.append(f"{key}: {value}")
    lines += ["---", "", "## Purpose", "", "Something.", ""]
    if render_text is not None:
        lines += ["## Render", "", render_text, ""]
    lines += ["## Estimates", "", "## History", ""]
    folder = vault / "vault" / "wiki" / category
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def rule(vault, slug, mode, governs, render_text, **extra):
    props = {
        "type": "rule",
        "kind": extra.pop("kind", "Leaf"),
        "purpose": "Prevents something",
        "status": "draft",
        "enforcement": "render",
        "governs": governs,
        "render_mode": mode,
    }
    props.update(extra)
    page(vault, slug, props, render_text)


def frame_vault(tmp_path):
    rule(
        tmp_path,
        "rule-frame",
        "full",
        "out/SKILL.md",
        FRAME,
        kind="MOC",
        children=["rule-one", "rule-two"],
    )
    rule(tmp_path, "rule-one", "partial", "out/SKILL.md", ONE, parent="rule-frame")
    rule(tmp_path, "rule-two", "partial", "out/SKILL.md", TWO, parent="rule-frame")
    return tmp_path


def run(argv, project_dir):
    out, err = io.StringIO(), io.StringIO()
    code = render.run(argv, stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue(), err.getvalue()


def test_full_frame_takes_its_children_in_order_and_drops_its_own_markers(tmp_path):
    frame_vault(tmp_path)
    code, _out, err = run([], tmp_path)
    assert (code, err) == (0, "")
    assert (tmp_path / "out" / "SKILL.md").read_text(encoding="utf-8") == EXPECTED_FULL


def test_partial_splices_between_the_markers_of_an_existing_file(tmp_path):
    rule(tmp_path, "rule-one", "partial", "CLAUDE.md", ONE, parent="rule-x")
    target = tmp_path / "CLAUDE.md"
    target.write_text(
        "# Title\n\n<!-- rule-one -->\nold text\n<!-- /rule-one -->\n\nAfter.\n",
        encoding="utf-8",
        newline="\n",
    )
    code, _out, err = run([], tmp_path)
    assert (code, err) == (0, "")
    assert target.read_text(encoding="utf-8") == (
        "# Title\n\n<!-- rule-one -->\n@one\n<!-- /rule-one -->\n\nAfter.\n"
    )


def test_partial_without_markers_in_its_target_writes_nothing(tmp_path):
    rule(tmp_path, "rule-one", "partial", "CLAUDE.md", ONE, parent="rule-x")
    target = tmp_path / "CLAUDE.md"
    target.write_text("# Title\n", encoding="utf-8", newline="\n")
    code, _out, err = run([], tmp_path)
    assert code == 1
    assert "rule-one" in err and "CLAUDE.md" in err
    assert target.read_text(encoding="utf-8") == "# Title\n"


def test_check_names_a_differing_file_and_writes_nothing(tmp_path):
    frame_vault(tmp_path)
    target = tmp_path / "out" / "SKILL.md"
    target.parent.mkdir()
    target.write_text("stale\n", encoding="utf-8", newline="\n")
    code, out, _err = run(["--check"], tmp_path)
    assert code == 1
    assert "out/SKILL.md" in out
    assert target.read_text(encoding="utf-8") == "stale\n"


def test_check_is_silent_on_an_identical_file(tmp_path):
    frame_vault(tmp_path)
    run([], tmp_path)
    code, out, err = run(["--check"], tmp_path)
    assert (code, out, err) == (0, "", "")


def test_full_json_body_is_the_whole_file(tmp_path):
    body = '<!-- rule-reg -->\n{\n  "hooks": {}\n}\n<!-- /rule-reg -->'
    rule(tmp_path, "rule-reg", "full", ".claude/settings.json", body, parent="rule-x")
    code, _out, err = run([], tmp_path)
    assert (code, err) == (0, "")
    text = (tmp_path / ".claude" / "settings.json").read_text(encoding="utf-8")
    assert text == '{\n  "hooks": {}\n}\n'
    assert json.loads(text) == {"hooks": {}}


def test_full_naming_a_child_that_does_not_render_writes_nothing(tmp_path):
    rule(
        tmp_path,
        "rule-frame",
        "full",
        "out/SKILL.md",
        FRAME,
        kind="MOC",
        children=["rule-one", "rule-two"],
    )
    rule(tmp_path, "rule-one", "partial", "out/SKILL.md", ONE, parent="rule-frame")
    page(
        tmp_path,
        "rule-two",
        {
            "type": "rule",
            "kind": "Leaf",
            "purpose": "x",
            "status": "draft",
            "enforcement": "hook",
            "parent": "rule-frame",
        },
    )
    code, _out, err = run([], tmp_path)
    assert code == 1
    assert "rule-two" in err
    assert not (tmp_path / "out" / "SKILL.md").exists()


def test_a_child_without_render_contributes_nothing_and_needs_no_marker(tmp_path):
    rule(
        tmp_path,
        "rule-frame",
        "full",
        "out/SKILL.md",
        FRAME.replace("<!-- rule-two -->\n", ""),
        kind="MOC",
        children=["rule-one", "rule-two"],
    )
    rule(tmp_path, "rule-one", "partial", "out/SKILL.md", ONE, parent="rule-frame")
    page(
        tmp_path,
        "rule-two",
        {
            "type": "rule",
            "kind": "Leaf",
            "purpose": "x",
            "status": "draft",
            "enforcement": "check",
            "parent": "rule-frame",
        },
    )
    code, _out, err = run([], tmp_path)
    assert (code, err) == (0, "")
    text = (tmp_path / "out" / "SKILL.md").read_text(encoding="utf-8")
    assert text == EXPECTED_FULL.replace(
        "<!-- rule-two -->\nTwo: !`echo two`\n<!-- /rule-two -->\n\n", ""
    )


def test_two_full_pages_on_one_file_write_nothing(tmp_path):
    rule(
        tmp_path,
        "rule-a",
        "full",
        "out/X.md",
        "<!-- rule-a -->\na\n<!-- /rule-a -->",
        parent="rule-x",
    )
    rule(
        tmp_path,
        "rule-b",
        "full",
        "out/X.md",
        "<!-- rule-b -->\nb\n<!-- /rule-b -->",
        parent="rule-x",
    )
    code, _out, err = run([], tmp_path)
    assert code == 1
    assert "out/X.md" in err
    assert not (tmp_path / "out" / "X.md").exists()


def test_render_section_without_its_own_markers_is_an_error(tmp_path):
    rule(tmp_path, "rule-a", "full", "out/X.md", "no markers here", parent="rule-x")
    code, _out, err = run([], tmp_path)
    assert code == 1
    assert "rule-a" in err


@pytest.mark.parametrize("argv", [["--check"], []])
def test_a_vault_with_no_render_pages_does_nothing(tmp_path, argv):
    page(
        tmp_path,
        "rule-hook",
        {"type": "rule", "kind": "Leaf", "purpose": "x", "status": "draft", "enforcement": "hook"},
    )
    assert run(argv, tmp_path) == (0, "", "")


def test_cli_dispatches_to_render(tmp_path, monkeypatch, capsys):
    from guppi import cli

    frame_vault(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["render", "--check"]) == 1
    assert "out/SKILL.md" in capsys.readouterr().out


def test_sync_prints_the_diff_of_a_differing_file_and_writes_it(tmp_path):
    frame_vault(tmp_path)
    target = tmp_path / "out" / "SKILL.md"
    target.parent.mkdir()
    target.write_text("stale\n", encoding="utf-8", newline="\n")
    code, out, err = run(["--sync"], tmp_path)
    assert (code, err) == (0, "")
    assert out.startswith("--- out/SKILL.md (file)\n+++ out/SKILL.md (rendered)\n")
    assert "-stale\n" in out and "+Recorded: yes\n" in out
    assert target.read_text(encoding="utf-8") == EXPECTED_FULL


def test_sync_prints_nothing_and_writes_nothing_for_an_identical_file(tmp_path):
    frame_vault(tmp_path)
    run([], tmp_path)
    target = tmp_path / "out" / "SKILL.md"
    before = target.stat().st_mtime_ns
    assert run(["--sync"], tmp_path) == (0, "", "")
    assert target.stat().st_mtime_ns == before


def test_sync_writes_a_missing_file_after_a_diff_against_nothing(tmp_path):
    frame_vault(tmp_path)
    code, out, err = run(["--sync"], tmp_path)
    assert (code, err) == (0, "")
    assert out.startswith("--- out/SKILL.md (file)\n+++ out/SKILL.md (rendered)\n")
    assert not any(line.startswith("-") and not line.startswith("---") for line in out.splitlines())
    assert (tmp_path / "out" / "SKILL.md").read_text(encoding="utf-8") == EXPECTED_FULL


def test_sync_on_a_render_error_reports_on_stderr_writes_nothing_and_exits_0(tmp_path):
    rule(
        tmp_path,
        "rule-a",
        "full",
        "out/X.md",
        "<!-- rule-a -->\na\n<!-- /rule-a -->",
        parent="rule-x",
    )
    rule(
        tmp_path,
        "rule-b",
        "full",
        "out/X.md",
        "<!-- rule-b -->\nb\n<!-- /rule-b -->",
        parent="rule-x",
    )
    code, out, err = run(["--sync"], tmp_path)
    assert (code, out) == (0, "")
    assert "out/X.md" in err
    assert not (tmp_path / "out" / "X.md").exists()


def test_sync_and_check_together_are_a_bad_invocation(tmp_path):
    frame_vault(tmp_path)
    code, _out, _err = run(["--sync", "--check"], tmp_path)
    assert code == 2
