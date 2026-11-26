---
type: decision
case: "1070"
status: current
children: ["[[decision-case-1070.1]]", "[[decision-case-1070.2]]", "[[decision-case-1070.3]]", "[[decision-case-1070.4]]", "[[decision-case-1070.5]]", "[[decision-case-1070.6]]", "[[decision-case-1070.7]]"]
origin: raw/2026-11-26/1515/ledger.md#case-1070
sprint: plugin
created: 2026-11-26
tags: [harness, render, git, sprint, plugin, session, workflow, librarian, ledger]
---

## Problem

A project whose main branch is not `main` cannot keep GUPPI's rules on branches: the skills open pull requests into a branch that does not exist, and Work Mode and `/box` run on the shared branch. No setting holds the name, and the setup Case does not ask for one.

## Recommend

- **Where the name is kept and how the texts read it**
  - Recommended: (a) a setting `main_branch` in `guppi.toml`, `main` in the copy that ships; the render puts its value where a Render writes `{{main_branch}}`, and the code reads it by one function of the settings module, `main` when the file or the setting is missing.
  - Answer: agreed, (a).
- **How the setup finds the name**
  - Recommended: (a) proposed from the branch that `/hi` printed under `Branch:`, shown for the person to correct, with no question.
  - Answer: agreed, (a).
- **Which texts take the name in place of `main`**
  - Recommended: (a) only the texts that ship; `/merge-main`, `/pr-review` and the other pages of the repository of GUPPI keep `main`.
  - Answer: agreed, (a).
- **Change**
  - Asked: on the findings of `/pre-spec`, the person chose that `/sprint-open` and `/work`, in the session of the setup Case, take the name of the main branch from the ratified setup Case and not from the placeholder, the name going into the prompt of the opening Case as the branch of `Branch:` does; the other findings asked that `/setup` write that branch into its prompt and render each file that names the main branch, that the Criterion of the setup Estimate read only text, and that the `method` of the Estimate of `/work` name the main branch in words.
  - Taken: Cases 1070.4 and 1070.7 take the name from the setup Case and read that run; Case 1070.3 writes the branch into the prompt, renders those files and reads only the texts of the setup; Case 1070.6 gives that `method` words and no transcript.

## History

- 2026-11-26 created · raw/2026-11-26/1515/ledger.md#case-1070
