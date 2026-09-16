---
type: estimate
kind: QA
status: passed
target: "[[rule-permissions]]"
checked: 2026-09-16
origin: raw/2026-09-12/ledger.md#case-85.5
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Context

How to describe `settings.json` so that permissions have their own rule, the mode has
its own and the hooks have their own, while the file keeps one source.

## Criterion

Given:
The Render of `rule-case-protocol` is spliced into `CLAUDE.md`; the text of 195 stands in the Spec of this session.
**＋** A `replace` in `generate` is one occurrence, whitespace collapsed; `sections` is a whole replacement.
**＋** `settings.json` is rendered from `rule-permissions`; `estimate-permissions` promises six allow entries.
**－** A `supersedes` marks every entry of the named Case: 195 and 196.4 carry one each, 189 nine, so 189 is not superseded.

When:
The skill `carry` writes `vault/wiki/brief.md` or `vault/raw/<date>/<HHMM>/carry.md`.

Then:
The client does not ask: the allow list of `settings.json` holds eight entries — Edit and Write for `frontier.md`, `spec.md`, `handoff.md`, `carry.md` under `vault/raw/**` and for `vault/wiki/brief.md`.
**－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed.

## Method

the six entries in the rendered .claude/settings.json and the JSON case of tests/test_render.py; the live probe — one edit of the session's spec.md in Work Mode and one of frontier.md, each recorded as asked or not asked, and the same at the next session's /hi in Plan Mode

## Result

2026-09-16, the live probe at this session's /hi in Plan Mode: the Write of raw/2026-09-16/1955/frontier.md returned without a prompt; `.claude/settings.json` allow holds nine entries — Edit and Write for frontier.md, spec.md, handoff.md, Write for carry.md under vault/raw/**, Edit and Write for vault/wiki/brief.md — deny and ask empty; the Criterion says eight and lists nine: its own count is off by one, the set it names is what stands

## History

- 2026-09-12 created · [[decision-case-85.5]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L47
- 2026-09-16 updated: the Criterion replaced whole by case 200.5 — nine allow entries, carry.md and brief.md among them (case 200.5) · [[decision-case-200.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L39
