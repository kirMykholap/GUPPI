---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: A decision the person asks to put off in Plan Mode, from a source other than the sprint or the backlog, is shown as a short-form Case and written in the reply that shows it, with no round of ratification; when the item has a Case built and not ratified, that reply comes in the turn that the answer Dropped of its case-guppi opens
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
checked: 2026-10-08
origin: raw/2026-09-24/1916/ledger.md#case-405
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Criterion

When:
In Plan Mode, the person asks in the chat to put off a decision: an item of `raw/<date>/<hi HHMM>/frontier.md` whose source is neither the sprint nor the backlog, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
**＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
**＋** The person's words asking for the defer are its ratification: no question asks for it.
**＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
**＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
**＋** When no line under `## Cases` is open before `/pre-spec`, the question whether to go on to `/pre-spec` follows the Frontier and ends the reply. The agent calls `/pre-spec` only after the person says to go on.
**＋** When no line under `## Cases` is open after `/pre-spec`, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on with the loop after the findings.
**＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
**＋** When the item has a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, the drop goes to that `case-guppi` first and the turn of the person's words ends with one `**Waiting:**` line; the short Case, its `LEDGER` block and the Frontier come in the turn that the answer `**Dropped:**` opens.
**－** No text follows the question, or the Frontier when no question stands.
**－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
**－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line but for the short Case of a take-back of a ratified Case, which is the moment of `estimate-orchestration-takes-back-a-ratified-case`, and a reply that closes only such lines with no take-back is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.

## Result

2026-10-08, the person's decision, case 728: the Render of rule-orchestration as it stands read against the Criterion; each line of the Criterion is stated in it
2026-10-07, Retro, not read: its method needs a decision of a source other than the sprint or the backlog put off with its line closed [-] … · defer case N; in session 2114 only the sprint items C1 and C2 were put off, closed · sprint · defer, which the method excludes

## History

- 2026-09-25 created · [[decision-case-405]]
- 2026-09-25 updated: the Criterion replaced whole — the agent shows the defer, the hook writes it (case 421.2) · [[decision-case-421.2]]
- 2026-09-26 status: pending → failed · raw/2026-09-26/1745/ledger.md#L35
- 2026-09-27 status: failed → failed · raw/2026-09-27/1255/ledger.md#L53
- 2026-09-27 updated: the Criterion replaced whole — in Plan Mode a question of what comes next follows the Frontier and ends the defer reply (case 461) · [[decision-case-461]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1134/ledger.md#L71
- 2026-09-29 updated: the method reads a defer that closes the last Cases line, the branch that failed; the Criterion and the failed status stand (case 523) · [[decision-case-523]]
- 2026-09-30 updated: the Criterion replaced whole — a defer the person asks for in Plan Mode; Retro writes no short defer (case 531.14) · [[decision-case-531.14]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0248/ledger.md#L37
- 2026-10-01 updated: the Criterion replaced whole - no question when no line under Cases is open; the reply ends with the Frontier (case 561.7) · [[decision-case-561.7]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L31
- 2026-10-02 renamed from `estimate-case-protocol-defers-in-one-reply` · [[decision-case-595.10]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the short form as orchestration.md sets it (case 595.10) · [[decision-case-595.10]]
- 2026-10-03 updated: the Criterion replaced whole — the trigger is a decision put off, not an item of the sprint or the backlog; their closers are not this moment (case 609) · [[decision-case-609]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L5
- 2026-10-07 updated: the Criterion replaced whole — on an empty Frontier before /pre-spec the defer reply asks whether to go on · [[decision-case-697.3]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L38
- 2026-10-07 updated: the Criterion replaced whole — the short Case of an item whose built Case is dropped comes in the turn of the answer Dropped · [[decision-case-701.5]]
- 2026-10-07 status: pending → failed · raw/2026-10-07/0425/ledger.md#L25
- 2026-10-07 status: failed → passed · raw/2026-10-07/0636/ledger.md#L13
- 2026-10-07 updated: the Criterion replaced whole — a sprint or backlog item takes no short Case but for the short Case of a take-back (case 723.2) · [[decision-case-723.2]]
- 2026-10-07 status: pending → failed · raw/2026-10-07/2114/ledger.md#L22
- 2026-10-08 updated: the method reads the new Render of rule-orchestration in the Spec at Retro; passed by the person's decision, the Criterion written back unchanged (case 728) · [[decision-case-728]]
