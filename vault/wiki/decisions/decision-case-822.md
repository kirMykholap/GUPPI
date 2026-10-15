---
type: decision
case: "822"
status: current
children: ["[[decision-case-822.1]]", "[[decision-case-822.2]]", "[[decision-case-822.3]]", "[[decision-case-822.4]]", "[[decision-case-822.5]]", "[[decision-case-822.6]]", "[[decision-case-822.7]]", "[[decision-case-822.8]]", "[[decision-case-822.9]]"]
origin: raw/2026-10-15/0553/ledger.md#case-822
sprint: plugin
created: 2026-10-15
tags: [ci, plugin, tests, render, git, harness, schema, sprint, workflow, session, github]
---

## Problem

A project that installs GUPPI gets its rules without their Estimates, no tests, none of the files that its first `/hi` loads, no CI, and texts that describe GUPPI's own repository as its project, and nothing stops a build of `prod` that holds a rule that is not done.

## Recommend

- **How the copy knows that an Estimate ships**
  - Recommended: (a) judged from the target: `guppi ship` takes each Estimate whose target ships and writes `core: true` into its copy.
  - Answer: agreed, (a).
- **Which Estimates ship, by their status**
  - Recommended: (a) only those with a result, `passed` and `failed`.
  - Answer: only `passed` Estimates ship; a `failed` one may not ship, nor a `pending` one.
- **What a shipped Estimate says where it names a case or a session**
  - Recommended: (a) one line in place of the Result; a pointer left outside a bracket stops the build and a later Case moves it.
  - Answer: agreed, (a).
- **What happens to the case numbers in the tests**
  - Recommended: (b) comments and docstrings cleaned, strings kept as samples.
  - Answer: agreed, (b).
- **What the skeletons hold, and whether the first /hi opens a sprint**
  - Recommended: (a) skeletons that lead to a new sprint, each as its own writer writes it over the copy.
  - Answer: agreed, (a).
- **How CLAUDE.md gets the project's own description**
  - Recommended: (a) a marked block that the copy swaps.
  - Answer: agreed, (a).
- **How far the neutral rewrite goes in this Case**
  - Recommended: (a) the pages a search finds now, the rest after a check.
  - Answer: agreed, (a).
- **What checks that this is done**
  - Recommended: (a) new Estimates for each part, and the other Case drops its lines that this Case makes false.
  - Answer: agreed, (a).
- **What a draft rule takes into the copy**
  - Recommended: (a) a draft rule ships with no Estimate.
  - Answer: none of the options: a page with `core: true` may not be `draft`; a check must catch it, and the fix is to take `core` off, so the page does not ship, or to bring the page to `built`. Replaced by the question on where the guard sits.
- **Where the guard against a draft core page sits, and what happens to the six drafts now**
  - Recommended: (a) lint now, the build later.
  - Answer: `guppi ship` refuses to build `prod` while such a page stands, and `guppi lint` reminds of it too; the six are settled by the question on how they are settled.
- **Where lint reports a draft core page**
  - Recommended: (a) only where the command `ship` stands.
  - Answer: agreed, (a).
- **How the six drafts are settled, and what the sprint reads before the close**
  - Recommended: (b) `core` off `rule-skill-merge-main`, `rule-skill-pr-review` and `rule-morph`, a Case gives `entity-sprint` an Estimate, and an option of `guppi ship` writes a local copy for the sprint's install check before the close.
  - Answer: agreed, (b).
- **Change**
  - Asked: at `/pre-spec`, every Estimate that waits for a run that writes `prod` is read from a local copy that `guppi ship --allow-draft` writes, and `rule-morph` keeps `core: true`, while `rule-skill-merge-main` and `rule-skill-pr-review` still lose it.
  - Taken: Case 822.8 takes `core` off two pages and not `rule-morph`; Cases 816, 818 and 819 already read the local copy; the Case is built again under a new number.
- **Change**
  - Asked: at `/pre-spec`, `rule-guppi-config` ships with the values of this repository.
  - Taken: the reading of Case 822.7 leaves the Render of `rule-guppi-config` out.
- **Change**
  - Asked: at `/pre-spec`, for now the copy does not ship a `passed` Estimate whose `method` names a `make` target, until a later Case moves it to pytest.
  - Taken: Case 822.1 leaves such an Estimate out, judged by `MAKE_TARGET` of `guppi/lint.py`.
- **Change**
  - Asked: the findings of `/pre-spec`: a pointer outside a bracket in the pair on `rule-language`, the scope of the neutral reading, the Criteria of `estimate-lint-checks-the-statuses` and `estimate-claude-md-rendered`, the defer of `decision-case-805`, the count of the draft pages, the name of the function that tells whether the module of `ship` stands, and the moment of three readings.
  - Taken: the pair on `rule-language` takes the bracket whole; the reading of Case 822.7 holds the rules, the entities and `CLAUDE.md` to no sentence that holds only here, and for the shipped Estimates it lists such sentences for a later Case and passes when the list is made; the reading covers each shipped text but History and samples; Cases 822.5 and 822.9 replace the two Criteria; Case 822.1 takes up the defer; the context names the draft pages by kind; `ship_stands` of `.guppi/guppi/pages.py` is named; the three readings wait for the librarian's run.

## History

- 2026-10-15 created · raw/2026-10-15/0553/ledger.md#case-822
