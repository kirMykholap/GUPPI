"""`guppi materialize`: the ledger and the Spec become one yaml, one entry per record line."""

import io

import yaml

from guppi import materialize

DATE = "2026-09-10"

LEDGER = """<!-- a comment line -->
- decision[case 1][create][rule-root]{tags:harness}
- 10:00:00 decision[case 2][create][rule-child]{ref:rule-root}{tags:harness,workflow}
- 10:00:00 decision[case 2][create][estimate-child-works]{ref:rule-child}{tags:harness,workflow}
- 10:00:01 decision[case 3][update][rule-old]
- 10:00:02 decision[case 4][delete][rule-gone]
- 10:00:03 decision[case 5][defer][rule-later]
- 10:00:04 decision[case 6][update][rule-old]{supersedes:case 3}
- 10:00:05 estimate[estimate-child-works][passed] twelve tests green
- 10:00:06 estimate[estimate-old-holds][failed] the reading was red
- 10:00:07 lesson[error][lesson-hooks-late-fire]{tags:hooks} trigger: the hook fired late root_cause: the matcher was wrong
- 10:00:08 decision[case 7][update][glossary]
- this line is not a record
"""

SPEC = """# Spec

## Case 1 — the root

> **context:**
> A root MOC.

> **problem:**
> None yet.

> **given:**
> Nothing exists.

> **then:**
> The root exists.

```then
create:
  - slug: rule-root
    type: rule
    kind: MOC
    purpose: Prevents nothing yet
    children: []
    tags: [harness]
```

## Case 2 — the child

> **context:**
> A Leaf under the root.

> **problem:**
> The root has no child.

> **given:**
> The root exists.

```then
create:
  - slug: rule-child
    type: rule
    kind: Leaf
    purpose: Prevents the child from being missing
    enforcement: check
    implementation_ref: [guppi/child.py]
    tags: [harness, workflow]
    sections:
      Purpose: |
        Two lines of
        purpose.
    estimate:
      slug: estimate-child-works
      kind: QA
      context: "Why: it matters"
      criterion: the child works
      method: pytest in tests/test_child.py
```

## Case 3 — an update

> **context:**
> Words change.

> **problem:**
> Old words.

> **given:**
> The page says old.

> **then:**
> The page says new.

```then
update:
  - slug: rule-old
    set: {tags: [harness, git]}
    sections:
      Purpose: |
        New purpose text.
    replace:
      - old: "old words"
        new: "new words"
    change: old words become new words
```

## Case 5 — a defer

```then
defer:
  - slug: rule-later
    type: rule
    purpose: Prevents something, later
```

## Case 7 — glossary

```then
update:
  - slug: glossary
    file: vault/wiki/glossary.md
    change: a row changes
new_tags:
  - tag: git
    meaning: the repository
    aliases: гит
```
"""


def seed(tmp_path, ledger=LEDGER, spec=SPEC):
    raw = tmp_path / "vault" / "raw" / DATE
    raw.mkdir(parents=True)
    (raw / "ledger.md").write_text(ledger, encoding="utf-8", newline="\n")
    (raw / "spec.md").write_text(spec, encoding="utf-8", newline="\n")
    wiki = tmp_path / "vault" / "wiki"
    (wiki / "rules").mkdir(parents=True)
    (wiki / "sprint.md").write_text("# Sprint\n\n## migration — open\n", encoding="utf-8")
    (wiki / "rules" / "rule-old.md").write_text("---\ntype: rule\n---\n", encoding="utf-8")
    return tmp_path


def run(project_dir, argv=()):
    out, err = io.StringIO(), io.StringIO()
    code = materialize.run(
        list(argv) + ["--date", DATE], stdout=out, stderr=err, project_dir=project_dir
    )
    return code, out.getvalue(), err.getvalue()


def load(project_dir):
    return yaml.safe_load(
        (project_dir / "vault" / "raw" / DATE / "materialize.yaml").read_text(encoding="utf-8")
    )


def by_slug(data, slug, kind=None):
    return [e for e in data["entries"] if e["slug"] == slug and (kind is None or e["kind"] == kind)]


def test_one_entry_per_record_line_in_ledger_order(tmp_path):
    seed(tmp_path)
    code, out, err = run(tmp_path)
    assert code == 0 and err == ""
    data = load(tmp_path)
    assert data["date"] == DATE and data["sprint"] == "migration"
    lines = [e["line"] for e in data["entries"]]
    assert lines == sorted(lines)
    assert [e["kind"] for e in data["entries"]] == [
        "create",
        "create",
        "create",
        "update",
        "delete",
        "defer",
        "update",
        "estimate",
        "lesson",
        "update",
    ]
    first = data["entries"][0]
    assert first["case"] == "1" and first["category"] == "rules" and first["slug"] == "rule-root"
    assert first["origin"] == f"raw/{DATE}/ledger.md#case-1" and first["line"] == 2
    assert first["text"].startswith("decision[case 1]") and first["decision"] == "decision-case-1"
    assert first["tags"] == ["harness"] and first["fields"]["kind"] == "MOC"
    assert "materialize.yaml written with 11 entries" in out


def test_the_nested_estimate_is_its_own_create_entry(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    (entry,) = by_slug(load(tmp_path), "estimate-child-works", "create")
    assert entry["ref"] == "rule-child" and entry["category"] == "estimates"
    assert entry["fields"] == {"type": "estimate", "kind": "QA"}
    assert entry["sections"] == {
        "Context": "Why: it matters",
        "Criterion": "the child works",
        "Method": "pytest in tests/test_child.py",
    }
    assert entry["tags"] == ["harness", "workflow"]
    (child,) = by_slug(load(tmp_path), "rule-child")
    assert child["ref"] == "rule-root" and child["sections"]["Purpose"].startswith("Two lines")


def test_estimate_lines_fold_into_this_ledgers_create_or_become_an_entry(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    (create,) = by_slug(data, "estimate-child-works", "create")
    assert create["status"] == "passed" and create["result"] == "twelve tests green"
    assert by_slug(data, "estimate-child-works", "estimate") == []
    (old,) = by_slug(data, "estimate-old-holds", "estimate")
    assert old["status"] == "failed" and old["result"] == "the reading was red"
    assert old["origin"] == f"raw/{DATE}/ledger.md#L10"


def test_a_supersedes_chain_marks_the_earlier_entry(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    earlier, later = by_slug(data, "rule-old", "update")
    assert earlier["case"] == "3" and earlier["superseded_by"] == "6"
    assert later["supersedes"] == "3" and "superseded_by" not in later
    assert earlier["set"] == {"tags": ["harness", "git"]}
    assert earlier["replace"] == [{"old": "old words", "new": "new words"}]
    assert earlier["change"] == "old words become new words"
    decisions = {d["case"]: d for d in data["decisions"]}
    assert decisions["6"]["supersedes"] == ["decision-case-3"]
    assert decisions["3"]["superseded_by"] == ["decision-case-6"]


def test_a_lesson_line_is_a_create_with_its_text_and_line_origin(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    (lesson,) = by_slug(load(tmp_path), "lesson-hooks-late-fire")
    assert lesson["kind"] == "lesson" and lesson["category"] == "lessons"
    assert lesson["fields"] == {
        "type": "lesson",
        "kind": "error",
        "root_cause": "the matcher was wrong",
    }
    assert lesson["sections"] == {
        "Trigger": "the hook fired late",
        "Root cause": "the matcher was wrong",
    }
    assert lesson["tags"] == ["hooks"] and lesson["origin"] == f"raw/{DATE}/ledger.md#L11"


def test_unparsable_lines_incomplete_creates_and_existing_pages_are_marked(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    assert data["unparsed"] == [{"line": 13, "text": "this line is not a record"}]
    (gone,) = by_slug(data, "rule-gone")
    assert gone["incomplete"] == ["then"]
    (later,) = by_slug(data, "rule-later")
    assert later["fields"] == {"type": "rule", "purpose": "Prevents something, later"}
    assert later["exists"] is False
    (root,) = by_slug(data, "rule-root")
    assert "exists" not in root
    (tmp_path / "vault" / "wiki" / "rules" / "rule-root.md").write_text("---\ntype: rule\n---\n")
    (tmp_path / "vault" / "raw" / DATE / "materialize.yaml").unlink()
    run(tmp_path)
    (root,) = by_slug(load(tmp_path), "rule-root")
    assert root["exists"] is True


def test_a_rule_class_slug_routes_to_a_file_and_new_tags_are_kept(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    (glossary,) = by_slug(data, "glossary")
    assert glossary["category"] == "file" and glossary["path"] == "vault/wiki/glossary.md"
    assert data["new_tags"] == [{"tag": "git", "meaning": "the repository", "aliases": "гит"}]


def test_one_decision_entry_per_case_with_case_text_and_targets(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    decisions = {d["case"]: d for d in load(tmp_path)["decisions"]}
    assert set(decisions) == {"1", "2", "3", "4", "5", "6", "7"}
    two = decisions["2"]
    assert two["decision"] == "decision-case-2" and two["origin"] == f"raw/{DATE}/ledger.md#case-2"
    assert two["targets"] == [
        {"kind": "create", "category": "rules", "slug": "rule-child", "ref": "rule-root"},
        {
            "kind": "create",
            "category": "estimates",
            "slug": "estimate-child-works",
            "ref": "rule-child",
        },
    ]
    assert two["tags"] == ["harness", "workflow"]
    assert decisions["1"]["case_text"] == {
        "context": "A root MOC.",
        "problem": "None yet.",
        "given": "Nothing exists.",
        "then": "The root exists.",
    }
    assert "incomplete" not in decisions["1"]
    assert decisions["4"]["incomplete"] == ["context", "problem", "given", "then"]
    assert decisions["7"]["targets"][0]["path"] == "vault/wiki/glossary.md"


def test_an_existing_yaml_gains_only_the_new_lines(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    path = tmp_path / "vault" / "raw" / DATE / "materialize.yaml"
    data = load(tmp_path)
    (root,) = by_slug(data, "rule-root")
    root["kind"] = "update"  # the librarian's judgment
    root["applied"] = "10:30:00"
    (create,) = by_slug(data, "estimate-child-works", "create")
    create["applied"] = "10:30:00"
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    ledger = tmp_path / "vault" / "raw" / DATE / "ledger.md"
    ledger.write_text(
        LEDGER
        + "- 11:00:00 estimate[estimate-child-works][failed] broke later\n"
        + "- 11:00:01 decision[case 8][update][rule-root]{supersedes:case 1}\n",
        encoding="utf-8",
        newline="\n",
    )
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "extended with 2 entries" in out
    data = load(tmp_path)
    root, late_root = by_slug(data, "rule-root")
    assert root["kind"] == "update" and root["applied"] == "10:30:00"
    assert root["superseded_by"] == "8" and late_root["case"] == "8"
    assert len(data["entries"]) == 12
    (late,) = by_slug(data, "estimate-child-works", "estimate")
    assert late["status"] == "failed" and late["line"] == 14
    assert {d["case"] for d in data["decisions"]} == {"1", "2", "3", "4", "5", "6", "7", "8"}


def test_an_entry_the_librarian_appended_has_no_line_and_is_kept(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    path = tmp_path / "vault" / "raw" / DATE / "materialize.yaml"
    data = load(tmp_path)
    data["entries"].append(
        {
            "kind": "create",
            "category": "insights",
            "slug": "insight-x",
            "fields": {"pattern": "p"},
            "librarian": "synthesis",
            "applied": "10:30:00",
        }
    )
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    ledger = tmp_path / "vault" / "raw" / DATE / "ledger.md"
    ledger.write_text(
        LEDGER + "- 11:00:00 lesson[error][lesson-y-z] trigger: t root_cause: r\n",
        encoding="utf-8",
        newline="\n",
    )
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "extended with 1 entries" in out
    data = load(tmp_path)
    (insight,) = by_slug(data, "insight-x")
    assert "line" not in insight and insight["applied"] == "10:30:00"
    assert by_slug(data, "lesson-y-z")


def test_a_changed_line_is_reported_and_left_alone(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    ledger = tmp_path / "vault" / "raw" / DATE / "ledger.md"
    ledger.write_text(
        LEDGER.replace("[rule-root]{tags:harness}", "[rule-root]{tags:git}"), encoding="utf-8"
    )
    code, _, err = run(tmp_path)
    assert code == 0 and "line 2 changed" in err
    (root,) = by_slug(load(tmp_path), "rule-root")
    assert root["tags"] == ["harness"]


def test_a_missing_ledger_is_an_error(tmp_path):
    (tmp_path / "vault" / "wiki").mkdir(parents=True)
    code, _, err = run(tmp_path)
    assert code == 1 and "does not exist" in err


def test_cli_dispatches_to_materialize(tmp_path, monkeypatch, capsys):
    from guppi import cli

    seed(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["materialize", "--date", DATE]) == 0
    assert "written with" in capsys.readouterr().out


EARLIER = "2026-09-09"


def seed_earlier(tmp_path):
    raw = tmp_path / "vault" / "raw" / EARLIER
    raw.mkdir(parents=True)
    (raw / "ledger.md").write_text(
        "- decision[case 1][create][rule-early]{tags:harness}\n", encoding="utf-8", newline="\n"
    )
    return raw


def run_walk(project_dir, argv=()):
    out, err = io.StringIO(), io.StringIO()
    code = materialize.run(list(argv), stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue(), err.getvalue()


def test_without_date_every_folder_with_a_ledger_is_walked_in_date_order(tmp_path):
    seed(tmp_path)
    seed_earlier(tmp_path)
    (tmp_path / "vault" / "raw" / "notes").mkdir()  # no ledger: not a date to walk
    code, out, err = run_walk(tmp_path)
    assert code == 0 and err == ""
    lines = out.splitlines()
    assert [line.split()[1] for line in lines] == [
        f"vault/raw/{EARLIER}/materialize.yaml",
        f"vault/raw/{DATE}/materialize.yaml",
    ]
    assert (tmp_path / "vault" / "raw" / EARLIER / "materialize.yaml").exists()
    assert load(tmp_path)["date"] == DATE
    # a later run picks up a line written after the earlier date's yaml was closed
    with (tmp_path / "vault" / "raw" / EARLIER / "ledger.md").open("a", encoding="utf-8") as f:
        f.write("- estimate[estimate-early-holds][passed] read later\n")
    code, out, _ = run_walk(tmp_path)
    assert code == 0
    assert out.splitlines()[0].endswith("extended with 1 entries")
    assert out.splitlines()[1].endswith("extended with 0 entries")


def test_with_date_only_that_folder_is_read(tmp_path):
    seed(tmp_path)
    seed_earlier(tmp_path)
    code, out, _ = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and len(out.splitlines()) == 1
    assert not (tmp_path / "vault" / "raw" / EARLIER / "materialize.yaml").exists()


def test_an_error_on_one_date_stops_the_walk_with_exit_1(tmp_path):
    seed(tmp_path)
    raw = seed_earlier(tmp_path)
    (raw / "materialize.yaml").mkdir()  # the yaml cannot be written
    code, out, err = run_walk(tmp_path)
    assert code == 1 and out == ""
    assert err.startswith("materialize: materialize.yaml not written")
    assert not (tmp_path / "vault" / "raw" / DATE / "materialize.yaml").exists()
