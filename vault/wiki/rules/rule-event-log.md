---
type: rule
kind: Leaf
purpose: Prevents the ledger from being written into a session nothing recorded
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/event.py, .guppi/guppi/gate.py, .guppi/guppi/cli.py, .guppi/tests/test_gate.py, .guppi/tests/test_event.py, .claude/settings.json]
parent: "[[rule-session-start]]"
estimates: ["[[estimate-event-log-records]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness]
core: true
---

## Purpose

Prevents the ledger from being written into a session nothing recorded. The event log is
the noisy record of a session — starts, tool calls, agent dispatches, commits, test runs —
written by hooks rather than by instructions, so it still fills when the agent deviates or
crashes. It is gitignored: debugging material, not traceability. Its governance jobs: to carry the `hi` mark that tells the ledger hook a working session is open, and to name the session's plan file by its `tool Write:` and `tool Edit:` lines for `guppi gate`.

## History

- 2026-11-03 shipped with GUPPI
