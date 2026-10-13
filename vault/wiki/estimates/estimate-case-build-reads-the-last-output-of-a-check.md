---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, before it recommends an option that rests on whether a check passes, reads what that check printed at its last run, from the brief, judges the option against it, or by the state at the moment the check runs where another Case of the session changes the check or the pages it reads, and names it in context, or says in the After line and context that the output was not read
method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-13/1426/ledger.md#case-798.2
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, writes a round with an option that rests on whether a check passes, such as `make lint`, `make test` or a check on GitHub.

Then:
Before it recommends that option, it reads what that check printed at its last run, as `## Flags` and `## Readings at the close` of `vault/wiki/brief.md` report it, judges the option against that output, and quotes it with its source in the `context`.
**＋** Where another Case of the same session changes that check or the pages it reads, it judges the option by the state at the moment the check runs, as `rule-case-build` sets it for such a Case, and not by the last output alone.
**＋** Where the brief does not report that output, the `**After:**` line of the option and the `context` say that its last output was not read.
**－** An option whose last output was not read may still be recommended.

## Result

2026-10-13, Retro of session 1426, the new Render sentence of rule-case-build in raw/2026-10-13/1426/spec.md (case 798.2) read against the Criterion: it reads the last output from ## Flags and ## Readings at the close of the brief, judges the option against it, defers to the state at the moment the check runs where another Case of the session changes the check, and says in the After line and context when the output was not read; but it says only that `context` names that output, not that it quotes it with its source, which the first Then line asks

## History

- 2026-10-13 created · [[decision-case-798.2]]
- 2026-10-13 status: pending → failed · raw/2026-10-13/1426/ledger.md#L28
