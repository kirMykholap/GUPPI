"""`guppi links`: the graph of the links between the vault pages and the harness files
(case 967.1, `estimate-link-graph-prints-the-neighbours`; case 967.3,
`estimate-link-graph-at-session-start-writes-the-file`). Entity page:
`vault/wiki/entities/entity-link-graph.md`; Rule page of the hook:
`vault/wiki/rules/rule-link-graph-at-session-start.md`.

The tests build a small vault in a temporary folder; nothing here reads the repository's
own pages."""

import io

import pytest
import yaml

from guppi import links

AGENT = """<!-- rule-agent -->
---
name: a-guppi
skills: [s-two]
---
Run `uv run --project .guppi guppi links` and the skill /s-one.
<!-- /rule-agent -->"""

SKILL = """<!-- rule-skill-one -->
The main agent hands each question to a-guppi; `s-two` sets its shape.
<!-- /rule-skill-one -->"""

SKILL_TWO = """<!-- rule-skill-two -->
Ask one question at a time.
<!-- /rule-skill-two -->"""


def page(project, category, slug, props, sections=None):
    folder = project / "vault" / "wiki" / category
    folder.mkdir(parents=True, exist_ok=True)
    body = "".join(f"\n## {name}\n\n{text}\n" for name, text in (sections or {}).items())
    text = "---\n" + yaml.safe_dump(props, sort_keys=False) + "---\n" + body
    (folder / f"{slug}.md").write_text(text, encoding="utf-8")


def render_rule(project, slug, governs, text, **props):
    page(
        project,
        "rules",
        slug,
        {
            "type": "rule",
            "status": "draft",
            "purpose": f"the rule {slug}",
            "enforcement": "render",
            "governs": governs,
            "render_mode": "full",
            **props,
        },
        {"Render": text},
    )


@pytest.fixture
def project(tmp_path):
    render_rule(tmp_path, "rule-agent", ".claude/agents/a-guppi.md", AGENT)
    render_rule(tmp_path, "rule-skill-one", ".claude/skills/s-one/SKILL.md", SKILL)
    render_rule(tmp_path, "rule-skill-two", ".claude/skills/s-two/SKILL.md", SKILL_TWO)
    page(
        tmp_path,
        "rules",
        "rule-graph",
        {
            "type": "rule",
            "status": "draft",
            "purpose": "the rule of the graph",
            "enforcement": "hook",
            "implementation_ref": [".guppi/guppi/links.py"],
            "applies_to": ["[[entity-thing]]"],
            "deferred_by": ["[[decision-case-1]]"],
        },
        {
            "Purpose": "It rests on `rule-agent` and [[rule-skill-one]].",
            "History": "- 2026-10-31 — created by [[decision-case-1]]; it named `rule-skill-two`",
        },
    )
    page(
        tmp_path,
        "entities",
        "entity-thing",
        {"type": "entity", "status": "draft", "purpose": "the thing", "code_ref": [".claude/"]},
    )
    page(
        tmp_path,
        "estimates",
        "estimate-graph-works",
        {
            "type": "estimate",
            "status": "pending",
            "purpose": "the graph works",
            "target": "[[rule-graph]]",
        },
    )
    page(tmp_path, "lessons", "lesson-x", {"type": "lesson", "root_cause": "the cause of x"})
    page(tmp_path, "insights", "insight-y", {"type": "insight", "pattern": "the pattern of y"})
    page(
        tmp_path,
        "decisions",
        "decision-case-1",
        {"type": "decision", "status": "current", "purpose": "a decision"},
        {"Problem": "It names `rule-graph`, `lesson-x` and `insight-y`."},
    )
    return tmp_path


def run(project, *argv):
    out, err = io.StringIO(), io.StringIO()
    code = links.run(list(argv), stdout=out, stderr=err, project_dir=project)
    return code, out.getvalue(), err.getvalue()


def lines(project, name):
    code, out, err = run(project, name)
    assert (code, err) == (0, "")
    return out.splitlines()


def test_a_block_opens_with_its_heading_and_purpose_line(project):
    out = lines(project, "rule-graph")
    assert out[:3] == ["## rule-graph", "", "the rule of the graph"]


def test_a_page_links_out_by_its_fields_its_wikilinks_and_its_path_fields(project):
    out = lines(project, "rule-graph")
    assert "- out applies_to: entity-thing — the thing" in out
    assert "- out body: rule-skill-one — the rule rule-skill-one" in out
    assert "- out implementation_ref: .guppi/guppi/links.py" in out


def test_a_page_links_out_by_a_slug_its_body_names_outside_history(project):
    out = lines(project, "rule-graph")
    assert "- out name: rule-agent — the rule rule-agent" in out
    assert not [line for line in out if "rule-skill-two" in line]  # named only in History


def test_each_link_out_is_a_link_in_of_the_other(project):
    assert "- in target: estimate-graph-works — the graph works" in lines(project, "rule-graph")
    assert "- in applies_to: rule-graph — the rule of the graph" in lines(project, "entity-thing")


def test_a_rendered_file_links_out_by_the_names_of_agents_skills_and_commands(project):
    out = lines(project, ".claude/skills/s-one/SKILL.md")
    assert "- out agent a-guppi: rule-agent — the rule rule-agent" in out
    assert "- out skill s-two: rule-skill-two — the rule rule-skill-two" in out
    agent = lines(project, ".claude/agents/a-guppi.md")
    assert "- out skill s-two: rule-skill-two — the rule rule-skill-two" in agent  # skills: list
    assert "- out skill s-one: rule-skill-one — the rule rule-skill-one" in agent  # after a slash
    assert "- out command links: rule-graph — the rule of the graph" in agent


def test_a_rendered_file_is_read_as_the_render_writes_it_not_from_disk(project):
    assert not (project / ".claude" / "agents" / "a-guppi.md").exists()
    assert "- in governs: rule-agent — the rule rule-agent" in lines(
        project, ".claude/agents/a-guppi.md"
    )


def test_a_file_inside_a_folder_a_page_names_links_into_that_page(project):
    out = lines(project, ".claude/skills/s-two/SKILL.md")
    assert "- in code_ref: entity-thing — the thing" in out


def test_the_purpose_line_of_a_lesson_and_an_insight(project):
    page(
        project,
        "rules",
        "rule-z",
        {"type": "rule", "purpose": "z"},
        {"Purpose": "See `lesson-x` and `insight-y`."},
    )
    assert lines(project, "lesson-x")[2] == "the cause of x"
    assert "- out name: insight-y — the pattern of y" in lines(project, "rule-z")


def test_no_decision_page_is_read_or_printed(project):
    for name in ("rule-graph", "lesson-x", "insight-y"):
        assert not [line for line in lines(project, name) if "decision-case-1" in line]
    code, out, _ = run(project, "decision-case-1")
    assert code == 1 and "neither a live page nor a file" in out
    code, out, _ = run(project, "vault/wiki/decisions/decision-case-1.md")
    assert code == 1 and "neither a live page nor a file" in out


def test_an_unknown_slug_or_path_prints_one_line_and_exits_non_zero(project):
    code, out, err = run(project, "rule-nothing")
    assert (code, out, err) == (1, "links: rule-nothing is neither a live page nor a file\n", "")


def test_write_puts_every_block_into_the_graph_file(project):
    assert run(project, "--write") == (0, "", "")
    text = (project / ".guppi" / "links.md").read_text(encoding="utf-8")
    for name in (
        "rule-graph",
        "entity-thing",
        "lesson-x",
        ".claude/agents/a-guppi.md",
        ".guppi/guppi/links.py",
    ):
        assert f"\n## {name}\n" in text
    assert "".join(lines(project, "rule-graph")) in text.replace("\n", "")
    assert "decision-case-1" not in text


def test_git_ignores_the_graph_file():
    gitignore = links.Path(__file__).resolve().parents[1] / ".gitignore"
    assert links.OUTPUT.name in gitignore.read_text(encoding="utf-8").splitlines()


def test_write_prints_one_line_and_exits_zero_on_an_error(project):
    (project / "vault" / "wiki" / "rules" / "rule-agent.md").write_text(
        "---\nenforcement: render\ngoverns: x.md\nrender_mode: full\n---\n## Render\n\nno markers\n",
        encoding="utf-8",
    )
    code, out, err = run(project, "--write")
    assert (code, out) == (0, "")
    assert err.startswith("links: .guppi/links.md not written:") and err.count("\n") == 1
    assert not (project / ".guppi" / "links.md").exists()
