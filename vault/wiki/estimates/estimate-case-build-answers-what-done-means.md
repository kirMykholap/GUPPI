---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether each Case case-guppi builds creates or replaces an Estimate or names the one that already checks the change, and asks in a round when it can do neither
method: by hand at the close of a later session, each Case of the plan and the rounds before it read in the transcript
origin: raw/2026-09-30/2356/ledger.md#case-561.11
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
`case-guppi` answers with a Case, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`.

Then:
Each Case and sub-case of the answer creates an Estimate or replaces the Criterion of one, or its `context`, or its parent's, names by slug the Estimate that already checks the change and says why its Criterion stands.
**＋** When the person's words and the frame give neither, `case-guppi` asks in a round, before it answers with the Case, what the Estimate will check, and the `recommend` of the Case holds that question.
**－** A deferred decision in the short form is no answer of `case-guppi` and carries no such Estimate.

## History

- 2026-10-01 created · [[decision-case-561.11]]
