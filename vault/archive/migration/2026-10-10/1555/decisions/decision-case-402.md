---
type: decision
case: "402"
status: archived
update: ["[[rule-spec-write]]", "[[rule-case-protocol]]", "[[estimate-spec-write-copies-the-ratified-case]]"]
supersedes: ["[[decision-case-394]]"]
origin: raw/2026-09-24/1916/ledger.md#case-402
sprint: migration
created: 2026-09-24
tags: [hooks, harness, workflow, session, ledger]
---

## Context

The hook of `rule-spec-write` reads the value of a sub-point with `code_value` in `guppi/ratified.py`, as CommonMark reads a code span. Case 393 set the rule: a value that opens or closes with a backtick takes its outer span padded by one space on each side, and a value that opens with a code span and ends in text, written without the spaces, is refused. A second shape remains: a value that opens and closes with a code span, written without the spaces — ``` ```a` and `b``` ``` — is read by CommonMark and by `code_value` alike as one span whose edge backticks are eaten, and the hook writes the value without them, silently. The text cannot tell this from a lawful span: CommonMark reads both the same. The one mechanical guard left is to require the padding whenever the value holds a backtick.

`rule-spec-write` stands `built`, deferred by Case 394; this Case takes the defer up. Its one Estimate, `estimate-spec-write-copies-the-ratified-case`, speaks of the form of a value, so its Criterion is replaced whole. The rule of the form also stands in the Render of `rule-case-protocol` (the Language paragraph); by Case 378.5 the edit of the Render does not touch `estimate-case-protocol-loaded`.

`frame-guppi` found one contradiction: the fixture `SHOWING` in `tests/test_ratified.py` carries `` old: ``the `old` text`` `` without the spaces; under the new rule it would be refused and three tests of the writer would fail. A task line for the fixture was added. No other user of `code_value` stands in `guppi/`. In this session the agent itself wrote values holding backticks without the spaces, the `old` of Case 395 among them; after the change such values are refused.

## Problem

A value that opens and closes with a code span, written without the spaces, enters the Spec with its edge backticks lost, and nothing says so. Should the hook refuse a span whose content holds a backtick when the outer span is not padded?

## Given

`rule-spec-write` — the hook that writes a ratified Case into the plan file; its `How it works`.
**＋** `guppi/ratified.py` — `code_value` and `read_tasks`, the reading of a sub-point value.
**＋** `guppi/gate.py` — `plan_path`, the plan file of the session.
**＋** `.claude/settings.json` — the `Stop` hook `uv run guppi ratified`.
**＋** `tests/test_ratified.py` — fixes the reading of a value and the fixture `SHOWING`.
**＋** `estimate-spec-write-copies-the-ratified-case` — the promise of the hook; its Criterion names the form of a value.
**＋** `rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the form of a sub-point value in the Language paragraph.

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-402
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
