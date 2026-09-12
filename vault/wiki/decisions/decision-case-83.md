---
type: decision
case: "83"
status: superseded
defer: [rule-governed-files-hook]
superseded_by: [decision-case-91]
origin: raw/2026-09-12/ledger.md#case-83
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render]
---

## Context

The live clause of `estimate-governed-files-hook-refuses` says the refused call is in
the event log. At the probe of session J the guard refused the Edit and named the rule,
and the event log gained no line: PostToolUse does not fire for a tool a PreToolUse
hook blocked (`lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event`). The
reading is `failed`; `rule-governed-files-hook` stays `draft`.

## Problem

Either the guard writes its own event line on a refusal, or the clause leaves the
criterion. An `update` of `rule-governed-files-hook` with its Estimate; the next Plan
Mode.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-83
- 2026-09-12 superseded by decision-case-91 · [[decision-case-91]]
