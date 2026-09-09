---
title: "No rule is written against a copy of a schema's `values:` list, and the drift is left to the gate"
type: decision
status: archived
authority: schema-values-copy-rule
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "job_hunt_ai_vault/wiki/proposals/_schema.yaml"]
tags: [vault, record-schema, testing]
---

# The ruling, 2026-08-26

*(the owner selected it, against writing the rule.)*

**A rule forbidding a second copy of a folder's `values:` list is not written.** The item is closed
rather than deferred.

**The drift is already caught by the gate.** A page carrying a value outside its folder's list goes
red, so a copy that has drifted from the schema shows up the first time somebody uses the value it
claims is legal ([[the-legal-value-list-lives-in-each-folders-schema]],
[[a-fields-legal-values-live-beside-its-legal-keys]]).

**The uncovered direction costs one red run.** A copy that is *missing* a value the schema has is not
caught — the gate reads the schema, not the copy — so the first page written against the copy is
refused for a value that is in fact legal. That is one confusing run and a lookup, paid once.

# Rejected

**Rejected: the rule.** Its price is permanent — every reader of the schema carries one more
prohibition — against a failure worth one red run. **The general shape is that a copy of a list is
what drifts and a sweep is what cannot** ([[a-copied-list-drifts-and-a-sweep-cannot]]); here the
sweep already exists and is the gate, so a rule about the copy adds a reader's obligation and no
detector.
