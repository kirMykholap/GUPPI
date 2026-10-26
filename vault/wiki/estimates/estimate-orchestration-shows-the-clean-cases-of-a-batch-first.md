---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether, when the Stop check of rule-case-check refuses the showing of a batch for a finding stored with one of its Cases, the main agent sends that Case back to its case-guppi, out of the batch, and shows the other Cases for ratification, before /pre-spec and in the loop after its findings
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-26/0118/ledger.md#case-890.3
sprint: plugin
created: 2026-10-26
tags: [session, workflow]
---

## Criterion

When:
In Plan Mode, the `Stop` check of `rule-case-check` refuses a reply of the main agent that shows the Cases of a batch, for a finding that `<plan>.checked.json` holds with one of them, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The main agent sends the Case whose finding the refusal names, with its top-level Case and each sub-case of that file, back to its `case-guppi` by `SendMessage` with the finding, and that Case leaves the batch.
**＋** In its answer to the refusal it shows the other Cases of the batch, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification, and the person ratifies them at once or names the ids.
**＋** The Case sent back is shown when its `case-guppi` answers, as a Case the person questions or changes is shown again: alone when no other Case of the session is out, and otherwise in a batch with the Cases still out.
**＋** The answer to the refusal ends as a showing ends, its own text after the horizontal rule naming the Case sent back as still out; the Case sent back is out of the batch, so neither the `**Waiting:**` line of a batch nor the joining of Cases out at the same time holds for it in that answer.
**＋** Each later turn that ends while its `case-guppi` has not answered, and while no Case shown waits for the person's word, ends with one line under the bold label `**Waiting:**`, translated, that names the Case sent back, and nothing else.
**＋** This holds in every batch before `/pre-spec` and in the loop after the findings of `/pre-spec` that `rule-prespec` sets.
**－** A refusal for a file not sent, or for a showing that differs from the stored text, sends no Case back: the main agent sends the file and shows the Cases as `vault/wiki/orchestration.md` sets it.
**－** The main agent puts before the person no Case that the check refused for a stored finding.

## Result

2026-10-26, Retro of 0118, by hand: the two new pairs of rule-orchestration in the Spec of 0118 read against the Criterion of 890.3 — the Case with a stored finding goes back by SendMessage with each Case of its file and leaves the batch, the answer to the refusal shows the others for one ratification and ends as a showing naming the Case sent back, later turns end with a Waiting line naming it, before /pre-spec and in the loop after its findings, a refusal for a file not sent sends no Case back, and the sentence of case 730.1 makes the Case sent back no route of Cases out at once

## History

- 2026-10-26 created · [[decision-case-890.3]]
- 2026-10-26 status: pending → passed · raw/2026-10-26/0118/ledger.md#L22
