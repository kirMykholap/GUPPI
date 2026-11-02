---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: Whether guppi check runs every step, guppi ship --check last, when an earlier one is red, prints the lines of each, exits non-zero when any step is red, with --exit-zero prints the exit code on a last line and exits 0 by the function guppi test uses, and skips guppi ship --check where the command ship is missing
method: "uv run --project .guppi pytest .guppi/tests/test_check.py; by hand, at Retro: a Grep of make with the target lint over the live rules, entities and Estimates and over .claude/, read against the Criterion"
checked: 2026-11-02
origin: raw/2026-10-02/1202/ledger.md#case-587
sprint: migration
created: 2026-10-02
tags: [harness, workflow]
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi check` in a project: by hand, in the librarian's run of `.claude/agents/librarian-guppi.md`, or in the job `lint` of `.github/workflows/checks.yml`.
**＋** Or `.claude/skills/work/SKILL.md` runs it with `--exit-zero` as it loads.
**＋** Or `.guppi/tests/test_check.py` runs it in a temporary project whose steps record each call: once with the step `guppi backlog --check` failing, once with every step exiting 0, once with no module `.guppi/guppi/ship.py`, and with `--exit-zero` with a step failing.

Then:
It runs `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint` and `guppi ship --check`, in that order, whether an earlier step exited 0 or not.
**＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
**＋** Without `--exit-zero`, it exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
**＋** With `--exit-zero`, it prints the same lines, then one last line `exit code: <n>`, where n is the exit code of the run without the flag, and it exits 0.
**＋** `guppi check` takes the flag and writes that last line by the function of `.guppi/guppi/commands.py` that `guppi test` and `guppi style` use, and holds no copy of it.
**＋** No live rule, entity or Estimate outside History and Result, and no file of `.claude/`, names make with the target `lint` as the way to run the vault checks.
**－** Where the module `.guppi/guppi/ship.py` is missing, as in a project that installed GUPPI, it runs the other five steps and prints one line that it skips `guppi ship --check`, and that skip sets no exit code.
**－** No step reads the stdin of its caller, and it writes nothing to the tree.

## Result

2026-11-02, Retro of session 1337, on the Criterion of Case 1003.2: uv run --project .guppi pytest .guppi/tests/test_check.py passed, among them a red step with --exit-zero, every step run, the last line exit code: 1 and exit 0, and the test that check.add_exit_zero and check.exit_zero are the functions of commands.py, with no copy in check.py; uv run --project .guppi guppi check --exit-zero in Work Mode printed the three baseline lines and exit code: 1, exit 0; a search for make lint as whole words outside History and Result over the live rules, entities and Estimates and .claude/: 1 hit, the method of estimate-harness-make-runs-in-both-shells, the Estimate of the Makefile's own targets, not the way to run the vault checks

## History

- 2026-10-02 created · [[decision-case-587]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 deferred · [[decision-case-631]]
- 2026-10-05 updated: the Criterion replaced whole — tests run make lint with a fake uv, one whose backlog step is red and one whose steps are all green; the method is those tests, and the defer of case 631 is taken up (case 637.3) · [[decision-case-637.3]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/0109/ledger.md#L2
- 2026-10-14 updated: the Criterion replaced whole — guppi ship --check is the last step of make lint (case 807.2) · [[decision-case-807.2]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L21
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — guppi check runs the vault checks in place of the target lint of the Makefile · [[decision-case-820.1]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1959/ledger.md#L4
- 2026-11-02 updated: the Criterion replaced whole — guppi check takes --exit-zero; purpose and method name it · [[decision-case-1003.2]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/1337/ledger.md#L20
