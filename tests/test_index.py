"""`guppi index`: `vault/wiki/<category>-index.md`, one line per live page.

Rule page: `vault/wiki/rules/rule-index.md`. Built against a temp vault.
"""

import io

from guppi import index
from tests.test_render import page

FIVE = ["entities", "rules", "estimates", "lessons", "insights"]


def run(argv, project_dir):
    out, err = io.StringIO(), io.StringIO()
    code = index.run(argv, stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue(), err.getvalue()


def wiki(project_dir):
    return project_dir / "vault" / "wiki"


def seed(tmp_path):
    page(
        tmp_path, "entity-zeta", {"type": "entity", "purpose": "Last by name"}, category="entities"
    )
    page(
        tmp_path,
        "entity-alpha",
        {"type": "entity", "purpose": "First by name"},
        category="entities",
    )
    page(tmp_path, "rule-x", {"type": "rule", "purpose": "Prevents x"})
    page(tmp_path, "lesson-a-b", {"type": "lesson", "root_cause": "because b"}, category="lessons")
    page(tmp_path, "insight-c", {"type": "insight", "pattern": "always c"}, category="insights")
    page(tmp_path, "decision-x", {"type": "decision", "kind": "create"}, category="decisions")
    archive = wiki(tmp_path) / "archive" / "rules"
    archive.mkdir(parents=True)
    (archive / "rule-old.md").write_text("---\ntype: rule\npurpose: gone\n---\n", encoding="utf-8")
    estimate = wiki(tmp_path) / "estimates" / "estimate-x-works.md"
    estimate.parent.mkdir(parents=True)
    estimate.write_text(
        "---\ntype: estimate\ntarget: rule-x\n---\n\n## Context\n\nc\n\n## Criterion\n\n"
        "Given a\nmulti-line\n  criterion.\n\n## Method\n\nm\n",
        encoding="utf-8",
        newline="\n",
    )


def test_each_category_gets_one_line_per_live_page_in_slug_order(tmp_path):
    seed(tmp_path)
    code, out, err = run([], tmp_path)
    assert (code, out, err) == (0, "", "")
    read = lambda name: (wiki(tmp_path) / f"{name}-index.md").read_text(encoding="utf-8")
    assert read("entities") == "entity-alpha: First by name\nentity-zeta: Last by name\n"
    assert read("rules") == "rule-x: Prevents x\n"
    assert read("estimates") == "estimate-x-works: Given a multi-line criterion.\n"
    assert read("lessons") == "lesson-a-b: because b\n"
    assert read("insights") == "insight-c: always c\n"
    assert not (wiki(tmp_path) / "decisions-index.md").exists()
    assert "rule-old" not in read("rules")


def test_an_empty_category_yields_an_empty_file(tmp_path):
    page(tmp_path, "rule-x", {"type": "rule", "purpose": "Prevents x"})
    run([], tmp_path)
    for name in FIVE:
        assert (wiki(tmp_path) / f"{name}-index.md").exists()
    assert (wiki(tmp_path) / "lessons-index.md").read_text(encoding="utf-8") == ""


def test_check_names_a_stale_index_and_writes_nothing(tmp_path):
    seed(tmp_path)
    run([], tmp_path)
    page(tmp_path, "rule-y", {"type": "rule", "purpose": "Prevents y"})
    code, out, _err = run(["--check"], tmp_path)
    assert code == 1
    assert out == "index: vault/wiki/rules-index.md is stale\n"
    assert "rule-y" not in (wiki(tmp_path) / "rules-index.md").read_text(encoding="utf-8")


def test_check_is_silent_when_every_index_matches(tmp_path):
    seed(tmp_path)
    run([], tmp_path)
    assert run(["--check"], tmp_path) == (0, "", "")


def test_check_counts_a_missing_index_as_stale(tmp_path):
    seed(tmp_path)
    code, out, _err = run(["--check"], tmp_path)
    assert code == 1
    assert len(out.splitlines()) == 5


def test_cli_dispatches_to_index(tmp_path, monkeypatch, capsys):
    from guppi import cli

    seed(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["index", "--check"]) == 1
    assert "rules-index.md" in capsys.readouterr().out
