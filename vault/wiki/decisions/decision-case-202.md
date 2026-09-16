---
type: decision
case: "202"
status: current
update: ["[[rule-lint]]", "[[estimate-lint-catches]]"]
origin: raw/2026-09-16/1955/ledger.md#case-202
sprint: migration
created: 2026-09-16
tags: [harness, workflow]
---

## Context

`rule-lint` is a Leaf, `enforcement: check`, its code `guppi/lint.py`, its tests `tests/test_lint.py`, the target `make lint` after `render --check`. The page carries `## Purpose` and a long `## How it works`; one Estimate — `estimate-lint-catches`: a head plus four blocks (103.5, 112.1, 149.3, 156), `passed`. The Estimate schemas are already in the new shape (193): `purpose`, `method`, `checked` optional fields, `## Context` and `## Method` optional sections. The code does not know it: `check_method` reads the `## Method` section only and says nothing of the `method` field on the thirteen new pages; `check_criterion` accepts `### case N` blocks; a `pending` Estimate is invisible to lint — ten today, known to the brief alone. Decision 191 deferred the page with the text: the finding `unread` on every `pending` and `failed`; the schema without `## Context` and `## Method`; the `unmigrated` counter for the transition and the removal of the old shape at zero; the change of 186.3 (`deferred`) stands. The Case touches the one Estimate of the rule.

## Problem

The model of 182 says: a rule changes → the Estimate `pending` → lint red → the reading → `passed` → lint clean. Today the chain is broken in the middle: lint does not see `pending`, and an Estimate can stand unread for any length of time. Nobody checks the `method` field on the new pages, and the 42 pages of the old shape are not visible as a remainder. The question: how lint sees an unread promise and the remainder of the migration, and what it checks in `method` once it is a line, not a section.

## History

- 2026-09-16 created · raw/2026-09-16/1955/ledger.md#case-202
