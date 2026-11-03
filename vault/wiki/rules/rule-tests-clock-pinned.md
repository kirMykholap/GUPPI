---
type: rule
kind: Leaf
purpose: Prevents a test from passing on the day it is written and failing later because the code read the real clock
status: built
enforcement: check
implementation_ref: [.guppi/tests/conftest.py, .guppi/tests/test_conftest.py]
parent: "[[rule-harness]]"
estimates: ["[[estimate-tests-clock-pinned]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [tests, harness]
core: true
---

## Purpose

Prevents a test from passing on the day it is written and failing later because
the code read the real clock. A test that pins a date goes red a day after it is written when the code reads `datetime.now()`.
Every `run()` of `.guppi/guppi/` takes `now`; this Rule makes forgetting it fail at once.

## History

- 2026-11-03 shipped with GUPPI
