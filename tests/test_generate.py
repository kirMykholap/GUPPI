"""`guppi generate`: pages from `materialize.yaml`, derived fields, backlinks, History, log."""

import io
from datetime import UTC, datetime
from pathlib import Path

import pytest
import yaml

from guppi import generate, lint
from guppi.pages import strip_refs

DATE = "2026-09-10"
ORIGIN = f"raw/{DATE}/ledger.md#case-1"
REPO = Path(__file__).resolve().parent.parent

# The decisions schema the tests run against: the four kind lists of case 59.4, so the
# suite does not depend on the live `vault/wiki/decisions/schema.yaml`.
DECISIONS_YAML = """\
type: decision
properties:
  required: [type, case, status, origin, sprint, created, tags]
  optional: [create, update, delete, defer, source, supersedes, superseded_by]
  values:
    status: [current, superseded, archived]
body:
  required: ["## Problem", "## History"]
  optional: ["## Context", "## Given", "## When", "## Criterion", "## Note"]
"""


def records_for(entries):
    """One minimal Decision record per Case among the entries, as materialize would make."""
    records = {}
    for entry in entries:
        case = entry.get("case")
        if case is None or entry.get("kind") not in ("create", "update", "delete", "defer"):
            continue
        record = records.setdefault(
            case,
            {
                "case": case,
                "decision": f"decision-case-{case}",
                "origin": f"raw/{DATE}/ledger.md#case-{case}",
                "targets": [],
                "tags": [],
                "case_text": {"context": "c", "problem": "p", "given": "g", "when": "w"},
            },
        )
        record["targets"].append(
            {"kind": entry["kind"], "category": entry.get("category"), "slug": entry["slug"]}
        )
    return list(records.values())


def described(text):
    """The yaml with a description under `fields` and `sections` for every listed name,
    the shape lint checks since case 304.8; a yaml that carries them already stands."""
    data = yaml.safe_load(text)
    for block, key in (("properties", "fields"), ("body", "sections")):
        if key not in data:
            data[key] = {n: "d" for n in sorted(lint.listed_names(data.get(block) or {}))}
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True)


def seed(tmp_path, entries=(), decisions=None, new_tags=(), pages=()):
    if decisions is None:
        decisions = records_for(entries)
    wiki = tmp_path / "vault" / "wiki"
    for category in ("entities", "rules", "estimates", "lessons", "insights", "decisions"):
        (wiki / category).mkdir(parents=True)
        source = REPO / "vault" / "wiki" / category / "schema.yaml"
        text = DECISIONS_YAML if category == "decisions" else source.read_text(encoding="utf-8")
        (wiki / category / "schema.yaml").write_text(
            described(text), encoding="utf-8", newline="\n"
        )
    (wiki / "sprint.md").write_text("# Sprint\n\n## migration — open\n", encoding="utf-8")
    (wiki / "tags.md").write_text(
        "# Tags\n\n| tag | meaning | aliases (ru) |\n|---|---|---|\n| harness | the harness | харнесс |\n",
        encoding="utf-8",
    )
    (wiki / "log.md").write_text("# Log\n", encoding="utf-8")
    for category, slug, text in pages:
        (wiki / category / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")
    raw = tmp_path / "vault" / "raw" / DATE
    raw.mkdir(parents=True)
    (raw / "ledger.md").write_text(
        "- decision[case 1][create][rule-root]\n- decision[case 2][update][rule-root]\n"
        "- decision[case 3][defer][rule-later]\n- decision[case 4][defer][rule-root]\n"
        "- lesson[error][x] trigger: t root_cause: r\n",
        encoding="utf-8",
    )
    data = {
        "date": DATE,
        "sprint": "migration",
        "entries": list(entries),
        "decisions": list(decisions),
        "unparsed": [],
    }
    if new_tags:
        data["new_tags"] = list(new_tags)
    (raw / "materialize.yaml").write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    return tmp_path


NOW = datetime(2026, 9, 10, 12, 0, 0, tzinfo=UTC)  # pinned: History carries the run's date


def run(project_dir):
    out, err = io.StringIO(), io.StringIO()
    code = generate.run(["--date", DATE], stdout=out, stderr=err, project_dir=project_dir, now=NOW)
    return code, out.getvalue(), err.getvalue()


def page(project_dir, category, slug):
    return (project_dir / "vault" / "wiki" / category / f"{slug}.md").read_text(encoding="utf-8")


def props(text):
    return strip_refs(yaml.safe_load(text.split("---")[1]))  # the ref fields bare (148.1)


def load_yaml(project_dir):
    path = project_dir / "vault" / "raw" / DATE / "materialize.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def create(slug, category, fields, ref=None, sections=None, tags=None, **extra):
    entry = {
        "line": extra.pop("line", 1),
        "text": "",
        "case": "1",
        "kind": "create",
        "category": category,
        "slug": slug,
        "origin": ORIGIN,
        "decision": "decision-case-1",
        "fields": fields,
    }
    if ref:
        entry["ref"] = ref
    if sections:
        entry["sections"] = sections
    if tags:
        entry["tags"] = tags
    entry.update(extra)
    return entry


ROOT = create(
    "rule-root",
    "rules",
    {"type": "rule", "kind": "MOC", "purpose": "Prevents root"},
    tags=["harness"],
)
CHILD = create(
    "rule-child",
    "rules",
    {
        "type": "rule",
        "kind": "Leaf",
        "purpose": "Prevents child",
        "enforcement": "check",
        "implementation_ref": ["guppi/x.py"],
    },
    ref="rule-root",
    sections={"Purpose": "Two lines of\npurpose."},
    tags=["harness"],
    line=2,
)
CHILD_ESTIMATE = create(
    "estimate-child-works",
    "estimates",
    {
        "type": "estimate",
        "kind": "QA",
        "purpose": "The child works",
        "method": "pytest tests/test_x.py",
    },
    ref="rule-child",
    sections={"Criterion": "the child works"},
    tags=["harness"],
    line=3,
)


def test_a_created_page_takes_the_sprint_of_its_yaml_over_the_heading(tmp_path):
    """Case 628.6: `sprint` is the yaml's, which `materialize` sets to the new sprint's id in
    the unit that creates its page; the heading of `sprint.md` names the closed one."""
    seed(tmp_path, entries=[ROOT])
    path = tmp_path / "vault" / "raw" / DATE / "materialize.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["sprint"] = "next"
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    code, _, err = run(tmp_path)
    assert code == 0, err
    assert props(page(tmp_path, "rules", "rule-root"))["sprint"] == "next"


def test_creates_yield_conformant_pages_with_backlinks_in_order(tmp_path):
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT])  # the parent comes last, on purpose
    (tmp_path / "guppi").mkdir()
    (tmp_path / "guppi" / "x.py").write_text("")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_x.py").write_text("")
    code, out, err = run(tmp_path)
    assert code == 0 and err == "", err
    root = props(page(tmp_path, "rules", "rule-root"))
    assert root["children"] == ["rule-child"] and root["status"] == "draft"
    assert (
        root["origin"] == ORIGIN and root["sprint"] == "migration" and str(root["created"]) == DATE
    )
    assert "## Children" not in page(tmp_path, "rules", "rule-root")  # 166.2: the field is the link
    child = page(tmp_path, "rules", "rule-child")
    assert props(child)["parent"] == "rule-root" and props(child)["estimates"] == [
        "estimate-child-works"
    ]
    assert "## Purpose\n\nTwo lines of\npurpose.\n" in child
    assert props(child)["implementation_ref"] == ["guppi/x.py"]
    for section in ("## Estimates", "## Parent", "## Implementation"):
        assert section not in child
    assert f"## History\n\n- {DATE} created · [[decision-case-1]]\n" in child
    estimate = page(tmp_path, "estimates", "estimate-child-works")
    assert props(estimate)["target"] == "rule-child" and props(estimate)["status"] == "pending"
    assert "## Criterion\n\nthe child works" in estimate
    # the seed is not a whole vault: its root files have no rule of their own (case 315)
    findings = [f for f in lint.lint(tmp_path) if ": layout: " not in f]
    assert findings == ["estimates/estimate-child-works: unread: pending"], findings  # 202
    log = page(tmp_path, "", "log")
    assert (
        f"- {DATE} rules/rule-root child rule-child added · [[decision-case-1]] · generate" in log
    )
    assert log.index("decisions/decision-case-1 created") < log.index("rules/rule-child created")
    assert "3 page(s) written" in out or "page(s) written" in out


def test_an_update_sets_fields_sections_and_text_and_appends_history(tmp_path):
    seed(
        tmp_path,
        entries=[
            ROOT,
            {
                "line": 2,
                "text": "",
                "case": "2",
                "kind": "update",
                "category": "rules",
                "slug": "rule-root",
                "origin": f"raw/{DATE}/ledger.md#case-2",
                "decision": "decision-case-2",
                "set": {"tags": ["harness"], "governs": "x.md"},
                "sections": {"How it works": "It works like this."},
                "replace": [{"old": "Prevents root", "new": "Prevents the root"}],
                "change": "the root gets a body",
            },
        ],
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = page(tmp_path, "rules", "rule-root")
    assert props(text)["tags"] == ["harness"] and props(text)["governs"] == "x.md"
    assert (
        "## Purpose\n\nPrevents the root\n" in text
        and "## How it works\n\nIt works like this." in text
    )
    assert f"- {DATE} updated: the root gets a body · [[decision-case-2]]" in text


def test_an_update_with_no_content_prints_nothing_applied_and_is_marked_applied(tmp_path):
    empty = {
        "line": 2,
        "text": "",
        "case": "2",
        "kind": "update",
        "category": "rules",
        "slug": "rule-root",
        "origin": f"raw/{DATE}/ledger.md#case-2",
        "decision": "decision-case-2",
    }
    seed(tmp_path, entries=[ROOT, empty])
    code, out, err = run(tmp_path)
    text = page(tmp_path, "rules", "rule-root")
    assert code == 0 and err == ""  # case 366: stdout, no error, the exit code alone
    assert (
        "generate: rule-root: an update with no content in the Spec; nothing applied"
        in out.splitlines()
    )
    assert "updated:" not in text  # the page as the create left it
    assert load_yaml(tmp_path)["entries"][1]["applied"]


def test_a_replace_absent_or_not_unique_fails_that_entry_alone(tmp_path):
    bad = {
        "line": 2,
        "text": "",
        "case": "2",
        "kind": "update",
        "category": "rules",
        "slug": "rule-root",
        "origin": ORIGIN,
        "decision": "decision-case-2",
        "replace": [{"old": "no such words", "new": "x"}],
        "change": "nothing",
    }
    seed(tmp_path, entries=[ROOT, bad, CHILD])
    code, _, err = run(tmp_path)
    assert code == 1 and "rule-root: replace" in err
    assert (tmp_path / "vault" / "wiki" / "rules" / "rule-child.md").exists()
    data = load_yaml(tmp_path)
    assert "applied" not in data["entries"][1] and "failed" in data["entries"][1]
    assert data["entries"][0]["applied"] and data["entries"][2]["applied"]


# --- case 543.3: an old that opens with spaces takes the spaces before its first word ------


def indented(text):
    return generate.Page("rules", "rule-x", Path("rule-x.md"), sections={"## Render": text})


TEMPLATE = "    > the quote\n\n        **Options:**\n\n    🔹 **(a) one**\n"


def test_an_old_and_a_new_that_open_with_spaces_leave_the_indent_of_new():
    page = indented(TEMPLATE)
    old = "    > the quote\n\n        **Options:**"
    new = "    > the quote\n\n    **Options:**"
    assert generate.replace_once(page, old, new) == 1
    assert (
        page.sections["## Render"] == "    > the quote\n\n    **Options:**\n\n    🔹 **(a) one**\n"
    )


def test_an_old_with_no_leading_space_leaves_the_spaces_of_the_page():
    page = indented(TEMPLATE)
    assert generate.replace_once(page, "> the quote", "> a quote") == 1
    assert page.sections["## Render"].startswith("    > a quote\n")


def test_the_hit_count_is_the_same_with_and_without_the_leading_spaces():
    text = "    FIRST here\nFIRST there\n  FIRST again\n"
    for old in ("FIRST", "    FIRST", "\tFIRST"):
        assert len(generate.replace_hits(indented(text), old)) == 3
    assert len(generate.replace_hits(indented("  only once\n"), "   only once")) == 1


# --- case 514: a Case ratified again changes each page once --------------------------------


def root_update(line, **extra):
    entry = {
        "line": line,
        "text": "",
        "case": "2",
        "kind": "update",
        "category": "rules",
        "slug": "rule-root",
        "origin": f"raw/{DATE}/ledger.md#case-2",
        "decision": "decision-case-2",
        "replace": [{"old": "Prevents root", "new": "Prevents the root"}],
        "change": "the root reworded",
    }
    entry.update(extra)
    return entry


def test_a_repeated_update_whose_anchor_the_first_consumed_applies_nothing(tmp_path):
    seed(tmp_path, entries=[ROOT, root_update(2), root_update(5, supersedes="1")])
    code, out, err = run(tmp_path)
    assert code == 0 and err == "", err
    assert (
        "generate: rule-root: line 5 repeats line 2 of case 2; nothing applied" in out.splitlines()
    )
    text = page(tmp_path, "rules", "rule-root")
    assert "## Purpose\n\nPrevents the root\n" in text
    assert text.count("updated: the root reworded") == 1  # one History line
    assert page(tmp_path, "", "log").count("updated: the root reworded") == 1  # one log line
    repeat = load_yaml(tmp_path)["entries"][2]
    assert repeat["applied"] and "failed" not in repeat


def test_a_repeat_that_failed_on_an_earlier_run_closes_on_the_rerun(tmp_path):
    root = page_text("rules", "rule-root")  # as the first entry left it
    first = root_update(2, applied="11:00:00")
    repeat = root_update(5, failed="generate: rule-root: replace: 'Prevents root' is absent")
    seed(tmp_path, entries=[first, repeat], pages=[("rules", "rule-root", root)])
    before = page(tmp_path, "rules", "rule-root")
    code, out, err = run(tmp_path)
    assert code == 0 and err == "", err
    assert "line 5 repeats line 2 of case 2; nothing applied" in out
    assert page(tmp_path, "rules", "rule-root") == before  # no page changed
    repeat = load_yaml(tmp_path)["entries"][1]
    assert repeat["applied"] and "failed" not in repeat  # the stale mark dropped


def test_a_repeated_create_writes_no_collision(tmp_path):
    seed(tmp_path, entries=[ROOT, dict(ROOT, line=4)])
    code, out, err = run(tmp_path)
    assert code == 0 and err == "", err
    assert "generate: rule-root: line 4 repeats line 1 of case 1; nothing applied" in out
    assert page(tmp_path, "rules", "rule-root").count("created ·") == 1


def test_an_estimate_entry_of_a_repeated_slug_is_applied_as_before(tmp_path):
    """An `estimate` entry carries no `case`: two readings of one page both apply."""
    reading = {
        "text": "",
        "kind": "estimate",
        "category": "estimates",
        "slug": "estimate-child-works",
        "status": "passed",
    }
    entries = [
        CHILD,
        CHILD_ESTIMATE,
        ROOT,
        dict(reading, line=4, result="first", origin=f"raw/{DATE}/ledger.md#L4"),
        dict(reading, line=5, result="second", origin=f"raw/{DATE}/ledger.md#L5"),
    ]
    seed(tmp_path, entries=entries)
    code, out, err = run(tmp_path)
    assert code == 0 and err == "", err
    assert "repeats" not in out
    text = page(tmp_path, "estimates", "estimate-child-works")
    assert "## Result\n\nsecond\n" in text and "ledger.md#L4" in text


def test_delete_archives_and_defer_writes_a_placeholder_or_a_history_line(tmp_path):
    entries = [
        ROOT,
        {
            "line": 2,
            "text": "",
            "case": "2",
            "kind": "delete",
            "category": "rules",
            "slug": "rule-root",
            "origin": ORIGIN,
            "decision": "decision-case-2",
        },
        {
            "line": 3,
            "text": "",
            "case": "3",
            "kind": "defer",
            "category": "rules",
            "slug": "rule-later",
            "origin": ORIGIN,
            "decision": "decision-case-3",
            "fields": {"type": "rule", "purpose": "Prevents something, later"},
        },
        {
            "line": 4,
            "text": "",
            "case": "4",
            "kind": "defer",
            "category": "rules",
            "slug": "rule-root",
            "origin": ORIGIN,
            "decision": "decision-case-4",
        },
    ]
    seed(tmp_path, entries=entries)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    root = page(tmp_path, "rules", "rule-root")
    assert props(root)["status"] == "archived" and f"- {DATE} deleted · [[decision-case-2]]" in root
    assert f"- {DATE} deferred · [[decision-case-4]]" in root
    assert props(root)["deferred_by"] == ["decision-case-4"]
    later = page(tmp_path, "rules", "rule-later")
    assert props(later) == {
        "type": "rule",
        "status": "draft",
        "purpose": "Prevents something, later",
        "deferred_by": ["decision-case-3"],
        "origin": ORIGIN,
        "sprint": "migration",
        "created": yaml.safe_load(DATE),
    }
    assert f"- {DATE} deferred, placeholder · [[decision-case-3]]" in later


# --- the purpose of a defer on the Decision page (case 186.1): `estimate-generate-writes`


def defer_entry(case, slug, purpose=None, line=None):
    entry = {
        "line": line or int(case),
        "text": "",
        "case": case,
        "kind": "defer",
        "category": "rules",
        "slug": slug,
        "origin": f"raw/{DATE}/ledger.md#case-{case}",
        "decision": f"decision-case-{case}",
    }
    if purpose is not None:
        entry["fields"] = {"type": "rule", "purpose": purpose}
    return entry


LONG_PURPOSE = "Slice 3d — the model.\n\n1. One promise per Estimate.\n2. No blocks.\n"


def test_a_defer_writes_its_purpose_verbatim_under_deferred_on_the_decision_page(tmp_path):
    entries = [ROOT, defer_entry("3", "rule-root", LONG_PURPOSE)]  # a page that exists
    seed(tmp_path, entries=entries)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    decision = page(tmp_path, "decisions", "decision-case-3")
    assert "\n## Deferred\n\n### [[rule-root]]\n\n" + LONG_PURPOSE.strip() + "\n" in decision
    assert decision.index("## Deferred") < decision.index("## History")
    assert props(page(tmp_path, "rules", "rule-root"))["purpose"] == "Prevents root"  # untouched


def test_two_targets_give_two_headings_in_the_order_of_the_defer_list(tmp_path):
    entries = [
        ROOT,
        defer_entry("3", "rule-zeta", "The last alphabetically, the first deferred", line=3),
        defer_entry("3", "rule-alpha", "The placeholder's own purpose", line=4),
    ]
    seed(tmp_path, entries=entries)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    decision = page(tmp_path, "decisions", "decision-case-3")
    section = decision.split("## Deferred\n", 1)[1].split("## History", 1)[0]
    assert section.strip() == (
        "### [[rule-zeta]]\n\nThe last alphabetically, the first deferred\n\n"
        "### [[rule-alpha]]\n\nThe placeholder's own purpose"
    )
    alpha = page(tmp_path, "rules", "rule-alpha")  # the placeholder still gets its field
    assert props(alpha)["purpose"] == "The placeholder's own purpose"


def test_a_defer_without_a_purpose_writes_no_deferred_section(tmp_path):
    seed(tmp_path, entries=[ROOT, defer_entry("3", "rule-root")])
    run(tmp_path)
    decision = page(tmp_path, "decisions", "decision-case-3")
    assert "## Deferred" not in decision and "## History" in decision


# --- a create over a placeholder (case 101.1) -------------------------------------------

PLACEHOLDER = (
    "---\ntype: rule\npurpose: Prevents something, later\nstatus: draft\n"
    "deferred_by: [decision-case-3]\norigin: raw/2026-09-01/ledger.md#case-3\n"
    "sprint: migration\ncreated: 2026-09-01\n---\n\n## Purpose\n\nPrevents something, later\n\n"
    "## History\n\n- 2026-09-01 deferred, placeholder · [[decision-case-3]]\n"
)


def test_a_create_over_a_placeholder_fills_it_and_keeps_its_birth(tmp_path):
    later = create(
        "rule-later",
        "rules",
        {
            "type": "rule",
            "kind": "Leaf",
            "purpose": "Prevents later",
            "enforcement": "check",
            "implementation_ref": ["guppi/x.py"],
        },
        ref="rule-root",
        tags=["harness"],
        line=2,
    )
    later["case"] = "9"
    later["decision"] = "decision-case-9"
    seed(tmp_path, entries=[ROOT, later], pages=[("rules", "rule-later", PLACEHOLDER)])
    (tmp_path / "guppi").mkdir()
    (tmp_path / "guppi" / "x.py").write_text("")
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    filled = page(tmp_path, "rules", "rule-later")
    fields = props(filled)
    assert fields["kind"] == "Leaf" and fields["purpose"] == "Prevents later"
    assert fields["origin"] == ORIGIN  # the create's, not the defer's
    assert str(fields["created"]) == "2026-09-01" and fields["deferred_by"] == ["decision-case-3"]
    assert fields["parent"] == "rule-root" and fields["status"] == "draft"
    assert "- 2026-09-01 deferred, placeholder · [[decision-case-3]]" in filled
    assert f"- {DATE} created over placeholder · [[decision-case-9]]" in filled
    assert "[[rule-later]]" in page(tmp_path, "rules", "rule-root")


def test_a_create_over_a_real_page_is_still_a_collision(tmp_path):
    seed(tmp_path, entries=[ROOT], pages=[("rules", "rule-root", page_text("rules", "rule-root"))])
    code, _, err = run(tmp_path)
    assert code == 1 and "a collision is an error" in err


def page_text(category, slug, status="draft", **extra):
    lines = [f"type: {category[:-1]}", "kind: MOC", f"status: {status}", f"purpose: {slug}"]
    lines += [f"{k}: {v}" for k, v in extra.items()]
    body = "\n".join(lines)
    return f"---\n{body}\n---\n\n## Purpose\n\n{slug}\n\n## History\n\n- 2026-09-01 created · x\n"


# --- the cascades over the archive (cases 104.1–104.3) -----------------------------------


def insight_text(slug, status, children):
    kids = "[" + ", ".join(children) + "]"
    return (
        f"---\ntype: insight\npattern: p\nstatus: {status}\nseverity: {len(children)}\n"
        f"children: {kids}\norigin: 2026-09-01 A\nsprint: migration\ncreated: 2026-09-01\n"
        f"tags: [harness]\n---\n\n## Pattern\n\np\n\n## History\n\n- 2026-09-01 created · x\n"
    )


def lesson_text(slug, status, insight=None):
    extra = f"insight: {insight}\n" if insight else ""
    return (
        f"---\ntype: lesson\nkind: error\nroot_cause: r\nstatus: {status}\n{extra}"
        f"origin: raw/2026-09-01/ledger.md#L1\nsprint: migration\ncreated: 2026-09-01\ntags: [harness]\n"
        f"---\n\n## Trigger\n\nt\n\n## Root cause\n\nr\n\n## History\n\n- 2026-09-01 created · x\n"
    )


def test_the_lessons_of_an_actioned_insight_are_archived_and_the_open_ones_recounted(tmp_path):
    pages = [
        (
            "insights",
            "insight-done",
            insight_text("insight-done", "actioned", ["lesson-a", "lesson-b"]),
        ),
        ("lessons", "lesson-a", lesson_text("lesson-a", "clustered", "insight-done")),
        ("lessons", "lesson-b", lesson_text("lesson-b", "archived", "insight-done")),
        (
            "insights",
            "insight-thin",
            insight_text("insight-thin", "open", ["lesson-c", "lesson-d"]),
        ),
        ("lessons", "lesson-c", lesson_text("lesson-c", "clustered", "insight-thin")),
        ("lessons", "lesson-d", lesson_text("lesson-d", "archived", "insight-thin")),
        ("insights", "insight-gone", insight_text("insight-gone", "open", ["lesson-e"])),
        ("lessons", "lesson-e", lesson_text("lesson-e", "archived", "insight-gone")),
        ("insights", "insight-kept", insight_text("insight-kept", "actioned", ["lesson-f"])),
        ("lessons", "lesson-f", lesson_text("lesson-f", "archived", "insight-kept")),
    ]
    seed(tmp_path, entries=[ROOT], pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    a = page(tmp_path, "lessons", "lesson-a")
    assert props(a)["status"] == "archived" and f"- {DATE} archived · insight actioned" in a
    done = props(page(tmp_path, "insights", "insight-done"))
    assert done["status"] == "actioned" and done["severity"] == 0
    assert done["children"] == ["lesson-a", "lesson-b"]
    thin = props(page(tmp_path, "insights", "insight-thin"))
    assert thin["status"] == "open" and thin["severity"] == 1
    assert props(page(tmp_path, "lessons", "lesson-c"))["status"] == "clustered"
    gone = page(tmp_path, "insights", "insight-gone")
    assert props(gone)["status"] == "archived" and f"- {DATE} archived · no live child" in gone
    assert props(gone)["children"] == ["lesson-e"]
    assert props(page(tmp_path, "insights", "insight-kept"))["status"] == "actioned"


def test_a_lesson_added_to_a_reopened_insight_stays_live(tmp_path):
    pages = [
        (
            "insights",
            "insight-back",
            insight_text("insight-back", "open", ["lesson-old", "lesson-new"]),
        ),
        ("lessons", "lesson-old", lesson_text("lesson-old", "archived", "insight-back")),
        ("lessons", "lesson-new", lesson_text("lesson-new", "clustered", "insight-back")),
    ]
    seed(tmp_path, entries=[ROOT], pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    assert props(page(tmp_path, "lessons", "lesson-new"))["status"] == "clustered"
    back = props(page(tmp_path, "insights", "insight-back"))
    assert back["status"] == "open" and back["severity"] == 1


# --- the recount reads a child in the archive (case 110) ----------------------------------


NL = chr(10)


def archive_lesson(tmp_path, slug, text, folder="2026-09-01/0900"):
    path = tmp_path / "vault" / "archive" / "migration" / folder / "lessons" / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline=NL)


def test_an_archived_child_in_the_archive_is_not_counted_live(tmp_path):
    pages = [
        (
            "insights",
            "insight-two",
            insight_text("insight-two", "open", ["lesson-live", "lesson-gone"]),
        ),
        ("lessons", "lesson-live", lesson_text("lesson-live", "clustered", "insight-two")),
        ("insights", "insight-one", insight_text("insight-one", "open", ["lesson-only"])),
        ("insights", "insight-lost", insight_text("insight-lost", "open", ["lesson-nowhere"])),
    ]
    seed(tmp_path, entries=[ROOT], pages=pages)
    archive_lesson(tmp_path, "lesson-gone", lesson_text("lesson-gone", "archived", "insight-two"))
    archive_lesson(tmp_path, "lesson-only", lesson_text("lesson-only", "archived", "insight-one"))
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    two = props(page(tmp_path, "insights", "insight-two"))
    assert two["status"] == "open" and two["severity"] == 1
    assert two["children"] == ["lesson-live", "lesson-gone"]
    one = page(tmp_path, "insights", "insight-one")
    assert props(one)["status"] == "archived" and f"- {DATE} archived · no live child" in one
    lost = props(page(tmp_path, "insights", "insight-lost"))
    assert lost["status"] == "open" and lost["severity"] == 1  # no page anywhere: still live


# --- no ## Insight section: the field is the link (cases 166.2, 166.3) --------------------


def test_a_lesson_with_an_insight_field_stays_without_a_section_on_write_and_in_the_cascade(
    tmp_path,
):
    pages = [
        ("insights", "insight-x", insight_text("insight-x", "open", ["lesson-a", "lesson-b"])),
        ("lessons", "lesson-a", lesson_text("lesson-a", "new")),
        ("lessons", "lesson-b", lesson_text("lesson-b", "clustered", "insight-x")),
        ("lessons", "lesson-c", lesson_text("lesson-c", "new")),
    ]
    update = {
        "kind": "update",
        "slug": "lesson-a",
        "category": "lessons",
        "line": 9,
        "case": "5",
        "origin": "raw/2026-09-10/ledger.md#case-5",
        "set": {"status": "clustered", "insight": "insight-x"},
        "change": "clustered",
    }
    seed(tmp_path, entries=[ROOT, update], pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    a = page(tmp_path, "lessons", "lesson-a")
    assert props(a)["insight"] == "insight-x" and "## Insight" not in a
    b = page(tmp_path, "lessons", "lesson-b")
    assert "## Insight" not in b and "insight section derived" not in b
    assert "## Insight" not in page(tmp_path, "lessons", "lesson-c")


def test_a_section_a_page_still_carries_is_left_as_it_is_on_an_update(tmp_path):
    stale = lesson_text("lesson-b", "clustered", "insight-x").replace(
        "## History", "## Insight\n\n- [[insight-old]]\n\n## History"
    )
    update = {
        "kind": "update",
        "slug": "lesson-b",
        "category": "lessons",
        "line": 9,
        "case": "5",
        "origin": "raw/2026-09-10/ledger.md#case-5",
        "set": {"insight": "insight-x"},
        "change": "re-clustered",
    }
    seed(tmp_path, entries=[ROOT, update], pages=[("lessons", "lesson-b", stale)])
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    b = page(tmp_path, "lessons", "lesson-b")
    assert props(b)["insight"] == "insight-x"
    assert "## Insight\n\n- [[insight-old]]\n" in b  # neither touched nor derived again


# --- an update reaches an archived page (case 105.3) --------------------------------------


def test_an_update_edits_an_archived_page_in_the_archive_and_cleanup_restores_it(tmp_path):
    from guppi import cleanup

    seed(
        tmp_path,
        entries=[
            ROOT,
            update_of("rule-old", 2, set={"status": "draft", "purpose": "back"}, change="restored"),
        ],
    )
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-05" / "1200" / "rules"
    archived.mkdir(parents=True)
    (archived / "rule-old.md").write_text(
        page_text("rules", "rule-old", status="archived"), encoding="utf-8"
    )
    code, _, err = run(tmp_path)
    assert code == 0, err
    text = (archived / "rule-old.md").read_text(encoding="utf-8")
    assert props(text)["status"] == "draft" and props(text)["purpose"] == "back"
    assert f"- {DATE} updated: restored · [[decision-case-2]]" in text
    out, err = io.StringIO(), io.StringIO()
    assert cleanup.run([], stdout=out, stderr=err, project_dir=tmp_path, now=NOW) == 0
    assert (tmp_path / "vault" / "wiki" / "rules" / "rule-old.md").exists()
    assert not (archived / "rule-old.md").exists()


def test_a_page_under_an_archived_raw_folder_is_not_found(tmp_path):
    seed(tmp_path, entries=[ROOT, update_of("rule-old", 2, set={"purpose": "x"}, change="c")])
    raw = tmp_path / "vault" / "archive" / "migration" / "2026-09-05" / "1200" / "raw" / "rules"
    raw.mkdir(parents=True)
    (raw / "rule-old.md").write_text(page_text("rules", "rule-old"), encoding="utf-8")
    code, _, err = run(tmp_path)
    assert code == 1 and "rule-old" in err


def test_a_supersedes_clears_deferred_by_on_the_targets(tmp_path):
    entries = [
        ROOT,
        {
            "line": 2,
            "text": "",
            "case": "2",
            "kind": "defer",
            "category": "rules",
            "slug": "rule-root",
            "origin": f"raw/{DATE}/ledger.md#case-2",
            "decision": "decision-case-2",
        },
        {
            "line": 3,
            "text": "",
            "case": "3",
            "kind": "update",
            "category": "rules",
            "slug": "rule-root",
            "origin": f"raw/{DATE}/ledger.md#case-3",
            "decision": "decision-case-3",
            "supersedes": "2",
            "set": {"governs": "x.md"},
            "change": "taken up",
        },
    ]
    decisions = records_for(entries)
    decisions[2]["supersedes"] = ["decision-case-2"]
    seed(tmp_path, entries=entries, decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    root = page(tmp_path, "rules", "rule-root")
    assert "deferred_by" not in props(root)
    assert f"- {DATE} deferred · [[decision-case-2]]" in root
    assert f"- {DATE} defer by decision-case-2 superseded · [[decision-case-3]]" in root
    two = props(page(tmp_path, "decisions", "decision-case-2"))
    assert two["status"] == "archived" and two["defer"] == [
        "rule-root"
    ]  # superseded, then archived by the cascade (104.1)


def test_a_supersedes_of_a_page_with_only_a_defer_list_clears_deferred_by(tmp_path):
    """The earlier page carries the four lists and no `kind`/`target_slug` (case 59.4)."""
    earlier = (
        '---\ntype: decision\ncase: "2"\nstatus: current\ndefer: [rule-root]\n'
        f"origin: raw/{DATE}/ledger.md#case-2\nsprint: migration\ncreated: {DATE}\ntags: []\n---\n\n"
        "## Context\n\nc\n\n## Problem\n\np\n\n## History\n\n- created\n"
    )
    entry = {
        "line": 3,
        "text": "",
        "case": "3",
        "kind": "update",
        "category": "rules",
        "slug": "rule-root",
        "origin": f"raw/{DATE}/ledger.md#case-3",
        "decision": "decision-case-3",
        "supersedes": "2",
        "set": {"governs": "x.md"},
        "change": "taken up",
    }
    root_page = (
        "---\ntype: rule\nkind: MOC\npurpose: Old root\nstatus: draft\nchildren: []\n"
        "estimates: []\ndeferred_by: [decision-case-2]\norigin: x\nsprint: s\ncreated: 2026-09-09\n"
        "tags: [harness]\n---\n\n## Purpose\n\nOld root\n\n## History\n\n- old\n"
    )
    decisions = records_for([entry])
    decisions[0]["supersedes"] = ["decision-case-2"]
    seed(
        tmp_path,
        entries=[entry],
        decisions=decisions,
        pages=[("rules", "rule-root", root_page), ("decisions", "decision-case-2", earlier)],
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    root = page(tmp_path, "rules", "rule-root")
    assert "deferred_by" not in props(root)
    assert f"- {DATE} defer by decision-case-2 superseded · [[decision-case-3]]" in root
    assert props(page(tmp_path, "decisions", "decision-case-2"))["status"] == "archived"


def test_an_estimate_entry_always_fills_status_and_result(tmp_path):
    entries = [
        CHILD,
        CHILD_ESTIMATE,
        ROOT,
        {
            "line": 4,
            "text": "",
            "kind": "estimate",
            "category": "estimates",
            "slug": "estimate-child-works",
            "status": "passed",
            "result": "twelve tests green",
            "origin": f"raw/{DATE}/ledger.md#L4",
        },
        {
            "line": 5,
            "text": "",
            "kind": "estimate",
            "category": "estimates",
            "slug": "estimate-child-works",
            "status": "passed",
            "result": "a second reading",
            "origin": f"raw/{DATE}/ledger.md#L5",
        },
    ]
    seed(tmp_path, entries=entries)
    code, out, err = run(tmp_path)
    assert code == 0 and err == ""
    text = page(tmp_path, "estimates", "estimate-child-works")
    assert props(text)["status"] == "passed" and "## Result\n\na second reading\n" in text
    assert "twelve tests green" not in text and "skipped" not in out
    assert f"- {DATE} status: pending → passed · raw/{DATE}/ledger.md#L4" in text
    assert f"- {DATE} status: passed → passed · raw/{DATE}/ledger.md#L5" in text
    assert props(page(tmp_path, "rules", "rule-child"))["status"] == "built"
    assert f"- {DATE} status: draft → built · cascade" in page(tmp_path, "rules", "rule-child")
    assert (
        props(page(tmp_path, "rules", "rule-root"))["status"] == "draft"
    )  # a MOC with no estimate


def test_a_lesson_writes_the_lesson_and_no_estimate(tmp_path):
    entries = [
        {
            "line": 1,
            "text": "",
            "kind": "lesson",
            "category": "lessons",
            "slug": "lesson-hooks-late-fire",
            "origin": f"raw/{DATE}/ledger.md#L1",
            "tags": ["harness"],
            "fields": {"type": "lesson", "kind": "error", "root_cause": "the matcher was wrong"},
            "sections": {"Trigger": "the hook fired late", "Root cause": "the matcher was wrong"},
        },
        {
            "line": 2,
            "text": "",
            "kind": "lesson",
            "category": "lessons",
            "slug": "lesson-docs-agents-at-import",
            "origin": f"raw/{DATE}/ledger.md#L2",
            "tags": ["harness"],
            "fields": {
                "type": "lesson",
                "kind": "knowledge",
                "root_cause": "an @ in an agent file is literal",
                "source": "docs",
            },
            "sections": {
                "Trigger": "read the docs",
                "Root cause": "an @ in an agent file is literal",
            },
        },
    ]
    seed(tmp_path, entries=entries)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    lesson = page(tmp_path, "lessons", "lesson-hooks-late-fire")
    assert props(lesson)["status"] == "new" and "estimates" not in props(lesson)
    assert "## Trigger\n\nthe hook fired late" in lesson and "## Estimates" not in lesson
    assert f"- {DATE} created · raw/{DATE}/ledger.md#L1" in lesson
    assert list((tmp_path / "vault" / "wiki" / "estimates").glob("estimate-*.md")) == []
    assert [f for f in lint.lint(tmp_path) if ": layout: " not in f] == []


def test_one_decision_page_per_case_and_supersedes_marks_the_earlier(tmp_path):
    decisions = [
        {
            "case": "1",
            "decision": "decision-case-1",
            "origin": ORIGIN,
            "tags": ["harness"],
            "targets": [{"kind": "create", "category": "rules", "slug": "rule-root"}],
            "case_text": {
                "context": "A root.",
                "problem": "No root.",
                "given": "Nothing.",
                "when": "Someone asks.",
                "then": "A root exists.\n**＋** It is a MOC.",
            },
        },
        {
            "case": "2",
            "decision": "decision-case-2",
            "origin": f"raw/{DATE}/ledger.md#case-2",
            "tags": [],
            "targets": [{"kind": "update", "category": "rules", "slug": "rule-root"}],
            "supersedes": ["decision-case-1"],
            "case_text": {},
        },
    ]
    seed(tmp_path, entries=[ROOT], decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    one = page(tmp_path, "decisions", "decision-case-1")
    assert props(one)["case"] == "1" and props(one)["status"] == "archived"  # 104.1
    assert props(one)["superseded_by"] == ["decision-case-2"]
    assert props(one)["create"] == ["rule-root"]
    assert not {"kind", "target_slug", "targets", "update", "delete", "defer"} & set(props(one))
    assert (
        "## Context" not in one  # the Case file keeps it (case 513)
        and "## Problem\n\nNo root." in one
        and "## Given" not in one  # the Case file keeps the frame (case 513)
        and "## When" not in one  # the contract lives on the Estimate (cases 72.4, 201.2)
        and "Someone asks." not in one
        and "## Then" not in one
        and "A root exists." not in one
    )
    assert one.index("## Problem") < one.index("## History")
    assert f"- {DATE} superseded by decision-case-2 · [[decision-case-2]]" in one
    two = props(page(tmp_path, "decisions", "decision-case-2"))
    assert two["supersedes"] == ["decision-case-1"] and two["tags"] == [
        "harness"
    ]  # from the target page
    findings = [f for f in lint.lint(tmp_path) if "decision-case-2" in f]
    assert findings == ["decisions/decision-case-2: schema: missing section ## Problem"]


def test_a_decision_page_lists_its_targets_by_kind_in_ledger_order(tmp_path):
    """One list per kind present, `create`, `update`, `delete`, `defer` in that order, the
    slugs of each in ledger order; a kind with no line is absent (case 59.4)."""
    decisions = [
        {
            "case": "1",
            "decision": "decision-case-1",
            "origin": ORIGIN,
            "tags": [],
            "targets": [
                {"kind": "update", "category": None, "slug": "case-schema"},
                {"kind": "create", "category": "rules", "slug": "rule-root"},
                {"kind": "defer", "category": "rules", "slug": "rule-later"},
                {"kind": "create", "category": "estimates", "slug": "estimate-root-holds"},
                {"kind": "update", "category": None, "slug": "index"},
            ],
            "case_text": {"context": "c", "problem": "p"},
        }
    ]
    seed(tmp_path, entries=[ROOT], decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = page(tmp_path, "decisions", "decision-case-1")
    assert (  # page slugs as quoted wikilinks, a slug with no category prefix bare (148.1)
        'create: ["[[rule-root]]", "[[estimate-root-holds]]"]\nupdate: [case-schema, index]\n'
        'defer: ["[[rule-later]]"]\n' in text
    )
    assert "delete:" not in text and "kind:" not in text and "target_slug:" not in text
    assert text.index("status: current\n") < text.index("create:") < text.index("origin:")


def test_new_tags_register_and_undeclared_ones_are_reported(tmp_path):
    entries = [dict(ROOT, tags=["harness", "git", "lost"])]
    seed(
        tmp_path,
        entries=entries,
        new_tags=[{"tag": "git", "meaning": "the repository", "aliases": "гит"}],
    )
    code, _, err = run(tmp_path)
    assert code == 0
    tags = (tmp_path / "vault" / "wiki" / "tags.md").read_text(encoding="utf-8")
    assert "| git | the repository | гит |" in tags and "lost" not in tags
    assert "tag lost is used but not registered" in err


def test_applied_entries_are_marked_and_a_rerun_writes_nothing(tmp_path):
    seed(tmp_path, entries=[ROOT, CHILD, CHILD_ESTIMATE])
    run(tmp_path)
    before = {p: p.read_text(encoding="utf-8") for p in (tmp_path / "vault").rglob("*.md")}
    data = load_yaml(tmp_path)
    assert all(e["applied"] for e in data["entries"])
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "0 page(s)" in out
    after = {p: p.read_text(encoding="utf-8") for p in (tmp_path / "vault").rglob("*.md")}
    assert before == after


def test_an_entry_that_applies_loses_a_stale_failed_mark(tmp_path):
    seed(tmp_path, entries=[dict(ROOT, failed="generate: rule-root: an earlier run's error")])
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    entry = load_yaml(tmp_path)["entries"][0]
    assert entry["applied"] and "failed" not in entry


def test_a_collision_fails_and_an_existing_create_is_skipped(tmp_path):
    seed(
        tmp_path,
        entries=[ROOT, dict(CHILD, exists=True, status="passed", result="ignored")],
        pages=[
            (
                "rules",
                "rule-root",
                "---\ntype: rule\nkind: MOC\npurpose: Old root\nstatus: draft\nchildren: []\nestimates: []\norigin: x\nsprint: s\ncreated: 2026-09-09\ntags: [harness]\n---\n\n## Purpose\n\nOld root\n\n## History\n\n- old\n",
            )
        ],
    )
    code, _, err = run(tmp_path)
    assert code == 1 and "rule-root: a page with this slug exists" in err
    assert "Old root" in page(tmp_path, "rules", "rule-root")
    assert not (tmp_path / "vault" / "wiki" / "rules" / "rule-child.md").exists()


def test_cli_dispatches_to_generate(tmp_path, monkeypatch, capsys):
    from guppi import cli

    seed(tmp_path, entries=[ROOT])
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["generate", "--date", DATE]) == 0
    assert "page(s) written" in capsys.readouterr().out


EARLIER = "2026-09-09"


def seed_earlier(tmp_path, entries):
    raw = tmp_path / "vault" / "raw" / EARLIER
    raw.mkdir(parents=True)
    (raw / "ledger.md").write_text("- decision[case 1][create][rule-root]\n", encoding="utf-8")
    data = {
        "date": EARLIER,
        "sprint": "migration",
        "entries": list(entries),
        "decisions": [],
        "unparsed": [],
    }
    (raw / "materialize.yaml").write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )


def run_walk(project_dir, argv=()):
    out, err = io.StringIO(), io.StringIO()
    code = generate.run(list(argv), stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue(), err.getvalue()


def test_without_date_every_folder_with_a_yaml_is_applied_in_date_order(tmp_path):
    seed(tmp_path, entries=[CHILD])  # its ref needs the root of the earlier date, applied first
    seed_earlier(tmp_path, [ROOT])
    (tmp_path / "guppi").mkdir()
    (tmp_path / "guppi" / "x.py").write_text("")
    code, out, err = run_walk(tmp_path)
    assert code == 0, err
    assert [line.split(":")[1].strip() for line in out.splitlines()] == [EARLIER, DATE]
    assert "[[rule-child]]" in page(tmp_path, "rules", "rule-root")
    assert str(props(page(tmp_path, "rules", "rule-root"))["created"]) == EARLIER
    # a second walk: nothing unapplied, nothing written
    code, out, _ = run_walk(tmp_path)
    assert code == 0
    assert all(line.endswith("0 page(s) written or changed") for line in out.splitlines())


def seed_session(tmp_path, entries, folder="1610", date=DATE):
    """A session folder with its own yaml (case 103.3)."""
    raw = tmp_path / "vault" / "raw" / date / folder
    raw.mkdir(parents=True)
    (raw / "ledger.md").write_text("- decision[case 9][create][rule-late]\n", encoding="utf-8")
    data = {
        "date": date,
        "session": folder,
        "sprint": "migration",
        "entries": list(entries),
        "decisions": [],
        "unparsed": [],
    }
    (raw / "materialize.yaml").write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    return raw


def test_the_walk_applies_a_session_yaml_after_the_date_level_one(tmp_path):
    seed(tmp_path, entries=[ROOT])
    late = create("rule-late", "rules", {"type": "rule", "kind": "MOC", "purpose": "Prevents late"})
    session = seed_session(tmp_path, [late])
    code, out, err = run_walk(tmp_path)
    assert code == 0, err
    units = [line.split("generate: ")[1].split(":")[0] for line in out.splitlines()]
    assert units == [DATE, f"{DATE}/1610"]
    assert (tmp_path / "vault" / "wiki" / "rules" / "rule-late.md").exists()
    marks = yaml.safe_load((session / "materialize.yaml").read_text(encoding="utf-8"))
    assert marks["entries"][0]["applied"]
    assert str(props(page(tmp_path, "rules", "rule-late"))["created"]) == DATE
    # --date takes both units of the date
    code, out, _ = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and len(out.splitlines()) == 2


def test_with_date_only_that_folder_is_applied(tmp_path):
    seed(tmp_path, entries=[ROOT])
    seed_earlier(
        tmp_path,
        [
            create(
                "rule-early", "rules", {"type": "rule", "kind": "MOC", "purpose": "Prevents early"}
            )
        ],
    )
    code, out, _ = run_walk(tmp_path, ["--date", DATE])
    assert code == 0 and len(out.splitlines()) == 1
    assert not (tmp_path / "vault" / "wiki" / "rules" / "rule-early.md").exists()


def test_a_failure_on_one_date_is_reported_and_the_walk_goes_on(tmp_path):
    seed(tmp_path, entries=[ROOT])
    bad = {**create("rule-gone", "rules", {}), "kind": "update", "set": {"purpose": "x"}}
    seed_earlier(tmp_path, [bad])  # an update of a page that does not exist
    code, out, err = run_walk(tmp_path)
    assert code == 1
    assert "rule-gone" in err
    assert len(out.splitlines()) == 2
    assert (tmp_path / "vault" / "wiki" / "rules" / "rule-root.md").exists()


# --- Cases 47 and 48: one entry fails alone, the log per entry, the run's date, a delete
# outside the vault ----------------------------------------------------------------------


def run_at(project_dir, argv=None):
    out, err = io.StringIO(), io.StringIO()
    argv = ["--date", DATE] if argv is None else list(argv)
    code = generate.run(argv, stdout=out, stderr=err, project_dir=project_dir, now=NOW)
    return code, out.getvalue(), err.getvalue()


def update_of(slug, line, **content):
    return {
        "line": line,
        "text": "",
        "case": str(line),
        "kind": "update",
        "category": "rules",
        "slug": slug,
        "origin": ORIGIN,
        "decision": f"decision-case-{line}",
        **content,
    }


def test_a_replace_mapping_fails_that_entry_alone(tmp_path):
    bad = update_of("rule-root", 2, replace={"old": "Prevents root", "new": "x"}, change="c")
    seed(tmp_path, entries=[ROOT, bad, CHILD])
    code, _, err = run_at(tmp_path)
    assert code == 1 and "rule-root: replace: expected a list of old/new pairs" in err
    data = load_yaml(tmp_path)
    assert "failed" in data["entries"][1] and "applied" not in data["entries"][1]
    assert data["entries"][0]["applied"] and data["entries"][2]["applied"]
    assert "Prevents root" in page(tmp_path, "rules", "rule-root")


def test_an_exception_inside_one_entry_fails_it_alone_and_the_log_keeps_the_earlier(
    tmp_path, monkeypatch
):
    third = update_of("rule-root", 3, set={"purpose": "Prevents boom"}, change="boom")
    fourth = update_of("rule-child", 4, set={"purpose": "Prevents four"}, change="four")
    seed(tmp_path, entries=[ROOT, CHILD, third, fourth])
    original = generate.Vault.update

    def explode(self, entry):
        if entry["change"] == "boom":
            raise RuntimeError("boom")
        return original(self, entry)

    monkeypatch.setattr(generate.Vault, "update", explode)
    code, _, err = run_at(tmp_path)
    assert code == 1 and "rule-root: RuntimeError: boom" in err
    data = load_yaml(tmp_path)
    assert data["entries"][2]["failed"].endswith("RuntimeError: boom")
    assert data["entries"][0]["applied"] and data["entries"][1]["applied"]
    assert data["entries"][3]["applied"]
    log = (tmp_path / "vault" / "wiki" / "log.md").read_text(encoding="utf-8")
    assert "rules/rule-root created" in log and "rules/rule-child created" in log
    assert "updated: four" in log and "updated: boom" not in log


def test_the_log_is_appended_after_each_entry(tmp_path, monkeypatch):
    seen = []
    original = generate.Vault.update

    def peek(self, entry):
        seen.append((tmp_path / "vault" / "wiki" / "log.md").read_text(encoding="utf-8"))
        return original(self, entry)

    monkeypatch.setattr(generate.Vault, "update", peek)
    later = update_of("rule-root", 3, set={"purpose": "Prevents later"}, change="later")
    seed(tmp_path, entries=[ROOT, CHILD, later])
    code, _, err = run_at(tmp_path)
    assert code == 0, err
    # when the update ran, the two creates were already in the log
    assert "rules/rule-root created" in seen[0] and "rules/rule-child created" in seen[0]


def test_history_and_log_carry_the_run_date_and_created_the_yamls(tmp_path):
    seed(tmp_path, entries=[])
    seed_earlier(tmp_path, [ROOT])
    code, _, err = run_at(tmp_path, [])
    assert code == 0, err
    root = page(tmp_path, "rules", "rule-root")
    assert str(props(root)["created"]) == EARLIER
    assert f"- {DATE} created · [[decision-case-1]]" in root
    assert f"- {EARLIER} created" not in root
    log = (tmp_path / "vault" / "wiki" / "log.md").read_text(encoding="utf-8")
    assert f"- {DATE} rules/rule-root created" in log and f"- {EARLIER} " not in log


def test_a_delete_outside_the_vault_applies_and_a_delete_of_a_missing_page_fails(tmp_path):
    outside = {
        "line": 2,
        "text": "",
        "case": "2",
        "kind": "delete",
        "category": "unknown",
        "slug": "old-thing",
        "origin": ORIGIN,
        "decision": "decision-case-2",
        "source": "docs/old.md",
    }
    missing = {**outside, "line": 3, "case": "3", "category": "rules", "slug": "rule-nothing"}
    seed(tmp_path, entries=[ROOT, outside, missing])
    code, out, err = run_at(tmp_path)
    assert code == 1
    assert "generate: old-thing: outside the vault, nothing to archive" in out
    assert "rule-nothing: no page to delete" in err
    data = load_yaml(tmp_path)
    assert data["entries"][1]["applied"] and "failed" not in data["entries"][1]
    assert "failed" in data["entries"][2]


def test_a_delete_of_an_unknown_category_is_outside_the_vault(tmp_path):
    # case 320: with the file route gone, a slug without a category prefix takes this road
    entry = {
        "line": 2,
        "case": "2",
        "kind": "delete",
        "category": "unknown",
        "slug": "index",
        "origin": ORIGIN,
        "decision": "decision-case-2",
    }
    seed(tmp_path, entries=[ROOT, entry])
    code, out, err = run_at(tmp_path)
    assert code == 0 and err == ""
    assert "generate: index: outside the vault, nothing to archive" in out
    assert load_yaml(tmp_path)["entries"][1]["applied"]
    wiki = tmp_path / "vault" / "wiki"
    assert not list(wiki.glob("*/old-thing.md"))
    log = (wiki / "log.md").read_text(encoding="utf-8")
    assert "old-thing" not in log


# --- Case 201: the Estimate page by the model, `checked`, the old shape refused, the
# Decision page without Given and without a Criterion list -------------------------------

WRITTEN_CRITERION = "When:\nthe hook fires.\n\nThen:\nthe page exists.\n**＋** It is listed."
MODEL_ESTIMATE = create(
    "estimate-child",
    "estimates",
    {
        "type": "estimate",
        "kind": "QA",
        "purpose": "The page exists once the hook fires",
        "method": "pytest tests/test_x.py",
    },
    ref="rule-child",
    sections={"Criterion": WRITTEN_CRITERION},
    tags=["harness"],
    line=2,
)


def estimate_page(criterion, slug="estimate-child", target="rule-child", status="pending"):
    """A page of the model: `method` a field, `## Criterion` and `## History` its sections."""
    return (
        f"---\ntype: estimate\nkind: QA\nstatus: {status}\ntarget: {target}\n"
        "method: by hand\norigin: x\nsprint: s\ncreated: 2026-09-09\ntags: [harness]\n---\n\n"
        f"## Criterion\n\n{criterion}\n\n## History\n\n- old\n"
    )


def reading(slug, result, line=4):
    return {
        "line": line,
        "text": "",
        "kind": "estimate",
        "category": "estimates",
        "slug": slug,
        "status": "passed",
        "result": result,
        "origin": f"raw/{DATE}/ledger.md#L{line}",
    }


def test_an_estimate_create_writes_purpose_method_and_criterion_and_no_old_sections(tmp_path):
    seed(tmp_path, entries=[ROOT, CHILD, MODEL_ESTIMATE])
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    estimate = page(tmp_path, "estimates", "estimate-child")
    fields = props(estimate)
    assert fields["status"] == "pending" and fields["target"] == "rule-child"
    assert fields["purpose"] == "The page exists once the hook fires"
    assert fields["method"] == "pytest tests/test_x.py" and "checked" not in fields
    keys = list(yaml.safe_load(estimate.split("---")[1]))
    assert (
        keys.index("target") < keys.index("purpose") < keys.index("method") < keys.index("origin")
    )
    assert f"## Criterion\n\n{WRITTEN_CRITERION}\n" in estimate
    assert "## Context" not in estimate and "## Method" not in estimate
    assert "## Result" not in estimate
    assert props(page(tmp_path, "rules", "rule-child"))["estimates"] == ["estimate-child"]


def recut_entry(set_fields, sections=None, change="the Criterion replaced whole"):
    entry = {
        "line": 5,
        "text": "",
        "case": "5",
        "kind": "update",
        "category": "estimates",
        "slug": "estimate-child",
        "origin": f"raw/{DATE}/ledger.md#case-5",
        "decision": "decision-case-5",
        "set": set_fields,
        "change": change,
    }
    if sections is not None:
        entry["sections"] = sections
    return entry


NEW_CRITERION = "Given:\nnothing.\n\nWhen:\nasked.\n\nThen:\nanswered."


def test_an_estimate_update_whose_set_carries_method_leaves_every_section(tmp_path):
    """Case 506.6: `set.method` writes the field and drops no section; the Criterion is
    replaced whole as before."""
    entry = recut_entry(
        {"status": "pending", "method": "pytest tests/test_x.py"},
        sections={"Criterion": NEW_CRITERION},
    )
    old = (
        estimate_page("old", status="passed")
        .replace("## Criterion", "## Context\n\nWhy.\n\n## Criterion")
        .replace("## History", "## Method\n\nold method\n\n## History")
    )
    seed(tmp_path, entries=[entry], pages=[("estimates", "estimate-child", old)])
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = page(tmp_path, "estimates", "estimate-child")
    fields = props(text)
    assert fields["status"] == "pending" and fields["method"] == "pytest tests/test_x.py"
    assert f"## Criterion\n\n{NEW_CRITERION}\n" in text
    assert "## Context\n\nWhy.\n" in text and "## Method\n\nold method\n" in text  # kept
    assert "## History\n\n- old\n" in text
    assert f"- {DATE} updated: the Criterion replaced whole · [[decision-case-5]]" in text


def test_a_criterion_update_on_an_estimate_without_method_applies(tmp_path):
    """Case 506.5: `sections.Criterion` on a page without a `method` field, and no
    `set.method`, applies; `generate` refuses no recut for want of the field."""
    entry = recut_entry({"status": "pending"}, sections={"Criterion": NEW_CRITERION})
    old = estimate_page("the old criterion", status="passed").replace("method: by hand\n", "")
    seed(tmp_path, entries=[ROOT, entry], pages=[("estimates", "estimate-child", old)])
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = page(tmp_path, "estimates", "estimate-child")
    assert props(text)["status"] == "pending" and "method" not in props(text)
    assert f"## Criterion\n\n{NEW_CRITERION}\n" in text
    assert "applied" in load_yaml(tmp_path)["entries"][1]


def test_a_reading_writes_checked_from_the_result_date_or_the_yamls_date(tmp_path):
    seed(
        tmp_path,
        entries=[
            reading("estimate-child", "2026-09-14, `pytest tests/test_x.py`: 3 green", line=4),
            reading("estimate-plain", "three tests green, no date", line=5),
        ],
        pages=[
            ("estimates", "estimate-child", estimate_page("c")),
            ("estimates", "estimate-plain", estimate_page("c", "estimate-plain")),
        ],
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    child = props(page(tmp_path, "estimates", "estimate-child"))
    assert child["status"] == "passed" and str(child["checked"]) == "2026-09-14"
    plain = props(page(tmp_path, "estimates", "estimate-plain"))
    assert str(plain["checked"]) == DATE
    text = page(tmp_path, "estimates", "estimate-child")
    keys = list(yaml.safe_load(text.split("---")[1]))
    assert keys.index("target") < keys.index("checked") < keys.index("origin")
    assert "## Result\n\n2026-09-14, `pytest tests/test_x.py`: 3 green\n" in text


def test_the_old_shape_criterion_block_and_remove_criterion_fail_alone(tmp_path):
    block_update = {
        "line": 5,
        "text": "",
        "case": "5",
        "kind": "update",
        "category": "estimates",
        "slug": "estimate-child",
        "origin": f"raw/{DATE}/ledger.md#case-5",
        "decision": "decision-case-5",
        "criterion_block": "### case 5\n\nWhen:\nx.\n\nThen:\ny.",
        "set": {"status": "pending"},
        "change": "criterion: case 5 added",
    }
    removal = {
        "line": 6,
        "text": "",
        "case": "6",
        "kind": "remove_criterion",
        "case_removed": "1",
        "origin": f"raw/{DATE}/ledger.md#case-6",
        "decision": "decision-case-6",
    }
    seed(
        tmp_path,
        entries=[block_update, removal, ROOT],
        pages=[
            ("estimates", "estimate-child", estimate_page("### case 1\n\nold", status="passed"))
        ],
    )
    code, _, err = run(tmp_path)
    assert code == 1
    assert "estimate-child: criterion_block: a shape the script no longer knows" in err
    assert "unknown kind 'remove_criterion'" in err
    text = page(tmp_path, "estimates", "estimate-child")
    assert props(text)["status"] == "passed" and "### case 1\n\nold" in text  # untouched
    data = load_yaml(tmp_path)
    assert "failed" in data["entries"][0] and "failed" in data["entries"][1]
    assert data["entries"][2]["applied"]  # the rest apply
    assert props(page(tmp_path, "rules", "rule-root"))["status"] == "draft"


def test_a_decision_page_carries_the_problem_and_no_given_or_criterion_list(tmp_path):
    entries = [ROOT, CHILD, MODEL_ESTIMATE, CHILD_ESTIMATE]
    decisions = records_for(entries)
    decisions[0]["criterion"] = [{"estimate": "estimate-child", "case": "1"}]  # an old record
    seed(tmp_path, entries=entries, decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = page(tmp_path, "decisions", "decision-case-1")
    # a Case with `given` keeps its context and frame in its Case file (case 513)
    assert "---\n\n## Problem\n\np\n\n## History" in text
    assert "## Context" not in text and "## Given" not in text
    assert "## When" not in text and "## Criterion" not in text
    assert "§ case" not in text
    assert not [f for f in lint.lint(tmp_path) if "decision-case-1" in f]


def test_a_decision_page_of_a_case_without_given_keeps_its_context(tmp_path):
    entries = [ROOT]
    decisions = records_for(entries)
    del decisions[0]["case_text"]["given"]  # a defer-only Case writes none
    seed(tmp_path, entries=entries, decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = page(tmp_path, "decisions", "decision-case-1")
    # the short form has no Case file: its page keeps the context (case 513)
    assert "---\n\n## Context\n\nc\n\n## Problem\n\np\n\n## History" in text
    assert "## Given" not in text


def test_a_decision_page_carries_its_recommend(tmp_path):  # case 544.7
    entries = [ROOT]
    decisions = records_for(entries)
    decisions[0]["case_text"]["recommend"] = "- **Which?**\n  - Recommended: (a).\n  - Answer: yes."
    seed(tmp_path, entries=entries, decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = page(tmp_path, "decisions", "decision-case-1")
    assert "## Problem\n\np\n\n## Recommend\n\n- **Which?**\n  - Recommended: (a).\n" in text


def sub_cases(parent_text):
    """Case 9 with two sub-cases 9.1 and 9.2 on the pages of ROOT and CHILD, the records as
    materialize writes them (case 544.6): the parent's record last, with `children`."""
    entries = [
        dict(
            ROOT, case="9.1", decision="decision-case-9.1", origin=f"raw/{DATE}/ledger.md#case-9.1"
        ),
        dict(
            CHILD, case="9.2", decision="decision-case-9.2", origin=f"raw/{DATE}/ledger.md#case-9.2"
        ),
    ]
    decisions = records_for(entries)
    for record in decisions:
        record["parent"] = "decision-case-9"
        record["tags"] = ["harness"]  # the tags of its lines
        del record["case_text"]["problem"]
    decisions[1]["case_text"]["recommend"] = "- **Own?**\n  - Answer: yes."
    decisions.append(
        {
            "case": "9",
            "decision": "decision-case-9",
            "origin": f"raw/{DATE}/ledger.md#case-9",
            "children": ["decision-case-9.1", "decision-case-9.2"],
            "tags": [],
            "case_text": parent_text,
        }
    )
    return entries, decisions


@pytest.mark.parametrize(
    "parent_text",
    [
        {"context": "c", "problem": "p", "recommend": "r", "given": "g"},
        {"context": "c", "problem": "p", "recommend": "r"},
    ],
)
def test_a_parent_case_gets_its_page_first_with_children_and_no_context(tmp_path, parent_text):
    entries, decisions = sub_cases(parent_text)
    seed(tmp_path, entries=entries, decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    parent = page(tmp_path, "decisions", "decision-case-9")
    fields = props(parent)
    assert fields["children"] == ["decision-case-9.1", "decision-case-9.2"]
    assert not any(kind in fields for kind in ("create", "update", "delete", "defer"))
    assert fields["tags"] == ["harness"]  # the tags of its sub-cases
    assert "---\n\n## Problem\n\np\n\n## Recommend\n\nr\n\n## History" in parent
    assert "## Context" not in parent
    log = (tmp_path / "vault" / "wiki" / "log.md").read_text(encoding="utf-8")
    assert log.index("decision-case-9 ") < log.index("decision-case-9.1")


def test_a_sub_case_page_carries_parent_and_no_problem(tmp_path):  # case 544.7
    entries, decisions = sub_cases({"context": "c", "problem": "p", "recommend": "r"})
    seed(tmp_path, entries=entries, decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    first = page(tmp_path, "decisions", "decision-case-9.1")
    assert props(first)["parent"] == "decision-case-9" and props(first)["create"] == ["rule-root"]
    assert "## Problem" not in first and "## Recommend" not in first
    second = page(tmp_path, "decisions", "decision-case-9.2")
    assert "## Problem" not in second and "## Recommend\n\n- **Own?**\n  - Answer: yes." in second


def test_a_defer_marks_an_insight_deferred_by_and_a_supersedes_clears_it(tmp_path):
    entries = [
        ROOT,
        {
            "line": 2,
            "text": "",
            "case": "2",
            "kind": "defer",
            "category": "insights",
            "slug": "insight-thin",
            "origin": f"raw/{DATE}/ledger.md#case-2",
            "decision": "decision-case-2",
        },
    ]
    pages = [
        ("insights", "insight-thin", insight_text("insight-thin", "open", ["lesson-c"])),
        ("lessons", "lesson-c", lesson_text("lesson-c", "clustered", "insight-thin")),
    ]
    seed(tmp_path, entries=entries, pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    thin = page(tmp_path, "insights", "insight-thin")
    assert props(thin)["deferred_by"] == ["decision-case-2"]
    assert f"- {DATE} deferred · [[decision-case-2]]" in thin
    assert "## Addressed by" not in thin
    # the index line is the page's own field now, read by a Grep of the frontmatter (147.1)
    assert 'deferred_by: ["[[decision-case-2]]"]' in thin
    # the supersedes of a later session clears it
    later = [
        {
            "line": 1,
            "text": "",
            "case": "3",
            "kind": "update",
            "category": "insights",
            "slug": "insight-thin",
            "origin": f"raw/{DATE}/ledger.md#case-3",
            "decision": "decision-case-3",
            "supersedes": "2",
            "set": {"addressed_by": "decision-case-3", "status": "actioned"},
            "change": "the proposal taken up",
        },
    ]
    decisions = records_for(later)
    decisions[0]["supersedes"] = ["decision-case-2"]
    raw = tmp_path / "vault" / "raw" / DATE
    raw.joinpath("materialize.yaml").unlink()
    data = {
        "date": DATE,
        "sprint": "migration",
        "entries": later,
        "decisions": decisions,
        "unparsed": [],
    }
    (raw / "materialize.yaml").write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    thin = page(tmp_path, "insights", "insight-thin")
    assert "deferred_by" not in props(thin)
    assert props(thin)["status"] == "actioned" and props(thin)["addressed_by"] == "decision-case-3"
    assert "## Addressed by" not in thin
    assert props(page(tmp_path, "lessons", "lesson-c"))["status"] == "archived"
    assert props(thin)["severity"] == 0


def test_a_defer_marks_an_estimate_deferred_by_after_checked_and_a_supersedes_clears_it(
    tmp_path,
):
    # case 781: an Estimate is a page a defer marks, its `deferred_by` after `checked`
    entries = [
        {
            "line": 1,
            "text": "",
            "case": "2",
            "kind": "defer",
            "category": "estimates",
            "slug": "estimate-held",
            "origin": f"raw/{DATE}/ledger.md#case-2",
            "decision": "decision-case-2",
        },
    ]
    held = estimate_text("estimate-held", "pending", "rule-held").replace(
        "method: pytest tests/test_x.py\n", "method: pytest tests/test_x.py\nchecked: 2026-09-02\n"
    )
    pages = [
        ("rules", "rule-held", page_text("rules", "rule-held", estimates="[estimate-held]")),
        ("estimates", "estimate-held", held),
    ]
    seed(tmp_path, entries=entries, pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = page(tmp_path, "estimates", "estimate-held")
    assert props(text)["deferred_by"] == ["decision-case-2"]
    assert f"- {DATE} deferred · [[decision-case-2]]" in text
    assert text.index("checked:") < text.index("deferred_by:") < text.index("origin:")
    later = [
        {
            "line": 1,
            "text": "",
            "case": "3",
            "kind": "update",
            "category": "estimates",
            "slug": "estimate-held",
            "origin": f"raw/{DATE}/ledger.md#case-3",
            "decision": "decision-case-3",
            "supersedes": "2",
            "set": {"purpose": "taken up"},
            "change": "taken up",
        },
    ]
    decisions = records_for(later)
    decisions[0]["supersedes"] = ["decision-case-2"]
    raw = tmp_path / "vault" / "raw" / DATE
    raw.joinpath("materialize.yaml").unlink()
    data = {
        "date": DATE,
        "sprint": "migration",
        "entries": later,
        "decisions": decisions,
        "unparsed": [],
    }
    (raw / "materialize.yaml").write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    assert "deferred_by" not in props(page(tmp_path, "estimates", "estimate-held"))


# --- Case 783: a defer of an Estimate with no page writes no placeholder -------------------


def estimate_defer(slug="estimate-unborn"):
    return {
        "line": 2,
        "text": "",
        "case": "2",
        "kind": "defer",
        "category": "estimates",
        "slug": slug,
        "origin": f"raw/{DATE}/ledger.md#case-2",
        "decision": "decision-case-2",
        "fields": {"type": "estimate", "purpose": "later"},
    }


ESTIMATE_DEFER_ERROR = (
    "generate: estimate-unborn: an Estimate is deferred only with its page"
    " — defer the page it would check"
)


def test_a_defer_of_an_estimate_with_no_page_writes_no_page_and_fails_alone(tmp_path):
    seed(tmp_path, entries=[ROOT, estimate_defer()])
    code, _, err = run(tmp_path)
    assert code == 1 and ESTIMATE_DEFER_ERROR in err
    entries = load_yaml(tmp_path)["entries"]
    assert entries[0]["applied"] and entries[1]["failed"]
    assert not list(tmp_path.joinpath("vault").rglob("estimate-unborn.md"))
    assert (tmp_path / "vault" / "wiki" / "rules" / "rule-root.md").exists()


@pytest.mark.parametrize(
    "folder",
    ["plugin/2026-09-01/0900/rules", "plugin/2026-09-01/0900/raw/estimates"],
)
def test_a_defer_of_an_estimate_archived_outside_an_estimates_folder_fails(tmp_path, folder):
    # where `page_paths` and `archived_paths` used to part: `has_page` takes neither (783)
    seed(tmp_path, entries=[ROOT, estimate_defer()])
    stray = tmp_path / "vault" / "archive" / folder / "estimate-unborn.md"
    stray.parent.mkdir(parents=True)
    text = estimate_text("estimate-unborn", "pending", "rule-root")
    stray.write_text(text, encoding="utf-8", newline="\n")
    code, _, err = run(tmp_path)
    assert code == 1 and ESTIMATE_DEFER_ERROR in err
    assert load_yaml(tmp_path)["entries"][1]["failed"]
    assert stray.read_text(encoding="utf-8") == text
    assert not (tmp_path / "vault" / "wiki" / "estimates" / "estimate-unborn.md").exists()


def test_a_defer_of_an_estimate_archived_in_an_estimates_folder_marks_it_there(tmp_path):
    seed(tmp_path, entries=[ROOT, estimate_defer()])
    archived = tmp_path / "vault" / "archive" / "plugin" / "2026-09-01" / "0900" / "estimates"
    archived.mkdir(parents=True)
    path = archived / "estimate-unborn.md"
    path.write_text(
        estimate_text("estimate-unborn", "pending", "rule-root"), encoding="utf-8", newline="\n"
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = path.read_text(encoding="utf-8")
    assert props(text)["deferred_by"] == ["decision-case-2"]
    assert f"- {DATE} deferred · [[decision-case-2]]" in text


def test_a_synthesis_create_of_an_insight_marked_librarian_applies(tmp_path):
    entry = {
        "kind": "create",
        "category": "insights",
        "slug": "insight-new",
        "origin": f"raw/{DATE}/ledger.md#L7",
        "fields": {"type": "insight", "pattern": "p", "children": ["lesson-a", "lesson-b"]},
        "tags": ["harness"],
        "sections": {"Pattern": "Two lessons on one path.", "Proposal": "A suggestion."},
        "librarian": "synthesis",
    }
    pages = [
        ("lessons", "lesson-a", lesson_text("lesson-a", "clustered", "insight-new")),
        ("lessons", "lesson-b", lesson_text("lesson-b", "clustered", "insight-new")),
    ]
    seed(tmp_path, entries=[ROOT, entry], pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    new = page(tmp_path, "insights", "insight-new")
    fields = props(new)
    assert fields["status"] == "open" and fields["severity"] == 2
    assert fields["children"] == ["lesson-a", "lesson-b"] and fields["tags"] == ["harness"]
    assert fields["origin"] == f"raw/{DATE}/ledger.md#L7"
    assert "## Pattern\n\nTwo lessons on one path.\n" in new
    assert "## Proposal\n\nA suggestion.\n" in new
    assert "## Children" not in new
    assert f"## History\n\n- {DATE} created · raw/{DATE}/ledger.md#L7\n" in new


def test_a_create_or_delete_of_an_insight_through_the_yaml_is_an_error(tmp_path):
    entries = [
        ROOT,
        create(
            "insight-new", "insights", {"type": "insight", "pattern": "p"}, tags=["harness"], line=2
        ),
    ]
    entries[1]["case"] = "2"
    entries.append(
        {
            "line": 3,
            "text": "",
            "case": "3",
            "kind": "delete",
            "category": "insights",
            "slug": "insight-thin",
            "origin": f"raw/{DATE}/ledger.md#case-3",
            "decision": "decision-case-3",
        }
    )
    pages = [("insights", "insight-thin", insight_text("insight-thin", "open", ["lesson-c"]))]
    seed(tmp_path, entries=entries, pages=pages)
    code, _, err = run(tmp_path)
    assert code == 1 and "insight-new" in err and "insight-thin" in err
    assert props(page(tmp_path, "insights", "insight-thin"))["status"] == "open"


# --- an entry materialize failed, an entry superseded (cases 142.2, 151) -------------------


def test_an_entry_materialize_failed_is_skipped_with_its_mark_kept(tmp_path):
    not_lifted = {
        "line": 2,
        "text": "decision[case 9][update][rule-root]",
        "failed": "ValueError: odd item",
    }
    seed(tmp_path, entries=[ROOT, not_lifted])
    code, _, err = run(tmp_path)
    assert code == 1
    assert "generate: line 2: not lifted by materialize; ValueError: odd item" in err
    assert (tmp_path / "vault" / "wiki" / "rules" / "rule-root.md").exists()  # the rest apply
    entries = load_yaml(tmp_path)["entries"]
    assert entries[1] == not_lifted  # the mark as materialize wrote it, no `applied`
    assert entries[0].get("applied")


def test_an_entry_with_superseded_by_is_not_applied_and_its_decision_page_is_written(tmp_path):
    superseded = {
        "line": 2,
        "text": "",
        "case": "2",
        "kind": "update",
        "category": "rules",
        "slug": "rule-root",
        "origin": f"raw/{DATE}/ledger.md#case-2",
        "decision": "decision-case-2",
        "replace": [{"old": "absent words", "new": "x"}],
        "change": "the old words",
        "failed": "generate: rule-root: replace: 'absent words' is absent or not unique",
        "superseded_by": "3",
    }
    later = {
        "line": 3,
        "text": "",
        "case": "3",
        "kind": "update",
        "category": "rules",
        "slug": "rule-root",
        "origin": f"raw/{DATE}/ledger.md#case-3",
        "decision": "decision-case-3",
        "set": {"purpose": "Prevents root, the new words"},
        "change": "the new words",
        "supersedes": "2",
    }
    decisions = records_for([ROOT, superseded, later])
    decisions[1]["superseded_by"] = ["decision-case-3"]
    decisions[2]["supersedes"] = ["decision-case-2"]
    seed(tmp_path, entries=[ROOT, superseded, later], decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    entries = load_yaml(tmp_path)["entries"]
    assert "applied" not in entries[1] and entries[1]["failed"].startswith("generate:")
    assert entries[2].get("applied")
    root = props(page(tmp_path, "rules", "rule-root"))
    assert root["purpose"] == "Prevents root, the new words"
    assert "the old words" not in page(tmp_path, "rules", "rule-root")
    early = props(page(tmp_path, "decisions", "decision-case-2"))
    assert early["status"] in ("superseded", "archived")
    assert props(page(tmp_path, "decisions", "decision-case-3"))["supersedes"] == [
        "decision-case-2"
    ]


def test_the_decision_page_of_a_case_gone_from_the_spec_has_a_two_line_body(tmp_path):
    # case 299.4: the record of Case 2 carries superseded_by and no case_text — Case 2 was
    # superseded in its own session and left the Spec
    superseded = {
        "line": 2,
        "text": "",
        "case": "2",
        "kind": "update",
        "category": "rules",
        "slug": "rule-root",
        "origin": f"raw/{DATE}/ledger.md#case-2",
        "decision": "decision-case-2",
        "superseded_by": "3",
    }
    later = {
        "line": 3,
        "text": "",
        "case": "3",
        "kind": "update",
        "category": "rules",
        "slug": "rule-root",
        "origin": f"raw/{DATE}/ledger.md#case-3",
        "decision": "decision-case-3",
        "set": {"purpose": "Prevents root, the new words"},
        "change": "the new words",
        "supersedes": "2",
    }
    decisions = records_for([ROOT, superseded, later])
    del decisions[1]["case_text"]
    decisions[1]["superseded_by"] = ["decision-case-3"]
    decisions[2]["supersedes"] = ["decision-case-2"]
    seed(tmp_path, entries=[ROOT, superseded, later], decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = page(tmp_path, "decisions", "decision-case-2")
    early = props(text)
    assert early["status"] == "archived" and early["superseded_by"] == ["decision-case-3"]
    assert (
        "## Context\n\nSuperseded by [[decision-case-3]] in its own session, before the Spec "
        "was approved; the Case left the Spec (case 299).\n\n## Problem\n\nDecided under "
        "[[decision-case-3]].\n"
    ) in text
    assert early["update"] == ["rule-root"]
    with_text = props(page(tmp_path, "decisions", "decision-case-3"))
    assert with_text["status"] == "current"
    three = page(tmp_path, "decisions", "decision-case-3")
    assert "## Context" not in three and "## Problem\n\np\n" in three  # case 513


# --- the tick of the Spec beside the yaml (case 226.1) -----------------------------------


SPEC = """# Spec

## Case 1 — the root

```tasks
- [ ] create `rule-root` (no `ref`)
- [ ] `guppi/x.py`: the code, tests first
```

### Case 1.1 — the child

```tasks
- [ ] create `rule-child` (`ref: rule-root`)
```

## Case 2 — the root again

```tasks
- [ ] update `rule-root`: `set`, `change`
- [ ] update `rule-root`: a second time
- [ ] read `estimate-root-works`
```

## Deferred

## Case 3 — later

```then
defer:
  - slug: rule-later
```
"""


def with_spec(tmp_path, text=SPEC):
    spec = tmp_path / "vault" / "raw" / DATE / "spec.md"
    spec.write_text(text, encoding="utf-8", newline="\n")
    return spec


def spec_update(case, slug="rule-root", line=2, **extra):
    entry = {
        "line": line,
        "text": "",
        "case": case,
        "kind": "update",
        "category": "rules",
        "slug": slug,
        "origin": f"raw/{DATE}/ledger.md#case-{case}",
        "decision": f"decision-case-{case}",
        "change": f"change of {case}",
    }
    entry.update(extra)
    return entry


def test_an_applied_entry_ticks_its_line_under_its_own_case(tmp_path):
    child = dict(CHILD, case="1.1")
    seed(tmp_path, entries=[ROOT, child, spec_update("2")])
    spec = with_spec(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] create `rule-root` (no `ref`)" in text
    assert "- [x] create `rule-child` (`ref: rule-root`)" in text
    assert "- [x] update `rule-root`: `set`, `change`" in text
    assert "- [ ] update `rule-root`: a second time" in text  # one entry, one line
    assert "- [ ] `guppi/x.py`: the code, tests first" in text  # the agent's line
    assert "- [ ] read `estimate-root-works`" in text


def test_a_repeat_ticks_no_second_line_of_its_kind_and_slug(tmp_path):
    # case 522: the second entry of one kind and slug in one Case is a repeat; it does no
    # work, so the second line stays open for Retro to count
    seed(tmp_path, entries=[ROOT, spec_update("2"), spec_update("2", line=3)])
    spec = with_spec(tmp_path)
    code, out, err = run(tmp_path)
    assert code == 0 and err == ""
    assert "generate: rule-root: line 3 repeats line 2 of case 2; nothing applied" in out
    text = spec.read_text(encoding="utf-8")
    assert "- [x] update `rule-root`: `set`, `change`" in text
    assert "- [ ] update `rule-root`: a second time" in text


def test_a_missing_spec_section_or_line_is_no_error(tmp_path):
    entries = [ROOT, spec_update("2"), spec_update("9", line=3)]
    without = seed(tmp_path / "a", entries=entries)
    code, out, err = run(without)  # no spec at all
    assert code == 0 and err == "" and "spec" not in out.lower()
    assert all(e.get("applied") for e in load_yaml(without)["entries"])
    partial = seed(tmp_path / "b", entries=entries)
    text = "## Case 2 — only\n\n- [ ] update `rule-other`\n"
    spec = with_spec(partial, text)  # no line for case 2's slug, no section for case 9
    code, _, err = run(partial)
    assert code == 0 and err == ""
    assert spec.read_text(encoding="utf-8") == text
    assert all(e.get("applied") for e in load_yaml(partial)["entries"])


def test_a_failed_entry_a_file_entry_and_a_lesson_entry_tick_nothing(tmp_path):
    bad = spec_update("2", replace=[{"old": "no such words", "new": "x"}])
    file_entry = {
        "line": 3,
        "text": "",
        "case": "2",
        "kind": "update",
        "category": "file",
        "slug": "glossary",
        "path": "vault/wiki/glossary.md",
        "origin": ORIGIN,
        "decision": "decision-case-2",
        "change": "by hand",
    }
    lesson = {
        "line": 4,
        "text": "",
        "kind": "lesson",
        "category": "lessons",
        "slug": "lesson-hooks-late-fire",
        "origin": f"raw/{DATE}/ledger.md#L4",
        "tags": ["harness"],
        "fields": {"type": "lesson", "kind": "error", "root_cause": "the matcher was wrong"},
        "sections": {"Trigger": "the hook fired late", "Root cause": "the matcher was wrong"},
    }
    seed(tmp_path, entries=[ROOT, bad, file_entry, lesson])
    text = (
        "## Case 2 — x\n\n- [ ] update `rule-root`\n- [ ] update `glossary`, by hand\n"
        "- [ ] read `lesson-hooks-late-fire`\n"
    )
    spec = with_spec(tmp_path, text)
    code, _, _ = run(tmp_path)
    assert code == 1
    assert spec.read_text(encoding="utf-8") == text


# --- the tick of a reading (case 270.1) --------------------------------------------------


def child_reading(line=4):
    return reading("estimate-child-works", "twelve tests green", line=line)


READ_SPEC = """# Spec

## Case 1 — the root

```tasks
- [ ] create `rule-root` (no `ref`)
- [ ] read `estimate-child-works`: pytest, then live
- [ ] `guppi/x.py`: the code
```

## Case 2 — the root again

```tasks
- [ ] read `estimate-child-works`: a second reading, another Criterion
```
"""


def test_a_reading_ticks_every_read_line_of_its_slug_in_the_spec(tmp_path):
    # case 312: one reading is of the page, whose Criterion is one, however many Cases of
    # the session touched it
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, child_reading()])
    spec = with_spec(tmp_path, READ_SPEC)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] read `estimate-child-works`: pytest, then live" in text
    assert "- [x] read `estimate-child-works`: a second reading" in text
    assert "- [ ] `guppi/x.py`: the code" in text


def test_two_readings_tick_two_read_lines_in_order(tmp_path):
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, child_reading(), child_reading(line=5)])
    spec = with_spec(tmp_path, READ_SPEC)
    assert run(tmp_path)[0] == 0
    assert "- [ ] read `estimate-child-works`" not in spec.read_text(encoding="utf-8")


def test_a_create_with_a_folded_reading_ticks_the_page_line_and_the_read_line(tmp_path):
    folded = dict(CHILD_ESTIMATE, status="passed", result="green", folded=[4])
    seed(tmp_path, entries=[CHILD, folded, ROOT])
    spec = with_spec(
        tmp_path,
        "## Case 1 — x\n\n- [ ] create `estimate-child-works`\n"
        "- [ ] read `estimate-child-works`: pytest\n",
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] create `estimate-child-works`" in text
    assert "- [x] read `estimate-child-works`: pytest" in text


def test_a_reading_ticks_the_read_line_in_every_live_spec(tmp_path):
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, child_reading()])
    with_spec(tmp_path, "## Case 1 — x\n\n- [ ] create `rule-root`\n")  # no read line here
    raw = tmp_path / "vault" / "raw"
    older = raw / "2026-09-09" / "0900" / "spec.md"
    newer = raw / DATE / "0800" / "spec.md"
    for path in (older, newer):
        path.parent.mkdir(parents=True)
        path.write_text(
            "## Case 7 — y\n\n- [ ] read `estimate-child-works`: by hand\n",
            encoding="utf-8",
            newline="\n",
        )
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-08" / "0700" / "raw"
    archived.mkdir(parents=True)
    (archived / "spec.md").write_text(
        "## Case 5 — z\n\n- [ ] read `estimate-child-works`: archived\n", encoding="utf-8"
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    # case 326: a promise changed in two sessions leaves a read line in each, and one
    # reading is of the page — so every live Spec closes, not the first that holds a line
    assert "- [x] read `estimate-child-works`: by hand" in older.read_text(encoding="utf-8")
    assert "- [x] read `estimate-child-works`: by hand" in newer.read_text(encoding="utf-8")
    # the archive keeps its open line: the record of a task nobody performed
    assert "- [ ] read" in (archived / "spec.md").read_text(encoding="utf-8")


def test_a_reading_with_no_read_line_anywhere_is_applied_without_a_word(tmp_path):
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, child_reading()])
    with_spec(tmp_path, "## Case 1 — x\n\n- [ ] create `rule-root`\n")
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "read" not in out.lower()
    assert all(e.get("applied") for e in load_yaml(tmp_path)["entries"])


def test_a_sprint_page_keeps_milestones_backlog_and_closed_in_order(tmp_path):
    sprint = create(
        "entity-sprint-x",
        "entities",
        {"type": "entity", "kind": "MOC", "purpose": "The sprint"},
        sections={"Purpose": "The sprint.", "Closed": "Nothing yet."},
        tags=["harness"],
    )
    later = spec_update(
        "2",
        slug="entity-sprint-x",
        sections={"Milestones": "### Slice 1\n\n- [[rule-root]] — x", "Backlog": "- a plain line"},
    )
    later["category"] = "entities"
    seed(tmp_path, entries=[ROOT, sprint, later])
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = page(tmp_path, "entities", "entity-sprint-x")
    order = [
        text.index(h)
        for h in ("## Purpose", "## Milestones", "## Backlog", "## Closed", "## History")
    ]
    assert order == sorted(order)


# --- an update with `rename` (case 258.1): `estimate-generate-renames` ---------------------

OLD_RULE = """\
---
type: rule
kind: Leaf
purpose: Prevents the old thing
status: draft
enforcement: check
parent: "[[rule-parent]]"
estimates: ["[[estimate-old-holds]]"]
origin: raw/2026-09-01/ledger.md#case-9
sprint: migration
created: 2026-09-01
tags: [harness]
---

## Purpose

Prevents the old thing; `rule-old` is its own name here.

## History

- 2026-09-01 created · [[decision-case-9]]
"""

PARENT_RULE = """\
---
type: rule
kind: MOC
purpose: Holds the old thing
status: draft
children: ["[[rule-old]]"]
origin: raw/2026-09-01/ledger.md#case-9
sprint: migration
created: 2026-09-01
tags: [harness]
---

## Purpose

Holds [[rule-old]] and names `rule-old` in prose; `rule-older` is another slug.

## History

- 2026-09-01 child rule-old added · [[decision-case-9]]
"""

OLD_ESTIMATE = """\
---
type: estimate
kind: QA
status: passed
target: "[[rule-old]]"
purpose: The old thing holds
method: pytest
checked: 2026-09-01
origin: raw/2026-09-01/ledger.md#case-9
sprint: migration
created: 2026-09-01
tags: [harness]
---

## Criterion

When:
`rule-old` is read.

Then:
It holds.

## Result

2026-09-01, pytest: rule-old holds

## History

- 2026-09-01 created · [[decision-case-9]]
"""

OLD_DECISION = """\
---
type: decision
case: "9"
status: current
update: ["[[rule-old]]"]
origin: raw/2026-09-01/ledger.md#case-9
sprint: migration
created: 2026-09-01
tags: [harness]
---

## Context

The Case that touched [[rule-old]].

## Problem

p

## History

- 2026-09-01 created · raw/2026-09-01/ledger.md#case-9
"""

RENAME_PAGES = [
    ("rules", "rule-old", OLD_RULE),
    ("rules", "rule-parent", PARENT_RULE),
    ("estimates", "estimate-old-holds", OLD_ESTIMATE),
    ("decisions", "decision-case-9", OLD_DECISION),
]


def rename_entry(new="rule-new", **extra):
    entry = {
        "line": 2,
        "text": "",
        "case": "2",
        "kind": "update",
        "category": "rules",
        "slug": "rule-old",
        "origin": f"raw/{DATE}/ledger.md#case-2",
        "decision": "decision-case-2",
        "rename": new,
        "set": {"purpose": "Prevents the new thing"},
        "change": "rule-old becomes rule-new",
    }
    entry.update(extra)
    return entry


def test_a_rename_moves_the_page_applies_the_rest_and_writes_its_history(tmp_path):
    seed(tmp_path, entries=[rename_entry()], pages=RENAME_PAGES)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    wiki = tmp_path / "vault" / "wiki"
    assert not (wiki / "rules" / "rule-old.md").exists()
    text = page(tmp_path, "rules", "rule-new")
    assert props(text)["purpose"] == "Prevents the new thing"  # `set` lands on the new file
    assert props(text)["origin"] == "raw/2026-09-01/ledger.md#case-9"  # never rewritten
    assert "`rule-new` is its own name here" in text
    assert f"- {DATE} renamed from `rule-old` · [[decision-case-2]]" in text
    assert f"- {DATE} updated: rule-old becomes rule-new · [[decision-case-2]]" in text
    assert load_yaml(tmp_path)["entries"][0]["applied"]


def test_a_rename_rewrites_links_ref_fields_and_the_word_in_live_pages(tmp_path):
    seed(tmp_path, entries=[rename_entry()], pages=RENAME_PAGES)
    assert run(tmp_path)[0] == 0
    parent = page(tmp_path, "rules", "rule-parent")
    assert props(parent)["children"] == ["rule-new"]
    assert (
        "Holds [[rule-new]] and names `rule-new` in prose; `rule-older` is another slug." in parent
    )
    assert f"- {DATE} ref `rule-old` → `rule-new` · [[decision-case-2]]" in parent
    assert "- 2026-09-01 child rule-old added" in parent  # History is not rewritten
    estimate = page(tmp_path, "estimates", "estimate-old-holds")
    assert props(estimate)["target"] == "rule-new"
    assert "`rule-new` is read." in estimate
    assert "2026-09-01, pytest: rule-old holds" in estimate  # Result is not rewritten
    assert f"- {DATE} ref `rule-old` → `rule-new`" in estimate


def test_a_rename_retargets_the_decision_pages_without_a_history_line(tmp_path):
    seed(tmp_path, entries=[rename_entry()], pages=RENAME_PAGES)
    assert run(tmp_path)[0] == 0
    earlier = page(tmp_path, "decisions", "decision-case-9")
    assert props(earlier)["update"] == ["rule-new"]
    assert "The Case that touched [[rule-new]]." in earlier
    assert "ref `rule-old`" not in earlier
    own = page(tmp_path, "decisions", "decision-case-2")  # written before the entry (52.4)
    assert props(own)["update"] == ["rule-new"]


def test_a_rename_to_a_taken_or_foreign_slug_fails_the_entry_alone(tmp_path):
    seed(tmp_path, entries=[rename_entry(new="rule-parent"), CHILD], pages=RENAME_PAGES)
    code, _, err = run(tmp_path)
    assert code == 1 and "rule-old: rename: rule-parent is taken" in err
    wiki = tmp_path / "vault" / "wiki"
    assert (wiki / "rules" / "rule-old.md").exists() and (wiki / "rules" / "rule-child.md").exists()
    assert props(page(tmp_path, "rules", "rule-parent"))["children"] == ["rule-old"]
    data = load_yaml(tmp_path)
    assert "failed" in data["entries"][0] and data["entries"][1]["applied"]

    seed(tmp_path / "b", entries=[rename_entry(new="entity-new")], pages=RENAME_PAGES)
    code, _, err = run(tmp_path / "b")
    assert code == 1 and "rule-old: rename: entity-new is not a rules slug" in err
    assert (tmp_path / "b" / "vault" / "wiki" / "rules" / "rule-old.md").exists()

    seed(tmp_path / "c", entries=[rename_entry(new="rule-gone")], pages=RENAME_PAGES)
    archived = tmp_path / "c" / "vault" / "archive" / "migration" / "2026-09-01" / "rules"
    archived.mkdir(parents=True)
    (archived / "rule-gone.md").write_text(
        page_text("rules", "rule-gone", "archived"), encoding="utf-8"
    )
    code, _, err = run(tmp_path / "c")
    assert code == 1 and "rule-old: rename: rule-gone is taken" in err


# --- reword: the rename of a word without a page (case 274.1) ----------------------------


OWNER_RULE = """\
---
type: rule
kind: Leaf
purpose: Prevents the gadget from drifting
status: draft
enforcement: render
governs: .claude/skills/widget/SKILL.md
origin: raw/2026-09-01/ledger.md#case-9
sprint: migration
created: 2026-09-01
tags: [harness]
---

## Purpose

Prevents the gadget from drifting; the skill is `/widget` since case 9.

## Render

<!-- rule-owner -->
Run `/widget` once; the gadget is what it was called.
<!-- /rule-owner -->

## History

- 2026-09-01 created · [[decision-case-9]]
"""

OTHER_RULE = """\
---
type: rule
kind: Leaf
purpose: Asks the vault at gadget time
status: draft
enforcement: check
origin: raw/2026-09-01/ledger.md#case-9
sprint: migration
created: 2026-09-01
tags: [harness]
---

## Purpose

The agent at gadget and at retro asks once; a `/gadget` call is the same moment; `rule-gadget-hook` is another slug.

## History

- 2026-09-01 gadget added · [[decision-case-9]]
"""

WORD_ESTIMATE = """\
---
type: estimate
kind: QA
status: passed
target: "[[rule-other]]"
purpose: The gadget check runs
method: pytest, then one gadget by hand
checked: 2026-09-01
origin: raw/2026-09-01/ledger.md#case-9
sprint: migration
created: 2026-09-01
tags: [harness]
---

## Criterion

When:
The person invokes gadget.

Then:
It holds.

## Result

2026-09-01, pytest: gadget holds

## History

- 2026-09-01 created · [[decision-case-9]]
"""

REWORD_PAGES = [
    ("rules", "rule-owner", OWNER_RULE),
    ("rules", "rule-other", OTHER_RULE),
    ("estimates", "estimate-other-runs", WORD_ESTIMATE),
    ("decisions", "decision-case-9", OLD_DECISION.replace("touched", "touched gadget and")),
    (
        "lessons",
        "lesson-gadget-late",
        lesson_text("lesson-gadget-late", "new").replace("\n\nt\n", "\n\nthe gadget fired late\n"),
    ),
    (
        "insights",
        "insight-gadget-flag",
        insight_text("insight-gadget-flag", "open", []).replace("\n\np\n", "\n\nthe gadget flag\n"),
    ),
]


def reword_entry(pairs=None, **extra):
    entry = {
        "line": 2,
        "text": "",
        "case": "2",
        "kind": "update",
        "category": "rules",
        "slug": "rule-owner",
        "origin": f"raw/{DATE}/ledger.md#case-2",
        "decision": "decision-case-2",
        "reword": pairs if pairs is not None else [{"old": "gadget", "new": "widget"}],
        "change": "gadget is called widget",
    }
    entry.update(extra)
    return entry


def test_a_reword_replaces_the_word_on_the_live_rules_entities_and_estimates(tmp_path):
    seed(tmp_path, entries=[reword_entry()], pages=REWORD_PAGES)
    code, out, err = run(tmp_path)
    assert code == 0 and err == ""
    owner = page(tmp_path, "rules", "rule-owner")
    assert props(owner)["purpose"] == "Prevents the widget from drifting"
    assert "Prevents the widget from drifting; the skill is `/widget` since case 9." in owner
    assert "the widget is what it was called." in owner
    assert f"- {DATE} reworded: `gadget` → `widget` · [[decision-case-2]]" in owner
    assert f"- {DATE} updated: gadget is called widget · [[decision-case-2]]" in owner
    other = page(tmp_path, "rules", "rule-other")
    assert props(other)["purpose"] == "Asks the vault at widget time"
    assert (
        "The agent at widget and at retro asks once; a `/widget` call is the same moment; "
        "`rule-gadget-hook` is another slug." in other
    )
    assert "- 2026-09-01 gadget added" in other  # History is a record
    assert f"- {DATE} reworded: `gadget` → `widget` · [[decision-case-2]]" in other
    estimate = page(tmp_path, "estimates", "estimate-other-runs")
    assert props(estimate)["purpose"] == "The widget check runs"
    assert props(estimate)["method"] == "pytest, then one widget by hand"
    assert props(estimate)["status"] == "passed"  # the status of no Estimate changes
    assert "The person invokes widget." in estimate
    assert "2026-09-01, pytest: gadget holds" in estimate  # Result is a record
    assert "generate: reword `gadget` → `widget`: rules/rule-other (3)" in out
    assert "generate: reword `gadget` → `widget`: estimates/estimate-other-runs (3)" in out


def test_a_reword_leaves_decisions_lessons_insights_and_the_archive_alone(tmp_path):
    seed(tmp_path, entries=[reword_entry()], pages=REWORD_PAGES)
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-01" / "rules"
    archived.mkdir(parents=True)
    (archived / "rule-gone.md").write_text(OTHER_RULE, encoding="utf-8")
    assert run(tmp_path)[0] == 0
    assert "touched gadget and" in page(tmp_path, "decisions", "decision-case-9")
    assert "the gadget fired late" in page(tmp_path, "lessons", "lesson-gadget-late")
    assert "the gadget flag" in page(tmp_path, "insights", "insight-gadget-flag")
    assert "at gadget and" in (archived / "rule-gone.md").read_text(encoding="utf-8")


def test_a_reword_alone_is_content_and_applies(tmp_path):
    entry = reword_entry()
    entry.pop("change")
    seed(tmp_path, entries=[entry], pages=REWORD_PAGES)
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "nothing applied" not in out
    assert "the widget is what it was called." in page(tmp_path, "rules", "rule-owner")
    assert load_yaml(tmp_path)["entries"][0]["applied"]


def test_a_reword_pair_with_no_hit_or_a_new_the_owner_lacks_fails_the_entry(tmp_path):
    pairs = [{"old": "gadget", "new": "widget"}, {"old": "sprocket", "new": "widget"}]
    seed(tmp_path, entries=[reword_entry(pairs)], pages=REWORD_PAGES)
    code, _, err = run(tmp_path)
    assert code == 1 and "rule-owner: reword: `sprocket` has no hit on a live page" in err
    assert "gadget" in page(tmp_path, "rules", "rule-other")  # nothing applied
    assert "failed" in load_yaml(tmp_path)["entries"][0]

    pairs = [{"old": "gadget", "new": "cog"}]
    seed(tmp_path / "b", entries=[reword_entry(pairs)], pages=REWORD_PAGES)
    code, _, err = run(tmp_path / "b")
    assert code == 1 and "rule-owner: reword: `cog` is not in the owner's text" in err
    assert "gadget" in page(tmp_path / "b", "rules", "rule-other")

    mapping = {"old": "gadget", "new": "widget"}
    seed(tmp_path / "c", entries=[reword_entry(mapping)], pages=REWORD_PAGES)
    code, _, err = run(tmp_path / "c")
    assert code == 1 and "rule-owner: reword: expected a list of old/new pairs" in err


def test_the_owner_check_ignores_case(tmp_path):
    pairs = [{"old": "Gadget", "new": "Widget"}]
    other = OTHER_RULE.replace("The agent at gadget", "The agent at Gadget")
    pages = [p if p[1] != "rule-other" else ("rules", "rule-other", other) for p in REWORD_PAGES]
    seed(tmp_path, entries=[reword_entry(pairs)], pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    assert "The agent at Widget and at retro" in page(tmp_path, "rules", "rule-other")
    assert "the gadget is what it was called." in page(tmp_path, "rules", "rule-owner")  # case kept


# --- the read line of a Case ratified after the reading (case 280) ---------------------

LATER_SPEC = """# Spec

## Case 1 — the root

```tasks
- [ ] create `rule-root` (no `ref`)
```

## Case 2 — the recut, ratified after the reading

```tasks
- [ ] update `rule-root`: `set`, `change`
- [ ] read `estimate-child-works`: the next session, by hand
```
"""


def with_older_spec(tmp_path):
    older = tmp_path / "vault" / "raw" / "2026-09-09" / "0900" / "spec.md"
    older.parent.mkdir(parents=True)
    older.write_text(
        "## Case 7 — y\n\n- [ ] read `estimate-child-works`: by hand\n",
        encoding="utf-8",
        newline="\n",
    )
    return older


def test_a_reading_before_the_case_skips_its_line_and_ticks_the_older_spec(tmp_path):
    seed(
        tmp_path,
        entries=[CHILD, CHILD_ESTIMATE, ROOT, child_reading(line=4), spec_update("2", line=6)],
    )
    spec = with_spec(tmp_path, LATER_SPEC)
    older = with_older_spec(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] update `rule-root`: `set`, `change`" in text  # the page line, as before
    assert "- [ ] read `estimate-child-works`: the next session" in text  # Case 2 came after
    assert "- [x] read `estimate-child-works`: by hand" in older.read_text(encoding="utf-8")


def test_a_reading_after_the_case_ticks_its_line(tmp_path):
    seed(
        tmp_path,
        entries=[CHILD, CHILD_ESTIMATE, ROOT, spec_update("2", line=6), child_reading(line=8)],
    )
    spec = with_spec(tmp_path, LATER_SPEC)
    older = with_older_spec(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    assert "- [x] read `estimate-child-works`: the next session" in spec.read_text(encoding="utf-8")
    # case 326: the walk no longer stops at the first Spec that holds a line
    assert "- [x] read `estimate-child-works`: by hand" in older.read_text(encoding="utf-8")


def test_a_reading_before_the_case_with_no_other_line_ticks_nothing(tmp_path):
    seed(
        tmp_path,
        entries=[CHILD, CHILD_ESTIMATE, ROOT, child_reading(line=4), spec_update("2", line=6)],
    )
    spec = with_spec(tmp_path, LATER_SPEC)
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "read" not in out.lower()
    assert "- [ ] read `estimate-child-works`: the next session" in spec.read_text(encoding="utf-8")
    assert all(e.get("applied") for e in load_yaml(tmp_path)["entries"])


# --- the read line of a superseded Case (case 286) -------------------------------------

SUPERSEDED_SPEC = """# Spec

## Case 1 — the root

```tasks
- [ ] create `rule-root` (no `ref`)
```

## Case 2 — the first cut, superseded by 3

```tasks
- [ ] update `rule-root`: `set`, `change`
- [ ] read `estimate-child-works`: the next session, by hand
```

## Case 3 — the recut; supersedes 2

```tasks
- [ ] update `rule-root`: `set`, `change`, again
- [ ] read `estimate-child-works`: the next session, by hand, on the recut
```
"""


def other_session(tmp_path, folder="0900", date="2026-09-09", superseded=True, with_yaml=True):
    unit = tmp_path / "vault" / "raw" / date / folder
    unit.mkdir(parents=True)
    spec = unit / "spec.md"
    spec.write_text(
        "## Case 7 — y\n\n- [ ] read `estimate-child-works`: by hand\n\n"
        "## Case 8 — z\n\n- [ ] read `estimate-child-works`: by hand, on the recut\n",
        encoding="utf-8",
        newline="\n",
    )
    if with_yaml:
        entry = dict(spec_update("7", line=2), applied="10:00:00")
        if superseded:
            entry["superseded_by"] = "8"
        data = {"date": date, "sprint": "migration", "entries": [entry], "decisions": []}
        (unit / "materialize.yaml").write_text(
            yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )
    return spec


def test_a_reading_skips_the_read_line_of_a_superseded_case_beside_the_yaml(tmp_path):
    superseded = dict(spec_update("2", line=4), superseded_by="3")
    recut = spec_update("3", line=6, supersedes="2")
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, superseded, recut, child_reading(line=8)])
    spec = with_spec(tmp_path, SUPERSEDED_SPEC)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [ ] read `estimate-child-works`: the next session, by hand\n" in text  # Case 2
    assert "- [x] read `estimate-child-works`: the next session, by hand, on the recut" in text


def test_a_reading_skips_the_superseded_case_of_another_sessions_yaml(tmp_path):
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, child_reading()])
    with_spec(tmp_path, "## Case 1 — x\n\n- [ ] create `rule-root`\n")  # no read line here
    other = other_session(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = other.read_text(encoding="utf-8")
    assert "- [ ] read `estimate-child-works`: by hand\n" in text  # Case 7, superseded by 8
    assert "- [x] read `estimate-child-works`: by hand, on the recut" in text


def test_no_yaml_beside_another_sessions_spec_skips_nothing(tmp_path):
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, child_reading()])
    with_spec(tmp_path, "## Case 1 — x\n\n- [ ] create `rule-root`\n")
    other = other_session(tmp_path, with_yaml=False)
    assert run(tmp_path)[0] == 0
    text = other.read_text(encoding="utf-8")
    # case 312: no yaml beside it, so no Case is skipped and both lines of the slug tick
    assert "- [x] read `estimate-child-works`: by hand\n" in text
    assert "- [x] read `estimate-child-works`: by hand, on the recut" in text


def test_a_folded_reading_skips_a_superseded_case_too(tmp_path):
    folded = dict(CHILD_ESTIMATE, status="passed", result="green", folded=[4])
    seed(tmp_path, entries=[CHILD, folded, ROOT])
    spec = with_spec(tmp_path, "## Case 1 — x\n\n- [ ] create `estimate-child-works`\n")
    other = other_session(tmp_path)  # the read line is in the other session's Spec only
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    assert "- [x] create `estimate-child-works`" in spec.read_text(encoding="utf-8")
    text = other.read_text(encoding="utf-8")
    assert "- [ ] read `estimate-child-works`: by hand\n" in text  # Case 7, superseded by 8
    assert "- [x] read `estimate-child-works`: by hand, on the recut" in text


# --- the read lines of a deleted Estimate (case 463) -----------------------------------


def delete_entry(case, slug="estimate-child-works", line=6):
    return {
        "line": line,
        "text": "",
        "case": case,
        "kind": "delete",
        "category": "estimates",
        "slug": slug,
        "origin": f"raw/{DATE}/ledger.md#case-{case}",
        "decision": f"decision-case-{case}",
    }


DELETE_SPEC = """# Spec

## Case 1 — the root

```tasks
- [ ] create `rule-root` (no `ref`)
- [ ] read `estimate-child-works`: pytest, then live
```

## Case 2 — the delete

```tasks
- [ ] delete `estimate-child-works`
```
"""


def test_a_delete_ticks_the_read_lines_of_its_slug_beside_the_yaml_and_in_an_older_spec(
    tmp_path,
):
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, delete_entry("2")])
    spec = with_spec(tmp_path, DELETE_SPEC)
    older = with_older_spec(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] delete `estimate-child-works`" in text  # its page line, as before
    assert "- [x] read `estimate-child-works`: pytest, then live" in text
    assert "- [x] read `estimate-child-works`: by hand" in older.read_text(encoding="utf-8")


def test_a_delete_leaves_the_read_line_of_a_case_ratified_after_it(tmp_path):
    # an update can bring the archived page back (case 105.3); the later Case's line waits
    # for a reading of its own
    later = spec_update("3", line=8)
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, delete_entry("2", line=6), later])
    spec = with_spec(
        tmp_path,
        DELETE_SPEC + "\n## Case 3 — ratified after the delete\n\n"
        "```tasks\n- [ ] update `rule-root`\n"
        "- [ ] read `estimate-child-works`: on the page brought back\n```\n",
    )
    older = with_older_spec(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] read `estimate-child-works`: pytest, then live" in text  # Case 1, before
    assert "- [ ] read `estimate-child-works`: on the page brought back" in text  # Case 3
    assert "- [x] read `estimate-child-works`: by hand" in older.read_text(encoding="utf-8")


def test_a_repeated_delete_leaves_the_read_line_of_a_case_ratified_between(tmp_path):
    # case 522: a repeat of the delete after a later Case ticks no read line of that Case
    later = spec_update("3", line=8)
    repeat = delete_entry("2", line=10)
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, delete_entry("2", line=6), later, repeat])
    spec = with_spec(
        tmp_path,
        DELETE_SPEC + "\n## Case 3 — ratified between the two lines\n\n"
        "```tasks\n- [ ] update `rule-root`\n"
        "- [ ] read `estimate-child-works`: on the page brought back\n```\n",
    )
    code, out, err = run(tmp_path)
    assert code == 0 and err == ""
    assert "line 10 repeats line 6 of case 2; nothing applied" in out
    text = spec.read_text(encoding="utf-8")
    assert "- [x] read `estimate-child-works`: pytest, then live" in text  # the first delete
    assert "- [ ] read `estimate-child-works`: on the page brought back" in text


def test_a_delete_leaves_the_read_line_of_a_superseded_case(tmp_path):
    superseded = dict(spec_update("2", line=4), superseded_by="3")
    recut = spec_update("3", line=6, supersedes="2")
    entries = [CHILD, CHILD_ESTIMATE, ROOT, superseded, recut, delete_entry("4", line=8)]
    seed(tmp_path, entries=entries)
    spec = with_spec(
        tmp_path,
        SUPERSEDED_SPEC + "\n## Case 4 — the delete\n\n"
        "```tasks\n- [ ] delete `estimate-child-works`\n```\n",
    )
    other = other_session(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] delete `estimate-child-works`" in text
    assert "- [ ] read `estimate-child-works`: the next session, by hand\n" in text  # Case 2
    assert "- [x] read `estimate-child-works`: the next session, by hand, on the recut" in text
    text = other.read_text(encoding="utf-8")
    assert "- [ ] read `estimate-child-works`: by hand\n" in text  # Case 7, superseded by 8
    assert "- [x] read `estimate-child-works`: by hand, on the recut" in text


def test_a_failed_delete_ticks_nothing(tmp_path):
    seed(tmp_path, entries=[ROOT, delete_entry("2", slug="estimate-gone")])
    text = (
        "## Case 1 — x\n\n- [ ] read `estimate-gone`: pytest\n\n"
        "## Case 2 — the delete\n\n- [ ] delete `estimate-gone`\n"
    )
    spec = with_spec(tmp_path, text)
    older = tmp_path / "vault" / "raw" / "2026-09-09" / "0900" / "spec.md"
    older.parent.mkdir(parents=True)
    older_text = "## Case 7 — y\n\n- [ ] read `estimate-gone`: by hand\n"
    older.write_text(older_text, encoding="utf-8", newline="\n")
    code, _, err = run(tmp_path)
    assert code == 1 and "generate: estimate-gone: no page to delete" in err
    assert spec.read_text(encoding="utf-8") == text
    assert older.read_text(encoding="utf-8") == older_text
    assert load_yaml(tmp_path)["entries"][1]["failed"]


def test_a_delete_leaves_a_spec_under_the_archive_unchanged(tmp_path):
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, delete_entry("2")])
    spec = with_spec(tmp_path, DELETE_SPEC)
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-08" / "0700" / "raw"
    archived.mkdir(parents=True)
    archived_text = "## Case 5 — z\n\n- [ ] read `estimate-child-works`: archived\n"
    (archived / "spec.md").write_text(archived_text, encoding="utf-8", newline="\n")
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] read `estimate-child-works`: pytest, then live" in text
    # case 326: the archive keeps its open line, the record of a task nobody performed
    assert (archived / "spec.md").read_text(encoding="utf-8") == archived_text


# --- the read lines of an Estimate closed by the person's decision (case 672) -----------


def close_entry(case, status="passed", slug="estimate-child-works", line=6):
    return spec_update(case, slug=slug, line=line, category="estimates", set={"status": status})


CLOSE_SPEC = DELETE_SPEC.replace("## Case 2 — the delete", "## Case 2 — the close").replace(
    "- [ ] delete `estimate-child-works`", "- [ ] update `estimate-child-works`"
)


@pytest.mark.parametrize("status", ["passed", "failed"])
def test_an_update_that_closes_an_estimate_ticks_its_read_lines_beside_the_yaml_and_older(
    tmp_path, status
):
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, close_entry("2", status)])
    spec = with_spec(tmp_path, CLOSE_SPEC)
    older = with_older_spec(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] update `estimate-child-works`" in text  # its page line, as before
    assert "- [x] read `estimate-child-works`: pytest, then live" in text
    assert "- [x] read `estimate-child-works`: by hand" in older.read_text(encoding="utf-8")


@pytest.mark.parametrize("sets", [{"status": "pending"}, {"method": "pytest tests/test_y.py"}])
def test_an_update_that_sets_pending_or_no_status_ticks_no_read_line(tmp_path, sets):
    entry = spec_update("2", slug="estimate-child-works", line=6, category="estimates", set=sets)
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, entry])
    spec = with_spec(tmp_path, CLOSE_SPEC)
    older = with_older_spec(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] update `estimate-child-works`" in text
    assert "- [ ] read `estimate-child-works`: pytest, then live" in text
    assert "- [ ] read `estimate-child-works`: by hand" in older.read_text(encoding="utf-8")


def test_an_update_that_closes_leaves_the_read_line_of_a_case_ratified_after_it(tmp_path):
    later = spec_update("3", line=8)
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, close_entry("2", line=6), later])
    spec = with_spec(
        tmp_path,
        CLOSE_SPEC + "\n## Case 3 — ratified after the close\n\n"
        "```tasks\n- [ ] update `rule-root`\n"
        "- [ ] read `estimate-child-works`: on the new Criterion\n```\n",
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [x] read `estimate-child-works`: pytest, then live" in text  # Case 1, before
    assert "- [ ] read `estimate-child-works`: on the new Criterion" in text  # Case 3


def test_an_update_that_closes_leaves_the_read_line_of_a_superseded_case(tmp_path):
    superseded = dict(spec_update("2", line=4), superseded_by="3")
    recut = spec_update("3", line=6, supersedes="2")
    entries = [CHILD, CHILD_ESTIMATE, ROOT, superseded, recut, close_entry("4", line=8)]
    seed(tmp_path, entries=entries)
    spec = with_spec(
        tmp_path,
        SUPERSEDED_SPEC + "\n## Case 4 — the close\n\n"
        "```tasks\n- [ ] update `estimate-child-works`\n```\n",
    )
    other = other_session(tmp_path)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    text = spec.read_text(encoding="utf-8")
    assert "- [ ] read `estimate-child-works`: the next session, by hand\n" in text  # Case 2
    assert "- [x] read `estimate-child-works`: the next session, by hand, on the recut" in text
    text = other.read_text(encoding="utf-8")
    assert "- [ ] read `estimate-child-works`: by hand\n" in text  # Case 7, superseded by 8
    assert "- [x] read `estimate-child-works`: by hand, on the recut" in text


def test_a_repeated_update_that_closes_leaves_the_read_line_of_a_case_ratified_between(
    tmp_path,
):
    later = spec_update("3", line=8)
    repeat = close_entry("2", line=10)
    seed(tmp_path, entries=[CHILD, CHILD_ESTIMATE, ROOT, close_entry("2", line=6), later, repeat])
    spec = with_spec(
        tmp_path,
        CLOSE_SPEC + "\n## Case 3 — ratified between the two lines\n\n"
        "```tasks\n- [ ] update `rule-root`\n"
        "- [ ] read `estimate-child-works`: on the new Criterion\n```\n",
    )
    code, out, err = run(tmp_path)
    assert code == 0 and err == ""
    assert "line 10 repeats line 6 of case 2; nothing applied" in out
    text = spec.read_text(encoding="utf-8")
    assert "- [x] read `estimate-child-works`: pytest, then live" in text  # the first update
    assert "- [ ] read `estimate-child-works`: on the new Criterion" in text


def test_a_failed_update_that_closes_ticks_nothing(tmp_path):
    seed(tmp_path, entries=[ROOT, close_entry("2", slug="estimate-gone")])
    text = (
        "## Case 1 — x\n\n- [ ] read `estimate-gone`: pytest\n\n"
        "## Case 2 — the close\n\n- [ ] update `estimate-gone`\n"
    )
    spec = with_spec(tmp_path, text)
    code, _, err = run(tmp_path)
    assert code == 1 and "estimate-gone" in err
    assert spec.read_text(encoding="utf-8") == text
    assert load_yaml(tmp_path)["entries"][1]["failed"]


# --- case 305.3: the cascade writes rules on an Entity from the applies_to of the rules ----


def guard_text(slug, applies_to):
    return page_text("rules", slug, kind="Leaf", applies_to=f"[{', '.join(applies_to)}]")


def estimate_text(slug, status, target):
    return (
        f"---\ntype: estimate\nkind: QA\nstatus: {status}\ntarget: {target}\n"
        f"method: pytest tests/test_x.py\norigin: raw/2026-09-01/ledger.md#case-1\n"
        f"sprint: migration\ncreated: 2026-09-01\ntags: [harness]\n---\n\n"
        f"## Criterion\n\nc\n\n## Result\n\nr\n\n## History\n\n- 2026-09-01 created · x\n"
    )


def test_the_cascade_passes_over_an_archived_estimate(tmp_path):
    # case 328: a `delete` of the same run left the file under wiki/estimates/ and the slug
    # in the target's list; `cleanup` takes it out only after `generate`, so counting it
    # dropped a page whose live promises all hold back to `draft` for a whole session
    pages = [
        (
            "rules",
            "rule-counted",
            page_text(
                "rules",
                "rule-counted",
                estimates="[estimate-counted-holds, estimate-counted-retired]",
            ),
        ),
        ("estimates", "estimate-counted-holds", estimate_text("x", "passed", "rule-counted")),
        ("estimates", "estimate-counted-retired", estimate_text("y", "archived", "rule-counted")),
    ]
    seed(tmp_path, entries=[ROOT], pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    rule = page(tmp_path, "rules", "rule-counted")
    assert props(rule)["status"] == "built"
    assert f"- {DATE} status: draft → built · cascade" in rule


def test_the_cascade_recounts_rules_from_the_applies_to_of_the_live_rules(tmp_path):
    pages = [
        ("entities", "entity-thing", page_text("entities", "entity-thing")),
        ("entities", "entity-other", page_text("entities", "entity-other", rules="[rule-b]")),
        ("entities", "entity-plain", page_text("entities", "entity-plain")),
        ("rules", "rule-b", guard_text("rule-b", ["entity-thing"])),
        ("rules", "rule-a", guard_text("rule-a", ["entity-thing", "entity-nowhere"])),
    ]
    seed(tmp_path, entries=[ROOT], pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    thing = page(tmp_path, "entities", "entity-thing")
    assert props(thing)["rules"] == ["rule-a", "rule-b"]  # slug order, as wikilinks
    assert 'rules: ["[[rule-a]]", "[[rule-b]]"]' in thing
    assert f"- {DATE} rules: [rule-a, rule-b] · cascade" in thing
    other = page(tmp_path, "entities", "entity-other")
    assert props(other)["rules"] == [] and f"- {DATE} rules: [] · cascade" in other
    plain = page(tmp_path, "entities", "entity-plain")
    assert "rules:" not in plain and "cascade" not in plain  # no edge, no field
    assert "applies_to" not in thing  # never computed
    rule_a = props(page(tmp_path, "rules", "rule-a"))
    assert rule_a["applies_to"] == ["entity-thing", "entity-nowhere"]


def test_an_archived_rule_gives_no_edge_and_an_unchanged_rules_writes_no_history(tmp_path):
    pages = [
        ("entities", "entity-thing", page_text("entities", "entity-thing", rules="[rule-a]")),
        ("rules", "rule-a", guard_text("rule-a", ["entity-thing"])),
    ]
    seed(tmp_path, entries=[ROOT], pages=pages)
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-01" / "rules" / "rule-z.md"
    archived.parent.mkdir(parents=True)
    archived.write_text(guard_text("rule-z", ["entity-thing"]), encoding="utf-8", newline=NL)
    code, _, err = run(tmp_path)
    assert code == 0 and err == ""
    thing = page(tmp_path, "entities", "entity-thing")
    assert props(thing)["rules"] == ["rule-a"] and "cascade" not in thing


# --- no line of the sprint page moves (case 539.1): `estimate-sprint-items-move-only-by-a-
# case` -----------------------------------------------------------------------------

SPRINT_PAGE = """\
---
type: entity
kind: Leaf
purpose: The sprint
status: draft
origin: x
sprint: migration
created: 2026-09-01
tags: [sprint]
---

## Purpose

The sprint.

## Milestones

### Slice 3b — Work Mode

- [[rule-work]] — the work
- [[rule-agent]] — the agent

### Slice 4 — later

- [[rule-later]] — the later one

## Backlog

- an old note

## History

- 2026-09-01 created · x
"""


def frontier(tmp_path, where, *lines):
    """The Frontier of one session; `where` is `raw/<date>/<HHMM>`, or
    `archive/<sprint>/<date>/<HHMM>/raw` for an archived one."""
    path = tmp_path / "vault" / where / "frontier.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "# Frontier" + NL + NL + "## Cases" + NL + NL + NL.join(lines) + NL
    path.write_text(text, encoding="utf-8", newline=NL)


def passed(slug, closer="· sprint · sprint", box="-"):
    return f"- [{box}] C1 — `{slug}`, Slice 3b {closer}"


def seed_sprint(tmp_path, text=SPRINT_PAGE):
    return seed(tmp_path, pages=[("entities", "entity-sprint-x", text)])


def test_generate_moves_no_line_of_the_sprint_page(tmp_path):
    seed_sprint(tmp_path)
    for day in ("01", "02", "03", "04"):
        frontier(tmp_path, f"raw/2026-09-{day}/0900", passed("rule-work"), passed("rule-agent"))
    frontier(
        tmp_path, "archive/migration/2026-08-31/0900/raw", passed("rule-later", "· defer case 7")
    )
    code, out, err = run(tmp_path)
    assert code == 0 and err == ""
    # put off in four sessions in a row, the whole milestone included: every line in place
    assert page(tmp_path, "entities", "entity-sprint-x") == SPRINT_PAGE
    assert "moved" not in out and "left the Milestones" not in out


# --- Case 464: the roads of an entry of `category: unknown` ------------------------------


def unknown_entry(kind, slug, **extra):
    """An entry lifted from a ledger line whose slug has no category prefix (case 320)."""
    return {
        "line": 2,
        "text": "",
        "case": "2",
        "kind": kind,
        "category": "unknown",
        "slug": slug,
        "origin": f"raw/{DATE}/ledger.md#case-2",
        "decision": "decision-case-2",
        **extra,
    }


def test_an_update_of_an_unknown_category_applies_to_its_page_in_any_folder(tmp_path):
    entry = unknown_entry("update", "odd-thing", change="renamed by hand")
    odd = ("rules", "odd-thing", page_text("rules", "odd-thing"))
    seed(tmp_path, entries=[ROOT, entry], pages=[odd])
    tasks = "```tasks\n- [ ] update `odd-thing`\n```\n"
    spec = with_spec(tmp_path, "# Spec\n\n## Case 2 — odd\n\n" + tasks)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    assert load_yaml(tmp_path)["entries"][1]["applied"]
    assert "[[decision-case-2]]" in page(tmp_path, "rules", "odd-thing").split("## History")[1]
    assert "- [x] update `odd-thing`" in spec.read_text(encoding="utf-8")


def test_a_create_of_an_unknown_category_fails_not_a_vault_folder(tmp_path):
    entry = unknown_entry("create", "odd-thing", fields={"type": "rule", "purpose": "x"})
    seed(tmp_path, entries=[ROOT, entry])
    code, _, err = run(tmp_path)
    assert code == 1
    assert "generate: odd-thing: category 'unknown' is not a vault folder" in err
    assert "failed" in load_yaml(tmp_path)["entries"][1]
    assert not list((tmp_path / "vault" / "wiki").glob("*/odd-thing.md"))


def test_a_defer_of_an_unknown_category_with_no_page_fails_not_a_vault_folder(tmp_path):
    entry = unknown_entry("defer", "odd-thing", purpose="later")
    seed(tmp_path, entries=[ROOT, entry])
    code, _, err = run(tmp_path)
    assert code == 1
    assert "generate: odd-thing: category 'unknown' is not a vault folder" in err
    assert "failed" in load_yaml(tmp_path)["entries"][1]


# --- Case 467.3: a supersede clears a defer only from the pages its Case names -------------

SHARED_DEFER = (
    '---\ntype: decision\ncase: "2"\nstatus: {status}\ndefer: [rule-a, rule-b]\n{extra}'
    f"origin: raw/{DATE}/ledger.md#case-2\nsprint: migration\ncreated: {DATE}\ntags: []\n---\n\n"
    "## Context\n\nc\n\n## Problem\n\np\n\n## History\n\n- created\n"
)


def taking_up(slug, case):
    """An `update` of one page of the shared defer, superseding `decision-case-2`."""
    entry = update_of(slug, 3, change="taken up", supersedes="2")
    entry.update(case=case, decision=f"decision-case-{case}")
    return entry


def seed_shared(tmp_path, entry, deferred):
    """`decision-case-2` defers `rule-a` and `rule-b`; the pages in `deferred` carry it."""
    pages = []
    for slug in ("rule-a", "rule-b"):
        extra = {"deferred_by": "[decision-case-2]"} if slug in deferred else {}
        pages.append(("rules", slug, page_text("rules", slug, **extra)))
    decisions = records_for([entry])
    decisions[0]["supersedes"] = ["decision-case-2"]
    seed(tmp_path, entries=[entry], decisions=decisions, pages=pages)


def test_a_supersede_of_a_shared_defer_clears_only_the_page_its_case_names(tmp_path):
    seed_shared(tmp_path, taking_up("rule-a", "3"), ("rule-a", "rule-b"))
    (tmp_path / "vault" / "wiki" / "decisions" / "decision-case-2.md").write_text(
        SHARED_DEFER.format(status="current", extra=""), encoding="utf-8", newline="\n"
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    assert "deferred_by" not in props(page(tmp_path, "rules", "rule-a"))
    b = page(tmp_path, "rules", "rule-b")
    assert props(b)["deferred_by"] == ["decision-case-2"]
    assert "superseded" not in b.split("## History")[1]


def test_a_later_case_superseding_the_archived_decision_clears_the_page_it_names(tmp_path):
    seed_shared(tmp_path, taking_up("rule-b", "4"), ("rule-b",))  # rule-a cleared before
    archived = tmp_path / "vault" / "archive" / "migration" / DATE / "1200" / "decisions"
    archived.mkdir(parents=True)
    (archived / "decision-case-2.md").write_text(
        SHARED_DEFER.format(status="archived", extra="superseded_by: [decision-case-3]\n"),
        encoding="utf-8",
        newline="\n",
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    b = page(tmp_path, "rules", "rule-b")
    assert "deferred_by" not in props(b)
    assert f"- {DATE} defer by decision-case-2 superseded · [[decision-case-4]]" in b
    # case 683: the archived page stays archived where it lies, so cleanup leaves it there
    earlier = (archived / "decision-case-2.md").read_text(encoding="utf-8")
    assert props(earlier)["status"] == "archived"
    assert props(earlier)["superseded_by"] == ["decision-case-3", "decision-case-4"]
    assert earlier.count("superseded by decision-case-4") == 1
    assert not (tmp_path / "vault" / "wiki" / "decisions" / "decision-case-2.md").exists()


# --- Case 660.3: a superseded Decision page takes the pages of its sub-cases with it -------
# `estimate-generate-writes-the-decision-page`

SUPERSEDED_BY_SIX = "superseded by decision-case-6"


def family_record(case, **extra):
    record = {
        "case": case,
        "decision": f"decision-case-{case}",
        "origin": f"raw/{DATE}/ledger.md#case-{case}",
        "tags": [],
        "targets": [],
        "case_text": {"given": "g", "when": "w", "then": "t"},
    }
    record.update(extra)
    return record


def superseding_six():
    return family_record(
        "6",
        targets=[{"kind": "update", "category": "rules", "slug": "rule-root"}],
        supersedes=["decision-case-5"],
    )


def test_a_supersedes_of_a_parent_sets_its_sub_case_pages_superseded_in_the_same_run(tmp_path):
    later = page_text("rules", "rule-later", deferred_by="[decision-case-5.2.1]")
    decisions = [
        family_record("5.1", parent="decision-case-5"),
        family_record("5.2", parent="decision-case-5", children=["decision-case-5.2.1"]),
        family_record(
            "5.2.1",
            parent="decision-case-5.2",
            targets=[{"kind": "defer", "category": "rules", "slug": "rule-later"}],
        ),
        superseding_six(),
        family_record(
            "5",
            children=["decision-case-5.1", "decision-case-5.2"],
            case_text={"context": "c", "problem": "p"},
        ),
    ]
    seed(tmp_path, entries=[ROOT], decisions=decisions, pages=[("rules", "rule-later", later)])
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    for case in ("5", "5.1", "5.2", "5.2.1"):
        text = page(tmp_path, "decisions", f"decision-case-{case}")
        assert props(text)["superseded_by"] == ["decision-case-6"]
        assert props(text)["status"] == "archived"  # the cascade of 104.1 follows
        assert text.split("## History")[1].count(SUPERSEDED_BY_SIX) == 1
    # a child's `defer` target keeps its mark: only the page the tag names clears its own
    assert props(page(tmp_path, "rules", "rule-later"))["deferred_by"] == ["decision-case-5.2.1"]


def test_a_sub_case_superseded_with_its_parent_and_named_too_takes_one_line(tmp_path):
    # case 773: the parent step marks 5.1 first, the step of the named 5.1 writes nothing again
    six = superseding_six()
    six["supersedes"] = ["decision-case-5", "decision-case-5.1"]
    decisions = [
        family_record("5.1", parent="decision-case-5"),
        six,
        family_record(
            "5", children=["decision-case-5.1"], case_text={"context": "c", "problem": "p"}
        ),
    ]
    seed(tmp_path, entries=[ROOT], decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = page(tmp_path, "decisions", "decision-case-5.1")
    assert props(text)["superseded_by"] == ["decision-case-6"]
    assert text.split("## History")[1].count(SUPERSEDED_BY_SIX) == 1
    log = (tmp_path / "vault" / "wiki" / "log.md").read_text(encoding="utf-8")
    assert log.count(f"decision-case-5.1 {SUPERSEDED_BY_SIX}") == 1


def decision_page(case, status, extra=""):
    return (
        f'---\ntype: decision\ncase: "{case}"\nstatus: {status}\n{extra}'
        f"origin: raw/2026-09-01/ledger.md#case-{case}\nsprint: migration\n"
        "created: 2026-09-01\ntags: []\n---\n\n## Problem\n\np\n\n## History\n\n"
        "- 2026-09-01 created · x\n"
    )


def test_a_supersedes_of_a_parent_of_an_earlier_run_leaves_an_archived_child_alone(tmp_path):
    pages = [
        (
            "decisions",
            "decision-case-5",
            decision_page(
                "5",
                "current",
                "children: [decision-case-5.1, decision-case-5.2, decision-case-5.3]\n",
            ),
        ),
        ("decisions", "decision-case-5.1", decision_page("5.1", "current")),
        ("decisions", "decision-case-5.2", decision_page("5.2", "archived")),
        (
            "decisions",
            "decision-case-5.3",
            decision_page("5.3", "current", "superseded_by: [decision-case-6]\n"),
        ),
    ]
    seed(tmp_path, entries=[ROOT], decisions=[superseding_six()], pages=pages)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    first = page(tmp_path, "decisions", "decision-case-5.1")
    assert props(first)["superseded_by"] == ["decision-case-6"]
    assert first.split("## History")[1].count(SUPERSEDED_BY_SIX) == 1
    archived = page(tmp_path, "decisions", "decision-case-5.2")
    assert props(archived)["status"] == "archived" and "superseded_by" not in props(archived)
    assert SUPERSEDED_BY_SIX not in archived
    marked = page(tmp_path, "decisions", "decision-case-5.3")  # already names the Case
    assert SUPERSEDED_BY_SIX not in marked.split("## History")[1]
