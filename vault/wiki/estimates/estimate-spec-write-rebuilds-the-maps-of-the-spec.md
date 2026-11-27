---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the map of each approved document of spec.md that holds one is rebuilt from the Cases and the boxes of that document after each edit of the file and after each write of the Stop hook into it, whether an edit of the session's own spec.md rebuilds the map of the plan file too, and whether the hook after an edit changes no other file and refuses nothing
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k spec_map
checked: 2026-11-28
origin: raw/2026-11-27/1402/ledger.md#case-1085.2
sprint: plugin
created: 2026-11-27
tags: [hooks, harness, workflow]
---

## Criterion

When:
The agent's `Edit`, `Write` or `MultiEdit` of a `spec.md` in a session folder `vault/raw/<date>/<HHMM>/` ends, and `uv run --project .guppi guppi ratified --boxes` of `.guppi/guppi/ratified.py` runs on its `PostToolUse`.
**＋** Or the `Stop` hook `uv run --project .guppi guppi ratified` writes, places or removes a Case or a defer in `raw/<date>/<hi HHMM>/spec.md`.

Then:
Each approved document of that `spec.md` that holds a map has its map rebuilt from the Cases and the boxes of that document, in the form of the map of the plan file.
**＋** A document that holds no map gets none.
**＋** The line that opens each map of `spec.md` says that each box copies the box of its task line below and is no task of its own; the line that opens the map of the plan file names its Cases file `<plan stem>.cases.md` in place of below.
**＋** After an edit of the `spec.md` of the session's own folder, `--boxes` also rebuilds the map of the plan file of the session, with its boxes taken from that `spec.md`.
**＋** `--boxes` refuses no call, prints nothing on stdout and exits 0; an error gives one line on stderr.
**－** `--boxes` changes no file after an edit of any other file.

## Result

2026-11-28, Retro of session 2214, uv run --project .guppi pytest .guppi/tests/test_ratified.py -k spec_map: 9 passed; against Case 1087.2: the map of spec.md is rebuilt with MAP_HEAD after the plan text with its Cases file lands there, and the map of the plan file rebuilt after an edit of the session's spec.md opens with the line that names its Cases file

## History

- 2026-11-27 created · [[decision-case-1085.2]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/1402/ledger.md#L21
- 2026-11-28 updated: the Criterion replaced whole — the head line of the map of the plan file names its Cases file · [[decision-case-1087.2]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L31
