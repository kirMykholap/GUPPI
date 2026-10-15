---
type: decision
case: "817"
status: current
update: ["[[rule-morph]]", "[[estimate-morph-sets-up-the-project-at-the-first-hi]]", "[[entity-sprint-plugin]]"]
origin: raw/2026-10-15/0553/ledger.md#case-817
sprint: plugin
created: 2026-10-15
tags: [session, harness, plugin, sprint, workflow]
---

## Problem

Under the installer model, `/guppi:install` writes the settings of this repository into the project before any `/hi`. So `rule-morph` has no test of a project that is not set up yet, and its rule that no settings file changes outside the install Case is false.

## Recommend

- **Where the person gives the settings of a new project**
  - Recommended: (a) the install Case at the first `/hi`, after the bootstrap of `/guppi:install`.
  - Answer: agreed, (a).
- **How much of the install step this session builds**
  - Recommended: (a) this session changes the page and its Estimate only; a later session builds the skill and the check in `/hi`.
  - Answer: agreed, (a).
- **How `/hi` tells that the project has not been set up yet**
  - Recommended: (a) `/hi` compares the transcripts folder that the read rules name with the one the project's path gives.
  - Answer: (b) a new key in `guppi.toml` that the install Case sets and the clean version holds unset.
- **What checks that this is done**
  - Recommended: (a) replace the Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi` whole.
  - Answer: agreed, (a).
- **Change**
  - Asked: at the pre-spec, name the description of the project and the keys `test` and `style` among the values of the install Case, and `CLAUDE.md` among the files it renders; keep the milestone line of `rule-morph` on `entity-sprint-plugin` open with what remains; fix the sentence of `context` on what the copy holds.
  - Taken: the new text of `rule-morph`, the new Criterion and `context` name them, and an `update` of `entity-sprint-plugin` rewords its milestone line.

## History

- 2026-10-15 created · raw/2026-10-15/0553/ledger.md#case-817
