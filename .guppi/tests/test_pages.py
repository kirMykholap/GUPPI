"""The ref fields as quoted wikilinks (case 148.1): the writer wraps, the readers strip."""

from guppi import generate, materialize
from guppi.pages import REF_FIELDS, read_page, slug_of, strip_refs

BRACKETED = """---
type: rule
kind: Leaf
parent: "[[rule-harness]]"
estimates: ["[[estimate-x]]", "[[estimate-y]]"]
deferred_by: ["[[decision-case-9]]"]
implementation_ref: [guppi/x.py]
---

## Purpose

p
"""
BARE = (
    BRACKETED.replace('"[[rule-harness]]"', "rule-harness")
    .replace('["[[estimate-x]]", "[[estimate-y]]"]', "[estimate-x, estimate-y]")
    .replace('["[[decision-case-9]]"]', "[decision-case-9]")
)


def test_read_page_strips_the_brackets_and_reads_the_bare_form_the_same(tmp_path):
    for text in (BRACKETED, BARE):
        path = tmp_path / "rule-x.md"
        path.write_text(text, encoding="utf-8")
        page = read_page(path, "rules")
        assert page.error is None
        assert page.props["parent"] == "rule-harness"
        assert page.props["estimates"] == ["estimate-x", "estimate-y"]
        assert page.props["deferred_by"] == ["decision-case-9"]
        assert page.props["implementation_ref"] == ["guppi/x.py"]  # a path, not a ref


def test_the_writer_wraps_page_slugs_and_leaves_slugs_without_a_prefix_bare():
    props = {
        "type": "decision",
        "case": "1",
        "update": ["rule-x", "case-schema", "index"],
        "supersedes": ["decision-case-3"],
        "origin": "raw/2026-09-14/1633/ledger.md#case-1",
    }
    text = generate.frontmatter(props, "decisions")
    assert 'update: ["[[rule-x]]", case-schema, index]' in text
    assert 'supersedes: ["[[decision-case-3]]"]' in text
    assert "origin: raw/2026-09-14/1633/ledger.md#case-1" in text
    props = {"type": "rule", "parent": "rule-harness", "estimates": ["estimate-x"]}
    text = generate.frontmatter(props, "rules")
    assert 'parent: "[[rule-harness]]"' in text and 'estimates: ["[[estimate-x]]"]' in text
    # already bracketed values are not wrapped twice
    assert generate.wikilink("[[rule-x]]") == "[[rule-x]]"


def test_slug_of_and_strip_refs_cover_every_ref_field():
    assert slug_of("[[rule-x]]") == "rule-x" and slug_of("rule-x") == "rule-x"
    assert slug_of("[[rule-x|alias]]") == "rule-x" and slug_of(3) == 3
    props = {key: ["[[a]]", "b"] for key in REF_FIELDS}
    props["tags"] = ["[[not-a-ref]]"]
    stripped = strip_refs(dict(props))
    assert all(stripped[key] == ["a", "b"] for key in REF_FIELDS)
    assert stripped["tags"] == ["[[not-a-ref]]"]


def test_page_estimates_reads_through_the_brackets(tmp_path):
    rules = tmp_path / "vault" / "wiki" / "rules"
    rules.mkdir(parents=True)
    (rules / "rule-x.md").write_text(BRACKETED, encoding="utf-8")
    assert materialize.page_estimates(tmp_path, "rules", "rule-x") == ["estimate-x", "estimate-y"]
