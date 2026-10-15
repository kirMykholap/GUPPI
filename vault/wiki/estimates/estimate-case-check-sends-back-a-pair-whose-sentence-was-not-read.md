---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case sends back a pair whose sentence around a match no Read call of case-guppi on the page file, or on the file of the other Case that wrote into it, returned whole
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k unread_sentence
checked: 2026-10-07
origin: raw/2026-10-07/0636/ledger.md#case-711.3
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` whose Case carries a `replace` or `reword` pair on a page that stands on disk, and reads the record of the subagent at `agent_transcript_path`.

Then:
For each match of each pair of the Cases of the file — the one match of a `replace`, and each match of a `reword` on each live page — the hook takes the sentence around it on the page as the earlier pairs leave it, by the function of the sentence of `.guppi/guppi/prespec.py`.
**＋** The sentence counts as read when each part of it that no pair wrote stands whole in the outputs of the `Read` calls of the subagent on the page file, the line numbers of the output and the whitespace set aside.
**＋** A part of the sentence that a pair of another Case of the session wrote counts as read when it stands whole in the outputs of the `Read` calls of the subagent on the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of that Case.
**＋** A sentence not read is a finding of its Case: "case <N>: <slug>: the sentence around a pair was not read whole: <opening>: Read the page around it, and the file of each other Case that wrote into it, and check the pair."
**－** The output of a `Grep` call, or of any other tool than `Read`, is no read.
**－** A part of the sentence that a pair of the Cases of the file wrote is not judged.
**－** A transcript the hook cannot read, and a call of the check with no record of an agent, such as `.guppi/tests/test_case_schema.py` over the example of `vault/wiki/case-example.md`, judge no read.

## Result

2026-10-07, uv run pytest tests/test_casecheck.py -k unread_sentence: 6 passed, 192 deselected; tests/test_case_schema.py, a call with no record of an agent, gives the example no note: 2 passed

## History

- 2026-10-07 created · [[decision-case-711.3]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0636/ledger.md#L35
- 2026-10-07 updated: the Criterion written back with the example of tests/test_case_schema.py in vault/wiki/case-example.md (case 717.3) · [[decision-case-717.3]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/1804/ledger.md#L26
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
