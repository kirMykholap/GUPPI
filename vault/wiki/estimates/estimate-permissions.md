---
type: estimate
kind: QA
status: passed
target: "[[rule-permissions]]"
method: the nine entries in the rendered .claude/settings.json and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of frontier.md at /hi and an edit of spec.md, recorded in the estimate line — never the agent's, which cannot see the prompt
checked: 2026-09-18
origin: raw/2026-09-12/ledger.md#case-85.5
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Criterion

Given:
`.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
**＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
**＋** In Plan Mode the client asks before every edit outside the plan file, allow list or not.
**－** Nothing else under `wiki/` is allowed.

When:
The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`.

Then:
The allow list holds nine entries — Edit and Write for `frontier.md`, `spec.md`, `handoff.md` under `vault/raw/**`; Write for `carry.md` under `vault/raw/**`; Edit and Write for `vault/wiki/brief.md`.
**＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
**＋** A prompt in Plan Mode, approved by the person, is not a finding and not a `failed`.
**－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed.

## Result

2026-09-18, the person's word at session 1252 and the rendered .claude/settings.json: the allow list holds the nine entries the Criterion names — Edit and Write for frontier.md, spec.md, handoff.md and Write for carry.md under vault/raw/**, Edit and Write for vault/wiki/brief.md — deny and ask empty; the client's prompt appears in Plan Mode before the Write of raw/2026-09-18/1252/frontier.md and its Edits, allow list or not, and the person approves it each time — not a finding

## History

- 2026-09-12 created · [[decision-case-85.5]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L47
- 2026-09-16 updated: the Criterion replaced whole by case 200.5 — nine allow entries, carry.md and brief.md among them (case 200.5) · [[decision-case-200.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L39
- 2026-09-17 updated: the Criterion replaced whole by the facts — nine entries named, the given and when about permissions; method as a field, the old sections dropped (case 215) · [[decision-case-215]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L38
- 2026-09-18 updated: the Criterion replaced whole — the prompt is read by the person, a prompt in Plan Mode is not a finding (case 237) · [[decision-case-237]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L12
