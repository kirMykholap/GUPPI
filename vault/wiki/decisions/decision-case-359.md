---
type: decision
case: "359"
status: current
update: ["[[rule-agent-writing]]", "[[estimate-agent-writing-followed]]", "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"]
origin: raw/2026-09-23/0034/ledger.md#case-359
sprint: migration
created: 2026-09-23
tags: [harness, render, workflow, ledger, session, tests]
---

## Context

Two lessons share one mechanism: a fact signed on a check narrower than the claim. The reading line of `estimate-prespec-checks-the-plan` said "72 green in the file" after one combined pytest run over three files, the per-file number split from memory; `pytest tests/test_prespec.py` alone gives 52. Case 348 was ratified on the claim that every ledger line stands in `materialize.yaml`; what was checked was the shape of the entries the agent looked at, while the yaml covers lines 1–51, 58 and 60 of 64. In both, the question put to the tool was about a sample or a shape, and the sentence signed was about a whole. Today `rule-agent-writing` asks only "Name a real source or remove the claim" — the source is named, the width of the claim is not checked.
The Insight stands `open`, severity 2, two children; the rule stands `built`, its one Estimate `estimate-agent-writing-followed` `passed`, and it is touched.

## Problem

The rule asks a claim for a source and not for a source as wide as the claim, so a narrow check signs a wide sentence.

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#case-359
