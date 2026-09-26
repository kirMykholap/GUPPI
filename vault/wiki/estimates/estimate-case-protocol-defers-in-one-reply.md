---
type: estimate
kind: QA
status: failed
target: "[[rule-case-protocol]]"
purpose: A defer the person asks for is shown and written in the same reply, with no round of ratification
method: by hand, the first defer the person asks for after the render
checked: 2026-09-26
origin: raw/2026-09-24/1916/ledger.md#case-405
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Criterion

When:
The person asks in the chat to defer an item, in Plan Mode or at Retro.

Then:
In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
**＋** The agent writes nothing of the Case into the plan file or `spec.md`: the `Stop` hook of `rule-spec-write` writes it.
**＋** The person's words asking for the defer are its ratification: no question asks for it.
**＋** In Plan Mode the reply ends with the Frontier, the line of the item closed `[-] … · defer case N`; at Retro no Frontier is shown.
**＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.

## Result

2026-09-26, by hand, transcript of session 1745 at 22:00:17 and the plan edit at 22:01:43; Case 442 was shown in the short form with its LEDGER defer line and no tool call after it, but the agent then edited the plan file to translate its heading, context and problem, and text followed the Frontier in the reply

## History

- 2026-09-25 created · [[decision-case-405]]
- 2026-09-25 updated: the Criterion replaced whole — the agent shows the defer, the hook writes it (case 421.2) · [[decision-case-421.2]]
- 2026-09-26 status: pending → failed · raw/2026-09-26/1745/ledger.md#L35
