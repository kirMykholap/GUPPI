---
type: decision
case: "145.2"
status: archived
update: ["[[rule-harness]]"]
origin: raw/2026-09-14/1633/ledger.md#case-145.2
sprint: migration
created: 2026-09-14
tags: [harness, workflow]
---

## Context

An Insight of severity 2, `open`, two children (2026-09-10, 09-11): the CLI tests held `TODAY = 2026-09-09` while `cli.main` read the real clock — three tests went red the next day; the helper of `test_generate.py` called `generate.run` without `now` — five tests went red a day later on the committed tree. Pattern: a test pins the date on one side of the call and the code reads the real clock on the other; it passes on the day it is written and fails later. Proposal: every entry point that reads the clock takes `now`, every helper passes the pinned date; a run under a shifted date catches the rest of the class.

## Problem

The first half of the Proposal is done in place: all twelve `run()` in `guppi/` take `now=None` and read the clock only there (`datetime.now().astimezone()`); the helpers of ten test files pass `NOW`; `index`, `lint`, `render`, `tail`, `cli` read no clock, `materialize` does not use `now`. The second half does not exist: nothing stops the next helper from forgetting `now` — the error shows again on a later day, not on the day it is written. No Rule on the test suite as a whole exists in the vault; there is no `conftest.py`. Decide: close the class with one fixture file under its own Rule page, or close the Insight as done and wait for a recurrence.

## Given

`insight-tests-clock-not-pinned`: `open`, severity 2, children `lesson-tests-cli-date-pinned`, `lesson-tests-generate-history-date-unpinned`, both `clustered`; both fixes were code repairs recorded in the lesson line itself, no Decision; the cascade of 104.2.
**＋** No live Rule on the test suite; `tests/` appears only in the `implementation_ref` of thirteen Rules; no `conftest.py` (`ask-guppi`). `rule-harness` — MOC, `built`, `children: [rule-render-harness, rule-settings, rule-lint, rule-index, rule-governed-files-hook, rule-claude-md, rule-bash-guard]`, `estimates: [estimate-harness-pipeline]`; a child is added by an `update` of the MOC.
**＋** Code: `archive`, `bashguard`, `cleanup`, `event`, `gate`, `generate`, `guard`, `ledger`, `materialize`, `pretask`, `spec` — `from datetime import datetime`, the clock read only in `run()`: `now = datetime.now().astimezone() if now is None else now`. No other clock read (`date.today`, `time.time`) in `guppi/`.
**＋** Tests: `NOW`/`TODAY` pinned in ten files; `test_materialize`, `test_index`, `test_lint`, `test_render`, `test_tail` pass no `now` — their modules read no clock.
**＋** `Makefile`: `make test` is `uv run pytest -q`; the partial targets `test-session-start`, `test-plan-mode`, `test-documentation`. `rules/schema.md`: a `check` Rule carries `implementation_ref` and an Estimate through `method`.
**＋** No other live lesson about a test reading the real clock; `lesson-generate-walk-history-dated-by-yaml` is about the yaml's date against the run's date, another cause.
**－** The slug `rule-tests-clock-pinned` is free, not in the archive. Tags `tests` ("the harness's own test suite, its fixtures and clocks"), `harness` — in `tags.md`.
**－** An Insight is not a Leaf. No new dependency: a `datetime` subclass and pytest's `monkeypatch`.

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-145.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
