---
type: estimate
kind: QA
status: pending
target: "[[rule-default-mode]]"
purpose: "A session opens in Plan Mode: the settings file carries defaultMode plan from rule-default-mode"
method: "pytest tests/test_render.py, plus by hand at a later session start: the session opens in Plan Mode and nothing outside the plan file is edited without a sign-off"
origin: raw/2026-09-12/ledger.md#case-85.4
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Criterion

When:
A session starts with `.claude/settings.json` as `guppi render` wrote it from `rule-settings`.

Then:
`.claude/settings.json` carries `"defaultMode": "plan"` under `permissions`, the text of `rule-default-mode`, and the session opens in Plan Mode.
**＋** The Purpose of `rule-default-mode` says why: nothing is written before a Case is ratified.
**－** The Render of `rule-default-mode` holds no other permission field.

## Result

the rendered .claude/settings.json holds permissions.defaultMode "plan" and json.load parses it; live 2026-09-13 session L opened in Plan Mode and nothing outside the plan file was edited without a sign-off — the frontier edits are the /hi rule's and rule-permissions' own allowance

## History

- 2026-09-12 created · [[decision-case-85.4]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L45
- 2026-09-14 updated: Method names tests/test_render.py (case 112.2) · [[decision-case-112.2]]
- 2026-09-29 updated: the Criterion replaced whole — the block 85.4 as When and Then, the page named; purpose and method set, Context and Method out (case 498.4) · [[decision-case-498.4]]
