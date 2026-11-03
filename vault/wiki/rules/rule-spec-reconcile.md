---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/ratified.py, .guppi/guppi/ledger.py, .guppi/guppi/casecheck.py, .guppi/tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-reconcile-refuses-an-edit-of-the-plan]]", "[[estimate-spec-reconcile-refuses-a-case-file-another-agent-holds]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow, session]
core: true
---

## Purpose

Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again. The hooks alone write the Cases into the plan: the `Stop` hook of `rule-spec-write` writes the text of the file of `case-guppi` that `rule-case-check` stored, and a Case changes only through its `case-guppi` and a new ratification. The agent writes only the title line that creates the plan, and a hook refuses any other edit of it, and any edit of the file of a built Case that the person is sent, before it lands, unless `case-guppi` makes it and no other agent holds the number of that Case.

## History

- 2026-11-03 shipped with GUPPI
