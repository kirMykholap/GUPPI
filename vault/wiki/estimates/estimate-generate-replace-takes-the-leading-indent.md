---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: Whether a replace pair whose old opens with spaces or tabs leaves the indent of its new on the page, and no indent added twice
method: "pytest in tests/test_generate.py against a temp vault: an old that opens with spaces over an indented line, one that opens with none, and one whose hit count is the same with and without its leading spaces"
origin: raw/2026-09-30/1306/ledger.md#case-543.3
sprint: migration
created: 2026-09-30
tags: [harness, workflow]
---

## Criterion

When:
`guppi generate` applies a `replace` pair of an `update` entry to a page, or `check_pairs` of `guppi/prespec.py` applies it to a copy of the page, both by `replace_once` of `guppi/generate.py`.

Then:
An `old` that opens with a space or a tab matches, besides its words, every space and tab on the page just before its first word, and `new` takes their place.
**＋** An `old` that opens with neither matches from its first word, and the spaces and tabs before it on the page stay.
**＋** Between the words of `old` whitespace stays collapsed: a line break matches any whitespace.
**－** The spaces and tabs before the first word never make an anchor miss or hit twice: a pair that hits the page once without them still hits it once.

## History

- 2026-09-30 created · [[decision-case-543.3]]
