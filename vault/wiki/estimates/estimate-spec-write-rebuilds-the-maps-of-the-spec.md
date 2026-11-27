---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the map of each approved document of spec.md that holds one is rebuilt from the Cases and the boxes of that document after each edit of the file and after each write of the Stop hook into it, whether an edit of the session's own spec.md rebuilds the map of the plan file too, and whether the hook after an edit changes no other file and refuses nothing
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k spec_map
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
**＋** The line that opens each map, in `spec.md` and in the plan file, says that each box copies the box of its task line below and is no task of its own.
**＋** After an edit of the `spec.md` of the session's own folder, `--boxes` also rebuilds the map of the plan file of the session, with its boxes taken from that `spec.md`.
**＋** `--boxes` refuses no call, prints nothing on stdout and exits 0; an error gives one line on stderr.
**－** `--boxes` changes no file after an edit of any other file.

## Result

2026-11-27, uv run --project .guppi pytest .guppi/tests/test_ratified.py -k spec_map, Retro of session 1402: 8 passed; two approved documents each rebuilt from their own Cases after an edit by --boxes, a document with no map left with none, the plan map rebuilt after an edit of the session's spec.md and left after an edit of another session's, a file that is no spec.md of a session folder left as it was, exit 0 with nothing on stdout on an unreadable payload, an error as one line on stderr, and the map of spec.md rebuilt after the Stop hook places a Case

## History

- 2026-11-27 created · [[decision-case-1085.2]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/1402/ledger.md#L21
