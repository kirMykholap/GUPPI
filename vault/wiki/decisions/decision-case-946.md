---
type: decision
case: "946"
status: current
children: ["[[decision-case-946.1]]", "[[decision-case-946.2]]"]
origin: raw/2026-10-30/2345/ledger.md#case-946
sprint: plugin
created: 2026-10-30
tags: [harness, schema, hooks, workflow, session, librarian, render]
---

## Problem

Two facts of the removed `## How it works` sections stand in no docstring. One fact is false, and its false reason also stands in four other live texts. The Estimate on the moved facts asks for each fact as it stood, so it cannot pass.

## Recommend

- **What the docstring of guard.py says about subagents**
  - Recommended: (a) the docstring states the true fact: Claude Code runs the hook on a call of a subagent too, and the hook refuses it the same way.
  - Answer: agreed, (a).
- **Whether the Case also fixes the same false reason elsewhere**
  - Recommended: (a) a second sub-case fixes the docstring of `shellwrite.py`, the Purpose of `rule-shell-write-check`, the Criterion of its Estimate and the `## How it works` of `rule-documentation`.
  - Answer: agreed, (a).
- **What the docstring of ratified.py says about removing a parent**
  - Recommended: (a) the docstring adds one clause that joins the two wordings; the code does not change.
  - Answer: agreed, (a).
- **How the Estimate on the moved facts is checked**
  - Recommended: (a) replace the Criterion of `estimate-rules-schema-leaf-carries-no-how-it-works` whole, and set its purpose and method anew.
  - Answer: agreed, (a).

## History

- 2026-10-31 created · raw/2026-10-30/2345/ledger.md#case-946
