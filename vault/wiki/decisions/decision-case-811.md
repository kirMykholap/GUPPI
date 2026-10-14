---
type: decision
case: "811"
status: current
update: ["[[rule-clean-branch]]", "[[estimate-clean-branch-writes-a-clean-copy]]"]
origin: raw/2026-10-14/0232/ledger.md#case-811
sprint: plugin
created: 2026-10-14
tags: [ci, git, plugin]
---

## Problem

A comment or a docstring of the code that opens with a list of case numbers and a colon, or that is such a list alone, reaches the clean copy with no finding, though one case number in the same place is a finding.

## Recommend

- **Should an opening with a list of case numbers and a colon be caught?**
  - Recommended: (a) yes, with the same joining words as the bracket — a comma, a semicolon, `and` or a dash — read by one shared pattern.
  - Answer: agreed, (a).
- **Should a comment that is only a list of case numbers be caught too?**
  - Recommended: (a) yes, with the same joining words.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) replace the Criterion of `estimate-clean-branch-writes-a-clean-copy` whole, read in this session by `uv run pytest tests/test_ship.py` with a new test of the list shapes.
  - Answer: agreed, (a).

## History

- 2026-10-14 created · raw/2026-10-14/0232/ledger.md#case-811
