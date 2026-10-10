---
type: decision
case: "279.2"
status: archived
create: ["[[estimate-prespec-catches-a-command-line-off-form]]"]
update: ["[[rule-prespec]]"]
origin: raw/2026-09-20/1749/ledger.md#case-279.2
sprint: migration
created: 2026-09-20
tags: [harness, workflow, session]
---

## Context

The scripts tick three kinds of lines in the Spec: `generate` the page lines and the `read` lines, `render` and `sprint` the lines of their own commands. The schema names the form of the first two (`<kind> `<slug>``, `read `<slug>``) and not the form of the command lines; that form stands in `rule-render-harness` (case 235), a page the agent does not read when it writes the Spec. In session 1308 the agent wrote `render `<file>`` on the pattern of the page lines, and nine lines stood unticked after the librarian's run, the yaml applied whole. A sentence in the schema is instruction; what keeps it from repeating is a guard — `guppi prespec --check` already reads the `tasks` block of every Case (cases 59.3, 264.2).
Case 278 of this session already replaced the Criterion of `estimate-case-protocol-loaded` whole; an `update` of the Render of `rule-case-protocol` touches the same Estimate (187), so 279.1 supersedes 278 and carries its text plus one line. `rule-case-protocol` `draft`; `estimate-case-protocol-loaded` touched, `case-form`, `acknowledging-reply` and `ledger-line-form` not. `rule-prespec` `built`, its three Estimates untouched; the new promise is its own Estimate with a `ref`, no vault query due. `rule-render-harness` and its Estimates do not change — the ticker is right.

## Problem

The form of a line the scripts tick is written where the agent does not look, and nothing refuses a line of another form. Either the schema names the form and pre-spec refuses the rest, or the ticker accepts both — two forms of one line.

## History

- 2026-09-20 created · raw/2026-09-20/1749/ledger.md#case-279.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
