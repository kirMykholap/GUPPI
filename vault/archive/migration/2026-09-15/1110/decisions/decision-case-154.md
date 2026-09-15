---
type: decision
case: "154"
status: archived
defer: ["[[rule-ask]]"]
superseded_by: ["[[decision-case-155]]"]
origin: raw/2026-09-14/1633/ledger.md#case-154
sprint: migration
created: 2026-09-14
tags: [session, workflow, harness]
---

## Context

`rule-ask` says "One short question per Case"; `CLAUDE.md` asks the vault before a `create` without a `ref` and at pre-task. Session P dispatched `ask-guppi` six times — before Cases 142, 143, 144, 145, before the Obsidian direction (147) and at pre-task — about 355k tokens in subagents; four of the six were `update`s with a `ref`, where the Insight page and two greps would have given the `given`.

## Problem

The owner finds six dispatches dearer than one and of less use. The main agent's practice from now: `ask-guppi` before a `create` without `ref` and at pre-task; for an `update` with `ref`, the page and a grep; the rule's text still says "per Case". Decide at the next Plan Mode whether `rule-ask`'s clause follows the practice.

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-154
- 2026-09-15 superseded by decision-case-155 · [[decision-case-155]]
- 2026-09-15 archived · superseded
- 2026-09-15 archived · cleanup
