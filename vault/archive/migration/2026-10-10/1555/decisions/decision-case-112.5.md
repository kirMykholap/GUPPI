---
type: decision
case: "112.5"
status: archived
update: ["[[estimate-cleanup-moves]]"]
origin: raw/2026-09-14/0747/ledger.md#case-112.5
sprint: migration
created: 2026-09-14
tags: [harness, workflow]
---

## Context

F8 (e): seven findings of `guppi lint` that are wording, not behaviour — four `method`, two `## Context`, one `ref` — and the two wordings of `estimate-cleanup-moves` the brief flags every run. Each has stood for two or more librarian runs.

## Problem

Two of the four `method` findings are not the pages' fault: `estimate-documentation-completes` and `estimate-harness-pipeline` name a `make` target and add "the live reading by hand"; `check_method` (`lint.py:435-441`) tests for the words "by hand" before it looks for the target, so a MOC's Estimate that names both is flagged. The other five are pages with something missing or stale.

## Given

`rule-lint` (`built`, one Estimate `estimate-lint-catches`, `passed`): the Method classes of case 26.2 and 28 — a Leaf's Estimate names a `tests/` file or says "by hand"; a MOC's names a `make <target>`, or says "by hand" when every child's Estimate is by hand.
**＋** `estimate-default-mode` (target `rule-default-mode`, Leaf): Method names no `tests/` file; `tests/test_render.py` is the test that checks `defaultMode` in the rendered `settings.json`.
**＋** `estimate-settings` (target `rule-settings`, MOC, child of `rule-harness`): Method names no `make` target; `make test-harness` is the pipeline over `rule-harness`'s children.
**＋** `estimate-generate-walks-dates` and `estimate-materialize-walks-dates`: no `## Context`; both born of case 43, whose Problem on `decision-case-43` is in Russian — the Context is its English. `write_page` orders sections by the schema, so a section added by `update` lands before `## Criterion`.
**＋** `estimate-cleanup-moves`: the prose Criterion from before case 72 says `vault/archived/<sprint>/<date>/<category>/`; the block `### case 102.2` says `vault/archive/…/<HHMM>/…`. The block is the contract; the prose is the stale path.
**＋** `rule-page-generation`, History line of 2026-09-11: "History and log lines end with `· [[decision-case-N]]` when a decision exists" — a wikilink outside a code span, so lint resolves it. Line 44 has the same text inside a code span and is not flagged.
**－** Case 110 already updates `rule-page-generation`; a second `update` of the same page in one session is two entries on one page, in ledger order — allowed.
**－** The 31 decision pages of Cases 1–28 (F8 a) and the lessons (F8 d) are not this Case.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-112.5
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
