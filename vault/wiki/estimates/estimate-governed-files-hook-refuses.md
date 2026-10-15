---
type: estimate
kind: QA
status: passed
target: "[[rule-governed-files-hook]]"
purpose: guppi guard refuses a hand edit of a governed harness file, names its rule and logs the refusal
method: "pytest .guppi/tests/test_guard.py, plus by hand in a later session: one Edit of a governed file refused, the rule named, the line in the day's event log"
checked: 2026-10-01
origin: raw/2026-09-12/ledger.md#case-71.1
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render]
---

## Criterion

When:
Claude Code runs `uv run --project .guppi guppi guard` on `PreToolUse` of a tool call, and the hook reads the `governs` field of the live Rule pages under `vault/wiki/rules/`.

Then:
An `Edit`, `Write` or `MultiEdit` on a governed path exits 2. Stderr names the file and the slug of the rule that governs it, and the client blocks the call.
**＋** Before it exits 2, the hook appends one line to `vault/raw/<date>/event_log.md` with the time, the session, the tool, the path and the slug of the rule.
**＋** Another tool or an ungoverned path exits 0.
**＋** A payload the hook cannot read exits 0 with one line on stderr.
**－** A call the hook lets through writes no event line: `PostToolUse` logs it.
**－** A log the hook cannot write does not change the refusal: the exit stays 2, and the reason still goes to stderr.

## Result

2026-10-01, uv run pytest tests/test_guard.py: 20 passed; by hand in session 1441, one Edit of vault/wiki/case-schema.md refused with exit 2, stderr "guard: vault/wiki/case-schema.md is rendered from rule-case-protocol; change the Rule page through a decision", the line "- 17:11:39 85988eb7 guard refused Edit vault/wiki/case-schema.md (rule-case-protocol)" in vault/raw/2026-10-01/event_log.md, the file unchanged in git status

## History

- 2026-09-12 created · [[decision-case-71.1]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L152
- 2026-09-12 criterion: case 91 added · [[decision-case-91]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L206
- 2026-09-29 updated: the Criterion replaced whole — the unit paragraph and the block 91 into one When and Then, the live probe into method; purpose and method set, Context and Method out (case 498.5) · [[decision-case-498.5]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1441/ledger.md#L36
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
