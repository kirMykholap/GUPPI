---
type: decision
case: "385"
status: archived
update: ["[[rule-synthesis]]", "[[rule-insights-schema]]", "[[estimate-synthesis-keeps-actioned-by-the-mark]]", "[[insight-workflow-contract-change-leaves-its-derived-text-stale]]"]
origin: raw/2026-09-23/1859/ledger.md#case-385
sprint: migration
created: 2026-09-23
tags: [harness, workflow, librarian, render, schema]
---

## Context

At synthesis the librarian hangs a new lesson as a child on an Insight of the same pattern. When the Insight stands `actioned` and the lesson entry carries `addressed_by`, case 284.4 keeps the Insight `actioned` and moves `addressed_by` to the lesson's decision. Case 361 says `addressed_by` is one link, the latest. The rule was written for a lesson of a later session, whose decision is then the latest. Session 1355 went otherwise: Case 378.5 closed `insight-workflow-contract-change-leaves-its-derived-text-stale`, and a lesson of the same session carried the mark of 378.4. The librarian followed 284.4 word for word and moved the field to the earlier 378.4, so the two rules parted. It is a judgment of the librarian, not code: `materialize` only puts `addressed_by` on the lesson entry. The Criterion of `estimate-synthesis-keeps-actioned-by-the-mark` speaks of the move, so it is replaced whole; it stands `pending` already. Every item is an `update` with a `ref`, so no vault query.

## Problem

Where does `addressed_by` of an `actioned` Insight point when the new lesson's decision is earlier than the one in the field: at the latest decision (case 361) or at the lesson's decision (case 284.4)?

## Given

`rule-synthesis` — its Render tells the librarian to move `addressed_by` (case 284.4).
**＋** `.claude/agents/librarian-guppi.md` — the file `rule-synthesis` renders into.
**＋** `rule-insights-schema` — its Render says one link, the latest (361), and describes the move of 284.4.
**＋** `vault/wiki/insights/schema.yaml` — the file `rule-insights-schema` renders into.
**＋** `estimate-synthesis-keeps-actioned-by-the-mark` — the Estimate of `rule-synthesis`; its Criterion speaks of the move.
**＋** `insight-workflow-contract-change-leaves-its-derived-text-stale` — the Insight whose field went to the earlier decision.
**＋** `decision-case-M` — the decision the Insight's `addressed_by` names before the synthesis.

## History

- 2026-09-24 created · raw/2026-09-23/1859/ledger.md#case-385
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
