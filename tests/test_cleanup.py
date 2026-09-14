"""`guppi cleanup`: archived pages move to vault/archive/<sprint>/<date>/<HHMM>/<category>/."""

import io
from datetime import UTC, datetime

from guppi import cleanup

NOW = datetime(2026, 9, 10, 12, 0, 0, tzinfo=UTC)
DATE = "2026-09-10"


def page(category, slug, status="draft", **extra):
    lines = [f"type: {category[:-1] if category != 'entities' else 'entity'}", f"status: {status}"]
    lines += [f"{k}: {v}" for k, v in extra.items()]
    body = "\n".join(lines)
    return f"---\n{body}\n---\n\n## Purpose\n\n{slug}\n\n## History\n\n- 2026-09-09 created · x\n"


def seed(tmp_path, pages):
    wiki = tmp_path / "vault" / "wiki"
    for category in ("rules", "estimates", "lessons", "insights", "entities", "decisions"):
        (wiki / category).mkdir(parents=True)
    (wiki / "sprint.md").write_text("# Sprint\n\n## migration — open\n", encoding="utf-8")
    (wiki / "log.md").write_text("# Log\n", encoding="utf-8")
    for category, slug, text in pages:
        (wiki / category / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")
    return tmp_path


def run(project_dir):
    out, err = io.StringIO(), io.StringIO()
    code = cleanup.run([], stdout=out, stderr=err, project_dir=project_dir, now=NOW)
    return code, out.getvalue(), err.getvalue()


def archived(project_dir, category, slug):
    return project_dir / "vault" / "archive" / "migration" / DATE / category / f"{slug}.md"


def test_archived_pages_move_with_a_history_line_and_leave_the_lists(tmp_path):
    seed(
        tmp_path,
        [
            (
                "rules",
                "rule-root",
                page(
                    "rules",
                    "rule-root",
                    kind="MOC",
                    children="[rule-a, rule-b]",
                    estimates="[estimate-root]",
                ).replace(
                    "## History",
                    "## Children\n\n1. [[rule-a]]\n2. [[rule-b]]\n\n## Estimates\n\n- [[estimate-root]]\n\n## History",
                ),
            ),
            ("rules", "rule-a", page("rules", "rule-a", status="archived", parent="rule-root")),
            ("rules", "rule-b", page("rules", "rule-b", parent="rule-root")),
            (
                "estimates",
                "estimate-root",
                page("estimates", "estimate-root", status="archived", target="rule-root"),
            ),
            ("lessons", "lesson-x", page("lessons", "lesson-x", status="archived")),
            (
                "insights",
                "insight-x",
                page("insights", "insight-x", children="[lesson-x]", severity="1"),
            ),
        ],
    )
    code, out, err = run(tmp_path)
    assert code == 0 and err == "" and "3 page(s) moved" in out
    moved = archived(tmp_path, "rules", "rule-a")
    assert moved.exists() and not (tmp_path / "vault" / "wiki" / "rules" / "rule-a.md").exists()
    assert f"- {DATE} archived · cleanup" in moved.read_text(encoding="utf-8")
    assert archived(tmp_path, "estimates", "estimate-root").exists()
    root = (tmp_path / "vault" / "wiki" / "rules" / "rule-root.md").read_text(encoding="utf-8")
    assert 'children: ["[[rule-b]]"]' in root and "estimates: []" in root
    assert "## Estimates\n\n## Children\n\n1. [[rule-b]]\n\n## History" in root
    assert (
        f"- {DATE} child rule-a archived · cleanup" in root
        and f"- {DATE} estimate estimate-root archived · cleanup" in root
    )
    insight = (tmp_path / "vault" / "wiki" / "insights" / "insight-x.md").read_text(
        encoding="utf-8"
    )
    assert "children: [lesson-x]" in insight  # untouched by cleanup: the bare form stays
    log = (tmp_path / "vault" / "wiki" / "log.md").read_text(encoding="utf-8")
    assert f"- {DATE} rules/rule-a archived · cleanup" in log
    assert not (tmp_path / "vault" / "wiki" / "rules-index.md").exists()  # no index (147.6)


def test_a_page_whose_status_left_archived_comes_back(tmp_path):
    seed(tmp_path, [("rules", "rule-a", page("rules", "rule-a", status="archived"))])
    run(tmp_path)
    moved = archived(tmp_path, "rules", "rule-a")
    moved.write_text(
        moved.read_text(encoding="utf-8").replace("status: archived", "status: draft"),
        encoding="utf-8",
    )
    code, out, _ = run(tmp_path)
    assert code == 0 and "1 page(s) moved" in out
    back = tmp_path / "vault" / "wiki" / "rules" / "rule-a.md"
    assert back.exists() and not moved.exists()
    assert f"- {DATE} restored · cleanup" in back.read_text(encoding="utf-8")


# --- the session of the run (case 102.2) --------------------------------------------------


def with_session(tmp_path, date, hhmm):
    (tmp_path / "vault" / "raw" / date / hhmm).mkdir(parents=True, exist_ok=True)


def test_a_page_lands_under_the_latest_session_of_the_run_day(tmp_path):
    seed(tmp_path, [("rules", "rule-a", page("rules", "rule-a", status="archived"))])
    with_session(tmp_path, DATE, "0454")
    with_session(tmp_path, DATE, "1156")
    with_session(tmp_path, "2026-09-11", "0900")  # a later date is never the run's
    code, out, _ = run(tmp_path)
    assert code == 0 and "1 page(s) moved" in out
    moved = tmp_path / "vault" / "archive" / "migration" / DATE / "1156" / "rules" / "rule-a.md"
    assert moved.exists()
    assert not archived(tmp_path, "rules", "rule-a").exists()


def test_without_a_session_today_the_nearest_date_back_names_the_session(tmp_path):
    seed(tmp_path, [("rules", "rule-a", page("rules", "rule-a", status="archived"))])
    with_session(tmp_path, "2026-09-08", "0700")
    with_session(tmp_path, "2026-09-09", "2350")  # the session that crossed midnight
    run(tmp_path)
    moved = tmp_path / "vault" / "archive" / "migration" / DATE / "2350" / "rules" / "rule-a.md"
    assert moved.exists()


def test_a_page_restores_from_the_session_depth(tmp_path):
    seed(tmp_path, [("rules", "rule-a", page("rules", "rule-a", status="archived"))])
    with_session(tmp_path, DATE, "1156")
    run(tmp_path)
    moved = tmp_path / "vault" / "archive" / "migration" / DATE / "1156" / "rules" / "rule-a.md"
    moved.write_text(
        moved.read_text(encoding="utf-8").replace("status: archived", "status: draft"),
        encoding="utf-8",
    )
    code, out, _ = run(tmp_path)
    assert code == 0 and "1 page(s) moved" in out
    assert (tmp_path / "vault" / "wiki" / "rules" / "rule-a.md").exists() and not moved.exists()


def test_a_rerun_moves_nothing_and_a_dangling_parent_is_flagged(tmp_path):
    seed(
        tmp_path,
        [
            (
                "rules",
                "rule-root",
                page("rules", "rule-root", status="archived", kind="MOC", children="[rule-b]"),
            ),
            ("rules", "rule-b", page("rules", "rule-b", parent="rule-root")),
        ],
    )
    code, out, err = run(tmp_path)
    assert code == 0 and "1 page(s) moved" in out
    assert "rules/rule-b: parent rule-root is archived" in err
    code, out, _ = run(tmp_path)
    assert code == 0 and "0 page(s) moved" in out


def test_a_taken_name_in_the_archive_is_an_error_and_the_rest_still_move(tmp_path):
    seed(
        tmp_path,
        [
            ("rules", "rule-a", page("rules", "rule-a", status="archived")),
            ("rules", "rule-b", page("rules", "rule-b", status="archived")),
        ],
    )
    taken = archived(tmp_path, "rules", "rule-a")
    taken.parent.mkdir(parents=True)
    taken.write_text("old", encoding="utf-8")
    code, out, err = run(tmp_path)
    assert code == 1 and "rule-a" in err and "exists already" in err
    assert archived(tmp_path, "rules", "rule-b").exists() and "1 page(s) moved" in out
    assert (tmp_path / "vault" / "wiki" / "rules" / "rule-a.md").exists()


def test_cli_dispatches_to_cleanup(tmp_path, monkeypatch, capsys):
    from guppi import cli

    seed(tmp_path, [])
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["cleanup"]) == 0
    assert "0 page(s) moved" in capsys.readouterr().out
