---
type: estimate
kind: QA
status: pending
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

the rendered .claude/settings.json holds permissions.defaultMode as "plan" and parses; the live half at the next session start — the session opens in Plan Mode and an edit outside the plan file is not made without a sign-off

## History

- 2026-09-12 created · [[decision-case-85.4]]
