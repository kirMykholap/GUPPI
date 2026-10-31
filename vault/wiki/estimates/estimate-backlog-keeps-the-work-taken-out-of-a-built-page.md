---
type: estimate
kind: QA
status: pending
target: "[[rule-backlog]]"
purpose: Whether backlog.md shows the open work of Work Mode and the second part of the Spec box, kept as notes of the live sprint page, whatever the status of rule-work-mode and rule-spec-box; a one-time check of this data
method: "by hand, after the librarian's run of a session in which the Backlog of entity-sprint-plugin holds the notes taken out of rule-work-mode and rule-spec-box: vault/wiki/backlog.md, the file of the repository where the evidence is saved, read against the Criterion in the session whose brief puts the reading under Work, the file named and its lines quoted in the estimate line"
origin: raw/2026-10-31/0431/ledger.md#case-962
sprint: plugin
created: 2026-10-31
tags: [sprint, workflow]
---

## Criterion

When:
The librarian runs `uv run --project .guppi guppi backlog` over `vault/wiki/` and `vault/archive/`, after the `## Backlog` of `entity-sprint-plugin` holds the notes taken out of `rule-work-mode` and `rule-spec-box`.

Then:
`vault/wiki/backlog.md` holds under `## Deferred` a line with the text of the note on the rest of Work Mode: the test of each Estimate written first and turned green, and the full model the person plans.
**＋** It holds a line with the text of the note on the second part of the Spec box.
**＋** Each of these lines stands whatever the status of `rule-work-mode` and of `rule-spec-box`, `built` included.
**－** The line of `vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md` that names `rule-work-mode` does not keep the work in the list: it may leave once that page stands `built`.

## History

- 2026-10-31 created · [[decision-case-962]]
