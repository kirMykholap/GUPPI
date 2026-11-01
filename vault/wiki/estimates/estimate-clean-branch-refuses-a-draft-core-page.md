---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: "Whether guppi ship writes nothing and exits 1 while a draft page with core: true stands that was never built or has a failed Estimate, writes as it stands one built before that only waits for a reading, writes the copy with --allow-draft, and lint judges by the same is_draft_core"
method: uv run --project .guppi pytest .guppi/tests/test_ship.py .guppi/tests/test_lint.py -k draft_core
checked: 2026-11-02
origin: raw/2026-10-15/0553/ledger.md#case-822.8
sprint: plugin
created: 2026-10-15
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` or `uv run --project .guppi guppi ship --review <folder>`, as `rule-clean-branch` sets it, builds the clean version into an empty folder, with or without the option `--allow-draft`, or `uv run --project .guppi guppi lint` runs where the module of the command `ship` stands.

Then:
A rule or an entity with `core: true` that stands `draft` blocks the build when its `## History` holds no line that set its status to `built`, or when one of its Estimates stands `failed`.
**＋** While a page that blocks the build stands, `guppi ship` prints one line for each such page, writes nothing and exits 1.
**＋** A `draft` page with `core: true` whose History holds such a line and none of whose Estimates stands `failed` gets no line, and the build writes it as it stands.
**＋** With `--allow-draft`, the build writes the clean version all the same and prints those lines, which set no exit code; `.github/workflows/prod.yml` never passes that option.
**＋** The build and lint tell a page that blocks the build by `is_draft_core` of `.guppi/guppi/pages.py`, imported by both, and a test runs the cascade of `.guppi/guppi/generate.py` that sets a page `built` and asserts that the page, set `draft` again, then blocks nothing.
**＋** `rule-skill-merge-main` and `rule-skill-pr-review` carry no `core`, so the clean version holds neither them nor the files they render.
**－** `uv run --project .guppi guppi ship --check` does not judge the status of a page.

## Result

2026-11-02, Retro of session 2227, uv run --project .guppi pytest .guppi/tests/test_ship.py .guppi/tests/test_lint.py -k draft_core: 16 passed, 164 deselected — a draft core page never built exits 1 with its line, one built before with a pending Estimate is written with exit 0, one with a failed Estimate exits 1, --allow-draft writes, --check prints nothing, the cascade test sets a page built and finds it no draft core when set draft again with a pending Estimate, ship and lint import the one is_draft_core; rule-skill-merge-main and rule-skill-pr-review carry no core and .github/workflows/prod.yml holds no --allow-draft (grep)

## History

- 2026-10-15 created · [[decision-case-822.8]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L5
- 2026-11-02 updated: the Criterion replaced whole — only a draft page with core: true that was never built or has a failed Estimate blocks the build · [[decision-case-996.1]]
- 2026-11-02 status: pending → passed · raw/2026-11-01/2227/ledger.md#L23
