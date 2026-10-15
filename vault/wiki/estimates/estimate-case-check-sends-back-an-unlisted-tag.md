---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case sends back a Case whose create, set of tags or decision line carries a tag that tags.md does not hold and no tag line of the file or of a ratified Case of the session declares
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k unlisted_tag
origin: raw/2026-10-07/0636/ledger.md#case-703.1
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` whose Case carries a tag in the `tags` of a `create`, in `tags` under the `set` of an `update`, or in a `{tags:...}` block of a decision line of its `ratification`.

Then:
A tag that no row of `vault/wiki/tags.md` holds is a finding of its Case: "case <N>: tag <tag> is not in tags.md: use a tag of tags.md, or declare it by a tag line in this Case."
**＋** A tag that a `tag` line of the same file declares is no finding.
**＋** A tag that a `tag` line of another Case of the session declares is no finding when a decision line of that Case stands in the session's ledger; the hook reads that tag line from the text of that Case as the check stored it.
**＋** `.guppi/guppi/casecheck.py` and `.guppi/guppi/generate.py` read the rows of `vault/wiki/tags.md` by one function of `.guppi/guppi/tags.py`.
**－** A tag line of a Case of the session with no decision line in the session's ledger does not make a tag listed.
**－** Where `vault/wiki/tags.md` does not stand, no tag is judged.

## Result

2026-10-07, Retro of session 0636, uv run pytest tests/test_casecheck.py -k unlisted_tag; 8 passed

## History

- 2026-10-07 created · [[decision-case-703.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0636/ledger.md#L29
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
