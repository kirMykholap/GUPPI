---
type: decision
case: "187"
status: current
create: ["[[estimate-plan-mode-names-its-estimates]]"]
update: ["[[rule-plan-mode]]"]
origin: raw/2026-09-16/1034/ledger.md#case-187
sprint: migration
created: 2026-09-16
tags: [session, workflow]
---

## Context

`rule-plan-mode` is the MOC of Plan Mode, with `rule-ask`, `rule-pretask-hook`,
`rule-pretask` and `rule-spec-capture` as its children. It carries one Estimate,
`estimate-plan-mode-verified`, whose promise is another action: the vault query before a
`create` and the firing of the pre-task hook. Today the script decides which Estimate a
ratified Case changes: `materialize` reads `contract: changed` from the `then` block and
appends a block to the rule's Estimate, setting it `pending`. Case 182 deferred this page
together with the whole Estimate model; this Case takes point 8 of that model. The vault
was asked: no live rule and no Estimate carries this promise.

## Problem

The script decides which promise changed, from a flag that says only "something changed".
Three failures follow. A Case that edits the rule's `Purpose` — prose no promise depends
on — raises the same flag and sends an Estimate to `pending` for nothing. A Case that
changes two promises of one page can mark only one. And a Case that changed no promise but
raised the flag sends back for re-reading something nobody touched. The judgment of which
promise is touched belongs to the person who signs the Case, not to the parsing of a
`then` block.

## Given

`materialize.py:583` derives the Estimate update from `item.get("contract") == "changed"`;
`contract` sits in `DERIVED_KEYS`, so it never reaches a page field.
**＋** `estimate-plan-mode-verified` is QA, `passed`, Method `make test-plan-mode`, its
Criterion the two verification points of Plan Mode — another action.
**＋** the slug `estimate-plan-mode-names-its-estimates` is free: no live page and no hit
in the archive.
**＋** the tags `session` and `workflow` are already on `rule-plan-mode`; `harness` does not
apply, the scripts are Cases 189 and 190.
**＋** `rule-materialize` holds today's opposite and is deferred by the same case 182.
**＋** the librarian runs `materialize` and `generate` once, at the close of the session,
with the new code; so the `then` blocks of this Spec from Case 187 on are written in the
new form, and the blocks of Case 186 are rewritten by a Work Mode task.
**－** `{supersedes:case 182}` is not written on this Case: one such mark clears
`deferred_by` from all five targets of 182 at once. It goes on the last Case of the group.

## History

- 2026-09-16 created · raw/2026-09-16/1034/ledger.md#case-187
