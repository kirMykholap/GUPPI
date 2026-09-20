---
type: estimate
kind: QA
status: passed
target: "[[rule-retro-commit]]"
method: pytest in tests/test_gate.py with piped payloads against a temp repository; the live reading once by hand
checked: 2026-09-20
origin: raw/2026-09-10/ledger.md#case-38.2
sprint: migration
created: 2026-09-10
tags: [session, workflow, hooks, harness, git]
---

## Criterion

Given:
`guppi gate` runs on `PreToolUse` for `Skill` and on `UserPromptSubmit` for a typed `/pre-spec`, `/retro` or `/handoff`, with or without arguments; a refusal is exit 2 with the reason on stderr, and the client blocks the call.

When:
The gate receives such a call or prompt.

Then:
`handoff`: a dirty tree — exit 2, the reason "commit first"; a clean tree — exit 0; live, the first `/handoff` from Retro on a dirty tree is refused and passes after the commit.
**＋** `/retro`: with a `hi` but no `spec.md` in the session's folder, no plan file named by the event log and no `- decision[`, `- estimate[` or `- lesson[` line in the window — exit 2, "gate: /retro refused — nothing to review: no Spec and no ledger line in raw/<date>/<HHMM>/. Ratify a Case or write a reading or a lesson first, then type /retro again.", on the `Skill` path "…then call /retro in the next reply."; otherwise the check of the Spec against the session's ledger — N items without a line — exit 2, "gate: /retro refused — N item(s) of the Spec have no ledger line (case A). Ask the agent to end its reply with the LEDGER block, then type /retro again".
**＋** Letting through, on either path it writes the same mark `prespec`/`retro`/`handoff` into the event log; a refusal writes no mark.
**＋** Any other prompt or skill, `/hi` included — exit 0, no output, no mark; without `hi` — nothing to check, exit 0.
**－** `guppi event prompt` does not change and does not fail.

## Result

2026-09-20, `uv run pytest -q tests/test_gate.py` 30 green after the recut; live, the typed /retro of session 0958 passed the gate with the mark `12:54:19 c27cd9be retro` in raw/2026-09-20/event_log.md — 29 lines of the session's ledger, every item of the Spec with its line; the refusal of /handoff on a dirty tree is not played in this session, the commit precedes the call, and stands in the Result from session 1034

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L78
- 2026-09-15 criterion: case 169.1 added · [[decision-case-169.1]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L1
- 2026-09-16 criterion: case 180 added · [[decision-case-180]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1034/ledger.md#L1
- 2026-09-20 updated: the recut to the shape of case 193: the base text and the blocks 169.1, 180 folded into one Criterion, /pre-task and pretask now /pre-spec and prespec, method as a field; pending for the reading (case 265.2) · [[decision-case-265.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L30
