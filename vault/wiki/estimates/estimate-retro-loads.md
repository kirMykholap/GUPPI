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
ends as a lesson line, an estimate line, a short defer with its Case under ## Retro in
spec.md, or a handoff note; no decision line other than defer is written in Retro;
every Estimate whose work is finished has its reading line; a red test ends as a fix
that traces to today's ledger or as a patch in raw/ with a short defer, with a
lesson[error] either way; every edit made in Retro traces to a line of today's ledger;
the closing reply lists the ratifications, the done and the not done; the commit
precedes the /handoff call.

## Method

one reading by hand at the first /retro, recorded in the estimate line

## Result

live 2026-09-10 session F: the /retro context held make test (132), make style and today's ledger with no read-tool call; event_log.md line `retro` at 11:46:56; no edit was made in Retro; no bug and no new deferral, so no lesson and no defer line; the closing reply listed the ratifications (Cases 42, 43), the done and the not done; the commit 893b3d9 at 11:47:54 preceded the /handoff call at 11:47:58

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L86
- 2026-09-11 updated: the frontier, the four outcomes, the readings and the red-test paths added; pending until the next live /retro · [[decision-case-56]]
