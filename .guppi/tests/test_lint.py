"""`guppi lint`: one finding per defect class, nothing on a clean vault.

Rule page: `vault/wiki/rules/rule-lint.md`. Each test seeds a small vault with its own
schemas, one page per defect, and asserts the finding names the page and the class.
"""

import importlib.machinery
import io
import os
import shutil
import subprocess
import sys
import textwrap
import types
from pathlib import Path

import pytest
import yaml

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
  required: ["## Purpose", "## History"]
  optional: ["## Render"]
"""

ESTIMATES_YAML = """\
type: estimate
properties:
  required: [type, kind, status, target, origin]
  optional: [purpose, method, checked]
  values:
    kind: [QA, Research]
    status: [pending, passed, failed]
body:
  required: ["## Criterion", "## History"]
  optional: ["## Context", "## Method", "## Result"]
"""


def described(text):
    """The yaml with a one-line description under `fields` and `sections` for every name
    its lists carry — the shape lint checks (since case 304.8)."""
    data = yaml.safe_load(text)
    for block, key in (("properties", "fields"), ("body", "sections")):
        data[key] = {name: "d" for name in sorted(lint.listed_names(data.get(block) or {}))}
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True)


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
        "status": "built",  # its one Estimate is passed by default (case 202)
        "enforcement": "hook",
        "implementation_ref": "[guppi/x.py]",
        "parent": "rule-root",
        "estimates": "[estimate-x-works]",
        "origin": ORIGIN,
    }
    props.update(over)
    front = "\n".join(f"{k}: {v}" for k, v in props.items() if v is not None)
    return f"---\n{front}\n---\n\n## Purpose\n\nx\n\n## History\n\n- created\n"


def estimate_page(status="passed", method="pytest tests/test_x.py", result=True, **over):
    """A page of the model (case 193): `method` a field, no `## Context`, no `## Method`;
    `passed` with a Result by default, so the clean vault has nothing unread."""
    props = {
        "type": "estimate",
        "kind": "QA",
        "status": status,
        "target": "rule-x",
        "method": method,
        "origin": ORIGIN,
    }
    props.update(over)
    front = "\n".join(
        f'{k}: "{v}"' if k == "method" else f"{k}: {v}" for k, v in props.items() if v is not None
    )
    body = f"---\n{front}\n---\n\n## Criterion\n\ncr\n\n"
    if status != "pending" and result:
        body += "## Result\n\nr\n\n"
    return body + "## History\n\n- created\n"


def old_estimate_page(status="passed", method="pytest in `tests/test_x.py`.", **over):
    """A page of the old shape: `## Context` and `## Method` as sections, no `method`
    field — no longer counted or read by lint (the shape before case 193; cases 506.2,
    506.3)."""
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
    if status != "pending":
        body += "## Result\n\nr\n\n"
    return body + "## History\n\n- created\n"


def root_page():
    return (
        "---\ntype: rule\nkind: MOC\npurpose: Prevents root\nstatus: built\n"
        "children: [rule-x]\nestimates: []\norigin: raw/2026-09-09/ledger.md#case-1\n---\n\n"
        "## Purpose\n\nr\n\n## History\n\n- created\n"
    )


def seed(tmp_path, rule=None, estimate=None):
    wiki = tmp_path / "vault" / "wiki"
    write(wiki / "rules" / "schema.yaml", described(RULES_YAML))
    write(wiki / "estimates" / "schema.yaml", described(ESTIMATES_YAML))
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


def test_unmet_conditions_is_the_one_judgment_of_a_condition():
    # `check_schema` reports each `what` it gives, and pre-spec calls it on the page
    # as a Case leaves it (case 714)
    schema = yaml.safe_load(RULES_YAML)
    schema["body"]["conditional"] = [{"when": {"enforcement": "render"}, "required": ["## Render"]}]
    props = {"kind": "MOC", "enforcement": "hook"}
    assert lint.unmet_conditions(props, {"## Purpose"}, schema) == [
        (
            {"enforcement": "hook"},
            "missing field implementation_ref (given {'enforcement': 'hook'})",
        ),
        ({"kind": "MOC"}, "missing field children (given {'kind': 'MOC'})"),
        ({"kind": "MOC"}, "enforcement may not be 'hook' (given {'kind': 'MOC'})"),
    ]
    rendered = {"kind": "Leaf", "enforcement": "render"}
    assert lint.unmet_conditions(rendered, {"## Purpose"}, schema) == [
        ({"enforcement": "render"}, "missing section ## Render (given {'enforcement': 'render'})")
    ]
    assert lint.unmet_conditions(rendered, {"## Render"}, schema) == []
    page = lint.Page(category="rules", slug="rule-x", path=Path("rule-x.md"), props=props)
    page.sections = {"## Purpose": "p", "## History": ""}
    reported = [finding.text for finding in lint.check_schema(page, schema)]
    judged = [
        f"rules/rule-x: schema: {what}"
        for _, what in lint.unmet_conditions(props, page.sections, schema)
    ]
    assert [line for line in reported if "given" in line] == judged


def test_a_list_in_a_single_field_is_a_schema_finding(tmp_path):
    # a field `properties.single` names holds one value, never a list (case 362.1)
    wiki = seed(tmp_path, rule=rule_page(parent="[rule-root, rule-x]"))
    single = RULES_YAML.replace("  values:\n", "  single: [parent]\n  values:\n", 1)
    write(wiki / "rules" / "schema.yaml", described(single))
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-x: schema: parent holds a list; one link is its shape"]
    write(wiki / "rules" / "rule-x.md", rule_page())  # one value: no finding
    assert run(tmp_path) == (0, [], "")


def test_a_list_in_a_field_no_single_names_is_no_finding(tmp_path):
    seed(tmp_path, rule=rule_page(parent="[rule-root]"))  # the schema has no `single`
    assert run(tmp_path) == (0, [], "")


def test_a_missing_section_is_a_schema_finding(tmp_path):
    seed(tmp_path, estimate=estimate_page().replace("## Criterion\n\ncr\n\n", ""))
    _, lines, _ = run(tmp_path)
    assert lines == ["estimates/estimate-x-works: schema: missing section ## Criterion"]


def test_a_listed_name_without_a_description_and_a_stray_one_are_schema_description_findings(
    tmp_path,
):
    wiki = seed(tmp_path)
    text = described(RULES_YAML).replace("  governs: d\n", "  owns: d\n")
    text = text.replace("  '## Render': d\n", "  '## Notes': d\n")
    write(wiki / "rules" / "schema.yaml", text)
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/schema: schema-description: field governs has no description",
        "rules/schema: schema-description: fields describes owns, which no list names",
        "rules/schema: schema-description: section ## Render has no description",
        "rules/schema: schema-description: sections describes ## Notes, which no list names",
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
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-10" / "rules"
    write(archived / "rule-gone.md", "---\ntype: rule\n---\n")
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-root: orphan: no other live page names it in its frontmatter"]


def test_a_wikilink_inside_a_code_span_is_prose_not_a_link(tmp_path):
    seed(
        tmp_path,
        rule=rule_page().replace(
            "## Purpose\n\nx", "## Purpose\n\nx [[rule-root]], and `[[slug]]` links stay"
        ),
    )
    assert run(tmp_path) == (0, [], "")


def test_a_wikilink_to_nothing_is_a_ref_finding(tmp_path):
    seed(
        tmp_path,
        rule=rule_page().replace(
            "## Purpose\n\nx", "## Purpose\n\nx [[rule-root]] and [[rule-ghost]]"
        ),
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: ref: body names rule-ghost, which no live or archived page carries"
    ]


def test_a_wikilink_to_a_hub_file_under_wiki_resolves(tmp_path):
    seed(
        tmp_path,
        rule=rule_page().replace(
            "## Purpose\n\nx",
            "## Purpose\n\nx [[rule-root]], [[brief]], [[rules/schema]] and [[nowhere]]",
        ),
    )
    write(tmp_path / "vault" / "wiki" / "brief.md", "# Brief\n")
    _, lines, _ = run(tmp_path)
    assert lines == [  # the stem of a root file; a schema is no file (cases 149.3, 304)
        "rules/rule-x: ref: body names rules/schema, which no live or archived page carries",
        "rules/rule-x: ref: body names nowhere, which no live or archived page carries",
    ]


def test_an_origin_without_its_ledger_line_is_an_origin_finding(tmp_path):
    seed(tmp_path, rule=rule_page(origin="raw/2026-09-09/ledger.md#case-7"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: origin: raw/2026-09-09/ledger.md#case-7: no line carrying [case 7]"
    ]


# --- both forms of origin, in raw/ or in the archive (case 103.5) ------------------------


def test_a_session_origin_resolves_in_the_session_folder(tmp_path):
    seed(tmp_path, rule=rule_page(origin="raw/2026-09-10/1610/ledger.md#case-1"))
    write(tmp_path / "vault" / "raw" / "2026-09-10" / "1610" / "ledger.md", LEDGER)
    assert run(tmp_path) == (0, [], "")


def test_an_origin_resolves_in_the_archive_once_the_unit_moved(tmp_path):
    seed(tmp_path, rule=rule_page(origin="raw/2026-09-10/1610/ledger.md#case-1"))
    archive = tmp_path / "vault" / "archive" / "migration"
    write(archive / "2026-09-10" / "1610" / "raw" / "ledger.md", LEDGER)
    assert run(tmp_path) == (0, [], "")
    # the date form, archived at <date>/raw/
    (tmp_path / "vault" / "raw" / "2026-09-09" / "ledger.md").unlink()
    write(archive / "2026-09-09" / "raw" / "ledger.md", LEDGER)
    seed_rule = tmp_path / "vault" / "wiki" / "rules" / "rule-x.md"
    write(seed_rule, rule_page())
    assert run(tmp_path) == (0, [], "")


def test_an_origin_in_neither_place_or_in_both_is_a_finding(tmp_path):
    seed(tmp_path, rule=rule_page(origin="raw/2026-09-10/1610/ledger.md#L1"))
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-x: origin: raw/2026-09-10/1610/ledger.md#L1: no such ledger"]
    write(tmp_path / "vault" / "raw" / "2026-09-10" / "1610" / "ledger.md", LEDGER)
    write(
        tmp_path / "vault" / "archive" / "migration" / "2026-09-10" / "1610" / "raw" / "ledger.md",
        LEDGER,
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: origin: raw/2026-09-10/1610/ledger.md#L1: two ledgers for raw/2026-09-10/1610"
    ]


def test_the_shipped_origin_is_no_finding_on_a_core_page_only(tmp_path):  # (case 804.4)
    seed(tmp_path, rule=rule_page(origin="guppi", core="true"))
    assert run(tmp_path) == (0, [], "")
    seed(tmp_path, rule=rule_page(origin="guppi"))
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-x: origin: guppi: not raw/<date>[/<HHMM>]/ledger.md#case-N"]


def test_a_page_under_an_archived_raw_folder_is_no_known_slug(tmp_path):
    seed(tmp_path)
    write(
        tmp_path / "vault" / "archive" / "migration" / "2026-09-10" / "1610" / "raw" / "spec.md",
        "# Spec\n",
    )
    assert "spec" not in lint.archived_slugs(tmp_path / "vault" / "wiki")


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


# --- a placeholder says what is true (case 186.3): `estimate-lint-catches` ------------

PLACEHOLDER = (
    "---\ntype: rule\npurpose: Prevents something, later\nstatus: draft\n"
    'deferred_by: ["[[decision-case-64]]"]\norigin: ' + ORIGIN + "\nsprint: migration\n"
    "created: 2026-09-09\n---\n\n## Purpose\n\nLater.\n\n## History\n\n"
    "- 2026-09-10 deferred, placeholder · raw/2026-09-09/ledger.md#case-29\n"
    "- 2026-09-11 deferred_by decision-case-29 set · [[decision-case-52.3]]\n"
    "- 2026-09-12 deferred · [[decision-case-64]]\n"
    "- 2026-09-12 defer by decision-case-64 superseded · [[decision-case-70]]\n"
    "- 2026-09-13 deferred · [[decision-case-70]]\n"
)


def test_a_placeholder_earns_one_deferred_finding_with_its_count(tmp_path):
    wiki = seed(tmp_path)
    write(wiki / "rules" / "rule-later.md", PLACEHOLDER)
    _, lines, _ = run(tmp_path)  # the decision pages are not seeded: their `ref` lines stand
    mine = [line for line in lines if "rule-later" in line and ": ref:" not in line]
    assert mine == ["rules/rule-later: deferred: 3 times since case 29"]  # no schema, no orphan


def test_a_page_with_deferred_by_whose_fields_are_in_place_earns_no_deferred_finding(tmp_path):
    seed(tmp_path, rule=rule_page(deferred_by='["[[decision-case-64]]"]'))
    _, lines, _ = run(tmp_path)
    assert not any("deferred:" in line for line in lines)


def test_a_placeholder_missing_another_field_still_earns_that_schema_finding(tmp_path):
    wiki = seed(tmp_path)
    write(wiki / "rules" / "rule-later.md", PLACEHOLDER.replace("origin: ", "origin_was: "))
    _, lines, _ = run(tmp_path)
    mine = [line for line in lines if "rule-later" in line and ": ref:" not in line]
    assert "rules/rule-later: schema: missing field origin" in mine
    assert "rules/rule-later: deferred: 3 times since case 29" in mine
    assert not any("missing field kind" in line or "orphan" in line for line in mine)


def test_built_with_a_pending_estimate_is_a_status_finding(tmp_path):
    seed(tmp_path, rule=rule_page(status="built"), estimate=estimate_page(status="pending"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: status: built while estimate-x-works is not passed",
        "estimates/estimate-x-works: unread: pending",
    ]


def test_draft_with_every_estimate_passed_is_a_status_finding(tmp_path):
    seed(tmp_path, rule=rule_page(status="draft"))
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-x: status: draft while every Estimate is passed"]


def test_a_pending_or_failed_estimate_is_an_unread_finding(tmp_path):
    # red between a change of a promise and its reading, by design (case 202)
    seed(tmp_path, rule=rule_page(status="draft"), estimate=estimate_page(status="pending"))
    _, lines, _ = run(tmp_path)
    assert lines == ["estimates/estimate-x-works: unread: pending"]
    seed(tmp_path, rule=rule_page(status="draft"), estimate=estimate_page(status="failed"))
    _, lines, _ = run(tmp_path)
    assert lines == ["estimates/estimate-x-works: unread: failed"]


def unread_lines(tmp_path, status, method):
    seed(tmp_path, rule=rule_page(status="draft"), estimate=estimate_page(status, method))
    _, lines, _ = run(tmp_path)
    return [line for line in lines if ": unread: " in line]


# a pending Estimate whose method waits for a later moment is not red (case 799)
@pytest.mark.parametrize(
    "method",
    [
        "by hand, after a pull request from a second account: the page read against the Criterion",
        "by hand, in a session of the sprint plugin before its close: the run read",
        "by hand: the person's answer in the session after the close of a sprint",
        "pytest tests/test_x.py; by hand, after the first merge of main: the page read",
    ],
)
def test_a_pending_estimate_whose_method_waits_for_a_later_moment_is_no_unread_finding(
    tmp_path, method
):
    assert unread_lines(tmp_path, "pending", method) == []


def test_a_pending_estimate_read_at_its_own_retro_is_an_unread_finding(tmp_path):
    method = "by hand at the Retro of this session: the Render read against the Criterion"
    assert unread_lines(tmp_path, "pending", method) == [
        "estimates/estimate-x-works: unread: pending"
    ]


def test_a_failed_estimate_whose_method_waits_for_an_event_is_an_unread_finding(tmp_path):
    method = "by hand, after a pull request from a second account: the page read"
    assert unread_lines(tmp_path, "failed", method) == [
        "estimates/estimate-x-works: unread: failed"
    ]


# --- a draft page with core: true where the command ship stands; each test name holds
# draft_core (case 822) ---------------------------------------------------------------------


def ship_module(monkeypatch, stands: bool) -> None:
    """The module `guppi.ship` found or missing for `ship_stands`, by its entry in
    `sys.modules`, in this repository and in a project that installed GUPPI alike."""
    module = None
    if stands:
        module = types.ModuleType("guppi.ship")
        module.__spec__ = importlib.machinery.ModuleSpec("guppi.ship", None)
    monkeypatch.setitem(sys.modules, "guppi.ship", module)


def own_lines(tmp_path) -> list[str]:
    _, lines, _ = run(tmp_path)
    return [line for line in lines if line.startswith("rules/rule-x: ")]


def test_a_draft_core_page_without_estimates_is_a_status_finding_where_ship_stands(
    tmp_path, monkeypatch
):
    seed(tmp_path, rule=rule_page(status="draft", core="true", estimates="[]"))
    ship_module(monkeypatch, stands=True)
    assert lint.ship_stands()
    assert own_lines(tmp_path) == ["rules/rule-x: status: a page with core: true that is draft"]


def test_a_draft_core_page_is_no_finding_where_the_module_of_ship_is_missing(tmp_path, monkeypatch):
    seed(tmp_path, rule=rule_page(status="draft", core="true", estimates="[]"))
    ship_module(monkeypatch, stands=False)
    assert not lint.ship_stands()
    assert own_lines(tmp_path) == []


def test_a_draft_core_page_with_a_pending_estimate_is_one_status_finding(tmp_path, monkeypatch):
    seed(
        tmp_path,
        rule=rule_page(status="draft", core="true"),
        estimate=estimate_page(status="pending"),
    )
    ship_module(monkeypatch, stands=True)
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: status: a page with core: true that is draft",
        "estimates/estimate-x-works: unread: pending",
    ]


def test_a_draft_page_without_core_or_a_built_core_page_is_no_draft_core_finding(
    tmp_path, monkeypatch
):
    ship_module(monkeypatch, stands=True)
    seed(tmp_path, rule=rule_page(status="draft", estimates="[]"))
    assert own_lines(tmp_path) == []
    seed(tmp_path, rule=rule_page(status="built", core="true"))
    assert own_lines(tmp_path) == []


def test_lint_check_and_cli_judge_whether_ship_stands_by_one_function_draft_core():
    from guppi import check, cli, pages

    for module in (lint, check, cli):
        assert module.ship_stands is pages.ship_stands, module.__name__
        source = Path(module.__file__).read_text(encoding="utf-8")
        assert "def ship_stands(" not in source and "find_spec" not in source, module.__name__


def test_lint_and_ship_judge_a_draft_core_page_by_one_function():
    from guppi import pages

    ship = pytest.importorskip("guppi.ship")  # the clean version holds no `guppi.ship`
    assert lint.is_draft_core is pages.is_draft_core
    assert ship.is_draft_core is pages.is_draft_core
    for module in (lint, ship):
        source = Path(module.__file__).read_text(encoding="utf-8")
        assert "def is_draft_core(" not in source, module.__name__


def test_a_page_with_context_and_method_sections_prints_no_unmigrated_line(tmp_path):
    # the count of the old shape is gone, whatever the page holds (cases 193, 506.2)
    old = estimate_page().replace(
        "## Criterion\n\ncr\n\n", "## Context\n\nc\n\n## Criterion\n\ncr\n\n## Method\n\nm\n\n"
    )
    seed(tmp_path, rule=rule_page(status="built"), estimate=old)
    code, lines, _ = run(tmp_path)
    assert not [line for line in lines if "unmigrated" in line]
    assert (code, lines) == (0, [])


def test_passed_without_a_result_is_a_status_finding(tmp_path):
    seed(tmp_path, rule=rule_page(status="built"), estimate=estimate_page(result=False))
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
    seed(
        tmp_path, rule=rule_page(status="built"), estimate=estimate_page(method="Run it and look.")
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "estimates/estimate-x-works: method: names no test file, pytest, guppi command "
            "or make target "
            "and is not a reading"
        )
    ]


# --- the class `markers` (case 325.2) ---------------------------------------------------

WRAPPED = "\n## Render\n\n<!-- rule-x -->\nthe body\n<!-- /rule-x -->\n"


def render_rule(body=WRAPPED, **over):
    """A rule that forces by render: the Render section stands after Purpose, before History."""
    props = {"enforcement": "render", "governs": ".claude/x.md", "render_mode": "full"}
    props.update(over)
    page = rule_page(**props)
    return page.replace("\n## History\n", body + "\n## History\n")


def test_a_render_page_without_a_render_section_is_a_markers_finding(tmp_path):
    seed(tmp_path, rule=render_rule(body="\n"))
    write(tmp_path / ".claude" / "x.md", "")
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-x: markers: no ## Render section"]


def test_a_render_not_wrapped_in_its_own_markers_is_a_markers_finding(tmp_path):
    seed(tmp_path, rule=render_rule(body="\n## Render\n\nthe body, bare\n"))
    write(tmp_path / ".claude" / "x.md", "")
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: markers: ## Render is not wrapped in <!-- rule-x --> … <!-- /rule-x -->"
    ]


def test_a_wrapped_render_is_no_markers_finding(tmp_path):
    seed(tmp_path, rule=render_rule())
    write(tmp_path / ".claude" / "x.md", "")
    assert run(tmp_path) == (0, [], "")


def test_a_closing_marker_for_a_child_in_a_full_render_is_a_markers_finding(tmp_path):
    # a parent carries one opening line per child; the closing line is the
    # renderer's own, and a stray one silently swallows the text after it (case 325.2)
    body = "\n## Render\n\n<!-- rule-x -->\nthe body\n<!-- /rule-root -->\nmore\n<!-- /rule-x -->\n"
    seed(tmp_path, rule=render_rule(body=body, children="[rule-root]"))
    write(tmp_path / ".claude" / "x.md", "")
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "rules/rule-x: markers: a closing line <!-- /rule-root --> for the child rule-root; "
            "a parent carries one opening line per child"
        )
    ]


# --- the class `fence` (case 487.2) ---------------------------------------------------------


def fenced_rule(inside):
    return render_rule(body=f"\n## Render\n\n<!-- rule-x -->\n{inside}\n<!-- /rule-x -->\n")


def test_a_closing_run_with_text_after_it_is_a_fence_finding(tmp_path):
    # a defect: the line reads as code; a later closing line ends the fence (case 483)
    seed(tmp_path, rule=fenced_rule("```\nsample\n``` When the person approves\nmore\n```"))
    write(tmp_path / ".claude" / "x.md", "")
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "rules/rule-x: fence: ## Render: a code fence with text after its run: "
            "``` When the person approves"
        )
    ]


def test_a_fence_left_open_is_a_fence_finding(tmp_path):
    seed(tmp_path, rule=fenced_rule("```yaml\na: 1"))
    write(tmp_path / ".claude" / "x.md", "")
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: fence: ## Render: a code fence open at the end of the section: ```yaml"
    ]


def test_normal_fences_are_no_fence_finding(tmp_path):
    seed(tmp_path, rule=fenced_rule("```yaml\na: 1\n```\n\n````\n``` inner\n````"))
    write(tmp_path / ".claude" / "x.md", "")
    assert run(tmp_path) == (0, [], "")


def test_a_leaf_method_naming_a_reading_without_by_hand_is_a_method_finding(tmp_path):
    # `by hand` is the one spelling of a reading; the word `reading` alone is not one (case 330.1)
    seed(
        tmp_path,
        rule=rule_page(status="built"),
        estimate=estimate_page(method="one reading of the first reply of a session"),
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "estimates/estimate-x-works: method: names no test file, pytest, guppi command "
            "or make target "
            "and is not a reading"
        )
    ]


def test_a_leaf_method_field_names_a_test_a_make_target_or_a_reading(tmp_path):
    # the field is read; a test command, a make target or a reading passes (case 202)
    for method in (
        "pytest tests/test_x.py, the tests of x",
        "pytest in the tests of guppi/x.py",
        "make test-root over the pipeline",
        "One reading by hand at a session start",
    ):
        seed(tmp_path, rule=rule_page(status="built"), estimate=estimate_page(method=method))
        assert run(tmp_path) == (0, [], ""), method
    seed(tmp_path, rule=rule_page(status="built"), estimate=estimate_page(method="make test-nope"))
    _, lines, _ = run(tmp_path)
    assert lines == ["estimates/estimate-x-works: method: the Makefile has no target test-nope"]


def test_a_method_section_without_the_field_earns_no_method_finding(tmp_path):
    # lint reads the `method` field alone, never a `## Method` section (case 506.3)
    seed(
        tmp_path,
        rule=rule_page(status="built"),
        estimate=old_estimate_page(method="pytest in `tests/test_gone.py`."),
    )
    _, lines, _ = run(tmp_path)
    assert not [line for line in lines if ": method:" in line]


def test_a_leaf_method_naming_a_missing_test_file_is_a_method_finding(tmp_path):
    seed(
        tmp_path,
        rule=rule_page(status="built"),
        estimate=estimate_page(method="pytest in `tests/test_gone.py`."),
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        "estimates/estimate-x-works: method: names tests/test_gone.py, which does not exist"
    ]


def test_a_test_path_is_read_whole_from_its_start_and_looked_up_from_the_root(tmp_path):
    # a path under `.guppi/tests/` or under a folder `tests` of the project's code (case 819.1)
    for path in (".guppi/tests/test_x.py", "discounts/tests/test_x.py"):
        seed(
            tmp_path,
            rule=rule_page(status="built"),
            estimate=estimate_page(method=f"pytest {path}"),
        )
        assert run(tmp_path) == (
            1,
            [f"estimates/estimate-x-works: method: names {path}, which does not exist"],
            "",
        ), path
        write(tmp_path / path, "")
        assert run(tmp_path) == (0, [], ""), path
    assert lint.TEST_PATH.findall(
        "`.guppi/tests/test_a.py`, tests/test_b.py and discounts/tests/test_c.py; x.tests/d.py"
    ) == [".guppi/tests/test_a.py", "tests/test_b.py", "discounts/tests/test_c.py"]


def test_a_leaf_method_by_hand_is_the_exception(tmp_path):
    seed(
        tmp_path,
        rule=rule_page(status="built"),
        estimate=estimate_page(method="One reading by hand."),
    )
    assert run(tmp_path) == (0, [], "")


MOMENT_LINE = (
    "estimates/estimate-x-works: moment: ties its reading by hand to the first moment after the "
    "render or the change — name the kind of its moment"
)


def test_moment_a_reading_tied_to_the_first_moment_after_the_render_or_the_change(tmp_path):
    # a moment that passes once and is gone when missed (case 613.1)
    for method in (
        "by hand at the first /handoff after the render",
        "pytest tests/test_x.py; by hand once, the ledger of the first session after the change",
    ):
        seed(tmp_path, rule=rule_page(status="built"), estimate=estimate_page(method=method))
        assert run(tmp_path) == (1, [MOMENT_LINE], ""), method


def test_moment_a_kind_of_moment_a_first_event_and_a_method_not_by_hand_pass(tmp_path):
    for method in (
        "by hand at a /handoff, against the close of its Retro",
        "by hand, the vault read after the first close of a sprint",
        "pytest tests/test_x.py, the first run after the render",
        "pytest tests/test_x.py, the first run after the render; by hand at a /retro",
    ):
        seed(tmp_path, rule=rule_page(status="built"), estimate=estimate_page(method=method))
        assert run(tmp_path) == (0, [], ""), method


def test_moment_the_one_predicate(tmp_path):
    # the predicate pre-spec imports; a `;` splits the parts of a method
    assert lint.tied_to_a_one_off_moment("by hand at the first /retro after the render")
    assert not lint.tied_to_a_one_off_moment("by hand once; the first session after the change")


def test_waits_the_one_predicate_names_another_session(tmp_path):
    # the predicate pre-spec imports; a `;` splits the parts of a method (case 670.4)
    for method in (
        "pytest tests/test_x.py; by hand in a later session",
        "by hand at the /hi of the next session",
        "by hand in a session after the render",
        "by hand after the librarian's run",
        "by hand at /hi",
        "by hand, a CI run on GitHub, in a session of the sprint plugin before its close",
        "by hand, at the end of Work Mode of the session that closes entity-sprint-plugin",
    ):
        assert lint.waits_for_another_session(method), method
    for method in (
        "pytest tests/test_x.py; the person's answer at the /hi of the next session",
        "pytest tests/test_x.py; by hand at the Retro of this session",
        "uv run --project .guppi guppi render --check; .claude/skills/hi/SKILL.md read",
    ):
        assert not lint.waits_for_another_session(method), method


def test_waits_a_part_that_waits_for_an_event_it_names_is_no_wait(tmp_path):
    # a part that opens with `after`, or `by hand, after`, and names its event
    # before a colon (case 781)
    for method in (
        "by hand, after a pull request from a second account: the output read",
        "pytest tests/test_x.py; after the librarian's run of a session: brief.md read",
    ):
        assert not lint.waits_for_another_session(method), method
    for method in (
        "by hand after the librarian's run",
        "by hand at the /hi of the next session after the change: read",
    ):
        assert lint.waits_for_another_session(method), method
    assert lint.waits_for_an_event("after a pull request from a second account: read")
    assert not lint.waits_for_an_event("after a pull request from a second account")
    assert not lint.waits_for_an_event("read after a pull request: x")


def test_waits_the_lint_run_gives_no_finding_on_a_live_page(tmp_path):
    method = "pytest tests/test_x.py; by hand in a later session"
    seed(tmp_path, rule=rule_page(status="built"), estimate=estimate_page(method=method))
    assert run(tmp_path) == (0, [], "")


def test_a_moc_method_needs_a_make_target_that_exists(tmp_path):
    wiki = seed(tmp_path, rule=rule_page(status="built"))
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
    wiki = seed(
        tmp_path,
        rule=rule_page(status="built"),
        estimate=estimate_page(method="One reading by hand."),
    )
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
    wiki = seed(tmp_path, rule=rule_page(status="built"))
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


# --- a render child of a full MOC is not counted against the MOC's reading (case 459) ------

MOC_FINDING = (
    "estimates/estimate-root-holds: method: says by hand while estimate-x-works names a test file"
)


def render_root(render_mode="full"):
    """`rule-root` forced by render, its one Estimate a reading; `render_mode` None leaves
    the field out."""
    mode = f"render_mode: {render_mode}\n" if render_mode else ""
    return (
        "---\ntype: rule\nkind: MOC\npurpose: Prevents root\nstatus: built\n"
        f"enforcement: render\n{mode}children: [rule-x]\nestimates: [estimate-root-holds]\n"
        "origin: raw/2026-09-09/ledger.md#case-1\n---\n\n## Purpose\n\nr\n\n"
        "## Render\n\n<!-- rule-root -->\nr\n<!-- rule-x -->\n<!-- /rule-root -->\n\n"
        "## History\n\n- created\n"
    )


def render_child():
    """`rule-x` forced by render and spliced into its parent's file; its Estimate names
    `tests/test_x.py` by default."""
    return rule_page(enforcement="render", implementation_ref=None).replace(
        "## History", "## Render\n\n<!-- rule-x -->\nx\n<!-- /rule-x -->\n\n## History"
    )


def seed_render_moc(tmp_path, root, child):
    wiki = seed(tmp_path, rule=child)
    write(wiki / "rules" / "rule-root.md", root)
    write(
        wiki / "estimates" / "estimate-root-holds.md",
        estimate_page(target="rule-root", method="One reading at a session start, by hand."),
    )


def test_a_full_moc_reading_over_a_render_child_with_a_tested_estimate_passes(tmp_path):
    seed_render_moc(tmp_path, render_root(), render_child())
    assert run(tmp_path) == (0, [], "")


def test_a_full_moc_reading_over_a_child_not_forced_by_render_is_a_method_finding(tmp_path):
    seed_render_moc(tmp_path, render_root(), rule_page(status="built"))
    _, lines, _ = run(tmp_path)
    assert lines == [MOC_FINDING]


def test_a_moc_reading_without_render_mode_full_over_a_render_child_is_a_method_finding(
    tmp_path,
):
    seed_render_moc(tmp_path, render_root(render_mode=None), render_child())
    _, lines, _ = run(tmp_path)
    assert lines == [MOC_FINDING]


def test_cli_dispatches_to_lint(tmp_path, monkeypatch, capsys):
    from guppi import cli

    seed(tmp_path, rule=rule_page(status="draft"))
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["lint"]) == 1
    assert "rules/rule-x: status" in capsys.readouterr().out


# --- decision lists, deferred_by, History links, an estimate's target (cases 52 and 53) ------

DECISIONS_YAML = """\
type: decision
properties:
  required: [type, case, status, origin]
  optional: [create, update, delete, defer, source, supersedes, superseded_by]
  values:
    status: [current, superseded, archived]
body:
  required: ["## Context", "## Problem", "## History"]
  optional: ["## Given", "## When", "## Criterion", "## Note"]
"""


def decision_page(lists="defer: [rule-x]"):
    """A decision page whose kind lists are the given frontmatter lines (case 59.4)."""
    return (
        f"---\ntype: decision\ncase: '50'\nstatus: current\n{lists}\n"
        f"origin: {ORIGIN}\n---\n\n## Context\n\nc\n\n## Problem\n\np\n\n## History\n\n- created\n"
    )


def seed_decisions(tmp_path, page=None):
    wiki = seed(tmp_path)
    write(wiki / "decisions" / "schema.yaml", described(DECISIONS_YAML))
    write(wiki / "decisions" / "decision-case-50.md", decision_page() if page is None else page)
    return wiki


def test_a_decision_with_kind_lists_naming_pages_is_clean(tmp_path):
    seed_decisions(tmp_path, decision_page("update: [rule-x, case-schema]\ndefer: [rule-root]"))
    assert run(tmp_path) == (0, [], "")


def test_a_decision_with_none_of_the_four_lists_is_a_decision_finding(tmp_path):
    seed_decisions(tmp_path, decision_page("source: [x]"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "decisions/decision-case-50: decision: none of create, update, delete, defer is present"
    ]


def test_a_parent_decision_with_children_and_no_kind_list_is_clean(tmp_path):  # (case 544.9)
    wiki = seed_decisions(tmp_path, decision_page("children: ['[[decision-case-50.1]]']"))
    write(wiki / "decisions" / "decision-case-50.1.md", decision_page("defer: [rule-x]"))
    assert not [line for line in run(tmp_path)[1] if "decision:" in line]


def test_a_parent_decision_with_neither_is_a_decision_finding(tmp_path):  # (case 544.9)
    seed_decisions(tmp_path, decision_page("children: []"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "decisions/decision-case-50: decision: none of create, update, delete, defer is present"
    ]


def test_a_parent_origin_is_found_by_a_line_of_a_sub_case(tmp_path):  # (case 544.9)
    seed(tmp_path, rule=rule_page(origin="raw/2026-09-10/1610/ledger.md#case-9"))
    ledger = "- decision[case 9.1][update][rule-x]{ref:rule-x}\n"
    write(tmp_path / "vault" / "raw" / "2026-09-10" / "1610" / "ledger.md", ledger)
    assert run(tmp_path) == (0, [], "")


def test_a_parent_origin_with_no_line_of_either_is_an_origin_finding(tmp_path):  # (case 544.9)
    seed(tmp_path, rule=rule_page(origin="raw/2026-09-10/1610/ledger.md#case-9"))
    ledger = "- decision[case 91][update][rule-x]{ref:rule-x}\n"
    write(tmp_path / "vault" / "raw" / "2026-09-10" / "1610" / "ledger.md", ledger)
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: origin: raw/2026-09-10/1610/ledger.md#case-9: no line carrying [case 9]"
    ]


def test_kind_or_target_slug_on_a_decision_is_a_decision_finding(tmp_path):
    seed_decisions(tmp_path, decision_page("defer: [rule-x]\nkind: [defer]\ntarget_slug: [rule-x]"))
    _, lines, _ = run(tmp_path)
    # the clean version removes the bracket of the pointer from the code, so it is left out
    # here (case 822)
    assert [line.removesuffix(" (case 59.4)") for line in lines] == [
        "decisions/decision-case-50: decision: kind is no longer a field",
        "decisions/decision-case-50: decision: target_slug is no longer a field",
    ]


def test_a_list_slug_naming_neither_a_live_nor_an_archived_page_is_a_decision_finding(
    tmp_path,
):
    seed_decisions(tmp_path, decision_page("defer: [rule-nowhere]"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "decisions/decision-case-50: decision: defer names rule-nowhere, "
            "which no live or archived page carries"
        )
    ]


def test_a_list_slug_naming_an_archived_page_is_not_a_finding(tmp_path):
    seed_decisions(tmp_path, decision_page("update: [rule-gone]"))
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-10" / "rules"
    write(archived / "rule-gone.md", "---\ntype: rule\n---\n")
    assert run(tmp_path) == (0, [], "")


def test_a_slug_without_a_prefix_in_a_list_is_not_looked_up(tmp_path):
    seed_decisions(tmp_path, decision_page("update: [case-schema]"))
    assert run(tmp_path) == (0, [], "")


# --- the prefixes of a Decision list are the one table of materialize (case 460.3) ----------


def test_a_list_slug_with_the_decision_prefix_naming_no_page_is_a_decision_finding(tmp_path):
    seed_decisions(tmp_path, decision_page("update: [rule-x]\ndefer: [decision-case-51]"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "decisions/decision-case-50: decision: defer names decision-case-51, "
            "which no live or archived page carries"
        )
    ]


def test_a_list_slug_naming_a_live_or_archived_decision_page_is_clean(tmp_path):
    wiki = seed_decisions(
        tmp_path, decision_page("update: [rule-x]\ndefer: [decision-case-49, decision-case-48]")
    )
    write(wiki / "decisions" / "decision-case-49.md", decision_page())
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-10" / "decisions"
    write(archived / "decision-case-48.md", "---\ntype: decision\n---\n")
    assert run(tmp_path) == (0, [], "")


def test_a_list_slug_without_a_prefix_of_category_of_is_not_looked_up(tmp_path):
    # `decisions` and `case-460` open with no prefix `category_of` knows: things outside the
    # vault, not looked up
    seed_decisions(tmp_path, decision_page("update: [rule-x]\ndefer: [decisions, case-460]"))
    assert run(tmp_path) == (0, [], "")


def test_a_deferred_by_naming_no_decision_is_a_ref_finding(tmp_path):
    seed_decisions(tmp_path)
    write(
        tmp_path / "vault" / "wiki" / "rules" / "rule-x.md",
        rule_page(deferred_by="[decision-case-51]"),
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: ref: deferred_by names decision-case-51, which no live or archived page carries"
    ]


def test_a_history_wikilink_to_nothing_is_a_ref_finding(tmp_path):
    seed(tmp_path, rule=rule_page().replace("- created", "- created · [[decision-case-99]]"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: ref: body names decision-case-99, which no live or archived page carries"
    ]


def test_an_estimate_whose_target_is_not_an_entity_or_rule_is_a_status_finding(tmp_path):
    wiki = seed(tmp_path, estimate=estimate_page(target="lesson-l"))
    write(
        wiki / "lessons" / "schema.yaml",
        "type: lesson\nproperties:\n  required: [type]\n  optional: []\nbody:\n  required: []\n  optional: []\nfields: {type: d}\n",
    )
    write(wiki / "lessons" / "lesson-l.md", "---\ntype: lesson\n---\n")
    _, lines, _ = run(tmp_path)
    assert (
        "estimates/estimate-x-works: status: target lesson-l is a lesson, not an entity or rule"
        in lines
    )
    assert not any("lesson-l: orphan" in line for line in lines)  # a lesson is never an orphan


def test_an_insight_nothing_names_is_not_an_orphan_finding(tmp_path):  # (case 156)
    wiki = seed(tmp_path)
    write(
        wiki / "insights" / "schema.yaml",
        "type: insight\nproperties:\n  required: [type]\n  optional: [status]\nbody:\n  required: []\n  optional: []\nfields: {type: d, status: d}\n",
    )
    write(wiki / "insights" / "insight-i.md", "---\ntype: insight\nstatus: actioned\n---\n")
    _, lines, _ = run(tmp_path)
    assert not any("insight-i: orphan" in line for line in lines)


# --- lint accepts both shapes of a decision page and an Estimate page (case 72.6) ---------


def criterion_decision(*lines):
    """The default decision page with a `## Criterion` section holding the given lines."""
    return decision_page().replace(
        "## History", "## Criterion\n\n" + "\n".join(lines) + "\n\n## History"
    )


def block_estimate(*cases):
    """The default Estimate page whose `## Criterion` is one `### case N` block per case."""
    blocks = "\n\n".join(f"### case {c}\n\n**when:** w.\n\n**then:** t." for c in cases)
    return estimate_page().replace("## Criterion\n\ncr\n\n", f"## Criterion\n\n{blocks}\n\n")


def test_a_decision_without_when_is_not_a_finding_even_when_the_yaml_requires_it(tmp_path):
    wiki = seed_decisions(tmp_path)
    write(
        wiki / "decisions" / "schema.yaml",
        described(
            DECISIONS_YAML.replace(
                '"## Problem", "## History"', '"## Problem", "## When", "## History"'
            ).replace('"## Given", "## When", "## Criterion"', '"## Given", "## Criterion"')
        ),
    )
    assert run(tmp_path) == (0, [], "")


def test_a_criterion_link_to_a_live_or_archived_estimate_page_is_clean(tmp_path):
    seed_decisions(
        tmp_path,
        criterion_decision("- [[estimate-x-works]] § case 50", "- [[estimate-gone]] § case 49"),
    )
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-10" / "estimates"
    write(archived / "estimate-gone.md", "---\ntype: estimate\n---\n")
    assert run(tmp_path) == (0, [], "")


def test_a_criterion_link_resolving_to_no_estimate_page_is_a_ref_finding(tmp_path):
    seed_decisions(
        tmp_path,
        criterion_decision("- [[estimate-ghost]] § case 50", "- [[rule-x]] § case 50"),
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "decisions/decision-case-50: ref: ## Criterion names estimate-ghost, "
            "which no live or archived Estimate page carries"
        ),
        (
            "decisions/decision-case-50: ref: ## Criterion names rule-x, "
            "which no live or archived Estimate page carries"
        ),
    ]


def test_a_case_block_naming_a_live_or_archived_decision_page_is_clean(tmp_path):
    wiki = seed_decisions(tmp_path)
    write(wiki / "estimates" / "estimate-x-works.md", block_estimate("50", "49"))
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-10" / "decisions"
    write(archived / "decision-case-49.md", "---\ntype: decision\n---\n")
    assert run(tmp_path) == (0, [], "")  # a block is no link and no longer counted


def test_a_case_block_naming_no_decision_page_earns_no_ref_finding(tmp_path):
    # a `### case N` line of an Estimate's Criterion is not read as a link (case 506.4)
    wiki = seed_decisions(tmp_path)
    write(wiki / "estimates" / "estimate-x-works.md", block_estimate("50", "51"))
    assert run(tmp_path) == (0, [], "")


def test_a_case_block_heading_is_not_a_section_boundary():
    from guppi.pages import split_sections

    body = "## Criterion\n\n### case 50\n\n**when:** w.\n\n## Method\n\nm\n"
    assert split_sections(body) == {
        "## Criterion": "### case 50\n\n**when:** w.",
        "## Method": "m",
    }


def test_a_moc_reading_passes_beside_a_sibling_estimate_naming_a_make_target(tmp_path):
    # a second, cross-cutting Estimate of the MOC is a reading; the pipeline is
    # the sibling's, so nothing is hidden (case 212)
    wiki = seed(tmp_path, rule=rule_page(status="built"))
    write(
        wiki / "rules" / "rule-root.md",
        root_page().replace(
            "estimates: []", "estimates: [estimate-root-holds, estimate-root-names]"
        ),
    )
    write(
        wiki / "estimates" / "estimate-root-holds.md",
        estimate_page(target="rule-root", method="`make test-root`, the pipeline."),
    )
    write(
        wiki / "estimates" / "estimate-root-names.md",
        estimate_page(target="rule-root", method="One reading of the Spec at the close, by hand."),
    )
    assert run(tmp_path) == (0, [], "")
    # the sibling names no make target: the reading is a finding as before
    write(
        wiki / "estimates" / "estimate-root-holds.md",
        estimate_page(target="rule-root", method="`make test-nope`, the pipeline."),
    )
    _, lines, _ = run(tmp_path)
    assert (
        "estimates/estimate-root-names: method: says by hand while estimate-x-works names a test file"
        in lines
    )


def test_a_moc_method_naming_a_make_target_passes_whatever_else_it_says(tmp_path):
    # the target is looked for first; "by hand" beside it is not a finding (case 112.1)
    wiki = seed(tmp_path, rule=rule_page(status="built"))
    write(
        wiki / "rules" / "rule-root.md",
        root_page().replace("estimates: []", "estimates: [estimate-root-holds]"),
    )
    write(
        wiki / "estimates" / "estimate-root-holds.md",
        estimate_page(
            target="rule-root",
            method="`make test-root`, the pipeline; the live reading by hand.",
        ),
    )
    assert run(tmp_path) == (0, [], "")


# --- the commands of a project, and a MOC's pipeline as its test files (case 820.3) --------

MOC_NO_FORM = (
    "estimates/estimate-root-holds: method: a MOC's Estimate names no `make <target>` "
    "or `pytest` with test files"
)


def seed_moc_method(tmp_path, method, sibling=None):
    """rule-root, a MOC, with one Estimate of `method`, and a second of `sibling` if given;
    the child rule-x carries a tested Estimate."""
    wiki = seed(tmp_path, rule=rule_page(status="built"))
    slugs = "estimate-root-holds" + (", estimate-root-sibling" if sibling else "")
    write(
        wiki / "rules" / "rule-root.md",
        root_page().replace("estimates: []", f"estimates: [{slugs}]"),
    )
    write(
        wiki / "estimates" / "estimate-root-holds.md",
        estimate_page(target="rule-root", method=method),
    )
    if sibling:
        write(
            wiki / "estimates" / "estimate-root-sibling.md",
            estimate_page(target="rule-root", method=sibling),
        )
    return wiki


def test_a_leaf_method_naming_a_command_of_the_project_passes(tmp_path):
    for method in (
        "uv run --project .guppi guppi test over the suite",
        "uv run --project .guppi guppi check over the vault",
        "`guppi style` over the code",
    ):
        seed(tmp_path, rule=rule_page(status="built"), estimate=estimate_page(method=method))
        assert run(tmp_path) == (0, [], ""), method


def test_a_moc_method_naming_pytest_with_test_files_that_exist_passes(tmp_path):
    seed_moc_method(tmp_path, "uv run --project .guppi pytest tests/test_x.py, the pipeline")
    assert run(tmp_path) == (0, [], "")


def test_a_moc_method_naming_a_test_file_that_does_not_exist_is_a_finding(tmp_path):
    seed_moc_method(tmp_path, "uv run --project .guppi pytest tests/test_x.py tests/test_gone.py")
    _, lines, _ = run(tmp_path)
    assert lines == [
        "estimates/estimate-root-holds: method: names tests/test_gone.py, which does not exist"
    ]


def test_a_moc_method_naming_pytest_a_path_or_a_command_alone_is_a_finding(tmp_path):
    for method in (
        "pytest over the pipeline",
        "tests/test_x.py, the pipeline",
        "uv run --project .guppi guppi test over the suite",
    ):
        seed_moc_method(tmp_path, method)
        _, lines, _ = run(tmp_path)
        assert lines == [MOC_NO_FORM], method


def test_a_moc_reading_passes_beside_a_sibling_naming_pytest_with_test_files(tmp_path):
    reading = "One reading of the Spec at the close, by hand."
    seed_moc_method(tmp_path, reading, sibling="pytest tests/test_x.py, the pipeline")
    assert run(tmp_path) == (0, [], "")
    # the sibling's test file does not exist: the reading is a finding as before
    seed_moc_method(tmp_path, reading, sibling="pytest tests/test_gone.py, the pipeline")
    _, lines, _ = run(tmp_path)
    assert (
        "estimates/estimate-root-holds: method: says by hand while estimate-x-works names a test file"
        in lines
    )


# --- the edge Rule → Entity — applies_to and rules under ref (case 305.5) -------------------

ENTITIES_YAML = """\
type: entity
properties:
  required: [type, kind, purpose, status, estimates, origin]
  optional: [parent, children, rules]
  values:
    kind: [MOC, Leaf]
    status: [draft, built, archived]
body:
  required: ["## Purpose", "## History"]
"""


def entity_page(**over):
    props = {
        "type": "entity",
        "kind": "MOC",
        "purpose": "The thing",
        "status": "draft",
        "children": "[]",
        "estimates": "[]",
        "origin": ORIGIN,
    }
    props.update(over)
    front = "\n".join(f"{k}: {v}" for k, v in props.items() if v is not None)
    return f"---\n{front}\n---\n\n## Purpose\n\nt\n\n## History\n\n- created\n"


def seed_edge(tmp_path, applies_to="[entity-thing]", rules="[rule-x]"):
    """rule-x guards entity-thing; the entity lists it back."""
    wiki = seed(tmp_path, rule=rule_page(applies_to=applies_to))
    write(wiki / "entities" / "schema.yaml", described(ENTITIES_YAML))
    write(wiki / "entities" / "entity-thing.md", entity_page(rules=rules))
    return wiki


def test_an_edge_written_on_both_sides_is_no_finding(tmp_path):
    seed_edge(tmp_path)
    assert run(tmp_path) == (0, [], "")


def test_an_applies_to_on_no_entity_is_a_ref_finding(tmp_path):
    seed_edge(tmp_path, applies_to="[entity-nowhere, rule-root, entity-thing]", rules="[rule-x]")
    _, lines, _ = run(tmp_path)
    assert lines == [
        "rules/rule-x: ref: applies_to names entity-nowhere, which no live or archived page carries",
        "rules/rule-x: ref: applies_to names rule-root, which is not an entity",
    ]


def test_a_rules_that_disagrees_with_the_live_applies_to_is_a_ref_finding(tmp_path):
    seed_edge(tmp_path, rules="[rule-root]")
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "entities/entity-thing: ref: rules differs from the applies_to of the live rules: "
            "+rule-root, -rule-x"
        )
    ]


# --- layout (case 315) ----------------------------------------------------------------


def test_a_page_under_the_folder_of_another_category_is_a_layout_finding(tmp_path):
    wiki = seed(tmp_path)
    write(wiki / "rules" / "estimate-stray.md", estimate_page())
    _, lines, _ = run(tmp_path)
    assert "rules/estimate-stray: layout: type is 'estimate' under rules/" in lines


def test_a_slug_field_that_is_not_the_filename_is_a_layout_finding(tmp_path):
    seed(tmp_path, rule=rule_page(slug="rule-other"))
    _, lines, _ = run(tmp_path)
    assert lines == ["rules/rule-x: layout: slug is 'rule-other', the file is rule-x"]


def test_a_root_file_no_rule_names_is_a_layout_finding(tmp_path):
    wiki = seed(tmp_path)
    write(wiki / "stray.md", "# stray")
    _, lines, _ = run(tmp_path)
    assert lines == ["wiki/stray: layout: no live rule page names this file"]


def test_a_root_file_a_rule_names_is_silent(tmp_path):
    wiki = seed(tmp_path)
    write(wiki / "kept.md", "# kept")
    write(
        wiki / "rules" / "rule-keeper.md",
        rule_page(
            purpose="Prevents kept.md from drifting",
            estimates="[]",
            status="draft",
            enforcement="check",
            implementation_ref=None,
        ),
    )
    _, lines, _ = run(tmp_path)
    assert [line for line in lines if "layout" in line] == []


# The target `lint` of the `Makefile` this repository keeps for now runs `guppi check` and
# nothing else (case 820.7); the steps of the vault checks are tested in `test_check.py`. A
# test runs the real recipe of the `Makefile` with a fake `uv` first on the search path, so
# the recipe is read at any time and nothing of the vault is staged (case 637.3).

MAKEFILE = Path(__file__).resolve().parents[2] / "Makefile"
CHECK_CALL = "run --project .guppi guppi check"
FAKE_UV = """\
#!/bin/sh
if read -r _; then input=read; else input=empty; fi
echo "$* stdin:$input" >> "$FAKE_UV_LOG"
echo "fake uv: $*"
if [ "$*" = "$FAKE_UV_FAIL" ]; then exit 1; fi
exit 0
"""


def make_lint(tmp_path, fail=""):
    """`make lint` of the repository's Makefile in a work folder holding that file alone,
    a fake `uv` first on the search path and a line on the caller's stdin; the calls the
    fake recorded, and the work folder before and after."""
    if shutil.which("make") is None:
        pytest.skip("no make on the search path")
    if not MAKEFILE.is_file():  # the clean version holds no `Makefile` (case 822)
        pytest.skip("no Makefile in this project")
    work, bin_dir = tmp_path / "work", tmp_path / "bin"
    work.mkdir()
    bin_dir.mkdir()
    shutil.copyfile(MAKEFILE, work / "Makefile")
    fake = bin_dir / "uv"
    fake.write_text(FAKE_UV, encoding="utf-8", newline="\n")
    fake.chmod(0o755)
    log = tmp_path / "calls.log"
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env.get("PATH", "")
    env["FAKE_UV_LOG"] = log.as_posix()
    env["FAKE_UV_FAIL"] = fail
    before = {p.name: p.read_bytes() for p in work.iterdir()}
    done = subprocess.run(
        ["make", "lint"],
        check=False,
        cwd=work,
        env=env,
        input="a line no step may read\n",
        capture_output=True,
        text=True,
        timeout=120,
    )
    calls = log.read_text(encoding="utf-8").splitlines() if log.exists() else []
    after = {p.name: p.read_bytes() for p in work.iterdir()}
    return done, calls, before, after


def test_the_makefile_lint_target_runs_guppi_check_alone(tmp_path):
    done, calls, before, after = make_lint(tmp_path)
    assert calls == [f"{CHECK_CALL} stdin:empty"]
    printed = [line for line in done.stdout.splitlines() if line.startswith("fake uv: ")]
    assert printed == [f"fake uv: {CHECK_CALL}"]
    assert done.returncode == 0, done.stdout + done.stderr
    assert after == before


def test_the_makefile_lint_target_is_red_when_guppi_check_is(tmp_path):
    done, calls, before, after = make_lint(tmp_path, fail=CHECK_CALL)
    assert calls == [f"{CHECK_CALL} stdin:empty"]
    assert done.returncode != 0
    assert after == before
