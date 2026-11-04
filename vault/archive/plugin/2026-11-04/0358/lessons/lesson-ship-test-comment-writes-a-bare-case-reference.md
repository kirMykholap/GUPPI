---
type: lesson
kind: error
root_cause: the agent wrote a case reference in a code comment without the bracket that the check of test_ship.py asks of every pointer in the live code
status: archived
insight: "[[insight-ship-live-code-writes-a-case-number-outside-a-bracket]]"
origin: raw/2026-11-02/2035/ledger.md#L13
sprint: plugin
created: 2026-11-02
tags: [session, workflow]
---

## Trigger

the full guppi test of the Work Mode of session 2035 failed on test_the_live_code_holds_no_pointer_outside_a_bracket for the comment "# case 1010.1" of a new test in .guppi/tests/test_casecheck.py, fixed to "# (case 1010.1)"

## Root cause

the agent wrote a case reference in a code comment without the bracket that the check of test_ship.py asks of every pointer in the live code

## History

- 2026-11-02 created · raw/2026-11-02/2035/ledger.md#L13
- 2026-11-03 updated: clustered under insight-ship-live-code-writes-a-case-number-outside-a-bracket (synthesis) · raw/2026-11-02/2155/ledger.md#L22
- 2026-11-04 archived · insight actioned
- 2026-11-04 archived · cleanup
