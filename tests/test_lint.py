"""`guppi lint`: one finding per defect class, nothing on a clean vault.

Rule page: `vault/wiki/rules/rule-lint.md`. Each test seeds a small vault with its own
schemas, one page per defect, and asserts the finding names the page and the class.
"""

import io
import textwrap

from guppi import lint

RULES_YAML = """\
type: rule
properties:
  required: [type, kind, purpose, status, estimates, origin]
  optional: [enforcement, implementation_ref, governs, render_mode, parent, children]
  values:
    kind: [MOC, Leaf]
    status: [draft, built, archived]
    enforcement: [hook, check, render]
  conditional:
    - when: {enforcement: hook}
      required: [implementation_ref]
    - when: {kind: MOC}
      required: [children]
      forbidden_values: {enforcement: [hook, check]}
body:
  required: ["## Purpose", "## Estimates", "## History"]
  optional: ["## Render", "## Children", "## Parent", "## Implementation"]
  conditional:
    - when: {kind: MOC}
      required: ["## Children"]
"""

RULES_MD = """\
# Rule — page schema

## Properties

| Field | Required |
|---|---|
| `type` | yes |
| `kind` | yes |
| `purpose` | yes |
| `status` | yes |
| `enforcement` | no |
| `implementation_ref` | no |
| `governs` | no |
| `render_mode` | no |
| `parent` | no |
| `children` | no |
| `estimates` | yes |
| `origin` | yes |

## Body

| Section | Required |
|---|---|
| `## Purpose` | yes |
| `## Render` | no |
| `## Estimates` | yes |
| `## Children` | no |
| `## Parent` | no |
| `## Implementation` | no |

## History
"""

ESTIMATES_YAML = """\
type: estimate
properties:
  required: [type, kind, status, target, origin]
  optional: []
  values:
    kind: [QA, Research]
    status: [pending, passed, failed]
body:
  required: ["## Context", "## Criterion", "## Method", "## History"]
  optional: ["## Result"]
"""

ESTIMATES_MD = """\
# Estimate — page schema

## Properties

| Field | Required |
|---|---|
| `type` | yes |
| `kind` | yes |
| `status` | yes |
| `target` | yes |
| `origin` | yes |

## Body

| Section | Required |
|---|---|
| `## Context` | yes |
| `## Criterion` | yes |
| `## Method` | yes |
| `## Result` | no |

## History
"""

LEDGER = (
    "- decision[case 1][create][rule-x]\n- decision[case 1][create][estimate-x-works]{ref:rule-x}\n"
)
ORIGIN = "raw/2026-09-09/ledger.md#case-1"


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text), encoding="utf-8", newline="\n")


def rule_page(**over):
    props = {
        "type": "rule",
        "kind": "Leaf",
        "purpose": "Prevents x",
        "status": "draft",
        "enforcement": "hook",
        "implementation_ref": "[guppi/x.py]",
        "parent": "rule-root",
        "estimates": "[estimate-x-works]",
        "origin": ORIGIN,
    }
    props.update(over)
    front = "\n".join(f"{k}: {v}" for k, v in props.items() if v is not None)
    return f"---\n{front}\n---\n\n## Purpose\n\nx\n\n## Estimates\n\n- [[estimate-x-works]]\n\n## Parent\n\n- [[rule-root]]\n\n## History\n\n- created\n"


def estimate_page(status="pending", method="pytest in `tests/test_x.py`.", result=True, **over):
    props = {
        "type": "estimate",
        "kind": "QA",
        "status": status,
        "target": "rule-x",
        "origin": ORIGIN,
    }
    props.update(over)
    front = "\n".join(f"{k}: {v}" for k, v in props.items())
    body = (
        f"---\n{front}\n---\n\n## Context\n\nc\n\n## Criterion\n\ncr\n\n## Method\n\n{method}\n\n"
    )
    if status != "pending" and result:
        body += "## Result\n\nr\n\n"
    return body + "## History\n\n- created\n"


def root_page():
    return (
        "---\ntype: rule\nkind: MOC\npurpose: Prevents root\nstatus: draft\n"
        "children: [rule-x]\nestimates: []\norigin: raw/2026-09-09/ledger.md#case-1\n---\n\n"
        "## Purpose\n\nr\n\n## Estimates\n\n## Children\n\n1. [[rule-x]]\n\n## History\n\n- created\n"
    )


def seed(tmp_path, rule=None, estimate=None):
    wiki = tmp_path / "vault" / "wiki"
    write(wiki / "rules" / "schema.yaml", RULES_YAML)
    write(wiki / "rules" / "schema.md", RULES_MD)
    write(wiki / "estimates" / "schema.yaml", ESTIMATES_YAML)
    write(wiki / "estimates" / "schema.md", ESTIMATES_MD)
    write(wiki / "rules" / "rule-root.md", root_page())
    write(wiki / "rules" / "rule-x.md", rule_page() if rule is None else rule)
    write(
        wiki / "estimates" / "estimate-x-works.md",
        estimate_page() if estimate is None else estimate,
    )
    write(tmp_path / "vault" / "raw" / "2026-09-09" / "ledger.md", LEDGER)
    write(tmp_path / "guppi" / "x.py", "")
    write(tmp_path / "tests" / "test_x.py", "")
    write(tmp_path / "Makefile", "test-root:\n\t@true\n")
    return wiki


def run(project_dir):
    out, err = io.StringIO(), io.StringIO()
    code = lint.run([], stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue().splitlines(), err.getvalue()


def test_a_clean_vault_is_silent(tmp_path):
    seed(tmp_path)
    assert run(tmp_path) == (0, [], "")


def test_a_missing_required_field_is_a_schema_finding(tmp_path):
    seed(tmp_path, rule=rule_page(purpose=None))
    code, lines, _ = run(tmp_path)
    assert code == 1
    assert lines == ["rules/rule-x: schema: missing field purpose"]


def test_a_value_outside_the_list_is_a_schema_finding(tmp_path):
    seed(tmp_path, rule=rule_page(kind="Branch"))
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-x: schema: kind is 'Branch', not one of ['MOC', 'Leaf']"]


def test_an_unmet_conditional_is_a_schema_finding(tmp_path):
    seed(tmp_path, rule=rule_page(implementation_ref=None))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: schema: missing field implementation_ref (given {'enforcement': 'hook'})"
    ]


def test_a_forbidden_value_is_a_schema_finding(tmp_path):
    wiki = seed(tmp_path)
    write(
        wiki / "rules" / "rule-root.md",
        root_page().replace("kind: MOC\n", "kind: MOC\nenforcement: hook\n"),
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-root: schema: missing field implementation_ref (given {'enforcement': 'hook'})",
        "rules/rule-root: schema: enforcement may not be 'hook' (given {'kind': 'MOC'})",
    ]


def test_a_missing_section_is_a_schema_finding(tmp_path):
    seed(
        tmp_path,
        estimate=estimate_page().replace("## Method\n\npytest in `tests/test_x.py`.\n\n", ""),
    )
    _, lines, _ = run(tmp_path)
    assert lines == ["estimates/estimate-x-works: schema: missing section ## Method"]


def test_prose_and_yaml_naming_different_fields_is_a_schema_prose_finding(tmp_path):
    wiki = seed(tmp_path)
    write(
        wiki / "rules" / "schema.md", RULES_MD.replace("| `governs` | no |\n", "| `owns` | no |\n")
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/schema: schema-prose: schema.md names field owns, schema.yaml does not",
        "rules/schema: schema-prose: schema.yaml names field governs, schema.md does not",
    ]


def test_a_slug_no_page_carries_is_a_ref_finding(tmp_path):
    seed(tmp_path, rule=rule_page(parent="rule-nowhere"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: ref: parent names rule-nowhere, which no live or archived page carries",
        "rules/rule-root: orphan: no other live page names it in its frontmatter",
    ]


def test_an_archived_page_still_resolves_a_ref(tmp_path):
    seed(tmp_path, rule=rule_page(parent="rule-gone"))
    archived = tmp_path / "vault" / "archived" / "migration" / "2026-09-10" / "rules"
    write(archived / "rule-gone.md", "---\ntype: rule\n---\n")
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-root: orphan: no other live page names it in its frontmatter"]


def test_a_wikilink_inside_a_code_span_is_prose_not_a_link(tmp_path):
    seed(
        tmp_path,
        rule=rule_page().replace("- [[rule-root]]", "- [[rule-root]], and `[[slug]]` links stay"),
    )
    assert run(tmp_path) == (0, [], "")


def test_a_wikilink_to_nothing_is_a_ref_finding(tmp_path):
    seed(
        tmp_path, rule=rule_page().replace("- [[rule-root]]", "- [[rule-root]] and [[rule-ghost]]")
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: ref: body names rule-ghost, which no live or archived page carries"
    ]


def test_an_origin_without_its_ledger_line_is_an_origin_finding(tmp_path):
    seed(tmp_path, rule=rule_page(origin="raw/2026-09-09/ledger.md#case-7"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: origin: raw/2026-09-09/ledger.md#case-7: no line carrying [case 7]"
    ]


def test_a_path_that_does_not_exist_is_a_path_finding(tmp_path):
    seed(tmp_path, rule=rule_page(implementation_ref="[guppi/x.py, guppi/missing.py]"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: path: implementation_ref names guppi/missing.py, which does not exist"
    ]


def test_a_page_nothing_names_is_an_orphan_finding(tmp_path):
    wiki = seed(tmp_path)
    write(
        wiki / "rules" / "rule-lonely.md",
        rule_page(estimates="[]").replace("- [[estimate-x-works]]", ""),
    )
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-lonely: orphan: no other live page names it in its frontmatter"]


def test_built_with_a_pending_estimate_is_a_status_finding(tmp_path):
    seed(tmp_path, rule=rule_page(status="built"))
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-x: status: built while estimate-x-works is not passed"]


def test_draft_with_every_estimate_passed_is_a_status_finding(tmp_path):
    seed(tmp_path, estimate=estimate_page(status="passed"))
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-x: status: draft while every Estimate is passed"]


def test_passed_without_a_result_is_a_status_finding(tmp_path):
    seed(
        tmp_path,
        rule=rule_page(status="built"),
        estimate=estimate_page(status="passed", result=False),
    )
    _, lines, _ = run(tmp_path)
    assert lines == ["estimates/estimate-x-works: status: passed without a ## Result section"]


def test_an_estimate_its_target_does_not_list_is_a_status_finding(tmp_path):
    seed(tmp_path, rule=rule_page(estimates="[]").replace("- [[estimate-x-works]]", ""))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "estimates/estimate-x-works: orphan: no other live page names it in its frontmatter",
        "estimates/estimate-x-works: status: target rule-x does not list it in estimates",
    ]


def test_a_leaf_method_naming_no_test_file_is_a_method_finding(tmp_path):
    seed(tmp_path, estimate=estimate_page(method="Run it and look."))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "estimates/estimate-x-works: method: names no tests/ file and does not say by hand"
    ]


def test_a_leaf_method_naming_a_missing_test_file_is_a_method_finding(tmp_path):
    seed(tmp_path, estimate=estimate_page(method="pytest in `tests/test_gone.py`."))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "estimates/estimate-x-works: method: names tests/test_gone.py, which does not exist"
    ]


def test_a_leaf_method_by_hand_is_the_exception(tmp_path):
    seed(tmp_path, estimate=estimate_page(method="One reading by hand."))
    assert run(tmp_path) == (0, [], "")


def test_a_moc_method_needs_a_make_target_that_exists(tmp_path):
    wiki = seed(tmp_path)
    write(
        wiki / "rules" / "rule-root.md",
        root_page().replace("estimates: []", "estimates: [estimate-root-holds]"),
    )
    write(
        wiki / "estimates" / "estimate-root-holds.md",
        estimate_page(target="rule-root", method="`make test-nope`, the pipeline."),
    )
    _, lines, _ = run(tmp_path)
    assert lines == ["estimates/estimate-root-holds: method: the Makefile has no target test-nope"]
    write(
        wiki / "estimates" / "estimate-root-holds.md",
        estimate_page(target="rule-root", method="`make test-root`, the pipeline."),
    )
    assert run(tmp_path) == (0, [], "")


def test_a_moc_method_by_hand_over_hand_read_children_is_the_exception(tmp_path):
    wiki = seed(tmp_path, estimate=estimate_page(method="One reading by hand."))
    write(
        wiki / "rules" / "rule-root.md",
        root_page().replace("estimates: []", "estimates: [estimate-root-holds]"),
    )
    write(
        wiki / "estimates" / "estimate-root-holds.md",
        estimate_page(target="rule-root", method="One reading at a session start, by hand."),
    )
    assert run(tmp_path) == (0, [], "")


def test_a_moc_method_by_hand_over_a_tested_child_is_a_method_finding(tmp_path):
    wiki = seed(tmp_path)
    write(
        wiki / "rules" / "rule-root.md",
        root_page().replace("estimates: []", "estimates: [estimate-root-holds]"),
    )
    write(
        wiki / "estimates" / "estimate-root-holds.md",
        estimate_page(target="rule-root", method="One reading at a session start, by hand."),
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        "estimates/estimate-root-holds: method: says by hand while estimate-x-works names a test file"
    ]


def test_cli_dispatches_to_lint(tmp_path, monkeypatch, capsys):
    from guppi import cli

    seed(tmp_path, rule=rule_page(status="built"))
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["lint"]) == 1
    assert "rules/rule-x: status" in capsys.readouterr().out
