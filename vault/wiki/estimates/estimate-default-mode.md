---
type: estimate
kind: QA
status: passed
target: rule-default-mode
origin: raw/2026-09-12/ledger.md#case-85.4
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Context

How to describe `settings.json` so that permissions have their own rule, the mode has
its own and the hooks have their own, while the file keeps one source.

## Criterion

### case 85.4

When:
A session starts.

Then:
`.claude/settings.json` carries `"defaultMode": "plan"` from `rule-default-mode`, a Leaf
child of `rule-settings`, and the session opens in Plan Mode.
**＋** The page says why: nothing is written before a Case is ratified.
**－** The page holds no other permission field.

## Method

tests/test_render.py: the rendered .claude/settings.json holds permissions.defaultMode as "plan" and parses; the live half at the next session start — the session opens in Plan Mode and an edit outside the plan file is not made without a sign-off

## Result

the rendered .claude/settings.json holds permissions.defaultMode "plan" and json.load parses it; live 2026-09-13 session L opened in Plan Mode and nothing outside the plan file was edited without a sign-off — the frontier edits are the /hi rule's and rule-permissions' own allowance

## History

- 2026-09-12 created · [[decision-case-85.4]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L45
- 2026-09-14 updated: Method names tests/test_render.py (case 112.2) · [[decision-case-112.2]]
