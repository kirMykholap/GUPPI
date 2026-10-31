---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when its Case adds a member to a list that texts spell out one by one, searches for a member already in the list and enters each text that would miss the new member in the Case, or names it in context
method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on a new member of a list and whose plan holds a Case that adds a member to a list: .claude/agents/case-guppi.md read against the Criterion, and the findings of ask-guppi at that /pre-spec read for a Case that adds a member to a list and misses a text that lists the members, both recorded in one estimate line with the count"
origin: raw/2026-10-30/2345/ledger.md#case-948.1
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that adds a member to a list that texts spell out one by one — a key of an item, a kind, a status or a field — and is about to answer with its summary.

Then:
It searches the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already.
**＋** It reads each hit that lists the members of the list.
**＋** Each text that lists the members and would miss the new member enters the Case, or the `context` of the Case names it and says why it stands.
**－** A hit in a History line, in `log.md` or in `brief.md` is not read.

## History

- 2026-10-31 created · [[decision-case-948.1]]
- 2026-10-31 updated: the Criterion written back unchanged; the method reads the live Render with the findings of the first /pre-spec whose plan holds a Case that adds a member to a list, in one estimate line, with no Retro part · [[decision-case-950.1]]
