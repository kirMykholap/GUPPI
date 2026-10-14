---
type: lesson
kind: error
root_cause: guppi/ship.py exempts the whole file EXAMPLE_FILE from cleaning and masks every line of the Render of EXAMPLE, not only the fenced example Case, so the prose around the example is never judged
status: new
origin: raw/2026-10-14/1536/ledger.md#L4
sprint: plugin
created: 2026-10-14
tags: [ci]
---

## Trigger

the first clean branch prod, written by run 38489789184, holds "(case 717.1)" and "(case 646)" in vault/wiki/case-example.md and in the Render of rule-case-example, and guppi ship --check printed nothing on them

## Root cause

guppi/ship.py exempts the whole file EXAMPLE_FILE from cleaning and masks every line of the Render of EXAMPLE, not only the fenced example Case, so the prose around the example is never judged

## History

- 2026-10-14 created · raw/2026-10-14/1536/ledger.md#L4
