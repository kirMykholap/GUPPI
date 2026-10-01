---
type: rule
kind: Leaf
purpose: Prevents Plan Mode from stopping where no person is needed, between the reply that acknowledges the last ratification and /pre-spec, and between the ratification of the Cases built again on its findings and the exit
status: draft
enforcement: hook
implementation_ref: [guppi/onward.py, tests/test_onward.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-prespec-onward-sends-the-agent-on]]"]
origin: raw/2026-09-30/2356/ledger.md#case-561.5
sprint: migration
created: 2026-09-30
tags: [session, workflow, hooks, harness]
---

## Purpose

Prevents Plan Mode from stopping where no person is needed: between the reply that acknowledges the last ratification of the Frontier and `/pre-spec`, and between the ratification of the Cases built again on its findings and the exit. In Claude Code the end of a reply hands the turn to the person, and a reply that carries a `LEDGER` block ends in that text, so that the ledger hook writes it; so the agent cannot call `/pre-spec` or exit Plan Mode in that reply. This hook, `uv run guppi onward --plan` on `Stop`, sends the agent on in the same turn, as `rule-retro-onward` does after Retro (case 561.5). It judges only the state of files and of the payload — the `hi` and `prespec` marks of the session in the event log, `spec.md`, the open lines under `## Cases` of `frontier.md`, the files under `cases/` against the times of the decision lines in `ledger.md` and in the reply, the flag `stop_hook_active` and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a turn and cannot loop. With no `prespec` line it sends the agent to `/pre-spec`; with the line it sends the agent to run the check and exit Plan Mode, where the hook of `rule-prespec-hook` refuses the exit while the check prints a finding. A reply that opens with `STOP:` ends, for the case where only the person can go on. An error of the hook itself after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to go on, and on the re-fire it exits 0.

## History

- 2026-10-01 created · [[decision-case-561.5]]
- 2026-10-01 estimate estimate-prespec-onward-sends-the-agent-on added · [[decision-case-561.5]]
