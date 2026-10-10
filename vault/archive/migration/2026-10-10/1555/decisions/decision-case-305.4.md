---
type: decision
case: "305.4"
status: archived
update: ["[[rule-sprint]]"]
origin: raw/2026-09-22/0014/ledger.md#case-305.4
sprint: migration
created: 2026-09-22
tags: [session, workflow, harness, librarian, sprint]
---

## Context

The audit over the 47 pages of `wiki/rules/` — kind, parent, purpose, taken by grep, no page opened. 38 rules carry a parent: each is a step of the sequence of its phase (`rule-session-start`, `rule-plan-mode`, `rule-end-of-work`, `rule-documentation`; the order of `children` is content) or a tool under `rule-harness` (`rule-lint`, `rule-render-harness`, `rule-governed-files-hook`, `rule-bash-guard`, `rule-tests-clock-pinned`, the MOCs `rule-settings` and `rule-claude-md`). All stand: none is a condition on the pages of one category — `rule-synthesis` is about Insights, but it is a step of Documentation, and a page has one `parent`. The rules that hold for one category alone are the six schemas, one per category; no category has two, no category MOC is made, the schemas stay under `rule-page-schemas`. The five roots are the four phases and the harness: no root MOC over them — it would hold no cross-cutting promise of its own (the order of the phases is held by the hooks of each: the ledger hook without `/hi`, the prespec hook, the retro commit), and a MOC without an Estimate is against the rule. The four placeholders (`rule-work-mode`, `rule-subagent-guppi`, `rule-spec-box`, `rule-morph`) get a parent when they are taken up.
The edge Rule → Entity. By case 240.2 an Entity is what is measured and has no guard of its own; its guard is a separate Rule. Today `rule-sprint` names `entity-sprint` in a code span; there is no edge. The precedents of the mechanism: `children` on an Entity is written by the script from the `parent` of the child; `severity` of an Insight is `computed`, recomputed by the cascade of `generate`. Two hand-written fields for one edge are two records of one fact, and they drift; so one side is written — `applies_to` on the Rule, in the Case — and `rules` on the Entity is the backlink the cascade of `generate` recomputes, as `severity`; lint checks the slugs and the agreement of the pair. `applies_to` names an Entity only: a rule constrains a case — a page, a session, a file — not another rule, and what a rule reads or guards among the rules is derived from `implementation_ref` and `governs`, never written (the person's decision of this session).
The pages: `rule-rules-schema` and `rule-entities-schema` were ratified in this session (304.2, 304.3) and do not exist yet — the field goes into their Render, so 305.1 supersedes 304.2 and 305.2 supersedes 304.3 (299.1): the pages are born in the right shape, and the live legs of `estimate-prespec-catches-a-superseded-case` and `estimate-materialize-marks-superseded` are taken by it. `rule-page-generation` `draft`, `rule-sprint` `built`, `entity-sprint` `draft` (MOC, `estimates: []`), `rule-lint` `built`. The Estimates: `estimate-rules-schema-checked` and `estimate-entities-schema-checked` are created anew by the superseding Cases with the field in their Criterion; `estimate-lint-catches` gets a second `replace` pair of the session, on its `ref` line; `estimate-generate-writes-rules-from-applies-to` is new, on `rule-page-generation`; `estimate-generate-rewords` and the other Estimates of `rule-page-generation` are not touched; `rule-sprint` gets a field alone, its Estimates are not touched (296). In `materialize` the filter by the schema stands on a `create` and a `defer`, not on the `set` of an `update`, so `set: {applies_to: …}` passes; in the librarian's run `render` comes after `generate`, so lint reads the new yaml. The slugs are free. Case 305.2 was superseded by 306.1 before the approval and left the Spec (299.1).

## Problem

Where every rule stands and whether a category MOC or a root is needed; how the edge Rule → Entity enters the schemas, who writes which side of it and who checks it; and how the field reaches the two Renders ratified an hour before.

## History

- 2026-09-22 created · raw/2026-09-22/0014/ledger.md#case-305.4
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
