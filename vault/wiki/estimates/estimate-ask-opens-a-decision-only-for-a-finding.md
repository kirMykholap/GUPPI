---
type: estimate
kind: QA
status: pending
target: "[[rule-ask]]"
purpose: Whether ask-guppi at /pre-spec opens the Decision behind a page with deferred_by only for a page that a finding of its answer names
method: "by hand, after a /pre-spec whose ask-guppi runs on .claude/agents/ask-guppi.md as rendered by case 800.2: the Read and Grep calls of ask-guppi on vault/wiki/decisions/ in its agent transcript and the findings of its answer read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-13/1753/ledger.md#case-800.2
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness]
---

## Criterion

When:
At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
Each page under `vault/wiki/decisions/` that `ask-guppi` reads, by a Read or by a Grep inside that folder, for a page that carries `deferred_by`, is the Decision of a page that a finding of its answer names.
**＋** A page that carries `deferred_by` and stands in no finding has its Decision left unread, also when a Case of the plan changes that page.
**－** A Decision read because the question asks why something was decided, reached through the `origin` of a page, is outside this promise.
**－** Decision reads by the main agent and by `case-guppi` are outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads them.

## History

- 2026-10-13 created · [[decision-case-800.2]]
