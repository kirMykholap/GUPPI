---
type: estimate
kind: QA
status: passed
target: "[[rule-plan-mode]]"
origin: raw/2026-09-16/1034/ledger.md#case-187
sprint: migration
created: 2026-09-16
tags: [session, workflow]
ref: rule-plan-mode
purpose: A ratified Case names by slug the Estimate it changes
method: live reading of this session's Spec at its close — every Case that changes a rule names the Estimate it changes by slug, and a Case that changes only the Purpose section names none
---

## Criterion

Given:
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

When:
A Case that changes a rule page is ratified.

Then:
The Case names by slug the Estimate it changes, in its `then` block.
**＋** only a replaced Criterion sets an Estimate `pending`.
**＋** an `update` of the rule's `Purpose` section touches no Estimate.
**＋** an `update` of the rule's `Render` section touches the Estimate of the live reading
of that Render.
**－** the `contract` flag decides nothing: no Estimate is derived from it.
**－** the hole is named, not closed: code in Work Mode can touch a promise the Case did
not name, and only that promise's own test catches it.

## Result

2026-09-16, the live reading of this session's Spec, raw/2026-09-16/1651/spec.md, Cases 193–200: every Case that replaced a Criterion named the Estimate by slug in its then block — 194.1 estimate-materialize-assembles, 194.2 -walks-dates, 196.1 estimate-carry-over-writes, 196.2 estimate-end-of-work-order, 197 estimate-brief-written, 200.5 estimate-permissions — and the Cases that changed a Render or a Purpose without replacing a promise named the touched Estimate in context and none in the block: 195/200.1 (estimate-case-protocol-loaded, pending by 188), 196.3 and 200.3 (estimate-brief-written, replaced by 197), 198 (estimate-pretask-reconciles, its recut deferred by 191), 196.2 and 194.1 Purpose updates touched none beyond the one they replaced; 193, 199, 200.2 changed Rule-class files and named none

## History

- 2026-09-16 created · [[decision-case-187]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L39
