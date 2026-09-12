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
        "update",
        "remove_criterion",  # the supersedes of case 6, no line of its own (case 72.3)
        "estimate",
        "lesson",
        "update",
    ]
    first = data["entries"][0]
    assert first["case"] == "1" and first["category"] == "rules" and first["slug"] == "rule-root"
    assert first["origin"] == f"raw/{DATE}/ledger.md#case-1" and first["line"] == 2
    assert first["text"].startswith("decision[case 1]") and first["decision"] == "decision-case-1"
    assert first["tags"] == ["harness"] and first["fields"]["kind"] == "MOC"
    assert "materialize.yaml written with 12 entries" in out


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
    assert code == 0 and err == "" and "extended with 3 entries" in out  # + a remove_criterion
    data = load(tmp_path)
    root, late_root = by_slug(data, "rule-root")
    assert root["kind"] == "update" and root["applied"] == "10:30:00"
    assert root["superseded_by"] == "8" and late_root["case"] == "8"
    assert len(data["entries"]) == 14
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

DERIVED_LEDGER = """- decision[case 11][create][rule-leaf]{ref:rule-root}{tags:harness}
- decision[case 12][update][rule-old]
- decision[case 13][update][rule-old]{supersedes:case 12}
- decision[case 14][update][rule-none]
- decision[case 15][create][entity-cart]
- decision[case 16][create][estimate-cart-alone]{ref:entity-cart}
- decision[case 17][update][rule-empty]
"""

DERIVED_SPEC = """# Spec

## Case 11 — a Leaf with method

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

## Case 12 — a contract change

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
    method: the new way
    replace:
      - old: old words
        new: new words
    change: the contract changes
```

## Case 13 — the same contract, superseding 12

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

## Case 15 — an entity with its own Estimate slug and kind, no when

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

## Case 16 — a standalone estimate

```then
create:
  - slug: estimate-cart-alone
    type: estimate
    kind: QA
    context: c
    criterion: cr
    method: m
    tags: [cart]
```

## Case 17 — a change on a page with no Estimate listed

> **when:**
> Something.

> **then:**
> Something else.

```then
update:
  - slug: rule-empty
    contract: changed
    change: a change without an Estimate
```
"""

CRITERION_11 = (
    "### case 11\n\nWhen:\nThe check runs.\n**＋** Twice.\n\n"
    "Then:\nIt passes.\n**－** Never on Sunday."
)


def seed_derived(tmp_path):
    seed(tmp_path, ledger=DERIVED_LEDGER, spec=DERIVED_SPEC)
    rules = tmp_path / "vault" / "wiki" / "rules"
    (rules / "rule-old.md").write_text(
        "---\ntype: rule\nkind: Leaf\nestimates: [estimate-old-holds, estimate-old-second]\n---\n",
        encoding="utf-8",
    )
    (rules / "rule-empty.md").write_text("---\ntype: rule\nestimates: []\n---\n", encoding="utf-8")
    return tmp_path


def of_case(data, case):
    return [e for e in data["entries"] if e.get("case") == case]


def test_a_leaf_create_with_method_yields_its_estimates_create_entry(tmp_path):
    seed_derived(tmp_path)
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "written with 13 entries" in out  # 7 lines, 6 derived
    data = load(tmp_path)
    leaf, estimate = of_case(data, "11")
    assert leaf["slug"] == "rule-leaf" and estimate["slug"] == "estimate-leaf"
    assert estimate["kind"] == "create" and estimate["category"] == "estimates"
    assert estimate["line"] == leaf["line"] == 1 and estimate["text"] == leaf["text"]
    assert estimate["origin"] == f"raw/{DATE}/ledger.md#case-11"
    assert estimate["decision"] == "decision-case-11" and estimate["ref"] == "rule-leaf"
    assert estimate["tags"] == ["harness"] and estimate["derived"] is True
    assert estimate["fields"] == {"type": "estimate", "kind": "QA"}
    assert estimate["sections"] == {
        "Context": "The Leaf has no check.",
        "Criterion": CRITERION_11,
        "Method": "pytest in tests/test_leaf.py",
    }
    assert "incomplete" not in estimate
    assert "method" not in leaf["fields"] and leaf["fields"]["kind"] == "Leaf"
    assert "incomplete" not in leaf


def test_the_derived_estimate_takes_estimate_slug_and_kind_and_names_a_missing_when(tmp_path):
    seed_derived(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    cart, estimate = of_case(data, "15")
    assert estimate["slug"] == "estimate-cart-renders" and estimate["ref"] == "entity-cart"
    assert estimate["fields"] == {"type": "estimate", "kind": "Research"}
    assert estimate["tags"] == ["cart"]
    assert estimate["sections"] == {
        "Context": "No cart yet.",
        "Criterion": "### case 15",
        "Method": "measure by hand",
    }
    assert estimate["incomplete"] == ["when", "then"]
    assert cart["fields"] == {
        "type": "entity",
        "kind": "MOC",
        "purpose": "Lets a buyer review an order",
        "tags": ["cart"],
    }
    assert by_slug(data, "estimate-cart") == []


def test_an_update_with_contract_changed_yields_the_estimates_update_entry(tmp_path):
    seed_derived(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    update, estimate = of_case(data, "12")
    assert update["slug"] == "rule-old" and update["kind"] == "update"
    assert set(update) & {"contract", "method", "fields"} == set()
    assert update["replace"] == [{"old": "old words", "new": "new words"}]
    assert estimate["kind"] == "update" and estimate["slug"] == "estimate-old-holds"
    assert estimate["category"] == "estimates" and estimate["derived"] is True
    assert estimate["criterion_block"] == (
        "### case 12\n\nWhen:\nThe page is read.\n\nThen:\nIt says new."
    )
    assert estimate["set"] == {"status": "pending"}
    assert estimate["sections"] == {"Method": "the new way"}
    assert estimate["change"] == "criterion: case 12 added"
    assert estimate["line"] == 2 and estimate["text"] == update["text"]
    assert estimate["origin"] == f"raw/{DATE}/ledger.md#case-12"
    assert estimate["decision"] == "decision-case-12" and estimate["case"] == "12"
    assert "incomplete" not in estimate
    assert estimate["superseded_by"] == "13"  # case 13 supersedes 12, the derived entry too


def test_contract_same_or_no_contract_yields_nothing(tmp_path):
    seed_derived(tmp_path)
    run(tmp_path)
    thirteen = of_case(load(tmp_path), "13")
    assert [e["kind"] for e in thirteen] == ["update", "remove_criterion"]
    raw = tmp_path / "vault" / "raw" / DATE  # the base Spec: updates without contract
    (raw / "ledger.md").write_text(LEDGER, encoding="utf-8", newline="\n")
    (raw / "spec.md").write_text(SPEC, encoding="utf-8", newline="\n")
    (raw / "materialize.yaml").unlink()
    run(tmp_path)
    data = load(tmp_path)
    assert [e["kind"] for e in of_case(data, "3")] == ["update"]
    assert by_slug(data, "estimate-old-holds", "update") == []


def test_a_contract_change_without_a_live_estimate_is_incomplete(tmp_path):
    seed_derived(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    for case in ("14", "17"):  # no page; a page with estimates: []
        update, estimate = of_case(data, case)
        assert update["kind"] == "update" and estimate["kind"] == "update"
        assert estimate["slug"] is None and estimate["category"] == "estimates"
        assert estimate["incomplete"] == ["estimate"]
        assert estimate["criterion_block"].startswith(f"### case {case}\n\nWhen:\nSomething.")
        assert estimate["set"] == {"status": "pending"} and "sections" not in estimate
        assert estimate["change"] == f"criterion: case {case} added"


def test_a_supersedes_yields_a_remove_criterion_entry(tmp_path):
    seed_derived(tmp_path)
    run(tmp_path)
    data = load(tmp_path)
    update, removal = of_case(data, "13")
    assert removal["kind"] == "remove_criterion" and removal["derived"] is True
    assert removal["case_removed"] == "12" and removal["change"] == "criterion: case 12 removed"
    assert removal["line"] == 3 and removal["text"] == update["text"]
    assert removal["origin"] == f"raw/{DATE}/ledger.md#case-13"
    assert removal["decision"] == "decision-case-13" and removal["case"] == "13"
    assert "slug" not in removal
    assert data["entries"].index(removal) == data["entries"].index(update) + 1


def test_the_decision_entry_names_the_estimates_the_case_shaped(tmp_path):
    seed_derived(tmp_path)
    run(tmp_path)
    decisions = {d["case"]: d for d in load(tmp_path)["decisions"]}
    assert decisions["11"]["criterion"] == [{"estimate": "estimate-leaf", "case": "11"}]
    assert decisions["11"]["targets"] == [
        {"kind": "create", "category": "rules", "slug": "rule-leaf", "ref": "rule-root"}
    ]
    assert decisions["12"]["criterion"] == [{"estimate": "estimate-old-holds", "case": "12"}]
    assert decisions["12"]["targets"] == [
        {"kind": "update", "category": "rules", "slug": "rule-old"}
    ]
    assert decisions["15"]["criterion"] == [{"estimate": "estimate-cart-renders", "case": "15"}]
    for case in ("13", "14", "16", "17"):  # same, no Estimate to name, a plain create
        assert "criterion" not in decisions[case]
    assert decisions["13"]["supersedes"] == ["decision-case-12"]


def test_a_standalone_estimate_create_with_ref_still_maps_its_sections(tmp_path):  # case 53.3
    seed_derived(tmp_path)
    run(tmp_path)
    (alone,) = of_case(load(tmp_path), "16")
    assert alone["slug"] == "estimate-cart-alone" and alone["ref"] == "entity-cart"
    assert alone["fields"] == {"type": "estimate", "kind": "QA", "tags": ["cart"]}
    assert alone["tags"] == ["cart"]
    assert alone["sections"] == {"Context": "c", "Criterion": "cr", "Method": "m"}
    assert "derived" not in alone and "incomplete" not in alone


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
    assert code == 0 and err == "" and "written with 12 entries" in out
    data = load(tmp_path)
    assert data["spec"] == []
    (root,) = by_slug(data, "rule-root")
    assert root["incomplete"] == ["then"]
    assert all("spec" not in d for d in data["decisions"])


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
    assert code == 0 and "written with 12 entries" in out
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
