"""`guppi ship` over a sample tree, `estimate-clean-branch-writes-a-clean-copy` (cases 804.6,
807.1): only the code, the harness and the pages with `core: true` are written, each bracket
that holds a pointer goes whole, a link to a page left out becomes its slug, samples stay,
the shipped values are written, a pointer outside a bracket exits 1, and `--review` and
`--check` work as the rule sets them."""

import io
from datetime import UTC, datetime
from pathlib import Path

from guppi import lint, ship
from guppi.pages import read_page

NOW = datetime(2026, 10, 13, 18, 0, tzinfo=UTC)
SCHEMA = "properties:\n  required: [type]\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def page(kind: str, slug: str, *, core=True, extra="", body="x", render=None) -> str:
    props = [
        f"type: {kind}",
        "kind: Leaf",
        "purpose: Prevents x (case 12)",
        "status: built",
        f"origin: raw/2026-09-10/1610/ledger.md#case-{slug[-1]}",
        "sprint: plugin",
        "created: 2026-09-10",
    ]
    if core:
        props.append("core: true")
    sections = f"## Purpose\n\n{body}\n"
    if render:
        sections += f"\n## Render\n\n<!-- {slug} -->\n{render}\n<!-- /{slug} -->\n"
    front = "\n".join(props + ([extra] if extra else []))
    return f"---\n{front}\n---\n\n{sections}\n## History\n\n- 2026-09-10 created\n"


def tree(root: Path, **pages: str) -> None:
    """A project with code, a harness, session records and the pages given by slug."""
    write(root / "CLAUDE.md", "# Project\n\nKeep the facts (case 59.8).\n")
    write(root / "Makefile", "test:\n\tuv run pytest\n")
    write(root / "pyproject.toml", "[project]\nname = 'x'\n")
    write(root / "uv.lock", "version = 1\n")
    write(root / ".gitattributes", "* text=auto\n")
    write(root / "guppi" / "x.py", "# reads a page (case 787)\nX = 1\n")
    write(root / "guppi" / "__pycache__" / "x.cpython-312.pyc", "junk")
    write(root / ".claude" / "settings.json", "{}\n")
    write(root / ".claude" / "settings.local.json", "{}\n")
    write(root / "guppi.toml", "documentation_lang = 'en'\n")
    write(root / ".github" / "workflows" / "checks.yml", "on: push\n")
    write(root / "vault" / "raw" / "2026-10-13" / "1753" / "frontier.md", "# Frontier\n")
    write(root / "vault" / "archive" / "plugin" / "x.md", "# old\n")
    wiki = root / "vault" / "wiki"
    for name in ("sprint", "backlog", "brief", "log"):
        write(wiki / f"{name}.md", f"# {name}\n")
    write(wiki / "tags.md", "# Tags\n")
    for category in ("entities", "rules", "estimates", "lessons", "insights", "decisions"):
        write(wiki / category / "schema.yaml", SCHEMA)
    folders = {"rule": "rules", "entity": "entities", "estimate": "estimates"}
    for slug, text in pages.items():
        write(wiki / folders[slug.split("_")[0]] / f"{slug.replace('_', '-')}.md", text)


def run(root: Path, out: Path) -> tuple[int, list[str]]:
    stdout, stderr = io.StringIO(), io.StringIO()
    code = ship.run([str(out)], stdout=stdout, stderr=stderr, project_dir=root, now=NOW)
    return code, stdout.getvalue().splitlines()


def written(out: Path) -> set[str]:
    return {p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file()}


def test_it_writes_the_code_the_harness_and_the_core_pages_only(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(
        root,
        rule_a=page("rule", "rule-a"),
        rule_b=page("rule", "rule-b", core=False),
        entity_x=page("entity", "entity-x"),
        estimate_x=page("estimate", "estimate-x", core=False),
    )
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    assert written(out) == {
        "CLAUDE.md",
        "Makefile",
        "pyproject.toml",
        "uv.lock",
        ".gitattributes",
        "guppi/x.py",
        ".claude/settings.json",
        "vault/wiki/tags.md",
        *(f"vault/wiki/{c}/schema.yaml" for c in lint.CATEGORIES),
        "vault/wiki/rules/rule-a.md",
        "vault/wiki/entities/entity-x.md",
    }


def test_it_writes_a_file_a_core_page_renders_and_not_one_a_loose_page_renders(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    render = "enforcement: render\nrender_mode: full\ngoverns: {}"
    tree(
        root,
        rule_a=page(
            "rule", "rule-a", extra=render.format("vault/wiki/ratification.md"), render="R"
        ),
        rule_b=page(
            "rule",
            "rule-b",
            core=False,
            extra=render.format(".claude/skills/b/SKILL.md"),
            render="B",
        ),
        rule_c=page("rule", "rule-c", extra=render.format("guppi.toml"), render="T"),
    )
    write(root / "vault" / "wiki" / "ratification.md", "R\n")
    write(root / ".claude" / "skills" / "b" / "SKILL.md", "B\n")
    code, _ = run(root, out)
    assert code == 0
    files = written(out)
    assert "vault/wiki/ratification.md" in files
    assert ".claude/skills/b/SKILL.md" not in files
    assert "guppi.toml" not in files


def test_it_writes_no_session_record_and_no_file_of_this_project(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    run(root, out)
    files = written(out)
    for name in files:
        assert not name.startswith(("vault/raw/", "vault/archive/", ".github/"))
    for name in ("sprint", "backlog", "brief", "log"):
        assert f"vault/wiki/{name}.md" not in files
    assert "guppi.toml" not in files
    assert ".claude/settings.local.json" not in files


def test_it_removes_each_bracket_that_holds_a_pointer_whole(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    body = (
        "One (case 12). Two (cases 3.1, 4 and kir-plugin-5). "
        "Three (`rule-a`, case 628.4). Four (as set in case 9). Five [[decision-case-7]]. "
        "Six (measured 2026-09-25, session 0051). Seven (see decision-case-3). "
        "Eight (across\nlines, case 2). Nine (a plain aside) stays."
    )
    tree(root, rule_a=page("rule", "rule-a", body=body))
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    text = (out / "vault" / "wiki" / "rules" / "rule-a.md").read_text(encoding="utf-8")
    assert "One. Two. Three. Four. Five. Six. Seven. Eight. Nine (a plain aside) stays." in text
    assert "purpose: Prevents x\n" in text
    assert (out / "guppi" / "x.py").read_text(encoding="utf-8") == "# reads a page\nX = 1\n"
    assert (out / "CLAUDE.md").read_text(encoding="utf-8").endswith("Keep the facts.\n")


def test_a_bracket_that_opens_a_line_leaves_no_mark_alone(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    write(root / "guppi" / "y.py", '"""It reads the page\n    (case 714)."""\n')
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    assert (out / "guppi" / "y.py").read_text(encoding="utf-8") == '"""It reads the page."""\n'


def test_a_link_to_a_page_left_out_is_written_as_its_slug(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    body = "It links [[rule-b]], [[rule-a]] and [[brief|the brief]]."
    tree(root, rule_a=page("rule", "rule-a", body=body), rule_b=page("rule", "rule-b", core=False))
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    text = (out / "vault" / "wiki" / "rules" / "rule-a.md").read_text(encoding="utf-8")
    assert "It links `rule-b`, [[rule-a]] and `brief`." in text


def test_it_writes_the_shipped_values(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    links = (
        'parent: "[[rule-a]]"\nestimates: ["[[estimate-x]]"]\ndeferred_by: ["[[decision-case-3]]"]'
    )
    tree(
        root,
        rule_a=page("rule", "rule-a"),
        rule_b=page("rule", "rule-b", extra=links),
        estimate_x=page("estimate", "estimate-x", core=False),
    )
    run(root, out)
    shipped = read_page(out / "vault" / "wiki" / "rules" / "rule-b.md", "rules")
    assert shipped.props["origin"] == "guppi"
    assert shipped.props["sprint"] == "guppi"
    assert str(shipped.props["created"]) == "2026-10-13"
    assert shipped.props["core"] is True
    assert shipped.props["parent"] == "rule-a"
    assert shipped.props["estimates"] == []
    assert "deferred_by" not in shipped.props
    assert shipped.sections["## History"] == "- 2026-10-13 shipped with GUPPI"


def test_a_pointer_outside_a_bracket_exits_1(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    body = "Since case 239 it reads.\n\nIn session 0051 it broke, and in sessions 1237 and 1441."
    tree(root, rule_a=page("rule", "rule-a", body=body))
    write(root / "guppi" / "y.py", "# decision-case-616 stays open\n")
    code, lines = run(root, out)
    assert code == 1
    assert "ship: guppi/y.py:1: a reference to a decision: decision-case-616" in lines
    assert any(
        l.startswith("ship: vault/wiki/rules/rule-a.md:") and "a reference to a case: case 239" in l
        for l in lines
    )
    assert any("a mention of a session: session 0051" in l for l in lines)
    assert any("a mention of a session: sessions 1237 and 1441" in l for l in lines)


def test_a_sample_is_no_pointer(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    fenced = "Before.\n\n````showing\n## Case 7 — A sample (case 3)\n````\n\nAfter."
    render = "enforcement: render\nrender_mode: full\ngoverns: vault/wiki/case-example.md"
    tree(
        root,
        rule_a=page("rule", "rule-a", body=fenced),
        rule_case_example=page("rule", "rule-case-example", extra=render, render="## Case 1 — x"),
    )
    write(root / "vault" / "wiki" / "case-example.md", "Cart (case 717.1).\n\n## Case 1 — x\n")
    write(
        root / "vault" / "wiki" / "decisions" / "schema.yaml",
        "description: |\n  A slug `decision-case-18.1`.\n  ```\n  case 4\n  ```\n",
    )
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    text = (out / "vault" / "wiki" / "rules" / "rule-a.md").read_text(encoding="utf-8")
    assert "## Case 7 — A sample (case 3)" in text
    example = (out / "vault" / "wiki" / "case-example.md").read_text(encoding="utf-8")
    assert example == "Cart (case 717.1).\n\n## Case 1 — x\n"


def test_review_lists_a_bracket_with_words_and_sets_no_exit_code(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    body = "One (case 12). Two (the folder, case 73)."
    tree(root, rule_a=page("rule", "rule-a", body=body))
    stdout = io.StringIO()
    code = ship.run(
        ["--review", str(out)], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW
    )
    lines = stdout.getvalue().splitlines()
    assert code == 0
    assert len(lines) == 1
    assert lines[0].startswith("ship: vault/wiki/rules/rule-a.md:")
    assert lines[0].endswith("a bracket with words: (the folder, case 73)")


def test_check_judges_the_files_outside_the_vault_in_place(tmp_path):
    root = tmp_path / "p"
    body = "Since case 239 it reads."
    tree(root, rule_a=page("rule", "rule-a", body=body))
    write(root / "guppi" / "y.py", "# since case 5 it reads\n# a note (as set in case 6)\n")
    write(root / "uv.lock", "case 9\n")
    before = written(root)
    stdout = io.StringIO()
    code = ship.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW)
    assert code == 1
    assert stdout.getvalue().splitlines() == ["ship: guppi/y.py:1: a reference to a case: case 5"]
    assert written(root) == before
    assert (root / "guppi" / "y.py").read_text(encoding="utf-8").endswith("(as set in case 6)\n")


def test_a_section_of_a_loose_page_exits_1(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"), rule_b=page("rule", "rule-b", core=False))
    write(
        root / ".claude" / "skills" / "hi" / "SKILL.md",
        "Hi\n<!-- rule-b -->\nB\n<!-- /rule-b -->\n",
    )
    code, lines = run(root, out)
    assert code == 1
    assert lines == [
        "ship: .claude/skills/hi/SKILL.md:2: a section of rule-b, a page without core: true",
        "ship: .claude/skills/hi/SKILL.md:4: a section of rule-b, a page without core: true",
    ]


def test_the_form_of_a_line_is_no_reference(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    body = "A line `- decision[case 7.1][update][rule-a]` and `(case 3)`.\n\nThe origin #case-4 and {supersedes:case 5}."
    tree(root, rule_a=page("rule", "rule-a", body=body))
    write(root / "guppi" / "z.py", 'LINE = "- decision[case 1][create][rule-a]"\n')
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    text = (out / "vault" / "wiki" / "rules" / "rule-a.md").read_text(encoding="utf-8")
    assert "`(case 3)`" in text


def test_a_folder_that_is_not_empty_writes_nothing(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    write(out / "x.txt", "x")
    stderr = io.StringIO()
    code = ship.run([str(out)], stdout=io.StringIO(), stderr=stderr, project_dir=root, now=NOW)
    assert code == 2
    assert written(out) == {"x.txt"}


def test_lint_finds_no_origin_on_a_page_ship_wrote(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    run(root, out)
    shipped = read_page(out / "vault" / "wiki" / "rules" / "rule-a.md", "rules")
    assert lint.check_origin(shipped, out) == []
