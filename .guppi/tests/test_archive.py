"""`guppi archive`: an applied unit of raw/ moves whole into vault/archive/<sprint>/ (case 100.1)."""

import io
from datetime import UTC, datetime

import yaml

from guppi import archive

NOW = datetime(2026, 9, 13, 12, 0, 0, tzinfo=UTC)
TODAY = "2026-09-13"
LEDGER = "- 10:00:00 decision[case 1][create][rule-a]\n- 10:00:01 estimate[estimate-a][passed] ok\n"


def entries(*marks):
    out = []
    for number, mark in enumerate(marks, 1):
        entry = {"line": number, "kind": "create", "slug": f"rule-{number}"}
        entry.update(mark)
        out.append(entry)
    return out


def unit(
    tmp_path, date, session=None, ledger=LEDGER, yaml_entries=None, extra=(), sprint="migration"
):
    folder = tmp_path / "vault" / "raw" / date
    if session:
        folder = folder / session
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "ledger.md").write_text(ledger, encoding="utf-8", newline="\n")
    if yaml_entries is not None:
        data = {"date": date, "entries": yaml_entries, "unparsed": []}
        if sprint is not None:
            data["sprint"] = sprint
        (folder / "materialize.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
    for name in extra:
        (folder / name).write_text(name, encoding="utf-8")
    return folder


APPLIED = entries({"applied": "10:00"}, {"applied": "10:00"})


def seed(tmp_path, today_session=True):
    wiki = tmp_path / "vault" / "wiki"
    wiki.mkdir(parents=True)
    (wiki / "sprint.md").write_text("# Sprint\n\n## migration — open\n", encoding="utf-8")
    if today_session:  # the session of the run is today's; without one it is the latest back
        (tmp_path / "vault" / "raw" / TODAY / "0700").mkdir(parents=True)
    return tmp_path


def run(project_dir):
    out, err = io.StringIO(), io.StringIO()
    code = archive.run([], stdout=out, stderr=err, project_dir=project_dir, now=NOW)
    return code, out.getvalue().splitlines(), err.getvalue().splitlines()


def archived(tmp_path, *parts):
    return tmp_path / "vault" / "archive" / "migration" / "/".join(parts)


def test_done_units_move_whole_and_the_others_stay_with_a_reason(tmp_path):
    seed(tmp_path)
    # a date-level unit, applied and covered, with a session folder without a ledger
    day = unit(tmp_path, "2026-09-10", yaml_entries=APPLIED, extra=("spec.md", "event_log.md"))
    (day / "1156").mkdir()
    (day / "1156" / "spec.md").write_text("# Spec\n", encoding="utf-8")
    # a session unit, applied and covered
    unit(tmp_path, "2026-09-11", "0900", yaml_entries=APPLIED, extra=("spec.md", "frontier.md"))
    (tmp_path / "vault" / "raw" / "2026-09-11" / "event_log.md").write_text("", encoding="utf-8")
    # a session with a failed entry; one with a record line outside its yaml; one dated today
    unit(tmp_path, "2026-09-11", "1400", yaml_entries=entries({"applied": "x"}, {"failed": "boom"}))
    unit(tmp_path, "2026-09-12", "0800", yaml_entries=entries({"applied": "x"}))
    unit(tmp_path, TODAY, "0700", yaml_entries=APPLIED)
    (tmp_path / "vault" / "raw" / "notes").mkdir()  # no ledger: not a unit
    code, out, err = run(tmp_path)
    assert (code, err) == (0, [])
    assert out == [
        "archive: raw/2026-09-10 → archive/migration/2026-09-10/raw",
        "archive: raw/2026-09-11/0900 → archive/migration/2026-09-11/0900/raw",
        "archive: raw/2026-09-11/1400 kept: 1 entries not applied",
        "archive: raw/2026-09-12/0800 kept: 1 ledger lines outside the yaml",
    ]
    assert archived(tmp_path, "2026-09-10", "raw", "ledger.md").exists()
    assert archived(tmp_path, "2026-09-10", "raw", "materialize.yaml").exists()
    assert archived(tmp_path, "2026-09-10", "raw", "spec.md").exists()
    assert archived(tmp_path, "2026-09-10", "1156", "raw", "spec.md").exists()
    assert archived(tmp_path, "2026-09-11", "0900", "raw", "frontier.md").exists()
    raw = tmp_path / "vault" / "raw"
    assert sorted(p.name for p in (raw / "2026-09-10").iterdir()) == ["event_log.md"]
    assert sorted(p.name for p in (raw / "2026-09-11").iterdir()) == ["1400", "event_log.md"]
    assert (raw / "2026-09-12" / "0800" / "ledger.md").exists()
    assert (raw / TODAY / "0700" / "ledger.md").exists()
    # a rerun moves nothing
    code, out, err = run(tmp_path)
    assert (code, err) == (0, [])
    assert not any("→" in line for line in out)


def test_the_session_of_the_run_never_moves_even_when_dated_yesterday(tmp_path):
    seed(tmp_path, today_session=False)
    unit(tmp_path, "2026-09-12", "2350", yaml_entries=APPLIED)  # hi yesterday, run today
    unit(tmp_path, "2026-09-12", "0800", yaml_entries=APPLIED)
    code, out, _ = run(tmp_path)
    assert code == 0
    assert out == ["archive: raw/2026-09-12/0800 → archive/migration/2026-09-12/0800/raw"]
    assert (tmp_path / "vault" / "raw" / "2026-09-12" / "2350" / "ledger.md").exists()


def test_a_unit_without_a_yaml_or_with_a_superseded_entry(tmp_path):
    seed(tmp_path)
    unit(tmp_path, "2026-09-10", "0900")
    unit(
        tmp_path,
        "2026-09-10",
        "1000",
        yaml_entries=entries({"applied": "x"}, {"superseded_by": "decision-case-9"}),
    )
    code, out, _ = run(tmp_path)
    assert code == 0
    assert out == [
        "archive: raw/2026-09-10/0900 kept: no yaml",
        "archive: raw/2026-09-10/1000 → archive/migration/2026-09-10/1000/raw",
    ]


def test_a_taken_name_in_the_archive_is_a_stderr_line_and_the_rest_moves(tmp_path):
    seed(tmp_path)
    unit(tmp_path, "2026-09-10", "0900", yaml_entries=APPLIED)
    unit(tmp_path, "2026-09-10", "1000", yaml_entries=APPLIED)
    taken = archived(tmp_path, "2026-09-10", "0900", "raw")
    taken.mkdir(parents=True)
    code, out, err = run(tmp_path)
    assert code == 1
    assert err == [
        "archive: raw/2026-09-10/0900 not moved: vault/archive/migration/2026-09-10/0900/raw exists"
    ]
    assert out == ["archive: raw/2026-09-10/1000 → archive/migration/2026-09-10/1000/raw"]
    assert (tmp_path / "vault" / "raw" / "2026-09-10" / "0900" / "ledger.md").exists()


def test_a_date_level_unit_leaves_a_session_with_its_own_ledger_behind(tmp_path):
    seed(tmp_path)
    day = unit(tmp_path, "2026-09-10", yaml_entries=APPLIED)
    unit(tmp_path, "2026-09-10", "1610", yaml_entries=entries({"failed": "x"}, {"applied": "y"}))
    code, out, _ = run(tmp_path)
    assert code == 0
    assert out == [
        "archive: raw/2026-09-10 → archive/migration/2026-09-10/raw",
        "archive: raw/2026-09-10/1610 kept: 1 entries not applied",
    ]
    assert (day / "1610" / "ledger.md").exists()
    assert not (day / "ledger.md").exists()


def test_sprint_of_the_unit_yaml_names_the_archive_folder(tmp_path):
    """A unit goes under the sprint its own yaml records, not that of sprint.md (case 743.2)."""
    seed(tmp_path)
    (tmp_path / "vault" / "wiki" / "sprint.md").write_text(
        "# Sprint\n\n## b — open\n", encoding="utf-8"
    )
    unit(tmp_path, "2026-09-10", "0900", yaml_entries=APPLIED, sprint="a")
    code, out, err = run(tmp_path)
    assert (code, err) == (0, [])
    assert out == ["archive: raw/2026-09-10/0900 → archive/a/2026-09-10/0900/raw"]
    assert (
        tmp_path / "vault" / "archive" / "a" / "2026-09-10" / "0900" / "raw" / "ledger.md"
    ).exists()
    assert not (tmp_path / "vault" / "archive" / "b").exists()


def test_sprint_of_sprint_md_when_the_unit_yaml_records_none(tmp_path):
    seed(tmp_path)
    (tmp_path / "vault" / "wiki" / "sprint.md").write_text(
        "# Sprint\n\n## b — open\n", encoding="utf-8"
    )
    unit(tmp_path, "2026-09-10", "0900", yaml_entries=APPLIED, sprint=None)
    code, out, _ = run(tmp_path)
    assert code == 0
    assert out == ["archive: raw/2026-09-10/0900 → archive/b/2026-09-10/0900/raw"]
    assert (
        tmp_path / "vault" / "archive" / "b" / "2026-09-10" / "0900" / "raw" / "ledger.md"
    ).exists()


def test_uncovered_lines_reads_line_folded_and_unparsed(tmp_path):
    seed(tmp_path)
    ledger = (
        "- 10:00:00 decision[case 1][create][rule-a]\n"
        "- 10:00:01 estimate[estimate-a][passed] folded into the create\n"
        "- 10:00:02 lesson[error][lesson-b]{tags:x} trigger: t root_cause: r\n"
        "not a record line\n"
        "- 10:00:04 decision[case 2][update][rule-a]\n"
        "- 10:00:05 estimate[estimate-a] broken\n"
    )
    folder = unit(tmp_path, "2026-09-10", "0900", ledger=ledger)
    data = {
        "entries": [{"line": 1, "folded": [2]}, {"line": 3}],
        "unparsed": [{"line": 6, "text": "estimate[estimate-a] broken"}],
    }
    (folder / "materialize.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
    assert archive.uncovered_lines(tmp_path, "2026-09-10/0900") == [
        (5, "- 10:00:04 decision[case 2][update][rule-a]")
    ]


def test_cli_dispatches_to_archive(tmp_path, monkeypatch, capsys):
    from guppi import cli

    seed(tmp_path)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(archive, "project_root", lambda: tmp_path)
    assert cli.main(["archive"]) == 0
    assert capsys.readouterr().out == ""
