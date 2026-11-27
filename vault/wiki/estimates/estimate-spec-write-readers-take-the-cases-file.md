---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-write]]"
purpose: Whether the pre-spec check, the exit gate of Plan Mode, the check of a Case file and the gate of /retro read the Cases of the plan from the plan file and its Cases file by one function, and whether /pre-spec gives ask-guppi both paths
method: "uv run --project .guppi pytest .guppi/tests/test_ledger.py -k cases_file; by hand, after the librarian's run that renders .claude/skills/pre-spec/SKILL.md: that file read against the Criterion"
origin: raw/2026-11-27/2214/ledger.md#case-1087.13
sprint: plugin
created: 2026-11-27
tags: [hooks, harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan file> --session <stamp>` of `.guppi/guppi/prespec.py` runs, the hook of `rule-prespec-hook` judges an exit from Plan Mode, the `SubagentStop` check `uv run --project .guppi guppi casecheck` of `.guppi/guppi/casecheck.py` reads the other Cases of the session, or `guppi gate` of `.guppi/guppi/gate.py` reads the unwritten items of the session for `/retro`, while the Cases file `<plan stem>.cases.md` stands beside the plan file.
**＋** Or the main agent runs the first `/pre-spec` of a session by `.claude/skills/pre-spec/SKILL.md`.

Then:
Each of those readers reads the Cases of the plan from the plan file and then its Cases file, by `plan_cases_text` of `.guppi/guppi/ledger.py`, imported, never copied.
**＋** A Case that stands only in the Cases file is judged as a Case of the plan: `--check` prints its findings, the exit from Plan Mode is refused on them, a Case file that clashes with it goes back to `case-guppi`, and its item with no decision line is an unwritten item for `/retro`.
**＋** `/pre-spec` dispatches `ask-guppi` with the absolute paths of the plan file and of its Cases file.
**－** With no Cases file, the plan file alone is read, its own Cases included.

## History

- 2026-11-28 created · [[decision-case-1087.13]]
