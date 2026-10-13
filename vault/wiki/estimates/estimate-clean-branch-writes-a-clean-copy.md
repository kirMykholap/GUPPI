---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: "Whether guppi ship writes only the code, the harness and the pages with core: true, removes the references to cases, writes the shipped values, and exits 1 on what it cannot clean"
method: uv run pytest tests/test_ship.py
origin: raw/2026-10-13/1753/ledger.md#case-804.6
sprint: plugin
created: 2026-10-13
tags: [ci, plugin]
---

## Criterion

When:
`uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

Then:
It writes `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
**＋** In each file it writes, it removes a parenthesis that holds only references to cases, the references to cases inside a longer parenthesis, and each `[[decision-case-N]]` link.
**＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
**＋** It exits 1, and prints the file and the line, for each reference to a case, each link in a text to a page or a file it does not write, and each mention of a session of this repository by its id that remains.
**＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
**－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
**－** It writes no file that a page without `core: true` renders in full.
**－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.

## Result

2026-10-13, uv run pytest tests/test_ship.py: 10 passed — the written set (code, harness, schema files, tags.md, core pages, files a core page renders), no session record, no sprint.md, backlog.md, brief.md, log.md, guppi.toml or file a loose page renders in full, the references to cases and decision links removed, origin and sprint guppi with the run date and a one-line History, exit 1 with file and line on a leftover reference, a link to a page left out, a session mention and a section of a loose page, the form of a line kept, and lint finds no origin on a page it wrote

## History

- 2026-10-13 created · [[decision-case-804.6]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1753/ledger.md#L120
