---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case sends a note once when a pair of the file changes a sentence into which a pair of another Case of the session wrote
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k shared_sentence
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` applies the pairs of the other Cases of the session and then those of a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `check_pairs` of `.guppi/guppi/prespec.py`.

Then:
`check_pairs` records the text that each pair writes into a page, with the Case of the pair.
**＋** The sentence around a place runs back to the last full stop before it that a space and a capital letter follow, or to the start of its paragraph, and on to the next such full stop or to the end of its paragraph, by one function of `.guppi/guppi/prespec.py`.
**＋** When the sentence around the match of a pair of a Case of the file holds text that a pair of another Case of the session wrote, the hook gives a note of the Case of the file that names the other Case, the page and the opening of the sentence: "case <N>: <slug>: a pair changes a sentence that case <M> changes too: <opening>: read both new texts side by side, and fix the pair or say in context why the two fit."
**＋** The note goes where a note of a Criterion line not carried goes: it is sent back once by exit 2 beside any findings, stored under `notes` in `<plan>.checked.json`, and not sent again for the same Case id.
**－** The note is no finding: the Case is stored with no finding for it, and the `Stop` check of `guppi casecheck` does not refuse a showing for it.
**－** Two pairs of the Cases of the file in one sentence give no note, and neither do two pairs of other Cases.
**－** `uv run --project .guppi guppi prespec --check` does not print the note.

## Result

2026-10-07, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
