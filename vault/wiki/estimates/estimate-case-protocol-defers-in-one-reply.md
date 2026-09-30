---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
purpose: A defer the person asks for is shown and written in the same reply, with no round of ratification
method: "by hand, the first defer the person asks for after the render that leaves no line under ## Cases of frontier.md open"
checked: 2026-09-30
origin: raw/2026-09-24/1916/ledger.md#case-405
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Criterion

When:
The person asks in the chat to defer an item in Plan Mode.

Then:
In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
**＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
**＋** The person's words asking for the defer are its ratification: no question asks for it.
**＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
**＋** A question follows the Frontier and ends the reply: which open item is next, or, when no line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, whether to run `/pre-spec` of `rule-prespec`.
**＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
**－** No text follows that question.
**－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.

## Result

2026-09-30, by hand, the first defer after the render: to the person's words "Откладываем все остальное" the one reply of session 0248 showed Case 540 in the short form (context, problem and a then fence with one defer item, rule-work-mode) and its LEDGER block with one defer line, no tool call after it; the agent wrote nothing into the plan file and the Stop hook put Case 540 under ## Deferred; the reply asked no question on the defer, showed the Frontier with C4 closed "[-] … · brief · defer case 540" and C2 "[-] … · sprint · defer", and ended with the question whether to run /pre-spec, no line under ## Cases being open

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
