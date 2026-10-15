---
type: estimate
kind: QA
status: failed
target: "[[rule-harness]]"
method: make test-harness over .guppi/tests/test_render.py and .guppi/tests/test_lint.py; the live reading of uv run --project .guppi guppi check by hand
checked: 2026-10-15
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi check` and `make test-harness` run, and someone reads the Purpose of `rule-harness`.

Then:
The Purpose says that three rules belong to no phase of the session: the renderer, the page `settings.json` is assembled from, and lint. With them, the checks of `rule-sprint` and `rule-backlog` run in `uv run --project .guppi guppi check`, in this order: the harness files against their pages, the sprint file against its page, the backlog file against its sources, the glossary file against its page, then the pages.
**＋** The Purpose names the rules that belong to it and run in no pipeline: the folder of the code of GUPPI and the command that runs it, the skill of the plugin that installs GUPPI into a project, the settings file `guppi.toml`, the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash, a file write or an interpreter it feeds, the hook that refuses a PowerShell here-string piped into an interpreter, the hook that repairs or names a file a shell call left with CRLF line endings, a byte-order mark or bytes that are not UTF-8, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, the hooks that read a page of the vault without its History, and the file under `.claude/rules/` that keeps the text of Decision pages out of a search.
**＋** `make test-harness` is green. The steps of `uv run --project .guppi guppi check` before `guppi lint` (`render --check`, `sprint --check`, `backlog --check` and `glossary --check`) exit 0 with no output on the committed tree. `guppi lint` is read by its own Estimates.

## Result

2026-10-15, Retro, not read: make test-harness 144 passed, render/sprint/glossary --check exit 0 with no output, but guppi backlog --check exits 1 (backlog.md differs from its sources) after /work deleted carry.md of raw/2026-10-15/0553/, until the librarian's guppi backlog; the new Purpose of rule-harness lands only at the librarian's run

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L74
- 2026-09-14 criterion: case 153 added · [[decision-case-153]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L3
- 2026-09-18 updated: the Criterion replaced whole — make lint with three steps (case 233.1) · [[decision-case-233.1]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L15
- 2026-09-22 updated: two lines of the Criterion — glossary --check the third step of make lint (case 306.5; pre-spec) · [[decision-case-306.5]]
- 2026-09-22 updated: the then line counts three file checks, glossary --check the third (case 311) · [[decision-case-311]]
- 2026-09-22 updated: the Purpose it reads names five rules outside the pipeline (case 323) · [[decision-case-323]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/0034/ledger.md#L60
- 2026-09-24 updated: the Criterion replaced whole — seven rules outside the pipeline, no Given (case 392.3) · [[decision-case-392.3]]
- 2026-09-25 updated: the Criterion replaced whole — eight rules outside the pipeline, the hooks of rule-page-read among them (case 420.2) · [[decision-case-420.2]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1654/ledger.md#L28
- 2026-09-27 updated: the Criterion replaced whole — backlog --check in the order of make lint (case 451.14) · [[decision-case-451.14]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L27
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-10-15 updated: the Criterion replaced whole — the rules in no pipeline include the folder of the code and the skill of the plugin, and the vault checks run by guppi check · [[decision-case-820.9]]
- 2026-10-15 status: pending → failed · raw/2026-10-15/1739/ledger.md#L14
