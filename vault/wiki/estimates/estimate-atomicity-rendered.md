---
type: estimate
kind: QA
status: pending
target: "[[rule-atomicity]]"
purpose: The text of rule-atomicity stands between its markers in case-schema.md, identical to the page, and a hand edit of the file is refused
method: make lint — render --check exit 0; the text between the markers of case-schema.md read by hand after the librarian's render
origin: raw/2026-09-22/1121/ledger.md#case-317
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Criterion

Given:
`rule-render-harness`: a page with `render_mode: partial` writes the body of its `## Render` between the markers `<!-- rule-slug -->` … `<!-- /rule-slug -->` of the file in `governs`; `render --check` catches a drift.
**＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
**＋** `rule-case-protocol` renders `case-schema.md` whole; `/hi` loads it in every working session.
**＋** `pre-spec` refuses a Case with two Estimate items and no written `sections: Criterion` — the one mechanical refusal of this rule, signed for `rule-prespec`.

When:
`guppi render` writes the files, and the agent reads `case-schema.md` at the start of a session.

Then:
`case-schema.md` holds the text of `rule-atomicity` between its markers: the statement, the pair test — list the conditions of "done", and for each pair ask whether one could fail while the other passes and needs a different fix — and the scope: Case, Entity, Rule, Estimate; not a Lesson, a recorded fact does not split; not an Insight, which is born by clustering, the same rule in reverse; depth is not fixed in advance.
**＋** `render --check` after the render exits 0; a hand edit of the file is refused by the hook.
**＋** `rule-case-protocol` is a MOC with the child `rule-atomicity` and a marker line in its Render.
**－** The rule has no refusal of its own in substance: the refusal of two promises in one Case stays with `rule-prespec`.

## History

- 2026-09-22 created · [[decision-case-317]]
