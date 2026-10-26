---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case takes another Case of the session that was built again after its ratification as its stored text holds it, in place of the plan file, in every judgment that reads the other Cases, so that the words its pairs wrote are found in a read of its file
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k built_again_sibling
origin: raw/2026-10-26/0118/ledger.md#case-890.1
sprint: plugin
created: 2026-10-26
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file under `raw/<date>/<hi HHMM>/cases/`, while the plan file of the session holds another Case that `<plan>.checked.json` holds under its number alone with another text, since it was built again after its ratification.

Then:
The hook takes that other Case as `<plan>.checked.json` holds it, in place of its text in the plan file, when its entry holds no finding and the file under `raw/<date>/<hi HHMM>/cases/` of its top-level Case holds its heading.
**＋** It takes it so in each judgment that reads the other Cases of the session through `other_blocks` of `.guppi/guppi/casecheck.py`: the clash of two Cases, the order of the `replace` and `reword` pairs, the read of the sentence around each pair, and the notes of the cascade.
**＋** A part of a sentence that a pair of that other Case wrote then counts as read when it stands whole in the outputs of the `Read` calls of the subagent on the file of that Case.
**＋** The other Cases keep the order of the plan file, and the entries the plan file does not hold come after them, as before.
**－** An entry with findings, an entry joined with an agent id, and an entry whose top-level file is empty or no longer holds its heading leave the other Case as the plan file holds it.
**－** The hook writes nothing to the plan file or to `<plan>.checked.json` for this judgment.

## Result

2026-10-26, Retro of 0118, uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k built_again_sibling: 4 passed; a part a Case built again wrote is found in a Read of its file, an old text only the plan's version wrote is a finding of check_pairs, an entry with findings and a file without its heading leave the plan's text; the first two fail on the old casecheck.py

## History

- 2026-10-26 created · [[decision-case-890.1]]
- 2026-10-26 status: pending → passed · raw/2026-10-26/0118/ledger.md#L20
