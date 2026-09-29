---
type: rule
kind: Leaf
purpose: Prevents the run from stopping between the reply that ends Retro and /handoff, where no person is needed
status: draft
enforcement: hook
implementation_ref: [guppi/onward.py, tests/test_onward.py, .claude/settings.json]
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-retro-onward-sends-the-agent-to-the-handoff]]"]
origin: raw/2026-09-29/2024/ledger.md#case-531.9
sprint: migration
created: 2026-09-29
tags: [session, workflow, hooks, harness]
---

## Purpose

Prevents the run from stopping between the reply that ends Retro and /handoff, where no person is needed. In Claude Code the end of a reply hands the turn to the person, and the ledger hook writes the lines of a reply only when it ends; so Retro ends one reply with its `LEDGER` block, and this hook sends the agent on to `/handoff` in the same turn (case 531.9). It judges only the state of files and of the payload — the mark `retro` of the session in the event log, the absence of `handoff.md`, the flag `stop_hook_active` and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a turn and cannot loop. A deliberate stop is a reply that opens with `STOP:`, on a condition of `rule-where-to-stop`.

## History

- 2026-09-30 created · [[decision-case-531.9]]
- 2026-09-30 estimate estimate-retro-onward-sends-the-agent-to-the-handoff added · [[decision-case-531.9]]
