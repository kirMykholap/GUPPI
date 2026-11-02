---
type: estimate
kind: QA
status: passed
target: "[[rule-guppi-config]]"
purpose: Whether guppi test and guppi style run the commands that the keys test and style of guppi.toml list, in order and each after a red one, exit non-zero when any is red, and exit 1 with one line when the file or the key is missing; whether with --exit-zero they print the exit code on a last line and exit 0; and whether the command of the key test runs the tests of .guppi/tests with the settings of .guppi/pyproject.toml whatever the root of the project holds
method: "uv run --project .guppi pytest .guppi/tests/test_commands.py; by hand, at Retro: uv run --project .guppi guppi test --exit-zero and uv run --project .guppi guppi style --exit-zero in this repository, their last lines and exit codes read, and a Grep for make test and make style over the live rules, entities and Estimates and over .claude/, read against the Criterion"
checked: 2026-11-02
origin: raw/2026-10-15/0553/ledger.md#case-820.2
sprint: plugin
created: 2026-10-15
tags: [harness, tests]
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi test` or `uv run --project .guppi guppi style` in a project, as `rule-guppi-config` sets it: by hand, in Work Mode, in Retro, or in the jobs `test` and `style` of `.github/workflows/checks.yml`.
**＋** Or `.claude/skills/work/SKILL.md` or `.claude/skills/retro/SKILL.md` runs one of them with `--exit-zero` as it loads.

Then:
It reads the list of commands of the key `test`, or of the key `style`, from `guppi.toml` at the root of the project.
**＋** It runs each command of the list in order, in the folder of the project and with no shell between, each one even after a red one.
**＋** The output of each command reaches the person whole, and no command gets the stdin of `guppi test` or `guppi style`.
**＋** Without `--exit-zero`, a single red command makes the run red, and the run is green only when all the listed commands pass.
**＋** With `--exit-zero`, it prints the same lines, then one last line `exit code: <n>`, where n is the exit code of the run without the flag, and it exits 0.
**＋** In this repository, the key `test` holds `uv run --project .guppi pytest -q .guppi/tests`, and the key `style` holds `uv run --project .guppi ruff check .` and `uv run --project .guppi ruff format --check .`; that command of `test` runs the tests of `.guppi/tests/` with the settings of `.guppi/pyproject.toml`, the tests marked `live` left out, whether the root of the project holds a `pyproject.toml` of its own or none.
**＋** The rules, entities and Estimates of the vault and the harness files of `.claude/` call the tests and the style check by these two commands, and never by make.
**－** When `guppi.toml` is missing or holds no such key, it prints one line that names the file and the key, runs nothing and exits 1; with `--exit-zero` it prints the line `exit code: 1` after it and exits 0.
**－** The render reads `documentation_lang` and `chat_lang` as before, and a key `test` or `style` does not stop it.

## Result

2026-11-02, Retro of session 1337, on the Criterion of Case 1003.1: uv run --project .guppi pytest .guppi/tests/test_commands.py .guppi/tests/test_check.py 20 passed, among them a red run, a green run and a missing key with --exit-zero each printing the last line exit code: <n> and exiting 0; uv run --project .guppi guppi test --exit-zero: 1896 passed, 6 skipped, 1 deselected, last line exit code: 0, exit 0; uv run --project .guppi guppi style --exit-zero: last line exit code: 0, exit 0; without the flag both exit 0 on a green tree; a search for make test, make style and make lint as whole words outside History and Result: 0 hits in .claude/, and over the live rules, entities and Estimates 2 hits, the method of this Estimate, which names the search, and the method of estimate-harness-make-runs-in-both-shells, the Estimate of the Makefile's own targets, read as no call of the tests by make

## History

- 2026-10-15 created · [[decision-case-820.2]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1959/ledger.md#L3
- 2026-10-30 updated: the Criterion replaced whole — the key test names .guppi/tests, and its command runs those tests with the settings of .guppi/pyproject.toml whatever the root holds · [[decision-case-929]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/2005/ledger.md#L1
- 2026-11-02 updated: the Criterion replaced whole — guppi test and guppi style take --exit-zero; purpose and method name it · [[decision-case-1003.1]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/1337/ledger.md#L19
