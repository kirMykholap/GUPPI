---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: "Whether guppi ship writes the code under .guppi/ without its cache folders, the harness and the pages with core: true, removes whole each bracket that holds a pointer, writes a link to a page it leaves out as its slug, writes the shipped values, exits 1 on a pointer outside such a bracket and on a bare case number in a comment or a docstring of a Python file, lists the brackets with words under --review, and judges in place under --check each file outside vault/ that it writes"
method: uv run --project .guppi pytest .guppi/tests/test_ship.py
checked: 2026-10-15
origin: raw/2026-10-13/1753/ledger.md#case-804.6
sprint: plugin
created: 2026-10-13
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
**＋** Or `uv run --project .guppi guppi ship --review <folder>` does the same.
**＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.

Then:
It writes `.guppi/` — what it writes of its tests, its Python environment and the module of the command `ship` is what `estimate-clean-branch-ships-the-tests` and `estimate-clean-branch-ships-no-ship-command` set — then `.claude/`, `CLAUDE.md`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
**＋** In each file it writes, it removes whole each bracket that holds a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — with every word in it and the space before it, and each `[[decision-case-N]]` link, but in a string of a test file, as `estimate-clean-branch-ships-the-tests` sets it; a bracket that holds no pointer stays as it is.
**＋** It writes each other `[[…]]` link of a Markdown file to a page or a file it does not write as the slug in a code span.
**＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
**＋** It exits 1, and prints the file and the line, for each pointer that stands outside such a bracket, each id of a list of sessions included.
**＋** In a comment or a docstring of a Python file it writes, it exits 1, and prints the file and the line, for each bracket that holds only case numbers, joined by a comma, a semicolon, `and` or a dash, such as `(274.1)` or `(513, 544.7)`.
**＋** It does the same for each comment or docstring that opens with one or more case numbers joined the same way, followed by a colon, such as `# 169.1:`, `"""75.2:` or `# 387.4, 445.4:`, and for each comment whose whole text is one or more case numbers joined the same way, such as `# 786` or `# 387.4, 445.4`.
**＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
**＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
**＋** With `--check` it judges each file it would write outside `vault/` — the code under `.guppi/`, `.claude/` and the files at the root of the project — but `.guppi/uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
**－** It writes no page without `core: true` but the Estimates that `estimate-clean-branch-ships-the-passed-estimates` sets, nothing of `vault/raw/` or `vault/archive/`, and no `guppi.toml`; what it writes of `.github/` and in place of the session files is what `estimate-clean-branch-ships-the-checks-workflow` and `estimate-clean-branch-writes-the-session-files` set.
**－** It writes no cache folder of Python, pytest or ruff, and `--check` does not judge one.
**－** It writes no file that a page without `core: true` renders in full.
**－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
**－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed; in `vault/wiki/case-example.md` and the Render of `rule-case-example` only the fenced blocks, the example Case among them, are set aside so, and the text around them is judged and cleaned like the text of any other page.
**－** It removes no bare case number: the copy holds it as written.
**－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number or a list of numbers that opens a comment with words and no colon after it, such as `# 3, 4 tries`, is no finding.

## Result

2026-10-15, uv run --project .guppi pytest .guppi/tests/test_ship.py: 50 passed, exit 0

## History

- 2026-10-13 created · [[decision-case-804.6]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1753/ledger.md#L120
- 2026-10-14 updated: the Criterion replaced whole — each bracket that holds a pointer removed whole, a link to a page left out as its slug, samples and examples kept, --review and --check (case 807.1) · [[decision-case-807.1]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L20
- 2026-10-14 updated: the Criterion replaced whole — guppi ship reports a bare case number in a comment or a docstring of a Python file · [[decision-case-808.1]]
- 2026-10-14 status: pending → passed · raw/2026-10-14/0101/ledger.md#L56
- 2026-10-14 updated: the Criterion replaced whole — guppi ship reports a list of bare case numbers at the opening of a comment or a docstring, or alone in a comment · [[decision-case-811]]
- 2026-10-14 status: pending → passed · raw/2026-10-14/0232/ledger.md#L11
- 2026-10-14 updated: the Criterion replaced whole — case-example.md and the Render of rule-case-example are cleaned outside their fenced blocks · [[decision-case-815]]
- 2026-10-14 status: pending → passed · raw/2026-10-14/1536/ledger.md#L9
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — the code ships under .guppi/, and the root pyproject.toml and uv.lock do not ship · [[decision-case-819.3]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L1
