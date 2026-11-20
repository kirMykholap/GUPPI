---
type: decision
case: "1032"
status: current
children: ["[[decision-case-1032.1]]", "[[decision-case-1032.2]]", "[[decision-case-1032.3]]", "[[decision-case-1032.4]]"]
origin: raw/2026-11-04/0807/ledger.md#case-1032
sprint: plugin
created: 2026-11-04
tags: [harness, plugin, hooks, render, session, workflow, librarian, ledger]
---

## Problem

A `cd` in a Bash call moves the folder that every later hook runs in, the relative `--project .guppi` then names no folder, and each hook refuses each tool call and each reply until the person stops the session.

## Recommend

- **How each hook command names the folder of the code**
  - Recommended: (a) a shell command with the project path in quotes, `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi <name>`.
  - Answer: agreed, (a).
- **Which commands the Case covers**
  - Recommended: (a) the hook commands only.
  - Answer: agreed, (a).
- **Change**
  - Asked: Case 1035 of this session asked by its lines `**Other Case:**` that a hook's own refusal be found as `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook` sets it, by its name after the bracket, and not under the forms of its command.
  - Taken: in 1032.1 the line on the modules that find their refusals points to that Estimate, `command_forms` keeps only the forms that `.guppi/guppi/ship.py` removes, and the test of `.guppi/tests/test_ledger.py` tests those forms alone; in 1032.2 and 1032.3 the refusal is a line whose text after its bracket opens with `ledger:` or `casecheck:`.
- **Change**
  - Asked: the findings of `/pre-spec`: the sentence of `rule-guppi-package` on what its test fails on still says "without `--project .guppi`"; the names and the `change` lines of 1032.2 and 1032.3 still spoke of the forms of the command; and the claim on the count Grep missed the Estimates that state the text of a registration.
  - Taken: 1032.1 gives `rule-guppi-package` a second pair on that sentence; 1032.2 and 1032.3 take new names and `change` lines on the name after the bracket; `context` names the three Estimates that state a registration, Case 1032.4 replaces `estimate-case-check-refuses-text-before-a-round`, and Case 1035 carries the two Estimates of `guppi onward`.

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#case-1032
