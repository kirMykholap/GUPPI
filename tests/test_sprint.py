"""`guppi sprint`: `vault/wiki/sprint.md` written from the sprint page, one tick per item
by the status of the page it names (case 209.1, `estimate-sprint-renders-the-backlog`)."""

import io

from guppi import sprint

SPRINT_PAGE = """---
type: entity
kind: MOC
purpose: The repository works by the model
status: draft
estimates: ["[[estimate-sprint-migration-lint-clean]]", "[[estimate-sprint-migration-merges]]"]
origin: raw/2026-09-16/2238/ledger.md#case-209.2
sprint: migration
created: 2026-09-16
tags: [sprint]
---

## Purpose

Open since 2026-09-09. The repository works by the model.

## Backlog

### Slice 3b — Work Mode

- [[rule-work-mode]] — Work Mode, the Spec as tasks
- [[rule-subagent-guppi]] — the subagent and the fork

### Slice 4 — conversion

- [[estimate-sprint-migration-lint-clean]] — lint exit 0

### Slice 5 — closing

- [[rule-old-thing]] — an archived rule
- [[rule-done]] — a rule built

### Slice 6 — nothing yet

## Closed

Slices 0–3d closed by 2026-09-16.

## History

- 2026-09-16 created
"""


def page(props, body="## History\n\n- x\n"):
    front = "\n".join(f"{k}: {v}" for k, v in props.items())
    return f"---\n{front}\n---\n\n{body}"


def seed(tmp_path, sprint_page=SPRINT_PAGE):
    wiki = tmp_path / "vault" / "wiki"
    for category in ("entities", "rules", "estimates"):
        (wiki / category).mkdir(parents=True)
    (wiki / "sprint.md").write_text("# Sprint\n\n## migration — by hand\n", encoding="utf-8")
    (wiki / "entities" / "entity-sprint-migration.md").write_text(
        sprint_page, encoding="utf-8", newline="\n"
    )
    write = lambda category, slug, props: (wiki / category / f"{slug}.md").write_text(
        page(props), encoding="utf-8", newline="\n"
    )
    write(
        "rules",
        "rule-work-mode",
        {
            "type": "rule",
            "status": "draft",
            "deferred_by": '["[[decision-case-183]]", "[[decision-case-206]]"]',
        },
    )
    write("rules", "rule-subagent-guppi", {"type": "rule", "status": "draft"})
    write("rules", "rule-done", {"type": "rule", "status": "built"})
    write(
        "estimates",
        "estimate-sprint-migration-lint-clean",
        {"type": "estimate", "status": "pending", "purpose": "make lint exits 0"},
    )
    write(
        "estimates",
        "estimate-sprint-migration-merges",
        {"type": "estimate", "status": "passed", "purpose": "the branch merged"},
    )
    archive = tmp_path / "vault" / "archive" / "migration" / "2026-09-10" / "rules"
    archive.mkdir(parents=True)
    (archive / "rule-old-thing.md").write_text(
        page({"type": "rule", "status": "archived"}), encoding="utf-8"
    )
    return tmp_path


def run(project_dir):
    out, err = io.StringIO(), io.StringIO()
    code = sprint.run([], stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue(), err.getvalue()


def rendered(project_dir):
    return (project_dir / "vault" / "wiki" / "sprint.md").read_text(encoding="utf-8")


EXPECTED = """# Sprint

## migration

Open since 2026-09-09. The repository works by the model.

**Done when**

- [ ] make lint exits 0 · pending
- [x] the branch merged · passed

## Backlog

### [ ] Slice 3b — Work Mode

- [ ] [[rule-work-mode]] — Work Mode, the Spec as tasks · draft · decision-case-183, decision-case-206
- [ ] [[rule-subagent-guppi]] — the subagent and the fork · draft

### [ ] Slice 4 — conversion

- [ ] [[estimate-sprint-migration-lint-clean]] — lint exit 0 · pending

### [x] Slice 5 — closing

- [x] [[rule-old-thing]] — an archived rule · archived
- [x] [[rule-done]] — a rule built · built

### [ ] Slice 6 — nothing yet

## Closed

Slices 0–3d closed by 2026-09-16.
"""


def test_the_file_is_written_from_the_page_with_one_tick_per_item(tmp_path):
    seed(tmp_path)
    assert run(tmp_path) == (0, "", "")
    assert rendered(tmp_path) == EXPECTED


def test_the_first_heading_keeps_the_sprint_id(tmp_path):
    from guppi.materialize import sprint_id

    seed(tmp_path)
    run(tmp_path)
    assert sprint_id(tmp_path) == "migration"


def test_an_item_without_a_page_is_an_error_and_nothing_is_written(tmp_path):
    seed(tmp_path, SPRINT_PAGE.replace("[[rule-done]]", "[[rule-nowhere]]"))
    code, out, err = run(tmp_path)
    assert code == 1 and out == ""
    assert err.strip() == "sprint: rule-nowhere: no live or archived page"
    assert rendered(tmp_path) == "# Sprint\n\n## migration — by hand\n"


def test_no_sprint_page_is_an_error_and_nothing_is_written(tmp_path):
    seed(tmp_path)
    (tmp_path / "vault" / "wiki" / "entities" / "entity-sprint-migration.md").unlink()
    code, _, err = run(tmp_path)
    assert code == 1 and err.strip() == "sprint: no live entity-sprint-<id> page"
    assert rendered(tmp_path) == "# Sprint\n\n## migration — by hand\n"


def test_the_cli_knows_the_command(monkeypatch, tmp_path, capsys):
    from guppi import cli

    seed(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["sprint"]) == 0
    assert rendered(tmp_path) == EXPECTED
