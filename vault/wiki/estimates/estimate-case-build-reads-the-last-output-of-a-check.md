---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, before it recommends an option that rests on whether a check passes, reads what that check printed at its last run, from the brief, judges the option against it, or by the state at the moment the check runs where another Case of the session changes the check or the pages it reads, and quotes it with its source in context, or says in the After line and context that the output was not read
method: "by hand: the Render of rule-case-build in .claude/agents/case-guppi.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-13
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, writes a round with an option that rests on whether a check passes, such as `uv run --project .guppi guppi check`, `uv run --project .guppi guppi test` or a check on GitHub.

Then:
Before it recommends that option, it reads what that check printed at its last run, as `## Flags` and `## Readings at the close` of `vault/wiki/brief.md` report it, judges the option against that output, and quotes it with its source in the `context`.
**＋** Where another Case of the same session changes that check or the pages it reads, it judges the option by the state at the moment the check runs, as `rule-case-build` sets it for such a Case, and not by the last output alone.
**＋** Where the brief does not report that output, the `**After:**` line of the option and the `context` say that its last output was not read.
**－** An option whose last output was not read may still be recommended.

## Result

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
