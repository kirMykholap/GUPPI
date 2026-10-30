---
type: rule
kind: Leaf
purpose: Prevents a test from passing on the day it is written and failing later because the code read the real clock
status: built
enforcement: check
implementation_ref: [.guppi/tests/conftest.py, .guppi/tests/test_conftest.py]
parent: "[[rule-harness]]"
estimates: ["[[estimate-tests-clock-pinned]]"]
origin: raw/2026-09-14/1633/ledger.md#case-145.1
sprint: migration
created: 2026-09-14
tags: [tests, harness]
core: true
---

## Purpose

Prevents a test from passing on the day it is written and failing later because
the code read the real clock. A test that pins a date goes red a day after it is written when the code reads `datetime.now()` (two lessons of 2026-09-10 and 09-11 went red that way, case 145.1).
Every `run()` of `.guppi/guppi/` takes `now`; this Rule makes forgetting it fail at once.

## History

- 2026-09-14 created · [[decision-case-145.1]]
- 2026-09-14 estimate estimate-tests-clock-pinned added · [[decision-case-145.1]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the dated lessons of the Purpose move into the bracket of their pointer · [[decision-case-875]]
- 2026-10-30 updated: ## How it works left the Leaf, its mechanism in the docstring of .guppi/tests/conftest.py · [[decision-case-942.1]]
