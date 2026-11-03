---
type: insight
pattern: the agent writes a case number into the live code — a comment of a test, a sample in a module docstring — outside a bracket at the end of its sentence, and the check of test_ship.py reads every case number in the docstrings and comments of the code as a pointer, so the full guppi test of Work Mode fails and the text is fixed to a bracket or to the placeholder `case N`
status: open
children: ["[[lesson-ship-test-comment-writes-a-bare-case-reference]]", "[[lesson-ship-docstring-sample-writes-a-real-case-number]]"]
severity: 2
origin: raw/2026-11-02/2155/ledger.md#L22
sprint: plugin
created: 2026-11-02
tags: [ci, tests, session, workflow]
---

## Pattern

In session 2035 a test comment "# case 1010.1" and in session 2155 a sample closer "case 1012" in the docstring of .guppi/guppi/frontierguard.py failed test_the_live_code_holds_no_pointer_outside_a_bracket of .guppi/tests/test_ship.py at the first full guppi test of Work Mode. In both the agent wrote a case number in the live code in a form other than the bracket at the end of a sentence that the check of the clean branch asks of every pointer, and in both the fix was made in the same Work Mode.

## Proposal

A suggestion, not a decision — the agent could run uv run --project .guppi pytest .guppi/tests/test_ship.py, or the one check of the live code, after it writes a docstring or a comment, before the full guppi test; or a PostToolUse hook on Edit and Write of a file under .guppi/ could run the same predicate of the pointer and name a bare case number at once.

## History

- 2026-11-03 created · raw/2026-11-02/2155/ledger.md#L22
