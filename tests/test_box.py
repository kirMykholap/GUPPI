"""`guppi box --check`: whether a conserved Spec can run now (case 593.3), and the judgment
whether an approved plan names one (case 591.3). Rule page: `vault/wiki/rules/rule-spec-box.md`.

Every test builds a temp repository with git, a conserved session folder and the session's
event log, the shapes `/carry` and `/hi` leave.
"""

import io
import subprocess
from datetime import UTC, datetime

import pytest

from guppi import box

NOW = datetime(2026, 9, 9, 18, 40, 5, tzinfo=UTC)
SESSION = "44c1aae1"
UNIT = "2026-09-01/0900"
EVENT_LOG = "- 15:01:00 44c1aae1 session-start startup\n- 15:01:30 44c1aae1 hi\n"

SPEC = """<!-- approved 09:30:00 · session 11111111 -->

# Spec — session 0900, 2026-09-01

## Case 100 — the change

> **context:**
> Something.

```then
update:
  - slug: rule-x
    change: one line
create:
  - slug: estimate-x-new
    type: estimate
    ref: rule-x
```

### Case 100.1 — a part

```then
update:
  - slug: rule-y
    change: one line
```

## Deferred

## Case 101 — later

> **context:**
> Later.

```then
defer:
  - slug: rule-z
    type: rule
    purpose: later
```
"""

PAGE = """---
type: rule
---

## Purpose

The rule.

## History

- 2026-08-30 created · [[decision-case-99]]
"""


def git(path, *args):
    subprocess.run(["git", *args], cwd=path, check=True, capture_output=True)


@pytest.fixture
def repo(tmp_path):
    git(tmp_path, "init", "-q", "-b", "main")
    git(tmp_path, "config", "user.email", "t@example.com")
    git(tmp_path, "config", "user.name", "t")
    folder = tmp_path / "vault" / "raw" / "2026-09-01" / "0900"
    folder.mkdir(parents=True)
    (folder / "carry.md").write_text("conserved\n", encoding="utf-8")
    (folder / "spec.md").write_text(SPEC, encoding="utf-8")
    rules = tmp_path / "vault" / "wiki" / "rules"
    rules.mkdir(parents=True)
    for slug in ("rule-x", "rule-y", "rule-z"):
        (rules / f"{slug}.md").write_text(PAGE, encoding="utf-8")
    today = tmp_path / "vault" / "raw" / "2026-09-09"
    (today / "1501").mkdir(parents=True)
    (today / "event_log.md").write_text(EVENT_LOG, encoding="utf-8")
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-q", "-m", "seed")
    git(tmp_path, "branch", "spec/2026-09-01-0900")
    git(tmp_path, "switch", "-q", "-c", "migration")
    return tmp_path


def reasons(repo):
    return box.check(repo, repo / "vault" / "raw" / "2026-09-01" / "0900", SESSION, NOW)


def ledger(repo, *lines):
    path = repo / "vault" / "raw" / "2026-09-09" / "1501" / "ledger.md"
    path.write_text("".join(f"- 15:30:00 {line}\n" for line in lines), encoding="utf-8")


def history(repo, slug, line):
    page = repo / "vault" / "wiki" / "rules" / f"{slug}.md"
    page.write_text(page.read_text(encoding="utf-8") + line + "\n", encoding="utf-8")


def test_a_clean_folder_gives_no_reason_and_exit_0(repo):
    out = io.StringIO()
    argv = ["--check", f"vault/raw/{UNIT}", "--session", SESSION]
    assert box.run(argv, stdout=out, project_dir=repo, now=NOW) == 0
    assert out.getvalue() == ""


def test_a_folder_without_carry_is_a_reason(repo):
    (repo / "vault" / "raw" / "2026-09-01" / "0900" / "carry.md").unlink()
    assert reasons(repo) == [
        "box: vault/raw/2026-09-01/0900/ holds no carry.md — no conserved Spec"
    ]


def test_a_folder_without_its_branch_is_a_reason(repo):
    git(repo, "branch", "-D", "spec/2026-09-01-0900")
    assert reasons(repo) == ["box: no branch spec/2026-09-01-0900"]


def test_a_run_from_main_is_a_reason(repo):
    git(repo, "switch", "-q", "main")
    assert reasons(repo) == ["box: the current branch is main — the shared branch never is"]


def test_a_decision_line_of_the_session_is_a_reason_and_a_defer_is_not(repo):
    ledger(repo, "decision[case 7][defer][rule-later]")
    assert reasons(repo) == []
    ledger(
        repo, "decision[case 7][defer][rule-later]", "decision[case 8][update][rule-q]{ref:rule-q}"
    )
    own = "box: case 8 of this session holds a decision line — a box session ratifies no Case"
    assert reasons(repo) == [own + " of its own"]


def test_a_page_changed_by_a_later_case_is_a_reason(repo):
    history(repo, "rule-y", "- 2026-09-05 updated: more · [[decision-case-102.1]]")
    assert reasons(repo) == [
        "box: rule-y — changed after the Spec was conserved, by decision-case-102"
    ]


def test_a_history_line_of_the_spec_itself_or_a_cascade_line_is_not_counted(repo):
    history(repo, "rule-x", "- 2026-09-05 updated: one line · [[decision-case-100]]")
    history(repo, "rule-z", "- 2026-09-05 deferred · [[decision-case-101]]")
    history(repo, "rule-x", "- 2026-09-06 status: draft → built · cascade")
    assert reasons(repo) == []


def test_a_slug_the_spec_creates_that_a_live_page_carries_is_a_reason(repo):
    estimates = repo / "vault" / "wiki" / "estimates"
    estimates.mkdir()
    (estimates / "estimate-x-new.md").write_text(PAGE, encoding="utf-8")
    assert reasons(repo) == [
        "box: estimate-x-new — the Spec creates it, and a live page carries it"
    ]


def test_the_check_writes_nothing_and_switches_no_branch(repo):
    history(repo, "rule-y", "- 2026-09-05 updated: more · [[decision-case-102]]")
    before = subprocess.run(
        ["git", "status", "--porcelain"], cwd=repo, capture_output=True, text=True, check=False
    ).stdout
    out = io.StringIO()
    argv = ["--check", f"vault/raw/{UNIT}", "--session", SESSION]
    assert box.run(argv, stdout=out, project_dir=repo, now=NOW) == 1
    after = subprocess.run(
        ["git", "status", "--porcelain"], cwd=repo, capture_output=True, text=True, check=False
    ).stdout
    branch = subprocess.run(
        ["git", "branch", "--show-current"], cwd=repo, capture_output=True, text=True, check=False
    ).stdout.strip()
    assert before == after and branch == "migration"


def test_a_plan_names_a_conserved_spec_by_its_title_line(repo):
    plan = f"# Session 1501 — runs the conserved Spec vault/raw/{UNIT}/spec.md\n"
    assert box.conserved_spec_named(plan, repo) == repo / "vault" / "raw" / "2026-09-01" / "0900"
    assert box.conserved_spec_named("# Spec — session 1501\n", repo) is None
    (repo / "vault" / "raw" / "2026-09-01" / "0900" / "carry.md").unlink()
    assert box.conserved_spec_named(plan, repo) is None
