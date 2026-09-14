---
type: estimate
kind: QA
status: passed
target: rule-ledger-tail
origin: raw/2026-09-13/ledger.md#case-101.2
sprint: migration
created: 2026-09-13
tags: [session, harness, ledger]
---

## Context

`/hi` sees nothing of what was written after the librarian's commit; a failed reading and a lesson wait one session more. `rule-ledger-tail` cannot be taken up as a `create`: the placeholder page exists and `generate` (`guppi/generate.py:289`) answers with a collision; none of the three placeholders has a way to be filled.

## Criterion

### case 101.2

When:
`uv run guppi tail` runs — from the render of `/hi`, or by hand.

Then:
For every `ledger.md` under `vault/raw/` — the date-level one of a date first, then its session ledgers in folder order, dates ascending — the script prints every line that `parse_line` reads as a record and whose number is neither in the `line` or `folded` of an entry nor under `unparsed` in the `materialize.yaml` beside that ledger, as `<date> L<n>: <the line>` or `<date>/<HHMM> L<n>: <the line>`.
**＋** A ledger without a yaml beside it prints every record line it has.
**＋** A ledger fully covered prints nothing; with an empty tail the output is empty.
**＋** Exit 0 always; a read error on one ledger is a stderr line and the walk goes on.
**＋** Render (`partial`, `.claude/skills/hi/SKILL.md`): between the markers `<!-- rule-ledger-tail -->` one line, `Tail: !`uv run guppi tail``.
**－** The coverage of a line is the function `guppi archive` uses: the two scripts cannot disagree on what "named in the yaml" means.

## Method

Unit, `tests/test_tail.py`: a fixture with a date-level ledger whose yaml covers
every record line, a session ledger with a yaml and two record lines outside it (an
estimate and a lesson after the last entry), a session ledger with no yaml, and a
ledger holding a line outside the grammar; one run prints exactly the two uncovered
lines of the second in the `<date>/<HHMM> L<n>: ` form and every record line of the
third, in order, nothing of the first, nothing for the ungrammatical line, exit 0; an
unreadable yaml is one stderr line and the other ledgers still print. Live,
2026-09-13, by hand: `uv run guppi tail` after the librarian's commit of this session
prints the readings and lessons written after it and nothing else; the next `/hi`
carries them under `Tail:`.

## Result

block 101.2: at /hi of 07:47 Tail: printed nothing — both units of 2026-09-13 covered by their yamls; by hand at 09:5x uv run guppi tail prints the 34 record lines of raw/2026-09-14/0747/ledger.md, the one ledger without a yaml, as 2026-09-14/0747 L<n>: <line>, exit 0; the render carries the Tail: line between the rule-ledger-tail markers

## History

- 2026-09-13 created · [[decision-case-101.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L45
