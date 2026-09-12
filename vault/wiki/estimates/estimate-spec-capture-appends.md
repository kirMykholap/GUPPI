---
type: estimate
kind: QA
status: pending
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
file untouched. Another tool's payload: nothing written, exit 0. A `## Deferred` section appended by the agent stays intact under a later approval's separator, and materialize reads its Cases. Live: the next plan approval lands in `raw/<date>/spec.md` by the hook, not by hand, and the reading records what a rejected plan produces.

### case 73.2

When:
`ExitPlanMode` is approved in a session with a `hi`.

Then:
The plan is copied to `raw/<hi date>/<hi HHMM>/spec.md`; a second approval of the same
session appends under `---` and the stamp, as before.
**－** Without a `hi` the hook refuses as before.

## Method

pytest in `tests/test_spec.py` with piped payloads against a temp vault; the live reading
once by hand, written into the estimate line.

## Result

live 2026-09-12 session I: the rejected ExitPlanMode of 04:58 wrote nothing — no raw/2026-09-12/spec.md, no spec line in the event log, the pretask hook's exit 2 stood alone; the approved plan of 10:48:13 landed by the hook as raw/2026-09-12/spec.md with the stamp `<!-- approved 10:48:13 · session 763dd08e -->`, 1595 lines, once, no separator since the file was new; tests/test_spec.py 8 green

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-20
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L77
- 2026-09-11 updated: the Retro section survives a later approval; pending until the live reading · [[decision-case-57]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L34
- 2026-09-12 updated: the Deferred heading (cases 59.5, 66) · [[decision-case-66]]
- 2026-09-12 criterion: case 73.2 added · [[decision-case-73.2]]
