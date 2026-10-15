---
type: estimate
kind: QA
status: passed
target: "[[rule-tests-clock-pinned]]"
purpose: "A test that leaves the code on the real clock fails on the day it is written: every guppi module's clock is pinned to 2001 by one autouse fixture"
method: pytest .guppi/tests/test_conftest.py, plus uv run --project .guppi guppi test green under the fixture
checked: 2026-09-29
origin: raw/2026-09-14/1633/ledger.md#case-145.1
sprint: migration
created: 2026-09-14
tags: [tests, harness]
---

## Criterion

When:
`pytest` collects `.guppi/tests/`, and a test calls the `run()` of a module of `.guppi/guppi/` without `now`, or the code reads the clock outside `run()`.

Then:
Before every test, an autouse fixture in `.guppi/tests/conftest.py` sets into every module of `.guppi/guppi/` that carries a `datetime` attribute a subclass whose `now(tz=None)` returns `2001-01-01 00:00:00 UTC`, and `astimezone` gives the same second. A test that leaves the code on the real clock sees the year 2001 and fails on the day it is written.
**＋** The list of modules comes from a walk over `.guppi/guppi/`, never from a hand list: a new module with a clock is covered with no change to the fixture.
**＋** `.guppi/tests/test_conftest.py` shows it: a `run()` without `now` writes a time dated 2001, and `datetime.strptime`, `fromisoformat` and the constructor of the subclass work as before.
**＋** The targets `test` and `test-*` of the `Makefile` run under the same fixture.
**－** A test that passes `now` does not notice the fixture: `run()` reads no clock.

## Result

2026-09-29, uv run pytest tests/test_conftest.py: 3 passed; tests/conftest.py builds the list by pkgutil.iter_modules over guppi; make test 900 passed under the fixture

## History

- 2026-09-14 created · [[decision-case-145.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1633/ledger.md#L57
- 2026-09-29 updated: the Criterion replaced whole — the block 145.1 as When and Then, the run the test calls named as it reads, the green run of make test into method; purpose and method set, Context and Method out (case 500.5) · [[decision-case-500.5]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L36
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
