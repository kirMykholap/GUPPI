---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: A defer the person asks for is shown and written in the same reply, with no round of ratification
method: by hand, the first defer the person asks for after the render
origin: raw/2026-09-24/1916/ledger.md#case-405
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Criterion

When:
The person asks in the chat to defer an item, in Plan Mode or at Retro.

Then:
In the same reply the agent appends the Case in the short form — `context`, `problem`, the `defer` block, no `ratification` section — under `## Deferred` of the plan file, or of `raw/<date>/<hi HHMM>/spec.md` at Retro, shows it in the chat, and ends the reply with its `LEDGER` block, one `defer` line per target.
**＋** The person's words asking for the defer are its ratification: no question asks for it.
**＋** In Plan Mode the reply ends with the Frontier, the line of the item closed `[-] … · defer case N`; at Retro no Frontier is shown.
**＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, written the same way.

## History

- 2026-09-25 created · [[decision-case-405]]
