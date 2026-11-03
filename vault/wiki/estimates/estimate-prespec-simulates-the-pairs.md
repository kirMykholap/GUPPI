---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether pre-spec catches an anchor that misses or is not unique once the pairs of the Spec are applied in entry order
method: pytest .guppi/tests/test_prespec.py on a temp plan over temp pages — an anchor that misses, one that hits twice, and a pair whose old is produced by an earlier Case
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` reads a plan whose Cases carry `replace` or `reword` pairs, and the live pages of the vault, before the Spec is approved.

Then:
The `replace` and `reword` pairs of every Case of the plan are applied in entry order to copies of the pages in memory, whitespace collapsed as `generate` collapses it; nothing is written to disk.
**＋** An anchor that misses, or hits more than once, gives one line with its Case, the page's slug and the opening of its `old`.
**＋** The anchor is judged against the page as the Spec leaves it, not as it stands today.
**－** The meaning of the words in their place is not judged by a machine.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
