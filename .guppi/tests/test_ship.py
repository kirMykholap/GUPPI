"""`guppi ship` over a sample tree, `estimate-clean-branch-writes-a-clean-copy` (cases 804.6,
807.1, 808.1): only the code, the harness and the pages with `core: true` are written, each
bracket that holds a pointer goes whole, a link to a page left out becomes its slug, samples
stay, the shipped values are written, a pointer outside a bracket and a bare case number in a
comment or a docstring of a Python file exit 1, and `--review` and `--check` work as the rule
sets them. The sample tree is a git repository whose history carries a tag `prod-x.y.z`: the
copy holds the manifest and the catalogue of the plugin, the manifest with the version of the
highest such tag, and exits 1 with none (case 816); it writes the skills of `plugin/skills/`
under `skills/` (case 818). The code is written under `.guppi/`, without its Python
environment, a cache folder or the root `pyproject.toml` and `uv.lock`, and `.guppi/uv.lock`
is not cleaned (case 819.3). The copy holds `.guppi/guppi/pointers.py` and no
`.guppi/guppi/ship.py`, so its `guppi` lists no command `ship`, and `--check` does not judge
that module; `estimate-clean-branch-ships-no-ship-command` runs the tests whose names hold
`ship_command` (case 820.5). The copy holds each passed Estimate of a page it writes, with
`core: true` and a Result of one line, and no other, by the tests whose names hold
`estimate`; the tests but those of `ship`, their comments and docstrings cleaned and their
other strings kept as samples, by the tests whose names hold `tests`; and the session files
as skeletons that their own checks pass, by the tests whose names hold `skeleton`; the CI of
the checks, cleaned, and no other file of `.github/`, by the tests whose names hold
`checks_workflow`; no build while a page with `core: true` is draft but with `--allow-draft`,
by the tests whose names hold `draft_core`; and a blank description of the project in
`CLAUDE.md` and in the Render of `rule-claude-md`, by the tests whose names hold `description`
(case 822)."""

import io
import json
import os
import shutil
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

from guppi import backlog, glossary, lint, ship, sprint
from guppi.pages import read_page

NOW = datetime(2026, 10, 13, 18, 0, tzinfo=UTC)
SCHEMA = "properties:\n  required: [type]\n"
REPO = Path(__file__).resolve().parents[2]
DESCRIPTION = (
    "A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into"
)
SKILL = "---\nname: install\n---\n\nInstall GUPPI (case 818).\n"
GLOSSARY_PAGE = (
    "---\ntype: entity\nkind: Leaf\npurpose: Prevents x\nstatus: built\n"
    "origin: raw/2026-09-10/1610/ledger.md#case-1\nsprint: plugin\ncreated: 2026-09-10\n"
    "core: true\n---\n\n## Terms\n\n| term | meaning | where |\n|---|---|---|\n"
    "| Glossary | the terms (case 306) | [[entity-glossary]] |\n\n"
    "## History\n\n- 2026-09-10 created\n"
)
# the CI of the checks, which the copy writes cleaned, and the workflow that writes `prod`,
# which it neither writes nor judges, so its pointer outside a bracket prints nothing
CHECKS_WORKFLOW = "# The checks of a pull request (case 787).\non: push\n"
PROD_WORKFLOW = "# since case 804 it writes prod\non: push\n"


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


def git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


def commit(root: Path, *tags: str) -> None:
    """Commits the whole tree and places each tag on that commit."""
    git(root, "add", "-A")
    git(root, "commit", "-q", "--allow-empty", "-m", "x")
    for tag in tags:
        git(root, "tag", tag)


def tree(root: Path, tags: tuple[str, ...] = ("prod-0.2.0",), **pages: str) -> None:
    """A project with code, a harness, the templates and the skill of the plugin, session
    records and the pages given by slug, committed in a git repository with `tags`."""
    write(root / "CLAUDE.md", "# Project\n\nKeep the facts (case 59.8).\n")
    write(root / "Makefile", "test:\n\tuv run --project .guppi pytest\n")
    write(root / "pyproject.toml", "[project]\nname = 'x'\n")
    write(root / "uv.lock", "version = 1\n")
    write(root / ".gitattributes", "* text=auto\n")
    write(root / ".guppi" / "guppi" / "x.py", "# reads a page (case 787)\nX = 1\n")
    write(root / ".guppi" / "guppi" / "__pycache__" / "x.cpython-312.pyc", "junk")
    write(root / ".guppi" / "pyproject.toml", "[project]\nname = 'guppi'\n")
    write(root / ".guppi" / "uv.lock", "version = 1\n")
    write(root / ".guppi" / ".gitignore", ".venv/\n")
    # the environment and a cache folder hold pointers, so a judgment of them would print
    write(root / ".guppi" / ".venv" / "lib" / "site.py", "# since case 5 it reads\n")
    write(root / ".guppi" / ".pytest_cache" / "README.md", "Since case 7 it caches.\n")
    write(root / ".claude" / "settings.json", "{}\n")
    write(root / ".claude" / "settings.local.json", "{}\n")
    write(root / "guppi.toml", "documentation_lang = 'en'\n")
    write(root / ".github" / "workflows" / "checks.yml", CHECKS_WORKFLOW)
    write(root / ".github" / "workflows" / "prod.yml", PROD_WORKFLOW)
    write(root / "vault" / "raw" / "2026-10-13" / "1753" / "frontier.md", "# Frontier\n")
    write(root / "vault" / "archive" / "plugin" / "x.md", "# old\n")
    wiki = root / "vault" / "wiki"
    for name in ("sprint", "backlog", "brief", "log"):
        write(wiki / f"{name}.md", f"# {name}\n")
    write(wiki / "tags.md", "# Tags\n")
    for category in ("entities", "rules", "estimates", "lessons", "insights", "decisions"):
        write(wiki / category / "schema.yaml", SCHEMA)
    write(wiki / "entities" / "entity-glossary.md", GLOSSARY_PAGE)
    folders = {"rule": "rules", "entity": "entities", "estimate": "estimates"}
    for slug, text in pages.items():
        write(wiki / folders[slug.split("_")[0]] / f"{slug.replace('_', '-')}.md", text)
    for name in ("plugin.json", "marketplace.json"):
        write(root / "plugin" / name, (REPO / "plugin" / name).read_text(encoding="utf-8"))
    write(root / "plugin" / "skills" / "install" / "SKILL.md", SKILL)
    git(root, "init", "-q")
    git(root, "config", "user.email", "t@example.com")
    git(root, "config", "user.name", "t")
    commit(root, *tags)


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
        ".gitattributes",
        ".guppi/guppi/x.py",
        ".guppi/pyproject.toml",
        ".guppi/uv.lock",
        ".guppi/.gitignore",
        ".claude/settings.json",
        ".github/workflows/checks.yml",
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        "skills/install/SKILL.md",
        "vault/wiki/tags.md",
        *(f"vault/wiki/{c}/schema.yaml" for c in lint.CATEGORIES),
        *ship.SKELETONS,
        "vault/wiki/rules/rule-a.md",
        "vault/wiki/entities/entity-x.md",
        "vault/wiki/entities/entity-glossary.md",
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
        assert not name.startswith(("vault/raw/", "vault/archive/"))
    assert [name for name in files if name.startswith(".github/")] == [ship.CI]
    for name in ("sprint", "backlog", "brief", "log"):  # a skeleton, not the file of the tree
        assert (out / "vault" / "wiki" / f"{name}.md").read_text(encoding="utf-8") != f"# {name}\n"
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
    assert (out / ".guppi" / "guppi" / "x.py").read_text(
        encoding="utf-8"
    ) == "# reads a page\nX = 1\n"
    assert (out / "CLAUDE.md").read_text(encoding="utf-8").endswith("Keep the facts.\n")


def test_a_bracket_that_opens_a_line_leaves_no_mark_alone(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    write(root / ".guppi" / "guppi" / "y.py", '"""It reads the page\n    (case 714)."""\n')
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    assert (out / ".guppi" / "guppi" / "y.py").read_text(
        encoding="utf-8"
    ) == '"""It reads the page."""\n'


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
    write(root / ".guppi" / "guppi" / "y.py", "# decision-case-616 stays open\n")
    code, lines = run(root, out)
    assert code == 1
    assert "ship: .guppi/guppi/y.py:1: a reference to a decision: decision-case-616" in lines
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
    example_case = "Cart (case 717.1).\n\n````case\n## Case 1 — x (case 3)\n````"
    tree(
        root,
        rule_a=page("rule", "rule-a", body=fenced),
        rule_case_example=page("rule", "rule-case-example", extra=render, render=example_case),
    )
    write(root / "vault" / "wiki" / "case-example.md", example_case + "\n")
    write(
        root / "vault" / "wiki" / "decisions" / "schema.yaml",
        "description: |\n  A slug `decision-case-18.1`.\n  ```\n  case 4\n  ```\n",
    )
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    text = (out / "vault" / "wiki" / "rules" / "rule-a.md").read_text(encoding="utf-8")
    assert "## Case 7 — A sample (case 3)" in text
    example = (out / "vault" / "wiki" / "case-example.md").read_text(encoding="utf-8")
    assert example == "Cart.\n\n````case\n## Case 1 — x (case 3)\n````\n"
    rule = (out / "vault" / "wiki" / "rules" / "rule-case-example.md").read_text(encoding="utf-8")
    assert "## Case 1 — x (case 3)" in rule
    assert "(case 717.1)" not in rule
    assert "Cart.\n" in rule


def test_a_pointer_in_the_prose_of_the_example_file_exits_1(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    render = "enforcement: render\nrender_mode: full\ngoverns: vault/wiki/case-example.md"
    tree(root, rule_case_example=page("rule", "rule-case-example", extra=render, render="x"))
    text = "Since case 717.1 the cart stands.\n\n````case\n## Case 1 — x\n````\n"
    write(root / "vault" / "wiki" / "case-example.md", text)
    code, lines = run(root, out)
    assert code == 1
    assert [line for line in lines if line.startswith("ship: vault/wiki/case-example.md:1:")]


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
    write(
        root / ".guppi" / "guppi" / "y.py", "# since case 5 it reads\n# a note (as set in case 6)\n"
    )
    write(root / ".guppi" / "uv.lock", "case 9\n")
    write(root / "pyproject.toml", "# since case 8, the root project\n")
    before = written(root)
    stdout = io.StringIO()
    code = ship.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW)
    assert code == 1
    assert stdout.getvalue().splitlines() == [
        "ship: .guppi/guppi/y.py:1: a reference to a case: case 5"
    ]
    assert written(root) == before
    assert (
        (root / ".guppi" / "guppi" / "y.py")
        .read_text(encoding="utf-8")
        .endswith("(as set in case 6)\n")
    )


BARE = '''"""75.2: the frontier (513, 544.7)."""

X = 1  # not the records (274.1)
# 169.1: the reason is for the person
Y = 2  # 786


def f():
    """Reads a page (280–281)."""
    return 3
'''


def test_a_bare_case_number_in_a_comment_or_a_docstring_exits_1_and_stays(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    write(root / ".guppi" / "guppi" / "y.py", BARE)
    code, lines = run(root, out)
    assert code == 1
    assert lines == [
        "ship: .guppi/guppi/y.py:1: a bare case number: (513, 544.7)",
        "ship: .guppi/guppi/y.py:1: a bare case number: 75.2:",
        "ship: .guppi/guppi/y.py:3: a bare case number: (274.1)",
        "ship: .guppi/guppi/y.py:4: a bare case number: 169.1:",
        "ship: .guppi/guppi/y.py:5: a bare case number: 786",
        "ship: .guppi/guppi/y.py:9: a bare case number: (280–281)",
    ]
    assert (out / ".guppi" / "guppi" / "y.py").read_text(encoding="utf-8") == BARE


BARE_LIST = '''"""387.4, 445.4 and 476.3: the frontier."""

# 387.4; 445.4: the reason is for the person
X = 1  # 387.4, 445.4
Y = 2  # 280–281
Z = 3  # 3, 4 tries
'''


def test_a_list_of_bare_case_numbers_at_an_opening_or_alone_exits_1_and_stays(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    write(root / ".guppi" / "guppi" / "y.py", BARE_LIST)
    code, lines = run(root, out)
    assert code == 1
    assert lines == [
        "ship: .guppi/guppi/y.py:1: a bare case number: 387.4, 445.4 and 476.3:",
        "ship: .guppi/guppi/y.py:3: a bare case number: 387.4; 445.4:",
        "ship: .guppi/guppi/y.py:4: a bare case number: 387.4, 445.4",
        "ship: .guppi/guppi/y.py:5: a bare case number: 280–281",
    ]
    assert (out / ".guppi" / "guppi" / "y.py").read_text(encoding="utf-8") == BARE_LIST


def test_check_reports_a_bare_case_number_in_place(tmp_path):
    root = tmp_path / "p"
    tree(root, rule_a=page("rule", "rule-a"))
    write(root / ".guppi" / "guppi" / "y.py", "X = 1  # not the records (274.1)\n")
    stdout = io.StringIO()
    code = ship.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW)
    assert code == 1
    assert stdout.getvalue().splitlines() == [
        "ship: .guppi/guppi/y.py:1: a bare case number: (274.1)"
    ]


def test_code_and_a_count_are_no_bare_case_number(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    code_text = (
        '"""Reads a page, measured (2026-09-25)."""\n'
        "N = m.group(1) + f(274.1)  # 3 tries, as in m.group(2)\n"
        'S = "(274.1)"\n'
        "call(\n"
        '    "75.2: a string argument",\n'
        ")\n"
    )
    write(root / ".guppi" / "guppi" / "y.py", code_text)
    write(root / ".guppi" / "pyproject.toml", "# 786\n[project]\nname = 'guppi'\n")
    code, lines = run(root, out)
    assert (code, lines) == (0, [])


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
    write(root / ".guppi" / "guppi" / "z.py", 'LINE = "- decision[case 1][create][rule-a]"\n')
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


def manifest_of(out: Path) -> dict:
    return json.loads((out / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))


def test_it_writes_the_manifest_and_the_catalogue_of_the_plugin(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    assert manifest_of(out) == {
        "name": "guppi",
        "version": "0.2.0",
        "description": DESCRIPTION,
        "author": {"name": "kirMykholap"},
        "repository": "https://github.com/kirMykholap/GUPPI",
    }
    catalogue = (out / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    assert json.loads(catalogue) == {
        "name": "guppi-marketplace",
        "owner": {"name": "kirMykholap"},
        "plugins": [{"name": "guppi", "source": "./", "description": DESCRIPTION}],
    }
    assert "version" not in json.loads((REPO / "plugin" / "plugin.json").read_text("utf-8"))


def test_the_version_is_the_highest_tag_prod_x_y_z_in_the_history(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, ("prod-0.9.0",), rule_a=page("rule", "rule-a"))
    write(root / ".guppi" / "guppi" / "y.py", "Y = 1\n")
    commit(root, "prod-0.10.0")
    git(root, "switch", "-q", "-c", "other")
    commit(root, "prod-1.0.0")
    git(root, "switch", "-q", "-")
    code, _ = run(root, out)
    assert code == 0
    assert manifest_of(out)["version"] == "0.10.0"


def test_a_tag_of_another_form_gives_no_version(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, ("prod-0.2.0", "prod-2", "prod-3.0", "prod-4.0.0.1"), rule_a=page("rule", "rule-a"))
    code, _ = run(root, out)
    assert code == 0
    assert manifest_of(out)["version"] == "0.2.0"


def test_no_tag_prod_x_y_z_in_the_history_exits_1_and_writes_nothing(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, ("prod-1", "prod-2"), rule_a=page("rule", "rule-a"))
    stderr = io.StringIO()
    code = ship.run([str(out)], stdout=io.StringIO(), stderr=stderr, project_dir=root, now=NOW)
    assert code == 1
    assert stderr.getvalue().startswith("ship: no tag prod-x.y.z")
    assert not out.exists()


def test_check_reads_no_tag(tmp_path):
    root = tmp_path / "p"
    tree(root, (), rule_a=page("rule", "rule-a"))
    stdout = io.StringIO()
    code = ship.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW)
    assert (code, stdout.getvalue()) == (0, "")


def test_the_plugin_skill_is_written_under_skills_without_its_pointer(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    skill = (out / "skills" / "install" / "SKILL.md").read_text(encoding="utf-8")
    assert skill == "---\nname: install\n---\n\nInstall GUPPI.\n"
    assert not (out / "plugin").exists()


def test_check_judges_the_plugin_skill_in_place(tmp_path):
    root = tmp_path / "p"
    tree(root, rule_a=page("rule", "rule-a"))
    write(root / "plugin" / "skills" / "install" / "SKILL.md", "Since case 818 it installs.\n")
    stdout = io.StringIO()
    code = ship.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW)
    assert code == 1
    assert stdout.getvalue().splitlines() == [
        "ship: plugin/skills/install/SKILL.md:1: a reference to a case: case 818"
    ]


# --- case 820.5: the clean version holds no command ship; each test name holds ship_command --

PACKAGE = Path(ship.__file__).resolve().parent


def guppi_of(code: Path, *argv: str) -> subprocess.CompletedProcess:
    """`guppi` run from the package under `code`, in a process of its own."""
    return subprocess.run(
        [sys.executable, "-P", "-m", "guppi.cli", *argv],
        check=False,
        cwd=code,
        env=dict(os.environ, PYTHONPATH=str(code)),
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120,
    )


def commands_listed(done: subprocess.CompletedProcess) -> list[str]:
    return done.stderr.split("commands: ", 1)[1].strip().split(", ")


def test_the_clean_version_holds_pointers_and_no_ship_command(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    shutil.copytree(
        PACKAGE,
        root / ".guppi" / "guppi",
        ignore=shutil.ignore_patterns("__pycache__"),
        dirs_exist_ok=True,
    )
    run(root, out)
    assert (out / ".guppi" / "guppi" / "pointers.py").is_file()
    assert not (out / ".guppi" / "guppi" / "ship.py").exists()
    listed = guppi_of(out / ".guppi")
    assert listed.returncode == 2, listed.stderr
    assert "ship" not in commands_listed(listed)
    assert "check" in commands_listed(listed)
    unknown = guppi_of(out / ".guppi", "ship", "--check")
    assert unknown.returncode == 2
    assert unknown.stderr.splitlines() == ["guppi: unknown command 'ship'"]


def test_this_repository_lists_the_ship_command():
    assert "ship" in commands_listed(guppi_of(PACKAGE.parent))


def test_check_judges_no_line_of_the_module_of_the_ship_command(tmp_path):
    root = tmp_path / "p"
    tree(root, rule_a=page("rule", "rule-a"))
    write(root / ".guppi" / "guppi" / "ship.py", "# since case 5 it ships\n")
    stdout = io.StringIO()
    code = ship.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW)
    assert (code, stdout.getvalue()) == (0, "")


def test_the_ship_command_judges_a_pointer_by_the_module_of_pointers():
    from guppi import pointers

    assert ship.outside is pointers.outside
    for name in ("masked", "removed", "unmasked", "DECISION_LINK"):
        assert getattr(ship, name) is getattr(pointers, name), name
    source = Path(ship.__file__).read_text(encoding="utf-8")
    for definition in ("def outside(", "def masked(", "def removed(", "\nREFS =", "\nBRACKET ="):
        assert definition not in source, definition


# --- the passed Estimates of the pages it writes; each test name holds estimate (case 822) ---


def estimate(
    slug: str,
    target: str,
    status: str = "passed",
    method: str = "uv run --project .guppi pytest .guppi/tests/test_x.py",
    checked: str | None = "2026-10-01",
    criterion: str = "When:\nIt runs.\n\nThen:\nIt holds (case 12).",
    result: str = "2026-10-01, uv run pytest tests/test_x.py in session 1610: 3 passed.",
) -> str:
    props = [
        "type: estimate",
        "kind: QA",
        f"status: {status}",
        f'target: "[[{target}]]"',
        "purpose: Whether it holds (case 12)",
        f"method: {method}",
        *([f"checked: {checked}"] if checked else []),
        f"origin: raw/2026-09-10/1610/ledger.md#case-{slug[-1]}",
        "sprint: plugin",
        "created: 2026-09-10",
    ]
    body = f"## Criterion\n\n{criterion}\n\n## Result\n\n{result}\n\n## History\n\n- 2026-09-10 x\n"
    return "---\n" + "\n".join(props) + "\n---\n\n" + body


ESTIMATES = 'estimates: ["[[estimate-a]]", "[[estimate-p]]", "[[estimate-f]]", "[[estimate-m]]"]'


def estimate_tree(root: Path, **pages: str) -> None:
    """A page with `core: true` with a passed, a pending and a failed Estimate and a passed
    one whose method names a make target, and a page without it with a passed Estimate."""
    sample = {
        "rule_a": page("rule", "rule-a", extra=ESTIMATES),
        "rule_b": page("rule", "rule-b", core=False, extra='estimates: ["[[estimate-b]]"]'),
        "estimate_a": estimate("estimate-a", "rule-a"),
        "estimate_p": estimate("estimate-p", "rule-a", status="pending"),
        "estimate_f": estimate("estimate-f", "rule-a", status="failed"),
        "estimate_m": estimate("estimate-m", "rule-a", method="`make test-x`"),
        "estimate_b": estimate("estimate-b", "rule-b"),
    }
    tree(root, **(sample | pages))


def test_it_writes_each_passed_estimate_of_a_page_it_writes_and_no_other(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    estimate_tree(root)
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    shipped = {p.name for p in (out / "vault" / "wiki" / "estimates").glob("estimate-*.md")}
    assert shipped == {"estimate-a.md"}
    rule = read_page(out / "vault" / "wiki" / "rules" / "rule-a.md", "rules")
    assert rule.props["estimates"] == ["estimate-a"]


def test_a_shipped_estimate_carries_core_and_a_result_of_one_line(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    estimate_tree(root)
    run(root, out)
    shipped = read_page(out / "vault" / "wiki" / "estimates" / "estimate-a.md", "estimates")
    assert shipped.props["core"] is True
    assert (shipped.props["origin"], shipped.props["sprint"]) == ("guppi", "guppi")
    assert (shipped.props["status"], str(shipped.props["checked"])) == ("passed", "2026-10-01")
    assert shipped.props["purpose"] == "Whether it holds"
    assert shipped.props["method"] == "uv run --project .guppi pytest .guppi/tests/test_x.py"
    assert shipped.sections["## Criterion"] == "When:\nIt runs.\n\nThen:\nIt holds."
    assert shipped.sections["## Result"] == "2026-10-01, passed in the repository of GUPPI."
    assert shipped.sections["## History"] == "- 2026-10-13 shipped with GUPPI"
    assert lint.check_origin(shipped, out) == []


def test_an_estimate_without_checked_takes_the_date_its_result_opens_with(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    estimate_tree(root, estimate_a=estimate("estimate-a", "rule-a", checked=None))
    run(root, out)
    shipped = read_page(out / "vault" / "wiki" / "estimates" / "estimate-a.md", "estimates")
    assert shipped.sections["## Result"] == "2026-10-01, passed in the repository of GUPPI."


def test_a_pointer_outside_a_bracket_in_a_shipped_estimate_exits_1(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    criterion = "When:\nIt runs.\n\nThen:\nSince case 12 it holds."
    estimate_tree(root, estimate_a=estimate("estimate-a", "rule-a", criterion=criterion))
    code, lines = run(root, out)
    assert code == 1
    (line,) = [line for line in lines if "estimate-a.md" in line]
    assert line.startswith("ship: vault/wiki/estimates/estimate-a.md:")
    assert line.endswith(": a reference to a case: case 12")


# --- the tests with their samples; each test name holds tests (case 822) --------------------

TEST_FILE = '''"""Reads a page (case 12)."""

LINE = "- decision[case 10][create][rule-a]"
NOTE = "a bracket (case 320) in a sample"
FORMS = (
    "uv run guppi",  # the old form (before case 819.1)
    "uv run --project .guppi guppi",
)


def test_x():
    # it reads a page (case 9)
    assert LINE and NOTE and FORMS
'''


def test_the_copy_holds_the_tests_with_their_samples_and_not_the_tests_of_ship(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    write(root / ".guppi" / "tests" / "test_x.py", TEST_FILE)
    write(root / ".guppi" / "tests" / "test_ship.py", "X = 1\n")
    write(root / ".guppi" / "tests" / "__pycache__" / "test_x.cpython-312.pyc", "junk")
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    files = written(out)
    assert ".guppi/tests/test_x.py" in files
    assert ".guppi/tests/test_ship.py" not in files
    assert not any(name.startswith(".guppi/tests/__pycache__") for name in files)
    text = (out / ".guppi" / "tests" / "test_x.py").read_text(encoding="utf-8")
    assert text == (
        TEST_FILE.replace(" (case 12)", "")
        .replace(" (before case 819.1)", "")
        .replace(" (case 9)", "")
    )
    assert 'LINE = "- decision[case 10][create][rule-a]"' in text
    assert 'NOTE = "a bracket (case 320) in a sample"' in text


def test_check_judges_the_comments_of_the_tests_and_not_their_strings(tmp_path):
    root = tmp_path / "p"
    tree(root, rule_a=page("rule", "rule-a"))
    write(
        root / ".guppi" / "tests" / "test_y.py",
        '# since case 5 it reads\nS = "since case 6 it reads"\n"""Since case 7 it reads."""\n',
    )
    write(root / ".guppi" / "tests" / "test_ship.py", "# since case 4 it ships\n")
    write(root / ".guppi" / "guppi" / "z.py", 'S = "since case 8 it reads"\n')
    stdout = io.StringIO()
    code = ship.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW)
    assert code == 1
    assert stdout.getvalue().splitlines() == [
        "ship: .guppi/guppi/z.py:1: a reference to a case: case 8",
        "ship: .guppi/tests/test_y.py:1: a reference to a case: case 5",
        "ship: .guppi/tests/test_y.py:3: a reference to a case: case 7",
    ]


# --- the session files as skeletons; each test name holds skeleton (case 822) ---------------


def test_the_copy_holds_the_session_files_as_skeletons(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    wiki = out / "vault" / "wiki"
    assert (wiki / "sprint.md").read_text(encoding="utf-8") == sprint.closed_form("guppi")
    brief = (wiki / "brief.md").read_text(encoding="utf-8")
    cases = brief.split("### Cases\n\n", 1)[1]
    assert cases.splitlines()[0] == (
        "- open the next sprint — no sprint is open since the close of guppi"
    )
    assert (wiki / "log.md").read_text(encoding="utf-8") == (
        "# Log\n\nEvery page change, one line each, appended by a hook and never by an agent "
        "following an\ninstruction. The global feed; a page's own `## History` is the per-page "
        "view.\n"
    )
    assert (wiki / "backlog.md").read_text(encoding="utf-8").startswith("# Backlog\n\n0 items\n")
    assert "| Glossary | the terms | [[entity-glossary]] |" in (wiki / "glossary.md").read_text(
        encoding="utf-8"
    )


def test_the_checks_of_the_session_files_pass_over_the_skeleton_copy(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    run(root, out)
    for module in (sprint, backlog, glossary):
        stdout = io.StringIO()
        code = module.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=out)
        assert (code, stdout.getvalue()) == (0, ""), module.__name__


def test_a_writer_that_refuses_its_skeleton_exits_1(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    (root / "vault" / "wiki" / "entities" / "entity-glossary.md").unlink()
    code, lines = run(root, out)
    assert code == 1
    assert lines == ["ship: vault/wiki/glossary.md: glossary: no live entity-glossary page"]
    assert not (out / "vault" / "wiki" / "glossary.md").exists()


# --- the CI of the checks; each test name holds checks_workflow (case 822) -------------------


def test_the_copy_holds_the_checks_workflow_cleaned_and_no_other_file_of_github(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=page("rule", "rule-a"))
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    workflow = (out / ".github" / "workflows" / "checks.yml").read_text(encoding="utf-8")
    assert workflow == "# The checks of a pull request.\non: push\n"
    assert not (out / ".github" / "workflows" / "prod.yml").exists()
    assert [name for name in written(out) if name.startswith(".github/")] == [ship.CI]


def test_check_judges_the_checks_workflow_in_place_and_no_other_file_of_github(tmp_path):
    root = tmp_path / "p"
    tree(root, rule_a=page("rule", "rule-a"))
    write(root / ".github" / "workflows" / "checks.yml", "# since case 787 it checks\non: push\n")
    stdout = io.StringIO()
    code = ship.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW)
    assert code == 1
    assert stdout.getvalue().splitlines() == [
        "ship: .github/workflows/checks.yml:1: a reference to a case: case 787"
    ]


def test_the_checks_workflow_of_this_repository_names_no_page_the_copy_does_not_hold():
    text = (REPO / ship.CI).read_text(encoding="utf-8")
    comment = "\n".join(line for line in text.splitlines() if line.startswith("#"))
    assert "rule-github-repository" not in comment
    assert "Makefile" not in comment
    assert "[[" not in comment


# --- a draft page with core: true; each test name holds draft_core (case 822) ----------------


def draft(text: str) -> str:
    return text.replace("status: built", "status: draft")


def test_a_draft_core_page_exits_1_with_its_line_and_writes_nothing(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(
        root,
        rule_a=draft(page("rule", "rule-a")),
        rule_b=draft(page("rule", "rule-b", core=False)),
        entity_x=draft(page("entity", "entity-x")),
    )
    code, lines = run(root, out)
    assert code == 1
    assert lines == [
        "ship: vault/wiki/entities/entity-x.md: a page with core: true that is draft",
        "ship: vault/wiki/rules/rule-a.md: a page with core: true that is draft",
    ]
    assert not out.exists()


def test_allow_draft_writes_the_copy_of_a_draft_core_page_and_exits_0(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    tree(root, rule_a=draft(page("rule", "rule-a")))
    stdout = io.StringIO()
    code = ship.run(
        ["--allow-draft", str(out)], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW
    )
    assert code == 0
    assert stdout.getvalue().splitlines() == [
        "ship: vault/wiki/rules/rule-a.md: a page with core: true that is draft"
    ]
    assert "vault/wiki/rules/rule-a.md" in written(out)


def test_check_prints_no_line_on_a_draft_core_page(tmp_path):
    root = tmp_path / "p"
    tree(root, rule_a=draft(page("rule", "rule-a")))
    stdout = io.StringIO()
    code = ship.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=root, now=NOW)
    assert (code, stdout.getvalue()) == (0, "")


def test_the_build_judges_a_draft_core_page_by_the_one_judgment_of_pages():
    from guppi import pages

    assert ship.is_draft_core is pages.is_draft_core
    assert "def is_draft_core(" not in Path(ship.__file__).read_text(encoding="utf-8")


# --- the blank description of the project; each test name holds description (case 822) -----

DESCRIBED = (
    "<!-- project-description -->\n# GUPPI\n\nA harness and a vault.\n"
    "<!-- /project-description -->\n\nThe vault is `vault/`."
)
BLANK = (
    "<!-- project-description -->\n# Project\n\nProject description: not set yet.\n"
    "<!-- /project-description -->\n\nThe vault is `vault/`."
)


def described_tree(root: Path) -> None:
    """A tree whose `rule-claude-md`, with `core: true`, renders `CLAUDE.md` in full, both
    with the block of the description."""
    render = "enforcement: render\nrender_mode: full\ngoverns: CLAUDE.md"
    tree(root, rule_claude_md=page("rule", "rule-claude-md", extra=render, render=DESCRIBED))
    write(root / "CLAUDE.md", DESCRIBED + "\n")


def test_the_copy_holds_a_blank_description_in_claude_md_and_its_page(tmp_path):
    root, out = tmp_path / "p", tmp_path / "out"
    described_tree(root)
    code, lines = run(root, out)
    assert (code, lines) == (0, [])
    assert (out / "CLAUDE.md").read_text(encoding="utf-8") == BLANK + "\n"
    shipped = read_page(out / "vault" / "wiki" / "rules" / "rule-claude-md.md", "rules")
    assert shipped.sections["## Render"] == (
        f"<!-- rule-claude-md -->\n{BLANK}\n<!-- /rule-claude-md -->"
    )
    source = read_page(root / "vault" / "wiki" / "rules" / "rule-claude-md.md", "rules")
    assert DESCRIBED in source.sections["## Render"]
    assert (root / "CLAUDE.md").read_text(encoding="utf-8") == DESCRIBED + "\n"


def test_the_render_check_passes_over_the_copy_with_a_blank_description(tmp_path):
    from guppi import render

    root, out = tmp_path / "p", tmp_path / "out"
    described_tree(root)
    run(root, out)
    stdout = io.StringIO()
    code = render.run(["--check"], stdout=stdout, stderr=io.StringIO(), project_dir=out)
    assert (code, stdout.getvalue()) == (0, "")


def test_a_text_without_both_marker_lines_keeps_its_description():
    opening, closing = ship.DESCRIPTION_MARKERS
    for text in ("# GUPPI\n\nx\n", f"{opening}\n# GUPPI\n", f"{closing}\n# GUPPI\n{opening}\n"):
        assert ship.blank_description(text) == text
