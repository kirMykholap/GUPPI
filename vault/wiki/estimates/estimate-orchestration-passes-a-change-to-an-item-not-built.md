---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the main agent keeps the change that an Other Case line asks of a Frontier item with no Case yet for the prompt that dispatches that item's case-guppi, sends it to that case-guppi by SendMessage when the item is in the same batch, and sends it back to the Case that wrote the line when the item ends with no Case
method: by hand, at the Retro of the session that changes it, the new Render of rule-orchestration in the Spec read against the Criterion, recorded in the estimate line
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the summary of `case-guppi` carries, under the item of a Case, a line `**Other Case:**` that names an item of `raw/<date>/<hi HHMM>/frontier.md` by its id, an item that no Case of the session has built, and the change that item's Case needs.

Then:
The main agent shows the Case as it stands, asks the person no question on the line, and sends no built Case back for it, in a batch too.
**＋** When the person takes up the named item later, the prompt that dispatches its `case-guppi` names the Case that wrote the line, as a related Case, and the change the line names.
**＋** When the person took up the named item in the same batch as the Case whose line names it, so that the `case-guppi` of the item is already out, the main agent sends the change to that `case-guppi` by `SendMessage`, and its Case stays in the batch.
**＋** When the line of the named item in `raw/<date>/<hi HHMM>/frontier.md` closes with no Case of its own — put off, kept, closed as work, or its built Case dropped — the main agent, in the turn that closes it, sends the change by `SendMessage` to the `case-guppi` of the Case that wrote the line, with no question to the person.
**＋** That Case is shown again when its `case-guppi` answers, in a batch while another Case of the session is out, and the person agrees or not at that showing.
**－** When the Case that wrote the line is dropped or taken back before the item is taken up, the main agent passes the change to nobody.
**－** A line `**Other Case:**` that names a Case of the session is handled as before.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
