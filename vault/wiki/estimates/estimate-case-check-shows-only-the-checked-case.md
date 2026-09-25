---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: The main agent shows a Case only as case-guppi answered it and the checks passed it
method: uv run pytest tests/test_casecheck.py -k stop, then by hand the first reply the hook refuses
checked: 2026-09-25
origin: raw/2026-09-25/1228/ledger.md#case-419.4
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
`Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

Then:
`uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json`, line by line once line ends and trailing spaces are the same.
**＋** A Case the store does not hold, a Case whose text differs from the stored one, or a Case stored with findings exits 2, the reason and the findings on stderr.
**＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
**－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared.
**－** On the re-fire (`stop_hook_active`) it exits 0.

## Result

2026-09-25, uv run pytest tests/test_casecheck.py -k stop: 8 passed; by hand, the first reply the hook refused in session 1654: the showing of Case 428 whose 428.3 ratification differed from the answer of case-guppi, refused with `case 428.3: differs from the answer of case-guppi — show that answer unchanged`; the acknowledging replies and the DIFF of the pre-spec prose fixes were not compared

## History

- 2026-09-25 created · [[decision-case-419.4]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1654/ledger.md#L26
