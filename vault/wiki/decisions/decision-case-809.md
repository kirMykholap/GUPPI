---
type: decision
case: "809"
status: current
create: ["[[estimate-clean-branch-pages-hold-pointers-only-in-brackets]]"]
update: ["[[entity-glossary]]", "[[entity-sprint]]", "[[rule-agent-writing]]", "[[rule-backlog]]", "[[rule-brief]]", "[[rule-carry-over]]", "[[rule-case-build]]", "[[rule-case-check]]", "[[rule-case-example]]", "[[rule-case-protocol]]", "[[rule-claude-md]]", "[[rule-cleanup]]", "[[rule-decisions-schema]]", "[[rule-documentation]]", "[[rule-end-of-work]]", "[[rule-entities-schema]]", "[[rule-estimates-schema]]", "[[rule-event-log]]", "[[rule-git-context]]", "[[rule-insights-schema]]", "[[rule-internal-context]]", "[[rule-language]]", "[[rule-ledger-tail]]", "[[rule-ledger-write]]", "[[rule-lessons-schema]]", "[[rule-materialize]]", "[[rule-orchestration]]", "[[rule-page-generation]]", "[[rule-page-read]]", "[[rule-page-schemas]]", "[[rule-permissions]]", "[[rule-prespec-hook]]", "[[rule-raw-archive]]", "[[rule-render-harness]]", "[[rule-retro]]", "[[rule-retro-commit]]", "[[rule-retro-onward]]", "[[rule-rules-schema]]", "[[rule-search-leaves-out-decisions]]", "[[rule-skill-grill-me]]", "[[rule-skill-hi]]", "[[rule-skill-sprint-close]]", "[[rule-skill-sprint-open]]", "[[rule-spec-capture]]", "[[rule-spec-reconcile]]", "[[rule-spec-write]]", "[[rule-sprint]]", "[[rule-synthesis]]", "[[rule-work-mode]]", "[[entity-sprint-plugin]]"]
origin: raw/2026-10-14/0101/ledger.md#case-809
sprint: plugin
created: 2026-10-14
tags: [ci, plugin, session, harness, sprint, workflow, render, librarian, hooks, ledger, schema, git]
---

## Problem

The pages that ship hold pointers outside a bracket, so `guppi ship` exits 1 and the CI run writes no clean branch, and some brackets that `guppi ship` removes hold a definition or the slug of a shipped rule that the sentence needs.

## Recommend

- **How a sentence with a pointer outside a bracket is rewritten**
  - Recommended: (a) the pointer and its history words go into one bracket at the end of the sentence.
  - Answer: agreed, (a).
- **Which brackets with words change**
  - Recommended: (a) fix the brackets that carry a definition, and move the slug of a shipped page out of its bracket.
  - Answer: agreed, (a).
- **Whether the code of `guppi ship` changes too**
  - Recommended: (a) pages only; the code stays as it is.
  - Answer: agreed, (a).
- **When the CI run takes place**
  - Recommended: (a) after the librarian's run, in a later session of the sprint.
  - Answer: agreed, (a).
- **How the rewording is checked**
  - Recommended: (a) one new Estimate on `rule-clean-branch` for the pages.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, the Frontier closes the sprint item with this Case, so the person was asked whether this Case updates `entity-sprint-plugin` so that the line of the milestone The clean branch says what remains, or the item is put off instead; the person agreed to the update. The findings of `/pre-spec` also asked that `context` name `estimate-glossary-terms-defined` and `estimate-decisions-schema-checked` and say that both Criteria hold, and that it correct what it said of Case 808 and `rule-clean-branch`.
  - Taken: an `update` of `entity-sprint-plugin` rewrites the milestone line with what remains; `context` names the two Estimates and why their Criteria stand, and says that Case 808 and this Case both write to `rule-clean-branch`, on no common sentence.

## History

- 2026-10-14 created · raw/2026-10-14/0101/ledger.md#case-809
