---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
purpose: Whether a reply after the first reply of /hi that closes a Frontier line in Plan Mode with no ratification and no defer ends with the Frontier and the question which item is next
method: "by hand, in a later session: the first reply in Plan Mode after the first reply of /hi that closes a line of frontier.md with no ratification and no defer, read against the Criterion"
checked: 2026-10-02
origin: raw/2026-09-30/1736/ledger.md#case-547
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
After the first reply of `/hi` and before the end of Plan Mode, with `vault/wiki/case-schema.md` rendered from `rule-case-protocol`, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

Then:
The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-case-protocol-acknowledging-reply` sets.
**＋** In the checklist the closed lines are folded into one line, and the lines put off stand as they are closed.
**＋** The open `W` lines are folded into one line that lists their ids.
**＋** Each other open line stands on its own line with a short title.
**＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
**＋** When no line under `## Cases` is open, no question follows the Frontier: a reply with no `LEDGER` block calls `/pre-spec` after it, and a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on.
**＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
**－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
**－** A line closed in Work Mode or at Retro shows no Frontier.
**－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-case-protocol-acknowledging-reply` sets it.

## Result

2026-10-02, by hand in the transcript of session 1a155152: the first Plan Mode reply after the first reply of /hi that closed lines with no ratification and no defer, C1 [-] · sprint · defer and C7 [-] · backlog · kept, ended with the heading Frontier, the closed lines folded into one (C2–C6 · cases 587–591), the put-off lines as closed, the open W lines folded into one line W1–W28, no question since no line under Cases stood open, then called /pre-spec, the reply carrying no LEDGER block

## History

- 2026-09-30 created · [[decision-case-547]]
- 2026-10-01 updated: the Criterion replaced whole - no question when no line under Cases is open; the reply calls /pre-spec or ends for the hook (case 561.6) · [[decision-case-561.6]]
- 2026-10-01 status: pending → failed · raw/2026-10-01/1237/ledger.md#L35
- 2026-10-01 updated: the Criterion replaced whole — the open W lines are folded into one line that lists their ids; each other open line stands on its own line (case 578.1) · [[decision-case-578.1]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1202/ledger.md#L55
