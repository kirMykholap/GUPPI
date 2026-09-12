---
type: estimate
kind: QA
status: passed
target: rule-governed-files-hook
origin: raw/2026-09-12/ledger.md#case-71.1
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render]
---

## Context

Signed as the nested Estimate of `rule-governed-files-hook` in Case 59.6 (session I,
2026-09-12); no paired `create` line was written, so the page is born of Case 71.1
with the criterion of 59.6 unchanged.

## Criterion

Unit, against a temp vault with one governing page per file: an `Edit`, `Write` or
`MultiEdit` on a governed path exits 2 naming the rule and the file; another tool,
an ungoverned path and an unreadable payload exit 0. Live: one probe in the session
that registers the hook —
an `Edit` on `.claude/skills/hi/SKILL.md` refused, the rule named, the call in the
event log.

### case 91

When:
`guppi guard` refuses an `Edit`, `Write` or `MultiEdit` of a governed file.

Then:
Before it exits 2 it appends one line to `vault/raw/<date>/event_log.md`.
**＋** The line carries the time, the session, the tool, the path and the slug of the rule
that governs the file.
**－** A call the hook lets through writes nothing: `PostToolUse` logs it as before.
**－** A log the hook cannot write does not change the refusal: the exit stays 2 and the
reason still goes to stderr.

## Method

pytest in `tests/test_guard.py` with piped payloads; the live probe once by hand,
written into the estimate line.

## Result

unit: tests/test_guard.py 20 green in the 267 of make test, with the three cases of 91 — a refusal writes its event line with the tool, the path and the rule; a call the guard lets through writes none; an append that raises leaves the exit at 2 and adds one stderr line; live 2026-09-12 session K: an Edit on .claude/skills/hi/SKILL.md was refused with "guard: .claude/skills/hi/SKILL.md is rendered from rule-skill-hi; change the Rule page through a decision", the file unchanged, and raw/2026-09-12/event_log.md gained "- 21:55:57 91c83351 guard refused Edit .claude/skills/hi/SKILL.md (rule-skill-hi)" — the third live clause, the one that failed in session J, now holds

## History

- 2026-09-12 created · [[decision-case-71.1]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L152
- 2026-09-12 criterion: case 91 added · [[decision-case-91]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L206
