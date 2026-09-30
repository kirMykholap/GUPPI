---
type: estimate
kind: QA
status: passed
target: "[[rule-permissions]]"
method: the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of work.md in Work Mode, recorded in the estimate line — never the agent's, which cannot see the prompt
checked: 2026-09-30
origin: raw/2026-09-12/ledger.md#case-85.5
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Criterion

When:
The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`.

Then:
The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, and Edit and Write for `vault/wiki/brief.md`.
**＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
**＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
**＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
**＋** In Plan Mode the client asks before every edit outside the plan file, allow list or not.
**＋** A prompt in Plan Mode, approved by the person, is not a finding and not a `failed`.
**－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed.

## Result

2026-09-30, the person's word at /hi of session 1736: Claude Code did not ask for permission when the agent changed vault/raw/2026-09-30/1306/work.md with the Edit tool in Work Mode; the rendered .claude/settings.json: the allow list holds Edit and Write for frontier.md, spec.md, handoff.md and work.md under vault/raw/**, Write for carry.md under vault/raw/**, Edit and Write for vault/wiki/brief.md, no deny and no ask; uv run pytest tests/test_render.py -k "json or permission": 4 passed

## History

- 2026-09-12 created · [[decision-case-85.5]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L47
- 2026-09-16 updated: the Criterion replaced whole by case 200.5 — nine allow entries, carry.md and brief.md among them (case 200.5) · [[decision-case-200.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L39
- 2026-09-17 updated: the Criterion replaced whole by the facts — nine entries named, the given and when about permissions; method as a field, the old sections dropped (case 215) · [[decision-case-215]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L38
- 2026-09-18 updated: the Criterion replaced whole — the prompt is read by the person, a prompt in Plan Mode is not a finding (case 237) · [[decision-case-237]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L12
- 2026-09-28 updated: the Criterion replaced whole — Edit and Write for work.md join the allow list (case 479.5) · [[decision-case-479.5]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L3
