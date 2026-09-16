---
type: estimate
kind: QA
status: passed
target: "[[rule-permissions]]"
method: the nine entries in the rendered .claude/settings.json and the JSON case of tests/test_render.py; the live probe — the Write of frontier.md at /hi in Plan Mode and one edit of spec.md in Work Mode, each recorded as asked or not asked
checked: 2026-09-17
origin: raw/2026-09-12/ledger.md#case-85.5
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Criterion

Given:
`.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the allow list.
**＋** The live probe is the Write of `frontier.md` at `/hi` in Plan Mode and an edit of `spec.md` in Work Mode, each recorded as asked or not asked.
**－** Nothing else under `wiki/` is allowed.

When:
The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`.

Then:
The client does not ask: the allow list holds nine entries — Edit and Write for `frontier.md`, `spec.md`, `handoff.md` under `vault/raw/**`; Write for `carry.md` under `vault/raw/**`; Edit and Write for `vault/wiki/brief.md`.
**－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed.

## Result

2026-09-17, the live probe at this session's /hi in Plan Mode: the Write of raw/2026-09-16/2238/frontier.md and its later Edits returned without a prompt; .claude/settings.json allow holds the nine entries the Criterion names — Edit and Write for frontier.md, spec.md, handoff.md, Write for carry.md under vault/raw/**, Edit and Write for vault/wiki/brief.md — deny and ask empty

## History

- 2026-09-12 created · [[decision-case-85.5]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L47
- 2026-09-16 updated: the Criterion replaced whole by case 200.5 — nine allow entries, carry.md and brief.md among them (case 200.5) · [[decision-case-200.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L39
- 2026-09-17 updated: the Criterion replaced whole by the facts — nine entries named, the given and when about permissions; method as a field, the old sections dropped (case 215) · [[decision-case-215]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L38
