---
type: estimate
kind: QA
status: pending
target: rule-handoff
origin: raw/2026-09-10/ledger.md#case-38.3
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Context

A handoff written from the artifacts says nothing the artifacts do not; one that skips the librarian leaves the ledger unmaterialized.

## Criterion

After a live /handoff: the first turn's context holds git status --porcelain and
the skill stops on a dirty tree; event_log.md carries a handoff line; handoff.md
gained a document with the three sections, written without read-tool calls on the
artifacts; the librarian-guppi agent was dispatched with the date and its report
was shown unchanged; no commit followed.

### case 73.7

When:
The person invokes `/handoff`.

Then:
`handoff.md` is written to `raw/<hi date>/<hi HHMM>/`, one document, no `---`; the
librarian is dispatched with that path.

## Method

one reading by hand at the first /handoff, recorded in the estimate line

## Result

live 2026-09-10 session F: the /handoff context held `git status --porcelain` (empty; the refusal path was read in session E); event_log.md line `handoff` at 11:47:58; handoff.md gained the document `Handoff — 2026-09-10, Slice 3 closes, session F` with the three sections, written from memory by one append with no read of the artifacts; librarian-guppi was dispatched with `Materialize 2026-09-10.`; its report was shown unchanged; no commit followed, the tree is clean at HEAD 8bbfa10

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.3
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L87
- 2026-09-12 criterion: case 73.7 added · [[decision-case-73.7]]
