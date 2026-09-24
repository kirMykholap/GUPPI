---
type: decision
case: "394"
status: current
defer: ["[[rule-spec-write]]"]
origin: raw/2026-09-24/1303/ledger.md#case-394
sprint: migration
created: 2026-09-24
tags: [hooks, harness, workflow, session]
---

## Context

The hook of `rule-spec-write` reads the value of a sub-point with `code_value` in `guppi/ratified.py`, as CommonMark reads a code span. A value that opens with a code span and ends in text, written without the padding spaces, is refused: that is the failure of Case 392.1 in session 1303. A value that opens and closes with a code span, written without them — three backticks on each side — is not refused: CommonMark and `code_value` read it as one span whose edge backticks are eaten, and the hook writes the value without them. The test of Case 393 checks the refusal on the first shape only; the task line of 393 says the same value unpadded is refused, which does not hold for the second shape.

## Problem

A value unpadded at both edges enters the Spec with its edge backticks lost, and nothing says so. Should the hook refuse a span whose content opens or closes with a backtick of its own, beyond what CommonMark reads?

## Deferred

### [[rule-spec-write]]

A sub-point value whose outer span is unpadded and whose content opens and closes with a code span is read with its edge backticks eaten, not refused

## History

- 2026-09-24 created · raw/2026-09-24/1303/ledger.md#case-394
