---
type: estimate
kind: QA
status: pending
target: "[[rule-ask]]"
purpose: Whether ask-guppi at /pre-spec reads no Decision page, the Decision of a page with deferred_by left unread whether a finding names the page or not
method: "by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the Read and Grep calls of ask-guppi on vault/wiki/decisions/ in its agent transcript read against the Criterion, recorded in the estimate line (the render of case 925.4)"
checked: 2026-10-14
origin: raw/2026-10-13/1753/ledger.md#case-800.2
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness]
---

## Criterion

When:
At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
`ask-guppi` runs no Read of a page under `vault/wiki/decisions/` and no Grep whose `path` is that folder or lies in it.
**＋** A page that carries `deferred_by` has its Decision left unread, whether a finding names the page or not, and also when a Case of the plan changes that page.
**－** What a finding on a page with `deferred_by` gives is outside this promise: `estimate-ask-finds` reads it.
**－** Whether the hook refuses such a call is outside this promise: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads it.
**－** Decision reads by the main agent and by `case-guppi` are outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads them.

## Result

2026-10-14, Work readings of session 0101, the agent transcript of the ask-guppi run of this session's /pre-spec, which ran on .claude/agents/ask-guppi.md as rendered by case 800.2: of its 85 tool calls no Read and no Grep names a path under vault/wiki/decisions/; the 6 Greps over vault/wiki or the repository root match the 6 times the string !**/decisions/** stands in the transcript; the pages with deferred_by that Case 809 changes (rule-page-generation, rule-work-mode, entity-sprint-plugin) had their Decisions left unread

## History

- 2026-10-13 created · [[decision-case-800.2]]
- 2026-10-14 status: pending → passed · raw/2026-10-14/0101/ledger.md#L55
- 2026-10-15 updated: the pointer of the method stands in a bracket at its end · [[decision-case-823.1]]
- 2026-10-30 updated: the Criterion replaced whole — ask-guppi reads no Decision page at /pre-spec (case 925.4) · [[decision-case-925.4]]
