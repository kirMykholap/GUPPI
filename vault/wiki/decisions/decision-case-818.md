---
type: decision
case: "818"
status: current
children: ["[[decision-case-818.1]]", "[[decision-case-818.2]]"]
origin: raw/2026-10-15/0553/ledger.md#case-818
sprint: plugin
created: 2026-10-15
tags: [harness, plugin, render, ci, git, sprint]
---

## Problem

An install of the plugin `guppi` gives a project no skill to run and no file of GUPPI, so GUPPI cannot be installed into a new project.

## Recommend

- **What `/guppi:install` puts into the project**
  - Recommended: (a) copy the ready files from the plugin's own copy; the first `/hi` renders.
  - Answer: agreed, (a).
- **How far this Case reaches while two questions stay open**
  - Recommended: (a) copy everything but the plugin's own files for now; a later Case narrows the set.
  - Answer: agreed, (a).
- **A project that is not empty**
  - Recommended: (a) list the files that already stand, write nothing and stop.
  - Answer: agreed, (a).
- **Skill names**
  - Recommended: (a) bare names in every project; only the plugin's skill is `/guppi:install`.
  - Answer: agreed, (a).
- **Which page governs the install skill**
  - Recommended: (a) a new rule `rule-plugin-install` with no `core: true`, whose Render `guppi ship` copies to `skills/install/SKILL.md`.
  - Answer: agreed, (a).
- **What checks that this is done**
  - Recommended: (a) a new Estimate on the install, and the Criterion of the sprint Estimate replaced.
  - Answer: agreed, (a).
- **Change**
  - Asked: build the Case again to agree with Case 819, which moves GUPPI's code, its `pyproject.toml` and its `uv.lock` into `.guppi/` and adds the `uv` steps to the install.
  - Taken: the install copies the code under `.guppi/` and no `pyproject.toml` at the root, so a file under `.guppi/` that already stands stops it and a project's own `pyproject.toml` does not. The first text of `rule-plugin-install` names `.guppi/`, and `uv` and the Python environment are left to Case 819.4.
- **Change**
  - Asked: build the Case again to agree with Case 821, which stops `guppi ship` while a page with `core: true` is `draft` and adds `--allow-draft` for a local copy.
  - Taken: the sprint Estimate of Case 818.2 reads an install from a local copy that `guppi ship --allow-draft` writes, added by `/plugin marketplace add` and installed by `/plugin install guppi@guppi-marketplace`, before the close. The `method` of the Estimate of Case 818.1 waits for the first run that writes `prod`.
- **Change**
  - Asked: at `/pre-spec`, read every Estimate that waited for a run that writes `prod` from a local copy that `guppi ship --allow-draft` writes, since a run that writes `prod` has already happened and the word first in a `method` stands only for an event that never happened.
  - Taken: the `when` of Case 818.1 and the `method` of its Estimate read the install from that local copy, by the same commands as Case 818.2, with no run of `.github/workflows/prod.yml` and no word first.

## History

- 2026-10-15 created · raw/2026-10-15/0553/ledger.md#case-818
