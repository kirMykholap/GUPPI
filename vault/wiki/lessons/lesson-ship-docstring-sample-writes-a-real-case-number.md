---
type: lesson
kind: error
root_cause: the agent wrote a real case number as the example closer of a Frontier line inside a code span of a module docstring, and guppi ship reads every case number in the docstrings and comments of the code as a pointer, which stands only in a bracket at the end of its sentence; a sample in code takes the placeholder `case N`
status: clustered
insight: "[[insight-ship-live-code-writes-a-case-number-outside-a-bracket]]"
origin: raw/2026-11-02/2155/ledger.md#L22
sprint: plugin
created: 2026-11-02
tags: [ci, tests]
---

## Trigger

the first full guppi test of Work Mode of session 2155 failed test_the_live_code_holds_no_pointer_outside_a_bracket on .guppi/guppi/frontierguard.py:5, "a reference to a case: case 1012", fixed in the same Work Mode by the sample `case N`

## Root cause

the agent wrote a real case number as the example closer of a Frontier line inside a code span of a module docstring, and guppi ship reads every case number in the docstrings and comments of the code as a pointer, which stands only in a bracket at the end of its sentence; a sample in code takes the placeholder `case N`

## History

- 2026-11-03 created · raw/2026-11-02/2155/ledger.md#L22
- 2026-11-03 updated: clustered under insight-ship-live-code-writes-a-case-number-outside-a-bracket (synthesis) · raw/2026-11-02/2155/ledger.md#L22
