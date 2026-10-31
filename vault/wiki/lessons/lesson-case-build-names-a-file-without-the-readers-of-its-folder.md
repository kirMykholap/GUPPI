---
type: lesson
kind: error
root_cause: Case 967.3 put a new generated file under .guppi/ and read its readers by the name of the file only; the readers of the folder, the tree walk of guppi ship and its test of the live code, hold no word of the file
status: clustered
insight: "[[insight-case-build-changes-a-step-without-reading-its-readers]]"
origin: raw/2026-10-31/1831/ledger.md#L32
sprint: plugin
created: 2026-10-31
tags: [case-build, harness]
---

## Trigger

in Work Mode of session 1831 the full guppi test run failed on test_the_live_code_holds_no_pointer_outside_a_bracket of test_ship.py, since guppi links --write wrote .guppi/links.md and the tree walk of ship.py copies every file under .guppi/ but those of LEFT_OUT, so the clean version would carry the graph; Work Mode added .guppi/links.md to LEFT_OUT of .guppi/guppi/ship.py

## Root cause

Case 967.3 put a new generated file under .guppi/ and read its readers by the name of the file only; the readers of the folder, the tree walk of guppi ship and its test of the live code, hold no word of the file

## History

- 2026-10-31 created · raw/2026-10-31/1831/ledger.md#L32
- 2026-10-31 updated: clustered under insight-case-build-changes-a-step-without-reading-its-readers (synthesis) · raw/2026-10-31/1831/ledger.md#L32
