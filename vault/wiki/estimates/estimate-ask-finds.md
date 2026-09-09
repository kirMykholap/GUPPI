---
type: estimate
kind: QA
status: pending
target: rule-ask
origin: raw/2026-09-09/ledger.md#case-23.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Context

The agent replaces reading category folders by hand. What has to hold is that it finds a
page by meaning in either language, names the rule a proposal crosses, and costs the
caller nothing but its five lines; and two things nobody measured yet — whether `@`
expands in an agent file, and what one dispatch costs in tokens.

## Criterion

Three live dispatches once the indexes exist: a question about an existing page, in
English, names its slug under `exists`; the same question in Russian names the same slug;
a proposal crossing a known rule (a `SessionStart` hook meant to block) names the rule or
lesson under `rules`. Each answer is the five lines, no index or page text reaches the
caller's context, each dispatch is in the event log; the reading records whether `@`
expanded and the tokens of one dispatch.

## Method

Three readings by hand in one session, written into the estimate line — the exception the
Method rule allows.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-23.1
