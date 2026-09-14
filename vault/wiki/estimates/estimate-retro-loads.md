---
type: estimate
kind: QA
status: failed
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

### case 109.1

When:
The person invokes `/retro`.

Then:
The Render: `Ledger of today: !`cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null``; the text "a line of today's ledger" becomes "a line of this session's ledger".
**＋** The revert patch goes to `raw/<hi date>/<hi HHMM>/patch-<slug>.diff`, the session folder.
**＋** `estimate-retro-loads` gets a `### case 109.1` block, `pending`.

## Method

one reading by hand at the first /retro, recorded in the estimate line

## Result

block 109.1: /retro of 2026-09-14 09:23 recorded its event, then its ledger substitution `cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null` exited 1 — no date-level ledger exists on the first day with the session form of case 103 alone — and the harness reported the substitution failed and did not load the skill text; the agent ran Retro from the SKILL.md file. Defer case 118.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L86
- 2026-09-11 updated: the frontier, the four outcomes, the readings and the red-test paths added; pending until the next live /retro · [[decision-case-56]]
- 2026-09-12 updated: the Deferred heading (cases 59.5, 66) · [[decision-case-66]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L106
- 2026-09-12 criterion: case 73.6 added · [[decision-case-73.6]]
- 2026-09-13 criterion: case 109.1 added · [[decision-case-109.1]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/0747/ledger.md#L50
