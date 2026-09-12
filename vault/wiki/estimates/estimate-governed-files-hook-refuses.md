---
type: estimate
kind: QA
status: failed
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

## Method

pytest in `tests/test_guard.py` with piped payloads; the live probe once by hand,
written into the estimate line.

## Result

unit: tests/test_guard.py green in the 211 of make test; live 2026-09-12 session J, first render of the session registered the hook in .claude/settings.json: an Edit on .claude/skills/hi/SKILL.md was refused with "guard: .claude/skills/hi/SKILL.md is rendered from rule-skill-hi; change the Rule page through a decision", the file unchanged; the call is NOT in the event log — PostToolUse does not fire for a tool a PreToolUse hook blocked, and the guard logs nothing itself; two of the three live clauses hold, the third does not

## History

- 2026-09-12 created · [[decision-case-71.1]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L152
