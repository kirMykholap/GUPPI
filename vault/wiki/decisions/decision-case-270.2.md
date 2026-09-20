---
type: decision
case: "270.2"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-loaded]]", case-schema]
origin: raw/2026-09-20/1308/ledger.md#case-270.2
sprint: migration
created: 2026-09-20
tags: [session, workflow, ledger]
---

## Context

Today `generate`, once it applied a `create`, `update`, `delete` or `defer` entry of `materialize.yaml`, ticks the page line of the Spec of the same session, in the section of the entry's Case (case 226.1). An `estimate` entry — the reading of an Estimate — ticks nothing: the Criterion of `estimate-generate-ticks-the-spec` says the `read` lines are the agent's. The agent writes the `estimate[...]` line into the ledger and must tick the `read` line of `spec.md` in the same reply; two actions of one event, and the second one is forgotten — three lines of the Specs 0958 and 0740 stand unticked with their readings `passed`. The librarian sees it and cannot repair it: the librarian writes only to `wiki/`. An `estimate` entry of the yaml carries no Case number, and a reading often lands in the Spec of another session (line 172 of session 0740 was read in 0958; the readings W1–W3 of this session are lines of the Spec 0958); a reading of the same session as the `create` folds into the `create` entry (`folded`).
State of the pages: `rule-page-generation` `built`, `estimate-generate-ticks-the-spec` `passed`, its Criterion excludes `estimate`; `rule-case-protocol` `built`, `estimate-case-protocol-loaded` `passed` and names the sentence "Work Mode ticks … readings" in its Then, the same sentence stands in `case-schema.md`; `rule-retro` `built`, `estimate-retro-loads` `passed` and counts every unticked `read` line as debt; `rule-work-mode` `draft` (Slice 3b) untouched; the other six Estimates of `rule-page-generation` untouched; every `update` carries a `ref`, no vault query due.

## Problem

The ledger line and the tick in the Spec are one event held by two agents: one has no right to write into the Spec, the other forgets. Who ticks the `read` line, and what the protocol and Retro say about Work Mode then.

## History

- 2026-09-20 created · raw/2026-09-20/1308/ledger.md#case-270.2
