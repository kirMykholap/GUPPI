"""`guppi pageread`: the `PreToolUse Read` hook reads a vault page without its `## History`,
and `--after` says where the History starts (case 420.1). Rule page:
`vault/wiki/rules/rule-page-read.md`."""

import io
import json

from guppi import pageread
from guppi.pages import history_line

PAGE = """---
type: rule
purpose: A page
---

## Purpose

Body line.

## History

- 2026-09-25 created
- 2026-09-25 updated
"""

RENDER_PAGE = """---
type: rule
---

## Render

<!-- rule-x -->
# Brief

## History

a heading of the rendered file, inside the block
<!-- /rule-x -->

## History

- 2026-09-25 created
"""


def write(root, relative, text):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def call(project_dir, tool_input, after=False, tool="Read"):
    out, err = io.StringIO(), io.StringIO()
    stdin = io.StringIO(json.dumps({"tool_name": tool, "tool_input": tool_input}))
    argv = ["--after"] if after else []
    code = pageread.run(argv, stdin=stdin, stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue(), err.getvalue()


def test_history_line_is_the_page_heading(tmp_path):
    assert history_line(PAGE) == 10
    assert history_line("---\ntype: x\n---\n\n## Purpose\n\ntext\n") is None


def test_history_line_skips_a_heading_inside_a_render_block():
    assert history_line(RENDER_PAGE) == 15


def test_a_page_is_cut_before_its_history(tmp_path):
    path = write(tmp_path, "vault/wiki/rules/rule-x.md", PAGE)
    code, out, _ = call(tmp_path, {"file_path": str(path)})
    assert code == 0
    output = json.loads(out)["hookSpecificOutput"]
    assert output["hookEventName"] == "PreToolUse"
    assert output["updatedInput"] == {"file_path": str(path), "limit": 9}
    assert "permissionDecision" not in output


def test_a_heading_inside_a_render_block_is_not_the_cut(tmp_path):
    path = write(tmp_path, "vault/wiki/rules/rule-x.md", RENDER_PAGE)
    _, out, _ = call(tmp_path, {"file_path": str(path)})
    assert json.loads(out)["hookSpecificOutput"]["updatedInput"]["limit"] == 14


def test_a_call_with_its_own_offset_or_limit_passes(tmp_path):
    path = write(tmp_path, "vault/wiki/rules/rule-x.md", PAGE)
    assert call(tmp_path, {"file_path": str(path), "offset": 10})[1] == ""
    assert call(tmp_path, {"file_path": str(path), "limit": 40})[1] == ""


def test_a_hub_file_and_a_file_outside_the_wiki_pass(tmp_path):
    hub = write(tmp_path, "vault/wiki/brief.md", "# Brief\n\n## Deferred\n\nnone\n")
    outside = write(tmp_path, "vault/raw/2026-09-25/1228/spec.md", PAGE)
    code_file = write(tmp_path, "guppi/x.md", PAGE)
    for path in (hub, outside, code_file):
        assert call(tmp_path, {"file_path": str(path)}) == (0, "", "")


def test_another_tool_and_an_unreadable_payload_pass(tmp_path):
    path = write(tmp_path, "vault/wiki/rules/rule-x.md", PAGE)
    assert call(tmp_path, {"file_path": str(path)}, tool="Edit")[1] == ""
    out = io.StringIO()
    code = pageread.run([], stdin=io.StringIO("not json"), stdout=out, project_dir=tmp_path)
    assert (code, out.getvalue()) == (0, "")


def test_after_names_the_history_of_a_cut_read(tmp_path):
    path = write(tmp_path, "vault/wiki/rules/rule-x.md", PAGE)
    code, out, _ = call(tmp_path, {"file_path": str(path), "limit": 9}, after=True)
    assert code == 0
    output = json.loads(out)["hookSpecificOutput"]
    assert output["hookEventName"] == "PostToolUse"
    context = output["additionalContext"]
    assert "rules/rule-x.md" in context
    assert "lines 10–13" in context
    assert "offset 10" in context


def test_after_says_nothing_on_a_read_it_did_not_cut(tmp_path):
    path = write(tmp_path, "vault/wiki/rules/rule-x.md", PAGE)
    assert call(tmp_path, {"file_path": str(path), "offset": 10}, after=True)[1] == ""
    assert call(tmp_path, {"file_path": str(path), "limit": 40}, after=True)[1] == ""
    assert call(tmp_path, {"file_path": str(path)}, after=True)[1] == ""


def test_the_page_on_disk_is_not_changed(tmp_path):
    path = write(tmp_path, "vault/wiki/rules/rule-x.md", PAGE)
    call(tmp_path, {"file_path": str(path)})
    call(tmp_path, {"file_path": str(path), "limit": 9}, after=True)
    assert path.read_text(encoding="utf-8") == PAGE
