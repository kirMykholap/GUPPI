---
type: rule
kind: Leaf
purpose: Prevents the ledger from being written into a session nothing recorded
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/event.py, .guppi/guppi/gate.py, .guppi/guppi/cli.py, .guppi/tests/test_gate.py, .guppi/tests/test_event.py, .claude/settings.json]
parent: "[[rule-session-start]]"
estimates: ["[[estimate-event-log-records]]"]
origin: raw/2026-09-09/ledger.md#case-9
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness]
core: true
---

## Purpose

Prevents the ledger from being written into a session nothing recorded. The event log is
the noisy record of a session — starts, tool calls, agent dispatches, commits, test runs —
written by hooks rather than by instructions, so it still fills when the agent deviates or
crashes. It is gitignored: debugging material, not traceability. Its governance jobs: to carry the `hi` mark that tells the ledger hook a working session is open, and to name the session's plan file by its `tool Write:` and `tool Edit:` lines for `guppi gate` (case 122).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-9
- 2026-09-10 status: draft → built · cascade
- 2026-09-14 updated: the hi line is written by guppi event prompt on UserPromptSubmit with the session's stamp, once per session; the known limit is lifted (case 111.1) · [[decision-case-111.1]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-14 updated: the prompt hook prints the hi it wrote, or the one already recorded, with the session's folder, into the context (case 125) · [[decision-case-125]]
- 2026-09-14 updated: the event log's second governance job, the plan path for guppi gate, named (case 132) · [[decision-case-132]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: the marks pretask, retro, handoff written by guppi gate with the session's stamp; the skills' Recorded lines dropped (case 136.1) · [[decision-case-136.1]]
- 2026-09-15 updated: the marks name the second entry of the gate, the typed command on UserPromptSubmit (case 169.1) · [[decision-case-169.1]]
- 2026-09-27 updated: no hi line outside plan mode; the refusal exits 2 (case 445.6) · [[decision-case-445.6]]
- 2026-09-27 status: built → draft · cascade
- 2026-10-03 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the history of the marks stands in the bracket of its pointer · [[decision-case-809]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-26 updated: the label of the stamp paragraph says what holds, not what was lifted · [[decision-case-881.18]]
- 2026-10-30 updated: ## How it works left the Leaf, its mechanism in the docstrings of .guppi/guppi/event.py and .guppi/guppi/gate.py · [[decision-case-942.1]]
