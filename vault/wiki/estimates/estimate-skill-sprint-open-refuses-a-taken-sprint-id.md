---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether the ledger hook refuses the create of a sprint page that has_page finds live or archived, writes one that it does not find, and opens no sprint by a refused line
method: "uv run --project .guppi pytest .guppi/tests/test_ledger.py -k taken_sprint; by hand at the Retro of this session: the new Render of rule-skill-sprint-open in raw/<date>/<hi HHMM>/spec.md read against the Criterion"
origin: raw/2026-10-12/2349/ledger.md#case-788.1
sprint: plugin
created: 2026-10-12
tags: [sprint, ledger, hooks]
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

2026-10-13, uv run pytest tests/test_ledger.py -k taken_sprint: 4 passed; Retro by hand: the Render of rule-skill-sprint-open in spec.md asks for another id and builds the opening Case again after a refusal (case 788.1)

## History

- 2026-10-13 created · [[decision-case-788.1]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L47
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
