---
type: decision
case: "286"
status: archived
update: ["[[rule-page-generation]]", "[[estimate-generate-ticks-the-spec]]"]
origin: raw/2026-09-21/0019/ledger.md#case-286
sprint: migration
created: 2026-09-21
tags: [harness, workflow, ledger]
---

## Context

`generate`, once it applied an `estimate` entry of the yaml, ticks the first unticked line `- [ ] read `<slug>`` — in the Spec beside the yaml first, then in the Specs of the other sessions of `raw/`, oldest first. In the Spec beside the yaml it skips the sections of the Cases ratified after the reading (280); in the other Specs it skips nothing and looks at no Case. When a Case is superseded by another (`{supersedes:case N}`), its yaml entries are marked `superseded_by`: `generate` neither applies them nor ticks their page lines (151, 200.2), and Retro does not count their lines (282). But the `read` line of such a Case is an ordinary line to `tick_read`: in the run of 2106 the reading of `estimate-case-protocol-loaded` landed on 1749:39 (Case 278, superseded by 279.1) and 1749:88 (279.1) stayed open. The Estimate page is right — `passed` on the Criterion of 279.1; the Spec says the opposite: a Criterion that is not there was read, and the signed one was not. The 1749 Spec is in the archive now, `generate` does not read it, and line 88 stays `[ ]` for good. The brief also names 1749:38 as ticked by the librarian of 1749 — in the file it is `[ ]`, as it should be for a superseded Case.
`rule-page-generation` `draft` (`estimate-generate-rewords` pending); of the eight Estimates of the rule one is touched — `estimate-generate-ticks-the-spec` (`passed` 2106), the other seven not; an `update` with a `ref`, no vault query due.

## Problem

A reading closes the line of a Case whose work stands under another Case. The record in the Spec is wrong, and the line of the superseding Case never closes. Either this is contract — and `tick_read` skips the sections of superseded Cases by the marks of the yaml — or a fact for the reading of the Estimate, and the record stays wrong.

## History

- 2026-09-21 created · raw/2026-09-21/0019/ledger.md#case-286
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
