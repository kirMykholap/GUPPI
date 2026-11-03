---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from entering the Spec in other words than the Case case-guppi wrote into its file, whose given, when, then, tasks and ratification the person signed and the check of rule-case-check stored
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/ratified.py, .guppi/tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-write-copies-the-ratified-case]]", "[[estimate-spec-write-checks-the-written-case]]", "[[estimate-spec-write-writes-a-defer]]", "[[estimate-spec-write-reaches-the-approved-spec]]", "[[estimate-spec-write-removes-a-superseded-case]]", "[[estimate-spec-write-exits-2-on-an-error]]", "[[estimate-spec-write-answers-a-refusal]]", "[[estimate-spec-write-refuses-a-changed-case-file]]", "[[estimate-spec-write-tells-each-reason-once]]", "[[estimate-spec-write-reads-a-new-tag]]", "[[estimate-spec-write-copies-a-built-defer-only-case]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow, session]
core: true
---

## Purpose

Prevents a ratified Case from entering the Spec in other words than the Case `case-guppi` wrote into its file, whose `given`, `when`, `then`, `tasks` and `ratification` the person signed and the check of `rule-case-check` stored. `case-guppi` writes the whole Case in the documentation language, and a hook copies its stored answer.

## History

- 2026-11-03 shipped with GUPPI
