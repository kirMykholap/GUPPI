---
type: decision
case: "349"
status: current
update: ["[[rule-documentation]]", "[[estimate-documentation-completes]]"]
supersedes: ["[[decision-case-348]]"]
origin: raw/2026-09-22/2046/ledger.md#case-349
sprint: migration
created: 2026-09-22
tags: [session, workflow, harness, librarian, render]
---

## Context

Case 348 wrote into the ban of the librarian's frame that every ledger line already stands in `materialize.yaml` with its `line`, `text` and `origin`, so the file is never needed. That is false. The ledger of session 0014 holds 64 lines; the yaml's entries cover 1–51, 58 and 60, and `unparsed` is empty. Lines 52–57, 59 and 61–64 have no entry: they are `estimate[...]` readings that folded into entries the run skipped. So the librarian went to the file not because the frame invited it but because the fact was nowhere else — "a ledger line this run did not apply" is the one fact the yaml lacks. A second inaccuracy: the entries the librarian appends at the synthesis carry no `line`, `text` or `origin`, and the frame reads those too.
`rule-documentation` stands `draft`, a MOC; `estimate-documentation-completes` stands `failed` on this very reading. The gap in `materialize` is recorded as a lesson of this session and is not repaired here.

## Problem

The ban sends the librarian to a place that does not answer the question the brief asks, which makes breaching the frame the only way to obey it.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#case-349
