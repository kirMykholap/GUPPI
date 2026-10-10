---
type: decision
case: "401.6"
status: archived
update: ["[[estimate-generate-ticks-the-spec]]"]
origin: raw/2026-09-24/1916/ledger.md#case-401.6
sprint: migration
created: 2026-09-24
tags: [harness, workflow, ledger]
---

## Context

The note of the journals in Slice 3g names three pages; only one of them is a real journal. `estimate-lint-catches`, the one Estimate of `rule-lint`, holds 12 `＋` lines in `then` and 2 in `Given:`, most of them one class of finding each and one line three classes, while `guppi/lint.py` checks 14 classes; a broken class turns the whole of lint `failed`. In the other two the long part is `Given:`, not `then`:
- `estimate-generate-ticks-the-spec` holds 5 `＋` lines in `then` and 8 lines of the history of cases 130.2–320 in `Given:`;
- `estimate-materialize-skips-a-carried-over-unit` holds one line in `then` and 10 lines in `Given:` written at Case 190.3 ("the slug is free", "`governs` is one file", "the word parked is not used").

For these two it is enough to remove `Given:` and the lines on the bounds of an edit; the other lines were checked against the code. Lint is cut by the functions of `guppi/lint.py`, by what a finding is about:
- the run, the schema, the layout, the paths and the markers stay in `estimate-lint-catches`;
- links: `check_refs`, `check_edges`, `check_criterion`, `check_origin`, `check_decision`, `check_orphans`;
- statuses: `check_status`, `check_unread`, `check_deferred`;
- `method`;
- the `unmigrated` count.

The four new slugs are free. All three pages stand `passed`; `rule-lint`, `rule-page-generation` and `rule-materialize` stand `built` and go `draft` by the cascade until the readings. The readings are `pytest` with no change of code. The note of the journals leaves Slice 3g in 401.8. Every item with a `ref`; `frame-guppi` was not dispatched. The agent read the code itself.

## Problem

One Criterion holds the fourteen classes of lint, which break and are fixed apart; in the two other Criteria `Given:` retells the history of their Case.

## Given

`estimate-generate-ticks-the-spec` — the Estimate whose Criterion is replaced.
**＋** `guppi/generate.py` — the ticker of page lines and `read` lines, `READ_LINE`.
**＋** `vault/raw/<date>/<HHMM>/` — `spec.md` and `materialize.yaml` of each session.
**＋** `vault/archive/` — the archived sessions, whose Specs are not read.
**＋** `tests/test_generate.py` — fixes the ticks.

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-401.6
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
