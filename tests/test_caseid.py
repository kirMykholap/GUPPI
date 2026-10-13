"""The one grammar of a Case id and the next id (cases 788.2, 788.4).

`estimate-ratification-case-id-carries-the-sprint`: every reader of a Case id takes an id
that carries its sprint and a plain id alike, and `guppi caseid --next` prints and holds the
next id of the open sprint.
"""

import io
import json
from datetime import UTC, date, datetime
from pathlib import Path

import pytest

from guppi import casecheck, caseid, gate, lint, materialize, ratified
from guppi.pages import Page

TODAY = date(2026, 9, 9)
NOW = datetime(2026, 9, 9, 15, 30, 0, tzinfo=UTC)
STAMP = "44c1aae1"
FORMS = ["kir-plugin-12.1", "785.1"]


@pytest.mark.parametrize("case", FORMS)
def test_parse_line_reads_both_forms(case):
    record = materialize.parse_line(
        f"- decision[case {case}][update][rule-x]{{ref:rule-x}}{{supersedes:case {case}}}"
    )
    assert record["case"] == case and record["supersedes"] == [case]


@pytest.mark.parametrize("case", FORMS)
def test_casecheck_reads_both_forms(case, tmp_path):
    top = case.split(".", 1)[0]
    assert casecheck.top_case(case) == top
    path = casecheck.case_file(tmp_path, case)
    assert path.name == f"case-{top}.md"
    assert casecheck.case_number(path) == top


@pytest.mark.parametrize("case", FORMS)
def test_check_origin_reads_both_forms(case, tmp_path):
    ledger = tmp_path / "vault" / "raw" / TODAY.isoformat() / "1501" / "ledger.md"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(f"- decision[case {case}][update][rule-x]{{ref:rule-x}}\n", encoding="utf-8")
    origin = f"raw/{TODAY.isoformat()}/1501/ledger.md#case-{case}"
    page = Page("rules", "rule-x", tmp_path / "rule-x.md", props={"origin": origin})
    assert lint.check_origin(page, tmp_path) == []


@pytest.mark.parametrize("case", FORMS)
def test_deferred_line_reads_both_forms(case):
    line = f"- 2026-09-09 deferred · [[decision-case-{case}]]"
    assert lint.DEFERRED_LINE.match(line).group(1) == case


def test_case_key_sorts_both_forms():
    order = ["case 9", "case 12.3", "case 12.10", "case kir-plugin-2", "case kir-plugin-12.1"]
    shuffled = ["case kir-plugin-12.1", "case 12.10", "case kir-plugin-2", "case 9", "case 12.3"]
    assert sorted(shuffled, key=gate.case_key) == order


@pytest.mark.parametrize(
    "case, parsed",
    [
        ("785.1", caseid.CaseId(None, 785, (1,))),
        ("kir-plugin-12.1", caseid.CaseId("kir-plugin", 12, (1,))),
        ("kir-v2-3", caseid.CaseId("kir-v2", 3, ())),
        ("kir.plugin-1", None),
        ("Kir-1", None),
    ],
)
def test_parse_splits_the_sprint_the_number_and_the_levels(case, parsed):
    assert caseid.parse(case) == parsed


def test_next_id_counts_the_sprint_or_the_plain_ids():
    ids = ["785.1", "786", "kir-a-3", "kir-a-12.2", "kir-b-40"]
    assert caseid.next_id("kir-a", ids) == "kir-a-13"
    assert caseid.next_id("kir-c", ids) == "kir-c-1"
    assert caseid.next_id("plugin", ids) == "787"
    assert caseid.next_id(None, ids) == "787"


# --- the guard reads a file named by an id of a sprint ------------------------------------


@pytest.fixture
def session(tmp_path):
    """A session: `hi` at 15:01, a plan file under `.claude/plans/`, a sprint page."""
    plan = tmp_path / ".claude" / "plans" / "plan.md"
    plan.parent.mkdir(parents=True)
    plan.write_text("# Session 1501\n", encoding="utf-8")
    log = tmp_path / "vault" / "raw" / TODAY.isoformat() / "event_log.md"
    log.parent.mkdir(parents=True)
    log.write_text(
        f"- 15:01:00 {STAMP} session-start startup\n"
        f"- 15:01:30 {STAMP} hi\n"
        f"- 15:02:00 {STAMP} tool Write: {plan}\n",
        encoding="utf-8",
    )
    return tmp_path


def folder_of(project: Path) -> Path:
    return project / "vault" / "raw" / TODAY.isoformat() / "1501"


def plan_of(project: Path) -> Path:
    return project / ".claude" / "plans" / "plan.md"


def sprint(project: Path, sprint_id: str) -> None:
    path = project / "vault" / "wiki" / "sprint.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# Sprint\n\n## {sprint_id}\n", encoding="utf-8")


@pytest.mark.parametrize("case", ["kir-plugin-12", "785"])
def test_held_number_reads_both_forms(session, case):
    casecheck.store_of(plan_of(session)).write_text(
        json.dumps({case: {"agent_id": "agent-a"}}), encoding="utf-8"
    )
    payload = {
        "session_id": STAMP,
        "tool_name": "Write",
        "agent_type": "case-guppi",
        "agent_id": "agent-b",
        "tool_input": {"file_path": str(casecheck.case_file(folder_of(session), case))},
    }
    held = ratified.held_number(payload, session, NOW, io.StringIO())
    assert held is not None and f"holds case {case} in the store" in held[1]


# --- guppi caseid --next ------------------------------------------------------------------


def next_ids(project: Path) -> list[str]:
    out = []
    for _ in range(2):
        stdout = io.StringIO()
        assert (
            caseid.run(["--next", "--session", STAMP], stdout=stdout, project_dir=project, now=NOW)
            == 0
        )
        out.append(stdout.getvalue().strip())
    return out


def test_next_of_a_new_sprint_starts_at_1_and_holds_each_id(session):
    sprint(session, "kir-next")
    assert next_ids(session) == ["kir-next-1", "kir-next-2"]
    store = json.loads(casecheck.store_of(plan_of(session)).read_text(encoding="utf-8"))
    assert set(store) == {"kir-next-1", "kir-next-2"}
    assert all("agent_id" not in entry and "text" not in entry for entry in store.values())


def test_next_of_a_session_that_creates_a_sprint_page_takes_that_sprint(session):
    sprint(session, "plugin")
    ledger = folder_of(session) / "ledger.md"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(
        "- 15:10:00 decision[case kir-new-1][create][entity-sprint-kir-new]{ref:entity-sprint}\n",
        encoding="utf-8",
    )
    assert next_ids(session) == ["kir-new-2", "kir-new-3"]


def test_next_of_the_sprint_plugin_stays_plain(session):
    sprint(session, "plugin")
    decisions = session / "vault" / "wiki" / "decisions"
    decisions.mkdir(parents=True)
    (decisions / "decision-case-790.md").write_text("---\n---\n", encoding="utf-8")
    cases = folder_of(session) / "cases"
    cases.mkdir(parents=True)
    (cases / "case-791.md").write_text("## Case 791 — x\n", encoding="utf-8")
    assert next_ids(session) == ["792", "793"]
