---
type: decision
case: "377.1"
status: archived
update: ["[[insight-session-vault-knowledge-not-loaded]]"]
origin: raw/2026-09-23/1355/ledger.md#case-377.1
sprint: migration
created: 2026-09-23
tags: [harness, workflow]
---

## Context

The Insight `insight-session-vault-knowledge-not-loaded` holds one pattern: a fact the vault holds does not reach the session that needs it. Each child so far was closed by moving the fact into a text loaded at the phase that needs it. The seventh child is `lesson-plan-mode-frontier-refused-at-hi-again`. In session 1126, Case 363 wrote the leave of plan mode into the Render of `rule-skill-hi`; at the `/hi` of this session plan mode was on, and the agent wrote `frontier.md` with no refusal.
The Insight opened again all the same, because of the order of the ledger lines. The refusal came at `/hi`; the decision lines of 363 were written at 11:33, the lesson line at 13:26, at Retro, as the last line of the ledger. The mark `{addresses:<lesson slug>}` stands on a decision line only when the lesson line already stands in the ledger (case 284.2), so there was nowhere to put it. Case 284.2 forbade the reverse mark: "no `{addressed_by}` on the lesson line"; it assumed a lesson line always comes before its fix, and that assumption failed. The synthesis sees only `addressed_by` on the lesson entry of the yaml, whichever line set it.
The mark on the lesson line is written into the Case schema by Case 379, which replaced 377.2 in the model of Case 378; the Insight (377.1) and the carrying of the mark by `materialize` (377.3) stay here. The Insight stands `open`, severity 1, one live child; `rule-materialize` stands `built`; every item an `update` with a `ref`, so no vault query.

## Problem

A lesson can reach the ledger after the decision that already closed its cause. Then the mark has no place, the synthesis opens the Insight again, and a Case is spent on a fact the yaml already holds. Apart from that, the Insight stands `open` now.

## Given

`insight-session-vault-knowledge-not-loaded` — the Insight the Case sets `actioned`.
**＋** `lesson-plan-mode-frontier-refused-at-hi-again` — its live child.
**＋** `rule-skill-hi` — its Render says plan mode does not stop the write of the Frontier (case 363).
**＋** `/hi` — the skill that assembles the Frontier.

## History

- 2026-09-23 created · raw/2026-09-23/1355/ledger.md#case-377.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
