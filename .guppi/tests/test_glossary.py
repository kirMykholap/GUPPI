"""`guppi glossary`: `vault/wiki/glossary.md` written from the `## Terms` of
`entity-glossary`, one group per parent MOC of the pages in `where` (case 306.4,
`estimate-glossary-renders-the-terms`); `--check` names the file when it differs and
writes nothing (case 306.5, `estimate-glossary-checks-the-file`); the plain run ticks the
`guppi glossary` lines of every applied Spec (case 306.6, `estimate-glossary-ticks-the-spec`)."""

import io

import yaml

from guppi import glossary

GLOSSARY_PAGE = """---
type: entity
kind: Leaf
purpose: The terms of GUPPI
status: draft
parent: "[[entity-guppi]]"
estimates: []
origin: raw/2026-09-22/0014/ledger.md#case-306.3
sprint: migration
created: 2026-09-22
tags: [session, harness]
---

## Purpose

The terms.

## Terms

| term | meaning | where |
|---|---|---|
| Ratification | Human sign-off on a Decision | [[rule-case-protocol]] |
| Vault | The folder of pages | [[rule-page-schemas]] |
| Plan Mode | Frontier items as Cases | [[rule-plan-mode]] |
| Case | The unit of dialogue; `given` + `when` + `then` | [[rule-case-protocol]] |
| Work Mode | The Spec as tasks | [[rule-work-mode]] |

## History

- 2026-09-22 created
"""

EXPECTED = """# Glossary

Written by `guppi glossary` from the `## Terms` of `entity-glossary`; a term changes by an `update` of that page.

## [[rule-plan-mode]]

| term | meaning | where |
|---|---|---|
| Ratification | Human sign-off on a Decision | [[rule-case-protocol]] |
| Plan Mode | Frontier items as Cases | [[rule-plan-mode]] |
| Case | The unit of dialogue; `given` + `when` + `then` | [[rule-case-protocol]] |

## [[rule-harness]]

| term | meaning | where |
|---|---|---|
| Vault | The folder of pages | [[rule-page-schemas]] |

## [[rule-work-mode]]

| term | meaning | where |
|---|---|---|
| Work Mode | The Spec as tasks | [[rule-work-mode]] |
"""


def page(props, body="## Purpose\n\np\n\n## History\n\n- x\n"):
    front = "\n".join(f"{k}: {v}" for k, v in props.items())
    return f"---\n{front}\n---\n\n{body}"


def seed(tmp_path, glossary_page=GLOSSARY_PAGE):
    wiki = tmp_path / "vault" / "wiki"
    for category in ("entities", "rules", "estimates"):
        (wiki / category).mkdir(parents=True, exist_ok=True)
    (wiki / "glossary.md").write_text("# Glossary\n\nby hand\n", encoding="utf-8")
    (wiki / "entities" / "entity-glossary.md").write_text(
        glossary_page, encoding="utf-8", newline="\n"
    )
    write = lambda category, slug, props: (wiki / category / f"{slug}.md").write_text(
        page(props), encoding="utf-8", newline="\n"
    )
    write("entities", "entity-guppi", {"type": "entity", "kind": "MOC", "status": "draft"})
    write("rules", "rule-plan-mode", {"type": "rule", "kind": "MOC", "status": "built"})
    write("rules", "rule-harness", {"type": "rule", "kind": "MOC", "status": "built"})
    write(
        "rules",
        "rule-case-protocol",
        {"type": "rule", "kind": "Leaf", "status": "draft", "parent": '"[[rule-plan-mode]]"'},
    )
    write(
        "rules",
        "rule-page-schemas",
        {"type": "rule", "kind": "MOC", "status": "draft", "parent": '"[[rule-harness]]"'},
    )
    write("rules", "rule-work-mode", {"type": "rule", "status": "draft"})  # a placeholder
    return tmp_path


def run(project_dir, *argv):
    out, err = io.StringIO(), io.StringIO()
    code = glossary.run(list(argv), stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue(), err.getvalue()


def rendered(project_dir):
    return (project_dir / "vault" / "wiki" / "glossary.md").read_text(encoding="utf-8")


# --- the render (case 306.4) ---------------------------------------------------------------


def test_the_file_is_written_from_the_table_grouped_by_the_parent_moc_of_where(tmp_path):
    seed(tmp_path)
    assert run(tmp_path) == (0, "", "")
    assert rendered(tmp_path) == EXPECTED


def test_a_where_with_no_live_page_is_an_error_and_nothing_is_written(tmp_path):
    seed(tmp_path, GLOSSARY_PAGE.replace("[[rule-page-schemas]]", "[[rule-nowhere]]"))
    code, out, err = run(tmp_path)
    assert (code, out) == (1, "")
    assert err.strip() == "glossary: Vault: where names rule-nowhere, which no live page carries"
    assert rendered(tmp_path) == "# Glossary\n\nby hand\n"


def test_a_row_of_another_shape_a_bare_where_and_a_term_twice_are_errors(tmp_path):
    seed(
        tmp_path,
        GLOSSARY_PAGE.replace(
            "| Vault | The folder of pages | [[rule-page-schemas]] |",
            "| Vault | The folder of pages |",
        ),
    )
    assert run(tmp_path)[2].strip() == (
        "glossary: a row of 2 cells, not three: | Vault | The folder of pages |"
    )
    seed(tmp_path, GLOSSARY_PAGE.replace("[[rule-page-schemas]]", "rule-page-schemas"))
    assert run(tmp_path)[2].strip() == "glossary: Vault: where is not a [[slug]]: rule-page-schemas"
    seed(tmp_path, GLOSSARY_PAGE.replace("| Case |", "| Vault |"))
    assert run(tmp_path)[2].strip() == "glossary: Vault: stands twice"


def test_no_glossary_page_and_no_terms_section_are_errors(tmp_path):
    seed(tmp_path)
    (tmp_path / "vault" / "wiki" / "entities" / "entity-glossary.md").unlink()
    assert run(tmp_path)[2].strip() == "glossary: no live entity-glossary page"
    seed(tmp_path, GLOSSARY_PAGE.replace("## Terms", "## Words"))
    assert run(tmp_path)[2].strip() == "glossary: entity-glossary has no ## Terms section"


def test_the_cli_knows_the_command(monkeypatch, tmp_path):
    from guppi import cli

    seed(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["glossary"]) == 0
    assert rendered(tmp_path) == EXPECTED


# --- `--check` (case 306.5) ---------------------------------------------------------------


def test_check_names_a_drifted_file_and_writes_nothing(tmp_path):
    seed(tmp_path)
    code, out, err = run(tmp_path, "--check")
    assert (code, err) == (1, "")
    assert out.strip() == "glossary: vault/wiki/glossary.md differs from entity-glossary"
    assert rendered(tmp_path) == "# Glossary\n\nby hand\n"


def test_check_is_silent_on_the_rendered_file(tmp_path):
    seed(tmp_path)
    assert run(tmp_path) == (0, "", "")
    assert run(tmp_path, "--check") == (0, "", "")


# --- the tick of the `guppi glossary` lines (case 306.6) ----------------------------------


GLOSSARY_SPEC = """# Spec

## Case 5 — x

```tasks
- [ ] update `entity-glossary`: one row
- [ ] `uv run --project .guppi guppi glossary`: `vault/wiki/glossary.md`
- [ ] `uv run --project .guppi guppi sprint` at the librarian's run
- [ ] read `estimate-glossary-ticks-the-spec`: pytest, plus the `guppi glossary` lines of this Spec
```
"""


def raw_unit(tmp_path, unit, applied=True):
    folder = tmp_path / "vault" / "raw" / unit
    folder.mkdir(parents=True)
    entry = {"line": 1, "kind": "update", "slug": "entity-glossary", "case": "5"}
    if applied:
        entry["applied"] = "10:00:00"
    data = {"date": unit.split("/")[0], "entries": [entry], "decisions": []}
    (folder / "materialize.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
    (folder / "spec.md").write_text(GLOSSARY_SPEC, encoding="utf-8", newline="\n")
    return folder / "spec.md"


def test_a_plain_glossary_ticks_its_lines_and_check_ticks_nothing(tmp_path):
    seed(tmp_path)
    spec = raw_unit(tmp_path, "2026-09-22/0014")
    unapplied = raw_unit(tmp_path, "2026-09-22/0100", applied=False)
    assert run(tmp_path, "--check")[0] == 1
    assert spec.read_text(encoding="utf-8") == GLOSSARY_SPEC
    assert run(tmp_path) == (0, "", "")
    text = spec.read_text(encoding="utf-8")
    assert "- [x] `uv run --project .guppi guppi glossary`: `vault/wiki/glossary.md`" in text
    assert "- [ ] update `entity-glossary`: one row" in text
    assert "- [ ] `uv run --project .guppi guppi sprint` at the librarian's run" in text
    assert (
        "- [ ] read `estimate-glossary-ticks-the-spec`: pytest, plus the `guppi glossary`" in text
    )
    assert unapplied.read_text(encoding="utf-8") == GLOSSARY_SPEC
