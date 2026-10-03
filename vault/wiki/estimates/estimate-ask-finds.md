---
type: estimate
kind: QA
status: failed
target: "[[rule-ask]]"
purpose: ask-guppi finds a page by meaning in either language, names the rule a proposal crosses and the state of a named slug, and answers in five lines, a list of the paths of the files it read allowed after them
method: "by hand in a later session: three dispatches of ask-guppi, one existing page asked in English and in Russian, one proposal that crosses a known rule, each read against the event log"
checked: 2026-10-04
origin: raw/2026-09-09/ledger.md#case-23.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent dispatches `ask-guppi` through the `Agent` tool with a question, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
The answer opens with exactly five lines: `exists`, `near`, `missing`, `rules` and the tags/slug line, each present, "none" when empty.
**＋** After the five lines a list of the paths of files the agent read may stand, as the general note of Claude Code asks of a sub-agent.
**＋** The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
**＋** A question about an existing page names its slug under `exists`, whether it is asked in English or in Russian.
**＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names it on the `rules` line.
**＋** A named slug gets on the tags/slug line `free`, `live` with its category, or `archived at <path> by [[decision-case-N]]`, found by a Glob over `vault/archive/`, N from the `origin` of the archived page.
**＋** The agent opens an archived page only when the question names its slug and asks what it said or why it was withdrawn.
**＋** Each dispatch stands in `vault/raw/<date>/event_log.md`.
**－** No index line, page text or other note reaches the caller beyond the five lines and that list of paths.
**－** An answer with no list after the five lines holds the promise as well.
**－** The archive is not searched by meaning: the `exists` and `near` lines name live pages only.

## Result

2026-10-04, session 0004, by hand: the four dispatches of ask-guppi since the Criterion of case 582, each at /pre-spec, read in their agent transcripts against the event log lines `02:35:24 cf8077b8`, `04:47:32 5b311f89`, `14:11:01 26e79919` and `14:36:33 682b0e2f` of vault/raw/2026-10-03/event_log.md: each started with the Grep `^(purpose|deferred_by):` over vault/wiki/rules/; the answer of 1341 is the five lines exists, near, missing, rules and tags/slug; the answer of 0115 opens with the five labels but holds nested list lines under each; the answer of 0317 opens "Six findings across 611, 612 and 613" and goes on in numbered sections with a Files list, and the answer of 1416 opens "The plan has no Case" with three numbered points, so two of four do not open with the five lines that `.claude/agents/ask-guppi.md` and the Criterion require, while the /pre-spec skill asks the agent for three kinds of findings; not exercised: a page asked in English and in Russian, a proposal that crosses a rule, a named slug checked in the archive

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-23.1
- 2026-09-10 status: pending → passed · written by hand, no generator yet
- 2026-09-13 criterion: case 105.1 added · [[decision-case-105.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L39
- 2026-09-14 criterion: case 147.2 added · [[decision-case-147.2]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L4
- 2026-09-29 updated: the Criterion replaced whole — the head and the blocks 105.1 and 147.2 into one When and Then, the one-time questions and the index files out; purpose and method set, Context and Method out (case 500.1) · [[decision-case-500.1]]
- 2026-10-01 status: pending → failed · raw/2026-10-01/1441/ledger.md#L33
- 2026-10-01 updated: the Criterion replaced whole — a list of file paths may follow the five lines, as the general note of Claude Code asks of a sub-agent; nothing else follows them (case 582) · [[decision-case-582]]
- 2026-10-04 status: pending → failed · raw/2026-10-04/0004/ledger.md#L17
- 2026-10-04 deferred · [[decision-case-623]]
