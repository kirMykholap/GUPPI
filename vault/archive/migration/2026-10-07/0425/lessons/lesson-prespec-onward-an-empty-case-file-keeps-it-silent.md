---
type: lesson
kind: error
root_cause: case_out counts a Case file with no decision line as out unless a supersedes mark retires it, so the file of a Case that was built and dropped, never ratified, keeps the hook silent for the rest of Plan Mode
status: archived
insight: "[[insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out]]"
origin: raw/2026-10-07/0211/ledger.md#L48
sprint: migration
created: 2026-10-07
tags: [orchestration]
---

## Trigger

in session 0211 the reply that acknowledged Cases 696–699 after /pre-spec got no reason from uv run guppi onward --plan; case_out over raw/2026-10-07/0211/ prints True, since cases/case-700.md, an empty file case-guppi wrote at 03:43:13 for a Case 700 it then dropped, has no decision line

## Root cause

case_out counts a Case file with no decision line as out unless a supersedes mark retires it, so the file of a Case that was built and dropped, never ratified, keeps the hook silent for the rest of Plan Mode

## History

- 2026-10-07 created · raw/2026-10-07/0211/ledger.md#L48
- 2026-10-07 updated: clustered under insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out (synthesis) · raw/2026-10-07/0211/ledger.md#L48
- 2026-10-07 archived · insight actioned
- 2026-10-07 archived · cleanup
