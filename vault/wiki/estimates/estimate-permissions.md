---
type: estimate
kind: QA
status: pending
target: "[[rule-permissions]]"
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

the six allow entries stand in the rendered .claude/settings.json, Edit and Write for frontier.md, spec.md and handoff.md under vault/raw/**, deny and ask absent; live 2026-09-13 session L: six Edit calls on raw/2026-09-13/0652/frontier.md in Plan Mode, where only the plan file is otherwise allowed, and two on 0652/spec.md in Work Mode, none asked the person; the file written by render --sync at this session's start took effect within the same session

## History

- 2026-09-12 created · [[decision-case-85.5]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L47
- 2026-09-16 updated: the Criterion replaced whole by case 200.5 — nine allow entries, carry.md and brief.md among them (case 200.5) · [[decision-case-200.5]]
