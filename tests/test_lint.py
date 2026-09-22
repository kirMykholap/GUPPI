"""`guppi lint`: one finding per defect class, nothing on a clean vault.

Rule page: `vault/wiki/rules/rule-lint.md`. Each test seeds a small vault with its own
schemas, one page per defect, and asserts the finding names the page and the class.
"""

import io
import textwrap

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
    its lists carry — the shape lint checks since case 304.8."""
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
    """A page of the shape before case 193: `## Context` and `## Method` as sections, no
    `method` field — counted by `unmigrated`."""
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


UNMIGRATED_ONE = "estimates: unmigrated: 1 page in the shape before case 193"


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


def test_a_list_in_a_single_field_is_a_schema_finding(tmp_path):
    # case 362.1: a field `properties.single` names holds one value, never a list
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
    assert lines == [  # case 149.3: the stem of a root file; a schema is no file since case 304
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
    # case 202: red between a change of a promise and its reading, by design
    seed(tmp_path, rule=rule_page(status="draft"), estimate=estimate_page(status="pending"))
    _, lines, _ = run(tmp_path)
    assert lines == ["estimates/estimate-x-works: unread: pending"]
    seed(tmp_path, rule=rule_page(status="draft"), estimate=estimate_page(status="failed"))
    _, lines, _ = run(tmp_path)
    assert lines == ["estimates/estimate-x-works: unread: failed"]


def test_a_page_of_the_old_shape_is_counted_once_in_unmigrated(tmp_path):
    # case 202: one line for the remainder of the recut, none at zero
    wiki = seed(tmp_path, rule=rule_page(status="built"), estimate=old_estimate_page())
    _, lines, _ = run(tmp_path)
    assert lines == [UNMIGRATED_ONE]
    write(wiki / "estimates" / "estimate-x-works.md", estimate_page())
    assert run(tmp_path) == (0, [], "")
    write(
        wiki / "estimates" / "estimate-x-works.md",
        estimate_page().replace("## Criterion\n\ncr", "## Criterion\n\n### case 1\n\ncr"),
    )
    _, lines, _ = run(tmp_path)
    assert lines[-1] == UNMIGRATED_ONE  # a block on a page with a method field still counts
    assert len(lines) == 2  # the block's ref finding beside it


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
            "estimates/estimate-x-works: method: names no tests/ file, pytest or make target "
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
    # case 325.2: a parent carries one opening line per child; the closing line is the
    # renderer's own, and a stray one silently swallows the text after it
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


def test_a_leaf_method_naming_a_reading_without_by_hand_is_a_method_finding(tmp_path):
    # case 330.1: `by hand` is the one spelling of a reading; the word `reading` alone is not one
    seed(
        tmp_path,
        rule=rule_page(status="built"),
        estimate=estimate_page(method="one reading of the first reply of a session"),
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "estimates/estimate-x-works: method: names no tests/ file, pytest or make target "
            "and is not a reading"
        )
    ]


def test_a_leaf_method_field_names_a_test_a_make_target_or_a_reading(tmp_path):
    # case 202: the field is read; a test command, a make target or a reading passes
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


def test_the_method_section_is_read_on_a_page_of_the_old_shape(tmp_path):
    seed(
        tmp_path,
        rule=rule_page(status="built"),
        estimate=old_estimate_page(method="pytest in `tests/test_gone.py`."),
    )
    _, lines, _ = run(tmp_path)
    assert lines == [
        "estimates/estimate-x-works: method: names tests/test_gone.py, which does not exist",
        UNMIGRATED_ONE,
    ]


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


def test_a_leaf_method_by_hand_is_the_exception(tmp_path):
    seed(
        tmp_path,
        rule=rule_page(status="built"),
        estimate=estimate_page(method="One reading by hand."),
    )
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


def test_cli_dispatches_to_lint(tmp_path, monkeypatch, capsys):
    from guppi import cli

    seed(tmp_path, rule=rule_page(status="draft"))
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["lint"]) == 1
    assert "rules/rule-x: status" in capsys.readouterr().out


# --- cases 52 and 53: decision lists, deferred_by, History links, an estimate's target ------

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


def test_kind_or_target_slug_on_a_decision_is_a_decision_finding(tmp_path):
    seed_decisions(tmp_path, decision_page("defer: [rule-x]\nkind: [defer]\ntarget_slug: [rule-x]"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        "decisions/decision-case-50: decision: kind is no longer a field (case 59.4)",
        "decisions/decision-case-50: decision: target_slug is no longer a field (case 59.4)",
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


def test_a_rule_class_slug_in_a_list_is_not_looked_up(tmp_path):
    seed_decisions(tmp_path, decision_page("update: [case-schema]"))
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


def test_an_insight_nothing_names_is_not_an_orphan_finding(tmp_path):  # case 156
    wiki = seed(tmp_path)
    write(
        wiki / "insights" / "schema.yaml",
        "type: insight\nproperties:\n  required: [type]\n  optional: [status]\nbody:\n  required: []\n  optional: []\nfields: {type: d, status: d}\n",
    )
    write(wiki / "insights" / "insight-i.md", "---\ntype: insight\nstatus: actioned\n---\n")
    _, lines, _ = run(tmp_path)
    assert not any("insight-i: orphan" in line for line in lines)


# --- case 72.6: lint accepts both shapes of a decision page and an Estimate page ---------


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
    _, lines, _ = run(tmp_path)
    assert lines == [UNMIGRATED_ONE]  # the blocks are the old shape, nothing else


def test_a_case_block_naming_no_decision_page_is_a_ref_finding(tmp_path):
    wiki = seed_decisions(tmp_path)
    write(wiki / "estimates" / "estimate-x-works.md", block_estimate("50", "51"))
    _, lines, _ = run(tmp_path)
    assert lines == [
        (
            "estimates/estimate-x-works: ref: ## Criterion names case 51, "
            "and no live or archived page decision-case-51 exists"
        ),
        UNMIGRATED_ONE,
    ]


def test_a_case_block_heading_is_not_a_section_boundary():
    from guppi.pages import split_sections

    body = "## Criterion\n\n### case 50\n\n**when:** w.\n\n## Method\n\nm\n"
    assert split_sections(body) == {
        "## Criterion": "### case 50\n\n**when:** w.",
        "## Method": "m",
    }


def test_a_moc_reading_passes_beside_a_sibling_estimate_naming_a_make_target(tmp_path):
    # case 212: a second, cross-cutting Estimate of the MOC is a reading; the pipeline is
    # the sibling's, so nothing is hidden
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
    # case 112.1: the target is looked for first; "by hand" beside it is not a finding
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


# --- case 305.5: the edge Rule → Entity — applies_to and rules under ref -------------------

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
