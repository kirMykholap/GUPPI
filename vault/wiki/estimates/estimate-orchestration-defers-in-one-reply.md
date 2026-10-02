---
type: estimate
kind: QA
status: pending
target: "[[rule-orchestration]]"
purpose: A defer the person asks for is shown and written in the same reply, with no round of ratification
method: "by hand, the first defer the person asks for after the render that leaves no line under ## Cases of frontier.md open"
checked: 2026-10-01
origin: raw/2026-09-24/1916/ledger.md#case-405
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Criterion

When:
The person asks in the chat to defer an item in Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
**＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
**＋** The person's words asking for the defer are its ratification: no question asks for it.
**＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
**＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
**＋** When no line under `## Cases` is open, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on.
**＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
**－** No text follows the question, or the Frontier when no question stands.
**－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.

## Result

2026-10-01, by hand, session 1237, the reply of 14:08:36 deferring C2, C3, C5-C9: each short-form Case shows context, problem and a then fence with one defer item and no other section; one LEDGER block of seven defer lines and no tool call after it; the agent wrote nothing into the plan file and the Spec hook wrote the seven under Deferred; no question asked about the defers; the Frontier shows C1 closed · sprint · defer and the others · defer case 570 to 576; with no open line under Cases the reply ended with the Frontier, and guppi onward --plan sent the agent on to /pre-spec; not exercised: a corrected wording with supersedes

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
