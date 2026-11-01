---
type: estimate
kind: QA
status: passed
target: "[[rule-backlog]]"
purpose: guppi backlog --check names backlog.md when it differs from the render with every Frontier and from the render without the Frontier of the newest session, exit 1, and writes nothing
method: uv run --project .guppi pytest .guppi/tests/test_backlog.py
checked: 2026-11-01
origin: raw/2026-09-27/1255/ledger.md#case-451.5
sprint: migration
created: 2026-09-27
tags: [harness, sprint]
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi backlog --check`, by hand or through `uv run --project .guppi guppi check`, over `vault/wiki/backlog.md` and the `frontier.md` files that `frontiers` of `.guppi/guppi/generate.py` finds.

Then:
The check renders the file in memory once with every Frontier file and once without the Frontier file of the newest session, the first in the order of `frontiers` of `.guppi/guppi/generate.py`.
**＋** When `vault/wiki/backlog.md` equals either render, the check is silent and exits 0.
**＋** When it equals neither, the check prints one line on stdout that names the file and exits 1.
**＋** `uv run --project .guppi guppi backlog` without `--check` writes the render with every Frontier file.
**＋** `uv run --project .guppi guppi check` runs it after `sprint --check` and before `glossary --check`.
**－** The check writes no file in either case.
**－** `uv run --project .guppi guppi check` writes nothing to the tree.
**－** The check reads each Frontier file once, by `frontier_marks` of `.guppi/guppi/generate.py`.

## Result

2026-11-01, Retro of session 1721: uv run --project .guppi pytest .guppi/tests/test_backlog.py 21 passed, among them --check silent on a file written before the newest session put an item off, red when the put-off of an older session is missing, each Frontier read once by frontier_marks; the live uv run --project .guppi guppi backlog --check exit 0 in Work Mode with C1 and C8 put off in this session's Frontier

## History

- 2026-09-27 created · [[decision-case-451.5]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L23
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-11-01 updated: the Criterion replaced whole — the check accepts the file without the put-offs of the newest session · [[decision-case-983]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/1721/ledger.md#L32
