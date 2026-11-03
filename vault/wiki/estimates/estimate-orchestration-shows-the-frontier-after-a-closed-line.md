---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether a reply after the first reply of /hi that closes a Frontier line in Plan Mode with no ratification and no defer ends with the Frontier and the question which item is next
method: "by hand, in a later session: the first reply in Plan Mode after the first reply of /hi that closes a line of frontier.md with no ratification and no defer, read against the Criterion"
checked: 2026-10-07
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
After the first reply of `/hi` and before the end of Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

Then:
The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-orchestration-acknowledging-reply` sets.
**＋** In the checklist the closed lines are folded into one line, and the lines put off stand as they are closed.
**＋** The open `W` lines are folded into one line that lists their ids.
**＋** Each other open line stands on its own line with a short title.
**＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
**＋** When no line under `## Cases` is open before `/pre-spec`, the question whether to go on to `/pre-spec` follows the Frontier and ends the reply, with a `LEDGER` block or without one. The agent calls `/pre-spec` only after the person says to go on.
**＋** When no line under `## Cases` is open after `/pre-spec`, no question follows the Frontier. A reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on. A reply with no `LEDGER` block goes on by itself after the Frontier, to the check and the exit or on with the loop after the findings, as `rule-prespec` sets it.
**＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
**＋** When the line it closes is the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, the turn of the person's words ends with one `**Waiting:**` line once the drop has gone to that `case-guppi`, and this reply comes in the turn that its answer `**Dropped:**` opens.
**－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
**－** The reply that takes a conserved Spec and closes the other lines goes on to `/pre-spec` with no question, as `rule-skill-hi` sets it.
**－** A line closed in Work Mode or at Retro shows no Frontier.
**－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-orchestration-acknowledging-reply` sets it.

## Result

2026-10-07, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
