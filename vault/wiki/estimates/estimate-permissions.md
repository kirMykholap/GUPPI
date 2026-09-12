---
type: estimate
kind: QA
status: pending
target: rule-permissions
origin: raw/2026-09-12/ledger.md#case-85.5
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Context

How to describe `settings.json` so that permissions have their own rule, the mode has
its own and the hooks have their own, while the file keeps one source.

## Criterion

### case 85.5

When:
The agent writes or edits `frontier.md`, `spec.md` or `handoff.md` under
`vault/raw/<date>/<HHMM>/`, in Plan Mode or in Work Mode.

Then:
The write happens with no question to the person, allowed by the six entries of the
Render of `rule-permissions`: `Edit` and `Write` for the three names.
**＋** Nothing else is allowed: `ledger.md`, `event_log.md`, `materialize.yaml` and every
file a Rule page governs stay outside the list.
**－** `deny` and `ask` stay empty.
**－** If Claude Code reads `settings.json` only at a session start, the effect begins at
the next start; the reading records which it was.

## Method

the six entries in the rendered .claude/settings.json and the JSON case of tests/test_render.py; the live probe — one edit of the session's spec.md in Work Mode and one of frontier.md, each recorded as asked or not asked, and the same at the next session's /hi in Plan Mode

## History

- 2026-09-12 created · [[decision-case-85.5]]
