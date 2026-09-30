---
type: decision
case: "543"
status: current
children: ["[[decision-case-543.1]]", "[[decision-case-543.2]]", "[[decision-case-543.3]]", "[[decision-case-543.4]]"]
origin: raw/2026-09-30/1306/ledger.md#case-543
sprint: migration
created: 2026-09-30
tags: [harness, workflow, session, ledger]
---

## Problem

A round of `case-guppi` can end with a list of files, because a general instruction of Claude Code asks for one and the frame does not set it aside. The grill-me template shows the `**Options:**` label four spaces too deep, so each round shows it as code. The writer made that indent: the leading spaces of an `old` are never matched, and the leading spaces of a `new` are added after the ones on the page. Neither pre-spec nor the Case check catches a pair that doubles an indent.

## History

- 2026-09-30 created · raw/2026-09-30/1306/ledger.md#case-543
