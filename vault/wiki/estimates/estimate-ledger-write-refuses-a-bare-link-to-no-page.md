---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a reading or a lesson line whose text holds a bare link that names no page, says why only for the reply just finished, and judges the link by the one function that guppi check and pre-spec share
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py .guppi/tests/test_lint.py -k bare_link
origin: raw/2026-11-01/0141/ledger.md#case-977
sprint: plugin
created: 2026-11-01
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds, in a `LEDGER` block of a session with a `hi`, a fresh `estimate[...]` or `lesson[...]` line whose text holds a `[[name]]` outside a code span.

Then:
While the name is neither a live or archived page, nor a hub file of the wiki, nor a slug that a `create` decision line of the session's ledger or of the same `Stop` creates, the line is not written.
**＋** When the line stands in the reply just finished, the hook exits 2 with one stderr line, told once a stretch, that names the link and asks for the name in a code span or for the slug of a page.
**＋** A refused line of an earlier text is judged again at every `Stop` without a word, and is written at the first `Stop` where each such name passes.
**＋** One function of `.guppi/guppi/lint.py` judges the names a link outside a code span may carry; `lint.py` reads the body of a page by it, and `.guppi/guppi/prespec.py` and the hook import it.
**＋** A file `schema.md` in a category folder is no page for lint, for `.guppi/guppi/prespec.py` or for the hook.
**－** A lesson line refused for its link is not held for its mark.
**－** A `[[name]]` inside a code span is not judged.

## Result

2026-11-01, Retro of session 0141: uv run --project .guppi pytest .guppi/tests/test_ledger.py .guppi/tests/test_lint.py -k bare_link 14 passed, 269 deselected; uv run --project .guppi guppi test 1878 passed, 6 skipped, 1 deselected

## History

- 2026-11-01 created · [[decision-case-977]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/0141/ledger.md#L12
