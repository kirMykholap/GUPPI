"""`guppi pretask`: the `PreToolUse ExitPlanMode` hook that holds Plan Mode open until
`/pre-task` has run in this session, and `guppi pretask --check <plan>`, the check of the
session's decision lines, frontier, tasks, the form of its Leaf items and the grammar of
its record lines against the plan (cases 59.1, 59.2, 59.3, 59.6, 72.5, 73.4, 74, 75.2).
Rule page: `vault/wiki/rules/rule-pretask-hook.md`.

Every hook test feeds the payload through a stream, the shape a hook is really handed. The
check tests build a temp project: an event log with the session's `hi`, a ledger written
after it, a plan file and a frontier in the session's folder `raw/<date>/<hi HHMM>/`.
"""

import io
import json
from datetime import UTC, date, datetime

from guppi import pretask

TODAY = date(2026, 9, 9)
NOW = datetime(2026, 9, 9, 18, 40, 5, tzinfo=UTC)
SESSION = "44c1aae1-4076-4a58-a7c0-d20bc274047c"
START = "- 15:01:00 44c1aae1 session-start startup\n"
HI = "- 15:01:30 -------- hi\n"
PRETASK = "- 16:20:00 -------- pretask\n"
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
    code = pretask.run([], stdin=stdin, stderr=err, project_dir=project_dir, now=NOW)
    return code, err.getvalue()


def test_pretask_after_hi_lets_the_plan_close(tmp_path):
    with_event_log(tmp_path, START + HI + PRETASK)
    assert run(payload(), tmp_path) == (0, "")


def test_hi_without_pretask_holds_plan_mode_open(tmp_path):
    with_event_log(tmp_path, START + HI)
    code, err = run(payload(), tmp_path)
    assert code == 2
    assert "/pre-task" in err and "44c1aae1" in err


def test_a_pretask_of_an_earlier_session_does_not_count(tmp_path):
    with_event_log(tmp_path, OTHER_START + HI + PRETASK + START + HI)
    code, err = run(payload(), tmp_path)
    assert code == 2
    assert "/pre-task" in err


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


def test_cli_dispatches_to_pretask(tmp_path, monkeypatch, capsys):
    from guppi import cli

    today = datetime.now().astimezone().date()  # the CLI reads the real clock

    with_event_log(tmp_path, START + HI, day=today)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr("sys.stdin", payload())
    assert cli.main(["pretask"]) == 2
    assert "/pre-task" in capsys.readouterr().err


# --- `guppi pretask --check <plan>` ---------------------------------------------------

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


def with_rule(project_dir, slug, governs):
    folder = project_dir / "vault" / "wiki" / "rules"
    folder.mkdir(parents=True, exist_ok=True)
    text = f"---\ntype: rule\nstatus: built\ngoverns: {governs}\n---\n\n## Purpose\n\nx\n"
    (folder / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")


def with_page(project_dir, category, slug, kind="Leaf", estimates=("estimate-x",)):
    folder = project_dir / "vault" / "wiki" / category
    folder.mkdir(parents=True, exist_ok=True)
    text = f"---\ntype: {category[:-1] if category != 'entities' else 'entity'}\n"
    text += f"kind: {kind}\nstatus: built\n"
    text += "estimates: [" + ", ".join(estimates) + "]\n---\n\n## Purpose\n\nx\n"
    (folder / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")


def check(project_dir, plan=PLAN, ledger=LINE, frontier=CLEAN_FRONTIER, event_log=START + HI):
    with_event_log(project_dir, event_log)
    with_ledger(project_dir, ledger)
    if frontier is not None:
        with_frontier(project_dir, frontier)
    plan_file = project_dir / "plan.md"
    plan_file.write_text(plan, encoding="utf-8", newline="\n")
    out, err = io.StringIO(), io.StringIO()
    code = pretask.run(
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


def test_a_line_of_a_case_the_plan_lacks_is_a_finding(tmp_path):
    extra = "- 16:00:01 decision[case 2][update][rule-y]{ref:rule-y}\n"
    _, out, _ = check(tmp_path, ledger=LINE + extra)
    assert out.splitlines() == ["case 2: line [update][rule-y]: no Case 2 heading in the plan"]


def test_a_defer_line_matches_a_defer_item(tmp_path):
    ledger = LINE + "- 16:00:01 decision[case 1][defer][rule-later]\n"
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\ndefer:\n  - slug: rule-later\n    type: rule\n    purpose: p\n",
    )
    assert check(tmp_path, plan=plan, ledger=ledger) == (0, "", "")
    _, out, _ = check(tmp_path, ledger=ledger)
    assert out.splitlines() == ["case 1: line [defer][rule-later] has no item in the plan"]


def test_a_rule_class_file_line_matches_a_file_item(tmp_path):
    ledger = LINE + "- 16:00:01 decision[case 1][update][index]{ref:index}\n"
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\n  - file: vault/wiki/index.md\n    change: a row\n",
    )
    assert check(tmp_path, plan=plan, ledger=ledger) == (0, "", "")
    _, out, _ = check(tmp_path, plan=plan)
    assert out.splitlines() == ["case 1: item [update][vault/wiki/index.md] has no decision line"]


def test_a_nested_estimate_is_covered_by_its_parents_create_line(tmp_path):
    # a Leaf's Estimate has no line of its own (case 72.5): the parent's line covers the
    # nested estimate of an older Spec; a line for the nested slug, if someone writes one,
    # still finds it
    parent = "- 16:00:00 decision[case 1][create][rule-z]{ref:rule-root}{tags:a}\n"
    paired = "- 16:00:00 decision[case 1][create][estimate-z-works]{ref:rule-z}{tags:a}\n"
    plan = PLAN.replace(
        "update:\n  - slug: rule-x\n    change: one line\n",
        "create:\n  - slug: rule-z\n    type: rule\n    estimate:\n      slug: estimate-z-works\n",
    ).replace("- [ ] guppi/x.py: the change", "- [ ] take the reading of estimate-z-works")
    assert check(tmp_path, plan=plan, ledger=parent) == (0, "", "")
    assert check(tmp_path, plan=plan, ledger=parent + paired) == (0, "", "")


def test_a_standalone_estimate_create_needs_its_own_line(tmp_path):
    plan = PLAN.replace(
        "update:\n  - slug: rule-x\n    change: one line\n",
        "create:\n  - slug: estimate-alone\n    type: estimate\n",
    ).replace("- [ ] guppi/x.py: the change", "- [ ] take the reading of estimate-alone")
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
    log = "- 11:55:00 44c1aae1 session-start startup\n- 11:56:22 -------- hi\n"
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
    code, out, _ = check(tmp_path, plan=plan, ledger=ledger)
    assert code == 1
    assert out.splitlines() == ["case 1: estimate-x-holds has no task line"]
    passing = plan.replace("- [ ] guppi/x.py: the change", "- [ ] the reading of estimate-x-holds")
    assert check(tmp_path, plan=passing, ledger=ledger) == (0, "", "")


def test_a_created_estimate_without_its_task_line_is_a_finding(tmp_path):
    ledger = "- 16:00:00 decision[case 1][create][estimate-fresh]{ref:rule-x}{tags:a}\n"
    plan = PLAN.replace(
        "update:\n  - slug: rule-x\n    change: one line\n",
        "create:\n  - slug: estimate-fresh\n    type: estimate\n",
    )
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
        "case 1: file .claude/skills/hi/SKILL.md is governed by rule-skill-hi" in out.splitlines()
    )


def test_check_without_a_plan_file_says_so(tmp_path):
    with_event_log(tmp_path, START + HI)
    err = io.StringIO()
    code = pretask.run(
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


# --- the form of a Leaf item (case 72.5) ------------------------------------------------

LEAF_CREATE = "create:\n  - slug: rule-z\n    type: rule\n    kind: Leaf\n    method: pytest\n"
CREATE_LINE = "- 16:00:00 decision[case 1][create][rule-z]{ref:rule-root}{tags:a}\n"


def create_plan(item=LEAF_CREATE):
    return PLAN.replace("update:\n  - slug: rule-x\n    change: one line\n", item)


def test_a_leaf_create_without_method_is_a_finding(tmp_path):
    plan = create_plan(LEAF_CREATE.replace("    method: pytest\n", ""))
    code, out, _ = check(tmp_path, plan=plan, ledger=CREATE_LINE)
    assert code == 1
    assert out.splitlines() == ["case 1: create rule-z has no method"]
    assert check(tmp_path, plan=create_plan(), ledger=CREATE_LINE) == (0, "", "")


def test_a_moc_create_needs_no_method(tmp_path):
    plan = create_plan(
        LEAF_CREATE.replace("kind: Leaf", "kind: MOC").replace("    method: pytest\n", "")
    )
    assert check(tmp_path, plan=plan, ledger=CREATE_LINE) == (0, "", "")


def test_a_leaf_update_without_contract_is_a_finding(tmp_path):
    with_page(tmp_path, "rules", "rule-x", kind="Leaf")
    code, out, _ = check(tmp_path)
    assert code == 1
    assert out.splitlines() == ["case 1: update rule-x has no contract"]
    plan = PLAN.replace("    change: one line\n", "    change: one line\n    contract: same\n")
    assert check(tmp_path, plan=plan) == (0, "", "")


def test_an_update_of_a_moc_or_of_a_missing_page_needs_no_contract(tmp_path):
    assert check(tmp_path) == (0, "", "")  # no page: the missing-page finding is elsewhere
    with_page(tmp_path, "rules", "rule-x", kind="MOC")
    assert check(tmp_path) == (0, "", "")


def test_two_contracts_in_one_case_is_a_finding(tmp_path):
    with_page(tmp_path, "rules", "rule-x", kind="Leaf")
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\n    contract: changed\n" + LEAF_CREATE,
    )
    code, out, _ = check(tmp_path, plan=plan, ledger=LINE + CREATE_LINE)
    assert code == 1
    assert out.splitlines() == ["case 1: two contracts in one Case — split it"]
    # a sub-case is its own Case: one contract each is fine
    split = plan.replace(
        LEAF_CREATE,
        "```\n\n```tasks\n- [ ] guppi/x.py: the change\n```\n\n### Case 1.1 — sub\n\n"
        "```then\n" + LEAF_CREATE,
    )
    ledger = LINE + CREATE_LINE.replace("[case 1]", "[case 1.1]")
    assert check(tmp_path, plan=split, ledger=ledger) == (0, "", "")


def test_a_derived_estimate_slug_that_names_a_page_needs_estimate_slug(tmp_path):
    with_page(tmp_path, "estimates", "estimate-z", kind="Leaf")
    code, out, _ = check(tmp_path, plan=create_plan(), ledger=CREATE_LINE)
    assert code == 1
    assert out.splitlines() == ["case 1: estimate estimate-z exists; name estimate_slug"]
    named = create_plan(LEAF_CREATE + "    estimate_slug: estimate-z-again\n")
    assert check(tmp_path, plan=named, ledger=CREATE_LINE) == (0, "", "")


def test_an_archived_estimate_page_counts_as_existing(tmp_path):
    archived = tmp_path / "vault" / "archive" / "migration" / "2026-09-01" / "estimates"
    archived.mkdir(parents=True)
    (archived / "estimate-z.md").write_text("---\ntype: estimate\n---\n", encoding="utf-8")
    _, out, _ = check(tmp_path, plan=create_plan(), ledger=CREATE_LINE)
    assert out.splitlines() == ["case 1: estimate estimate-z exists; name estimate_slug"]


def test_a_leaf_create_with_method_needs_no_estimate_line(tmp_path):
    # the Estimate is derived from the Case (72.3) and has no line of its own (72.5)
    assert check(tmp_path, plan=create_plan(), ledger=CREATE_LINE) == (0, "", "")


def test_file_and_defer_items_are_outside_the_form_checks(tmp_path):
    plan = PLAN.replace(
        "    change: one line\n",
        "    change: one line\n  - file: vault/wiki/index.md\n    change: a row\n"
        "defer:\n  - slug: rule-later\n    type: rule\n    purpose: p\n",
    )
    ledger = (
        LINE
        + "- 16:00:01 decision[case 1][update][index]{ref:index}\n"
        + "- 16:00:02 decision[case 1][defer][rule-later]\n"
    )
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
    log = "- 15:01:00 44c1aae1 session-start startup\n- 15:01:30 -------- hi\n"
    with_event_log(tmp_path, log, day=date(2026, 9, 8))
    with_ledger(tmp_path, LINE.replace("16:00:00", "23:00:00"), day=date(2026, 9, 8))
    with_frontier(tmp_path, CLEAN_FRONTIER, day=date(2026, 9, 8))
    plan_file = tmp_path / "plan.md"
    plan_file.write_text(PLAN, encoding="utf-8", newline="\n")
    out = io.StringIO()
    code = pretask.run(
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


def test_a_contract_change_names_the_estimate_when_the_page_does_not(tmp_path):
    plan = PLAN.replace("    change: one line\n", "    change: one line\n    contract: changed\n")
    with_page(tmp_path, "rules", "rule-x", kind="Leaf", estimates=("e-one", "e-two"))
    code, out, _ = check(tmp_path, plan=plan)
    assert code == 1
    assert "case 1: rule-x has 2 estimates (e-one, e-two); name estimate_slug" in out.splitlines()
    named = plan.replace(
        "    contract: changed\n", "    contract: changed\n    estimate_slug: e-two\n"
    )
    assert check(tmp_path, plan=named) == (0, "", "")
    with_page(tmp_path, "rules", "rule-x", kind="Leaf", estimates=())
    code, out, _ = check(tmp_path, plan=plan)
    assert "case 1: rule-x has 0 estimates (none); name estimate_slug" in out.splitlines()
    with_page(tmp_path, "rules", "rule-x", kind="Leaf", estimates=("e-one",))
    assert check(tmp_path, plan=plan) == (0, "", "")  # one Estimate names itself
