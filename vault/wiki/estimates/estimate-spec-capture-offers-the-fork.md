---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-capture]]"
purpose: The hook prints the fork between Work Mode and /carry after the Spec is written
method: pytest in tests/test_spec.py, the three tests of the printed fork, plus one live reading of the ExitPlanMode result of a session after the change
checked: 2026-09-20
origin: raw/2026-09-16/1034/ledger.md#case-190.5
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness]
---

## Criterion

Given:
For `PostToolUse` Claude Code adds to the agent's context only `hookSpecificOutput.additionalContext` from a JSON object on stdout; plain stdout with exit 0 goes to the debug log.
**＋** A `PostToolUse` hook blocks nothing: the tool has run.
**－** The path "no `/hi` for this session" — stderr, exit 2 — does not change.

When:
`guppi spec` has run on `PostToolUse` of `ExitPlanMode` and written the Spec, or found it already there.

Then:
The stdout of the hook is one JSON object: `hookSpecificOutput` with `hookEventName: PostToolUse` and `additionalContext`, holding the fork line — Work Mode on the Spec or `/carry` — with the session folder and the Spec file, and that nothing starts until the person answers.
**＋** The agent sees this line in the `ExitPlanMode` result.
**－** Without a Spec, nothing, as before.
**－** The writing of the Spec does not change: that is the promise of `estimate-spec-capture-appends`.

## Result

2026-09-20, the first ExitPlanMode of session 0740 (08:55:25): the result carried the fork as PostToolUse additionalContext — the Spec in vault/raw/2026-09-20/0740/spec.md, Work Mode or /carry with carry.md as the mark, nothing started until the person answers; the Spec copied whole, 245 lines; pytest tests/test_spec.py green at e69fd95

## History

- 2026-09-16 created · [[decision-case-190.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L36
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-20 updated: the Criterion replaced whole — the fork as additionalContext, read live (case 255) · [[decision-case-255]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0740/ledger.md#L12
