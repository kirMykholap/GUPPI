"""`guppi tail`: every ledger line under raw/ that its yaml does not name (case 101.2)."""

import io

import yaml

from guppi import tail

DATE = "2026-09-10"


def ledger(tmp_path, unit, text, data=None):
    folder = tmp_path / "vault" / "raw" / unit
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "ledger.md").write_text(text, encoding="utf-8", newline="\n")
    if data is not None:
        (folder / "materialize.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
    return folder


def run(project_dir):
    out, err = io.StringIO(), io.StringIO()
    code = tail.run([], stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue().splitlines(), err.getvalue().splitlines()


COVERED = (
    "- 09:00:00 decision[case 1][create][rule-a]\n- 09:00:01 estimate[estimate-a][passed] ok\n"
)
SESSION = (
    "- 16:00:00 decision[case 2][update][rule-a]\n"
    "- 16:00:01 estimate[estimate-a][failed] red after the librarian\n"
    "- 16:00:02 lesson[error][lesson-late]{tags:x} trigger: t root_cause: r\n"
    "- 16:00:03 estimate[estimate-a] outside the grammar\n"
)
ALONE = "- 17:00:00 decision[case 3][defer][rule-b]\n"


def test_the_uncovered_lines_print_in_unit_order_with_their_form(tmp_path):
    ledger(tmp_path, DATE, COVERED, {"entries": [{"line": 1, "folded": [2]}]})
    ledger(tmp_path, f"{DATE}/1610", SESSION, {"entries": [{"line": 1}], "unparsed": []})
    ledger(tmp_path, f"{DATE}/1800", ALONE)  # no yaml: every record line
    code, out, err = run(tmp_path)
    assert (code, err) == (0, [])
    assert out == [
        f"{DATE}/1610 L2: - 16:00:01 estimate[estimate-a][failed] red after the librarian",
        f"{DATE}/1610 L3: - 16:00:02 lesson[error][lesson-late]{{tags:x}} trigger: t root_cause: r",
        f"{DATE}/1800 L1: - 17:00:00 decision[case 3][defer][rule-b]",
    ]


def test_an_empty_tail_prints_nothing(tmp_path):
    ledger(tmp_path, DATE, COVERED, {"entries": [{"line": 1, "folded": [2]}]})
    assert run(tmp_path) == (0, [], [])
    assert run(tmp_path / "nowhere") == (0, [], [])


def test_an_unreadable_yaml_is_a_stderr_line_and_the_walk_goes_on(tmp_path):
    folder = ledger(tmp_path, f"{DATE}/0900", ALONE)
    (folder / "materialize.yaml").mkdir()  # a folder where the yaml should be
    ledger(tmp_path, f"{DATE}/1800", ALONE)
    code, out, err = run(tmp_path)
    assert code == 0
    assert out == [f"{DATE}/1800 L1: - 17:00:00 decision[case 3][defer][rule-b]"]
    assert len(err) == 1 and err[0].startswith(f"tail: raw/{DATE}/0900: ")


def test_cli_dispatches_to_tail(tmp_path, monkeypatch, capsys):
    from guppi import cli

    ledger(tmp_path, f"{DATE}/1800", ALONE)
    monkeypatch.setattr(tail, "project_root", lambda: tmp_path)
    assert cli.main(["tail"]) == 0
    assert capsys.readouterr().out.splitlines() == [
        f"{DATE}/1800 L1: - 17:00:00 decision[case 3][defer][rule-b]"
    ]
