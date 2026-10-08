---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: Whether guppi sprint, with no live sprint page, writes sprint.md with the closed sprint marked and exits 0
method: uv run pytest tests/test_sprint.py -k closed
origin: raw/2026-10-08/2352/ledger.md#case-743.5
sprint: migration
created: 2026-10-08
tags: [harness, sprint]
---

## Criterion

When:
`uv run guppi sprint` of `guppi/sprint.py` runs while no live sprint page stands, in the librarian's run after a close or in `tests/test_sprint.py` over a made-up vault.

Then:
`guppi sprint` writes `vault/wiki/sprint.md` as `# Sprint`, the heading `## <id> — closed` and the line `No sprint is open since the close of <id>.`, and exits 0.
**＋** `<id>` is the id that the first `## ` heading of the file named before, read by `sprint_id` of `guppi/materialize.py`, and a file already marked closed keeps its id.
**＋** `sprint_id` reads `<id>` from the closed heading, as from any heading.
**＋** One function of `guppi/sprint.py` writes the mark and judges a heading closed, and the hook of `rule-skill-sprint-open` imports it.
**＋** The run that writes the closed form is a run that wrote the file and exits 0, so it ticks the task lines of the Specs as `estimate-sprint-ticks-the-spec` sets it.
**－** With no live sprint page and no `vault/wiki/sprint.md`, the script prints one line on stderr and exits 1, and writes nothing.

## Result

2026-10-09, uv run pytest tests/test_sprint.py -k closed; 8 passed: the closed form with the earlier id and exit 0, a closed file keeps its id, sprint_id reads it, no page and no file exit 1 with no tick, the closed run ticks the guppi sprint line

## History

- 2026-10-09 created · [[decision-case-743.5]]
- 2026-10-09 status: pending → passed · raw/2026-10-08/2352/ledger.md#L33
