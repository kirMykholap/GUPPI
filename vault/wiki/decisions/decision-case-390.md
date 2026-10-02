---
type: decision
case: "390"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-orchestration-acknowledging-reply]]"]
supersedes: ["[[decision-case-389]]"]
origin: raw/2026-09-24/1303/ledger.md#case-390
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Context

Since Case 387.2 the `Stop` hook of `rule-spec-write` writes a Case into the Spec only after a reply whose `LEDGER` block holds that Case's decision lines. When a Case is shown again and ratified again, its lines are the same as the ones already written. The ledger hook skips a line that already stands in any `ledger.md` under `raw/` (`guppi/ledger.py`, docstring). So in session 1859 the agent acknowledged the re-ratification of 384–388 without the block, and with the hook live those texts would not have reached the Spec. The schema does not forbid it: the section `## The acknowledging reply` of `rule-case-protocol` is silent on a re-ratification. The code needs no change: `stop()` in `guppi/ratified.py` takes the lines from the reply itself, not from the ledger, finds the last showing of the Case and replaces its section in the plan and in the ratified copy. Repeating the lines does no harm: the ledger does not write them twice. `rule-case-protocol` stands `draft`. No vault query: every item is an `update` with a `ref`. Read against the Case: `rule-spec-write`, `estimate-spec-write-copies-the-ratified-case` and `guppi/ledger.py`; no contradiction. `estimate-orchestration-acknowledging-reply` speaks of the form of the acknowledging reply, so its Criterion is replaced whole, written in the model of Case 378: no `Given:` and no `－` line on the bounds of the measurement. `estimate-case-protocol-loaded` is not touched: its Criterion, still in the old model, lists the paragraphs of the Render, and the one pass of Slice 3g rewrites it whole (378.1); it is not read before that. `estimate-spec-write-copies-the-ratified-case` already asks for a reply with the `LEDGER` block and is not touched either.

## Problem

A re-ratified Case can stay out of the Spec: the schema lets the reply that acknowledges a re-ratification go without its `LEDGER` block.

## Given

`rule-case-protocol` — the section `## The acknowledging reply` of its Render.
**＋** `vault/wiki/case-schema.md` — the Render, written by `uv run guppi render`.
**＋** `estimate-orchestration-acknowledging-reply` — the Estimate of the acknowledging reply.
**＋** `rule-spec-write` — its `Stop` hook writes a Case into the Spec after a reply whose `LEDGER` block holds the Case's decision lines.
**＋** `rule-ledger-write` — the ledger hook, which appends each line once.

## History

- 2026-09-24 created · raw/2026-09-24/1303/ledger.md#case-390
