---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi compacts below 400000 tokens, keeps its earlier lines, reads its working note again and builds a Case that passes the check
method: "by hand, after the first compaction of a case-guppi in a working session: its transcript under ~/.claude/projects/, its note under cases/ and the event log of the session read against the Criterion, the preTokens of the compact_boundary record in the estimate line"
origin: raw/2026-10-28/2312/ledger.md#case-896.3
sprint: plugin
created: 2026-10-28
tags: [harness, case-build]
---

## Criterion

When:
`case-guppi`, run by `.claude/agents/case-guppi.md` with `autoCompactWindow: 400000`, compacts while it builds a Case in a working session.

Then:
Its transcript under `~/.claude/projects/` holds a `compact_boundary` record whose `preTokens` is below 400000.
**＋** That transcript keeps the lines of `case-guppi` before the record.
**＋** After the compaction `raw/<date>/<hi HHMM>/cases/note-<N>.md` stands in its context again, read by its own `Read` call or put back by Claude Code, before its next round, Case or summary.
**＋** The Case it then writes holds an item of `recommend` for each question of its rounds before and after the compaction, and the check of `rule-case-check` passes it.

## History

- 2026-10-29 created · [[decision-case-896.3]]
