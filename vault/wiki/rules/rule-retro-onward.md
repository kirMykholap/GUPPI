---
type: rule
kind: Leaf
purpose: Prevents the run from stopping between the reply that ends Retro and /handoff, where no person is needed
status: draft
enforcement: hook
implementation_ref: [guppi/onward.py, tests/test_onward.py, .claude/settings.json]
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-retro-onward-sends-the-agent-to-the-handoff]]", "[[estimate-retro-onward-exits-2-on-an-error]]"]
origin: raw/2026-09-29/2024/ledger.md#case-531.9
sprint: migration
created: 2026-09-29
tags: [session, workflow, hooks, harness]
---

## Purpose

Prevents the run from stopping between the reply that ends Retro and /handoff, where no person is needed. In Claude Code the end of a reply hands the turn to the person, and the ledger hook writes the lines of a reply only when it ends; so Retro ends one reply with its `LEDGER` block, and this hook sends the agent on to `/handoff` in the same turn (case 531.9). It judges only the state of files and of the payload — the mark `retro` of the session in the event log, the absence of `handoff.md`, the flag `stop_hook_active` and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a turn and cannot loop. An error of the hook itself after it has read the payload — an exception while it reads the reply, the session folder or the event log — exits 2 with `onward: not checked: <error>` on stderr and the advice to commit the session folder and call `/handoff` if Retro has ended and `handoff.md` does not stand, so the agent sees it, before Retro too; on the re-fire it exits 0, so this too fires at most once a turn (case 555.3). A deliberate stop is a reply that opens with `STOP:`, on a condition of `rule-where-to-stop`.

## History

- 2026-09-30 created · [[decision-case-531.9]]
- 2026-09-30 estimate estimate-retro-onward-sends-the-agent-to-the-handoff added · [[decision-case-531.9]]
- 2026-09-30 updated: the hook exits 2 on its own error after the payload is read, with the advice to call /handoff (case 555.3) · [[decision-case-555.3]]
- 2026-09-30 estimate estimate-retro-onward-exits-2-on-an-error added · [[decision-case-555.3]]
