"""`guppi prespec`: the `PreToolUse ExitPlanMode` hook that holds Plan Mode open until
`/pre-spec` has run in this session, and `guppi prespec --check <plan>`, the check of the
session's decision lines, frontier, tasks, the form of its Leaf items and the grammar of
its record lines against the plan (cases 59.1, 59.2, 59.3, 59.6, 72.5, 73.4, 74, 75.2).
Rule page: `vault/wiki/rules/rule-prespec-hook.md`.

Every hook test feeds the payload through a stream, the shape a hook is really handed. The
check tests build a temp project: an event log with the session's `hi`, a ledger written
after it, a plan file and a frontier in the session's folder `raw/<date>/<hi HHMM>/`.
"""

import io
import json
from datetime import UTC, date, datetime

import pytest

from guppi import prespec

TODAY = date(2026, 9, 9)
NOW = datetime(2026, 9, 9, 18, 40, 5, tzinfo=UTC)
SESSION = "44c1aae1-4076-4a58-a7c0-d20bc274047c"
START = "- 15:01:00 44c1aae1 session-start startup\n"
HI = "- 15:01:30 44c1aae1 hi\n"
PRETASK = "- 16:20:00 44c1aae1 prespec\n"
UNSTAMPED_PRETASK = "- 16:20:00 -------- prespec\n"
FOREIGN_PRETASK = "- 16:20:00 99999999 prespec\n"
OTHER_START = "- 14:00:00 99999999 session-start startup\n"


def payload(tool="ExitPlanMode", session=SESSION):
    fields = {"session_id": session, "hook_event_name": "PreToolUse", "tool_name": tool}
    return io.StringIO(json.dumps(fields))


def with_event_log(project_dir, text, day=TODAY):
    folder = project_dir / "vault" / "raw" / day.isoformat()
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "event_log.md").write_text(text, encoding="utf-8", newline="\n")


def run(stdin, project_dir):
    err = io.StringIO()
    code = prespec.run([], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def test_prespec_after_hi_lets_the_plan_close(tmp_path):
    with_event_log(tmp_path, START + HI + PRETASK)
    assert run(payload(), tmp_path) == (0, "")


def test_hi_without_prespec_holds_plan_mode_open(tmp_path):
    with_event_log(tmp_path, START + HI)
    code, err = run(payload(), tmp_path)
    assert code == 2
    assert "/pre-spec" in err and "44c1aae1" in err


def test_a_prespec_of_another_stamp_does_not_count(tmp_path):
    with_event_log(tmp_path, START + HI + OTHER_START + FOREIGN_PRETASK)
    code, err = run(payload(), tmp_path)
    assert code == 2
    assert "/pre-spec" in err


def test_an_unstamped_prespec_does_not_count(tmp_path):
    with_event_log(tmp_path, START + HI + UNSTAMPED_PRETASK)
    assert run(payload(), tmp_path)[0] == 2


def test_a_foreign_start_between_hi_and_prespec_resets_nothing(tmp_path):
    with_event_log(tmp_path, START + HI + OTHER_START + PRETASK)
    assert run(payload(), tmp_path) == (0, "")


def test_an_ordinary_session_without_hi_is_not_gated(tmp_path):
    with_event_log(tmp_path, START)
    assert run(payload(), tmp_path) == (0, "")


def test_another_tool_is_ignored(tmp_path):
    with_event_log(tmp_path, START + HI)
    assert run(payload(tool="Write"), tmp_path) == (0, "")


def test_no_event_log_means_an_ordinary_session(tmp_path):
    assert run(payload(), tmp_path) == (0, "")


def test_garbage_on_stdin_never_fails_the_session(tmp_path):
    with_event_log(tmp_path, START + HI)
    assert run(io.StringIO("not json"), tmp_path) == (0, "")


def test_cli_dispatches_to_prespec(tmp_path, monkeypatch, capsys, pinned_clock):
    from guppi import cli

    today = pinned_clock.date()  # the CLI reads the clock, pinned by conftest (case 145.1)

    with_event_log(tmp_path, START + HI, day=today)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", payload())
    assert cli.main(["prespec"]) == 2
    assert "/pre-spec" in capsys.readouterr().err


# --- `guppi prespec --check <plan>` ---------------------------------------------------

LINE = "- 16:00:00 decision[case 1][update][rule-x]{ref:rule-x}\n"
BEFORE_HI = "- 15:01:00 decision[case 1][update][rule-x]{ref:rule-x}\n"

PLAN = """# Plan

## Case 1 — one

> **context:**
> Something.

```then
update:
  - slug: rule-x
    change: one line
```

```tasks
- [ ] guppi/x.py: the change
```
"""

CLEAN_FRONTIER = "# Frontier\n\n- [x] F1 — the one item · owner · case 1\n"


def with_ledger(project_dir, text, day=TODAY):
    folder = project_dir / "vault" / "raw" / day.isoformat()
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "ledger.md").write_text(text, encoding="utf-8", newline="\n")


HI_FOLDER = "1501"  # the `hi` at 15:01:30 names the session's folder (case 73)


def with_frontier(project_dir, text, day=TODAY, hhmm=HI_FOLDER):
    folder = project_dir / "vault" / "raw" / day.isoformat() / hhmm
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "frontier.md").write_text(text, encoding="utf-8", newline="\n")


def with_rule(project_dir, slug, governs, enforcement=None):
    folder = project_dir / "vault" / "wiki" / "rules"
    folder.mkdir(parents=True, exist_ok=True)
    text = f"---\ntype: rule\nstatus: built\ngoverns: {governs}\n"
    if enforcement is not None:
        text += f"enforcement: {enforcement}\n"
    text += "---\n\n## Purpose\n\nx\n"
    (folder / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")


def with_page(project_dir, category, slug, kind="Leaf", estimates=("estimate-x",)):
    folder = project_dir / "vault" / "wiki" / category
    folder.mkdir(parents=True, exist_ok=True)
    text = f"---\ntype: {category[:-1] if category != 'entities' else 'entity'}\n"
    text += f"kind: {kind}\nstatus: built\n"
    text += "estimates: [" + ", ".join(estimates) + "]\n---\n\n## Purpose\n\nx\n"
    (folder / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")


def with_estimate(project_dir, slug="estimate-x"):
    folder = project_dir / "vault" / "wiki" / "estimates"
    folder.mkdir(parents=True, exist_ok=True)
    text = (
        "---\ntype: estimate\nkind: QA\nstatus: passed\ntarget: rule-x\n---\n\n## Criterion\n\nc\n"
    )
    (folder / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")


SETTINGS = 'documentation_lang = "en"\nchat_lang = "ru"\n'


def with_settings(project_dir, settings=SETTINGS):
    (project_dir / "guppi.toml").write_text(settings, encoding="utf-8", newline="\n")


def check(
    project_dir,
    plan=PLAN,
    ledger=LINE,
    frontier=CLEAN_FRONTIER,
    event_log=START + HI,
    settings=SETTINGS,
):
    with_event_log(project_dir, event_log)
    with_ledger(project_dir, ledger)
    if frontier is not None:
        with_frontier(project_dir, frontier)
    if settings is not None:
        with_settings(project_dir, settings)
    plan_file = project_dir / "plan.md"
    plan_file.write_text(plan, encoding="utf-8", newline="\n")
    out, err = io.StringIO(), io.StringIO()
    code = prespec.run(
        ["--check", str(plan_file), "--session", SESSION],
        stdout=out,
        stderr=err,
        project_dir=project_dir,
        now=NOW,
    )
    return code, out.getvalue(), err.getvalue()


def test_a_line_with_its_item_passes(tmp_path):
    assert check(tmp_path) == (0, "", "")


def test_a_line_before_hi_is_not_this_sessions(tmp_path):
    code, out, _ = check(tmp_path, ledger=BEFORE_HI + LINE)
    assert code == 0 and out == ""


def test_a_line_without_an_item_is_a_finding(tmp_path):
    extra = "- 16:00:01 decision[case 1][update][rule-y]{ref:rule-y}\n"
    code, out, _ = check(tmp_path, ledger=LINE + extra)
    assert code == 1
    assert out.splitlines() == ["case 1: line [update][rule-y] has no item in the plan"]


def test_an_item_without_a_line_is_a_finding(tmp_path):
    plan = PLAN.replace("    change: one line\n", "    change: one line\n  - slug: rule-y\n")
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out.splitlines() == ["case 1: item [update][rule-y] has no decision line"]


def test_an_item_under_another_sub_case_is_a_finding_each_way(tmp_path):
    # the then and tasks blocks now sit under 1.1: the line of 1 has no item, the item of
    # 1.1 no line, and Case 1 no tasks block
    plan = PLAN.replace("## Case 1 — one", "## Case 1 — one\n\n### Case 1.1 — sub")
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out.splitlines() == [
        "case 1: line [update][rule-x] has no item in the plan",
        "case 1.1: item [update][rule-x] has no decision line",
        "case 1: decision lines and no tasks block",
    ]


SECOND_ITEM = "  - slug: rule-x\n    rename: rule-y\n"
TWICE = "case 1: item [update][rule-x] stands twice — one entry per target"


def test_a_second_item_of_one_slug_in_one_fence_is_a_finding(tmp_path):  # case 426
    plan = PLAN.replace("    change: one line\n", "    change: one line\n" + SECOND_ITEM)
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out.splitlines() == [TWICE]


def test_a_second_item_of_one_slug_in_another_fence_is_a_finding(tmp_path):
    plan = PLAN.replace("```tasks", "```then\nupdate:\n" + SECOND_ITEM + "```\n\n```tasks")
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out.splitlines() == [TWICE]


def test_a_create_and_an_update_of_one_slug_are_no_second_item(tmp_path):
    ledger = LINE + "- 16:00:01 decision[case 1][create][rule-x]{ref:rule-root}{tags:harness}\n"
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\ncreate:\n  - slug: rule-x\n    type: rule\n",
    )
    _, out, _ = check(tmp_path, plan=plan, ledger=ledger)
    assert "stands twice" not in out


def test_one_slug_under_two_sub_cases_is_no_second_item(tmp_path):
    lines = (
        "- 16:00:00 decision[case 1.1][update][rule-x]{ref:rule-x}\n"
        "- 16:00:01 decision[case 1.2][update][rule-x]{ref:rule-x}\n"
    )
    sub = PLAN.split("\n", 2)[2]
    plan = (
        "# Plan\n\n## Case 1 — one\n\n> **context:**\n> P.\n\n"
        + sub.replace("## Case 1 — one", "### Case 1.1 — a")
        + "\n"
        + sub.replace("## Case 1 — one", "### Case 1.2 — b")
    )
    _, out, _ = check(tmp_path, plan=plan, ledger=lines)
    assert "stands twice" not in out


def test_a_line_of_a_case_the_plan_lacks_is_a_finding(tmp_path):
    extra = "- 16:00:01 decision[case 2][update][rule-y]{ref:rule-y}\n"
    _, out, _ = check(tmp_path, ledger=LINE + extra)
    assert out.splitlines() == ["case 2: line [update][rule-y]: no Case 2 heading in the plan"]


# --- a Case superseded in its own session leaves the plan (case 299.2) --------------------

SUPERSEDING = "- 16:00:02 decision[case 3][update][rule-x]{ref:rule-x}{supersedes:case 1}\n"
PLAN_3 = PLAN.replace("## Case 1 — one", "## Case 3 — three")


def test_a_superseded_case_still_in_the_plan_is_a_finding(tmp_path):
    # Case 1 stands in the plan, Case 3 supersedes it in the window: one finding for the
    # heading; the line of Case 1 is not reported although its item is gone with the heading
    plan = PLAN_3 + "\n## Case 1 — one\n\n> **context:**\n> Old.\n"
    code, out, _ = check(tmp_path, ledger=LINE + SUPERSEDING, plan=plan)
    assert code == 1
    assert out.splitlines() == ["case 1: superseded by case 3, still in the plan"]


def test_a_line_of_a_superseded_case_needs_no_heading_and_no_item(tmp_path):
    # the frontier line closes with the superseding Case, as the agent closes it (299.1)
    frontier = CLEAN_FRONTIER.replace("case 1", "case 3")
    code, out, _ = check(tmp_path, ledger=LINE + SUPERSEDING, plan=PLAN_3, frontier=frontier)
    assert code == 0 and out == ""


def test_a_superseded_sub_case_leaves_alone_and_its_parent_stays(tmp_path):
    line = "- 16:00:00 decision[case 1.1][update][rule-x]{ref:rule-x}\n"
    superseding = "- 16:00:02 decision[case 1.2][update][rule-x]{ref:rule-x}{supersedes:case 1.1}\n"
    plan = PLAN.replace("## Case 1 — one", "## Case 1 — one\n\n### Case 1.2 — two")
    code, out, _ = check(tmp_path, ledger=line + superseding, plan=plan)
    assert code == 0 and out == ""
    still = plan.replace("### Case 1.2 — two", "### Case 1.1 — one\n\n### Case 1.2 — two")
    code, out, _ = check(tmp_path, ledger=line + superseding, plan=still)
    assert out.splitlines() == ["case 1.1: superseded by case 1.2, still in the plan"]


def test_a_supersedes_of_an_earlier_sessions_case_is_no_finding(tmp_path):
    # Case 7 was ratified in another session: no heading in this plan, no line of it here
    taken_up = "- 16:00:00 decision[case 1][update][rule-x]{ref:rule-x}{supersedes:case 7}\n"
    code, out, _ = check(tmp_path, ledger=taken_up)
    assert code == 0 and out == ""


TWO_LINES = LINE + "- 16:00:01 decision[case 2][update][rule-x]{ref:rule-x}\n"
TWO_BLOCKS = "- 16:00:02 decision[case 3][update][rule-x]{ref:rule-x}{supersedes:case 1}{supersedes:case 2}\n"


def test_a_line_with_two_supersedes_blocks_covers_both_cases(tmp_path):  # case 429
    frontier = CLEAN_FRONTIER.replace("case 1", "case 3")
    code, out, _ = check(tmp_path, ledger=TWO_LINES + TWO_BLOCKS, plan=PLAN_3, frontier=frontier)
    assert code == 0 and out == ""  # neither Case needs its item
    old = (
        "\n## Case 1 — one\n\n> **context:**\n> Old.\n\n## Case 2 — two\n\n> **context:**\n> Old.\n"
    )
    _, out, _ = check(tmp_path, ledger=TWO_LINES + TWO_BLOCKS, plan=PLAN_3 + old, frontier=frontier)
    assert out.splitlines() == [
        "case 1: superseded by case 3, still in the plan",
        "case 2: superseded by case 3, still in the plan",
    ]


def test_a_defer_line_matches_a_defer_item(tmp_path):
    ledger = LINE + "- 16:00:01 decision[case 1][defer][rule-later]\n"
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\ndefer:\n  - slug: rule-later\n    type: rule\n    purpose: p\n",
    )
    assert check(tmp_path, plan=plan, ledger=ledger) == (0, "", "")
    _, out, _ = check(tmp_path, ledger=ledger)
    assert out.splitlines() == ["case 1: line [defer][rule-later] has no item in the plan"]


def test_a_file_item_is_a_finding_the_route_is_gone(tmp_path):
    # case 320: no file of the vault changes by hand, so an `update` with `file` has no route
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\n  - file: vault/wiki/index.md\n    change: a row\n",
    )
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert "case 1: file vault/wiki/index.md; the file route is gone (case 320)" in out.splitlines()


def test_a_nested_estimate_is_covered_by_its_parents_create_line(tmp_path):
    # a Leaf's Estimate has no line of its own (case 72.5): the parent's line covers the
    # nested estimate of an older Spec; a line for the nested slug, if someone writes one,
    # still finds it
    parent = "- 16:00:00 decision[case 1][create][rule-z]{ref:rule-root}{tags:a}\n"
    paired = "- 16:00:00 decision[case 1][create][estimate-z-works]{ref:rule-z}{tags:a}\n"
    plan = PLAN.replace(
        "update:\n  - slug: rule-x\n    change: one line\n",
        "create:\n  - slug: rule-z\n    type: rule\n    estimate:\n      slug: estimate-z-works\n",
    ).replace("- [ ] guppi/x.py: the change", "- [ ] read `estimate-z-works`")
    assert check(tmp_path, plan=plan, ledger=parent) == (0, "", "")
    assert check(tmp_path, plan=plan, ledger=parent + paired) == (0, "", "")


def test_a_standalone_estimate_create_needs_its_own_line(tmp_path):
    plan = PLAN.replace(
        "update:\n  - slug: rule-x\n    change: one line\n",
        "create:\n  - slug: estimate-alone\n    type: estimate\n    ref: rule-x\n"
        "    method: pytest tests/test_x.py\n",
    ).replace("- [ ] guppi/x.py: the change", "- [ ] read `estimate-alone`")
    with_page(tmp_path, "rules", "rule-x")
    _, out, _ = check(tmp_path, plan=plan, ledger="")
    assert out.splitlines() == ["case 1: item [create][estimate-alone] has no decision line"]


def test_a_bare_case_id_in_a_line_is_read_and_reported(tmp_path):
    # the comparison still finds its item (no "has no item" finding); the grammar check
    # of case 75.2 reports the line, once, with its date and number
    code, out, _ = check(tmp_path, ledger=LINE.replace("[case 1]", "[1]"))
    assert code == 1
    assert out.splitlines() == [
        (
            "raw/2026-09-09/ledger.md:1: does not parse: "
            "- 16:00:00 decision[1][update][rule-x]{ref:rule-x}"
        )
    ]


def test_the_same_lines_at_two_ratifications_are_fine(tmp_path):
    later = LINE.replace("16:00:00", "17:00:00")
    assert check(tmp_path, ledger=LINE + later) == (0, "", "")


def test_no_hi_means_no_check(tmp_path):
    code, out, err = check(tmp_path, event_log=START, plan="# nothing\n", frontier=None)
    assert (code, out) == (0, "")
    assert "hi" in err and err.count("\n") == 1


def test_a_missing_frontier_is_a_finding(tmp_path):
    code, out, _ = check(tmp_path, frontier=None)
    assert code == 1
    assert out.splitlines() == ["frontier: vault/raw/2026-09-09/1501/frontier.md is missing"]


def test_the_frontier_path_follows_the_hi_time(tmp_path):
    # case 73.4: the frontier of the session's folder, named by the hi's HHMM
    log = "- 11:55:00 44c1aae1 session-start startup\n- 11:56:22 44c1aae1 hi\n"
    code, out, _ = check(tmp_path, frontier=None, event_log=log)
    assert code == 1
    assert out.splitlines() == ["frontier: vault/raw/2026-09-09/1156/frontier.md is missing"]
    with_frontier(tmp_path, CLEAN_FRONTIER, hhmm="1156")
    assert check(tmp_path, frontier=None, event_log=log) == (0, "", "")


def test_an_open_frontier_line_is_a_finding(tmp_path):
    frontier = CLEAN_FRONTIER + "- [ ] F2 — still open · brief next 2\n"
    code, out, _ = check(tmp_path, frontier=frontier)
    assert code == 1
    assert out.splitlines() == ["frontier: F2 is open"]


def test_a_frontier_case_without_its_heading_is_a_finding(tmp_path):
    frontier = CLEAN_FRONTIER + "- [x] F2 — elsewhere · owner · case 7\n"
    _, out, _ = check(tmp_path, frontier=frontier)
    assert out.splitlines() == ["frontier: F2 closes with case 7, no Case 7 heading in the plan"]


def test_a_frontier_defer_without_its_item_is_a_finding(tmp_path):
    frontier = CLEAN_FRONTIER + "- [-] F2 — later · owner · defer case 1\n"
    _, out, _ = check(tmp_path, frontier=frontier)
    assert out.splitlines() == ["frontier: F2 defers to case 1, no defer item under Case 1"]
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\ndefer:\n  - slug: rule-later\n    type: rule\n    purpose: p\n",
    )
    ledger = LINE + "- 16:00:01 decision[case 1][defer][rule-later]\n"
    assert check(tmp_path, plan=plan, ledger=ledger, frontier=frontier) == (0, "", "")


# --- the box, the closer and the source (case 451.2) --------------------------------------

# Case 2 defers `rule-later`, so a line `· defer case 2` of another source is clean
DEFER_PLAN = (
    PLAN
    + "\n## Case 2 — later\n\n```then\ndefer:\n  - slug: rule-later\n    type: rule\n    purpose: p\n```\n"
)
DEFER_LEDGER = LINE + "- 16:00:01 decision[case 2][defer][rule-later]\n"


def check_deferring(project_dir, frontier):
    return check(project_dir, plan=DEFER_PLAN, ledger=DEFER_LEDGER, frontier=frontier)


def test_every_closer_on_its_own_box_and_source_is_clean(tmp_path):
    frontier = CLEAN_FRONTIER + (
        "- [x] F2 — no decision · brief · work\n"
        "- [-] F3 — `rule-a`, a theme left for later · sprint · defer\n"
        "- [-] F4 — `rule-b`, as it stands · backlog · kept\n"
        "- [-] F5 — a decision put off · brief · defer case 2\n"
    )
    assert check_deferring(tmp_path, frontier) == (0, "", "")


@pytest.mark.parametrize(
    ("line", "finding"),
    [
        ("- [x] F2 — a theme · sprint · defer", "closes [x] with defer; an item put off is [-]"),
        ("- [x] F2 — `rule-b` · backlog · kept", "closes [x] with kept; an item put off is [-]"),
        (
            "- [x] F2 — a decision · brief · defer case 2",
            "closes [x] with defer case 2; an item put off is [-]",
        ),
        ("- [-] F2 — a decision · owner · case 1", "closes [-] with case 1; an item ended is [x]"),
        ("- [-] F2 — no decision · brief · work", "closes [-] with work; an item ended is [x]"),
    ],
)
def test_a_box_that_disagrees_with_its_closer_is_a_finding(tmp_path, line, finding):
    code, out, _ = check_deferring(tmp_path, CLEAN_FRONTIER + line + "\n")
    assert code == 1
    assert out.splitlines() == [f"frontier: F2 {finding}"]


@pytest.mark.parametrize("source", ["backlog", "brief", "owner", "deferred"])
def test_defer_after_a_source_other_than_sprint_is_a_finding(tmp_path, source):
    frontier = CLEAN_FRONTIER + f"- [-] F2 — a theme · {source} · defer\n"
    code, out, _ = check(tmp_path, frontier=frontier)
    assert code == 1
    assert out.splitlines() == [
        "frontier: F2 closes with defer; only an item of the source sprint closes with defer"
    ]


def test_a_sprint_item_put_off_closes_with_defer(tmp_path):
    frontier = CLEAN_FRONTIER + "- [-] F2 — a theme · sprint · defer\n"
    assert check(tmp_path, frontier=frontier) == (0, "", "")


@pytest.mark.parametrize("source", ["sprint", "brief", "owner", "deferred"])
def test_kept_after_a_source_other_than_backlog_is_a_finding(tmp_path, source):
    frontier = CLEAN_FRONTIER + f"- [-] F2 — `rule-later` · {source} · kept\n"
    code, out, _ = check(tmp_path, frontier=frontier)
    assert code == 1
    assert out.splitlines() == [
        "frontier: F2 closes with kept; only an item of the source backlog closes with kept"
    ]


def test_a_backlog_item_left_as_it_stands_closes_with_kept(tmp_path):
    frontier = CLEAN_FRONTIER + "- [-] F2 — `rule-later`, as it stands · backlog · kept\n"
    assert check(tmp_path, frontier=frontier) == (0, "", "")


def test_a_box_finding_and_a_source_finding_are_both_given(tmp_path):
    frontier = CLEAN_FRONTIER + "- [x] F2 — `rule-later` · brief · kept\n"
    code, out, _ = check(tmp_path, frontier=frontier)
    assert code == 1
    assert out.splitlines() == [
        "frontier: F2 closes [x] with kept; an item put off is [-]",
        "frontier: F2 closes with kept; only an item of the source backlog closes with kept",
    ]


@pytest.mark.parametrize(("source", "closer"), [("sprint", "defer"), ("backlog", "kept")])
def test_defer_case_n_after_sprint_or_backlog_is_a_finding(tmp_path, source, closer):
    # the defer item under Case 2 stands: a sprint or backlog item is not deferred by a Case
    frontier = CLEAN_FRONTIER + f"- [-] F2 — `rule-later` · {source} · defer case 2\n"
    code, out, _ = check_deferring(tmp_path, frontier)
    assert code == 1
    finding = (
        f"frontier: F2 defers a {source} item by a Case; a {source} item put off "
        f"closes [-] with {closer}"
    )
    assert out.splitlines() == [finding]


@pytest.mark.parametrize("source", ["brief", "owner", "deferred", "ledger tail"])
def test_defer_case_n_after_another_source_needs_its_defer_item(tmp_path, source):
    frontier = CLEAN_FRONTIER + f"- [-] F2 — a decision put off · {source} · defer case 2\n"
    assert check_deferring(tmp_path, frontier) == (0, "", "")
    code, out, _ = check(tmp_path, plan=PLAN + "\n## Case 2 — later\n", frontier=frontier)
    assert code == 1
    assert out.splitlines() == ["frontier: F2 defers to case 2, no defer item under Case 2"]


@pytest.mark.parametrize("closer", ["sprint", "deferred", "put off", "case", "defer case"])
def test_a_closer_outside_the_five_is_a_finding(tmp_path, closer):
    # the old closer `sprint` is gone (case 451.2)
    frontier = CLEAN_FRONTIER + f"- [-] F2 — a theme · brief · {closer}\n"
    code, out, _ = check(tmp_path, frontier=frontier)
    assert code == 1
    assert out.splitlines() == [
        "frontier: F2 is closed without case N, work, defer, kept or defer case N"
    ]


def test_the_backlog_count_and_a_near_line_are_not_read(tmp_path):
    frontier = (
        "# Frontier\n\n## Cases\n\n- [x] C1 — the one item · brief · case 1\n"
        "  - near `rule-later` · sprint · kept\n"
        "  - [ ] near `rule-other`\n"
        "Backlog: 12 items · defer case 9\n\n"
        "## Work\n\n- [x] W1 — a reading · brief · work\n"
    )
    assert check(tmp_path, frontier=frontier) == (0, "", "")


# --- Case 467.1: a backlog item decided on its page ---------------------------------------


def with_deferred(project_dir, slug, deferred_by=("decision-case-7",)):
    folder = project_dir / "vault" / "wiki" / "rules"
    folder.mkdir(parents=True, exist_ok=True)
    text = "---\ntype: rule\nstatus: draft\n"
    if deferred_by:
        text += "deferred_by: [" + ", ".join(deferred_by) + "]\n"
    (folder / f"{slug}.md").write_text(text + "---\n\n## Purpose\n\nx\n", encoding="utf-8")


BACKLOG_LINE = CLEAN_FRONTIER + "- [x] F2 — `{slug}`, taken up · {source} · case 1\n"
SUPERSEDING_LINE = "- 16:00:00 decision[case 1][update][rule-x]{ref:rule-x}{supersedes:case 7}\n"


def test_backlog_a_page_its_case_supersedes_on_its_own_line_passes(tmp_path):
    with_deferred(tmp_path, "rule-x")
    frontier = BACKLOG_LINE.format(slug="rule-x", source="backlog")
    assert check(tmp_path, ledger=SUPERSEDING_LINE, frontier=frontier) == (0, "", "")


def test_backlog_a_page_named_by_no_line_of_its_case_is_a_finding(tmp_path):
    with_deferred(tmp_path, "rule-y")
    frontier = BACKLOG_LINE.format(slug="rule-y", source="backlog")
    code, out, _ = check(tmp_path, ledger=SUPERSEDING_LINE, frontier=frontier)
    assert code == 1
    assert out.splitlines() == [
        (
            "frontier: F2 closes a backlog item with case 1, and no decision line of Case 1 "
            "other than a defer names rule-y; generate clears a defer only from a page the "
            "Case names"
        ),
        (
            "frontier: F2: no Case among case 1 and its sub-cases names rule-y and carries "
            "{supersedes:case 7}"
        ),
    ]


def test_backlog_a_page_named_without_its_supersedes_is_a_finding(tmp_path):
    with_deferred(tmp_path, "rule-x", ("decision-case-7", "decision-case-8"))
    frontier = BACKLOG_LINE.format(slug="rule-x", source="backlog")
    code, out, _ = check(tmp_path, ledger=SUPERSEDING_LINE, frontier=frontier)
    assert code == 1
    assert out.splitlines() == [
        (
            "frontier: F2: no Case among case 1 and its sub-cases names rule-x and carries "
            "{supersedes:case 8}"
        )
    ]


SUB_CASE_PLAN = """# Plan

## Case 1 — one

> **context:**
> Something.

### Case 1.1 — takes it up

```then
update:
  - slug: rule-x
    change: taken up
```

```tasks
- [ ] guppi/x.py: the change
```

### Case 1.2 — another change of the page

```then
update:
  - slug: rule-x
    change: another
```

```tasks
- [ ] guppi/y.py: the change
```
"""
SUB_CASE_LINES = (
    "- 16:00:00 decision[case 1.1][update][rule-x]{ref:rule-x}{supersedes:case 7}\n"
    "- 16:00:01 decision[case 1.2][update][rule-x]{ref:rule-x}\n"
)


def test_backlog_a_sub_case_that_names_and_supersedes_covers_its_sibling(tmp_path):
    with_deferred(tmp_path, "rule-x")
    frontier = "# Frontier\n\n- [x] F2 — `rule-x`, taken up · backlog · case 1\n"
    code, out, _ = check(tmp_path, plan=SUB_CASE_PLAN, ledger=SUB_CASE_LINES, frontier=frontier)
    assert (code, out) == (0, "")


@pytest.mark.parametrize(
    ("slug", "deferred_by", "source"),
    [("rule-x", (), "backlog"), ("rule-x", ("decision-case-7",), "brief")],
)
def test_backlog_a_page_without_defers_or_a_line_of_another_source_is_no_finding(
    tmp_path, slug, deferred_by, source
):
    with_deferred(tmp_path, slug, deferred_by)
    frontier = BACKLOG_LINE.format(slug=slug, source=source)
    assert check(tmp_path, frontier=frontier) == (0, "", "")


def test_a_clean_frontier_passes(tmp_path):
    frontier = CLEAN_FRONTIER + "- [x] F2 — no decision · brief next 1 · work\n"
    assert check(tmp_path, frontier=frontier) == (0, "", "")


def test_a_case_with_lines_and_no_tasks_block_is_a_finding(tmp_path):
    plan = PLAN.split("```tasks")[0]
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out.splitlines() == ["case 1: decision lines and no tasks block"]


def test_an_estimate_without_its_task_line_is_a_finding(tmp_path):
    ledger = LINE + "- 16:00:01 decision[case 1][update][estimate-x-holds]{ref:estimate-x-holds}\n"
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\n  - slug: estimate-x-holds\n    set: {status: pending}\n",
    )
    with_estimate(tmp_path, "estimate-x-holds")
    code, out, _ = check(tmp_path, plan=plan, ledger=ledger)
    assert code == 1
    assert out.splitlines() == ["case 1: estimate-x-holds has no task line"]
    passing = plan.replace("- [ ] guppi/x.py: the change", "- [ ] read `estimate-x-holds`")
    assert check(tmp_path, plan=passing, ledger=ledger) == (0, "", "")


def test_an_estimate_named_on_another_read_line_has_no_line_of_its_own(tmp_path):
    # case 327: `generate` ticks by the first backticked slug of a read line, so a line
    # naming three Estimates closes the box of the first and says nothing of the rest; one
    # promise per sub-case (case 472.3), the read line of 1.2 naming both
    ledger = (
        LINE
        + "- 16:00:01 decision[case 1.1][update][estimate-x-holds]{ref:estimate-x-holds}\n"
        + "- 16:00:02 decision[case 1.2][update][estimate-x-stands]{ref:estimate-x-stands}\n"
    )

    def sub(case, slug, read):
        return (
            f"\n### Case {case} — {slug}\n\n```then\nupdate:\n  - slug: {slug}\n"
            "    set: {status: pending}\n    sections:\n      Criterion: |\n        Then:\n"
            f"        c\n```\n\n```tasks\n- [ ] {read}\n```\n"
        )

    plan = (
        PLAN
        + sub("1.1", "estimate-x-holds", "read `estimate-x-holds`")
        + sub("1.2", "estimate-x-stands", "read `estimate-x-holds` and `estimate-x-stands`")
    )
    with_estimate(tmp_path, "estimate-x-holds")
    with_estimate(tmp_path, "estimate-x-stands")
    code, out, _ = check(tmp_path, plan=plan, ledger=ledger)
    assert code == 1
    assert out.splitlines() == [
        "case 1.2: estimate-x-stands is named on another read line, not its own"
    ]
    # one line per reading, and both are clean
    apart = plan.replace(
        "- [ ] read `estimate-x-holds` and `estimate-x-stands`", "- [ ] read `estimate-x-stands`"
    )
    assert check(tmp_path, plan=apart, ledger=ledger) == (0, "", "")


def test_an_estimate_named_by_an_update_line_alone_has_no_task_line(tmp_path):
    # case 327: a mention on a line that is not a read line is no task line
    ledger = LINE + "- 16:00:01 decision[case 1][update][estimate-x-holds]{ref:estimate-x-holds}\n"
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\n  - slug: estimate-x-holds\n    set: {status: pending}\n",
    ).replace("- [ ] guppi/x.py: the change", "- [ ] update `estimate-x-holds` — the Criterion")
    with_estimate(tmp_path, "estimate-x-holds")
    code, out, _ = check(tmp_path, plan=plan, ledger=ledger)
    assert code == 1
    assert out.splitlines() == ["case 1: estimate-x-holds has no task line"]


def test_a_renamed_estimate_is_read_under_the_slug_of_its_rename(tmp_path):  # case 432
    ledger = LINE + "- 16:00:01 decision[case 1][update][estimate-x-holds]{ref:estimate-x-holds}\n"
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\n  - slug: estimate-x-holds\n    rename: estimate-x-stands\n"
        "    set: {status: pending}\n",
    )
    with_estimate(tmp_path, "estimate-x-holds")
    new = plan.replace("- [ ] guppi/x.py: the change", "- [ ] read `estimate-x-stands`")
    assert check(tmp_path, plan=new, ledger=ledger) == (0, "", "")
    old = plan.replace("- [ ] guppi/x.py: the change", "- [ ] read `estimate-x-holds`")
    code, out, _ = check(tmp_path, plan=old, ledger=ledger)
    assert code == 1
    assert out.splitlines() == ["case 1: estimate-x-stands has no task line"]


def test_a_created_estimate_without_its_task_line_is_a_finding(tmp_path):
    ledger = "- 16:00:00 decision[case 1][create][estimate-fresh]{ref:rule-x}{tags:a}\n"
    plan = PLAN.replace(
        "update:\n  - slug: rule-x\n    change: one line\n",
        "create:\n  - slug: estimate-fresh\n    type: estimate\n    ref: rule-x\n"
        "    method: pytest tests/test_x.py\n",
    )
    with_page(tmp_path, "rules", "rule-x")
    _, out, _ = check(tmp_path, plan=plan, ledger=ledger)
    assert out.splitlines() == ["case 1: estimate-fresh has no task line"]


def test_a_file_item_on_a_governed_path_is_a_finding(tmp_path):
    with_rule(tmp_path, "rule-skill-hi", ".claude/skills/hi/SKILL.md")
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\n  - file: .claude/skills/hi/SKILL.md\n    change: by hand\n",
    )
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert (
        "case 1: file .claude/skills/hi/SKILL.md, governed by rule-skill-hi; "
        "the file route is gone (case 320)" in out.splitlines()
    )


def test_check_without_a_plan_file_says_so(tmp_path):
    with_event_log(tmp_path, START + HI)
    err = io.StringIO()
    code = prespec.run(
        ["--check", str(tmp_path / "none.md"), "--session", SESSION],
        stdout=io.StringIO(),
        stderr=err,
        project_dir=tmp_path,
        now=NOW,
    )
    assert code == 2 and "none.md" in err.getvalue()


def test_a_defer_only_case_needs_no_tasks_block(tmp_path):
    plan = (
        PLAN
        + "\n## Case 2 — later\n\n```then\ndefer:\n  - slug: rule-later\n    type: rule\n    purpose: p\n```\n"
    )
    ledger = LINE + "- 16:00:01 decision[case 2][defer][rule-later]\n"
    frontier = CLEAN_FRONTIER + "- [-] F2 — later · brief deferred 1 · defer case 2\n"
    assert check(tmp_path, plan=plan, ledger=ledger, frontier=frontier) == (0, "", "")


def test_a_case_mixing_a_defer_with_an_update_needs_a_tasks_block(tmp_path):
    # case 74: a Case with a line of a kind other than defer and no tasks block is a finding
    plan = PLAN.split("```tasks")[0].replace(
        "    change: one line\n",
        "    change: one line\ndefer:\n  - slug: rule-later\n    type: rule\n    purpose: p\n",
    )
    ledger = LINE + "- 16:00:01 decision[case 1][defer][rule-later]\n"
    code, out, _ = check(tmp_path, plan=plan, ledger=ledger)
    assert code == 1
    assert out.splitlines() == ["case 1: decision lines and no tasks block"]


# --- the form of an Estimate item (case 203.1) ------------------------------------------

ESTIMATE_CREATE = (
    "create:\n  - slug: estimate-x-again\n    type: estimate\n    ref: rule-x\n"
    "    kind: QA\n    purpose: p\n    method: pytest tests/test_x.py\n    tags: [a]\n"
)
CREATE_LINE = "- 16:00:00 decision[case 1][create][estimate-x-again]{ref:rule-x}{tags:a}\n"
ESTIMATE_UPDATE = "  - slug: estimate-x\n    set: {status: pending}\n    change: recut\n"
UPDATE_LINE = "- 16:00:01 decision[case 1][update][estimate-x]{ref:estimate-x}\n"
WRITTEN = (
    "    sections:\n      Criterion: |\n        When:\n        w.\n\n        Then:\n        t.\n"
)
TASKS = (
    "```tasks\n- [ ] guppi/x.py: the change\n"
    "- [ ] read `estimate-x`\n- [ ] read `estimate-x-again`\n```"
)


def create_plan(item=ESTIMATE_CREATE):
    plan = PLAN.replace("update:\n  - slug: rule-x\n    change: one line\n", item)
    return plan.replace("```tasks\n- [ ] guppi/x.py: the change\n```", TASKS)


def test_an_estimate_create_whose_ref_names_no_live_page_is_a_finding(tmp_path):
    code, out, _ = check(tmp_path, plan=create_plan(), ledger=CREATE_LINE)
    assert code == 1
    assert out.splitlines() == ["case 1: create estimate-x-again: ref rule-x names no live page"]
    with_page(tmp_path, "rules", "rule-x")
    assert check(tmp_path, plan=create_plan(), ledger=CREATE_LINE) == (0, "", "")


def test_an_update_of_an_estimate_without_a_page_is_a_finding(tmp_path):
    plan = create_plan("update:\n" + ESTIMATE_UPDATE)
    code, out, _ = check(tmp_path, plan=plan, ledger=UPDATE_LINE)
    assert code == 1
    assert out.splitlines() == ["case 1: update estimate-x: no such Estimate page"]
    with_estimate(tmp_path)
    assert check(tmp_path, plan=plan, ledger=UPDATE_LINE) == (0, "", "")


def test_two_estimate_items_with_the_cases_criterion_is_a_finding(tmp_path):
    with_page(tmp_path, "rules", "rule-x")
    with_estimate(tmp_path)
    plan = create_plan(ESTIMATE_CREATE + "update:\n" + ESTIMATE_UPDATE)
    code, out, _ = check(tmp_path, plan=plan, ledger=CREATE_LINE + UPDATE_LINE)
    assert code == 1
    assert out.splitlines() == ["case 1: two promises in one Case — split it"]
    # a written Criterion is a promise too, on one item or on both (case 472.3)
    one_written = create_plan(ESTIMATE_CREATE + WRITTEN + "update:\n" + ESTIMATE_UPDATE)
    both_written = create_plan(ESTIMATE_CREATE + WRITTEN + "update:\n" + ESTIMATE_UPDATE + WRITTEN)
    # an update that names no part replaces the Criterion whole, by `names_a_part`: `change`
    # alone, or a status other than pending
    change_alone = create_plan(
        ESTIMATE_CREATE + "update:\n  - slug: estimate-x\n    change: recut\n"
    )
    passed = create_plan(
        ESTIMATE_CREATE + "update:\n" + ESTIMATE_UPDATE.replace("pending", "passed")
    )
    for counted in (one_written, both_written, change_alone, passed):
        code, out, _ = check(tmp_path, plan=counted, ledger=CREATE_LINE + UPDATE_LINE)
        findings = [line for line in out.splitlines() if not line.startswith("note:")]
        assert (code, findings) == (1, ["case 1: two promises in one Case — split it"])
    # an update that names a part alone changes that part, and is no promise
    a_part = create_plan(
        ESTIMATE_CREATE + "update:\n  - slug: estimate-x\n    set: {purpose: p2}\n"
        "    change: purpose\n"
    )
    assert check(tmp_path, plan=a_part, ledger=CREATE_LINE + UPDATE_LINE) == (0, "", "")
    # a sub-case is its own Case: one promise each is fine
    split = plan.replace(
        "update:\n" + ESTIMATE_UPDATE,
        "```\n\n" + TASKS + "\n\n### Case 1.1 — sub\n\n```then\nupdate:\n" + ESTIMATE_UPDATE,
    )
    ledger = CREATE_LINE + UPDATE_LINE.replace("[case 1]", "[case 1.1]")
    assert check(tmp_path, plan=split, ledger=ledger) == (0, "", "")


# --- the form of `method` in the plan (case 331) -----------------------------------------

NO_FORM_CREATE = (
    "create:\n  - slug: estimate-x-again\n    type: estimate\n    ref: rule-x\n"
    "    kind: QA\n    purpose: p\n    method: Run it and look\n    tags: [a]\n"
)
NO_METHOD_CREATE = (
    "create:\n  - slug: estimate-x-again\n    type: estimate\n    ref: rule-x\n"
    "    kind: QA\n    purpose: p\n    tags: [a]\n"
)
NO_FORM = (
    "case 1: create estimate-x-again: method names no form — "
    'a make target, pytest, a tests/ file or "by hand"'
)


def test_an_estimate_create_whose_method_names_no_form_is_a_finding(tmp_path):
    # case 331: the four forms lint classifies, judged in the plan by lint's own predicate
    with_page(tmp_path, "rules", "rule-x")
    code, out, _ = check(tmp_path, plan=create_plan(NO_FORM_CREATE), ledger=CREATE_LINE)
    assert code == 1
    assert out.splitlines() == [NO_FORM]


def test_an_estimate_create_without_a_method_is_the_same_finding(tmp_path):
    with_page(tmp_path, "rules", "rule-x")
    code, out, _ = check(tmp_path, plan=create_plan(NO_METHOD_CREATE), ledger=CREATE_LINE)
    assert code == 1
    assert out.splitlines() == [NO_FORM]


def test_each_of_the_four_forms_is_clean_in_the_plan(tmp_path):
    with_page(tmp_path, "rules", "rule-x")
    for method in (
        "make test-x, the pipeline",
        "pytest over the suite",
        "tests/test_x.py, one case per defect",
        "read by hand at the first /hi",
    ):
        item = NO_FORM_CREATE.replace("Run it and look", method)
        assert check(tmp_path, plan=create_plan(item), ledger=CREATE_LINE) == (0, "", ""), method


def test_an_estimate_update_setting_a_method_without_a_form_is_a_finding(tmp_path):
    with_page(tmp_path, "rules", "rule-x")
    with_estimate(tmp_path)
    item = "update:\n  - slug: estimate-x\n    set: {method: Run it and look}\n    change: recut\n"
    code, out, _ = check(tmp_path, plan=create_plan(item), ledger=UPDATE_LINE)
    assert code == 1
    assert out.splitlines() == [NO_FORM.replace("create estimate-x-again", "update estimate-x")]


def test_the_keys_of_the_old_shape_are_a_finding_on_every_kind(tmp_path):
    # case 440: `contract` on an `update` and `estimate_slug` on a rule's `create` are keys of
    # no item, judged by `item_keys` like any other
    with_page(tmp_path, "rules", "rule-x", kind="Leaf")
    plan = PLAN.replace("    change: one line\n", "    change: one line\n    contract: changed\n")
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out == "case 1: update rule-x: key contract is not a key of this item\n"
    schema = tmp_path / "vault" / "wiki" / "rules" / "schema.yaml"
    schema.write_text("properties:\n  required: [type, kind, purpose]\n", encoding="utf-8")
    leaf = PLAN.replace(
        "update:\n  - slug: rule-x\n    change: one line\n",
        "create:\n  - slug: rule-z\n    type: rule\n    kind: Leaf\n    estimate_slug: e\n",
    )
    line = "- 16:00:00 decision[case 1][create][rule-z]{ref:rule-root}{tags:a}\n"
    code, out, _ = check(tmp_path, plan=leaf, ledger=line)
    assert code == 1
    assert out == "case 1: create rule-z: key estimate_slug is not a key of this item\n"


def test_a_key_the_item_does_not_have_is_a_finding(tmp_path):
    # 436.2: `replace old` under an `update`, `old` under a `delete`; `slug`, `replace` and
    # `change` are keys of an `update`
    with_page(tmp_path, "rules", "rule-x", kind="Leaf")
    plan = PLAN.replace("    change: one line\n", "    change: one line\n    replace old: a\n")
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out == "case 1: update rule-x: key replace old is not a key of this item\n"
    fine = PLAN.replace(
        "    change: one line\n",
        "    change: one line\n    replace:\n      - old: a\n        new: b\n",
    )
    assert "is not a key" not in check(tmp_path, plan=fine)[1]
    gone = PLAN.replace(
        "update:\n  - slug: rule-x\n    change: one line\n",
        "delete:\n  - slug: rule-x\n    impact: none\n    old: a\n",
    )
    line = "- 16:00:00 decision[case 1][delete][rule-x]{ref:rule-x}\n"
    assert (
        "case 1: delete rule-x: key old is not a key of this item"
        in check(tmp_path, plan=gone, ledger=line)[1]
    )


def test_a_defer_item_is_outside_the_form_checks(tmp_path):
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\ndefer:\n  - slug: rule-later\n    type: rule\n    purpose: p\n",
    )
    ledger = LINE + "- 16:00:02 decision[case 1][defer][rule-later]\n"
    assert check(tmp_path, plan=plan, ledger=ledger) == (0, "", "")


# --- the session's ledger (case 103.4) ---------------------------------------------------


def with_session_ledger(project_dir, text, day=TODAY, hhmm=HI_FOLDER):
    folder = project_dir / "vault" / "raw" / day.isoformat() / hhmm
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "ledger.md").write_text(text, encoding="utf-8", newline="\n")


def test_the_lines_of_the_session_ledger_are_in_the_window(tmp_path):
    # the date-level ledger holds nothing; the session's own ledger holds the line
    with_session_ledger(tmp_path, LINE)
    assert check(tmp_path, ledger="") == (0, "", "")
    # a line the plan does not hold, in the session ledger, is found there
    with_session_ledger(
        tmp_path, LINE + "- 16:00:01 decision[case 2][update][rule-y]{ref:rule-y}\n"
    )
    code, out, _ = check(tmp_path, ledger="")
    assert code == 1 and "case 2" in out


def test_a_session_ledger_line_before_the_hi_time_still_counts(tmp_path):
    # the session ledger is the session's whole: its lines are not filtered by the hi time
    with_session_ledger(tmp_path, "- 15:00:00 " + LINE[11:])
    assert check(tmp_path, ledger="") == (0, "", "")


def test_a_grammar_finding_names_the_session_ledger(tmp_path):
    with_session_ledger(tmp_path, LINE + "- 16:00:02 estimate[estimate-x-holds] no outcome\n")
    code, out, _ = check(tmp_path, ledger="")
    assert code == 1
    assert out.splitlines() == [
        (
            f"raw/2026-09-09/{HI_FOLDER}/ledger.md:2: does not parse: "
            "- 16:00:02 estimate[estimate-x-holds] no outcome"
        )
    ]


# --- the grammar of the window's record lines (case 75.2) -------------------------------


def test_a_record_line_that_does_not_parse_is_a_finding_with_its_date_and_number(tmp_path):
    bad_estimate = "- 16:00:02 estimate[estimate-x-holds] no outcome given\n"
    bad_lesson = "- 16:00:03 lesson[lesson-no-kind] trigger: t root_cause: r\n"
    code, out, _ = check(tmp_path, ledger=LINE + bad_estimate + bad_lesson)
    assert code == 1
    assert out.splitlines() == [
        (
            "raw/2026-09-09/ledger.md:2: does not parse: "
            "- 16:00:02 estimate[estimate-x-holds] no outcome given"
        ),
        (
            "raw/2026-09-09/ledger.md:3: does not parse: "
            "- 16:00:03 lesson[lesson-no-kind] trigger: t root_cause: r"
        ),
    ]


def test_a_long_unparsed_line_is_cut_to_eighty_characters(tmp_path):
    long = "- 16:00:02 decision[1][update][rule-x]{ref:" + "x" * 100 + "}\n"
    _, out, _ = check(tmp_path, ledger=LINE + long)
    finding = out.splitlines()[0]
    assert finding.startswith("raw/2026-09-09/ledger.md:2: does not parse: ")
    assert len(finding.split("does not parse: ", 1)[1]) == 80


def test_a_line_before_the_hi_and_a_non_record_line_are_not_checked(tmp_path):
    # a preview is never in the ledger; what is there and is not a record line — a heading,
    # prose — is not a record and is not checked; a record before the hi is not read
    before = "- 15:01:00 decision[1][update][rule-x]{ref:rule-x}\n"
    prose = "# Ledger\n\nthe line decision[1] shown as a preview\n"
    assert check(tmp_path, ledger=prose + before + LINE) == (0, "", "")


def test_a_parsed_line_of_a_later_date_of_the_window_is_read(tmp_path):
    with_ledger(
        tmp_path, "- 00:10:00 decision[2][update][rule-y]{ref:rule-y}\n", day=date(2026, 9, 9)
    )
    log = "- 15:01:00 44c1aae1 session-start startup\n- 15:01:30 44c1aae1 hi\n"
    with_event_log(tmp_path, log, day=date(2026, 9, 8))
    with_ledger(tmp_path, LINE.replace("16:00:00", "23:00:00"), day=date(2026, 9, 8))
    with_frontier(tmp_path, CLEAN_FRONTIER, day=date(2026, 9, 8))
    with_settings(tmp_path)
    plan_file = tmp_path / "plan.md"
    plan_file.write_text(PLAN, encoding="utf-8", newline="\n")
    out = io.StringIO()
    code = prespec.run(
        ["--check", str(plan_file), "--session", SESSION],
        stdout=out,
        stderr=io.StringIO(),
        project_dir=tmp_path,
        now=NOW,
    )
    assert code == 1
    assert out.getvalue().splitlines() == [
        (
            "raw/2026-09-09/ledger.md:1: does not parse: "
            "- 00:10:00 decision[2][update][rule-y]{ref:rule-y}"
        ),
        "case 2: line [update][rule-y]: no Case 2 heading in the plan",
    ]


# --- the session bound by its stamp, not by position (case 213) --------------------------

YESTERDAY = date(2026, 9, 8)


def test_check_without_a_stamp_refuses_and_names_the_hi_line(tmp_path, monkeypatch):
    """Case 213.1: no `--session`, no `CLAUDE_SESSION_ID` — one line on stderr, exit 2,
    nothing checked; the last `session-start` of today's log is not a fallback."""
    monkeypatch.delenv("CLAUDE_SESSION_ID", raising=False)
    with_event_log(tmp_path, START + HI)
    with_ledger(tmp_path, LINE)
    plan_file = tmp_path / "plan.md"
    plan_file.write_text(PLAN, encoding="utf-8", newline="\n")
    out, err = io.StringIO(), io.StringIO()
    code = prespec.run(
        ["--check", str(plan_file)], stdout=out, stderr=err, project_dir=tmp_path, now=NOW
    )
    assert code == 2 and out.getvalue() == ""
    assert (
        err.getvalue().strip() == "prespec: no session id; pass --session <stamp> from the hi: line"
    )


def test_check_finds_yesterdays_hi_after_midnight(tmp_path):
    """Case 213.1: the window is the ledger hook's — the stamped `hi` of yesterday's log
    opens it, and the session's ledger of yesterday is read."""
    with_event_log(tmp_path, START + HI, day=YESTERDAY)
    with_event_log(tmp_path, "- 00:05:00 99999999 session-start startup\n")
    with_session_ledger(tmp_path, LINE.replace("16:00:00", "23:50:00"), day=YESTERDAY)
    with_frontier(tmp_path, CLEAN_FRONTIER, day=YESTERDAY)
    with_settings(tmp_path)
    plan_file = tmp_path / "plan.md"
    plan_file.write_text(PLAN, encoding="utf-8", newline="\n")
    out, err = io.StringIO(), io.StringIO()
    code = prespec.run(
        ["--check", str(plan_file), "--session", SESSION],
        stdout=out,
        stderr=err,
        project_dir=tmp_path,
        now=datetime(2026, 9, 9, 0, 30, 0, tzinfo=UTC),
    )
    assert (code, out.getvalue(), err.getvalue()) == (0, "", "")


def test_the_hook_finds_yesterdays_hi_and_prespec_after_midnight(tmp_path):
    """Case 213.2: the hook reads the logs the ledger hook reads — back to the date of this
    session's start — so yesterday's `hi` gates and yesterday's `prespec` releases."""
    after_midnight = datetime(2026, 9, 9, 0, 30, 0, tzinfo=UTC)
    with_event_log(tmp_path, START + HI, day=YESTERDAY)
    with_event_log(tmp_path, "- 00:05:00 99999999 session-start startup\n")
    err = io.StringIO()
    code = prespec.run([], stdin=payload(), stderr=err, project_dir=tmp_path, now=after_midnight)
    assert code == 2 and "/pre-spec" in err.getvalue()
    with_event_log(tmp_path, START + HI + PRETASK, day=YESTERDAY)
    err = io.StringIO()
    code = prespec.run([], stdin=payload(), stderr=err, project_dir=tmp_path, now=after_midnight)
    assert (code, err.getvalue()) == (0, "")


# --- a ref to a page the same plan creates (case 221) ------------------------------------

RULE_AND_ESTIMATE = (
    "create:\n  - slug: rule-new\n    type: rule\n    kind: Leaf\n    ref: rule-x\n"
    "    purpose: p\n    tags: [a]\n"
    "  - slug: estimate-x-again\n    type: estimate\n    ref: rule-new\n"
    "    kind: QA\n    purpose: p\n    method: pytest tests/test_x.py\n    tags: [a]\n"
)
RULE_AND_ESTIMATE_LINES = (
    "- 16:00:00 decision[case 1][create][rule-new]{ref:rule-x}{tags:a}\n"
    "- 16:00:01 decision[case 1][create][estimate-x-again]{ref:rule-new}{tags:a}\n"
)


def test_an_estimate_ref_to_a_rule_the_same_plan_creates_is_no_finding(tmp_path):
    with_page(tmp_path, "rules", "rule-x")
    code, out, _ = check(
        tmp_path, plan=create_plan(RULE_AND_ESTIMATE), ledger=RULE_AND_ESTIMATE_LINES
    )
    assert (code, out) == (0, "")
    # a ref to a slug no create of the plan carries is still a finding
    plan = create_plan(RULE_AND_ESTIMATE.replace("ref: rule-new", "ref: rule-nowhere"))
    lines = RULE_AND_ESTIMATE_LINES.replace("{ref:rule-new}", "{ref:rule-nowhere}")
    code, out, _ = check(tmp_path, plan=plan, ledger=lines)
    assert code == 1
    assert out.splitlines() == [
        "case 1: create estimate-x-again: ref rule-nowhere names no live page"
    ]


# --- a bare wikilink in the plan (case 264.2) -------------------------------------------


def bare_plan(sentence, block="update:\n  - slug: rule-x\n    change: one line\n"):
    plan = PLAN.replace("> Something.\n", f"> {sentence}\n")
    return plan.replace("update:\n  - slug: rule-x\n    change: one line\n", block)


def test_a_bare_wikilink_that_names_no_page_is_a_finding(tmp_path):
    code, out, _ = check(tmp_path, plan=bare_plan("History ends with [[decision-case-N]]."))
    assert code == 1
    assert out.splitlines() == ["case 1: [[decision-case-N]] outside a code span names no page"]


def test_a_wikilink_in_a_code_span_is_not_read(tmp_path):
    plan = bare_plan("History ends with `· [[decision-case-N]]`.")
    assert check(tmp_path, plan=plan) == (0, "", "")


def test_a_wikilink_to_a_live_an_archived_or_a_hub_page_is_no_finding(tmp_path):
    with_page(tmp_path, "rules", "rule-x")
    archive = tmp_path / "vault" / "archive" / "s" / "2026-01-01" / "0900" / "rules"
    archive.mkdir(parents=True)
    (archive / "rule-old.md").write_text("---\ntype: rule\n---\n", encoding="utf-8")
    (tmp_path / "vault" / "wiki" / "index.md").write_text("# Index\n", encoding="utf-8")
    plan = bare_plan("See [[rule-x]], [[rule-old]] and [[index]].")
    assert check(tmp_path, plan=plan) == (0, "", "")


def test_a_wikilink_to_a_slug_the_same_plan_creates_is_no_finding(tmp_path):
    with_page(tmp_path, "rules", "rule-x")
    block = (
        "create:\n  - slug: rule-new\n    type: rule\n    kind: Leaf\n"
        "    purpose: p\n    tags: [a]\n"
    )
    plan = bare_plan("The new rule is [[rule-new]].", block)
    ledger = "- 16:00:00 decision[case 1][create][rule-new]{ref:rule-x}{tags:a}\n"
    assert check(tmp_path, plan=plan, ledger=ledger) == (0, "", "")


def test_one_bare_slug_twice_in_a_case_is_one_line(tmp_path):
    plan = bare_plan("[[gone]] here and [[gone]] there.")
    plan = plan.replace("    change: one line\n", "    change: the [[gone]] line\n")
    _, out, _ = check(tmp_path, plan=plan)
    assert out.splitlines() == ["case 1: [[gone]] outside a code span names no page"]


def test_a_wikilink_in_a_then_block_string_is_read(tmp_path):
    plan = PLAN.replace("    change: one line\n", "    change: the [[gone]] line\n")
    _, out, _ = check(tmp_path, plan=plan)
    assert out.splitlines() == ["case 1: [[gone]] outside a code span names no page"]


def test_a_wikilink_in_a_tasks_fence_or_an_untagged_fence_is_not_read(tmp_path):
    plan = PLAN.replace("- [ ] guppi/x.py: the change\n", "- [ ] fix [[gone]]\n")
    plan += "\n```\n- decision[case 1][update][[gone]]\n```\n"
    assert check(tmp_path, plan=plan) == (0, "", "")


# --- the Frontier in two lists (case 268.2) -----------------------------------------------


def test_the_frontier_reads_cases_and_work_lines_under_their_headings(tmp_path):
    frontier = (
        "# Frontier\n\n## Cases\n\n- [x] C1 — the one item · brief · case 1\n"
        "- the pull fails, decided by the sprint page\n\n"
        "## Work\n\n- [x] W1 — a reading · brief · work\n"
    )
    assert check(tmp_path, frontier=frontier) == (0, "", "")
    # case 356.1: an open line under `## Work` waits for Work Mode; one under `## Cases` is open
    assert check(tmp_path, frontier=frontier + "- [ ] W2 — a commit · git status\n") == (0, "", "")
    cases_open = frontier.replace("## Work", "- [ ] C2 — a question · brief\n\n## Work")
    code, out, _ = check(tmp_path, frontier=cases_open)
    assert code == 1
    assert out.splitlines() == ["frontier: C2 is open"]
    # a closed `W` is read as any closed line
    code, out, _ = check(tmp_path, frontier=frontier + "- [x] W2 — a decision · brief · case 7\n")
    assert code == 1
    assert out.splitlines() == ["frontier: W2 closes with case 7, no Case 7 heading in the plan"]


def test_an_open_ask_line_is_no_finding_and_a_closed_one_is_judged(tmp_path):  # case 531.12
    frontier = (
        "# Frontier\n\n## Cases\n\n- [x] C1 — the one item · brief · case 1\n\n"
        "## Work\n\n- [x] W1 — a reading · brief · work\n\n"
        "## Ask\n\n- [ ] A1 — reading `estimate-x`: did the stop hold? · brief\n"
    )
    assert check(tmp_path, frontier=frontier) == (0, "", "")
    closed = frontier + "- [x] A2 — reading `estimate-y` · brief · case 7\n"
    code, out, _ = check(tmp_path, frontier=closed)
    assert code == 1
    assert out.splitlines() == ["frontier: A2 closes with case 7, no Case 7 heading in the plan"]


# --- a sprint line and the sprint page (cases 314.2, 451.3) ---------------------------


SPRINT_UPDATE = (
    "update:\n  - slug: rule-x\n    change: one line\n"
    "  - slug: entity-sprint-migration\n    change: the theme closed\n"
)
SPRINT_LEDGER = (
    LINE + "- 16:00:01 decision[case 1][update][entity-sprint-migration]"
    "{ref:entity-sprint-migration}\n"
)


def test_a_left_sprint_item_closes_with_sprint(tmp_path):
    # case 451.3: a sprint line left for a later session closes `[-] … · sprint · defer`
    frontier = "# Frontier\n\n- [-] C1 — a theme left for later · sprint · defer\n"
    assert check(tmp_path, frontier=frontier) == (0, "", "")


def test_a_sprint_item_closed_with_a_defer_case_is_a_finding(tmp_path):
    # case 356.2: a sprint item left for later closes `[-]` with `defer`, never a defer case
    frontier = "# Frontier\n\n- [-] C1 — `rule-x`, Slice 3b · sprint · defer case 1\n"
    code, out, _ = check(tmp_path, frontier=frontier)
    assert code == 1
    assert out.splitlines() == [
        "frontier: C1 defers a sprint item by a Case; a sprint item put off closes [-] with defer"
    ]
    # a line of another source defers as before: the defer item is what it needs
    brief = "# Frontier\n\n- [-] C1 — `rule-x` · brief · defer case 1\n"
    _, out, _ = check(tmp_path, frontier=brief)
    assert out.splitlines() == ["frontier: C1 defers to case 1, no defer item under Case 1"]


def test_the_old_sprint_closer_is_a_finding(tmp_path):
    # case 451.2: `sprint` is a source, no longer a closer, on either box
    frontier = "# Frontier\n\n- [-] C1 — a theme · sprint\n- [x] C2 — a theme · sprint\n"
    code, out, _ = check(tmp_path, frontier=frontier)
    assert code == 1
    assert out.splitlines() == [
        f"frontier: {item} is closed without case N, work, defer, kept or defer case N"
        for item in ("C1", "C2")
    ]


def test_a_sprint_defer_on_a_ticked_line_is_a_finding(tmp_path):
    frontier = "# Frontier\n\n- [x] C1 — a theme · sprint · defer\n"
    code, out, _ = check(tmp_path, frontier=frontier)
    assert code == 1
    assert out.splitlines() == ["frontier: C1 closes [x] with defer; an item put off is [-]"]


def test_a_decided_sprint_item_needs_an_update_of_the_sprint_page(tmp_path):
    frontier = "# Frontier\n\n- [x] C1 — a theme · sprint · case 1\n"
    code, out, _ = check(tmp_path, frontier=frontier)
    assert code == 1
    assert out.splitlines() == [
        "frontier: C1 closes a sprint item with case 1, no update of the sprint page under Case 1"
    ]


def test_a_decided_sprint_item_with_its_update_is_clean(tmp_path):
    frontier = "# Frontier\n\n- [x] C1 — a theme · sprint · case 1\n"
    plan = PLAN.replace("update:\n  - slug: rule-x\n    change: one line\n", SPRINT_UPDATE)
    assert check(tmp_path, plan=plan, ledger=SPRINT_LEDGER, frontier=frontier) == (0, "", "")


def test_a_line_whose_source_segment_is_not_sprint_needs_no_update(tmp_path):
    frontier = "# Frontier\n\n- [x] C1 — a reading · brief · case 1\n"
    assert check(tmp_path, frontier=frontier) == (0, "", "")


# --- the pairs of the Spec simulated in entry order (case 351) ----------------------------

TWO_CASES = """# Plan

## Case 1 — one

> **context:**
> Something.

```then
update:
  - slug: rule-x
    replace:
      - old: "FIRST"
        new: "SECOND"
    change: one line
```

```tasks
- [ ] guppi/x.py: the change
```

## Case 2 — two

> **context:**
> Something.

```then
update:
  - slug: rule-x
    replace:
      - old: "SECOND"
        new: "THIRD"
    change: one line
```

```tasks
- [ ] guppi/x.py: the change
```
"""
TWO_LINES = LINE + "- 16:00:02 decision[case 2][update][rule-x]{ref:rule-x}\n"
TWO_FRONTIER = "# Frontier\n\n- [x] F1 — one · owner · case 1\n- [x] F2 — two · owner · case 2\n"


def with_body(project_dir, text, slug="rule-x"):
    folder = project_dir / "vault" / "wiki" / "rules"
    folder.mkdir(parents=True, exist_ok=True)
    page = f"---\ntype: rule\nkind: Leaf\nstatus: built\n---\n\n## Purpose\n\n{text}\n"
    (folder / f"{slug}.md").write_text(page, encoding="utf-8", newline="\n")


def anchor_plan(old, new="SECOND"):
    return (
        TWO_CASES.split("## Case 2")[0]
        .replace('- old: "FIRST"', f'- old: "{old}"')
        .replace('        new: "SECOND"', f'        new: "{new}"')
    )


def test_a_replace_anchor_that_misses_is_a_finding(tmp_path):
    # case 351: the pair is applied to a copy of the page in memory, nothing is written
    with_body(tmp_path, "the body says nothing of it")
    code, out, _ = check(tmp_path, plan=anchor_plan("FIRST"))
    assert code == 1
    assert out.splitlines() == ["case 1: rule-x: a replace anchor is not in the page: FIRST"]


def test_a_replace_anchor_that_hits_twice_is_a_finding(tmp_path):
    with_body(tmp_path, "FIRST and again FIRST")
    code, out, _ = check(tmp_path, plan=anchor_plan("FIRST"))
    assert code == 1
    assert out.splitlines() == ["case 1: rule-x: a replace anchor hits 2 times: FIRST"]


def test_an_anchor_an_earlier_case_produces_is_clean(tmp_path):
    # the anchor is judged against the page as the Spec leaves it, not as it stands today:
    # Case 1 writes SECOND, and the anchor of Case 2 finds it
    with_body(tmp_path, "FIRST")
    assert check(tmp_path, plan=TWO_CASES, ledger=TWO_LINES, frontier=TWO_FRONTIER) == (0, "", "")


def test_the_simulation_writes_nothing_to_disk(tmp_path):
    # the pairs are applied to copies in memory: the page on disk is untouched, whether the
    # anchor hit or missed
    with_body(tmp_path, "FIRST")
    assert check(tmp_path, plan=anchor_plan("FIRST")) == (0, "", "")
    page = tmp_path / "vault" / "wiki" / "rules" / "rule-x.md"
    assert "FIRST" in page.read_text(encoding="utf-8")
    assert "SECOND" not in page.read_text(encoding="utf-8")


def test_a_reword_pair_no_live_page_holds_is_a_finding(tmp_path):
    with_body(tmp_path, "the body says nothing of it")
    plan = anchor_plan("FIRST").replace("    replace:\n", "    reword:\n")
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out.splitlines() == ["case 1: rule-x: a reword pair hits no live page: FIRST"]


def test_a_reword_pair_a_live_page_holds_is_clean(tmp_path):
    with_body(tmp_path, "FIRST stands here")
    plan = anchor_plan("FIRST").replace("    replace:\n", "    reword:\n")
    assert check(tmp_path, plan=plan) == (0, "", "")


def test_a_pair_whose_anchor_an_earlier_case_removes_is_a_finding(tmp_path):
    # the other side of the same coin: Case 1 takes FIRST away, so Case 2 cannot find it
    with_body(tmp_path, "FIRST")
    plan = TWO_CASES.replace('      - old: "SECOND"', '      - old: "FIRST"')
    code, out, _ = check(tmp_path, plan=plan, ledger=TWO_LINES, frontier=TWO_FRONTIER)
    assert code == 1
    assert out.splitlines() == ["case 2: rule-x: a replace anchor is not in the page: FIRST"]


# --- a code fence a pair or a written section breaks (case 487.1) --------------------------

SENTENCE = "No Case is named twice."
FENCED_NEW = SENTENCE + "\\n\\n```\\nsample\\n```"
BROKEN_UPDATE = (
    "update:\n  - slug: rule-x\n    sections:\n      Purpose: |\n        ```\n        open\n"
    "    change: one line\n"
)


def test_a_pair_that_joins_text_to_a_closing_fence_is_a_finding(tmp_path):
    # the defect of case 483: an anchor in the middle of a line, a `new` ending on a fence
    with_body(tmp_path, SENTENCE + " When the person approves, commit.")
    code, out, _ = check(tmp_path, plan=anchor_plan(SENTENCE, FENCED_NEW))
    assert code == 1
    assert out.splitlines() == [
        (
            "case 1: rule-x: ## Purpose: a pair leaves a code fence with text after it: "
            "``` When the person approves, commit."
        ),
        (
            "case 1: rule-x: ## Purpose: a pair leaves a code fence open at the end of the "
            "section: ```"
        ),
    ]
    page = tmp_path / "vault" / "wiki" / "rules" / "rule-x.md"
    assert "sample" not in page.read_text(encoding="utf-8")


def test_a_pair_that_closes_its_fence_on_its_own_line_is_clean(tmp_path):
    with_body(tmp_path, SENTENCE + "\n\nWhen the person approves, commit.")
    assert check(tmp_path, plan=anchor_plan(SENTENCE, FENCED_NEW)) == (0, "", "")


def test_a_fence_break_the_section_held_before_the_pair_is_not_a_finding(tmp_path):
    with_body(tmp_path, "FIRST\n\n```\nx\n``` word")
    assert check(tmp_path, plan=anchor_plan("FIRST")) == (0, "", "")


def test_a_sections_value_with_an_open_fence_is_a_finding(tmp_path):
    with_body(tmp_path, "the body")
    plan = PLAN.replace("update:\n  - slug: rule-x\n    change: one line\n", BROKEN_UPDATE)
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out.splitlines() == [
        (
            "case 1: rule-x: Purpose: a sections value leaves a code fence open at the end of "
            "the section: ```"
        )
    ]


# --- a Render written without the page's own markers (case 325.1) ------------------------

UNWRAPPED_UPDATE = (
    "update:\n  - slug: rule-x\n    sections:\n      Render: |\n        the body, no markers\n"
    "    change: the Render rewritten\n"
)
WRAPPED_UPDATE = UNWRAPPED_UPDATE.replace(
    "        the body, no markers\n",
    "        <!-- rule-x -->\n        the body\n        <!-- /rule-x -->\n",
)
UNWRAPPED_CREATE = (
    "create:\n  - slug: rule-z\n    type: rule\n    kind: Leaf\n    enforcement: render\n"
    "    governs: .claude/x.md\n    sections:\n      Render: |\n        the body, no markers\n"
)
CREATE_RULE_LINE = "- 16:00:00 decision[case 1][create][rule-z]{ref:rule-x}{tags:a}\n"


def unwrapped(slug, kind="update"):
    return f"case 1: {kind} {slug}: Render is not wrapped in <!-- {slug} --> … <!-- /{slug} -->"


def test_an_update_writing_a_render_without_its_markers_is_a_finding(tmp_path):
    # case 325.1: the page enforces by render, so the text it writes carries its own markers
    with_rule(tmp_path, "rule-x", ".claude/x.md", enforcement="render")
    plan = PLAN.replace("update:\n  - slug: rule-x\n    change: one line\n", UNWRAPPED_UPDATE)
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert out.splitlines() == [unwrapped("rule-x")]


def test_a_wrapped_render_is_clean(tmp_path):
    with_rule(tmp_path, "rule-x", ".claude/x.md", enforcement="render")
    plan = PLAN.replace("update:\n  - slug: rule-x\n    change: one line\n", WRAPPED_UPDATE)
    assert check(tmp_path, plan=plan) == (0, "", "")


def test_a_render_on_a_page_that_does_not_enforce_by_render_is_clean(tmp_path):
    with_rule(tmp_path, "rule-x", ".claude/x.md")
    plan = PLAN.replace("update:\n  - slug: rule-x\n    change: one line\n", UNWRAPPED_UPDATE)
    assert check(tmp_path, plan=plan) == (0, "", "")


def test_a_create_writing_a_render_without_its_markers_is_a_finding(tmp_path):
    # in a `create` the fields stand in the item itself: there is no page yet
    plan = PLAN.replace("update:\n  - slug: rule-x\n    change: one line\n", UNWRAPPED_CREATE)
    code, out, _ = check(tmp_path, plan=plan, ledger=CREATE_RULE_LINE)
    assert code == 1
    assert out.splitlines() == [unwrapped("rule-z", kind="create")]


def test_the_word_sprint_inside_a_title_is_not_the_source(tmp_path):
    # case 335: the source is the segment before the closer; six live Estimates hold
    # `sprint` in their slug, and a title naming one is no item of the sprint
    frontier = (
        "# Frontier\n\n- [x] C1 — estimate-sprint-migration-index-dissolved · brief · case 1\n"
    )
    assert check(tmp_path, frontier=frontier) == (0, "", "")


# --- the form of a render or sprint task line (case 279.2) ----------------------------


def tasks_plan(line):
    return PLAN.replace("- [ ] guppi/x.py: the change", line)


def test_a_render_line_opening_with_the_bare_word_is_a_finding(tmp_path):
    code, out, _ = check(tmp_path, plan=tasks_plan("- [ ] render `CLAUDE.md`"))
    assert code == 1
    assert out.splitlines() == ["case 1: render line off form: - [ ] render `CLAUDE.md`"]


def test_the_command_outside_a_code_span_is_a_finding(tmp_path):
    for line in (
        "- [ ] uv run guppi render: `CLAUDE.md`",
        "- [ ] guppi sprint after the render",
        "- [ ] sprint `vault/wiki/sprint.md`",
    ):
        code, out, _ = check(tmp_path, plan=tasks_plan(line))
        assert code == 1, line
        assert out.splitlines() == [f"case 1: render line off form: {line}"]


def test_the_tickers_form_is_no_finding(tmp_path):
    for line in (
        "- [ ] `uv run guppi render`: `CLAUDE.md`",
        "- [ ] `uv run guppi sprint`",
        "- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`",
    ):
        assert check(tmp_path, plan=tasks_plan(line)) == (0, "", ""), line


def test_a_read_line_naming_the_command_later_is_no_finding(tmp_path):
    line = "- [ ] read `estimate-x`: `uv run guppi render` and `--check` after the build"
    assert check(tmp_path, plan=tasks_plan(line)) == (0, "", "")
    line = "- [ ] the rendered `CLAUDE.md` read by hand after `guppi render`"
    assert check(tmp_path, plan=tasks_plan(line)) == (0, "", "")


# --- a pair inside a Criterion (case 378.4) --------------------------------------------

ESTIMATE_LINE = "- 16:00:00 decision[case 1][update][estimate-x]{ref:estimate-x}\n"


def with_criterion(project_dir):
    folder = project_dir / "vault" / "wiki" / "estimates"
    folder.mkdir(parents=True, exist_ok=True)
    text = (
        "---\ntype: estimate\nkind: QA\nstatus: passed\ntarget: rule-x\nmethod: by hand\n---\n\n"
        "## Criterion\n\nWhen:\nold words.\n\n## Result\n\nread on Monday\n"
    )
    (folder / "estimate-x.md").write_text(text, encoding="utf-8", newline="\n")


def pair_plan(old):
    block = (
        "update:\n  - slug: estimate-x\n    replace:\n"
        f'      - old: "{old}"\n        new: "new words."\n    change: one line\n'
    )
    return bare_plan("Something.", block)


def test_a_replace_pair_inside_a_criterion_is_a_finding(tmp_path):
    with_criterion(tmp_path)
    code, out, _ = check(tmp_path, plan=pair_plan("old words."), ledger=ESTIMATE_LINE)
    assert code == 1
    assert out.splitlines() == [
        (
            "case 1: update estimate-x: a replace pair inside the Criterion — "
            "a Criterion changes only whole: old words."
        )
    ]


def test_a_replace_pair_outside_the_criterion_is_clean(tmp_path):
    with_criterion(tmp_path)
    plan = pair_plan("read on Monday")
    assert check(tmp_path, plan=plan, ledger=ESTIMATE_LINE) == (0, "", "")


# --- the frame of a Case (case 378.7) --------------------------------------------------


def frame_plan(given, when, then, heading="## Case 1 — one"):
    return f"""# Plan

## Case 1 — one

> **context:**
> Something.

> **given:**
> {given}

{heading if heading != "## Case 1 — one" else ""}

> **when:**
> {when}

> **then:**
> {then}

```then
update:
  - slug: rule-x
    change: one line
```

```tasks
- [ ] guppi/x.py: the change
```
"""


def test_a_case_inside_its_frame_is_clean(tmp_path):
    plan = frame_plan(
        "`rule-x` — the rule.\n> **＋** `/hi` — the skill.",
        "The person types `/hi`.",
        "`rule-x` holds.",
    )
    assert check(tmp_path, plan=plan) == (0, "", "")


def test_a_slug_in_then_not_in_given_is_a_finding(tmp_path):
    plan = frame_plan("`rule-x` — the rule.", "The agent writes.", "`rule-y` holds.")
    assert check(tmp_path, plan=plan) == (1, "case 1: rule-y is not named in its given\n", "")


def test_a_target_of_the_then_block_not_in_given_is_a_finding(tmp_path):
    plan = frame_plan("`guppi/x.py` — the module.", "The agent writes.", "It holds.")
    assert check(tmp_path, plan=plan) == (1, "case 1: rule-x is not named in its given\n", "")


def test_a_slash_command_not_in_given_is_a_finding(tmp_path):
    plan = frame_plan("`rule-x` — the rule.", "The person types `/hi`.", "It holds.")
    assert check(tmp_path, plan=plan) == (1, "case 1: /hi is not named in its given\n", "")


def test_a_lone_slash_span_is_no_path(tmp_path):
    plan = frame_plan("`rule-x` — the rule.", "A span holds `/`.", "It holds.")
    assert check(tmp_path, plan=plan) == (0, "", "")


def test_a_sub_case_is_checked_against_its_parents_given(tmp_path):
    plan = frame_plan(
        "`rule-x` — the rule.", "The agent writes.", "`rule-x` holds.", heading="### Case 1.1 — sub"
    )
    ledger = "- 16:00:00 decision[case 1.1][update][rule-x]{ref:rule-x}\n"
    frontier = "# Frontier\n\n- [x] F1 — the one item · owner · case 1.1\n"
    assert check(tmp_path, plan=plan, ledger=ledger, frontier=frontier) == (0, "", "")
    plan = plan.replace("`rule-x` holds.", "`rule-y` holds.")
    code, out, _ = check(tmp_path, plan=plan, ledger=ledger, frontier=frontier)
    assert (code, out) == (1, "case 1.1: rule-y is not named in its given\n")


def test_a_case_without_given_is_not_checked(tmp_path):
    assert check(tmp_path, plan=bare_plan("`rule-y` is named in context only.")) == (0, "", "")


# --- a long chain of ＋ lines is a note (case 378.8) -----------------------------------


def chain(count):
    return "`rule-x` holds." + "".join(f"\n> **＋** `rule-x` holds {n}." for n in range(count))


def test_eight_and_lines_in_then_are_a_note_and_exit_zero(tmp_path):
    plan = frame_plan("`rule-x` — the rule.", "The agent writes.", chain(8))
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 0
    assert out == "note: case 1: then holds 8 ＋ lines — is the Case atomic?\n"


def test_seven_and_lines_are_no_note(tmp_path):
    plan = frame_plan("`rule-x` — the rule.", "The agent writes.", chain(7))
    assert check(tmp_path, plan=plan) == (0, "", "")


# --- the Cyrillic finding (cases 387.4, 445.4): `estimate-language-spec-prose-in-english` ---

DEFERRED_CASE = """
## Deferred

## Case 2 — later

> **context:**
> Later.

> **problem:**
> Not now.

```then
defer:
  - slug: rule-later
    type: rule
    purpose: Later
```
"""
DEFER_LINE = "- 16:00:02 decision[case 2][defer][rule-later]{ref:rule-later}\n"
FRONTIER_WITH_DEFER = CLEAN_FRONTIER + "- [-] F2 — later · owner · defer case 2\n"


def script_lines(out):
    return [line for line in out.splitlines() if "script" in line or "guppi.toml" in line]


OUTSIDE_LATIN = "holds a letter outside the Latin script of English — translate it"


def test_script_a_name_a_context_and_a_problem_are_found(tmp_path):
    plan = PLAN.replace("## Case 1 — one", "## Case 1 — один").replace(
        "> Something.", "> Что-то.\n\n> **problem:**\n> Вопрос."
    )
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert script_lines(out) == [
        f"case 1: its name {OUTSIDE_LATIN}",
        f"case 1: its context {OUTSIDE_LATIN}",
        f"case 1: its problem {OUTSIDE_LATIN}",
    ]


def test_script_a_short_form_under_deferred_is_found(tmp_path):
    plan = PLAN + DEFERRED_CASE.replace("## Case 2 — later", "## Case 2 — позже").replace(
        "> Later.", "> Позже."
    )
    code, out, _ = check(
        tmp_path, plan=plan, ledger=LINE + DEFER_LINE, frontier=FRONTIER_WITH_DEFER
    )
    assert code == 1
    assert script_lines(out) == [
        f"case 2: its name {OUTSIDE_LATIN}",
        f"case 2: its context {OUTSIDE_LATIN}",
    ]


def test_script_in_given_when_then_or_a_block_is_not_found(tmp_path):
    plan = frame_plan("`rule-x` — правило.", "Агент пишет.", "`rule-x` держится.").replace(
        "change: one line", "change: одна строка"
    )
    plan = plan.replace("- [ ] guppi/x.py: the change", "- [ ] guppi/x.py: изменение")
    assert check(tmp_path, plan=plan) == (0, "", "")


def test_script_an_english_plan_is_clean(tmp_path):
    plan = PLAN + DEFERRED_CASE
    code, out, err = check(
        tmp_path, plan=plan, ledger=LINE + DEFER_LINE, frontier=FRONTIER_WITH_DEFER
    )
    assert (code, out, err) == (0, "", "")


def test_script_follows_the_documentation_language_of_guppi_toml(tmp_path):
    plan = PLAN.replace("## Case 1 — one", "## Case 1 — один")
    russian = 'documentation_lang = "ru"\nchat_lang = "en"\n'
    code, out, _ = check(tmp_path, plan=plan, settings=russian)
    assert code == 1
    assert script_lines(out) == [
        "case 1: its context holds a letter outside the Cyrillic script of Russian — translate it"
    ]


@pytest.mark.parametrize(
    ("settings", "named"),
    [
        (None, "guppi.toml: missing"),
        ('documentation_lang = "xx"\nchat_lang = "ru"\n', "guppi.toml: documentation_lang = 'xx'"),
    ],
    ids=["missing guppi.toml", "unknown code"],
)
def test_script_a_missing_or_unknown_setting_is_one_finding_and_no_case_is_read(
    tmp_path, settings, named
):
    plan = PLAN.replace("## Case 1 — one", "## Case 1 — один")
    code, out, _ = check(tmp_path, plan=plan, settings=settings)
    assert code == 1
    lines = script_lines(out)
    assert len(lines) == 1
    assert lines[0].startswith(named)
    assert "no Case is read" in lines[0]


# --- the notes of the promise lines (cases 472.1, 472.2) -------------------------------

OLD_CRITERION = "When:\nw.\n\nThen:\nt one.\n**＋** t two."
ESTIMATE_LINE_1 = "- 16:00:00 decision[case 1][update][estimate-x]{ref:estimate-x}\n"


def with_old_criterion(project_dir, criterion=OLD_CRITERION, slug="estimate-x"):
    folder = project_dir / "vault" / "wiki" / "estimates"
    folder.mkdir(parents=True, exist_ok=True)
    text = (
        "---\ntype: estimate\nkind: QA\nstatus: passed\ntarget: rule-x\n---\n\n"
        f"## Criterion\n\n{criterion}\n\n## History\n\n- h\n"
    )
    (folder / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")


def recut_plan(then, item="    set: {status: pending}\n    change: recut\n"):
    return f"""# Plan

## Case 1 — one

> **context:**
> Something.

> **given:**
> `estimate-x` — the promise.

> **when:**
> w.

> **then:**
> {then}

```then
update:
  - slug: estimate-x
{item}```

```tasks
- [ ] read `estimate-x`
```
"""


def test_note_a_criterion_line_not_carried_is_a_note_and_exit_zero(tmp_path):
    with_old_criterion(tmp_path)
    code, out, _ = check(tmp_path, plan=recut_plan("t one."), ledger=ESTIMATE_LINE_1)
    assert code == 0
    assert out == "note: case 1: estimate-x: a line of its Criterion is not carried: t two.\n"


def test_note_a_criterion_carried_line_by_line_with_its_operands_changed_is_none(tmp_path):
    with_old_criterion(tmp_path)
    plan = recut_plan("t one.\n> **－** t two.")
    assert check(tmp_path, plan=plan, ledger=ESTIMATE_LINE_1) == (0, "", "")


def test_note_an_update_with_change_alone_is_compared(tmp_path):
    with_old_criterion(tmp_path)
    plan = recut_plan("t one.", item="    change: recut\n")
    _, out, _ = check(tmp_path, plan=plan, ledger=ESTIMATE_LINE_1)
    assert out == "note: case 1: estimate-x: a line of its Criterion is not carried: t two.\n"


def test_note_a_written_criterion_is_the_new_one(tmp_path):
    with_old_criterion(tmp_path)
    written = (
        "    set: {status: pending}\n    sections:\n      Criterion: |\n"
        "        When:\n        w.\n\n        Then:\n        t one.\n        **＋** t two.\n"
    )
    plan = recut_plan("something else.", item=written)
    assert check(tmp_path, plan=plan, ledger=ESTIMATE_LINE_1) == (0, "", "")


def test_note_an_update_that_names_a_part_and_a_create_are_none(tmp_path):
    with_old_criterion(tmp_path)
    a_part = recut_plan("t one.", item="    set: {purpose: p2}\n    change: purpose\n")
    assert check(tmp_path, plan=a_part, ledger=ESTIMATE_LINE_1) == (0, "", "")
    with_page(tmp_path, "rules", "rule-x")
    created = recut_plan("t one.").replace(
        "update:\n  - slug: estimate-x\n    set: {status: pending}\n    change: recut\n",
        "create:\n  - slug: estimate-x-again\n    type: estimate\n    ref: rule-x\n"
        "    kind: QA\n    purpose: p\n    method: pytest tests/test_x.py\n    tags: [a]\n",
    )
    created = created.replace(
        "> `estimate-x` — the promise.",
        "> `estimate-x-again` — the promise.\n> **＋** `rule-x` — the rule.",
    ).replace("read `estimate-x`", "read `estimate-x-again`")
    ledger = "- 16:00:00 decision[case 1][create][estimate-x-again]{ref:rule-x}{tags:a}\n"
    assert check(tmp_path, plan=created, ledger=ledger) == (0, "", "")


def siblings_plan(first, second):
    def sub(case, then):
        return (
            f"\n### Case {case} — part\n\n> **when:**\n> The agent writes.\n\n"
            f"> **then:**\n> {then}\n\n```then\nupdate:\n  - slug: rule-x\n"
            f"    change: one line\n```\n\n```tasks\n- [ ] guppi/x.py: the change\n```\n"
        )

    return (
        "# Plan\n\n## Case 1 — one\n\n> **context:**\n> Something.\n\n"
        "> **given:**\n> `rule-x` — the rule.\n" + sub("1.1", first) + sub("1.2", second)
    )


SIBLING_LINES = (
    "- 16:00:00 decision[case 1.1][update][rule-x]{ref:rule-x}\n"
    "- 16:00:01 decision[case 1.2][update][rule-x]{ref:rule-x}\n"
)


def test_note_two_siblings_with_one_promise_in_two_wordings(tmp_path):
    plan = siblings_plan(
        "The check sends each note back to the agent once.",
        "Each note goes back to the agent once, sent by the check.",
    )
    code, out, _ = check(tmp_path, plan=plan, ledger=SIBLING_LINES)
    assert code == 0
    assert out.splitlines() == [
        (
            "note: case 1.2: a then line shares most of its words with case 1.1: "
            "Each note goes back to the agent once, sent by the check. | "
            "The check sends each note back to the agent once."
        )
    ]


def test_note_two_siblings_with_unlike_lines_are_none(tmp_path):
    plan = siblings_plan("The check sends each note back.", "The page is read by hand.")
    assert check(tmp_path, plan=plan, ledger=SIBLING_LINES) == (0, "", "")


def test_note_a_line_with_no_word_of_four_characters_is_not_compared(tmp_path):
    plan = siblings_plan("It is so.", "It is so.")
    assert check(tmp_path, plan=plan, ledger=SIBLING_LINES) == (0, "", "")
