---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether pre-spec catches an anchor that misses or is not unique once the pairs of the Spec are applied in entry order
method: pytest tests/test_prespec.py on a temp plan over temp pages — an anchor that misses, one that hits twice, and a pair whose old is produced by an earlier Case
origin: raw/2026-09-22/2046/ledger.md#case-351
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Criterion

Given:
`prespec --check` reads the plan and the live pages of the vault; it has no check of an anchor at all.
**＋** `generate` applies the pairs in entry order and matches with whitespace collapsed, exactly one occurrence.
**＋** The pairs of one Spec can touch one span: 314.2 against 310.6.
**＋** `tests/test_prespec.py` fixes `--check` on a temp plan over temp pages.

When:
`uv run guppi prespec --check <plan> --session <id>` reads the plan before the Spec is approved.

Then:
The `replace` and `reword` pairs of every Case of the plan are applied in entry order to copies of the pages in memory, whitespace collapsed as `generate` collapses it; nothing is written to disk.
**＋** An anchor that misses, or hits more than once, gives one line with its Case, the page's slug and the opening of its `old`.
**＋** The anchor is judged against the page as the Spec leaves it, not as it stands today.
**－** The meaning of the words in their place is not judged by a machine.

## Result

2026-09-22, uv run pytest tests/test_prespec.py -k "anchor or earlier_case or reword or writes_nothing": 7 passed — the first reading of this page covered `replace` alone while the Criterion names both kinds of pair, so three cases were added: a `reword` pair no live page holds gives `case 1: rule-x: a reword pair hits no live page: FIRST`, one a live page holds is clean, and the page on disk still holds `FIRST` and not `SECOND` after a clean run, so nothing is written; the four `replace` cases stand as read before

## History

- 2026-09-23 created · [[decision-case-351]]
- 2026-09-23 status: pending → passed · raw/2026-09-22/2046/ledger.md#L36
