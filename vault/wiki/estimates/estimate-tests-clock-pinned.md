---
type: estimate
kind: QA
status: passed
target: "[[rule-tests-clock-pinned]]"
origin: raw/2026-09-14/1633/ledger.md#case-145.1
sprint: migration
created: 2026-09-14
tags: [tests, harness]
---

## Context

The first half of the Proposal is done in place: all twelve `run()` in `guppi/` take `now=None` and read the clock only there (`datetime.now().astimezone()`); the helpers of ten test files pass `NOW`; `index`, `lint`, `render`, `tail`, `cli` read no clock, `materialize` does not use `now`. The second half does not exist: nothing stops the next helper from forgetting `now` — the error shows again on a later day, not on the day it is written. No Rule on the test suite as a whole exists in the vault; there is no `conftest.py`. Decide: close the class with one fixture file under its own Rule page, or close the Insight as done and wait for a recurrence.

## Criterion

### case 145.1

When:
`pytest` collects `tests/`; then any test calls the `run()` of a `guppi/` module without `now`, or the code reads `datetime.now()` somewhere outside `run()`.

Then:
An autouse fixture in `tests/conftest.py` sets, before every test, into every `guppi/` module that imports `datetime` a subclass whose `now(tz=None)` returns `2001-01-01 00:00:00 UTC` (`astimezone` gives the same second); a test that leaves the code the real clock sees the year 2001 and fails on the day it is written.
**＋** The list of modules is built by walking `guppi/*.py` for a `datetime` attribute, not by hand: a new module with a clock is covered without a change of the fixture.
**＋** One test, `tests/test_conftest.py`: `guppi.ledger.run` without `now` writes a time dated 2001; `datetime.strptime` and the constructor of the subclass work as before.
**＋** `make test` is green under the fixture on the tree of this session.
**－** A test that passes `now` does not notice the fixture: `run()` reads no clock.
**－** The `Makefile` does not change; the `test-*` targets are covered by the same fixture.

## Method

`tests/test_conftest.py` green, `make test` green under the fixture; one reading by hand, recorded in the estimate line

## Result

block 145.1, 2026-09-14: tests/test_conftest.py — event.run without now writes under raw/2001-01-01 at 00:00:00; every module with a datetime attribute pinned; strptime, fromisoformat and the constructor unchanged; make test 368 green under the fixture, after it caught the three CLI tests that read the real clock (test_ledger, test_pretask, test_event), moved to the fixture

## History

- 2026-09-14 created · [[decision-case-145.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1633/ledger.md#L57
