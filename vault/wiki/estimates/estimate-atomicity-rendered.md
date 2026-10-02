---
type: estimate
kind: QA
status: passed
target: "[[rule-atomicity]]"
purpose: The text of rule-atomicity stands between its markers in ratification.md, identical to the page, and a hand edit of the file is refused
method: uv run guppi render --check exit 0; the text between the markers of ratification.md read by hand after the librarian's render
checked: 2026-10-02
origin: raw/2026-09-22/1121/ledger.md#case-317
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi render` writes the governed files, and `/hi` loads `vault/wiki/ratification.md` at the start of a working session.

Then:
`vault/wiki/ratification.md` holds the text of `rule-atomicity` between its markers: the statement, the pair test — list the conditions of "done", and for each pair ask whether one could fail while the other passes and needs a different fix — and the scope: Case, Entity, Rule, Estimate; not a Lesson, a recorded fact does not split; not an Insight, which is born by clustering, the same rule in reverse; depth is not fixed in advance.
**＋** `uv run guppi render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
**＋** `rule-ratification` is a MOC with the child `rule-atomicity` and a marker line for it in its Render.
**－** The rule has no refusal of its own in substance: the refusal of two promises in one Case stays with `rule-prespec`.

## Result

2026-10-02, the /hi of session 2049: `uv run guppi render --check` exit 0; ratification.md loaded at /hi holds the rule-atomicity text between its markers: the statement, the pair test, the scope Case, Entity, Rule, Estimate, not a Lesson, not an Insight, depth not fixed; rule-ratification kind: MOC, children [rule-atomicity], its marker line in the Render; the refusal of a hand edit not tried

## History

- 2026-09-22 created · [[decision-case-317]]
- 2026-09-23 updated: the method names render --check, not make lint (case 374) · [[decision-case-374]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L39
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the old form of the pre-spec refusal out (case 492.1) · [[decision-case-492.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L38
- 2026-10-02 updated: the Criterion replaced whole - the text renders into ratification.md under rule-ratification (case 595.5) · [[decision-case-595.5]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L4
