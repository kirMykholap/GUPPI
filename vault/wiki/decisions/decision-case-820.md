---
type: decision
case: "820"
status: current
children: ["[[decision-case-820.1]]", "[[decision-case-820.2]]", "[[decision-case-820.3]]", "[[decision-case-820.4]]", "[[decision-case-820.5]]", "[[decision-case-820.6]]", "[[decision-case-820.7]]", "[[decision-case-820.8]]", "[[decision-case-820.9]]"]
origin: raw/2026-10-15/0553/ledger.md#case-820
sprint: plugin
created: 2026-10-15
tags: [harness, tests, plugin, ci, workflow, render, schema, git, sprint, github]
---

## Problem

GUPPI runs its tests, its style check and its vault checks through `make`, which a project that installs GUPPI may not have and cannot get from GUPPI's Python environment, and it gives every such project a command `ship` that only this repository can use.

## Recommend

- **What runs the vault checks in place of `make lint`**
  - Recommended: (a) a new command `guppi check` that runs the same steps in the same order, each one even after a red step, red if any is.
  - Answer: agreed, (a).
- **Whether `guppi check` judges GUPPI's clean version in every project**
  - Recommended: (b) only where the folder `plugin/` stands.
  - Answer: (c) the user does not get `ship`: the clean version holds no `guppi/ship.py`, the judgment of a pointer moves into a module that `/pre-spec` and `guppi ship` both import, the list of commands has no `ship` when its module is missing, and `guppi check` skips that step then.
- **What runs the tests in place of `make test`**
  - Recommended: (a) `guppi test` runs a command set in `guppi.toml`.
  - Answer: agreed, (a).
- **What runs the style check in place of `make style`**
  - Recommended: (a) `guppi style` runs a second command set in `guppi.toml`.
  - Answer: agreed, (a).
- **What a group rule's Estimate names in place of a make target**
  - Recommended: (a) the method lists the test files.
  - Answer: agreed, (a).
- **When the `Makefile` leaves this repository**
  - Recommended: (a) a thin `Makefile` stays here until a Case of a later session removes it, and the clean version stops writing it now.
  - Answer: agreed, (a).
- **How the pages and the harness take the new commands**
  - Recommended: (a) one `reword` per command, and real changes only where make itself is the promise.
  - Answer: agreed, (a).
- **When the group Estimates switch to the list of test files**
  - Recommended: (a) this Case teaches the checks the new form, and a Case of a later session moves the Estimates.
  - Answer: agreed, (a).
- **Whether a method may name `guppi test`, `guppi check` or `guppi style`**
  - Recommended: (a) the three new commands count as a form.
  - Answer: agreed, (a).
- **What `guppi test` and `guppi style` do where `guppi.toml` sets no command**
  - Recommended: (a) say so and exit non-zero.
  - Answer: agreed, (a).
- **The form of the two settings in `guppi.toml`**
  - Recommended: (a) two keys, `test` and `style`, each a list of commands run in order.
  - Answer: agreed, (a).
- **What checks that this is done**
  - Recommended: (a) new Estimates where nothing checks the change, and the replaced Criteria where one does.
  - Answer: agreed, (a).
- **What the thin `Makefile` runs for `test` and `style` until the next session**
  - Recommended: (a) `lint` calls `guppi check`; `test` and `style` keep their own commands.
  - Answer: agreed, (a).
- **The check of the `Makefile` under both shells**
  - Recommended: (a) replace its Criterion, naming the targets in words that the replace leaves alone.
  - Answer: agreed, (a).
- **Change**
  - Asked: by the findings of `/pre-spec`, the person chose that `rule-guppi-config` ships with the commands of the repository of GUPPI until the install Case of `rule-morph` sets a project's own, and that the wording, not the shipping, changes; the shipped texts hold in any project; the two new children of `rule-harness` join its list; one function judges whether the module of `ship` stands; and the line on the texts gets a reading after the librarian's run.
  - Taken: the Purpose of `rule-guppi-config` says that a new project runs the tests of GUPPI until the install Case sets its own; the sentence of `rule-harness` names the repository of GUPPI and the clean version; Case 820.9 adds both rules to the list of `rule-harness` and replaces the Criterion of `estimate-harness-pipeline`; `ship_stands` of `guppi/pages.py` serves `guppi check`, the list of commands and `guppi lint`; the methods of the Estimates of Cases 820.1 and 820.2 read the texts by hand after the librarian's run.

## History

- 2026-10-15 created · raw/2026-10-15/0553/ledger.md#case-820
