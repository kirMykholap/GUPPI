---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: "Whether guppi ship writes nothing and exits 1 while a page with core: true is draft, and writes the copy with --allow-draft, judging such a page by is_draft_core"
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k draft_core
checked: 2026-10-15
origin: raw/2026-10-15/0553/ledger.md#case-822.8
sprint: plugin
created: 2026-10-15
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` or `uv run --project .guppi guppi ship --review <folder>`, as `rule-clean-branch` sets it, builds the clean version into an empty folder, with or without the option `--allow-draft`.

Then:
While a rule or an entity with `core: true` stands `draft`, `guppi ship` prints one line for each such page, writes nothing and exits 1.
**＋** With `--allow-draft`, it writes the clean version into the folder all the same and prints those lines, which set no exit code.
**＋** `.github/workflows/prod.yml` never passes `--allow-draft`, so it writes nothing to `prod` while such a page stands.
**＋** The build tells a draft page with `core: true` by `is_draft_core` of `.guppi/guppi/pages.py`, imported.
**＋** `rule-skill-merge-main` and `rule-skill-pr-review` carry no `core`, so the clean version holds neither them nor the files they render.
**－** `uv run --project .guppi guppi ship --check` does not judge the status of a page.

## Result

2026-10-15, uv run --project .guppi pytest .guppi/tests/test_ship.py -k draft_core: 4 passed, exit 0

## History

- 2026-10-15 created · [[decision-case-822.8]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L5
