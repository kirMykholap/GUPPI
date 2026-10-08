"""`guppi sprint-close`: the close of a sprint over a made-up vault of one sprint (cases 627, 628.1)."""

import io
from datetime import UTC, datetime

import yaml

from guppi import sprint_close

NOW = datetime(2026, 10, 5, 12, 0, 0, tzinfo=UTC)
DATE = "2026-10-05"
SPRINT = "alpha"


def page(category, status, **extra):
    kind = {"entities": "entity", "rules": "rule", "estimates": "estimate", "lessons": "lesson"}
    kind |= {"insights": "insight", "decisions": "decision"}
    lines = [f"type: {kind[category]}", f"status: {status}"]
    lines += [f"{k}: {v}" for k, v in extra.items()]
    return (
        "---\n"
        + "\n".join(lines)
        + "\n---\n\n## Purpose\n\nx\n\n## History\n\n- 2026-09-09 created · x\n"
    )


def seed(tmp_path, pages, specs=()):
    wiki = tmp_path / "vault" / "wiki"
    for category in ("rules", "estimates", "lessons", "insights", "entities", "decisions"):
        (wiki / category).mkdir(parents=True)
    (wiki / "sprint.md").write_text(f"# Sprint\n\n## {SPRINT}\n", encoding="utf-8")
    (wiki / "log.md").write_text("# Log\n", encoding="utf-8")
    base = [
        (
            "entities",
            "entity-sprint",
            page("entities", "draft", kind="MOC", children="[entity-sprint-alpha]"),
        ),
        (
            "entities",
            "entity-sprint-alpha",
            page(
                "entities",
                "draft",
                parent="entity-sprint",
                estimates="[estimate-sprint-alpha-done]",
                sprint=SPRINT,
            ),
        ),
        (
            "estimates",
            "estimate-sprint-alpha-done",
            page("estimates", "passed", target="entity-sprint-alpha"),
        ),
    ]
    for category, slug, text in base + list(pages):
        (wiki / category / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")
    for folder, text in specs:
        path = tmp_path / "vault" / "raw" / folder / "spec.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    return tmp_path


def run(project_dir, *args):
    out, err = io.StringIO(), io.StringIO()
    code = sprint_close.run(
        ["--sprint", SPRINT, *args], stdout=out, stderr=err, project_dir=project_dir, now=NOW
    )
    return code, out.getvalue(), err.getvalue()


def live(project_dir, category, slug):
    return (project_dir / "vault" / "wiki" / category / f"{slug}.md").exists()


def archived(project_dir, category, slug):
    return (project_dir / "vault" / "archive" / SPRINT / DATE / category / f"{slug}.md").exists()


def snapshot(project_dir):
    return {p: p.read_bytes() for p in (project_dir / "vault").rglob("*") if p.is_file()}


def test_decisions_of_the_sprint_archived_but_one_a_live_page_names(tmp_path):
    seed(
        tmp_path,
        [
            ("decisions", "decision-case-1", page("decisions", "current", sprint=SPRINT)),
            ("decisions", "decision-case-2", page("decisions", "current", sprint=SPRINT)),
            ("decisions", "decision-case-3", page("decisions", "current", sprint=SPRINT)),
            ("decisions", "decision-case-4", page("decisions", "current", sprint="beta")),
            ("rules", "rule-x", page("rules", "draft", deferred_by='["[[decision-case-2]]"]')),
            (
                "insights",
                "insight-x",
                page("insights", "open", addressed_by='"[[decision-case-3]]"', sprint="beta"),
            ),
        ],
    )
    before = snapshot(tmp_path)
    code, out, err = run(tmp_path)
    assert code == 0 and err == ""
    assert snapshot(tmp_path) == before  # the preview moves nothing
    assert "move: decisions/decision-case-1 · a Decision page of the sprint" in out
    assert "keep: decisions/decision-case-2 · named in deferred_by of rule-x" in out
    assert "keep: decisions/decision-case-3 · named in addressed_by of insight-x" in out
    assert "decision-case-4" not in out
    code, out, err = run(tmp_path, "--apply")
    assert code == 0, err
    assert archived(tmp_path, "decisions", "decision-case-1")
    assert live(tmp_path, "decisions", "decision-case-2") and live(
        tmp_path, "decisions", "decision-case-3"
    )
    assert live(tmp_path, "decisions", "decision-case-4")


def test_insights_actioned_and_lone_error_lessons_archived(tmp_path):
    seed(
        tmp_path,
        [
            (
                "insights",
                "insight-done",
                page("insights", "actioned", sprint=SPRINT, children="[lesson-a]"),
            ),
            (
                "insights",
                "insight-open",
                page("insights", "open", sprint=SPRINT, children="[lesson-held]"),
            ),
            ("lessons", "lesson-a", page("lessons", "archived", kind="error", sprint=SPRINT)),
            ("lessons", "lesson-lone", page("lessons", "new", kind="error", sprint=SPRINT)),
            ("lessons", "lesson-held", page("lessons", "new", kind="error", sprint=SPRINT)),
            ("lessons", "lesson-know", page("lessons", "new", kind="knowledge", sprint=SPRINT)),
            ("lessons", "lesson-other", page("lessons", "new", kind="error", sprint="beta")),
        ],
    )
    before = snapshot(tmp_path)
    code, out, _ = run(tmp_path)
    assert code == 0 and snapshot(tmp_path) == before
    assert "move: insights/insight-done" in out and "move: lessons/lesson-lone" in out
    assert "keep: insights/insight-open · an open Insight" in out
    assert "keep: lessons/lesson-held · a child of an open Insight" in out
    assert "keep: lessons/lesson-know · a knowledge lesson" in out
    code, _, err = run(tmp_path, "--apply")
    assert code == 0, err
    assert archived(tmp_path, "insights", "insight-done") and archived(
        tmp_path, "lessons", "lesson-lone"
    )
    for slug in ("lesson-held", "lesson-know", "lesson-other"):
        assert live(tmp_path, "lessons", slug)
    assert live(tmp_path, "insights", "insight-open")


def test_sprint_page_and_its_estimates_archived_the_rest_kept(tmp_path):
    seed(
        tmp_path,
        [
            (
                "entities",
                "entity-sprint-alpha",
                page(
                    "entities",
                    "draft",
                    parent="entity-sprint",
                    estimates="[estimate-sprint-alpha-done, estimate-sprint-alpha-open]",
                    sprint=SPRINT,
                ),
            ),
            (
                "estimates",
                "estimate-sprint-alpha-open",
                page("estimates", "pending", target="entity-sprint-alpha"),
            ),
            ("rules", "rule-y", page("rules", "built", estimates="[estimate-rule-y-works]")),
            ("estimates", "estimate-rule-y-works", page("estimates", "passed", target="rule-y")),
        ],
    )
    before = snapshot(tmp_path)
    code, out, _ = run(tmp_path, "--archive-unread", "estimate-sprint-alpha-open")
    assert code == 0 and snapshot(tmp_path) == before
    assert "move: entities/entity-sprint-alpha · the sprint page" in out
    assert "move: estimates/estimate-sprint-alpha-done" in out
    assert "move: estimates/estimate-sprint-alpha-open" in out
    code, _, err = run(tmp_path, "--apply", "--archive-unread", "estimate-sprint-alpha-open")
    assert code == 0, err
    assert archived(tmp_path, "entities", "entity-sprint-alpha")
    assert archived(tmp_path, "estimates", "estimate-sprint-alpha-done")
    assert archived(tmp_path, "estimates", "estimate-sprint-alpha-open")
    assert live(tmp_path, "entities", "entity-sprint")
    assert live(tmp_path, "estimates", "estimate-rule-y-works")
    rule = (tmp_path / "vault" / "wiki" / "rules" / "rule-y.md").read_text(encoding="utf-8")
    assert "estimate-rule-y-works" in rule


def settle_vault(tmp_path, own_status="pending"):
    return seed(
        tmp_path,
        [
            (
                "entities",
                "entity-sprint-alpha",
                page(
                    "entities",
                    "draft",
                    parent="entity-sprint",
                    estimates="[estimate-sprint-alpha-done, estimate-sprint-alpha-open]",
                    sprint=SPRINT,
                ),
            ),
            (
                "estimates",
                "estimate-sprint-alpha-open",
                page("estimates", own_status, target="entity-sprint-alpha"),
            ),
            (
                "rules",
                "rule-z",
                page("rules", "draft", estimates="[estimate-rule-z-a, estimate-rule-z-b]"),
            ),
            ("estimates", "estimate-rule-z-a", page("estimates", "pending", target="rule-z")),
            ("estimates", "estimate-rule-z-b", page("estimates", "failed", target="rule-z")),
        ],
    )


def test_settle_preview_lists_each_unread_estimate_and_changes_nothing(tmp_path):
    settle_vault(tmp_path)
    before = snapshot(tmp_path)
    code, out, _ = run(tmp_path)
    assert code == 0 and snapshot(tmp_path) == before
    assert "unread: estimates/estimate-rule-z-a pending · rule-z · not settled" in out
    assert "unread: estimates/estimate-rule-z-b failed · rule-z · not settled" in out
    assert (
        "unread: estimates/estimate-sprint-alpha-open pending · entity-sprint-alpha · not settled"
        in out
    )


def test_settle_apply_refuses_while_one_is_not_named(tmp_path):
    settle_vault(tmp_path)
    before = snapshot(tmp_path)
    code, _, err = run(
        tmp_path,
        "--apply",
        "--carry",
        "estimate-rule-z-a",
        "--archive-unread",
        "estimate-sprint-alpha-open",
    )
    assert code == 1
    assert "estimate-rule-z-b: failed and not named" in err and "refused, nothing moved" in err
    assert snapshot(tmp_path) == before


def test_settle_carry_keeps_and_archive_unread_takes_off_estimates(tmp_path):
    settle_vault(tmp_path)
    code, out, err = run(
        tmp_path,
        "--apply",
        "--carry",
        "estimate-rule-z-a",
        "--archive-unread",
        "estimate-rule-z-b",
        "--archive-unread",
        "estimate-sprint-alpha-open",
    )
    assert code == 0, err
    carried = (tmp_path / "vault" / "wiki" / "estimates" / "estimate-rule-z-a.md").read_text(
        encoding="utf-8"
    )
    assert "status: pending" in carried
    assert archived(tmp_path, "estimates", "estimate-rule-z-b")
    rule = (tmp_path / "vault" / "wiki" / "rules" / "rule-z.md").read_text(encoding="utf-8")
    assert "estimate-rule-z-b" not in rule.split("---")[1] and "estimate-rule-z-a" in rule
    assert "estimate-rule-z-a pending · rule-z · carried into the next sprint" in out


def test_settle_carry_of_a_sprint_page_estimate_refused(tmp_path):
    settle_vault(tmp_path)
    before = snapshot(tmp_path)
    code, _, err = run(
        tmp_path,
        "--apply",
        "--carry",
        "estimate-rule-z-a",
        "--archive-unread",
        "estimate-rule-z-b",
        "--carry",
        "estimate-sprint-alpha-open",
    )
    assert code == 1 and "an Estimate of the sprint page is never carried" in err
    assert snapshot(tmp_path) == before


def test_settle_failed_sprint_page_estimate_goes_with_the_page_its_status_kept(tmp_path):
    settle_vault(tmp_path, own_status="failed")
    code, out, err = run(
        tmp_path, "--apply", "--carry", "estimate-rule-z-a", "--carry", "estimate-rule-z-b"
    )
    assert code == 0, err
    assert (
        "estimate-sprint-alpha-open failed · entity-sprint-alpha · goes with the sprint page, its status kept"
        in out
    )
    path = (
        tmp_path
        / "vault"
        / "archive"
        / SPRINT
        / DATE
        / "estimates"
        / "estimate-sprint-alpha-open.md"
    )
    assert f"- {DATE} status: failed → archived · the close of sprint {SPRINT}" in path.read_text(
        encoding="utf-8"
    )


def test_settle_unknown_slug_refused(tmp_path):
    settle_vault(tmp_path)
    code, _, err = run(tmp_path, "--apply", "--carry", "estimate-none")
    assert code == 1 and "estimate-none: no live Estimate that stands pending or failed" in err


def test_tick_the_close_line_after_a_run_that_moved(tmp_path):
    spec = (
        "- [ ] `uv run guppi sprint-close --sprint alpha --apply`\n"
        "- [ ] `uv run guppi sprint-close --sprint alphabet --apply`\n"
        "- [ ] `uv run guppi sprint`\n"
    )
    seed(tmp_path, [], specs=[("2026-10-05/1200", spec)])
    code, _, err = run(tmp_path, "--apply")
    assert code == 0, err
    text = (tmp_path / "vault" / "raw" / "2026-10-05" / "1200" / "spec.md").read_text(
        encoding="utf-8"
    )
    assert "- [x] `uv run guppi sprint-close --sprint alpha --apply`" in text
    assert "- [ ] `uv run guppi sprint-close --sprint alphabet --apply`" in text
    assert "- [ ] `uv run guppi sprint`" in text


def test_tick_nothing_after_a_refusal(tmp_path):
    spec = "- [ ] `uv run guppi sprint-close --sprint alpha --apply`\n"
    seed(
        tmp_path,
        [("estimates", "estimate-loose", page("estimates", "pending", target="rule-q"))],
        specs=[("2026-10-05/1200", spec)],
    )
    code, _, _ = run(tmp_path, "--apply")
    assert code == 1
    text = (tmp_path / "vault" / "raw" / "2026-10-05" / "1200" / "spec.md").read_text(
        encoding="utf-8"
    )
    assert text == spec


def test_no_sprint_page(tmp_path):
    seed(tmp_path, [])
    out, err = io.StringIO(), io.StringIO()
    code = sprint_close.run(
        ["--sprint", "gamma"], stdout=out, stderr=err, project_dir=tmp_path, now=NOW
    )
    assert code == 1 and "no live entity-sprint-gamma page" in err.getvalue()


# --- case 743.1: the sweep of raw/; case 743.3: the old event logs ---------------------

LEDGER = "- 10:00:00 decision[case 1][create][rule-a]\n"
APPLIED = {"sprint": SPRINT, "entries": [{"line": 1, "applied": "10:00"}], "unparsed": []}
PENDING = {"sprint": SPRINT, "entries": [{"line": 1, "failed": "boom"}], "unparsed": []}


def raw_unit(project_dir, unit, data=None, extra=()):
    folder = project_dir / "vault" / "raw" / unit
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "ledger.md").write_text(LEDGER, encoding="utf-8", newline="\n")
    if data is not None:
        (folder / "materialize.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
    for name in extra:
        (folder / name).write_text(name, encoding="utf-8")
    return folder


def sweep_vault(tmp_path):
    seed(tmp_path, [])
    raw_unit(tmp_path, f"{DATE}/0900", APPLIED)  # done, of the run day
    raw_unit(tmp_path, "2026-10-01/0800", APPLIED)  # done, of an earlier day
    raw_unit(tmp_path, f"{DATE}/1000", PENDING)  # an entry not applied
    raw_unit(tmp_path, "2026-10-02/1100", APPLIED, extra=("carry.md",))  # a conserved Spec
    raw_unit(tmp_path, f"{DATE}/1200", APPLIED)  # the session of the run
    return tmp_path


def test_sweep_moves_each_done_unit_whatever_its_day(tmp_path):
    sweep_vault(tmp_path)
    code, out, err = run(tmp_path, "--apply")
    assert code == 0, err
    raw = tmp_path / "vault" / "raw"
    base = tmp_path / "vault" / "archive" / SPRINT
    assert (base / DATE / "0900" / "raw" / "ledger.md").exists()
    assert (base / "2026-10-01" / "0800" / "raw" / "ledger.md").exists()
    assert not (raw / "2026-10-01").exists()  # the date folder the move left empty goes
    assert f"archive: raw/{DATE}/0900 → archive/{SPRINT}/{DATE}/0900/raw" in out
    assert f"archive: raw/{DATE}/1000 kept: 1 entries not applied" in out
    assert "archive: raw/2026-10-02/1100 kept: carried over" in out
    assert (raw / DATE / "1000" / "ledger.md").exists()
    assert (raw / "2026-10-02" / "1100" / "carry.md").exists()
    assert (raw / DATE / "1200" / "ledger.md").exists()  # the session of the run stays
    assert f"raw/{DATE}/1200" not in out


def test_sweep_the_preview_names_the_units_and_moves_none(tmp_path):
    sweep_vault(tmp_path)
    before = snapshot(tmp_path)
    code, out, _ = run(tmp_path)
    assert code == 0
    assert f"archive: raw/{DATE}/0900 would move → archive/{SPRINT}/{DATE}/0900/raw" in out
    assert "archive: raw/2026-10-01/0800 would move" in out
    assert snapshot(tmp_path) == before


def test_sweep_a_refused_close_moves_no_unit(tmp_path):
    sweep_vault(tmp_path)
    (tmp_path / "vault" / "wiki" / "estimates" / "estimate-loose.md").write_text(
        page("estimates", "pending", target="rule-q"), encoding="utf-8"
    )
    before = snapshot(tmp_path)
    code, out, _ = run(tmp_path, "--apply")
    assert code == 1
    assert "archive:" not in out
    assert snapshot(tmp_path) == before


def log(project_dir, date):
    path = project_dir / "vault" / "raw" / date / "event_log.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"log of {date}\n", encoding="utf-8")
    return path


def event_log_vault(tmp_path):
    seed(tmp_path, [])
    raw_unit(tmp_path, f"{DATE}/1200", APPLIED)  # the session of the run, on 2026-10-05
    for date in ("2026-10-02", "2026-10-03", "2026-10-04", DATE, "2026-10-06"):
        log(tmp_path, date)
    return tmp_path


def test_event_log_old_logs_move_and_their_empty_folders_go(tmp_path):
    event_log_vault(tmp_path)
    code, out, err = run(tmp_path, "--apply")
    assert code == 0, err
    raw = tmp_path / "vault" / "raw"
    base = tmp_path / "vault" / "archive" / SPRINT
    for date in ("2026-10-02", "2026-10-03"):
        assert (base / date / "event_log.md").read_text(encoding="utf-8") == f"log of {date}\n"
        assert not (raw / date).exists()
        assert f"archive: raw/{date}/event_log.md → archive/{SPRINT}/{date}/event_log.md" in out
    # the day before the session, the session's date and a later date stay
    for date in ("2026-10-04", DATE, "2026-10-06"):
        assert (raw / date / "event_log.md").exists()


def test_event_log_a_taken_target_is_a_stderr_line_and_exit_1(tmp_path):
    event_log_vault(tmp_path)
    taken = tmp_path / "vault" / "archive" / SPRINT / "2026-10-02" / "event_log.md"
    taken.parent.mkdir(parents=True)
    taken.write_text("there\n", encoding="utf-8")
    code, out, err = run(tmp_path, "--apply")
    assert code == 1
    assert err.splitlines() == [
        f"archive: raw/2026-10-02/event_log.md not moved: vault/archive/{SPRINT}/2026-10-02/event_log.md exists"
    ]
    assert (tmp_path / "vault" / "raw" / "2026-10-02" / "event_log.md").exists()
    assert "archive: raw/2026-10-03/event_log.md →" in out  # the other moves still run


def test_event_log_a_refused_close_moves_none(tmp_path):
    event_log_vault(tmp_path)
    (tmp_path / "vault" / "wiki" / "estimates" / "estimate-loose.md").write_text(
        page("estimates", "pending", target="rule-q"), encoding="utf-8"
    )
    before = snapshot(tmp_path)
    code, _, _ = run(tmp_path, "--apply")
    assert code == 1
    assert snapshot(tmp_path) == before
