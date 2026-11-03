---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether the ledger hook refuses the create of a sprint page that has_page finds live or archived, writes one that it does not find, and opens no sprint by a refused line
method: "uv run --project .guppi pytest .guppi/tests/test_ledger.py -k taken_sprint; by hand: the Render of rule-skill-sprint-open in .claude/skills/sprint-open/SKILL.md read against the Criterion"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, ledger, hooks]
core: true
---

## Criterion

When:
The ledger hook `guppi ledger` of `rule-ledger-write`, in `.guppi/guppi/ledger.py`, reads at a `Stop` a fresh `create` decision line of a page `entity-sprint-<id>`.

Then:
The ledger hook refuses the line when `has_page` of `.guppi/guppi/materialize.py` finds the page `entity-sprint-<id>` live or archived.
**＋** For such a line of the reply just finished, it exits 2 with one stderr line that names the id and asks for another id.
**＋** A `create` of a sprint page that `has_page` does not find is written.
**＋** `.claude/skills/sprint-open/SKILL.md` says that after such a refusal the main agent asks the person for another id, and the opening Case is built again under it.
**－** A refused `create` does not open the next sprint, so the other decision lines of the session stay refused while no sprint is open.
**－** The ledger hook does not check the GitHub name.

## Result

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
