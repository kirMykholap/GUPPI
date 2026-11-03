---
type: estimate
kind: QA
status: passed
target: "[[rule-governed-files-hook]]"
purpose: guppi guard refuses a hand edit of a governed harness file, names its rule and logs the refusal
method: "pytest .guppi/tests/test_guard.py, plus by hand in a later session: one Edit of a governed file refused, the rule named, the line in the day's event log"
checked: 2026-10-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, render]
core: true
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

2026-10-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
