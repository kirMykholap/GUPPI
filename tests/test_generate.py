"""`guppi generate`: pages from `materialize.yaml`, derived fields, backlinks, History, log."""

import io
import shutil
from datetime import UTC, datetime
from pathlib import Path

import yaml

from guppi import generate, lint

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
  required: ["## Context", "## Problem", "## History"]
  optional: ["## Given", "## When", "## Criterion", "## Note"]
"""
DECISIONS_MD = """\
# Decision — page schema

## Properties

| Field | Required |
|---|---|
| `type` | yes |
| `case` | yes |
| `status` | yes |
| `create` | no |
| `update` | no |
| `delete` | no |
| `defer` | no |
| `source` | no |
| `supersedes` | no |
| `superseded_by` | no |
| `origin` | yes |
| `sprint` | yes |
| `created` | yes |
| `tags` | yes |

## Body

| Section | Required |
|---|---|
| `## Context` | yes |
| `## Problem` | yes |
| `## Given` | no |
| `## When` | no |
| `## Criterion` | no |
| `## Note` | no |

## History
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


def seed(tmp_path, entries=(), decisions=None, new_tags=(), pages=()):
    if decisions is None:
        decisions = records_for(entries)
    wiki = tmp_path / "vault" / "wiki"
    for category in ("entities", "rules", "estimates", "lessons", "insights", "decisions"):
        (wiki / category).mkdir(parents=True)
        for name in ("schema.yaml", "schema.md"):
            shutil.copy(REPO / "vault" / "wiki" / category / name, wiki / category / name)
    (wiki / "decisions" / "schema.yaml").write_text(DECISIONS_YAML, encoding="utf-8", newline="\n")
    (wiki / "decisions" / "schema.md").write_text(DECISIONS_MD, encoding="utf-8", newline="\n")
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
    return yaml.safe_load(text.split("---")[1])


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
    {"type": "estimate", "kind": "QA"},
    ref="rule-child",
    sections={
        "Context": "Why it matters.",
        "Criterion": "the child works",
        "Method": "pytest in tests/test_x.py",
    },
    tags=["harness"],
    line=3,
)


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
    assert "## Children\n\n1. [[rule-child]]" in page(tmp_path, "rules", "rule-root")
    child = page(tmp_path, "rules", "rule-child")
    assert props(child)["parent"] == "rule-root" and props(child)["estimates"] == [
        "estimate-child-works"
    ]
    assert "## Purpose\n\nTwo lines of\npurpose.\n" in child
    assert (
        "## Estimates\n\n- [[estimate-child-works]]" in child
        and "## Parent\n\n- [[rule-root]]" in child
    )
    assert "## Implementation\n\n- `guppi/x.py`" in child
    assert f"## History\n\n- {DATE} created · [[decision-case-1]]\n" in child
    estimate = page(tmp_path, "estimates", "estimate-child-works")
    assert props(estimate)["target"] == "rule-child" and props(estimate)["status"] == "pending"
    assert "## Criterion\n\nthe child works" in estimate
    findings = lint.lint(tmp_path)
    assert findings == [], findings
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
    assert lint.lint(tmp_path) == []


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
        "## Context\n\nA root." in one
        and "## Problem\n\nNo root." in one
        and "## Given\n\nNothing." in one
        and "## When" not in one  # the when lives on the Estimate (case 72.4)
        and "Someone asks." not in one
        and "## Then" not in one
        and "A root exists." not in one
    )
    assert one.index("## Problem") < one.index("## Given") < one.index("## History")
    assert f"- {DATE} superseded by decision-case-2 · [[decision-case-2]]" in one
    two = props(page(tmp_path, "decisions", "decision-case-2"))
    assert two["supersedes"] == ["decision-case-1"] and two["tags"] == [
        "harness"
    ]  # from the target page
    findings = [f for f in lint.lint(tmp_path) if "decision-case-2" in f]
    assert findings == [
        "decisions/decision-case-2: schema: missing section ## Context",
        "decisions/decision-case-2: schema: missing section ## Problem",
    ]


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
    assert (
        "create: [rule-root, estimate-root-holds]\nupdate: [case-schema, index]\ndefer: [rule-later]\n"
        in text
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
    wiki = tmp_path / "vault" / "wiki"
    assert not list(wiki.glob("*/old-thing.md"))
    log = (wiki / "log.md").read_text(encoding="utf-8")
    assert "old-thing" not in log


# --- Case 72.4: the derived Estimate, the criterion block added and removed, the decision
# page's Criterion links -----------------------------------------------------------------

CASE_BLOCK_1 = (
    "### case 1\n\nWhen:\nthe hook fires.\n\nThen:\nthe page exists.\n**＋** It is listed."
)
CASE_BLOCK_5 = "### case 5\n\nWhen:\nthe hook fires twice.\n\nThen:\nnothing doubles."
DERIVED_ESTIMATE = create(
    "estimate-child",
    "estimates",
    {"type": "estimate", "kind": "QA"},
    ref="rule-child",
    sections={"Context": "Why it matters.", "Criterion": CASE_BLOCK_1, "Method": "pytest."},
    tags=["harness"],
    line=2,
    derived=True,
)


def estimate_page(criterion, slug="estimate-child", target="rule-child", status="pending"):
    return (
        f"---\ntype: estimate\nkind: QA\nstatus: {status}\ntarget: {target}\norigin: x\n"
        "sprint: s\ncreated: 2026-09-09\ntags: [harness]\n---\n\n## Context\n\nWhy.\n\n"
        f"## Criterion\n\n{criterion}\n\n## Method\n\nold method\n\n## History\n\n- old\n"
    )


def derived_update(slug, block, line=5, **content):
    return {
        "line": line,
        "text": "",
        "case": str(line),
        "kind": "update",
        "category": "estimates",
        "slug": slug,
        "origin": f"raw/{DATE}/ledger.md#case-{line}",
        "decision": f"decision-case-{line}",
        "derived": True,
        "criterion_block": block,
        "set": {"status": "pending"},
        "change": f"criterion: case {line} added",
        **content,
    }


def removal(case, line=6):
    return {
        "line": line,
        "text": "",
        "case": str(line),
        "kind": "remove_criterion",
        "case_removed": str(case),
        "change": f"criterion: case {case} removed",
        "origin": f"raw/{DATE}/ledger.md#case-{line}",
        "decision": f"decision-case-{line}",
    }


def test_a_derived_create_writes_the_estimate_and_lists_it_on_its_target(tmp_path):
    seed(tmp_path, entries=[ROOT, CHILD, DERIVED_ESTIMATE])
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    estimate = page(tmp_path, "estimates", "estimate-child")
    fields = props(estimate)
    assert fields["status"] == "pending" and fields["target"] == "rule-child"
    assert fields["origin"] == ORIGIN and fields["sprint"] == "migration"
    assert str(fields["created"]) == DATE and fields["tags"] == ["harness"]
    assert "derived" not in fields
    assert "## Context\n\nWhy it matters.\n" in estimate
    assert f"## Criterion\n\n{CASE_BLOCK_1}\n\n## Method\n\npytest.\n" in estimate  # verbatim
    assert "## Result" not in estimate
    assert f"## History\n\n- {DATE} created · [[decision-case-1]]\n" in estimate
    child = page(tmp_path, "rules", "rule-child")
    assert props(child)["estimates"] == ["estimate-child"]
    assert "## Estimates\n\n- [[estimate-child]]" in child
    assert f"- {DATE} estimate estimate-child added · [[decision-case-1]]" in child
    log = page(tmp_path, "", "log")
    assert f"- {DATE} estimates/estimate-child created · [[decision-case-1]] · generate" in log
    assert f"- {DATE} rules/rule-child estimate estimate-child added · [[decision-case-1]]" in log


def test_a_derived_update_appends_the_block_sets_pending_and_replaces_method(tmp_path):
    seed(
        tmp_path,
        entries=[
            derived_update("estimate-child", CASE_BLOCK_5, sections={"Method": "new method"}),
            derived_update("estimate-plain", CASE_BLOCK_5, line=7),
        ],
        pages=[
            ("estimates", "estimate-child", estimate_page(CASE_BLOCK_1, status="passed")),
            ("estimates", "estimate-plain", estimate_page("the child works", "estimate-plain")),
        ],
    )
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = page(tmp_path, "estimates", "estimate-child")
    assert props(text)["status"] == "pending"
    assert f"## Criterion\n\n{CASE_BLOCK_1}\n\n{CASE_BLOCK_5}\n\n## Method\n\nnew method\n" in text
    assert f"- {DATE} criterion: case 5 added · [[decision-case-5]]" in text
    assert "updated:" not in text
    plain = page(tmp_path, "estimates", "estimate-plain")
    assert (
        f"## Criterion\n\nthe child works\n\n{CASE_BLOCK_5}\n\n## Method\n\nold method\n" in plain
    )
    # N comes from the block's `### case N` line; the pointer from the entry's Case
    assert f"- {DATE} criterion: case 5 added · [[decision-case-7]]" in plain
    log = page(tmp_path, "", "log")
    assert f"- {DATE} estimates/estimate-child criterion: case 5 added · [[decision-case-5]]" in log


def test_a_derived_update_without_a_target_fails_that_entry_alone(tmp_path):
    missing = derived_update(None, CASE_BLOCK_5, incomplete=["estimate"])
    seed(tmp_path, entries=[ROOT, missing, CHILD])
    code, _, err = run(tmp_path)
    assert code == 1 and "no page to update" in err
    data = load_yaml(tmp_path)
    assert "failed" in data["entries"][1] and "applied" not in data["entries"][1]
    assert data["entries"][0]["applied"] and data["entries"][2]["applied"]


def test_a_remove_criterion_deletes_the_block_from_every_estimate_that_holds_it(tmp_path):
    seed(
        tmp_path,
        entries=[removal(1)],
        pages=[
            ("estimates", "estimate-child", estimate_page(CASE_BLOCK_1 + "\n\n" + CASE_BLOCK_5)),
            (
                "estimates",
                "estimate-other",
                estimate_page(CASE_BLOCK_5 + "\n\n" + CASE_BLOCK_1, "estimate-other", "rule-root"),
            ),
            ("estimates", "estimate-plain", estimate_page("the child works", "estimate-plain")),
        ],
    )
    code, out, err = run(tmp_path)
    assert code == 0 and err == "", err
    assert "no Estimate holds a block" not in out
    text = page(tmp_path, "estimates", "estimate-child")
    assert f"## Criterion\n\n{CASE_BLOCK_5}\n\n## Method" in text and "### case 1" not in text
    assert f"- {DATE} criterion: case 1 removed · [[decision-case-6]]" in text
    other = page(tmp_path, "estimates", "estimate-other")
    assert (
        f"## Criterion\n\n{CASE_BLOCK_5}\n\n## Method" in other and "the page exists" not in other
    )
    assert f"- {DATE} criterion: case 1 removed · [[decision-case-6]]" in other
    plain = page(tmp_path, "estimates", "estimate-plain")
    assert "## Criterion\n\nthe child works\n\n## Method" in plain and "removed" not in plain
    log = page(tmp_path, "", "log")
    assert (
        f"- {DATE} estimates/estimate-child criterion: case 1 removed · [[decision-case-6]]" in log
    )
    assert "estimate-plain" not in log
    assert load_yaml(tmp_path)["entries"][0]["applied"]


def test_a_remove_criterion_with_no_block_anywhere_applies_and_says_so(tmp_path):
    seed(
        tmp_path,
        entries=[removal(9)],
        pages=[("estimates", "estimate-child", estimate_page(CASE_BLOCK_1))],
    )
    code, out, err = run(tmp_path)
    assert code == 0 and err == ""
    assert "remove_criterion: case 9: no Estimate holds a block" in out
    assert "### case 1" in page(tmp_path, "estimates", "estimate-child")
    assert "removed" not in page(tmp_path, "", "log")
    assert load_yaml(tmp_path)["entries"][0]["applied"]


def test_a_decision_page_links_the_estimates_it_shaped_and_has_no_when(tmp_path):
    entries = [ROOT, CHILD, DERIVED_ESTIMATE, CHILD_ESTIMATE]
    decisions = records_for(entries)
    decisions[0]["criterion"] = [
        {"estimate": "estimate-child", "case": "1"},
        {"estimate": "estimate-child-works", "case": "1"},
    ]
    seed(tmp_path, entries=entries, decisions=decisions)
    code, _, err = run(tmp_path)
    assert code == 0 and err == "", err
    text = page(tmp_path, "decisions", "decision-case-1")
    assert "## Given\n\ng\n\n## Criterion\n\n- [[estimate-child]] § case 1\n" in text
    assert "- [[estimate-child-works]] § case 1\n\n## History" in text
    assert "## When" not in text and "criterion:" not in text.split("---")[1]
    assert not [f for f in lint.lint(tmp_path) if "decision-case-1" in f]
