---
type: decision
case: "1001"
status: current
update: ["[[rule-morph]]", "[[entity-sprint-plugin]]", "[[estimate-clean-branch-refuses-a-draft-core-page]]", "[[rule-permissions]]", "[[rule-guppi-config]]"]
origin: raw/2026-11-02/0254/ledger.md#case-1001
sprint: plugin
created: 2026-11-02
tags: [session, harness, plugin, sprint, workflow, ci, render]
---

## Problem

The clean build writes nothing while `rule-morph`, a page of a later milestone, stands `draft` with `core: true`, so the current milestone cannot close before work of a later one is done.

## Recommend

- **How rule-morph stops blocking the build**
  - Recommended: (a) rule-morph ships only once it is built: `core` comes off it, and its item in the milestone The plugin says that the Case that builds it gives `core` back.
  - Answer: agreed, (a).
- **What happens to rule-skill-approve-spec**
  - Recommended: (a) it keeps core, and the CLI trial clears it.
  - Answer: agreed, (a); the trial can be made in this session.
- **How the change is checked**
  - Recommended: (b) rewrite the line of `estimate-clean-branch-refuses-a-draft-core-page` that lists the pages without core, so that it names `rule-morph` too.
  - Answer: (b); close the Case now.
- **Change**
  - Asked: at `/pre-spec`, the line of the milestone item of `entity-sprint-plugin` names `rule-morph` in place of an unclear "it"; the `context` is set right on which pages carry `core` and on the ledger; and the Case also rewords the Purposes of `rule-permissions` and `rule-guppi-config` to say the setup Case of a project in place of `rule-morph`, `estimate-clean-branch-ships-neutral-texts` named as still holding.
  - Taken: the pair of `entity-sprint-plugin` names `rule-morph`; the `context` is fixed; the Case updates `rule-permissions` and `rule-guppi-config` with those pairs and names that Estimate in `context`.

## History

- 2026-11-02 created · raw/2026-11-02/0254/ledger.md#case-1001
