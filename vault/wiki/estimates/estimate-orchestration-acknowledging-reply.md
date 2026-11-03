---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: The reply that acknowledges a ratification has four parts in order
method: "by hand, after the librarian's render that writes into vault/wiki/orchestration.md the paragraph of rule-orchestration that names each heading and label of the acknowledging reply by what it says, with no English word for it in a code span or in bold: an acknowledging reply and a reply that acknowledges Cases ratified together in one answer, each written after that render, each read against the Criterion in the transcript of its session under ~/.claude/projects/"
checked: 2026-11-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, ledger]
core: true
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

2026-11-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
