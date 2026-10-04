"""`guppi backlog`: `vault/wiki/backlog.md` written from the conserved Specs, the pages with
`deferred_by`, the open Insights and the `## Backlog` of the sprint page, each item with its
`purpose` and the count of the sessions that put it off (case 451.4,
`estimate-backlog-renders`); `--check` names the file when it differs and writes nothing
(case 451.5, `estimate-backlog-checks-the-file`)."""

import io

from guppi import backlog

SPRINT_PAGE = """---
type: entity
kind: MOC
purpose: The repository works by the model
status: draft
sprint: migration
created: 2026-09-16
tags: [sprint]
---

## Purpose

The repository works by the model.

## Milestones

### Slice 1 — now

- [[rule-plain]] — a milestone item is no backlog item

## Backlog

- the categories as data of the project
- [[rule-in-backlog]] — a rule without a turn
- [[rule-gone]] — a slug with no page
- [[rule-deferred]] — also deferred by a Case

## Closed

Slice 0 closed.

## History

- 2026-09-16 created
"""

CONSERVED_SPEC = """# Spec — session 1255

## Case 7 — a conserved decision

> **context:**
> x

```then
update:
- slug: rule-conserved
  change: x
```

### Case 7.1 — a sub-case

```then
create:
- slug: rule-new
  type: rule
```

## Deferred

## Case 8 — a short Case

```then
defer:
- slug: insight-conserved
  type: insight
  purpose: put off
```
"""


def page(props, body="## History\n\n- x\n"):
    front = "\n".join(f"{k}: {v}" for k, v in props.items())
    return f"---\n{front}\n---\n\n{body}"


def write_page(project_dir, category, slug, props):
    folder = project_dir / "vault" / "wiki" / category
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{slug}.md").write_text(page(props), encoding="utf-8", newline="\n")


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def seed(tmp_path, sprint_page=SPRINT_PAGE):
    wiki = tmp_path / "vault" / "wiki"
    write(wiki / "entities" / "entity-sprint-migration.md", sprint_page)
    write_page(tmp_path, "rules", "rule-plain", {"type": "rule", "purpose": "plain"})
    write_page(
        tmp_path,
        "rules",
        "rule-deferred",
        {"type": "rule", "purpose": "a rule put off", "deferred_by": '["[[decision-case-3]]"]'},
    )
    write_page(tmp_path, "rules", "rule-in-backlog", {"type": "rule", "purpose": "waits its turn"})
    write_page(
        tmp_path,
        "insights",
        "insight-open",
        {"type": "insight", "status": "open", "pattern": "a pattern seen twice", "severity": 2},
    )
    write_page(
        tmp_path,
        "insights",
        "insight-actioned",
        {"type": "insight", "status": "actioned", "pattern": "fixed", "severity": 0},
    )
    return tmp_path


def frontier(project_dir, relative, *lines):
    write(
        project_dir / "vault" / relative / "frontier.md",
        "# Frontier\n\n## Cases\n\n" + "\n".join(lines) + "\n",
    )


def run(project_dir, *argv):
    out, err = io.StringIO(), io.StringIO()
    code = backlog.run(list(argv), stdout=out, stderr=err, project_dir=project_dir)
    return code, out.getvalue(), err.getvalue()


def target(project_dir):
    return project_dir / "vault" / "wiki" / "backlog.md"


def rendered(project_dir):
    return target(project_dir).read_text(encoding="utf-8")


def snapshot(project_dir):
    """Every file of the vault but `backlog.md`, by its content."""
    return {
        p: p.read_bytes()
        for p in (project_dir / "vault").rglob("*")
        if p.is_file() and p != target(project_dir)
    }


EXPECTED = """# Backlog

5 items

## Conserved Specs

## Deferred

- `rule-deferred` — a rule put off · put off in 0 sessions
- `insight-open` — a pattern seen twice · severity 2 · put off in 0 sessions
- the categories as data of the project · put off in 0 sessions
- `rule-in-backlog` — waits its turn · put off in 0 sessions
- `rule-gone` — a slug with no page · put off in 0 sessions
"""


def test_the_file_holds_each_source_once(tmp_path):
    seed(tmp_path)
    assert run(tmp_path) == (0, "", "")
    assert rendered(tmp_path) == EXPECTED


def test_a_page_without_deferred_by_and_an_insight_not_open_are_no_items(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    text = rendered(tmp_path)
    assert "rule-plain" not in text  # a milestone item, no deferred_by
    assert "insight-actioned" not in text


def test_a_slug_of_two_sources_stands_once(tmp_path):
    seed(tmp_path)  # rule-deferred: deferred_by and a line of the Backlog
    run(tmp_path)
    assert rendered(tmp_path).count("`rule-deferred`") == 1


def test_an_open_insight_with_deferred_by_stands_once_by_its_pattern(tmp_path):
    seed(tmp_path)
    write_page(
        tmp_path,
        "insights",
        "insight-open",
        {
            "type": "insight",
            "status": "open",
            "pattern": "a pattern seen twice",
            "severity": 2,
            "deferred_by": '["[[decision-case-4]]"]',
        },
    )
    run(tmp_path)
    text = rendered(tmp_path)
    assert text.count("`insight-open`") == 1
    assert "- `insight-open` — a pattern seen twice · severity 2 · put off in 0 sessions\n" in text


def test_the_backlog_of_an_archived_sprint_page_stays_beside_the_live_one(tmp_path):
    """Case 628.12: the `## Backlog` of each sprint page, live or under `vault/archive/`; a
    slug of both stands once."""
    seed(tmp_path)
    closed = (
        "---\ntype: entity\nstatus: archived\n---\n\n## Backlog\n\n"
        "- [[rule-in-backlog]] — named by both sprints\n"
        "- the merge of the closed sprint into main\n"
    )
    write(
        tmp_path
        / "vault"
        / "archive"
        / "old"
        / "2026-10-05"
        / "1200"
        / "entities"
        / "entity-sprint-old.md",
        closed,
    )
    assert run(tmp_path) == (0, "", "")
    text = rendered(tmp_path)
    assert text.count("`rule-in-backlog`") == 1
    assert "- the merge of the closed sprint into main · put off in 0 sessions\n" in text
    (tmp_path / "vault" / "wiki" / "entities" / "entity-sprint-migration.md").unlink()
    assert run(tmp_path) == (0, "", "")
    text = rendered(tmp_path)
    assert "- `rule-in-backlog` — waits its turn · put off in 0 sessions\n" in text
    assert "- the merge of the closed sprint into main · put off in 0 sessions\n" in text


def test_no_sprint_page_leaves_the_other_sources(tmp_path):
    seed(tmp_path)
    (tmp_path / "vault" / "wiki" / "entities" / "entity-sprint-migration.md").unlink()
    assert run(tmp_path) == (0, "", "")
    assert rendered(tmp_path).startswith("# Backlog\n\n2 items\n")


# --- the count (case 451.4) ---------------------------------------------------------------


def test_the_count_reads_the_frontiers_of_raw_and_the_archive(tmp_path):
    seed(tmp_path)
    frontier(
        tmp_path,
        "raw/2026-09-20/1000",
        "- [-] C1 — `rule-deferred` put off · sprint · defer",
        "- [-] C2 — `rule-deferred` again, one session · backlog · kept",
        "- [-] C3 — `insight-open` · backlog · kept",
    )
    frontier(
        tmp_path,
        "archive/migration/2026-09-10/0900/raw",
        "- [-] C1 — `rule-deferred` put off · deferred · kept",
    )
    frontier(
        tmp_path,
        "raw/2026-09-21/1100",
        "- [x] C1 — `rule-deferred` decided · case 9",
        "- [ ] C2 — `rule-in-backlog` open",
        "- [-] C3 — the slug only after the title · backlog · `rule-in-backlog`",
    )
    assert run(tmp_path) == (0, "", "")
    text = rendered(tmp_path)
    # raw and the archive, one session however many lines; an [x] line elsewhere counts none
    assert "- `rule-deferred` — a rule put off · put off in 2 sessions\n" in text
    assert "- `insight-open` — a pattern seen twice · severity 2 · put off in 1 session\n" in text
    # an open line and a slug outside the title count nothing
    assert "- `rule-in-backlog` — waits its turn · put off in 0 sessions\n" in text


def test_the_count_is_the_reader_of_the_sprint_move(tmp_path, monkeypatch):
    """One reader of a Frontier line (`rule-one-judgment-one-implementation`): the count
    goes through `generate.frontier_marks`."""
    from guppi import generate

    seed(tmp_path)
    frontier(tmp_path, "raw/2026-09-20/1000", "- [-] C1 — `rule-deferred` · sprint · defer")
    calls = []
    real = generate.frontier_marks
    monkeypatch.setattr(backlog, "frontier_marks", lambda path: calls.append(path) or real(path))
    run(tmp_path)
    assert [p.name for p in calls] == ["frontier.md"]
    assert "put off in 1 session\n" in rendered(tmp_path)


# --- the conserved Specs (case 451.4) -------------------------------------------------------


def test_a_conserved_spec_names_its_cases_and_its_items(tmp_path):
    seed(tmp_path)
    folder = tmp_path / "vault" / "raw" / "2026-09-27" / "1255"
    write(folder / "spec.md", CONSERVED_SPEC)
    write(folder / "carry.md", "carried\n")
    assert run(tmp_path) == (0, "", "")
    text = rendered(tmp_path)
    assert text.startswith("# Backlog\n\n6 items\n\n## Conserved Specs\n\n")
    assert (
        "## Conserved Specs\n\n"
        "- `vault/raw/2026-09-27/1255/spec.md` — Cases 7, 8\n"
        "  - update `rule-conserved` · case 7\n"
        "  - create `rule-new` · case 7.1\n"
        "  - defer `insight-conserved` · case 8\n\n"
        "## Deferred\n\n"
    ) in text


def test_a_slug_under_a_conserved_spec_is_not_repeated_under_deferred(tmp_path):
    seed(tmp_path)
    folder = tmp_path / "vault" / "raw" / "2026-09-27" / "1255"
    write(folder / "spec.md", CONSERVED_SPEC.replace("rule-conserved", "rule-deferred"))
    write(folder / "carry.md", "carried\n")
    run(tmp_path)
    text = rendered(tmp_path)
    assert text.count("`rule-deferred`") == 1
    assert "  - update `rule-deferred` · case 7\n" in text
    assert text.startswith("# Backlog\n\n5 items\n")  # one conserved Spec, four Deferred lines


def test_a_folder_without_carry_shows_nothing(tmp_path):
    seed(tmp_path)
    write(tmp_path / "vault" / "raw" / "2026-09-27" / "1255" / "spec.md", CONSERVED_SPEC)
    assert run(tmp_path) == (0, "", "")
    assert rendered(tmp_path) == EXPECTED


def test_a_conserved_spec_that_does_not_parse_writes_nothing(tmp_path):
    seed(tmp_path)
    folder = tmp_path / "vault" / "raw" / "2026-09-27" / "1255"
    write(folder / "spec.md", CONSERVED_SPEC.replace("update:\n- slug", "update: [\n- slug"))
    write(folder / "carry.md", "carried\n")
    code, out, err = run(tmp_path)
    assert code == 1 and out == ""
    assert err.startswith(
        "backlog: vault/raw/2026-09-27/1255/spec.md: Case 7: then block is not YAML"
    )
    assert not target(tmp_path).exists()


# --- what the script writes -----------------------------------------------------------------


def test_no_file_but_backlog_md_is_written(tmp_path):
    seed(tmp_path)
    folder = tmp_path / "vault" / "raw" / "2026-09-27" / "1255"
    write(folder / "spec.md", CONSERVED_SPEC)
    write(folder / "carry.md", "carried\n")
    write(
        tmp_path / "vault" / "raw" / "2026-09-26" / "1000" / "spec.md",
        "# Spec\n\n## Case 5 — x\n\n```tasks\n- [ ] `uv run guppi backlog`\n```\n",
    )
    before = snapshot(tmp_path)
    assert run(tmp_path)[0] == 0
    assert snapshot(tmp_path) == before
    assert target(tmp_path).is_file()


def test_the_cli_knows_the_command(monkeypatch, tmp_path):
    from guppi import cli

    seed(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    assert cli.main(["backlog"]) == 0
    assert rendered(tmp_path) == EXPECTED


# --- `--check` (case 451.5) -----------------------------------------------------------------


def test_check_names_a_differing_file_and_writes_nothing(tmp_path):
    seed(tmp_path)
    write(target(tmp_path), "# Backlog\n\nby hand\n")
    before = snapshot(tmp_path)
    code, out, err = run(tmp_path, "--check")
    assert (code, err) == (1, "")
    assert out == "backlog: vault/wiki/backlog.md differs from its sources\n"
    assert rendered(tmp_path) == "# Backlog\n\nby hand\n"
    assert snapshot(tmp_path) == before


def test_check_names_a_missing_file_and_writes_nothing(tmp_path):
    seed(tmp_path)
    code, out, _ = run(tmp_path, "--check")
    assert code == 1 and out.strip() == "backlog: vault/wiki/backlog.md differs from its sources"
    assert not target(tmp_path).exists()


def test_check_is_silent_on_the_rendered_file(tmp_path):
    seed(tmp_path)
    run(tmp_path)
    before = rendered(tmp_path)
    assert run(tmp_path, "--check") == (0, "", "")
    assert rendered(tmp_path) == before
