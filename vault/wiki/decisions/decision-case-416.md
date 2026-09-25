---
type: decision
case: "416"
status: current
defer: ["[[rule-frame-check]]", "[[rule-case-protocol]]", "[[rule-spec-write]]", "[[rule-spec-reconcile]]", "[[rule-ask]]"]
supersedes: ["[[decision-case-408]]"]
origin: raw/2026-09-25/0051/ledger.md#case-416
sprint: migration
created: 2026-09-25
tags: [session, workflow, harness, ledger, hooks]
---

## Context

Today the main agent reads the pages of a Case, then `frame-guppi` reads the same frame again, and the main agent writes the Case into the chat; the agent also edits the plan to translate it. In this session the person proposed a new scheme: the main agent reads only the Frontier item and its source and decides — answer itself, discuss a fork, or dispatch; a Case is always built by one subagent, `case-guppi` (the renamed `frame-guppi`, on Opus with effort medium), which asks the vault, reads the frame and writes the Case; a `SubagentStop` hook checks it by the checks of `prespec --check` and sends it back on a finding; a hook shows the checked Case to the person by `systemMessage`; a question or a change goes to the same `case-guppi` by `SendMessage`; `ratified` writes the Case the person saw; a guard refuses every edit of the plan by the agent while a line under `## Cases` of the Frontier is open, the defers written by the hook too, and the translation comes after; `ask-guppi` answers at pre-spec only; the orchestration of the main agent becomes a rule of its own, loaded by `/hi`, and `case-schema.md` goes to `case-guppi`. Measured in this session from the transcript: the answer of a subagent in the main transcript is wrapped and indented by the harness, its raw text stands in `subagents/agent-<id>.jsonl`; the reply to `SendMessage` comes as a `task-notification`; a `SendMessage` after a pause re-cached the agent's whole context. Not yet measured: how a long `systemMessage` renders, the live payload of `SubagentStop`, and whether a `systemMessage` stands in the transcript — the live probe of this session's Work Mode, reported in the handoff. The question of Case 408 — whether `frame-guppi` pays — is taken into this one.

## Problem

How a Case is built, checked, shown and written under the new scheme: decided in the next session, with the results of the live probe.

## Deferred

### [[rule-frame-check]]

frame-guppi becomes case-guppi, which builds the Case from the Frontier item and the person's choices — the vault query, the frame, the form — on Opus with effort medium, and is asked again by SendMessage; whether it pays, measured by its dispatches (the question of case 408)

### [[rule-case-protocol]]

case-schema.md read by case-guppi only; the orchestration of the main agent — the triage of a Frontier item, the dispatch, the acknowledging reply, LEDGER, defers and the one rule — a rule of its own loaded by /hi

### [[rule-spec-write]]

The Case checked on SubagentStop and shown by a hook from the answer of case-guppi; ratified writes the Case the person saw, and writes the defers too

### [[rule-spec-reconcile]]

The plan written by hooks alone — a guard refuses the agent's edits while a line under Cases of the Frontier is open; when and how the prose of a Case is translated (the question of case 410)

### [[rule-ask]]

ask-guppi answers at pre-spec only; the vault query before a create moves to case-guppi

## History

- 2026-09-25 created · raw/2026-09-25/0051/ledger.md#case-416
