---
type: rule
kind: Leaf
purpose: Shows at /hi every ledger line that no vault page holds yet, so a reading or a lesson written after the librarian's commit reaches the next session's Frontier
status: built
enforcement: render
implementation_ref: [guppi/tail.py, tests/test_tail.py]
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: "[[rule-skill-hi]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, harness, ledger]
core: true
---

## Purpose

Shows at `/hi` and at `/retro` every ledger line that no vault page holds yet. The readings of the
librarian's own run and the lessons of the close are written after its commit and
after its brief, so the next `/hi`, which reads the brief, would not see them until
the librarian after next. The tail closes that gap for the Frontier: the page of a
reading comes with the next librarian, the fact that it failed comes at once.

## Render

<!-- rule-ledger-tail -->
Tail: !`uv run guppi tail`
<!-- /rule-ledger-tail -->

## How it works

`uv run guppi tail` walks every `ledger.md` under `vault/raw/`: the date-level
ledger of a date first, then the session ledgers
`raw/<date>/<HHMM>/ledger.md` in folder order, dates ascending. For each it reads
the `materialize.yaml` beside it and prints every line that
`materialize.parse_line` reads as a record and whose number is neither in the
`line` or `folded` of an entry nor under `unparsed`, as
`<date> L<n>: <the line as in the ledger>` or `<date>/<HHMM> L<n>: <the line>`.
A ledger without a yaml beside it prints every record line it has; a ledger fully
covered prints nothing, and with an empty tail the output is empty. Exit 0 always;
a ledger that cannot be read is a line on stderr and the walk goes on. `hi` is
never in the tail: it goes to the event log. A line outside the ledger grammar is
not printed — it is either `unparsed` in the yaml or not a record. The coverage of
a line is the one function `guppi archive` uses to call a unit done
([[rule-raw-archive]]), so the two scripts cannot disagree; after the archive the
walk holds only the sessions not yet done. The Render splices one line into the
`/hi` skill, between the markers of this page, after `rule-git-context`; the
Frontier text of [[rule-skill-hi]] makes a `failed` reading or a lesson of the tail
an item, and a decision line not.

## History

- 2026-10-14 shipped with GUPPI
