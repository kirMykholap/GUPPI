---
type: decision
case: "70"
status: archived
delete: ["[[lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn]]"]
origin: raw/2026-09-12/ledger.md#case-70
sprint: migration
created: 2026-09-12
tags: [ledger, hooks, harness]
---

## Context

Session I wrote `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`
with `root_cause: not yet found`, and the librarian clustered it with session F's lesson
under `insight-ledger-hook-reads-only-the-final-text`. The reading of F24 (session J)
shows the trigger is false: no LEDGER block of session I was dropped; the eight Cases
never had one. The finding is recorded as
`lesson-ledger-preview-in-ratification-taken-for-the-record`.

## Problem

A Lesson page whose trigger and root cause are wrong stays live, in the index and in
`ask-guppi`'s answers, and holds an Insight at severity 2 over a pattern that has one
real member. The schema has no state for a lesson found wrong.

## Given

`lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`: `status: clustered`,
`insight: insight-ledger-hook-reads-only-the-final-text`, origin `raw/2026-09-12/ledger.md#L101`.
**＋** Referenced by that Insight (`children`, severity 2), by
`lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (History line), by
`lessons-index.md`, `log.md` and `brief.md`.
**＋** §5: `delete` sets `status: deleted` after an impact analysis, the librarian
archives, `origin` is kept; §8: an Insight is never a Decision target; `severity` is
recomputed by lint as the count of children not archived.
**＋** `guppi pretask --check` (case 59.1) reports an item of a `then` block with no
decision line of its Case, so the preview-for-record mistake is caught in the same session.
**－** `lessons/schema.md` has `archived` only for a lesson whose Insight is `actioned`;
a lesson archived by `delete` is a case the schema does not name, and this Case does not
change the schema.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-70
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
