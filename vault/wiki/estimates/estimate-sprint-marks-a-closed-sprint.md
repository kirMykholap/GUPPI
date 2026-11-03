---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: Whether guppi sprint, with no live sprint page, writes sprint.md with the closed sprint marked and exits 0
method: uv run --project .guppi pytest .guppi/tests/test_sprint.py -k closed
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, sprint]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi sprint` of `.guppi/guppi/sprint.py` runs while no live sprint page stands, in the librarian's run after a close or in `.guppi/tests/test_sprint.py` over a made-up vault.

Then:
`guppi sprint` writes `vault/wiki/sprint.md` as `# Sprint`, the heading `## <id> — closed` and the line `No sprint is open since the close of <id>.`, and exits 0.
**＋** `<id>` is the id that the first `## ` heading of the file named before, read by `sprint_id` of `.guppi/guppi/materialize.py`, and a file already marked closed keeps its id.
**＋** `sprint_id` reads `<id>` from the closed heading, as from any heading.
**＋** One function of `.guppi/guppi/sprint.py` writes the mark and judges a heading closed, and the hook of `rule-skill-sprint-open` imports it.
**＋** The run that writes the closed form is a run that wrote the file and exits 0, so it ticks the task lines of the Specs as `estimate-sprint-ticks-the-spec` sets it.
**－** With no live sprint page and no `vault/wiki/sprint.md`, the script prints one line on stderr and exits 1, and writes nothing.

## Result

2026-10-09, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
