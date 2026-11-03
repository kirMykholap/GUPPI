---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-tail]]"
purpose: guppi tail prints every ledger record line that no materialize.yaml covers, and /hi shows it as Tail
method: "pytest .guppi/tests/test_tail.py; by hand, after a /hi: the Tail line against a run of uv run --project .guppi guppi tail by hand, written into the estimate line"
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi tail` runs, from the line `Tail:` of `.claude/skills/hi/SKILL.md` or by hand, over every `ledger.md` under `vault/raw/` and the `materialize.yaml` beside each.

Then:
The script walks the date-level ledger of a date first, then its session ledgers in folder order, dates ascending. It prints every line that `parse_line` reads as a record and whose number is neither in the `line` or `folded` of an entry nor under `unparsed` of the yaml beside it. Each printed line opens with the date, and for a session ledger with the date, a slash and the session folder, then `L<n>:` and the line as the ledger holds it.
**＋** A ledger without a yaml beside it prints every record line it has.
**＋** A ledger fully covered prints nothing; with an empty tail the output is empty.
**＋** Exit 0 always; a ledger that cannot be read is a line on stderr, and the walk goes on.
**＋** The Render of `rule-ledger-tail`, `partial`, puts one line into `.claude/skills/hi/SKILL.md` between its markers: `` Tail: !`uv run --project .guppi guppi tail` ``.
**－** `.guppi/guppi/tail.py` holds no judgment of coverage of its own: the coverage of a line is `uncovered_lines` of `.guppi/guppi/archive.py`, the one `guppi archive` uses.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
