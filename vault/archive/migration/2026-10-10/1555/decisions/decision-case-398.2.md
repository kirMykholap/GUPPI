---
type: decision
case: "398.2"
status: archived
update: ["[[estimate-generate-fails-alone]]"]
origin: raw/2026-09-24/1916/ledger.md#case-398.2
sprint: migration
created: 2026-09-24
tags: [harness, workflow, ledger, tests]
---

## Context

Three Estimates of `rule-page-generation` on the list of Case 378 open with the same `Given:` of five lines. The block has two faults:
- it is out of date: it says a part inside the Criterion sets `pending`, while since Case 378.4 that is `incomplete: [criterion]`;
- it holds a line on the bounds of an edit: "`materialize`, `cleanup` and `lint` do not change here".

Beyond that, `estimate-generate-writes-the-decision-page` is false today: its `－` line says "no `## Given`", while since Case 378.3 `generate` writes `## Given` (`decision` in `guppi/generate.py`); that promise belongs to `estimate-generate-writes-the-given`. `estimate-generate-cascades` repeats the recount of an Entity's `rules`, which belongs to `estimate-generate-writes-rules-from-applies-to`; the line goes and the `purpose` is set. In `estimate-generate-fails-alone` only `Given:` changes: its lines were checked against the code (`error`, `a recut without method`, `not lifted by materialize`, `an update with no content`) and all hold.

All three stand `passed`, `rule-page-generation` `built`; after the ratification the rule goes `draft` by the cascade. The readings are `pytest` with no change of code. The other seven Estimates of the rule are not on the list of eleven: `estimate-generate-writes` and `-walks-dates` are C10, the old shape; `-ticks-the-spec` is C8. Every item an `update` with a `ref`; `frame-guppi` was not dispatched: the behaviour of the rule does not change. The agent read the code itself.

## Problem

Three Criteria carry a `Given:` out of date; one of them promises what the code no longer does, another repeats a promise of another Estimate.

## Given

`estimate-generate-fails-alone` — the Estimate whose Criterion is replaced.
**＋** `guppi/generate.py` — `error`, the apply of an `update`, the loop over the entries.
**＋** `tests/test_generate.py` — fixes the failed, skipped and marked entries.
**＋** `vault/raw/<date>/<HHMM>/materialize.yaml` — the entries and their marks.
**＋** `vault/wiki/log.md` — the feed of page changes.

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-398.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
