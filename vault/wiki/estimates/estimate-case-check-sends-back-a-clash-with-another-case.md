---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of an answer of case-guppi sends back a Case that sets one field, writes one section or replaces one Criterion that another Case of the session, ratified or only stored, sets, writes or replaces too; a dropped Case, whose file is empty, a stored Case that the file of its top-level Case no longer holds, and a Case left out as estimate-case-check-leaves-out-a-case-the-file-supersedes sets are no such other Case
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k session_clash
checked: 2026-10-26
origin: raw/2026-10-04/1439/ledger.md#case-629.1
sprint: migration
created: 2026-10-04
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
**＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up plan file, store and ledger.

Then:
The hook judges the Cases of the answer together with the other Cases of the session by `check_same_target` of `.guppi/guppi/prespec.py`, imported, not copied: each Case of the plan file, as `estimate-case-check-takes-a-case-built-again-from-its-file` sets it for a Case built again after its ratification, and each entry of `<plan>.checked.json` under its number alone whose id the plan file does not hold.
**＋** A Case of the answer whose `update` of a page sets one field to another value than another Case, writes a section that another Case writes, or replaces whole the Criterion of an Estimate that another Case replaces whole, gets a finding that names both Cases, the page and the field or the section.
**＋** The finding is stored with the Case, the hook exits 2, and `case-guppi` answers again before the main agent shows the Case.
**－** A stored Case that has findings, an entry joined with an agent id, a Case whose number a `{supersedes:case N}` mark of the session's ledger names, and a Case left out as `estimate-case-check-leaves-out-a-case-the-file-supersedes` sets are not compared.
**－** A stored Case whose top-level file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds nothing but blank space is a dropped Case and is not compared, judged by the one function of `.guppi/guppi/casecheck.py` that the hook of `rule-prespec-onward` uses too.
**－** A stored Case whose top-level file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds text but no heading of its id is a part that a Case built again no longer holds, and is not compared; its entry stays in the store.
**－** A Case whose id the answer holds is compared only as the answer holds it, and an answer that holds a top-level Case is compared with no part of that Case's family in the plan file or the store.
**－** Two other Cases that clash with each other give this answer no finding.
**－** The `Stop` hook `uv run --project .guppi guppi ratified` keeps its check of the Cases it writes, by the same function.

## Result

2026-10-26, Retro of 0118, uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k session_clash: 13 passed; the new test compares the answer with the stored value `draft` of Case 5 built again, not with the plan's `built`, and fails on the old casecheck.py

## History

- 2026-10-04 created · [[decision-case-629.1]]
- 2026-10-05 updated: the Criterion replaced whole — the step of case-guppi and of the main agent after a clash is no longer part of the promise; the method is pytest alone (case 637.2) · [[decision-case-637.2]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/0109/ledger.md#L1
- 2026-10-07 updated: the Criterion replaced whole — a dropped Case, whose file is empty, is not compared (case 701.7) · [[decision-case-701.7]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0425/ledger.md#L21
- 2026-10-07 updated: the Criterion replaced whole — a stored Case that the file of its top-level Case no longer holds is not compared (case 722.1) · [[decision-case-722.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/2114/ledger.md#L19
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-26 updated: the Criterion replaced whole — a Case of the plan built again after its ratification is compared as its stored text holds it · [[decision-case-890.2]]
- 2026-10-26 status: pending → passed · raw/2026-10-26/0118/ledger.md#L21
