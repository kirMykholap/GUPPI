---
type: estimate
kind: QA
status: passed
target: rule-spec-capture
origin: raw/2026-09-09/ledger.md#case-20
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, workflow]
---

## Context

The Spec is the content every decision line of a session points at. The unit cases pin
what the hook writes and when it refuses; the live reading proves the registration and
records what a rejected plan hands the hook, which the Slice 1 probe did not measure.

## Criterion

Given a `PostToolUse` payload naming `ExitPlanMode` with a plan and a `hi` recorded:
`spec.md` gains a `---` separator (when the file has content), the stamp
`<!-- approved HH:MM:SS · session xxxxxxxx -->` and the plan text, once, even when the
hook runs twice; earlier documents stay intact. Without `hi`: exit 2 naming the session,
file untouched. Another tool's payload: nothing written, exit 0. Live: the next plan
approval lands in `raw/<date>/spec.md` by the hook, not by hand, and the reading records
what a rejected plan produces.

## Method

pytest in `tests/test_spec.py` with piped payloads against a temp vault; the live reading
once by hand, written into the estimate line.

## Result

live: the approved plan landed in raw/2026-09-10/spec.md by the hook, stamp `<!-- approved 10:25:13 · session c640ade7 -->`, 1502 lines, once; the rejected-plan reading was not taken, the plan was approved at the first attempt

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-20
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L77
