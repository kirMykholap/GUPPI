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

> **when:**
> Someone asks.

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
    return [
        e for e in data["entries"] if e.get("slug") == slug and (kind is None or e["kind"] == kind)
    ]


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
        "update",  # the supersedes of case 6 derives nothing (cases 189, 194.1)
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
    assert entry["fields"] == {
        "type": "estimate",
        "kind": "QA",
        "method": "pytest in tests/test_child.py",  # a field since case 194.1
    }
    assert entry["sections"] == {"Criterion": "the child works"}  # written, so kept
    assert entry["tags"] == ["harness", "workflow"]
    assert entry["incomplete"] == ["purpose"]  # the old nested shape names none
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
    # exists only for the page this very line made (case 105.2): the same #case-N in origin
    page = tmp_path / "vault" / "wiki" / "rules" / "rule-root.md"
    page.write_text(f"---\ntype: rule\norigin: raw/{DATE}/ledger.md#case-1\n---\n")
    (tmp_path / "vault" / "raw" / DATE / "materialize.yaml").unlink()
    run(tmp_path)
    (root,) = by_slug(load(tmp_path), "rule-root")
    assert root["exists"] is True
    # a page of another Case, live or archived, leaves the entry a create
    page.write_text("---\ntype: rule\norigin: raw/2026-09-01/ledger.md#case-77\n---\n")
    (tmp_path / "vault" / "raw" / DATE / "materialize.yaml").unlink()
    run(tmp_path)
    (root,) = by_slug(load(tmp_path), "rule-root")
    assert "exists" not in root
    page.unlink()
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-01" / "rules"
    archived.mkdir(parents=True)
    (archived / "rule-root.md").write_text(
        "---\ntype: rule\norigin: raw/2026-09-01/ledger.md#case-77\n---\n"
    )
    (tmp_path / "vault" / "raw" / DATE / "materialize.yaml").unlink()
    run(tmp_path)
    (root,) = by_slug(load(tmp_path), "rule-root")
    assert "exists" not in root
    (archived / "rule-root.md").write_text(
        f"---\ntype: rule\norigin: raw/{DATE}/ledger.md#case-1\n---\n"
    )
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


def test_a_rule_class_item_with_file_and_no_slug_is_found(tmp_path):  # case 161
    spec = SPEC.replace(
        "  - slug: glossary\n    file: vault/wiki/glossary.md\n",
        "  - file: vault/wiki/glossary.md\n",
    )
    assert spec != SPEC
    seed(tmp_path, spec=spec)
    run(tmp_path)
    (glossary,) = by_slug(load(tmp_path), "glossary")
    assert "incomplete" not in glossary
    assert glossary["category"] == "file" and glossary["path"] == "vault/wiki/glossary.md"
    assert glossary["change"] == "a row changes"


def test_claude_md_is_not_a_rule_class_file(tmp_path):  # case 59.8
    ledger = "- decision[case 8][update][claude-md]{ref:claude-md}\n"
    spec = "## Case 8 — the prompt\n\n```then\nupdate:\n  - slug: claude-md\n    change: a\n```\n"
    seed(tmp_path, ledger=ledger, spec=spec)
    run(tmp_path)
    assert materialize.rule_class_path("claude-md") is None
    (entry,) = by_slug(load(tmp_path), "claude-md")
    assert entry["category"] == "unknown" and "path" not in entry
    assert entry["incomplete"] == ["category"]


SUB_LEDGER = """- decision[case 9.1][update][rule-old]
- decision[case 9.2][update][rule-old]
- decision[case 9.3][update][rule-old]
"""

SUB_SPEC = """# Spec

## Case 9 — the parent

> **context:**
> Shared context.

> **problem:**
> Shared problem.

> **recommend:**
> Three sub-cases.

> **given:**
> The parent's given.
> **＋** A second line.

> **when:**
> The parent's when.

### Case 9.1 — inherits given

> **when:**
> The first sub-case's when.

```then
update:
  - slug: rule-old
    change: one
new_tags:
  - tag: git
    meaning: the repository
    aliases: гит
```

### Case 9.2 — its own given

> **given:**
> The second sub-case's given.

> **when:**
> The second sub-case's when.

```then
update:
  - slug: rule-old
    change: two
```

### Case 9.3 — no when

```then
update:
  - slug: rule-old
    change: three
```

## Case 10 — a tag alone

```then
new_tags:
  - tag: tests
    meaning: the harness's own test suite
    aliases: тесты
  - tag: git
    meaning: the repository
    aliases: гит
```
"""


def test_a_sub_case_inherits_a_missing_given_never_when(tmp_path):  # case 60
    seed(tmp_path, ledger=SUB_LEDGER, spec=SUB_SPEC)
    run(tmp_path)
    decisions = {d["case"]: d for d in load(tmp_path)["decisions"]}
    first = decisions["9.1"]
    assert first["case_text"]["given"] == "The parent's given.\n**＋** A second line."
    assert first["case_text"]["when"] == "The first sub-case's when."
    assert first["case_text"]["context"] == "Shared context."
    assert "incomplete" not in first
    assert decisions["9.2"]["case_text"]["given"] == "The second sub-case's given."
    assert "incomplete" not in decisions["9.2"]
    third = decisions["9.3"]
    assert third["case_text"]["given"] == "The parent's given.\n**＋** A second line."
    assert "when" not in third["case_text"]
    assert third["incomplete"] == ["when"]


def test_new_tags_come_from_every_case_lines_or_none(tmp_path):  # case 61
    seed(tmp_path, ledger=SUB_LEDGER, spec=SUB_SPEC)
    run(tmp_path)
    assert load(tmp_path)["new_tags"] == [
        {"tag": "git", "meaning": "the repository", "aliases": "гит"},
        {"tag": "tests", "meaning": "the harness's own test suite", "aliases": "тесты"},
    ]


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
        "when": "Someone asks.",
        "then": "The root exists.",
    }
    assert "incomplete" not in decisions["1"]
    assert decisions["4"]["incomplete"] == ["context", "problem", "given", "when"]
    assert decisions["5"]["incomplete"] == ["context", "problem"]  # a defer alone: the short form
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


# --- the derived Estimate (case 72.3) -----------------------------------------------

ESTIMATE_LEDGER = """- decision[case 11][create][rule-leaf]{ref:rule-root}{tags:harness}
- decision[case 12][update][rule-old]
- decision[case 13][update][rule-old]{supersedes:case 12}
- decision[case 14][update][rule-none]
- decision[case 15][create][entity-cart]
- decision[case 16][create][estimate-cart-alone]{ref:entity-cart}{tags:cart}
- decision[case 17][update][estimate-old-holds]{ref:estimate-old-holds}
- decision[case 18][update][estimate-old-second]{ref:estimate-old-second}
- decision[case 19][create][estimate-cart-written]{ref:entity-cart}{tags:cart}
- decision[case 20][create][estimate-cart-bare]{ref:entity-cart}{tags:cart}
"""

ESTIMATE_SPEC = """# Spec

## Case 11 — a Leaf with the old method key

> **context:**
> A Leaf.

> **problem:**
> The Leaf has no check.

> **given:**
> The root exists.

> **when:**
> The check runs.
> **＋** Twice.

> **then:**
> It passes.
> **－** Never on Sunday.

```then
create:
  - slug: rule-leaf
    type: rule
    kind: Leaf
    purpose: Prevents the check from being missing
    enforcement: check
    implementation_ref: [guppi/leaf.py]
    tags: [harness]
    method: pytest in tests/test_leaf.py
```

## Case 12 — an update with the old contract keys

> **context:**
> Old words.

> **problem:**
> The contract moves.

> **given:**
> The page says old.

> **when:**
> The page is read.

> **then:**
> It says new.

```then
update:
  - slug: rule-old
    contract: changed
    estimate_slug: estimate-old-holds
    method: the new way
    replace:
      - old: old words
        new: new words
    change: the contract changes
```

## Case 13 — the same page, superseding 12

> **context:**
> Words again.

> **problem:**
> Only words.

> **given:**
> The page says new.

> **when:**
> The page is read.

> **then:**
> It says newer.

```then
update:
  - slug: rule-old
    contract: same
    change: newer words
```

## Case 14 — a change on a page that does not exist

> **when:**
> Something.

> **then:**
> Something else.

```then
update:
  - slug: rule-none
    contract: changed
    change: a change without an Estimate
```

## Case 15 — an entity with the old estimate keys

> **context:**
> A cart.

> **problem:**
> No cart yet.

> **given:**
> Nothing.

```then
create:
  - slug: entity-cart
    type: entity
    kind: MOC
    purpose: Lets a buyer review an order
    tags: [cart]
    method: measure by hand
    estimate_slug: estimate-cart-renders
    estimate_kind: Research
```

## Case 16 — an Estimate whose Criterion is the Case

> **context:**
> The cart.

> **problem:**
> Nobody measured it.

> **given:**
> A seeded database.
> **＋** Three sizes.

> **when:**
> A buyer opens the cart.

> **then:**
> It renders in time.
> **－** Not above 120 items.

```then
create:
  - slug: estimate-cart-alone
    type: estimate
    kind: QA
    purpose: The cart renders in time
    method: m
    context: c
    tags: [cart]
```

## Case 17 — an Estimate update lifted from the Case

> **given:**
> The page says old.

> **when:**
> The page is read.

> **then:**
> It says new.

```then
update:
  - slug: estimate-old-holds
    change: the Criterion replaced whole
```

### Case 17.1 — a sub-case without a given of its own

> **when:**
> The page is read twice.

> **then:**
> It says new twice.

```then
update:
  - slug: estimate-old-holds
    change: twice
```

## Case 18 — an Estimate update with a written Criterion

> **given:**
> Something.

> **when:**
> Something.

> **then:**
> Something else.

```then
update:
  - slug: estimate-old-second
    sections:
      Criterion: |
        When:
        The written one.
    set: {status: failed}
    change: the written Criterion stands
```

## Case 19 — an Estimate create with a written Criterion

> **when:**
> The lifted one would say this.

> **then:**
> And this.

```then
create:
  - slug: estimate-cart-written
    type: estimate
    kind: QA
    purpose: A written promise
    method: m
    sections:
      Criterion: |
        When:
        The written one.
```

## Case 20 — an Estimate create with nothing to lift

```then
create:
  - slug: estimate-cart-bare
    type: estimate
    kind: QA
    method: m
```
"""

CRITERION_16 = (
    "Given:\nA seeded database.\n**＋** Three sizes.\n\n"
    "When:\nA buyer opens the cart.\n\n"
    "Then:\nIt renders in time.\n**－** Not above 120 items."
)


def seed_estimates(tmp_path):
    seed(tmp_path, ledger=ESTIMATE_LEDGER, spec=ESTIMATE_SPEC)
    rules = tmp_path / "vault" / "wiki" / "rules"
    (rules / "rule-old.md").write_text(
        "---\ntype: rule\nkind: Leaf\nestimates: [estimate-old-holds, estimate-old-second]\n---\n",
        encoding="utf-8",
    )
    return tmp_path


def of_case(data, case):
    return [e for e in data["entries"] if e.get("case") == case]


# --- no Estimate is derived (cases 189, 194.1): `estimate-materialize-assembles` -------


def test_a_create_with_the_old_method_key_yields_no_estimate_and_keeps_the_key_off(tmp_path):
    seed_estimates(tmp_path)
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "written with 10 entries" in out  # one per line
    data = load(tmp_path)
    (leaf,) = of_case(data, "11")
    assert leaf["slug"] == "rule-leaf" and leaf["kind"] == "create"
    assert "method" not in leaf["fields"] and leaf["fields"]["kind"] == "Leaf"
    assert "incomplete" not in leaf
    assert by_slug(data, "estimate-leaf") == []
    (cart,) = of_case(data, "15")  # estimate_slug and estimate_kind ignored the same way
    assert cart["fields"] == {
        "type": "entity",
        "kind": "MOC",
        "purpose": "Lets a buyer review an order",
        "tags": ["cart"],
    }
    assert "incomplete" not in cart and by_slug(data, "estimate-cart-renders") == []


def test_an_update_with_the_old_contract_keys_yields_one_entry_without_them(tmp_path):
    seed_estimates(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    (update,) = of_case(data, "12")
    assert update["slug"] == "rule-old" and update["kind"] == "update"
    assert set(update) & {"contract", "method", "estimate_slug", "fields"} == set()
    assert update["replace"] == [{"old": "old words", "new": "new words"}]
    assert "incomplete" not in update and update["superseded_by"] == "13"
    assert by_slug(data, "estimate-old-holds", "update") == [of_case(data, "17")[0]]
    for case in ("13", "14"):  # contract: same, and contract: changed with no page
        (only,) = of_case(data, case)
        assert only["kind"] == "update" and "incomplete" not in only


def test_a_supersedes_yields_no_removal_and_marks_the_earlier_entries(tmp_path):
    seed_estimates(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    assert [e["kind"] for e in data["entries"]] == [
        "create",
        "update",
        "update",
        "update",
        "create",
        "create",
        "update",
        "update",
        "create",
        "create",
    ]
    assert not any(e.get("derived") or e.get("case_removed") for e in data["entries"])
    (thirteen,) = of_case(data, "13")
    assert thirteen["supersedes"] == "12"
    assert {e["case"] for e in data["entries"] if e.get("superseded_by")} == {"12"}


def test_an_estimate_create_lifts_its_criterion_from_the_case(tmp_path):
    seed_estimates(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    (alone,) = of_case(data, "16")
    assert alone["slug"] == "estimate-cart-alone" and alone["ref"] == "entity-cart"
    assert alone["category"] == "estimates" and alone["tags"] == ["cart"]
    assert alone["fields"] == {
        "type": "estimate",
        "kind": "QA",
        "purpose": "The cart renders in time",
        "method": "m",  # a field, not a section (case 194.1)
        "tags": ["cart"],
    }
    assert alone["sections"] == {"Criterion": CRITERION_16}  # no Context, no Method
    assert "incomplete" not in alone and "set" not in alone


def test_an_estimate_update_lifts_its_criterion_and_goes_pending(tmp_path):
    seed_estimates(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    (update,) = of_case(data, "17")
    assert update["slug"] == "estimate-old-holds" and update["kind"] == "update"
    assert update["sections"] == {
        "Criterion": "Given:\nThe page says old.\n\nWhen:\nThe page is read.\n\nThen:\nIt says new."
    }
    assert update["set"] == {"status": "pending"}
    assert update["change"] == "the Criterion replaced whole"
    assert "incomplete" not in update and "derived" not in update


def test_a_sub_case_lifts_its_parents_given_into_the_criterion(tmp_path):
    seed_estimates(tmp_path)
    ledger = tmp_path / "vault" / "raw" / DATE / "ledger.md"
    ledger.write_text(
        ESTIMATE_LEDGER
        + "- decision[case 17.1][update][estimate-old-holds]{ref:estimate-old-holds}\n",
        encoding="utf-8",
        newline="\n",
    )
    run(tmp_path)
    (_, sub) = by_slug(load(tmp_path), "estimate-old-holds", "update")
    assert sub["case"] == "17.1"
    assert sub["sections"]["Criterion"] == (
        "Given:\nThe page says old.\n\nWhen:\nThe page is read twice.\n\nThen:\nIt says new twice."
    )
    assert sub["set"] == {"status": "pending"} and "incomplete" not in sub


def test_a_written_criterion_stands_and_a_written_status_is_kept(tmp_path):
    seed_estimates(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    (update,) = of_case(data, "18")
    assert update["sections"]["Criterion"].strip() == "When:\nThe written one."
    assert update["set"] == {"status": "failed"}
    (create,) = of_case(data, "19")
    assert create["sections"]["Criterion"].strip() == "When:\nThe written one."
    assert create["fields"]["purpose"] == "A written promise" and "incomplete" not in create


def test_an_estimate_create_with_nothing_to_lift_is_incomplete(tmp_path):
    seed_estimates(tmp_path)
    run(tmp_path)
    (bare,) = of_case(load(tmp_path), "20")
    assert "sections" not in bare
    assert bare["incomplete"] == ["purpose", "criterion"]


def test_the_decision_entry_carries_no_criterion_list(tmp_path):
    seed_estimates(tmp_path)
    run(tmp_path)
    decisions = {d["case"]: d for d in load(tmp_path)["decisions"]}
    assert all("criterion" not in d for d in decisions.values())
    assert decisions["11"]["targets"] == [
        {"kind": "create", "category": "rules", "slug": "rule-leaf", "ref": "rule-root"}
    ]
    assert decisions["16"]["targets"] == [
        {
            "kind": "create",
            "category": "estimates",
            "slug": "estimate-cart-alone",
            "ref": "entity-cart",
        }
    ]
    assert decisions["13"]["supersedes"] == ["decision-case-12"]


SUPERSEDED_TWICE_SPEC = (
    ESTIMATE_SPEC
    + """
## Case 21 — superseding 13

> **context:**
> Words a third time.

> **problem:**
> Only words.

> **given:**
> The page says newer.

> **when:**
> The page is read.

> **then:**
> It says newest.

```then
update:
  - slug: rule-old
    change: newest words
```
"""
)


def test_a_supersedes_marks_every_entry_of_the_earlier_case(tmp_path):
    # case 13 supersedes 12; case 21 supersedes 13 (case 175)
    seed(
        tmp_path,
        ledger=ESTIMATE_LEDGER + "- decision[case 21][update][rule-old]{supersedes:case 13}\n",
        spec=SUPERSEDED_TWICE_SPEC,
    )
    run(tmp_path)
    data = load(tmp_path)
    (thirteen,) = of_case(data, "13")
    assert thirteen["kind"] == "update" and thirteen["superseded_by"] == "21"
    (mine,) = of_case(data, "21")
    assert mine["supersedes"] == "13"
    marked = {e["case"] for e in data["entries"] if e.get("superseded_by")}
    assert marked == {"12", "13"}  # 12 by 13 as before, 13 by 21; nothing else
    decisions = {d["case"]: d for d in data["decisions"]}
    assert decisions["13"]["superseded_by"] == ["decision-case-21"]


# --- every Spec of the date (case 73.5) ---------------------------------------------

SESSION_LEDGER = """- decision[case 3][update][rule-old]
- decision[case 21][update][rule-old]
- decision[case 22][update][rule-old]
"""


def session_spec(case, change):
    return (
        f"# Spec\n\n## Case {case} — a session\n\n> **context:**\n> Session {case}.\n\n"
        f"```then\nupdate:\n  - slug: rule-old\n    change: {change}\n```\n"
    )


def seed_sessions(tmp_path):
    seed(tmp_path, ledger=SESSION_LEDGER)  # the root spec.md holds Case 3, an older date's
    raw = tmp_path / "vault" / "raw" / DATE
    for folder, case in (("1156", "22"), ("0454", "21")):
        (raw / folder).mkdir()
        (raw / folder / "spec.md").write_text(
            session_spec(case, f"from {folder}"), encoding="utf-8", newline="\n"
        )
    (raw / "notes").mkdir()  # not a session folder: its spec.md is not read
    (raw / "notes" / "spec.md").write_text(session_spec("99", "never"), encoding="utf-8")
    return raw


def test_every_spec_of_the_date_is_read_in_folder_order(tmp_path):
    seed_sessions(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    data = load(tmp_path)
    assert data["spec"] == [
        f"vault/raw/{DATE}/spec.md",
        f"vault/raw/{DATE}/0454/spec.md",
        f"vault/raw/{DATE}/1156/spec.md",
    ]
    assert [e["change"] for e in data["entries"]] == [
        "old words become new words",
        "from 0454",
        "from 1156",
    ]
    decisions = {d["case"]: d for d in data["decisions"]}
    assert decisions["3"]["spec"] == f"vault/raw/{DATE}/spec.md"
    assert decisions["21"]["spec"] == f"vault/raw/{DATE}/0454/spec.md"
    assert decisions["22"]["spec"] == f"vault/raw/{DATE}/1156/spec.md"
    assert decisions["22"]["case_text"]["context"] == "Session 22."
    assert "99" not in decisions


def test_a_case_in_two_specs_stops_the_walk(tmp_path):
    raw = seed_sessions(tmp_path)
    with (raw / "1156" / "spec.md").open("a", encoding="utf-8") as f:
        f.write(session_spec("21", "again").split("\n", 2)[2])
    code, out, err = run(tmp_path)
    assert code == 1 and out == ""
    assert err == (
        f"materialize: Case 21 is in both vault/raw/{DATE}/0454/spec.md"
        f" and vault/raw/{DATE}/1156/spec.md\n"
    )
    assert not (raw / "materialize.yaml").exists()


def test_a_date_without_a_spec_behaves_as_today(tmp_path):
    seed(tmp_path)
    (tmp_path / "vault" / "raw" / DATE / "spec.md").unlink()
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "written with 11 entries" in out
    data = load(tmp_path)
    assert data["spec"] == []
    (root,) = by_slug(data, "rule-root")
    assert root["incomplete"] == ["then"]
    assert all("spec" not in d for d in data["decisions"])


# --- the ledger of a session (case 103.2) -------------------------------------------


def seed_session_unit(tmp_path, folder="1610"):
    """A session folder with its own ledger and Spec beside the date-level shape."""
    raw = seed_sessions(tmp_path)
    (raw / folder).mkdir()
    (raw / folder / "ledger.md").write_text(
        "- 16:20:00 decision[case 30][update][rule-old]\n"
        "- 16:21:00 estimate[estimate-old-holds][passed] read in the session\n",
        encoding="utf-8",
        newline="\n",
    )
    (raw / folder / "spec.md").write_text(
        session_spec("30", f"from {folder}"), encoding="utf-8", newline="\n"
    )
    return raw / folder


def test_a_session_unit_reads_its_own_spec_and_writes_its_own_yaml(tmp_path):
    session = seed_session_unit(tmp_path)
    code, out, err = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and err == ""
    assert [line.split()[1] for line in out.splitlines()] == [
        f"vault/raw/{DATE}/materialize.yaml",
        f"vault/raw/{DATE}/1610/materialize.yaml",
    ]
    data = yaml.safe_load((session / "materialize.yaml").read_text(encoding="utf-8"))
    assert data["date"] == DATE and data["session"] == "1610"
    assert data["ledger"] == f"vault/raw/{DATE}/1610/ledger.md"
    assert data["spec"] == [f"vault/raw/{DATE}/1610/spec.md"]
    update, reading = data["entries"]
    assert update["origin"] == f"raw/{DATE}/1610/ledger.md#case-30"
    assert update["change"] == "from 1610"
    assert reading["origin"] == f"raw/{DATE}/1610/ledger.md#L2"
    (decision,) = data["decisions"]
    assert decision["origin"] == f"raw/{DATE}/1610/ledger.md#case-30"
    assert decision["spec"] == f"vault/raw/{DATE}/1610/spec.md"
    # the date-level unit still reads the Specs of the date and keeps the date form
    date_level = load(tmp_path)
    assert "session" not in date_level
    assert f"vault/raw/{DATE}/1610/spec.md" in date_level["spec"]
    assert date_level["entries"][0]["origin"] == f"raw/{DATE}/ledger.md#case-3"


def test_the_walk_takes_the_date_level_unit_first_then_the_sessions(tmp_path):
    seed_session_unit(tmp_path)
    seed_earlier(tmp_path)
    assert materialize.units_with(tmp_path, "ledger.md") == [EARLIER, DATE, f"{DATE}/1610"]
    code, out, _ = run_walk(tmp_path)
    assert code == 0
    assert [line.split()[1] for line in out.splitlines()] == [
        f"vault/raw/{EARLIER}/materialize.yaml",
        f"vault/raw/{DATE}/materialize.yaml",
        f"vault/raw/{DATE}/1610/materialize.yaml",
    ]


def test_a_session_unit_alone_is_a_unit_of_its_own(tmp_path):
    session = seed_session_unit(tmp_path)
    (tmp_path / "vault" / "raw" / DATE / "ledger.md").unlink()
    assert materialize.units_with(tmp_path, "ledger.md", DATE) == [f"{DATE}/1610"]
    code, out, err = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and err == "" and len(out.splitlines()) == 1
    assert (session / "materialize.yaml").exists()
    assert not (tmp_path / "vault" / "raw" / DATE / "materialize.yaml").exists()


# --- --show (case 76) ---------------------------------------------------------------


def test_show_prints_the_yaml_and_writes_nothing(tmp_path):
    seed(tmp_path)
    raw = tmp_path / "vault" / "raw" / DATE
    before = sorted(p.name for p in raw.iterdir())
    code, out, err = run(tmp_path, ["--show"])
    assert code == 0 and err == ""
    assert sorted(p.name for p in raw.iterdir()) == before
    shown = yaml.safe_load(out)
    assert shown["date"] == DATE and shown["unparsed"] == [
        {"line": 13, "text": "this line is not a record"}
    ]
    assert "materialize.yaml" not in out.splitlines()[0]
    code, out, _ = run(tmp_path)
    assert code == 0 and "written with 11 entries" in out
    assert load(tmp_path) == shown
    # an applied entry of an existing yaml is shown as it is, the new lines beside it
    data = load(tmp_path)
    (root,) = by_slug(data, "rule-root")
    root["applied"] = "10:30:00"
    (raw / "materialize.yaml").write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    with (raw / "ledger.md").open("a", encoding="utf-8") as f:
        f.write("- 11:00:00 lesson[error][lesson-y-z] trigger: t root_cause: r\n")
    stamp = (raw / "materialize.yaml").read_text(encoding="utf-8")
    code, out, err = run(tmp_path, ["--show"])
    assert code == 0 and err == ""
    shown = yaml.safe_load(out)
    assert by_slug(shown, "rule-root")[0]["applied"] == "10:30:00" and by_slug(shown, "lesson-y-z")
    assert (raw / "materialize.yaml").read_text(encoding="utf-8") == stamp


def test_show_walks_every_date_one_document_each(tmp_path):
    seed(tmp_path)
    seed_earlier(tmp_path)
    code, out, err = run_walk(tmp_path, ["--show"])
    assert code == 0 and err == ""
    docs = list(yaml.safe_load_all(out))
    assert [d["date"] for d in docs] == [EARLIER, DATE]
    assert "\n---\n" in out
    assert not (tmp_path / "vault" / "raw" / EARLIER / "materialize.yaml").exists()
    assert not (tmp_path / "vault" / "raw" / DATE / "materialize.yaml").exists()


def test_show_exits_1_on_an_error_as_without_it(tmp_path):
    seed(tmp_path)
    raw = seed_earlier(tmp_path)
    (raw / "materialize.yaml").mkdir()  # the yaml cannot be read
    code, out, err = run_walk(tmp_path, ["--show"])
    assert code == 1 and out == ""
    assert err.startswith("materialize: materialize.yaml not written")
    code, _, err = run(tmp_path / "elsewhere", ["--show"])  # no ledger at all
    assert code == 1 and "does not exist" in err


def test_a_lesson_line_carries_the_source_of_its_braces(tmp_path):
    seed(tmp_path)
    raw = tmp_path / "vault" / "raw" / DATE
    with (raw / "ledger.md").open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(
            "- 11:00:00 lesson[knowledge][lesson-k-with]{tags:hooks}{source:a live probe} "
            "trigger: t root_cause: r\n"
            "- 11:00:01 lesson[knowledge][lesson-k-without]{tags:hooks} trigger: t root_cause: r\n"
            "- 11:00:02 lesson[error][lesson-e-with]{tags:hooks}{source:a live probe} "
            "trigger: t root_cause: r\n"
        )
    run(tmp_path)
    data = load(tmp_path)
    (with_source,) = by_slug(data, "lesson-k-with")
    assert with_source["fields"]["source"] == "a live probe"
    assert "incomplete" not in with_source
    (without,) = by_slug(data, "lesson-k-without")
    assert "source" not in without["fields"] and without["incomplete"] == ["source"]
    (error,) = by_slug(data, "lesson-e-with")  # an error lesson keeps a source it was given
    assert error["fields"]["source"] == "a live probe" and "incomplete" not in error


# --- a supersedes reaches another unit's yaml (case 130.2) --------------------------------


def seed_two_units(tmp_path):
    """Unit A, `<date>/0900`, with a yaml holding an unapplied entry of case 5; unit B,
    `<date>/1600`, with a ledger whose line supersedes case 5."""
    raw = tmp_path / "vault" / "raw" / DATE
    (tmp_path / "vault" / "wiki" / "rules").mkdir(parents=True)
    (tmp_path / "vault" / "wiki" / "sprint.md").write_text(
        "# Sprint\n\n## migration — open\n", encoding="utf-8"
    )
    a = raw / "0900"
    a.mkdir(parents=True)
    (a / "ledger.md").write_text(
        "- 09:10:00 decision[case 5][update][rule-old]{ref:rule-old}\n",
        encoding="utf-8",
        newline="\n",
    )
    (a / "spec.md").write_text(session_spec("5", "the old words"), encoding="utf-8", newline="\n")
    b = raw / "1600"
    b.mkdir()
    (b / "ledger.md").write_text(
        "- 16:10:00 decision[case 9][update][rule-old]{ref:rule-old}{supersedes:case 5}\n",
        encoding="utf-8",
        newline="\n",
    )
    (b / "spec.md").write_text(session_spec("9", "the new words"), encoding="utf-8", newline="\n")
    return a, b


def unit_yaml(folder):
    return yaml.safe_load((folder / "materialize.yaml").read_text(encoding="utf-8"))


def test_a_supersedes_marks_the_earlier_entry_in_another_units_yaml(tmp_path):
    from guppi import archive

    a, b = seed_two_units(tmp_path)
    code, _, err = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and err == ""
    before = unit_yaml(a)
    (entry,) = [e for e in before["entries"] if e.get("case") == "5"]
    assert entry["superseded_by"] == "9" and "applied" not in entry
    (decision,) = before["decisions"]
    assert decision["superseded_by"] == ["decision-case-9"]
    assert archive.kept_reason(tmp_path, f"{DATE}/0900") is None
    later = unit_yaml(b)
    (mine,) = [e for e in later["entries"] if e.get("case") == "9" and e.get("kind") == "update"]
    assert mine["supersedes"] == "5" and "superseded_by" not in mine
    # the rest of A is untouched: a second walk changes nothing
    text_a = (a / "materialize.yaml").read_text(encoding="utf-8")
    code, _, err = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and err == ""
    assert (a / "materialize.yaml").read_text(encoding="utf-8") == text_a


def test_a_supersedes_of_a_case_no_yaml_holds_changes_nothing(tmp_path):
    a, b = seed_two_units(tmp_path)
    (a / "ledger.md").write_text(
        "- 09:10:00 decision[case 4][update][rule-old]{ref:rule-old}\n",
        encoding="utf-8",
        newline="\n",
    )
    (a / "spec.md").write_text(session_spec("4", "other"), encoding="utf-8", newline="\n")
    code, _, err = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and err == ""
    assert all("superseded_by" not in e for e in unit_yaml(a)["entries"])
    (mine,) = [
        e for e in unit_yaml(b)["entries"] if e.get("case") == "9" and e.get("kind") == "update"
    ]
    assert mine["supersedes"] == "5"


# --- a carried-over unit is passed by (case 190.3) ----------------------------------------
# `estimate-materialize-skips-a-carried-over-unit`


def test_a_unit_holding_carry_md_is_passed_by_with_one_line(tmp_path):
    a, b = seed_two_units(tmp_path)
    (b / "materialize.yaml").unlink(missing_ok=True)
    (a / "carry.md").write_text("conserved\n", encoding="utf-8")
    code, out, err = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and err == ""
    lines = out.splitlines()
    assert len(lines) == 2
    assert lines[0] == (
        f"materialize: vault/raw/{DATE}/0900/ passed by — carry.md marks its Spec as "
        "ratified and not done"
    )
    assert lines[1].startswith(f"materialize: vault/raw/{DATE}/1600/materialize.yaml written")
    assert not (a / "materialize.yaml").exists()  # not written, not marked from unit B
    assert (b / "materialize.yaml").exists()


def test_a_carried_over_units_yaml_is_not_extended(tmp_path):
    a, _ = seed_two_units(tmp_path)
    run_walk(tmp_path, ["--date", DATE])  # both yamls written, A's entry marked by B
    before = (a / "materialize.yaml").read_text(encoding="utf-8")
    with (a / "ledger.md").open("a", encoding="utf-8", newline="\n") as fh:
        fh.write("- 09:20:00 decision[case 6][update][rule-old]{ref:rule-old}\n")
    (a / "carry.md").write_text("", encoding="utf-8")  # the content is not read
    code, out, _ = run_walk(tmp_path)
    assert code == 0 and "passed by" in out
    assert (a / "materialize.yaml").read_text(encoding="utf-8") == before


def test_show_passes_a_carried_over_unit_by_too(tmp_path):
    a, _ = seed_two_units(tmp_path)
    (a / "carry.md").write_text("conserved\n", encoding="utf-8")
    code, out, _ = run_walk(tmp_path, ["--show"])
    assert code == 0
    assert out.count("passed by") == 1 and out.count("---") == 0  # one document, no separator


def test_without_carry_md_the_unit_is_read_as_before(tmp_path):
    seed_two_units(tmp_path)
    code, out, _ = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and "passed by" not in out
    assert len(out.splitlines()) == 2


# --- an entry fails alone (cases 142.1, 142.4) --------------------------------------------


def test_a_line_whose_lift_raises_fails_alone_and_the_yaml_is_written(tmp_path, monkeypatch):
    seed(tmp_path)

    def boom(record, number, text, date, block, project_dir):
        raise ValueError("odd item")

    monkeypatch.setattr(materialize, "decision_entry", boom)
    code, out, err = run(tmp_path)
    assert code == 1
    assert "materialize: line 2: ValueError: odd item" in err
    assert "written with" in out
    data = load(tmp_path)
    failed = [e for e in data["entries"] if e.get("failed")]
    assert failed and all("kind" not in e for e in failed)
    assert failed[0]["line"] == 2 and failed[0]["text"].startswith("decision[case 1]")
    # the other lines of the ledger are lifted
    assert any(e.get("kind") == "estimate" or e.get("status") for e in data["entries"])


def test_a_failed_line_is_lifted_again_and_replaced_on_the_next_run(tmp_path, monkeypatch):
    seed(tmp_path)
    monkeypatch.setattr(
        materialize, "decision_entry", lambda *a, **k: (_ for _ in ()).throw(ValueError("x"))
    )
    assert run(tmp_path)[0] == 1
    monkeypatch.undo()
    code, _out, err = run(tmp_path)
    assert code == 0 and err == ""
    data = load(tmp_path)
    assert not [e for e in data["entries"] if e.get("failed") and "kind" not in e]
    assert [e for e in data["entries"] if e.get("line") == 2 and e.get("kind") == "create"]


def test_an_entry_the_script_cannot_read_is_left_alone(tmp_path):
    seed(tmp_path)
    assert run(tmp_path)[0] == 0
    path = tmp_path / "vault" / "raw" / DATE / "materialize.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["entries"].append("a bare string")
    data["entries"].append({"note": "a mapping without line or derived"})
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    code, _out, err = run(tmp_path)
    assert code == 0
    assert err.count("an entry the script cannot read is left alone") == 2
    after = load(tmp_path)
    assert {"note": "a mapping without line or derived"} in after["entries"]


def test_a_failed_line_in_one_unit_does_not_stop_the_walk(tmp_path, monkeypatch):
    a, b = seed_two_units(tmp_path)
    calls = {"n": 0}
    real = materialize.decision_entry

    def first_fails(record, number, text, date, block, project_dir):
        calls["n"] += 1
        if calls["n"] == 1:
            raise RuntimeError("first unit")
        return real(record, number, text, date, block, project_dir)

    monkeypatch.setattr(materialize, "decision_entry", first_fails)
    code, _out, err = run_walk(tmp_path, ["--date", DATE])
    assert code == 1
    assert "materialize: line 1: RuntimeError: first unit" in err
    assert (a / "materialize.yaml").exists() and (b / "materialize.yaml").exists()
    assert unit_yaml(a)["entries"][0]["failed"].startswith("RuntimeError")
    assert any(e.get("case") == "9" for e in unit_yaml(b)["entries"])


def test_an_error_of_the_unit_itself_still_stops_the_walk(tmp_path, monkeypatch):
    a, b = seed_two_units(tmp_path)
    real = materialize.read_specs

    def two_files(project_dir, unit):
        if unit.endswith("0900"):
            raise materialize.MaterializeError("Case 5 found in two files")
        return real(project_dir, unit)

    monkeypatch.setattr(materialize, "read_specs", two_files)
    code, _out, err = run_walk(tmp_path, ["--date", DATE])
    assert code == 1 and "Case 5 found in two files" in err
    assert not (a / "materialize.yaml").exists()
    assert not (b / "materialize.yaml").exists()
