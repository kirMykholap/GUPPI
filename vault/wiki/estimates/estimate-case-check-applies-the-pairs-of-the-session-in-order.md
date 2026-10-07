---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case applies the pairs of the other Cases of the session first and those of the file last, and sends back an old text of the file that then misses or hits more than once
method: uv run pytest tests/test_casecheck.py -k session_pairs
origin: raw/2026-10-07/0636/ledger.md#case-711.1
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `SubagentStop` hook `uv run guppi casecheck --subagent` of `guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` whose Case carries a `replace` or `reword` pair, while the plan file of the session or `<plan>.checked.json` holds other Cases of the session.

Then:
The hook applies the `replace` and `reword` pairs of the other Cases of the session first, in the order `other_blocks` gives them, and the pairs of the Cases of the file last, to copies of the pages in memory, by `check_pairs` of `guppi/prespec.py`, imported; nothing is written to disk.
**＋** An old text of a Case of the file that then misses, or hits more than once, is a finding of that Case in the words `check_pairs` gives it.
**＋** An old text of a Case of the file that hits once only after a pair of another Case is no finding, though the page on disk does not hold it.
**－** A finding of that run that opens with another Case is no finding of the file.
**－** The other Cases are those `other_blocks` gives: a dropped Case, a Case a `{supersedes:case N}` mark names, a stored Case with findings and the family of a Case of the file are not among them.
**－** With no other Case of the session, the pairs are judged against the pages on disk as before.

## Result

2026-10-07, Retro of session 0636, uv run pytest tests/test_casecheck.py -k session_pairs; 6 passed

## History

- 2026-10-07 created · [[decision-case-711.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0636/ledger.md#L33
