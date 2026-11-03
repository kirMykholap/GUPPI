---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether pre-spec, and the Case check through judge, report a replace pair whose new opens with spaces or tabs while its old opens with neither
method: "pytest .guppi/tests/test_prespec.py on a temp plan over temp pages: a pair whose new opens with spaces and old with none, one where both open with spaces, one where neither does"
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` reads a plan whose Cases carry `replace` pairs, or the hook of `rule-case-check` runs `judge` of `.guppi/guppi/prespec.py` over an answer of `case-guppi`.

Then:
A `replace` pair whose `new` opens with a space or a tab while its `old` opens with neither gives one finding with its Case, the page's slug and the opening of its `old`.
**＋** The predicate lives in `.guppi/guppi/generate.py`, beside the matching rule of a pair, and `check_pairs` of `.guppi/guppi/prespec.py` imports it.
**＋** The hook of `rule-case-check` sends such a Case back to `case-guppi` before the person sees it.
**－** A pair whose `old` and `new` both open with spaces or tabs, or whose `new` opens with neither, gives no such finding.
**－** `guppi generate` applies such a pair as before: the finding stands at pre-spec and at the check of the Case only.

## Result

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
