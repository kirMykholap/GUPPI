---
type: estimate
kind: QA
status: passed
target: "[[rule-default-mode]]"
purpose: "A session opens in Plan Mode: the settings file carries defaultMode plan from rule-default-mode"
method: "pytest .guppi/tests/test_render.py, plus by hand at a later session start: the session opens in Plan Mode and nothing outside the plan file is edited without a sign-off"
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, session]
core: true
---

## Criterion

When:
A session starts with `.claude/settings.json` as `guppi render` wrote it from `rule-settings`.

Then:
`.claude/settings.json` carries `"defaultMode": "plan"` under `permissions`, the text of `rule-default-mode`, and the session opens in Plan Mode.
**＋** The Purpose of `rule-default-mode` says why: nothing is written before a Case is ratified.
**－** The Render of `rule-default-mode` holds no other permission field.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
