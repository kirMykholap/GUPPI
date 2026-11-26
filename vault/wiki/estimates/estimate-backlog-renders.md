---
type: estimate
kind: QA
status: passed
target: "[[rule-backlog]]"
purpose: guppi backlog writes backlog.md from the conserved Specs, the pages with deferred_by, the open Insights and the Backlog of each sprint page, live or archived, a line of a closed sprint left out once the live sprint takes it or its pages stand finished now or stood so, by their History, on or after the day that sprint closed, each item with its purpose and its count
method: uv run --project .guppi pytest .guppi/tests/test_backlog.py
checked: 2026-11-26
origin: raw/2026-09-27/1255/ledger.md#case-451.4
sprint: migration
created: 2026-09-27
tags: [harness, sprint]
---

## Criterion

When:
`uv run --project .guppi guppi backlog` runs over `vault/wiki/`, `vault/raw/` and `vault/archive/`. The librarian runs it after `guppi sprint`, and the skill `carry` runs it after it writes `carry.md`.
**＋** Or `.guppi/tests/test_backlog.py` runs `.guppi/guppi/backlog.py` over a made-up vault.

Then:
The script writes `vault/wiki/backlog.md`: the heading `# Backlog`, the line `N items`, then `## Conserved Specs` and `## Deferred`.
**＋** `## Conserved Specs` holds each session folder under `vault/raw/` that holds `carry.md`. Each has one line that names its `spec.md` and its Cases. Under that line stands one line per item of its `then` blocks, with the kind and the slug, read by the Spec reader of `.guppi/guppi/materialize.py`.
**＋** `## Deferred` holds one line per item. The items are each live page with a `deferred_by` that is not empty, each Insight whose `status` is `open`, and each line of the `## Backlog` of each `entity-sprint-<id>`, live under `vault/wiki/entities/` or archived under `vault/archive/`. A line holds the slug, the page's `purpose` (for an Insight, its `pattern` and `severity`) and the count. A Backlog line that names no page stands by its text.
**＋** The count of an item is the number of sessions whose `frontier.md`, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names its slug in a code span of its title. It is read by `generate.frontier_marks`, and `.guppi/guppi/backlog.py` holds no copy of that reader.
**＋** `N` counts the conserved Specs and the lines of `## Deferred`. A slug that stands under a conserved Spec does not stand again under `## Deferred`, and a slug of two sources stands once.
**＋** A folder whose `carry.md` is gone shows nothing. Its defers enter `## Deferred` through `deferred_by` once `materialize` and `generate` have applied them.
**＋** One reader of `.guppi/guppi/pages.py` reads each line of `## History` that sets a status, with the status it sets and the date the line opens with. `is_draft_core` of the same module and `.guppi/guppi/backlog.py` judge by it, and it reads the lines that the cascade of `.guppi/guppi/generate.py` and the close of `.guppi/guppi/sprint_close.py` write.
**－** A slug of a line of the `## Backlog` of an archived sprint page does not stand when the live sprint page names it in its `## Milestones` or its `## Backlog`, or when its page stands `built`, `passed` or `archived`, the statuses that tick an item in `.guppi/guppi/sprint.py`.
**－** Such a slug does not stand either when its page stood `built`, `passed` or `archived` on or after the day of the close of its sprint. The day of the close is the date of the last line of the `## History` of the archived sprint page that set it `archived`. The page stood so when the last dated status line of its `## History` before that day set one of those statuses, or when a dated status line on that day or after it set one. A new Estimate that sets the page `draft` after that day does not bring the line back.
**－** An archived sprint page whose `## History` holds no line that set it `archived` gives no day of the close, and a slug of its `## Backlog` is judged by the status of its page alone. A status line with no date is not counted for the day of the close.
**－** A line of the `## Backlog` of an archived sprint page that names no page does not stand when the live sprint page holds a line of the same text.
**－** The script writes no page of `vault/wiki/` and no file but `vault/wiki/backlog.md`. The governed-files hook refuses a hand edit of that file.

## Result

2026-11-26, Retro of session 1336, uv run --project .guppi python -m pytest .guppi/tests/test_backlog.py: 27 passed, the new tests among them — a line of a closed sprint leaves for good once its page stood finished since the close (a page set built after the close, and one set built before it and still built on its day, leave; one set built and draft again before the close, and one never set built, stand), the day of the close the last History line that set the sprint page archived, an archived sprint page with no such line judged by the status alone, a status line with no date not counted, the reader status_lines of pages.py reading what the cascade of generate and mark of sprint_close write, and HISTORY_DATE held once in pages.py; uv run --project .guppi guppi test: 2000 passed, 6 skipped, 2 deselected

## History

- 2026-09-27 created · [[decision-case-451.4]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L24
- 2026-09-30 updated: the Criterion replaced whole — the reader of the count named without the sprint move, removed by case 539.1 (case 539.4) · [[decision-case-539.4]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1306/ledger.md#L1
- 2026-10-04 updated: the Criterion replaced whole — the Backlog of each sprint page, live or archived (case 628.12) · [[decision-case-628.12]]
- 2026-10-09 updated: the Criterion replaced whole — a line of a closed sprint leaves once taken or finished; the method a test of the session (case 743.4) · [[decision-case-743.4]]
- 2026-10-09 status: pending → passed · raw/2026-10-08/2352/ledger.md#L32
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-31 status: passed → passed · raw/2026-10-31/0128/ledger.md#L15
- 2026-11-26 updated: the Criterion replaced whole — a line of a closed sprint leaves for good once its pages stood finished on or after the day of the close · [[decision-case-1067]]
- 2026-11-26 status: pending → passed · raw/2026-11-26/1336/ledger.md#L12
