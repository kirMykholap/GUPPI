---
type: estimate
kind: QA
status: passed
target: "[[rule-ask]]"
purpose: Whether ask-guppi at /pre-spec reads no Decision page, the Decision of a page with deferred_by left unread whether a finding names the page or not
method: "by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the Read and Grep calls of ask-guppi on vault/wiki/decisions/ in its agent transcript read against the Criterion, recorded in the estimate line"
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
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

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
