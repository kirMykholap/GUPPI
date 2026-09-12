---
type: estimate
kind: QA
status: pending
target: rule-retro
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Context

A Retro that starts by reading files spends the context it exists to save; one that edits new scope hides a decision.

## Criterion

After a live /retro: the first turn's context holds the output of make test, make
style and today's ledger with no read-tool call; event_log.md carries a retro line;
the first message is the frontier in three blocks — ratified by Case, done and not
done against the Spec, noticed — with no read call; every item raised by either side
ends as a lesson line, an estimate line, a short defer with its Case under ## Deferred in
spec.md, or a handoff note; no decision line other than defer is written in Retro;
every Estimate whose work is finished has its reading line; a red test ends as a fix
that traces to today's ledger or as a patch in raw/ with a short defer, with a
lesson[error] either way; every edit made in Retro traces to a line of today's ledger;
the closing reply lists the ratifications, the done and the not done; the commit
precedes the /handoff call.

### case 73.6

When:
`/retro` writes a short defer.

Then:
It is appended under `## Deferred` of `raw/<hi date>/<hi HHMM>/spec.md`; the unticked
`tasks` Retro counts are that file's.

## Method

one reading by hand at the first /retro, recorded in the estimate line

## Result

live 2026-09-12 session I, the first /retro of the new form: the skill loaded make test (211 green), make style (clean) and the ledger of the day (101 lines) by its substitutions, the agent made no read call; the opening was one message — the ratifications grouped by Case, done and not done against the tasks of the Spec, nine observations; the person added their answers; every item ended as a lesson, a reading, a short defer under ## Deferred or a handoff note; no create, update or delete was ratified

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L86
- 2026-09-11 updated: the frontier, the four outcomes, the readings and the red-test paths added; pending until the next live /retro · [[decision-case-56]]
- 2026-09-12 updated: the Deferred heading (cases 59.5, 66) · [[decision-case-66]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L106
- 2026-09-12 criterion: case 73.6 added · [[decision-case-73.6]]
