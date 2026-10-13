---
type: decision
case: "793"
status: current
defer: ["[[rule-page-generation]]"]
origin: raw/2026-10-12/2349/ledger.md#case-793
sprint: plugin
created: 2026-10-12
tags: [harness, workflow, ledger]
---

## Context

In the loop after the findings of `/pre-spec`, the person put off Case 792 (Frontier item C8), a new form of a page `update` that removes a section. A Case of this session could not use such a form, since the check of a Case file runs the code that stands before Work Mode. Case 787.2 changes one sentence of `## How it works` of `rule-git-context` instead, and the section stays until a later Case drops it with that form.

## Problem

No form of a page `update` removes a section, so a Leaf cannot lose `## How it works` at its next touch without an edit by hand.

## Deferred

### [[rule-page-generation]]

An update of a page can remove a section, heading and text, so that a Leaf loses its How it works section at its next touch by guppi generate and not by hand; put off in the loop after the findings of /pre-spec

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#case-793
