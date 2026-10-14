---
type: rule
kind: Leaf
purpose: Prevents a test from passing on the day it is written and failing later because the code read the real clock
status: built
enforcement: check
implementation_ref: [tests/conftest.py, tests/test_conftest.py]
parent: "[[rule-harness]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [tests, harness]
core: true
---

## Purpose

Prevents a test from passing on the day it is written and failing later because
the code read the real clock. Two lessons of 2026-09-10 and 09-11 went red a day
after they were written: the test pinned a date, the code read `datetime.now()`.
Every `run()` of `guppi/` takes `now`; this Rule makes forgetting it fail at once.

## How it works

`tests/conftest.py` holds one autouse fixture. Before every test it walks every
module under `guppi/` that carries a `datetime` attribute and replaces it, with
pytest's `monkeypatch`, by a subclass of `datetime` whose `now(tz=None)` returns
`2001-01-01 00:00:00 UTC`; `astimezone` gives the same second. A test that calls a
`run()` without `now`, or code that reads the clock outside `run()`, sees the year
2001 and fails on the day it is written, not on a later one. The list of modules is
built by the walk, never by hand. `datetime.strptime`, `fromisoformat` and the
constructor of the subclass work as before. A test that passes `now` does not
notice the fixture. `tests/test_conftest.py` checks the fixture itself: a `run()`
without `now` writes a time dated 2001.

## History

- 2026-10-14 shipped with GUPPI
