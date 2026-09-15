---
type: decision
case: "180"
status: current
update: ["[[rule-retro-commit]]"]
origin: raw/2026-09-15/2225/ledger.md#case-180
sprint: migration
created: 2026-09-15
tags: [session, workflow, hooks, harness, git]
---

## Context

`rule-retro-commit` is the hook `guppi gate`. It runs on `PreToolUse` for the agent's `Skill` call and on `UserPromptSubmit` for the person's typed `/pre-task`, `/retro` and `/handoff`. It has two refusals: a `then` item of the Spec without its ledger line (case 122), and a dirty tree for `/handoff`. It looks for the Spec in `spec.md` of the session's folder and in the plan file the event log named last. No `hi`, no Spec, no plan file: nothing to check, exit 0, the mark is written.

## Problem

Retro is the analysis of what the session did: Cases, readings, lessons. A session with no Spec and no ledger line did nothing, and its Retro is empty — as at 22:34 today. The gate lets it through. Must the gate refuse, and on which condition?

## Given

`rule-retro-commit` is `draft`; `estimate-retro-commit-gates` was `pending` on block 169.1, read `passed` at 22:34 (a line of this session's ledger).
**＋** `guppi/gate.py`: `spec_check` returns an empty list without `hi`, without `spec.md` and without a plan file; `run` then goes on to the tree check and the mark.
**＋** `session_decisions(window_lines(...))` reads the lines of the session's ledger window; `window_lines` returns every line of the window, not only `decision`.
**＋** `tests/test_gate.py`: piped payloads against a temp repository; 6 tests on the head block, the tests of 169.1 on the typed path.
**＋** An `estimate[...]` line is written the moment the measurement exists, in Plan Mode too (`rule-ledger-write`): a session of readings has a ledger line before `/retro`.
**－** `/handoff` and `/pre-task` are not changed by this Case; their contract stays.

## Criterion

- [[estimate-retro-commit-gates]] § case 180

## History

- 2026-09-16 created · raw/2026-09-15/2225/ledger.md#case-180
