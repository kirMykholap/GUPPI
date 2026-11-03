---
type: estimate
kind: QA
status: passed
target: "[[rule-atomicity]]"
purpose: The text of rule-atomicity stands between its markers in ratification.md, identical to the page, and a hand edit of the file is refused
method: uv run --project .guppi guppi render --check exit 0; the text between the markers of ratification.md read by hand after the librarian's render
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi render` writes the governed files, and `/hi` loads `vault/wiki/ratification.md` at the start of a working session.

Then:
`vault/wiki/ratification.md` holds the text of `rule-atomicity` between its markers: the statement, the pair test — list the conditions of "done", and for each pair ask whether one could fail while the other passes and needs a different fix — and the scope: Case, Entity, Rule, Estimate; not a Lesson, a recorded fact does not split; not an Insight, which is born by clustering, the same rule in reverse; depth is not fixed in advance.
**＋** `uv run --project .guppi guppi render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
**＋** `rule-ratification` is a MOC with the child `rule-atomicity` and a marker line for it in its Render.
**－** The rule has no refusal of its own in substance: the refusal of two promises in one Case stays with `rule-prespec`.

## Result

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
