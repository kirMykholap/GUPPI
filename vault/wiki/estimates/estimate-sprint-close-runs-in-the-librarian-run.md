---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint-close]]"
purpose: Whether the close of a sprint runs in the librarian's run of a session of its own, from the task line of its closing Case, after guppi generate and before guppi cleanup, so that the readings of that session count, with Work Mode leaving the line, Retro not counting it as debt and the command ticking it
method: "pytest tests/test_sprint_close.py -k tick; by hand, after the librarian's run of the session that closes a sprint: its ledger, spec.md, handoff.md, the librarian's event log and report, and vault/archive/"
origin: raw/2026-10-04/1439/ledger.md#case-628.1
sprint: migration
created: 2026-10-04
tags: [sprint, workflow, librarian]
---

## Criterion

When:
The session that closes `entity-sprint-<id>` runs from `/hi` to the librarian's run, its closing Case holding the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choices; someone reads its ledger, its `spec.md`, its `handoff.md`, the librarian's event log and report, and `vault/archive/` after it.
**＋** Or `tests/test_sprint_close.py` runs `guppi sprint-close --apply` over a made-up vault whose `spec.md` holds that line.

Then:
The ledger of the session holds the decision lines of the closing Case and of the Cases that prepare its readings, and no other decision line but a `defer`.
**＋** Work Mode neither runs nor ticks the close line, and the handoff does not name it as debt.
**＋** The librarian runs the line as it stands after `guppi generate` and before `guppi cleanup`, and a reading that the session's ledger holds is applied before the command reads the Estimates.
**＋** After a run that moved the pages, the line stands ticked in `spec.md`, found by `command_line` of `guppi/render.py`.
**－** A run that refuses moves nothing and ticks nothing, and the librarian names its stderr lines as flags.

## History

- 2026-10-04 created · [[decision-case-628.1]]
