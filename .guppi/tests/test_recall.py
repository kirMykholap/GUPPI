"""`guppi recall`: after a compaction of a working session the hook prints the session's
folder, the paths of the files `/hi` imports, the Frontier and the Spec, and the Frontier's
text; an ordinary session and another source get nothing (case 287)."""

import io
import json
from datetime import UTC, datetime

from guppi import recall

NOW = datetime(2026, 9, 21, 11, 0, 0, tzinfo=UTC)
SESSION = "bf4dd2b3-5302-4ac5-b15a-8d01bb9cdff4"
STAMP = "bf4dd2b3"
START = f"- 10:29:02 {STAMP} session-start startup\n"
HI = f"- 10:29:12 {STAMP} hi\n"
SKILL = (
    "---\nname: hi\n---\n<!-- rule-internal-context -->\n@vault/wiki/sprint.md\n"
    "@vault/wiki/brief.md\n@vault/wiki/case-schema.md\n<!-- /rule-internal-context -->\n"
    "Assemble the Frontier.\n"
)
FRONTIER = "# Frontier\n\n## Cases\n\n- [ ] C1 — a thing · brief\n"


def payload(source="compact", session=SESSION):
    return io.StringIO(json.dumps({"session_id": session, "source": source}))


def run(project_dir, stdin=None):
    out = io.StringIO()
    code = recall.run([], stdin=stdin or payload(), stdout=out, project_dir=project_dir, now=NOW)
    return code, out.getvalue()


def with_event_log(project_dir, text):
    folder = project_dir / "vault" / "raw" / "2026-09-21"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "event_log.md").write_text(text, encoding="utf-8", newline="\n")


def with_skill(project_dir, text=SKILL):
    path = project_dir / ".claude" / "skills" / "hi" / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def session_folder(project_dir):
    folder = project_dir / "vault" / "raw" / "2026-09-21" / "1029"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def working_session(project_dir, frontier=True, spec=True):
    with_event_log(project_dir, START + HI)
    with_skill(project_dir)
    folder = session_folder(project_dir)
    if frontier:
        (folder / "frontier.md").write_text(FRONTIER, encoding="utf-8", newline="\n")
    if spec:
        (folder / "spec.md").write_text("# Spec\n", encoding="utf-8", newline="\n")
    return folder


def test_compact_with_a_hi_prints_the_header_the_paths_and_the_frontier(tmp_path):
    working_session(tmp_path)
    code, out = run(tmp_path)
    assert code == 0
    lines = out.splitlines()
    assert lines[0] == (
        "recall: the context was compacted at 11:00:00; the session is raw/2026-09-21/1029/. "
        "Read before the next reply:"
    )
    assert lines[1:7] == [
        "vault/wiki/sprint.md",
        "vault/wiki/brief.md",
        "vault/wiki/case-schema.md",
        "vault/raw/2026-09-21/1029/frontier.md",
        "vault/raw/2026-09-21/1029/spec.md",
        "Frontier:",
    ]
    assert "\n".join(lines[7:]) + "\n" == FRONTIER
    assert "# Spec" not in out  # the paths only, the Frontier apart


def test_a_fourth_import_line_of_the_skill_is_a_fourth_path(tmp_path):
    working_session(tmp_path)
    with_skill(
        tmp_path,
        SKILL.replace(
            "@vault/wiki/case-schema.md\n", "@vault/wiki/case-schema.md\n@vault/wiki/glossary.md\n"
        ),
    )
    _, out = run(tmp_path)
    lines = out.splitlines()
    assert lines[1:5] == [
        "vault/wiki/sprint.md",
        "vault/wiki/brief.md",
        "vault/wiki/case-schema.md",
        "vault/wiki/glossary.md",
    ]


def test_compact_without_a_hi_prints_nothing(tmp_path):
    with_event_log(tmp_path, START)  # an ordinary session: started, no /hi
    with_skill(tmp_path)
    code, out = run(tmp_path)
    assert code == 0 and out == ""


def test_another_source_prints_nothing(tmp_path):
    working_session(tmp_path)
    for source in ("startup", "resume", "clear", "fork", ""):
        code, out = run(tmp_path, payload(source=source))
        assert (code, out) == (0, ""), source


def test_no_frontier_and_no_spec_leave_their_lines_out(tmp_path):
    working_session(tmp_path, frontier=False, spec=False)
    code, out = run(tmp_path)
    assert code == 0
    lines = out.splitlines()
    assert lines[1:] == ["vault/wiki/sprint.md", "vault/wiki/brief.md", "vault/wiki/case-schema.md"]
    assert "Frontier:" not in out


def test_the_spec_is_the_plan_file_before_the_approval_and_spec_md_after(tmp_path):
    folder = working_session(tmp_path, spec=False)
    plan = tmp_path / ".claude" / "plans" / "quiet-plan.md"
    plan.parent.mkdir(parents=True)
    plan.write_text("# Spec — draft\n", encoding="utf-8", newline="\n")
    with_event_log(tmp_path, START + HI + f"- 10:35:00 {STAMP} tool Write: {plan}\n")
    _, out = run(tmp_path)
    assert ".claude/plans/quiet-plan.md" in out.splitlines()[5]
    (folder / "spec.md").write_text("# Spec\n", encoding="utf-8", newline="\n")
    _, out = run(tmp_path)
    assert out.splitlines()[5] == "vault/raw/2026-09-21/1029/spec.md"
    assert "quiet-plan" not in out


def test_a_payload_that_is_not_json_prints_nothing_and_exits_0(tmp_path):
    working_session(tmp_path)
    code, out = run(tmp_path, io.StringIO("not json"))
    assert code == 0 and out == ""
