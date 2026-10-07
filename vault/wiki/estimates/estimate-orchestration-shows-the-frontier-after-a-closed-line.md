---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether a reply after the first reply of /hi that closes a Frontier line in Plan Mode with no ratification and no defer ends with the Frontier and the question which item is next
method: "by hand, in a later session: the first reply in Plan Mode after the first reply of /hi that closes a line of frontier.md with no ratification and no defer, read against the Criterion"
checked: 2026-10-07
origin: raw/2026-09-30/1736/ledger.md#case-547
sprint: migration
created: 2026-09-30
tags: [session, workflow]
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
**－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
**－** The reply that takes a conserved Spec and closes the other lines goes on to `/pre-spec` with no question, as `rule-skill-hi` sets it.
**－** A line closed in Work Mode or at Retro shows no Frontier.
**－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-orchestration-acknowledging-reply` sets it.

## Result

2026-10-07, Retro, the new Render of rule-orchestration in the Spec (case 697.2): its anchor stands once; before /pre-spec the reply asks whether to go on, with a LEDGER block or without, the conserved Spec taken at /hi excepted; after /pre-spec a reply with no block goes on by itself, as the Criterion sets

## History

- 2026-09-30 created · [[decision-case-547]]
- 2026-10-01 updated: the Criterion replaced whole - no question when no line under Cases is open; the reply calls /pre-spec or ends for the hook (case 561.6) · [[decision-case-561.6]]
- 2026-10-01 status: pending → failed · raw/2026-10-01/1237/ledger.md#L35
- 2026-10-01 updated: the Criterion replaced whole — the open W lines are folded into one line that lists their ids; each other open line stands on its own line (case 578.1) · [[decision-case-578.1]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1202/ledger.md#L55
- 2026-10-02 ref `estimate-case-protocol-acknowledging-reply` → `estimate-orchestration-acknowledging-reply` · [[decision-case-595.8]]
- 2026-10-02 renamed from `estimate-case-protocol-shows-the-frontier-after-a-closed-line` · [[decision-case-595.9]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the reply as orchestration.md sets it (case 595.9) · [[decision-case-595.9]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L22
- 2026-10-07 updated: the Criterion replaced whole — on an empty Frontier before /pre-spec the reply asks whether to go on · [[decision-case-697.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L37
