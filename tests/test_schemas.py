"""The six category schemas, read from the live `vault/wiki/<category>/schema.yaml` — the
Render of `rule-<category>-schema` (case 304): a page in the shape has no `schema` finding;
a required field missing, a value outside the list, a conditional not met and a required
section missing earn one finding each (`estimate-<category>-schema-checked`)."""

from pathlib import Path

import pytest
import yaml

from guppi import lint
from guppi.pages import CATEGORIES, Page

REPO = Path(__file__).resolve().parent.parent


def schema(category):
    path = REPO / "vault" / "wiki" / category / "schema.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def sample(field, values):
    """A value inside the list when the schema has one — the last, a Leaf rather than a MOC — a plain word otherwise."""
    allowed = values.get(field)
    return allowed[-1] if allowed else "x"


def page_in_shape(category, data):
    """The smallest page the schema accepts: every required field, the fields of every
    conditional its `when` matches, every required section."""
    props = data.get("properties") or {}
    body = data.get("body") or {}
    values = props.get("values") or {}
    fields = {f: sample(f, values) for f in props.get("required") or []}
    for rule in props.get("conditional") or []:
        if all(str(fields.get(k)) == str(v) for k, v in (rule.get("when") or {}).items()):
            for f in rule.get("required") or []:
                fields.setdefault(f, sample(f, values))
    sections = {s: "t" for s in body.get("required") or []}
    for rule in body.get("conditional") or []:
        if all(str(fields.get(k)) == str(v) for k, v in (rule.get("when") or {}).items()):
            for s in rule.get("required") or []:
                sections.setdefault(s, "t")
    page = Page(category=category, slug=f"{category[:-1]}-x", path=Path(f"{category}-x.md"))
    page.props, page.sections = fields, sections
    return page


def findings(page, data):
    if page.category == "decisions":
        data = lint.without_when(data)
    return [f.text for f in lint.check_schema(page, data)]


@pytest.mark.parametrize("category", CATEGORIES)
def test_a_page_in_the_shape_has_no_finding(category):
    data = schema(category)
    assert findings(page_in_shape(category, data), data) == []


@pytest.mark.parametrize("category", CATEGORIES)
def test_a_required_field_missing_is_one_finding(category):
    data = schema(category)
    page = page_in_shape(category, data)
    field = (data["properties"]["required"])[-1]
    del page.props[field]
    assert findings(page, data) == [f"{category}/{page.slug}: schema: missing field {field}"]


def test_an_estimate_without_method_is_one_finding():
    """Case 506.1: `method` is a required field of an Estimate, so a page without it earns
    one `schema` finding. Skipped until the librarian renders the live file of 506.1."""
    data = schema("estimates")
    if "method" not in data["properties"]["required"]:
        pytest.skip("estimates/schema.yaml waits for the librarian's render of case 506.1")
    page = page_in_shape("estimates", data)
    del page.props["method"]
    assert findings(page, data) == ["estimates/estimate-x: schema: missing field method"]


def test_a_decision_page_without_context_has_no_finding():
    """Case 513.1: `## Context` is an optional section of a Decision page — the Case file
    keeps the context — so a page with `## Problem` and `## History` alone earns no
    `schema` finding. Skipped until the librarian renders the live file of 513.1."""
    data = schema("decisions")
    if "## Context" in data["body"]["required"]:
        pytest.skip("decisions/schema.yaml waits for the librarian's render of case 513.1")
    page = page_in_shape("decisions", data)
    page.sections.pop("## Context", None)
    assert "## Problem" in page.sections and "## History" in page.sections
    assert findings(page, data) == []


def test_a_decision_page_without_problem_with_recommend_parent_and_children_has_no_finding():
    """Case 544.8: `## Problem` is optional and `## Recommend`, `parent` and `children` are
    known to the schema of a Decision page, so the page of a sub-case or of its parent earns
    no `schema` finding. Skipped until the librarian renders the live file of 544.8."""
    data = schema("decisions")
    if "## Problem" in data["body"]["required"]:
        pytest.skip("decisions/schema.yaml waits for the librarian's render of case 544.8")
    page = page_in_shape("decisions", data)
    page.sections.pop("## Problem", None)
    page.sections["## Recommend"] = "- **Which?**\n  - Answer: yes."
    page.props["parent"] = "decision-case-9"
    page.props["children"] = ["decision-case-9.1", "decision-case-9.2"]
    assert findings(page, data) == []


@pytest.mark.parametrize("category", CATEGORIES)
def test_a_value_outside_the_list_is_one_finding(category):
    data = schema(category)
    page = page_in_shape(category, data)
    field, allowed = next(iter((data["properties"].get("values") or {}).items()))
    page.props[field] = "zzz"
    assert findings(page, data) == [
        f"{category}/{page.slug}: schema: {field} is 'zzz', not one of {allowed}"
    ]


@pytest.mark.parametrize("category", CATEGORIES)
def test_a_conditional_not_met_is_one_finding_where_the_schema_has_one(category):
    data = schema(category)
    rules = data["properties"].get("conditional") or []
    if not rules:
        pytest.skip(f"{category}: no conditional on a field")
    page = page_in_shape(category, data)
    rule = rules[0]
    page.props.update(rule["when"])
    for f in rule.get("required") or []:
        page.props.pop(f, None)
    expected = [
        f"{category}/{page.slug}: schema: missing field {f} (given {rule['when']})"
        for f in rule.get("required") or []
    ]
    assert findings(page, data) == expected


@pytest.mark.parametrize("category", CATEGORIES)
def test_a_required_section_missing_is_one_finding(category):
    data = schema(category)
    page = page_in_shape(category, data)
    section = data["body"]["required"][0]
    del page.sections[section]
    assert findings(page, data) == [f"{category}/{page.slug}: schema: missing section {section}"]
