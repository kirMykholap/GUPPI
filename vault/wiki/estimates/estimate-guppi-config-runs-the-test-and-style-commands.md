---
type: estimate
kind: QA
status: passed
target: "[[rule-guppi-config]]"
purpose: Whether guppi test and guppi style run the commands that the keys test and style of guppi.toml list, in order and each after a red one, exit non-zero when any is red, and exit 1 with one line when the file or the key is missing; and whether the command of the key test runs the tests of .guppi/tests with the settings of .guppi/pyproject.toml whatever the root of the project holds
method: "uv run --project .guppi pytest .guppi/tests/test_commands.py; by hand, after the librarian's run that renders guppi.toml with the key test that names .guppi/tests: uv run --project .guppi guppi test and uv run --project .guppi guppi style in this repository, and a Grep for make test and make style over the live rules, entities and Estimates and over .claude/, read against the Criterion"
checked: 2026-10-30
origin: raw/2026-10-15/0553/ledger.md#case-820.2
sprint: plugin
created: 2026-10-15
tags: [harness, tests]
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi test` or `uv run --project .guppi guppi style` in a project, as `rule-guppi-config` sets it: by hand, in Work Mode, in Retro, or in the jobs `test` and `style` of `.github/workflows/checks.yml`.

Then:
It reads the list of commands of the key `test`, or of the key `style`, from `guppi.toml` at the root of the project.
**＋** It runs each command of the list in order, in the folder of the project and with no shell between, each one even after a red one.
**＋** The output of each command reaches the person whole, and no command gets the stdin of `guppi test` or `guppi style`.
**＋** A single red command makes the run red; the run is green only when all the listed commands pass.
**＋** In this repository, the key `test` holds `uv run --project .guppi pytest -q .guppi/tests`, and the key `style` holds `uv run --project .guppi ruff check .` and `uv run --project .guppi ruff format --check .`.
**＋** That command of `test` runs the tests of `.guppi/tests/` with the settings of `.guppi/pyproject.toml`, the tests marked `live` left out, whether the root of the project holds a `pyproject.toml` of its own or none.
**＋** The rules, entities and Estimates of the vault and the harness files of `.claude/` call the tests and the style check by these two commands, and never by make.
**－** When `guppi.toml` is missing or holds no such key, it prints one line that names the file and the key, runs nothing and exits 1.
**－** The render reads `documentation_lang` and `chat_lang` as before, and a key `test` or `style` does not stop it.

## Result

2026-10-30, the /hi of session 2005: guppi.toml holds test = ["uv run --project .guppi pytest -q .guppi/tests"] and style the two ruff commands; uv run --project .guppi pytest -q .guppi/tests/test_commands.py 8 passed; uv run --project .guppi guppi style exit 0, "All checks passed!" and "100 files already formatted"; uv run --project .guppi guppi test exit 0, 1814 passed, 6 skipped, 1 deselected, with a pyproject.toml of its own at the root; a search for make test, make style and make lint as whole words outside History and Result: 0 hits in .claude/, and over the live rules, entities and Estimates 2 hits, the method of this Estimate, which names the search, and the method of estimate-harness-make-runs-in-both-shells, the Estimate of the Makefile's own targets that case 927 set, read as no call of the tests by make

## History

- 2026-10-15 created · [[decision-case-820.2]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1959/ledger.md#L3
- 2026-10-30 updated: the Criterion replaced whole — the key test names .guppi/tests, and its command runs those tests with the settings of .guppi/pyproject.toml whatever the root holds · [[decision-case-929]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/2005/ledger.md#L1
