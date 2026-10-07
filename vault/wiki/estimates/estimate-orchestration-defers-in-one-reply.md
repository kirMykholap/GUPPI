---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: A decision the person asks to put off in Plan Mode, from a source other than the sprint or the backlog, is shown as a short-form Case and written in the same reply, with no round of ratification
method: by hand, a decision the person asks to put off, its line of frontier.md closed [-] … · defer case N, in a reply that leaves no line under the Cases heading of frontier.md open; a sprint item put off or a backlog item kept is not this reading
checked: 2026-10-07
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
**－** No text follows the question, or the Frontier when no question stands.
**－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
**－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line, and a reply that closes only such lines is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.

## Result

2026-10-07, Retro, the new Render of rule-orchestration in the Spec (case 697.3): its anchor stands once; the defer reply on an empty Frontier before /pre-spec ends with the question whether to go on, with no text after it, as the Criterion sets

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
