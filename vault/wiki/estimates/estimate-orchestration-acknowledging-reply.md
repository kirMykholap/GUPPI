---
type: estimate
kind: QA
status: failed
target: "[[rule-orchestration]]"
purpose: The reply that acknowledges a ratification has four parts in order
method: "by hand, after the librarian's render that writes into vault/wiki/orchestration.md the paragraph of rule-orchestration that names the headings and labels of the acknowledging reply as translated: an acknowledging reply and a reply that acknowledges Cases ratified together in one answer, each written after that render, each read against the Criterion in the transcript of its session under ~/.claude/projects/"
checked: 2026-11-02
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
---

## Criterion

When:
The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The reply has four parts, in this order. First, the `LEDGER` block, before which stands nothing but the `STOP:` line that `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` checks. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
**＋** Each heading and label of the reply stands translated into the language of the chat that `CLAUDE.md` sets: the heading `## Case N — ratified`, the labels `Changes:` and `Notes:` and the heading `## Frontier` stand in that language, not in the English words by which this Criterion names them.
**＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
**＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
**＋** While a line under `## Cases` is open, the question which item is next ends the reply.
**＋** When none is open before `/pre-spec`, the question whether to go on to `/pre-spec` ends the reply, in the plain form of the question which item is next. The agent calls `/pre-spec` only after the person says to go on. A reply that answers a question of the person instead ends with the same question again.
**＋** When none is open after `/pre-spec`, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
**＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
**＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
**＋** No tool call follows the `LEDGER` block in the same reply.
**－** Slugs, paths, the tag of the `LEDGER` block, the ledger lines and the word `STOP:` that opens a reply keep their own words in any language of the chat; the rest of the `STOP:` line stands in the language of the chat.
**－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
**－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written, but for a decision line the ledger hook holds, as `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` sets it.

## Result

2026-11-02, session 0254 (hi 68effdf4), the reply that acknowledges Case 1001, read against the Criterion in this session's transcript: the LEDGER block first, the heading of the Case and the labels Changes and Notes in Russian, closed lines and W lines folded, the closing question whether to go on to /pre-spec, no tool call after the block all held; the heading ## Frontier stood in English, not translated into the language of the chat; no reply that acknowledges Cases ratified together came in this session

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
- 2026-10-06 updated: the Criterion replaced whole — the LEDGER block stands written after a refusal of another hook, but for a decision line the ledger hook holds (case 688.9) · [[decision-case-688.9]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L43
- 2026-10-07 updated: the Criterion replaced whole — on an empty Frontier before /pre-spec the reply asks whether to go on · [[decision-case-697.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L36
- 2026-11-01 updated: the Criterion replaced whole — after /pre-spec, a reply that waits for the person opens with STOP:, the LEDGER block right after it · [[decision-case-992.2]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/2038/ledger.md#L22
- 2026-11-02 updated: the Criterion replaced whole — the STOP: line after /pre-spec split off into its own Estimate · [[decision-case-993.1]]
- 2026-11-02 status: pending → failed · raw/2026-11-01/2227/ledger.md#L21
- 2026-11-02 updated: the Criterion replaced whole — each heading and label of the reply stands translated into the language of the chat; the reading waits for the render · [[decision-case-997]]
- 2026-11-02 status: pending → failed · raw/2026-11-02/0254/ledger.md#L4
