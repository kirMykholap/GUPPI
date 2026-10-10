---
type: decision
case: "158"
status: archived
update: ["[[rule-materialize]]"]
origin: raw/2026-09-15/1110/ledger.md#case-158
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger]
---

## Context

Case 142.1 ratified: "An existing entry the script cannot read — not a mapping, or a mapping without `line` and without `derived` — is left as it is, named on stderr, and does not end the run". The librarian's own entries — the synthesis `create` of an Insight, the `update` of a lesson — carry `librarian: synthesis` and neither `line` nor `derived`. By the letter of the rule they are unreadable and are named on stderr every run; the code (`materialize.py:842-850`) takes `librarian` as a third mark of a readable entry and says nothing. The handoff of P recorded this as a caveat "for a later `update`".

## Problem

The text of `rule-materialize` and block 142.1 of `estimate-materialize-assembles` describe a behaviour that does not exist; the code does the right thing, but the text has not signed it.

## Given

`rule-materialize` (`built`, `check`, `estimates: [estimate-materialize-assembles, estimate-materialize-walks-dates]`, both `passed`): line 43, the text of 142.1 with "without `line` and without `derived`"; the docstring of `materialize.py` lines 22–23 says the same; the comment in the code at line 843 says "none of `line`, `derived`, `librarian`".
**＋** `estimate-materialize-assembles`: block 142.1, line 116, repeats the wording; `passed` (P, 1633 L55).
**＋** `tests/test_materialize.py:486` fixes the behaviour (`err == ""` for an entry with `librarian` and no `line`); `:1336` — two unreadable entries named.
**＋** `rule-documentation` describes the marks `librarian`, `synthesis`, `near` — unchanged.
**＋** An `update` with a `ref`: the pages and the code were read, `ask-guppi` not dispatched.
**－** Block 142.1 is not removed (a `supersedes` would drop the whole block with its four other conditions); block 158 refines it.

## Criterion

- [[estimate-materialize-assembles]] § case 158

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#case-158
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
