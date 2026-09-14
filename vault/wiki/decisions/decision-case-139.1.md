---
type: decision
case: "139.1"
status: current
update: [rule-render-harness]
origin: raw/2026-09-14/1229/ledger.md#case-139.1
sprint: migration
created: 2026-09-14
tags: [harness, render]
---

## Context

An Insight of severity 2, the oldest (2026-09-10), two children with opposite claims: session D rendered `ask-guppi.md` and three calls in a row got "Agent type not found"; session E rendered `librarian-guppi.md` at 10:40 and the Agent tool saw it at 10:52 without a restart. The difference was not measured. Proposal: one reading — render a throwaway agent mid-session, dispatch it at once, record the result and the session state; until then plan as if a rendered agent were unusable in its own session.

## Problem

Four sessions took no reading, because nothing pressed for it: the librarian's render is the last step before its commit, and its frames apply in the next session anyway. But the Insight stands in the brief and two lessons contradict each other. Decide: take the reading now, in this session's Work Mode, and close the Insight — or close it unmeasured.

## Given

`insight-harness-agent-visibility`: `open`, `severity: 2`, children `lesson-agents-loaded-at-session-start` (root cause: agents are read at session start), `lesson-agents-visible-in-session` (root cause: the list is re-read during the session); both `clustered`.
**＋** `rule-render-harness` (`Leaf`, `check`, `built`, `estimate-render-harness-reproduces` `passed`, `estimate-render-sync-reports`): writes the governed files, `.claude/agents/ask-guppi.md` and `librarian-guppi.md` among them; the page says nothing about when Claude Code reads an agent.
**＋** `guppi guard` (59.6) refuses only a path a live Rule governs; `.claude/agents/probe-guppi.md` is governed by none — the write passes.
**＋** The agent list of this session in the system prompt holds `ask-guppi`, `librarian-guppi` and the built-in ones — enumerated at start; whether it is re-read during the session is the question of the reading.
**＋** The cascade of 104.2: the two children go `archived`; a new lesson reopens the Insight.
**－** The probe file is a hand-written harness file without a Rule page; the exception is ratified here explicitly: it lives one task, is removed before Retro, and never enters a commit.
**－** The outcome of the reading is not ratified in advance: the Rule page gets a sentence that holds under any outcome; the outcome goes into the estimate line.

## Criterion

- [[estimate-render-harness-reproduces]] § case 139.1

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#case-139.1
