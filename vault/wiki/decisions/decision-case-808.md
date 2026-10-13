---
type: decision
case: "808"
status: current
children: ["[[decision-case-808.1]]", "[[decision-case-808.2]]"]
origin: raw/2026-10-14/0101/ledger.md#case-808
sprint: plugin
created: 2026-10-14
tags: [ci, git, plugin]
---

## Problem

A case number written with no word before it, such as `(274.1)`, is a pointer that `guppi ship` does not see, so it reaches the clean copy, and nothing reports a new one.

## Recommend

- **How a bare case number leaves the clean copy**
  - Recommended: (b) write each bare number in the word form at its source, by hand in Work Mode, comments and docstrings only; `guppi ship` stays as it is.
  - Answer: agreed, (b).
- **Whether a check stops new bare numbers**
  - Recommended: (b) `guppi ship --check` reports a bare case number in a comment or a docstring of a Python file, read by Python's own tokenizer, and removes nothing.
  - Answer: agreed, (b).
- **How the two changes are checked**
  - Recommended: (a) replace the Criterion of both existing Estimates, one sub-case each.
  - Answer: agreed, (a).
- **Whether the check also reports a docstring that opens with a case number**
  - Recommended: (a) the check also reports a comment or a docstring that opens with a case number followed by a colon, and a comment whose whole text is a case number.
  - Answer: (a).

## History

- 2026-10-14 created · raw/2026-10-14/0101/ledger.md#case-808
