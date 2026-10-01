---
type: estimate
kind: QA
status: failed
target: "[[rule-ask]]"
purpose: ask-guppi finds a page by meaning in either language, names the rule a proposal crosses and the state of a named slug, and answers in five lines
method: "by hand in a later session: three dispatches of ask-guppi, one existing page asked in English and in Russian, one proposal that crosses a known rule, each read against the event log"
checked: 2026-10-01
origin: raw/2026-09-09/ledger.md#case-23.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent dispatches `ask-guppi` through the `Agent` tool with a question, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
The answer is exactly five lines: `exists`, `near`, `missing`, `rules` and the tags/slug line, each present, "none" when empty. No index line or page text reaches the caller beyond them.
**＋** The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
**＋** A question about an existing page names its slug under `exists`, whether it is asked in English or in Russian.
**＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names it on the `rules` line.
**＋** A named slug gets on the tags/slug line `free`, `live` with its category, or `archived at <path> by [[decision-case-N]]`, found by a Glob over `vault/archive/`, N from the `origin` of the archived page.
**＋** The agent opens an archived page only when the question names its slug and asks what it said or why it was withdrawn.
**＋** Each dispatch stands in `vault/raw/<date>/event_log.md`.
**－** The archive is not searched by meaning: the `exists` and `near` lines name live pages only.

## Result

2026-10-01, by hand, three dispatches of ask-guppi in session 1441 at 17:11:15 (event_log lines 1075-1077): a page asked in English and in Russian whether a rule sends the agent from Retro to /handoff, both naming rule-retro-onward under exists; a proposal of a SessionStart hook that blocks until /hi, whose rules line names lesson-hooks-sessionstart-cannot-block, rule-session-start and rule-hook-registry and whose tags/slug line gives the slug free after a Glob over vault/archive/; each dispatch stands in the event log; but the English answer and the SessionStart answer each add a Files: list of six and five page paths after the five lines, against exactly five lines and nothing beyond them; the Russian answer holds five lines

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-23.1
- 2026-09-10 status: pending → passed · written by hand, no generator yet
- 2026-09-13 criterion: case 105.1 added · [[decision-case-105.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L39
- 2026-09-14 criterion: case 147.2 added · [[decision-case-147.2]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L4
- 2026-09-29 updated: the Criterion replaced whole — the head and the blocks 105.1 and 147.2 into one When and Then, the one-time questions and the index files out; purpose and method set, Context and Method out (case 500.1) · [[decision-case-500.1]]
- 2026-10-01 status: pending → failed · raw/2026-10-01/1441/ledger.md#L33
