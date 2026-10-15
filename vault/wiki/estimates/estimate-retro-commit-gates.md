---
type: estimate
kind: QA
status: passed
target: "[[rule-retro-commit]]"
purpose: guppi gate refuses /handoff on a dirty tree and /retro with nothing to review or a Spec ahead of the ledger, and marks each call it lets through
method: pytest in .guppi/tests/test_gate.py with piped payloads against a temp repository; the live reading once by hand
checked: 2026-09-30
origin: raw/2026-09-10/ledger.md#case-38.2
sprint: migration
created: 2026-09-10
tags: [session, workflow, hooks, harness, git]
---

## Criterion

When:
`guppi gate` receives a `PreToolUse` payload of a `Skill` call, or a `UserPromptSubmit` payload whose prompt, trimmed, opens with one of the three commands the gate marks, with or without arguments.

Then:
A `/handoff` on a dirty tree, where `git status --porcelain` is not empty, exits 2 with the reason "commit first" on stderr, and the client blocks the call; on a clean tree it exits 0.
**＋** A `/retro` in a session with a `hi` but no `spec.md` in its folder, no plan file named by the event log and no `- decision[`, `- estimate[` or `- lesson[` line in its window exits 2 with "gate: /retro refused — nothing to review: no Spec and no ledger line in raw/<date>/<HHMM>/. Ratify a Case or write a reading or a lesson first, then type /retro again."; on the `Skill` path the end reads "…first. This refusal is a stop of vault/wiki/where-to-stop.md: end your reply with the question to the person."
**＋** Otherwise a `/retro` whose Spec holds an item with no decision line of its Case exits 2 with "gate: /retro refused — N item(s) of the Spec have no ledger line (case A). Ask the agent to end its reply with the LEDGER block, then type /retro again".
**＋** A call it lets through, on either path, writes the same mark `prespec`, `retro` or `handoff` into the day's event log `vault/raw/<date>/event_log.md`; a refusal writes no mark.
**＋** Any other prompt or skill, `/hi` included, exits 0 with no output and no mark.
**－** Without a `hi` in the session, the checks of `/retro` do not run.
**－** On the `Skill` path the refusal "nothing to review" asks for no call in a next reply.

## Result

2026-09-30, uv run pytest tests/test_gate.py: 30 passed; live in session 2042: the Skill call of /pre-spec wrote the mark prespec at 23:04:05 and the Skill call of /retro was let through and wrote the mark retro at 23:45:07; no refusal of the gate met live

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L78
- 2026-09-15 criterion: case 169.1 added · [[decision-case-169.1]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L1
- 2026-09-16 criterion: case 180 added · [[decision-case-180]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1034/ledger.md#L1
- 2026-09-20 updated: the recut to the shape of case 193: the base text and the blocks 169.1, 180 folded into one Criterion, /pre-task and pretask now /pre-spec and prespec, method as a field; pending for the reading (case 265.2) · [[decision-case-265.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L30
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out, the pass without hi narrowed to what the gate does; purpose set (case 493.3) · [[decision-case-493.3]]
- 2026-09-30 updated: the Criterion replaced whole — on the Skill path the refusal nothing to review names a stop of vault/wiki/where-to-stop.md, not a call in the next reply (case 531.15) · [[decision-case-531.15]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/2042/ledger.md#L34
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
