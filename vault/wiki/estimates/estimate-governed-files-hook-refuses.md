---
type: estimate
kind: QA
status: pending
target: "[[rule-governed-files-hook]]"
purpose: guppi guard refuses a hand edit of a governed harness file, names its rule and logs the refusal
method: "pytest tests/test_guard.py, plus by hand in a later session: one Edit of a governed file refused, the rule named, the line in the day's event log"
origin: raw/2026-09-12/ledger.md#case-71.1
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render]
---

## Criterion

When:
Claude Code runs `uv run guppi guard` on `PreToolUse` of a tool call, and the hook reads the `governs` field of the live Rule pages under `vault/wiki/rules/`.

Then:
An `Edit`, `Write` or `MultiEdit` on a governed path exits 2. Stderr names the file and the slug of the rule that governs it, and the client blocks the call.
**＋** Before it exits 2, the hook appends one line to `vault/raw/<date>/event_log.md` with the time, the session, the tool, the path and the slug of the rule.
**＋** Another tool or an ungoverned path exits 0.
**＋** A payload the hook cannot read exits 0 with one line on stderr.
**－** A call the hook lets through writes no event line: `PostToolUse` logs it.
**－** A log the hook cannot write does not change the refusal: the exit stays 2, and the reason still goes to stderr.

## Result

unit: tests/test_guard.py 20 green in the 267 of make test, with the three cases of 91 — a refusal writes its event line with the tool, the path and the rule; a call the guard lets through writes none; an append that raises leaves the exit at 2 and adds one stderr line; live 2026-09-12 session K: an Edit on .claude/skills/hi/SKILL.md was refused with "guard: .claude/skills/hi/SKILL.md is rendered from rule-skill-hi; change the Rule page through a decision", the file unchanged, and raw/2026-09-12/event_log.md gained "- 21:55:57 91c83351 guard refused Edit .claude/skills/hi/SKILL.md (rule-skill-hi)" — the third live clause, the one that failed in session J, now holds

## History

- 2026-09-12 created · [[decision-case-71.1]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L152
- 2026-09-12 criterion: case 91 added · [[decision-case-91]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L206
- 2026-09-29 updated: the Criterion replaced whole — the unit paragraph and the block 91 into one When and Then, the live probe into method; purpose and method set, Context and Method out (case 498.5) · [[decision-case-498.5]]
