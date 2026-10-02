---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: The reply that acknowledges a ratification has four parts in order
method: one reading by hand of the first acknowledging reply of a session, and of the first reply that acknowledges Cases ratified together in one answer
checked: 2026-10-03
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
---

## Criterion

When:
The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
**＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
**＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
**＋** While a line under `## Cases` is open, the question which item is next ends the reply; when none is open, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
**＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
**＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
**＋** The headings and labels are in the language of the chat.
**＋** No tool call follows the `LEDGER` block in the same reply.
**－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
**－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written.

## Result

2026-10-03, by hand in the transcript of session 2300: the first acknowledging reply (Case 601) and the reply that acknowledged 601.1–601.5, 602, 603.1, 603.2 and 605 ratified in one answer each open with the LEDGER block, then one heading naming the ids, Changes:, Notes:, the Frontier with the closed lines folded into one and the open W lines into one; the first ends with the question which item is next, the batch reply ends with the Frontier while no Cases line was open; re-ratified Cases carry their lines again; headings in Russian; no tool call after the block

## History

- 2026-09-16 created · [[decision-case-188]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L36
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-23 updated: the Criterion names the one acknowledging reply of a Case with sub-cases (case 355.2) · [[decision-case-355.2]]
- 2026-09-23 updated: the other replies are not measured here, their form stands in the schema (case 368) · [[decision-case-368]]
- 2026-09-24 updated: the Criterion replaced whole — the LEDGER block of a re-ratification (case 390) · [[decision-case-390]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L16
- 2026-09-25 updated: the Criterion replaced whole — the answer to a Stop hook's refusal is a reply of its own (case 414.2) · [[decision-case-414.2]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1228/ledger.md#L38
- 2026-09-27 updated: the Criterion replaced whole — the lines put off shown by the closers of case 451 (case 451.10) · [[decision-case-451.10]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L19
- 2026-10-01 updated: the Criterion replaced whole - the question which item is next only while a line under Cases is open (case 561.8) · [[decision-case-561.8]]
- 2026-10-01 status: pending → failed · raw/2026-10-01/1237/ledger.md#L30
- 2026-10-01 updated: the Criterion replaced whole — the open W lines are folded into one line that lists their ids; each other open line stands on its own line (case 578.2) · [[decision-case-578.2]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1725/ledger.md#L14
- 2026-10-02 renamed from `estimate-case-protocol-acknowledging-reply` · [[decision-case-595.8]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the reply as orchestration.md sets it (case 595.8) · [[decision-case-595.8]]
- 2026-10-02 updated: the Criterion replaced whole — one reply acknowledges every Case ratified in one answer (case 598.2) · [[decision-case-598.2]]
- 2026-10-03 status: pending → passed · raw/2026-10-02/2300/ledger.md#L23
