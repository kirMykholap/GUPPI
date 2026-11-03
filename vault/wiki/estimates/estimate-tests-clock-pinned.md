---
type: estimate
kind: QA
status: passed
target: "[[rule-tests-clock-pinned]]"
purpose: "A test that leaves the code on the real clock fails on the day it is written: every guppi module's clock is pinned to 2001 by one autouse fixture"
method: pytest .guppi/tests/test_conftest.py, plus uv run --project .guppi guppi test green under the fixture
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [tests, harness]
core: true
---

## Criterion

When:
`pytest` collects `.guppi/tests/`, and a test calls the `run()` of a module of `.guppi/guppi/` without `now`, or the code reads the clock outside `run()`.

Then:
Before every test, an autouse fixture in `.guppi/tests/conftest.py` sets into every module of `.guppi/guppi/` that carries a `datetime` attribute a subclass whose `now(tz=None)` returns `2001-01-01 00:00:00 UTC`, and `astimezone` gives the same second. A test that leaves the code on the real clock sees the year 2001 and fails on the day it is written.
**＋** The list of modules comes from a walk over `.guppi/guppi/`, never from a hand list: a new module with a clock is covered with no change to the fixture.
**＋** `.guppi/tests/test_conftest.py` shows it: a `run()` without `now` writes a time dated 2001, and `datetime.strptime`, `fromisoformat` and the constructor of the subclass work as before.
**＋** Each run of the tests of `.guppi/tests/` under pytest runs under the same fixture, whatever command starts it.
**－** A test that passes `now` does not notice the fixture: `run()` reads no clock.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
