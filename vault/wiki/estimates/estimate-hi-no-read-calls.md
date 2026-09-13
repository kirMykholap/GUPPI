---
type: estimate
kind: QA
status: pending
target: rule-skill-hi
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Context

The whole point of the skill is that the context is present before the agent's first turn.
A read-tool call for the brief or the sprint means a substitution did not resolve, and the
frame of the skill is broken regardless of which child failed.

## Criterion

After `/hi` the context holds `sprint.md`, `brief.md`, the current branch, `git status` and
the issue list (or `gh`'s message) with no read-tool call having occurred, and
`raw/<date>/event_log.md` carries a `hi` line.

### case 101.3

When:
The person invokes `/hi`.

Then:
The Render of `rule-skill-hi` carries the marker `<!-- rule-ledger-tail -->` after `<!-- rule-github-issues -->`; `rule-ledger-tail` is the fourth child.
**＋** After `/hi` the context holds the output of `guppi tail` without a read call.
**＋** `estimate-hi-no-read-calls` gets a `### case 101.3` block, `pending`.

## Method

One reading at a session start, by hand, recorded in the estimate line.

## Result

Passing. Session B start, 2026-09-09 16:11: `sprint.md`, `brief.md`, the branch, the
short status and `gh`'s message were in the first turn's context with no read-tool call;
`raw/2026-09-09/event_log.md` carries `16:11:19 -------- hi`.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-13 criterion: case 101.3 added · [[decision-case-101.3]]
